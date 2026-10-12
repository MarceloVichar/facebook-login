---
tags:
  - oportunidade
  - mercado/global
  - status/morta
  - finalista
status: morta
veredito: KILL
score: 17
score_inicial: 26
mercado: global
rodada: final
fonte:
  - "[[us_eu_regulatory_demand]]"
  - "[[finalists_global_verification]]"
  - "[[Oportunidade de produto validada 2026]]"
---

# Botão de desistência da UE fora do Shopify

Voltar para [[Ranking]] · [[Armadilhas e ideias mortas]].

> [!failure] Morta na rodada final (17/35)
> A obrigação é real, mas a **lacuna fora do Shopify fechou** e o prazo **já passou** (19/06/2026). A disposição a pagar ficou no Shopify. Mistura o [[Padrão - plataforma absorve o recurso]] com o [[Padrão - saturação]].

## O que era

Uma função de desistência hospedada, em duas etapas, para sites e serviços online **fora do Shopify**: botão embutível, formulário sem login, verificação opcional do pedido via plataforma ou Stripe, confirmação automática em suporte durável, caixa de entrada do lojista e log de auditoria exportável, em DE, FR, NL, IT, ES, PL e EN.

## Comprador

Lojistas B2C da UE em Wix, Squarespace, Webflow ou sites próprios; vendedores de serviços online (cursos, mentorias, assinaturas, SaaS B2C no Stripe); comerciantes de fora da UE que vendem para lá. Para escala: só o Shopify tem ~446 mil lojas ativas nos cinco maiores mercados da UE ([EightX](https://eightx.co/blog/eu-shopify-landscape)).

## Evidências

- **Obrigação real:** Diretiva (UE) 2023/2673, verificada na transposição alemã, o **§356a BGB**. A função precisa se chamar "Vertrag widerrufen" ou equivalente e estar sempre disponível, em destaque e acessível ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__356a.html)). Está em vigor desde **19/06/2026**.
- **Fora do Shopify, a lacuna fechou:**
  - WooCommerce: **68 plugins de desistência novos em 2026**, quase todos grátis, além do Germanized (70 mil instalações), que já traz o recurso ([WP API](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[search]=withdrawal%20button&request[per_page]=50)).
  - Shopware: recurso **no core desde a 6.7.9.0** (abril de 2026) ([Xictron](https://www.xictron.com/de/blog/widerrufsbutton-umsetzung-shopware-juni-2026/)).
  - Wix: ~7 apps, todos grátis ou freemium, com no máximo 4 avaliações cada. PrestaShop: ao menos 4 módulos pagos de €29–60. Jimdo: botão nativo. eRecht24, Händlerbund e widerrufonline.de cobrem os construtores de site.
- **A disposição a pagar ficou no Shopify:** o app líder tem **2.317 avaliações** ([Shopify](https://apps.shopify.com/eu-widerrufsbutton)), contra no máximo 17 notas em qualquer plugin WooCommerce e no máximo 4 avaliações em qualquer app Wix.
- **Fiscalização branda:** uma carta de associação de €416,50, junto com outras infrações. Basta para manter lojistas instalando ferramentas grátis, mas não para pagar um fornecedor novo.

## Pontuação

| Rodada | WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|---|
| Final ([[finalists_global_verification]]) | 2 | 1 | 3 | 2 | 5 | 2 | 2 | **17/35** |
| Exploratória ([[us_eu_regulatory_demand]], C1) | 4 | 2 | 4 | 4 | 5 | 4 | 3 | 26/35 |

## Veredito

**KILL.** A lacuna de plataforma fechou, o prazo passou e a disposição a pagar fora do Shopify é quase zero. Os micronichos que sobram (Webflow, serviços fora do portal do Stripe) são pequenos demais ou arriscados demais para um fundador que não fala alemão: implementações com defeito atraem cartas de advertência.

## Notas de pesquisa

- [[finalists_global_verification]], Q2 e Q6
- [[us_eu_regulatory_demand]], seções 13 e 14
- Relacionadas: [[Mais um app de desistência no Shopify]], [[Scanner de green claims (EmpCo)]]
