---
tags:
  - oportunidade
  - mercado/global
  - status/condicional
  - promissora
status: condicional
veredito: NÃO TESTADA NA RODADA FINAL
score: 21
mercado: global
rodada: exploratória
fonte:
  - "[[us_eu_regulatory_demand]]"
  - "[[Oportunidade de produto validada 2026]]"
---

# Kit EUDR para micro-operadores da UE

Voltar para [[Ranking]].

> [!tip] Promissora, não testada (21/35, rodada exploratória)
> Explora o abismo entre o **TRACES manual e gratuito** e plataformas de **€3–4 mil/ano**. Mas **o número de compradores é desconhecido**, e o regulamento já foi adiado duas vezes.

## O que é

Um web app self-service para micro e pequenos operadores da UE:
1. **Link para o fornecedor** (PT, ES, EN, FR) registrar as parcelas no mapa ou subir arquivos KML, SHP, CSV ou do CAR.
2. **Validação e correção automática de GeoJSON** segundo as restrições do TRACES: CRS84, anéis fechados, sem autointerseção, 2D, até 10 MB, ponto único para parcelas abaixo de 4 ha.
3. **Gerador do dossiê de due diligence** (modelo de avaliação de risco, checklist de documentos de legalidade), com arquivo de 5 anos.
4. Exportação de GeoJSON e mapeamento dos campos da DDS para preenchimento manual no TRACES, com API depois, se houver.

Isca gratuita: um validador e corretor público de GeoJSON.

## Comprador

Micro e pequenos operadores da UE que colocam no mercado café, cacau, madeira, couro, borracha, soja ou palma: importadores e torrefadores de café especial que compram direto, chocolateiros artesanais, pequenos importadores de móveis ou artigos de madeira. **A contagem é desconhecida.**

## Evidências

- **Datas finais:** o Regulamento (UE) 2025/2650 fixa **30/12/2026** para operadores grandes e médios e **30/6/2027** para micro e pequenos. A revisão da Comissão de maio de 2026 não propôs novas mudanças ([EC Access2Markets](https://trade.ec.europa.eu/access-to-markets/en/news/delay-until-december-2026-and-other-developments-implementation-eudr-regulation)).
- **O Brasil é "risco padrão"**, então a due diligence completa vale para quem compra do Brasil ([Fieldfisher](https://www.fieldfisher.com/en/insights/the-eu-deforestation-regulation-european-commission-classifies-countries-as-high-low-or-standard-risk)).
- **Abismo de preço** (preços autodeclarados):
  - Grátis: [geojson.io](https://geojson.io) e o [GeoRoots Editor](https://efi.int/news/georoots-editor-accessible-secure-and-eudr-ready-geodata-editing-directly-your-browser-2026-02) do European Forest Institute.
  - TradeAware Professional: **€399/mês** ou €3.990/ano, com 50 DDS por ano ([TradeAware](https://www.live-eo.com/tradeaware-pricing)).
  - Polygon One: a partir de **~€3.000/ano** ([Polygon One](https://polygon-one.com/en/article-eudr-software-comparison)).
  - Enterprise: €10–50 mil/ano ([Qelvyn](https://qelvyn.co/en/blog/eudr/farm-plot-mapping-cost-cooperatives-eudr)).
- **Demanda indireta:** fornecedores publicam muito SEO recente sobre erros de GeoJSON e guias para PMEs ([TraceX](https://tracextech.com/geojson-file-errors/); [Coolset](https://www.coolset.com/academy/eudr-reporting-guide-for-smes)). Não há dado de volume de busca.
- **Vantagem brasileira:** a fluência em português e o conhecimento do Brasil (grande origem de café) ajudam do lado do fornecedor.

## Riscos

> [!warning] Riscos
> - **Mudança regulatória:** dois adiamentos no passado.
> - Isenções para operadores a jusante e traders reduzem o número de quem declara.
> - Ferramentas grátis e planos grátis de fornecedores.
> - **Número de compradores desconhecido.**
> - **Responsabilidade:** a due diligence continua sendo do operador, então o produto deve ser posicionado como preparação de dados.
> - Receita mais lenta, B2B e sazonal (picos antes de 30/12/2026 e 30/6/2027).

## Pontuação (rodada exploratória, [[us_eu_regulatory_demand]], C3)

| WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|
| 3 | 3 | 4 | 3 | 4 | 2 | 2 | **21/35** |

## Construção e caminho

- **Construção:** média, 2–4 semanas (bibliotecas GIS, interface de mapa, conversões de arquivo, PDF, links de fornecedor multi-tenant).
- **Primeira receita:** ~4–12 semanas.
- **Caminho até ~US$ 5 mil/mês:** ~50–100 clientes a €49–99/mês, ou preço por embarque (inferência).
- **Canal:** SEO na dor técnica ("EUDR GeoJSON error", "TRACES upload"), o validador grátis, comunidades de café especial e chocolate artesanal, LinkedIn.

## Veredito

**Condicional.** Começar pelo validador gratuito de GeoJSON como ativo de SEO e depois vender o fluxo de coleta de fornecedores e o dossiê.

## Notas de pesquisa

- [[Oportunidade de produto validada 2026]], "Ideias promissoras que não passaram pela rodada final"
- [[us_eu_regulatory_demand]], seções 3, 13 e 14
- Relacionada (armadilha): [[EUDR para pequenos produtores brasileiros]]
