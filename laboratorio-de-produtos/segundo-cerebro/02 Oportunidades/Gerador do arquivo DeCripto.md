---
tags:
  - oportunidade
  - mercado/br
  - status/condicional
  - promissora
status: condicional
veredito: NÃO TESTADA NA RODADA FINAL
score: 23
mercado: BR
rodada: exploratória
fonte:
  - "[[brazil_regulatory_demand]]"
  - "[[Oportunidade de produto validada 2026]]"
---

# Gerador do arquivo DeCripto

Voltar para [[Ranking]].

> [!tip] Promissora, não testada (23/35, rodada exploratória)
> Os compradores têm **alta renda** e os concorrentes cobram **R$ 697–2.499/ano**. Mas a base é **pequena e pode encolher**, e erros custam ao usuário **1,5% do valor da operação**, o que torna a responsabilidade alta.

## O que é

Um web app que importa o histórico de exchanges estrangeiras (CSV ou chaves de API **somente leitura**) e de carteiras, converte os valores pela PTAX e classifica cada operação nos tipos de registro oficiais. Ele sinaliza os meses acima de R$ 35 mil e exporta os arquivos "Exchange Estrangeira" e "Sem Exchange", delimitados por barra vertical, com trilha de auditoria.

## A obrigação

- **IN RFB 2.291/2025**, publicada em 14/11/2025. Desde **1/7/2026**, pessoas físicas e jurídicas declaram as operações feitas por provedores estrangeiros, DEX ou sem intermediário quando o total do mês passa de **R$ 35 mil** ([Exame](https://exame.com/invest/minhas-financas/nova-declaracao-de-cripto-nao-muda-tributacao-mas-aumenta-risco-de-multas/)).
- A declaração é mensal, até o último dia útil do mês seguinte, no Coleta Nacional do e-CAC. A primeira (operações de julho) venceu em 31/8/2026. Segundo a Blue Consult, *"ninguém monta a DeCripto dentro do Coleta Nacional. Monta-se fora, numa planilha ou num software"* ([Blue Consult](https://blueconsult.com.br/coleta-nacional-decripto-tela-a-tela/)).
- **Multas** (art. 13): R$ 100/mês por atraso para pessoa física; **1,5% do valor da operação** por informação incorreta ou omitida (3% para empresas, mínimo de R$ 100) ([Blue Consult](https://blueconsult.com.br/decripto-nova-declaracao-criptoativos/)).

## Comprador

Pessoas físicas que movimentam mais de R$ 35 mil/mês fora das exchanges nacionais. A nota estimou **~500–12.000 declarantes em dia por mês**, dividindo o volume mensal declarado em 2025 via exchanges estrangeiras (R$ 94–584 milhões) por R$ 50–200 mil por declarante. Provavelmente há um grande grupo que não declara.

## Concorrentes

| Ferramenta | Preço | Observação |
|---|---|---|
| Blue Cripto | R$ 697 por ano fiscal (plano Completo) | A Blue Consult diz ter processado mais de 10 mil declarações (autodeclarado) e faz upsell de consultoria |
| Fiscal Cripto | R$ 2.499 por 1.000 operações/mês | Caro |
| Declare Cripto | Só sob cotação | Preço opaco |
| Koinly, CoinTracking | US$ 49–899/ano | Não geram a DeCripto, segundo a Blue (que é concorrente) |

Fonte: [Blue Consult](https://blueconsult.com.br/melhor-programa-imposto-criptomoedas/).

## Demanda

Autocomplete: "decripto receita federal", "declarar binance 2026". Os dados de Trends para "decripto" não foram obtidos (limite de requisições).

## Riscos

> [!warning] Riscos
> - **Mercado pequeno e que pode encolher:** se as exchanges estrangeiras passarem a reportar como provedoras obrigadas, a obrigação do usuário se reduz a DEX, P2P e autocustódia.
> - **Responsabilidade:** um aviso legal sozinho **não basta**, porque um valor errado custa 1,5% da operação ao usuário. Mitigação: o usuário revisa e transmite o arquivo, a metodologia é publicada, não há garantia de conformidade, o produto nunca declara em nome do usuário, e quem usa muito DeFi deve passar por um contador.
> - Complexidade de DeFi; formatos de CSV das exchanges mudam; segurança das chaves de API (sempre somente leitura).
> - Para R$ 27 mil/mês seriam ~470 assinantes anuais a R$ 697 ou ~550 mensais a R$ 49, uma fatia grande da base estimada.

## Pontuação (rodada exploratória, [[brazil_regulatory_demand]], C2)

| WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|
| 4 | 3 | 5 | 3 | 3 | 3 | 2 | **23/35** |

## Construção e canal

- **Construção:** média; MVP de 2–4 semanas com 3 exchanges, CSV genérico e entrada manual. A nota assume que a PTAX do BCB pode ser obtida programaticamente, sem ter verificado.
- **Canal:** SEO por exchange e carteira ("decripto binance", "decripto bybit", "decripto okx", "decripto metamask"), YouTube, grupos públicos de cripto e anúncios curtos nos últimos dez dias de cada mês.
- **Validação sugerida pela nota:** landing page com lista de espera e um conversor para uma única exchange primeiro.

## Veredito

**Condicional.** É uma aposta de receita por usuário mais alta, que precisa de validação.

## Notas de pesquisa

- [[Oportunidade de produto validada 2026]], "Ideias promissoras que não passaram pela rodada final"
- [[brazil_regulatory_demand]], seções 13, 15 e 16 (candidato C2)
