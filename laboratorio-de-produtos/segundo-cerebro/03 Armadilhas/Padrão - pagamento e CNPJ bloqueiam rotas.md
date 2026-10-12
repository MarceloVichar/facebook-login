---
tags:
  - armadilha
  - padrao
atualizado: 2026-10-12
fonte:
  - "[[Validação condicionais e novos focos]]"
  - "[[certified_mail_validation]]"
  - "[[brazil_emerging_platforms]]"
  - "[[exam_prep_deep]]"
---

# Padrão: pagamento e CNPJ bloqueiam rotas inteiras

Voltar para [[Armadilhas e ideias mortas]] · [[Pagamentos e impostos]].

> [!warning] A regra
> **Antes de validar a demanda, valide se dá para receber.** Na rodada 2, várias ideias com demanda real morreram ou travaram em G7 ([[Portões de aprovação]]) porque o merchant of record proíbe a categoria ou porque a plataforma exige empresa aberta.

## O Paddle proíbe categorias inteiras

A política de uso do Paddle, atualizada em 13/04/2026 ([Paddle AUP](https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle)), proíbe ou restringe:

| Categoria do Paddle | Ideia atingida |
|---|---|
| "Certifications and exam preparation services" | [[Simulado do exame de despachante aduaneiro dos EUA (CBLE)]], [[Preparatório do teste de nacionalidade portuguesa]] |
| "Government Services" | Serviços de despachante ou de trâmite oficial |
| Produtos que exigem **entrega física** | [[Cartas registradas online (EUA e Reino Unido)]] |
| Ferramentas automáticas de **avaliações** | Coletor de avaliações do Google para PMEs portuguesas (KILL em [[portuguese_spanish_arbitrage]]) |
| **Televendas** ativas (telemarketing), restringidas | Listas de leads como a [[Feed de transportadoras recém-registradas (FMCSA)|FMCSA]]; a venda por telefone da SmartCondo ([[Software de condomínio autogerido em Portugal]]) |

## As alternativas também têm limites

- **Lemon Squeezy:** veta serviços e paga o Brasil só via PayPal ([Lemon Squeezy](https://docs.lemonsqueezy.com/help/getting-started/prohibited-products)). Está migrando para o Stripe Managed Payments, que não atende o Brasil ([[exam_prep_deep]]).
- **Polar:** só software, e não paga no Brasil ([Polar AUP](https://polar.sh/docs/merchant-of-record/acceptable-use)).
- **Gumroad:** é MoR a 10% + US$ 0,50 e **não proíbe** cursos nem preparatórios ([Gumroad prohibited](https://gumroad.com/prohibited)). Mas o Brasil **não está** na lista de repasse bancário, então o repasse é só por PayPal ([Gumroad: Getting paid](https://gumroad.com/help/article/13-getting-paid)). Isso precisa de um teste de US$ 1 antes de construir ([[Carteira de testes]]).
- **Stripe Brasil:** aceita conta de pessoa física e não restringe correspondência ([Stripe restricted](https://stripe.com/legal/restricted-businesses)), mas não é MoR: o vendedor carrega o VAT europeu. Cobra 3,99% + R$ 0,39, mais 2% em cartão internacional ([Stripe BR](https://stripe.com/br/pricing)).

## TikTok, Shopee e Temu exigem CNPJ, e o MEI não cobre programação

- O cadastro de desenvolvedor no TikTok Shop, na Shopee e na Temu só aceita **empresa registrada** ([requisitos TikTok](https://partner.tiktokshop.com/docv2/page/64f19899cb677b0286e75d67); [Shopee Open Platform](https://open.shopee.com/developer-guide/12)).
- **O MEI não cobre programação** ([[Pagamentos e impostos]]; ver **ME / EPP / MEI** no [[07 Glossário]]).
- Consequência: todo app de marketplace brasileiro obriga a abrir uma ME **antes da primeira venda**, o que contradiz o plano de começar no CPF. Atinge o [[Lucro por live e comissão de host no TikTok Shop]] e todas as ideias de TikTok Shop mortas na rodada 2.

## O que sobra no orçamento de R$ 700

Segundo o relatório da rodada 2, cabem as ideias que:
- cobram **em reais pelo Asaas, Kiwify ou Hotmart com CPF**; ou
- vendem **software puro** por um MoR que aceite a categoria (o Paddle aceita o [[Visualizador de p7m para a Itália]], desde que não prometa verificação jurídica da assinatura).

A regra da [[Carteira de testes]] vem daqui: **nenhuma empresa é aberta antes de um teste passar.**

## Relacionadas

[[Padrão - plataforma absorve o recurso]] · [[Portões de aprovação]]
