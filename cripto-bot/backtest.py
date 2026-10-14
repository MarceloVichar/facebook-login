"""Backtest simples e honesto, só posição comprada (spot).

Regras anti-autoengano:
- o sinal é calculado no FECHAMENTO do candle e executado na ABERTURA do próximo (sem olhar o futuro);
- cada compra/venda paga taxa + slippage;
- parâmetros escolhidos só no período de treino; o período de teste é visto uma única vez.
"""
from dataclasses import dataclass

import numpy as np
import pandas as pd

TAXA = 0.001       # 0,1% por lado (taxa padrão spot da Binance)
SLIPPAGE = 0.0003  # 0,03% de escorregão estimado por lado
CUSTO = TAXA + SLIPPAGE


@dataclass
class Resultado:
    retorno: float
    max_dd: float
    trades: int
    acerto: float
    profit_factor: float
    exposicao: float
    curva: pd.Series

    def resumo(self) -> dict:
        return {"retorno_%": round(self.retorno * 100, 1), "max_dd_%": round(self.max_dd * 100, 1),
                "trades": self.trades, "acerto_%": round(self.acerto * 100, 1),
                "profit_factor": round(self.profit_factor, 2), "exposicao_%": round(self.exposicao * 100, 1)}


def rodar(df: pd.DataFrame, posicao_alvo: pd.Series) -> Resultado:
    """posicao_alvo: 1 = comprado, 0 = fora; decidido no fechamento de cada candle."""
    pos = posicao_alvo.shift(1).fillna(0).clip(0, 1)          # executa no candle seguinte
    ret_candle = df["open"].shift(-1) / df["open"] - 1         # retorno de abertura a abertura
    ret_candle = ret_candle.fillna(0)
    mudancas = pos.diff().abs().fillna(pos.iloc[0])
    ret = pos * ret_candle - mudancas * CUSTO
    curva = (1 + ret).cumprod()

    # trades individuais
    entradas = pos.index[(pos.diff() == 1) | ((pos.index == pos.index[0]) & (pos == 1))]
    saidas = pos.index[pos.diff() == -1]
    resultados = []
    for e in entradas:
        s = saidas[saidas > e]
        fim = s[0] if len(s) else pos.index[-1]
        trecho = ret.loc[e:fim]
        resultados.append((1 + trecho).prod() - 1)
    r = np.array(resultados)
    ganhos, perdas = r[r > 0].sum(), -r[r < 0].sum()
    return Resultado(
        retorno=curva.iloc[-1] - 1,
        max_dd=(curva / curva.cummax() - 1).min(),
        trades=len(r),
        acerto=(r > 0).mean() if len(r) else 0.0,
        profit_factor=ganhos / perdas if perdas > 0 else float("inf"),
        exposicao=pos.mean(),
        curva=curva,
    )


# ---------------- estratégias ----------------

def buy_hold(df):
    return pd.Series(1, index=df.index)


def cruzamento_medias(df, rapida=20, lenta=100):
    c = df["close"]
    return (c.ewm(span=rapida).mean() > c.ewm(span=lenta).mean()).astype(int)


def donchian(df, entrada=55, saida=20):
    """Rompimento: compra na máxima de N candles, vende na mínima de M candles (tartarugas)."""
    maxima = df["high"].rolling(entrada).max().shift(1)
    minima = df["low"].rolling(saida).min().shift(1)
    sinal = pd.Series(np.nan, index=df.index)
    sinal[df["close"] > maxima] = 1
    sinal[df["close"] < minima] = 0
    return sinal.ffill().fillna(0)


def rsi(c, n):
    d = c.diff()
    g = d.clip(lower=0).ewm(alpha=1 / n).mean()
    p = (-d.clip(upper=0)).ewm(alpha=1 / n).mean()
    return 100 - 100 / (1 + g / p)


def reversao_rsi(df, n=14, compra=30, venda=55, filtro=200):
    """Compra exagero de queda, mas só quando a tendência de fundo é de alta."""
    c = df["close"]
    r = rsi(c, n)
    tendencia = c > c.rolling(filtro).mean()
    sinal = pd.Series(np.nan, index=df.index)
    sinal[(r < compra) & tendencia] = 1
    sinal[(r > venda) | ~tendencia] = 0
    return sinal.ffill().fillna(0)


ESTRATEGIAS = {
    "buy_hold": (buy_hold, [{}]),
    "medias": (cruzamento_medias, [{"rapida": f, "lenta": l} for f in (10, 20, 50) for l in (50, 100, 200) if f < l]),
    "donchian": (donchian, [{"entrada": e, "saida": s} for e in (20, 55, 100) for s in (10, 20, 50) if s < e]),
    "reversao_rsi": (reversao_rsi, [{"n": n, "compra": b, "venda": v} for n in (2, 14) for b in (10, 20, 30) for v in (50, 70)]),
}
