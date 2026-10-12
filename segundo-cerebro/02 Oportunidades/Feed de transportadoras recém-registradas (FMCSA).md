---
tags:
  - oportunidade
  - mercado/global
  - status/condicional
  - promissora
status: condicional
veredito: NÃO TESTADA NA RODADA FINAL (próxima a verificar)
score: 24
mercado: global
rodada: exploratória
fonte:
  - "[[verified_revenue_niches]]"
  - "[[Oportunidade de produto validada 2026]]"
---

# Feed de transportadoras recém-registradas (FMCSA)

Voltar para [[Ranking]].

> [!tip] A próxima a verificar (24/35, rodada exploratória)
> Das ideias que não passaram pela rodada final, é **a que mais merece a próxima verificação**. Tem um concorrente com **receita verificada** sobre **dados públicos gratuitos** e só usa SEO como canal. Segue o mesmo padrão dos laudos: o valor está no formato e no filtro, não em IA. O relatório indica esta como o plano C se os laudos falharem.

## O que é

Um **feed diário de transportadoras recém-registradas** nos EUA, filtrado por estado ou tipo, com alertas de renovação de seguro e de mudança de autorização. A entrega é por e-mail, CSV ou webhook.

## Comprador

Corretores de seguro, empresas de factoring, despachantes e serviços de compliance que precisam abordar transportadoras novas. O TruckerDB diz que surgem "15,000+ new DOT carriers" por mês (autodeclarado) ([truckerdb.com](https://www.truckerdb.com/)). A dor, nas palavras dele: *"getting in front of them — with the right contact information — is a grind"*.

## Evidências

- **Concorrente verificado:** o TruckerDB tem **US$ 1.580 de MRR com 20 assinantes**, a US$ 49 e US$ 99/mês, com **192 visitas/mês**, domain rating 25 e **SEO como único canal** ([TrustMRR TruckerDB](https://trustmrr.com/startup/truckerdb)). Vinte assinantes com 192 visitas/mês sugerem intenção alta e pouca concorrência de SEO.
- **Dados públicos e gratuitos:** o dataset "Motor Carrier Registrations – Census Files" traz "contact information and demographic information" das transportadoras registradas ([data.transportation.gov](https://data.transportation.gov/Trucking-and-Motorcoaches/Motor-Carrier-Registrations-Census-Files/4a2k-zf79)). A API QCMobile da FMCSA exige chave ([FMCSA API](https://mobile.fmcsa.dot.gov/QCDevsite/docs/qcApi)).
- **O padrão "dados públicos → leads B2B" se repete com fundadores independentes** (receita verificada no TrustMRR):
  - Leads de inventário (probate): US$ 70.481 de MRR ([b2bsaas](https://trustmrr.com/startup/b2bsaas))
  - Harper (Companies House, Reino Unido): US$ 2.580 de MRR, £300/mês ([Harper](https://trustmrr.com/startup/harper))
  - Subbasta (leilões em Malta): US$ 3.681 de MRR ([Subbasta](https://trustmrr.com/startup/subbasta))
  - Exemplos fracos do mesmo padrão: Insider Trade Alerts (SEC Form 4), US$ 405 no total; Property Alerts USA, US$ 0.

## Concorrentes

TruckerDB é o único medido. **A densidade de concorrentes de listas FMCSA não foi verificada**, e essa é a primeira coisa a checar.

## Riscos

> [!warning] Riscos
> - **Conformidade da abordagem do comprador** (ligações e e-mails frios). A exposição legal é do comprador, mas respinga no vendedor; precisa de avisos.
> - Listas viram commodity; o dataset da FMCSA pode mudar.
> - Produtos B2B de leads tendem a ter churn alto.
> - Mais lento até a primeira receita que as cartas, porque depende de SEO. A saída é oferecer uma lista de amostra grátis.

## Pontuação (rodada exploratória, [[verified_revenue_niches]])

| WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|
| 4 | 3 | 4 | 3 | 4 | 3 | 3 | **24/35** |

## Construção e caminho

- **Construção:** ~1–2 semanas: ETL diário dos arquivos da FMCSA, deduplicação, digest por e-mail e cobrança.
- **Primeira receita:** ~4–10 semanas.
- **Caminho até ~US$ 5 mil/mês:** 50–100 assinaturas a US$ 49–99.
- **Diferenciação possível:** alertas de mudança de autorização e de seguro, filtros por estado, entrega para CRM e webhook.
- **Se a FMCSA estiver lotada,** o mesmo padrão de construção se transfere para outros datasets públicos (os análogos Harper e Subbasta).
- **Pagamento:** como produto digital vendido no exterior, cabe no Paddle ([[Pagamentos e impostos]]).

## Veredito

**Condicional, à espera de verificação.** É a próxima candidata a passar pelo teste de estresse caso os laudos sejam abandonados.

## Notas de pesquisa

- [[Oportunidade de produto validada 2026]], seções "Ideias promissoras que não passaram pela rodada final" e "Conclusão"
- [[verified_revenue_niches]], questões 1, 2, 5 e 6 (candidato C2)
