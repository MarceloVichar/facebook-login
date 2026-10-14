"""Escolhe parâmetros no treino (2022–2024) e mede no teste (2025 em diante)."""
import pandas as pd

from backtest import ESTRATEGIAS, rodar
from dados import carregar

FIM_TREINO = "2024-12-31"
INICIO_TESTE = "2025-01-01"


def avaliar(simbolo, intervalo):
    df = carregar(simbolo, intervalo)
    linhas = []
    for nome, (func, grade) in ESTRATEGIAS.items():
        sinais = {str(p): func(df, **p) for p in grade}
        treino = {k: rodar(df[:FIM_TREINO], s[:FIM_TREINO]) for k, s in sinais.items()}
        melhor = max(treino, key=lambda k: treino[k].retorno / max(-treino[k].max_dd, 0.05))
        teste = rodar(df[INICIO_TESTE:], sinais[melhor][INICIO_TESTE:])
        linhas.append({"ativo": simbolo, "tempo": intervalo, "estrategia": nome, "params": melhor,
                       "treino_ret_%": round(treino[melhor].retorno * 100, 1),
                       **{f"teste_{k}": v for k, v in teste.resumo().items()}})
    return linhas


if __name__ == "__main__":
    pd.set_option("display.width", 250, "display.max_columns", 20)
    todas = []
    for s in ("BTCUSDT", "ETHUSDT"):
        for i in ("15m", "1h", "4h"):
            todas += avaliar(s, i)
    tabela = pd.DataFrame(todas)
    print(tabela.to_string(index=False))
    tabela.to_csv("resultados.csv", index=False)
