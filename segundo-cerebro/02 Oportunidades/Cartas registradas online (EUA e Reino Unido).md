---
tags:
  - oportunidade
  - mercado/global
  - status/alternativa
  - finalista
status: alternativa
veredito: CONDICIONAL
score: 21
score_inicial: 28
mercado: global
rodada: final
fonte:
  - "[[verified_revenue_niches]]"
  - "[[finalists_global_verification]]"
  - "[[Oportunidade de produto validada 2026]]"
---

# Cartas registradas online (EUA e Reino Unido)

Voltar para [[Ranking]].

> [!tip] Alternativa nº 1 (CONDICIONAL, 21/35)
> Nenhuma outra candidata tem prova tão boa de que **um estreante sem audiência consegue faturar**. Mas a margem é fina, o mercado é lotado e há bloqueios **contratuais e de pagamento** que dependem de terceiros. O ticket com a Lob custa zero e pode ser aberto hoje, em paralelo aos laudos.

## O que é

O cliente faz upload de um PDF ou digita a carta. O serviço imprime e envia (First-Class ou Certified Mail com rastreio) por uma API de impressão e postagem, com modelos por caso de uso.

## Comprador

Pessoas físicas e pequenas empresas nos EUA e no Reino Unido: locadores, pessoas em disputa e pequenos escritórios. O número de compradores não foi quantificado. A dor: *"sending a physical letter is still surprisingly difficult"* ([TrustMRR Send Letters Online](https://trustmrr.com/startup/send-letters-online-uk)); o usuário quer evitar a impressora e a agência dos correios ([TrustMRR PostalForm](https://trustmrr.com/startup/postal-form)).

## Evidências (receita verificada via Stripe no TrustMRR)

| Produto | Origem | Receita | Observação |
|---|---|---|---|
| **PostalForm** | EUA, fundada em 1/10/2024 | US$ 20.404 no total; **US$ 6.380 em 30 dias** | Fundador com **116 seguidores** no X. US$ 3,40 a partir de; US$ 11,80 a carta registrada ([TrustMRR](https://trustmrr.com/startup/postal-form); [site](https://postalform.com/)) |
| **Send Letters Online** | Reino Unido, fundada em 14/5/2026 | US$ 21.192 no total; **US$ 4.315 em 30 dias** | Operada pela **Spark Labs FZ-LLC, dos Emirados Árabes**, o que prova que dá para operar de fora. Domain rating 5, ~80 páginas de SEO (HMRC, DVLA, Section 8) ([TrustMRR](https://trustmrr.com/startup/send-letters-online-uk); [site](https://sendlettersonline.co.uk/)) |
| Postage.to | Mundial, 2025 | US$ 2.888 no total | À venda por US$ 9.500: nem todo estreante vence ([TrustMRR](https://trustmrr.com/startup/postage-to)) |

> [!note] Sinal contrário
> O Trustpilot da Send Letters Online mostra nota 3,2 com uma única avaliação, que reclama de entrega em 8–10 dias (resumo de busca).

## Economia unitária

Conta da nota de verificação, a partir de preços verificados:
- **Lob:** Certified Mail US$ 6,95 + carta First-Class US$ 1,066 = **US$ 8,02** (US$ 8,26 com a taxa de 3% do cartão) ([Lob pricing](https://help.lob.com/print-and-mail/ready-to-get-started/pricing-details.md)).
- **Ao preço da PostalForm (US$ 11,80):** sobram ~US$ 3,54 brutos. Depois das taxas do Stripe Brasil (~4% + 2% internacional + 2% de câmbio, cerca de US$ 0,95), ficam **~US$ 2,6 por carta registrada** ([Stripe BR](https://stripe.com/br/pricing)).
- **Carta simples:** ~US$ 1,9 de margem.
- **Volume:** **US$ 5 mil/mês de lucro bruto exigem ~1.900 cartas registradas por mês.** Uma única contestação no Stripe (R$ 55) apaga a margem de várias cartas.
- **USPS** (Notice 123, vigente desde 4/10/2026): Certified Mail US$ 5,55; aviso de recebimento eletrônico US$ 2,91; First-Class 1 oz US$ 0,82 com selo ([USPS](https://pe.usps.com/text/dmm300/Notice123.htm)).

## Concorrentes

- **EUA (10+):** Mailform (US$ 2,99 + US$ 8,99 registrada), LetterStream/OnlineCertifiedMail.com, Certified Mail Labels (o maior varejista de registradas, **#433.484 no [Tranco](https://tranco-list.eu/)**), The Letter Pilot (registrada a partir de US$ 11,00; "10,000+ letters"), Click2Mail, Quadient e-Certify, USPS Click-N-Ship, PostalMethods, Docsmit, SimpleCertifiedMail.
- **Reino Unido (6+):** UK Postbox, Modernmail, PrintPigeon, Postworks, CFH Docmail, Stannp (API B2B).
- Os pequenos que ganham competem com dezenas de páginas por intenção: a PostalForm cobre cartas de contestação, avisos de locador por estado e respostas a cobradores; a Send Letters Online cobre HMRC, DVLA, Section 8 e mais.

## Bloqueios e riscos

> [!warning] Os bloqueios são estruturais e dependem de terceiros
> - **Lob:** o cliente não pode *"rent, lease, copy, transfer, resell, sublicense, lease, time-share, or otherwise provide access to the Lob Service to a third party"* ([Lob Terms](https://www.lob.com/legal)). Uma loja que envia os pedidos por conta própria talvez não "dê acesso", mas o texto é ambíguo. É preciso aprovação por escrito.
> - **PostGrid:** licença só para *"internal business purposes"* e proibição de *"competing product"* ([PostGrid Terms](https://www.postgrid.com/terms-of-service/)).
> - **ClickSend Post** fechou para novos clientes ([ClickSend](https://www.clicksend.com/us/pricing/us/)).
> - **Paddle**, o merchant of record acessível a brasileiros, proíbe produtos *"that require physical delivery"* ([Paddle](https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle)). Sobra o Stripe Brasil, que adiciona ~4% entre taxa internacional e câmbio e torna o fundador o vendedor. Uma LLC americana (Stripe Atlas ou similar) passa do orçamento de US$ 130.
> - **Postagem pré-paga em dólar**, contestações e abuso (assédio, ameaças legais falsas). Os concorrentes adotam política de "sem reembolso depois da impressão" e de conteúdo proibido.
> - **Demanda sensível a preço:** o autocomplete de "send certified mail online" traz "free", "cheap", "cheapest" e "reddit".

## Pontuação

| Rodada | WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|---|
| Final ([[finalists_global_verification]]) | 4 | 2 | 3 | 3 | 4 | 3 | 2 | **21/35** |
| Exploratória ([[verified_revenue_niches]]) | 5 | 3 | 4 | 4 | 5 | 4 | 3 | 28/35 |

A rodada final colocou as cartas **acima** do Jira (22) de propósito: é a única finalista com evidência verificada de que um estreante sem audiência chegou a US$ 4–6 mil em 30 dias.

## Veredito

**CONDICIONAL GO.** Só seguir se as três condições forem verdadeiras:
1. **Autorização por escrito da Lob** (ou de outro provedor) para uma loja voltada ao consumidor.
2. Uma conta **Stripe Brasil** que aceite checkout internacional para esse serviço.
3. Lançamento com um **nicho vertical** (avisos de locador por estado, cartas de contestação, notificações ao HMRC/DVLA) em vez de "envie uma carta".

Se qualquer uma falhar, a ideia morre. Construção estimada em 1–2 semanas com Claude Code: Next.js, Stripe, PDF, validação de endereço, API de postagem e webhooks de rastreio.

## Notas de pesquisa

- [[Oportunidade de produto validada 2026]], seção "Cartas registradas online têm a melhor prova, mas margem fina"
- [[finalists_global_verification]], Q1 e Q6
- [[verified_revenue_niches]], candidato C1 (questões 1, 2, 5 e 6)
- Relacionadas: [[Pagamentos e impostos]] (Paddle × Stripe), [[Próximos passos]] (ticket com a Lob)
