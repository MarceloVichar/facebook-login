---
tags:
  - oportunidade
  - mercado/global
  - status/alternativa
  - finalista
  - marketplace/atlassian
status: alternativa
veredito: CONDICIONAL (só nicho estreito)
score: 22
score_inicial: 26
mercado: global
rodada: final
fonte:
  - "[[marketplace_gaps]]"
  - "[[finalists_global_verification]]"
  - "[[Oportunidade de produto validada 2026]]"
---

# App Forge de Gantt para Jira

Voltar para [[Ranking]].

> [!tip] Alternativa nº 2 (CONDICIONAL, só nicho estreito, 22/35)
> Tem comprador em dólar, cobrança feita pela plataforma e 100% da receita Forge até US$ 1 milhão. Mas o mercado está lotado de incumbentes que **já migraram para Forge**, e o início é frio. É a alternativa com o **horizonte mais longo** das três.

## O que é

A ideia original ([[marketplace_gaps]], C1) era um Gantt nativo em Forge para issues do Jira, com dependências (issue links), linhas de base e arrastar para reagendar, vendido pela cobrança da Atlassian. A ideia era substituir apps Gantt em Connect, que entra em fim de suporte no 4º trimestre de 2026.

Depois da verificação, a versão que sobrevive é uma **cunha estreita, abaixo de US$ 1/usuário/mês**, que o Timeline nativo e as grandes suítes não cobrem bem. Exemplos (inferência, demanda não validada):
- exportar o Gantt para PDF ou PowerPoint;
- acompanhar linha de base e variação sobre o Timeline nativo;
- um gadget leve de Gantt para dashboard.

## Comprador

Times de Jira Cloud. A Atlassian tem 300 mil+ clientes ([Atlassian](https://www.atlassian.com/company)) e 6.623 apps cloud no Marketplace. Cobrança por assento, em dólar, B2B.

## Evidências

**Disposição a pagar (preços anuais na API do Marketplace)**

| App | 10 usuários | 50 usuários | 100 usuários |
|---|---|---|---|
| BigGantt | US$ 0 | US$ 1.045 | US$ 2.090 |
| WBS Gantt | US$ 0 | US$ 660 | US$ 1.320 |
| Structure Gantt | US$ 100 | US$ 730 | US$ 1.460 |
| GanttTable | US$ 0 | US$ 750 | US$ 1.500 |
| Gantt Cloud | US$ 25 | US$ 225 | US$ 450 |

**Lotação (API do Marketplace, 12/10/2026)**
- "gantt": 69 resultados; "timeline": 237; "roadmap": 122 ([API](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=gantt&limit=50&withVersion=true)).
- Os maiores **já estão no Forge, com versões de 2026**: BigGantt (Appfire, 5.548 instalações, 3,46★, versão de 17/8/2026), Portfolio by HeroCoders (4.993, 4,45★, 3/10/2026), Swanly (1.418, 4/5/2026) e GanttTable (1.300, 28/7/2026).
- A maioria é **grátis até 10 usuários**. O Timeline nativo (todos os planos) e o Plans (Premium/Enterprise) cobrem o básico.

**A tese "os apps Connect vão morrer" é fraca**
- Na fase 2, os apps Connect podem continuar recebendo atualizações se adotarem o manifesto Forge ([Atlassian blog](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps)). O cliente não é forçado a trocar de fornecedor.

**Economia e repasse** ([Atlassian billing](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/))
- Desde 1/1/2026, o parceiro fica com **100% da receita Forge até US$ 1 milhão vitalício**.
- O repasse só começa após **US$ 500 de lucro** e é pago 30–60 dias depois.
- **Não dá para passar um app de grátis a pago depois do lançamento:** ele precisa nascer pago.
- **Precedente brasileiro:** o desenvolvedor Victor Torres (Belo Horizonte) lista 3 apps "Paid via Atlassian" com 0–1 instalações cada, lançados entre maio e agosto de 2026 ([vendor](https://marketplace.atlassian.com/vendors/683198338/victor-torres)). A Fator Tec LTDA tem um app pago com 2 instalações.

## Riscos

> [!warning] Riscos
> - **Início frio:** a busca do Marketplace ordena por instalações e avaliações. Os recém-chegados observados, inclusive o brasileiro, estão com 0–7 instalações meses depois do lançamento.
> - **Demora até a primeira receita:** grátis até 10 usuários, limite de US$ 500 e mais 30–60 dias.
> - **Paridade leva meses:** arrastar para reagendar, linha de base, caminho crítico e desempenho em instâncias grandes dentro dos limites do Forge.
> - **Repasse a pessoa física brasileira não confirmado:** a Atlassian não publica lista de países. É preciso confirmar com o time de parceiros.
> - **Segurança:** a participação em bug bounty é exigida em alguns níveis do programa de parceiros (Platinum: todos os apps cloud pagos), e os prêmios são pagos pelo parceiro.

## Pontuação

| Rodada | WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|---|
| Final ([[finalists_global_verification]]) | 5 | 2 | 5 | 3 | 2 | 2 | 3 | **22/35** |
| Exploratória ([[marketplace_gaps]]) | 5 | 3 | 5 | 4 | 3 | 3 | 3 | 26/35 |

Tem a maior nota bruta da rodada final, mas fica em terceiro de propósito. A nota vem do preço por assento, enquanto os estreantes observados não decolaram.

## Veredito

**CONDICIONAL, só como nicho estreito.** Não construir um Gantt genérico. Seguir só com uma cunha abaixo de US$ 1/usuário/mês, **depois de a Atlassian confirmar onboarding e repasse para pessoa física brasileira**, e lançar como "Paid via Atlassian" desde o primeiro dia. A nota exploratória estimou US$ 5 mil/mês com ~100–200 sites pagantes a US$ 300–600/ano (inferência).

## Notas de pesquisa

- [[Oportunidade de produto validada 2026]], seção "Jira só serve como nicho estreito e lento"
- [[finalists_global_verification]], Q3 e Q6
- [[marketplace_gaps]], C1 e seções 8–10
- Relacionadas: [[Macros docs-as-code para Confluence]] (segundo app Forge possível), [[Padrão - saturação]]
