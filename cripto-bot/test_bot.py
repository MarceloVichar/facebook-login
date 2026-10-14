"""Testa compra, venda e stop do bot com uma corretora falsa (sem internet)."""
import pandas as pd

import bot


class CorretoraFalsa:
    minimo_usdt = 5.0

    def __init__(self):
        self.preco, self.ordens = 100.0, []

    def saldo_livre(self, ativo):
        return 1000.0

    def comprar_usdt(self, valor):
        self.ordens.append(("BUY", valor))
        qtd = valor * 0.999 / self.preco
        return {"executedQty": str(qtd), "cummulativeQuoteQty": str(valor)}

    def vender_qtd(self, qtd):
        self.ordens.append(("SELL", qtd))
        return {"executedQty": str(qtd), "cummulativeQuoteQty": str(qtd * self.preco * 0.999)}


def preparar(tmp_path, monkeypatch, precos):
    monkeypatch.setattr(bot, "ARQ_OPERACOES", tmp_path / "op.csv")
    monkeypatch.setattr(bot, "ARQ_ESTADO", tmp_path / "estado.json")
    serie = pd.Series(precos, index=pd.date_range("2026-01-01", periods=len(precos), freq="4h", tz="UTC"))
    monkeypatch.setattr(bot, "candles_fechados", lambda: pd.DataFrame({"close": serie}))


def test_compra_quando_tendencia_de_alta_e_vende_quando_vira(tmp_path, monkeypatch):
    c, estado = CorretoraFalsa(), bot.carregar_estado()
    preparar(tmp_path, monkeypatch, [100.0] * 150 + [101 + i for i in range(20)])
    c.preco = 120.0
    bot.ciclo(c, estado)
    assert c.ordens[0] == ("BUY", 15.0) and estado["qtd_ativo"] > 0 and estado["caixa_usdt"] == 0

    bot.ciclo(c, estado)                       # mesma tendência: não faz nada
    assert len(c.ordens) == 1

    preparar(tmp_path, monkeypatch, [100.0] * 150 + [99 - i for i in range(20)])
    c.preco = 80.0
    bot.ciclo(c, estado)
    assert c.ordens[1][0] == "SELL" and estado["qtd_ativo"] == 0 and estado["caixa_usdt"] > 0


def test_stop_de_perda_vende_e_desliga(tmp_path, monkeypatch):
    c, estado = CorretoraFalsa(), bot.carregar_estado()
    estado.update(caixa_usdt=0.0, qtd_ativo=0.15)   # comprado; 0,15 × 50 = 7,5 USDT < 8
    preparar(tmp_path, monkeypatch, [40.0] * 150 + [41 + i for i in range(10)])  # tendência ainda de alta
    c.preco = 50.0
    bot.ciclo(c, estado)
    assert c.ordens[0][0] == "SELL" and estado["desligado"] is True


def test_nao_compra_abaixo_do_minimo(tmp_path, monkeypatch):
    c, estado = CorretoraFalsa(), bot.carregar_estado()
    estado["caixa_usdt"] = 3.0
    preparar(tmp_path, monkeypatch, [100.0] * 150 + [101 + i for i in range(20)])
    bot.ciclo(c, estado)
    assert c.ordens == []
