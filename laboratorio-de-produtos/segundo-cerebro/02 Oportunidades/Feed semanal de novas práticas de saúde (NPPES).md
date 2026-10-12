---
tags:
  - oportunidade
  - mercado/eua
  - status/condicional
  - rodada/2
status: condicional
veredito: "CONDICIONAL (G1 sem prova de pagamento)"
score: 23
mercado: EUA
rodada: "2"
teste: "[[Carteira de testes]]"
fonte:
  - "[[public_records_data]]"
  - "[[Validação condicionais e novos focos]]"
---

# Feed semanal de novas práticas de saúde (NPPES)

Voltar para [[Ranking]].

> [!info] Condicional (23/35, rodada 2): o substituto do FMCSA
> Quando a [[Feed de transportadoras recém-registradas (FMCSA)|lista da FMCSA]] morreu por saturação, a nota de dados públicos apontou o NPPES como o melhor teste de reposição: o arquivo semanal é pequeno e o teste cabe no orçamento. Mas **ninguém foi visto pagando** por esse feed. O relatório da rodada 2 o deixa fora da carteira e o indica como **substituto do [[Visualizador de p7m para a Itália|.p7m]]** se o CPC na Itália for proibitivo.

## O que é

Toda segunda-feira, as novas organizações de saúde (Type-2) e, opcionalmente, os novos profissionais (Type-1), filtrados por estado e especialidade, com telefone e endereço, em CSV e webhook para CRM ([[public_records_data]], C2).

## Comprador

Empresas de faturamento médico (medical billing), credenciamento e RCM, corretores de seguro de responsabilidade e revendedores de prontuário. A contagem de compradores é uma lacuna.

## Evidências

- **Oferta de dados:** 2.763 novas organizações e 10.036 profissionais numa semana, num zip de 6,7 MB ([NPPES weekly](https://download.cms.gov/nppes/NPPES_Data_Dissemination_100526_101126_Weekly_V2.zip)). O dado é público e gratuito ([CMS](https://www.cms.gov/regulations-and-guidance/administrative-simplification/nationalprovidentstand/datadissemination)).
- **Demanda:** "medical billing leads", "buy medical billing leads", "medical billing leads list" ([autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=medical%20billing%20leads)).
- **Concorrentes:** edições semanais no Apify a US$ 9 por estado ou US$ 29 nacional ([Apify](https://apify.com/fixmyerrorcode/newly-enumerated-us-healthcare-organizations-weekly-npi-feed)); 213 atores de NPI com no máximo 130 usuários cada; **nenhum SaaS dedicado** e **nenhuma receita verificada**.

## Portas ([[Portões de aprovação]])

G1 **NÃO PROVADO** · G2 PASS · G3 PASS · G4 PARCIAL · G5 PASS (~1 semana) · G6 PASS · G7 PASS, mas o merchant of record precisa aceitar listas (cláusula de telemarketing do Paddle; [[Padrão - pagamento e CNPJ bloqueiam rotas]]) · G8 plausível: 51–102 assinaturas a US$ 49–99.

## Pontuação

| WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|
| 2 | 4 | 4 | 3 | 5 | 2 | 3 | **23/35** |

## Teste proposto pela nota

- Página com amostra grátis das novas organizações da semana anterior num estado, plano Pro a US$ 49/mês e **US$ 50** de Google Ads em "buy medical billing leads", "medical billing leads list" e "credentialing leads".
- **Passa:** ≥ 2 assinaturas pagas, ou ≥ 15 downloads de amostra a menos de US$ 4 por lead, em 14 dias.
- **Falha:** zero pagos e < 5 downloads.

## Riscos

Registro não significa consultório funcionando (o próprio vendedor do Apify avisa); não há e-mails nos dados; churn alto de produtos de leads.

## Veredito

**CONDICIONAL.** A nota alerta: mesmo as condicionais de dados públicos falham em G1 com a evidência atual. O teste de US$ 50 é a porta, não a construção.

## Notas de pesquisa

- [[public_records_data]], Key questions 3 e 4 (C2)
- [[Validação condicionais e novos focos]], seção "Os demais condicionais"
