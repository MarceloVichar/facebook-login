---
tags:
  - oportunidade
  - mercado/global
  - status/condicional
  - rodada/2
  - marketplace/atlassian
status: condicional
veredito: "CONDICIONAL (fraca); fora da carteira"
score: 23
mercado: global
rodada: "2"
fonte:
  - "[[unmet_feature_requests]]"
  - "[[Validação condicionais e novos focos]]"
---

# Merge de tickets para Jira Service Management

Voltar para [[Ranking]].

> [!info] Condicional fraca (23/35, rodada 2), fora da carteira
> Um dos dois substitutos que sobraram quando o [[App Forge de Gantt para Jira]] morreu. A dor é antiga e votada, mas o líder levou **cerca de oito anos para chegar a 759 instalações**, e dois novatos em 12 meses ficaram com 0 e 35. Leva **3–5 meses** até o primeiro pagamento.

## O que é

App Forge para JSM e Jira que funde pedidos duplicados num principal: copia comentários, anexos, participantes e observadores; liga e fecha o duplicado com resolução; avisa o cliente; e deixa comentário de auditoria. Funciona em lote pela fila e como ação de Automation ([[unmet_feature_requests]], Q6).

## Evidências

- **Dor:** JSDCLOUD-4685, **1.238 votos** e 201 comentários desde 2017; a Atlassian disse em 2022 que não pretende construir ([JSDCLOUD-4685](https://jira.atlassian.com/rest/api/2/issue/JSDCLOUD-4685?fields=status,description,comment)).
- **Concorrentes:** Merge Agent 759 instalações, 7 avaliações, US$ 260/ano para 25 usuários ([Merge Agent](https://marketplace.atlassian.com/rest/2/addons/com.codefortynine.merge-for-jira/pricing/cloud/live)); Ticket Merger grátis (3,75★, 390 instalações); Duplicate AI, Merge Assistant, IssueMerge. Nicho inteiro ≈ 1.300 sites.
- **Repasse:** viável para pessoa física brasileira com CPF, KYC e W-8BEN, mas sem tratado tributário Brasil–EUA uma classificação como royalty significaria 30% de retenção; precisa de confirmação por escrito ([Partner Agreement](https://www.atlassian.com/licensing/marketplace/publisheragreement); [IRS tratados](https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z)).

## Portas ([[Portões de aprovação]])

G1 PASS fraco · G2 **FAIL até agora** · G3 PASS · G4 **FRACO** (busca do Marketplace ordenada por instalações) · G5 PASS (2–3 semanas) · G6 PASS · G7 PASS pendente da confirmação de repasse · G8 **FAIL**: mesmo igualando as 759 instalações do líder, ~US$ 9,5 mil/mês seria o teto do líder depois de anos.

## Pontuação

| WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|
| 4 | 3 | 5 | 2 | 4 | 2 | 3 | **23/35** |

## Teste proposto pela nota (~US$ 15, 4 semanas)

Registrar o perfil de parceiro e fazer o KYC (isso também responde à dúvida do repasse); página "em breve" com preço de fundador divulgada no ticket de votos e na Atlassian Community. **Passa:** ≥ 15 opt-ins de sites JSM distintos em 30 dias **e** confirmação por escrito do repasse e da classificação da receita. **Falha:** ≤ 5 opt-ins.

## Notas de pesquisa

- [[unmet_feature_requests]], Q4 e Q6
- Relacionadas: [[Compartilhamento externo de dashboards do Jira]], [[Padrão - enxurrada de micro-SaaS feito com IA]] (Katabarwa)
