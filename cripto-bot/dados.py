"""Baixa candles históricos públicos da Binance (sem chave de API) e salva em CSV."""
import sys
import time
from pathlib import Path

import pandas as pd
import requests

URL = "https://data-api.binance.vision/api/v3/klines"
PASTA = Path(__file__).parent / "data"


def baixar(simbolo: str, intervalo: str, inicio: str, fim: str | None = None) -> pd.DataFrame:
    ini_ms = int(pd.Timestamp(inicio, tz="UTC").timestamp() * 1000)
    fim_ms = int((pd.Timestamp(fim, tz="UTC") if fim else pd.Timestamp.now("UTC")).timestamp() * 1000)
    linhas = []
    while ini_ms < fim_ms:
        r = requests.get(URL, params={"symbol": simbolo, "interval": intervalo,
                                      "startTime": ini_ms, "endTime": fim_ms, "limit": 1000}, timeout=30)
        r.raise_for_status()
        lote = r.json()
        if not lote:
            break
        linhas += lote
        ini_ms = lote[-1][0] + 1
        time.sleep(0.2)
    df = pd.DataFrame(linhas, columns=["open_time", "open", "high", "low", "close", "volume",
                                       "close_time", "qv", "n", "tb", "tq", "x"])
    df = df[["open_time", "open", "high", "low", "close", "volume"]]
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms", utc=True)
    return df.set_index("open_time").astype(float)


def carregar(simbolo: str, intervalo: str, inicio: str = "2022-01-01") -> pd.DataFrame:
    arq = PASTA / f"{simbolo}_{intervalo}.csv"
    if arq.exists():
        return pd.read_csv(arq, index_col=0, parse_dates=True)
    PASTA.mkdir(exist_ok=True)
    df = baixar(simbolo, intervalo, inicio)
    df.to_csv(arq)
    return df


if __name__ == "__main__":
    for s in sys.argv[1:] or ["BTCUSDT", "ETHUSDT"]:
        for i in ["15m", "1h", "4h"]:
            print(s, i, len(carregar(s, i)))
