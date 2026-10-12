---
tags:
  - oportunidade
  - mercado/global
  - status/condicional
  - rodada/2
status: condicional
veredito: CONDICIONAL
score: 24
mercado: Itália
rodada: "2"
teste: "[[Carteira de testes]]"
fonte:
  - "[[trustmrr_newcomers]]"
  - "[[Validação condicionais e novos focos]]"
  - "[[brazil_regulated_documents]]"
---

# Visualizador de p7m para a Itália

Voltar para [[Ranking]].

> [!tip] Condicional (24/35, rodada 2): a única prova de um novato sem audiência vencendo em 2026
> O **P7M.io**, fundado em 28/03/2026, abre os arquivos de assinatura **CAdES (.p7m)** que a Itália exige em documentos públicos e que nenhum sistema operacional abre sozinho. Fez **US$ 4.627 em 30 dias** com 261 assinaturas, apesar de ferramentas grátis. O MVP web leva uma semana; o teste custa **€ 40** ([[Carteira de testes]]).

## O que é

Um visualizador no navegador, **sem upload**, para arquivos .p7m/.p7s e faturas eletrônicas XML: extrai o PDF e mostra os dados do signatário. Um arquivo grátis, depois €3,99 por arquivo ou €12,99 por ano, espelhando o P7M.io ([[trustmrr_newcomers]], candidato A). Na rodada 3, o site do P7M.io já mostrava **€15,99/ano** ([p7m.io](https://p7m.io), visto em 12/10/2026).

## Comprador

Profissionais italianos, usuários de PEC e pequenas empresas que recebem documentos assinados da administração pública e faturas eletrônicas ([p7m.io](https://p7m.io)). O tamanho do universo não foi medido.

## Evidências

- **P7M.io:** US$ 4.627 em 30 dias, 261 assinaturas, fundado em 28/03/2026 ([TrustMRR P7M.io](https://trustmrr.com/startup/confidential-startup-70)). Alega 40 mil cliques orgânicos por mês e está **à venda por US$ 120 mil**.
- **Demanda (autocomplete it-IT):** "p7m to pdf", "p7m viewer online", "aprire file p7m" → "online", **"online gratis"**, "gratis", "aruba download" ([autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=it&gl=it&q=aprire%20file%20p7m)).
- **Romênia:** só 3 sugestões; demanda fraca.

## Concorrentes

- Ferramentas grátis dos certificadores (DiKe, ArubaSign, InfoCert), visualizadores online e o complemento P7Matic do Google Drive, que avisa não servir para verificação legal ([partitaiva.it](https://www.partitaiva.it/file-p7m/); [P7Matic](https://workspace.google.com/marketplace/app/p7matic/939303881041)).

> [!note] Corrige a regra "o governo dá de graça, então morre"
> A ferramenta gratuita só mata quando ela própria ocupa a busca comercial. Aqui ela não ocupa, e o pago vence por privacidade, conveniência e posição no Google ([[Padrão - governo entrega de graça]]). O análogo brasileiro (.p7s) morreu na rodada 3 porque o validador do ITI é gratuito e o volume de arquivos é muito menor ([[brazil_regulated_documents]], Q4).

## Portas ([[Portões de aprovação]])

| Porta | Veredito | Evidência |
|---|---|---|
| G1 | PASS fraco | P7M.io verificado; nenhum segundo produto **pago** verificado |
| G2 | PASS na prova de novato; FAIL na poluição de ferramentas grátis | — |
| G3 | PASS (ticket baixo) | €3,99–12,99 |
| G4 | CONDICIONAL | Sugestões fortes, mas "gratis" domina |
| G5 | PASS | MVP web em ≤ 7 dias (inferência) |
| G6 | PASS | — |
| G7 | PASS com ressalvas | Sem licença; **nunca prometer verificação jurídica da assinatura**; VAT B2C europeu exige merchant of record; o Paddle aceita software |
| G8 | **DUVIDOSO** | US$ 5 mil/mês ≈ 1.250 vendas avulsas ou ~385 planos anuais por mês, com o líder já nas primeiras posições orgânicas |

## Pontuação

| WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|
| 3 | 2 | 3 | 3 | 5 | 4 | 4 | **24/35** |

## Teste (resumo; detalhes em [[Carteira de testes]])

- Visualizador web (≤ 7 dias) + cinco páginas em italiano ("aprire file p7m", "p7m in pdf", "fattura elettronica p7m") + **€ 40** de Google Ads na Itália.
- **Passa:** CPC ≤ €0,40 **e** ≥ 1 conversão paga a cada 80 cliques.
- **Falha:** zero vendas com os €40, ou CPC > €0,80.
- O relatório da rodada 2 diz que o [[Feed semanal de novas práticas de saúde (NPPES)|NPPES]] é o substituto natural se o Keyword Planner mostrar CPC proibitivo na Itália.

## Veredito

**CONDICIONAL.** É a frente mais rápida de testar e a mais autocontida (sem risco de conteúdo). O risco é que o único vencedor verificado já ocupe a busca orgânica, e a economia de anúncio não foi medida.

## Notas de pesquisa

- [[trustmrr_newcomers]], "Deep validation of the top 3", candidato A
- [[Validação condicionais e novos focos]], seção "Visualizador .p7m"
- [[brazil_regulated_documents]], Q4 (o análogo brasileiro, morto)
