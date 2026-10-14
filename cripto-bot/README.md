# cripto-bot — laboratório de trading automatizado

Experimento pessoal com dinheiro de brincadeira (orçamento de perda: R$ 50–100).
Ativos: BTC/USDT e ETH/USDT na Binance (spot, só posição comprada).

## Como rodar

```bash
pip install -r requirements.txt
python dados.py          # baixa o histórico público (sem chave de API) para data/
python experimento.py    # treino 2022–2024, teste 2025 em diante -> resultados.csv
```

## Regras do backtest
- Sinal no fechamento do candle, execução na abertura do próximo (sem olhar o futuro).
- Custo de 0,13% por lado (0,1% de taxa + 0,03% de slippage).
- Parâmetros escolhidos **só** no treino (2022–2024); o teste (2025–out/2026) é visto uma vez.

## Resultado da 1ª rodada (teste fora da amostra, 2025-01 → 2026-10)

| Ativo | Tempo | Estratégia | Retorno | Máx. queda | Trades |
|---|---|---|---|---|---|
| BTC | — | buy & hold | −11,5% | −53% | 1 |
| BTC | 15m | médias / donchian | −50% / −66% | −62% / −73% | 191 / 324 |
| BTC | 1h | médias / donchian | −24% / −26% | −43% / −45% | 50 / 56 |
| BTC | 4h | **médias 10/100** | **+10,5%** | −31% | 33 |
| ETH | — | buy & hold | −25,6% | −68% | 1 |
| ETH | 15m | médias / donchian | −52% / −53% | −60% / −62% | 203 / 293 |
| ETH | 4h | **médias 10/100** | **+27,2%** | −38% | 36 |

### Lições
1. **Day trade de verdade (15m) perde muito**: centenas de trades × 0,26% de custo ida e volta consomem tudo.
2. Quanto maior o tempo gráfico, menos custo e mais chance de sobrar algo.
3. A única que ficou positiva nos dois ativos fora da amostra: **cruzamento de médias exponenciais 10/100 no 4h**
   (trend following; acerta só ~27% das vezes, ganha nas poucas tendências grandes).
4. ~35 trades ainda é pouco para ter certeza estatística; pode ter sido sorte. Próximo passo é paper trading.

## O bot autônomo (`bot.py`)

Regra, aplicada sozinha a cada candle de 4h (00h, 04h, 08h… UTC):
- média exponencial de 10 candles **acima** da de 100 → fica **comprado** em BTC;
- **abaixo** → fica **fora**, em USDT.

Proteções no código:
- usa no máximo `ORCAMENTO_USDT` (15 USDT) e só mexe no que ele mesmo comprou;
- se o patrimônio dele cair abaixo de `PARAR_ABAIXO_DE_USDT` (8 USDT), vende tudo e se desliga;
- criar um arquivo `PARAR` na pasta desliga o bot no próximo ciclo;
- conta real só com `--real` e digitando `SIM`.

Tudo fica registrado em `operacoes.csv` (cada decisão) e `bot.log`.

### Rodando no Windows
1. Instale o Python 3.12+ em python.org (marque "Add Python to PATH").
2. Baixe esta pasta e, no terminal dentro dela: `pip install -r requirements.txt`
3. Teste sem ordens: `python bot.py --simular --uma-vez`
4. Crie as chaves em https://testnet.binance.vision (login com GitHub → Generate HMAC_SHA256 Key),
   copie `.env.exemplo` para `.env` e cole as chaves.
5. Rode: `python bot.py` e deixe a janela aberta (e o PC sem hibernar).

Testes: `python -m pytest test_bot.py`

## Próximos passos
- [x] Bot em modo **testnet** (dinheiro falso) rodando a estratégia 4h, com log de cada decisão.
- [x] Limites de risco no código: valor máximo por ordem, stop de perda total, botão de desligar.
- [ ] Rodar no PC Windows com as chaves da testnet.
- [ ] 4–8 semanas de testnet; comparar com o backtest.
- [ ] Só então: conta real com R$ 50–100.
