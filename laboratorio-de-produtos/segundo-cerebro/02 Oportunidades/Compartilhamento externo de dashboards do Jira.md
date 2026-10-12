---
tags:
  - oportunidade
  - mercado/global
  - status/condicional
  - rodada/2
  - marketplace/atlassian
status: condicional
veredito: "CONDICIONAL (fraca); fora da carteira"
score: 21
mercado: global
rodada: "2"
fonte:
  - "[[unmet_feature_requests]]"
  - "[[Validação condicionais e novos focos]]"
---

# Compartilhamento externo de dashboards do Jira

Voltar para [[Ranking]].

> [!info] Condicional fraca (21/35, rodada 2), fora da carteira
> Links públicos ou com senha para dashboards, filtros e linhas do tempo do Jira, para clientes e executivos sem licença. Tem o **maior preço por assento** visto na rodada, mas há risco técnico no Forge e um concorrente grátis crescendo rápido.

## O que é

Links somente leitura com expiração, bloqueio por IP ou e-mail e um retrato estático em HTML/PNG em vez de dados ao vivo ([[unmet_feature_requests]], Q6).

## Evidências

- **Dor:** JRACLOUD-68499 (548 votos) e JRACLOUD-87846 (440), desde 2018–2019; autocomplete com "share jira dashboard externally" e "with customer".
- **Concorrentes:** External Share, 1.057 instalações, 4,71★, **US$ 687,50/ano para 25 usuários**; Laya Board grátis, 317 instalações em 3 meses; miniOrange 135; Apportunity 69.

## Portas ([[Portões de aprovação]])

G1 PASS · G2 fraco (concorrente grátis de um vendedor com portfólio) · G3 PASS · G4 fraco · G5 **RISCO**: servir páginas a usuários anônimos exige web triggers do Forge ou hospedagem externa, não verificado · G6 PASS · G7 pendente da confirmação de repasse (ver [[Merge de tickets para Jira Service Management]]) · G8 ~90–100 sites pagantes a ~US$ 600/ano chegariam a US$ 5 mil/mês, mas G2 não está provado.

## Pontuação

| WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|
| 5 | 3 | 5 | 2 | 2 | 2 | 2 | **21/35** |

## Teste proposto pela nota

O mesmo teste de página "em breve" do merge, mais confirmar em developer.atlassian.com que os web triggers do Forge servem HTML sem autenticação e mantêm o selo "Runs on Atlassian". **Passa:** ≥ 10 opt-ins e caminho viável no Forge; senão, KILL.

## Notas de pesquisa

- [[unmet_feature_requests]], Q6 (Top 2)
- Relacionada: [[App Forge de Gantt para Jira]]
