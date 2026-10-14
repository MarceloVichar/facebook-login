"""Bot autônomo: cruzamento de médias exponenciais (10/100) em candles de 4h, só comprado.

Como ele decide, sozinho, a cada 4 horas:
  - média rápida (10) ACIMA da lenta (100)  -> quer estar COMPRADO
  - média rápida (10) ABAIXO da lenta (100) -> quer estar FORA (em USDT)
Se a posição atual for diferente da desejada, ele manda a ordem a mercado.

Os preços para decidir vêm sempre do mercado real (dados públicos).
As ordens vão para a testnet (dinheiro falso) a menos que você rode com --real.

Uso:
  python bot.py --simular      # só mostra o que faria, não manda ordem nenhuma
  python bot.py                # testnet (precisa de BINANCE_KEY e BINANCE_SECRET no .env)
  python bot.py --real         # conta real (só depois de semanas de testnet!)

Para parar: crie um arquivo chamado PARAR na pasta do bot (ou Ctrl+C).
"""
import argparse
import csv
import hashlib
import hmac
import json
import logging
import time
from datetime import datetime, timezone
from decimal import ROUND_DOWN, Decimal
from pathlib import Path
from urllib.parse import urlencode

import pandas as pd
import requests

# ---------------- configuração ----------------
SIMBOLO = "BTCUSDT"
ATIVO = "BTC"
INTERVALO = "4h"
MEDIA_RAPIDA = 10
MEDIA_LENTA = 100
ORCAMENTO_USDT = 15.0        # quanto o bot pode usar no total (~R$ 85)
PARAR_ABAIXO_DE_USDT = 8.0   # se o patrimônio do bot cair abaixo disso, vende tudo e desliga

DADOS_PUBLICOS = "https://data-api.binance.vision"
URL_TESTNET = "https://testnet.binance.vision"
URL_REAL = "https://api.binance.com"

PASTA = Path(__file__).parent
ARQ_ESTADO = PASTA / "estado.json"
ARQ_OPERACOES = PASTA / "operacoes.csv"
ARQ_PARAR = PASTA / "PARAR"

log = logging.getLogger("bot")


# ---------------- decisão (lógica pura, testável) ----------------

def candles_fechados(simbolo: str = SIMBOLO, intervalo: str = INTERVALO, limite: int = 1000) -> pd.DataFrame:
    r = requests.get(f"{DADOS_PUBLICOS}/api/v3/klines",
                     params={"symbol": simbolo, "interval": intervalo, "limit": limite}, timeout=30)
    r.raise_for_status()
    df = pd.DataFrame(r.json()).iloc[:, :7]
    df.columns = ["open_time", "open", "high", "low", "close", "volume", "close_time"]
    agora_ms = time.time() * 1000
    df = df[df["close_time"] < agora_ms]          # descarta o candle que ainda está aberto
    df.index = pd.to_datetime(df["open_time"], unit="ms", utc=True)
    return df[["open", "high", "low", "close", "volume"]].astype(float)


def decidir(fechamentos: pd.Series) -> dict:
    rapida = fechamentos.ewm(span=MEDIA_RAPIDA).mean().iloc[-1]
    lenta = fechamentos.ewm(span=MEDIA_LENTA).mean().iloc[-1]
    return {"candle": str(fechamentos.index[-1]), "preco": float(fechamentos.iloc[-1]),
            "media_rapida": round(float(rapida), 2), "media_lenta": round(float(lenta), 2),
            "quer_comprado": bool(rapida > lenta)}


# ---------------- corretora ----------------

class Binance:
    def __init__(self, base: str, chave: str, segredo: str):
        self.base, self.chave, self.segredo = base, chave, segredo.encode()
        self.s = requests.Session()
        self.s.headers["X-MBX-APIKEY"] = chave
        servidor = self.s.get(f"{base}/api/v3/time", timeout=15).json()["serverTime"]
        self.desvio_ms = servidor - int(time.time() * 1000)
        filtros = {f["filterType"]: f for f in
                   self.s.get(f"{base}/api/v3/exchangeInfo", params={"symbol": SIMBOLO}, timeout=15)
                   .json()["symbols"][0]["filters"]}
        self.passo = Decimal(filtros["LOT_SIZE"]["stepSize"])
        nocional = filtros.get("NOTIONAL") or filtros.get("MIN_NOTIONAL") or {}
        self.minimo_usdt = float(nocional.get("minNotional", 5))

    def _assinado(self, metodo: str, caminho: str, **params):
        params.update(timestamp=int(time.time() * 1000) + self.desvio_ms, recvWindow=10000)
        consulta = urlencode(params)
        assinatura = hmac.new(self.segredo, consulta.encode(), hashlib.sha256).hexdigest()
        r = self.s.request(metodo, f"{self.base}{caminho}?{consulta}&signature={assinatura}", timeout=30)
        if r.status_code != 200:
            raise RuntimeError(f"Binance {r.status_code}: {r.text}")
        return r.json()

    def saldo_livre(self, ativo: str) -> float:
        for b in self._assinado("GET", "/api/v3/account")["balances"]:
            if b["asset"] == ativo:
                return float(b["free"])
        return 0.0

    def comprar_usdt(self, valor_usdt: float) -> dict:
        return self._assinado("POST", "/api/v3/order", symbol=SIMBOLO, side="BUY", type="MARKET",
                              quoteOrderQty=f"{valor_usdt:.2f}")

    def vender_qtd(self, qtd: float) -> dict:
        q = (Decimal(str(qtd)) / self.passo).to_integral_value(ROUND_DOWN) * self.passo
        return self._assinado("POST", "/api/v3/order", symbol=SIMBOLO, side="SELL", type="MARKET",
                              quantity=format(q.normalize(), "f"))


# ---------------- estado e registro ----------------
# O bot só mexe no que ele mesmo comprou: guarda o próprio caixa e a própria quantidade.

def carregar_estado() -> dict:
    if ARQ_ESTADO.exists():
        return json.loads(ARQ_ESTADO.read_text())
    return {"caixa_usdt": ORCAMENTO_USDT, "qtd_ativo": 0.0, "desligado": False}


def salvar_estado(estado: dict) -> None:
    ARQ_ESTADO.write_text(json.dumps(estado, indent=2))


def registrar(acao: str, decisao: dict, estado: dict, ordem: dict | None = None) -> None:
    novo = not ARQ_OPERACOES.exists()
    with ARQ_OPERACOES.open("a", newline="") as f:
        w = csv.writer(f)
        if novo:
            w.writerow(["quando", "acao", "candle", "preco", "media_rapida", "media_lenta",
                        "qtd_executada", "usdt_executado", "caixa_usdt", "qtd_ativo"])
        w.writerow([datetime.now(timezone.utc).isoformat(timespec="seconds"), acao, decisao["candle"],
                    decisao["preco"], decisao["media_rapida"], decisao["media_lenta"],
                    ordem and ordem.get("executedQty"), ordem and ordem.get("cummulativeQuoteQty"),
                    round(estado["caixa_usdt"], 4), estado["qtd_ativo"]])


# ---------------- ciclo ----------------

def ciclo(corretora: Binance | None, estado: dict) -> None:
    decisao = decidir(candles_fechados()["close"])
    preco = decisao["preco"]
    patrimonio = estado["caixa_usdt"] + estado["qtd_ativo"] * preco
    comprado = estado["qtd_ativo"] * preco >= 1.0
    log.info("candle %s | preço %.2f | média10 %.2f | média100 %.2f | quer %s | está %s | patrimônio %.2f USDT",
             decisao["candle"], preco, decisao["media_rapida"], decisao["media_lenta"],
             "COMPRADO" if decisao["quer_comprado"] else "FORA",
             "COMPRADO" if comprado else "FORA", patrimonio)

    stop_total = patrimonio < PARAR_ABAIXO_DE_USDT
    if stop_total:
        log.warning("Patrimônio abaixo de %.2f USDT: vendendo tudo e desligando.", PARAR_ABAIXO_DE_USDT)

    if comprado and (stop_total or not decisao["quer_comprado"]):
        acao = "VENDA"
        if corretora:
            qtd = min(estado["qtd_ativo"], corretora.saldo_livre(ATIVO))
            ordem = corretora.vender_qtd(qtd)
            estado["qtd_ativo"] = max(0.0, estado["qtd_ativo"] - float(ordem["executedQty"]))
            estado["caixa_usdt"] += float(ordem["cummulativeQuoteQty"])
        else:
            ordem = None
            estado["caixa_usdt"] += estado["qtd_ativo"] * preco * (1 - 0.0013)
            estado["qtd_ativo"] = 0.0
        registrar(acao, decisao, estado, ordem)
        log.info("%s feita. Caixa agora: %.2f USDT", acao, estado["caixa_usdt"])

    elif not comprado and decisao["quer_comprado"] and not stop_total:
        valor = min(estado["caixa_usdt"], ORCAMENTO_USDT)
        minimo = corretora.minimo_usdt if corretora else 5.0
        if valor < minimo:
            log.warning("Caixa %.2f USDT abaixo do mínimo da corretora (%.2f); não compra.", valor, minimo)
        else:
            if corretora:
                valor = min(valor, corretora.saldo_livre("USDT"))
                ordem = corretora.comprar_usdt(valor)
                estado["qtd_ativo"] += float(ordem["executedQty"])
                estado["caixa_usdt"] -= float(ordem["cummulativeQuoteQty"])
            else:
                ordem = None
                estado["qtd_ativo"] += valor * (1 - 0.0013) / preco
                estado["caixa_usdt"] -= valor
            registrar("COMPRA", decisao, estado, ordem)
            log.info("COMPRA feita. Quantidade agora: %.8f %s", estado["qtd_ativo"], ATIVO)
    else:
        registrar("MANTEM", decisao, estado)

    if stop_total:
        estado["desligado"] = True
    salvar_estado(estado)


def segundos_ate_proximo_candle(horas: int = 4, folga: int = 30) -> float:
    agora = time.time()
    periodo = horas * 3600
    return (agora // periodo + 1) * periodo + folga - agora


def ler_env() -> dict:
    arq = PASTA / ".env"
    valores = {}
    if arq.exists():
        for linha in arq.read_text().splitlines():
            if "=" in linha and not linha.strip().startswith("#"):
                k, v = linha.split("=", 1)
                valores[k.strip()] = v.strip()
    return valores


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--simular", action="store_true", help="não manda ordens, só simula")
    p.add_argument("--real", action="store_true", help="usa a conta REAL (cuidado)")
    p.add_argument("--uma-vez", action="store_true", help="roda um ciclo e sai")
    args = p.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                        handlers=[logging.StreamHandler(), logging.FileHandler(PASTA / "bot.log", encoding="utf-8")])

    corretora = None
    if not args.simular:
        env = ler_env()
        if args.real:
            if input("Conta REAL. Digite SIM para continuar: ").strip() != "SIM":
                return
            corretora = Binance(URL_REAL, env["BINANCE_KEY"], env["BINANCE_SECRET"])
        else:
            corretora = Binance(URL_TESTNET, env["BINANCE_KEY"], env["BINANCE_SECRET"])
    log.info("Modo: %s | %s %s | médias %d/%d | orçamento %.2f USDT",
             "SIMULAÇÃO" if args.simular else ("REAL" if args.real else "TESTNET"),
             SIMBOLO, INTERVALO, MEDIA_RAPIDA, MEDIA_LENTA, ORCAMENTO_USDT)

    estado = carregar_estado()
    while True:
        if ARQ_PARAR.exists() or estado.get("desligado"):
            log.info("Bot desligado (arquivo PARAR ou stop de perda). Saindo.")
            return
        try:
            ciclo(corretora, estado)
        except Exception:
            log.exception("Erro no ciclo; tento de novo no próximo candle.")
        if args.uma_vez:
            return
        espera = segundos_ate_proximo_candle()
        log.info("Dormindo %.0f min até o próximo candle de 4h.", espera / 60)
        time.sleep(espera)


if __name__ == "__main__":
    main()
