---
tags:
  - armadilha
  - padrao
atualizado: 2026-10-12
fonte:
  - "[[Validação condicionais e novos focos]]"
  - "[[brazil_emerging_platforms]]"
  - "[[unmet_feature_requests]]"
  - "[[public_records_data]]"
  - "[[finalists_global_verification]]"
---

# Padrão: a enxurrada de micro-SaaS feito com IA

Voltar para [[Armadilhas e ideias mortas]].

> [!warning] A regra
> **Em 2026, os nichos óbvios enchem de micro-SaaS montados com assistentes de programação antes de qualquer validação.** O código deixou de ser barreira: qualquer pessoa constrói o MVP numa tarde. Uma lacuna visível (um prazo novo, um ticket muito votado, um dataset público, uma loja de apps nova) recebe dezenas de ofertas em semanas. É a versão acelerada do [[Padrão - saturação]].

## Evidências

| Onde | O que aconteceu | Fonte |
|---|---|---|
| **TikTok Shop Brasil** | **297 apps** na loja em 12/10/2026; **cerca de 57%** dos apps capturados foram criados em 2026, 127 só entre abril e agosto. Um deles tem como desenvolvedor, literalmente, "claude code" | [[brazil_emerging_platforms]]; [loja BR](https://seller-br.tiktok.com/appstore/br/search?category_id=1&dtc=&fromRecommendation=&page=1&sort=3); [listing Charme](https://seller-br.tiktok.com/appstore/br/7642635725993248530) |
| TikTok Shop, aumento de taxas de 15/07/2026 | Cerca de 20 apps de "lucro real" até outubro, vários grátis | [[Validação condicionais e novos focos]] |
| Shopee, NFS-e da Comissão Extra (01/08/2026) | Ferramenta da Conta Azul em 24/07 e pelo menos seis ofertas em ~10 semanas | [Conta Azul](https://contaazul.com/blog/como-emitir-nota-fiscal-afiliado-shopee-na-conta-azul/) |
| **WooCommerce, botão de desistência da UE** | **68 plugins** de 2026 para o mesmo prazo | [WP API](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[search]=withdrawal%20button&request[per_page]=50); [[Botão de desistência da UE fora do Shopify]] |
| **Atlassian Marketplace** | A Katabarwa Labs publicou **mais de 10 apps Forge** entre 01/09 e 06/10/2026, cada um baseado num ticket muito votado; todos com **0–2 instalações** | [[unmet_feature_requests]]; [API Katabarwa](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=Katabarwa&limit=10&withVersion=true) |
| **Apify** | Dezenas a centenas de raspadores por dataset público: 578 atores para alvarás de obra, 213 para NPI, 194 para CNPJ e 67 para FMCSA | [Apify alvarás](https://api.apify.com/v2/store?search=building%20permit&limit=40); [Apify FMCSA](https://api.apify.com/v2/store?search=fmcsa&limit=40) |
| FMCSA | Pelo menos oito SaaS sobre o mesmo censo gratuito surgiram em 2026, depois de a receita do TruckerDB ficar pública | [[Feed de transportadoras recém-registradas (FMCSA)]] |
| Hotmart, laudos | 55 produtos de laudo datados só em 2026; dos 66 datados desde 2025, só 1 tem avaliação | [[laudos_validation]] |
| App Store de Portugal, teste de nacionalidade | Pelo menos cinco apps com 0 avaliações e um site concorrente lançados entre maio e agosto de 2026, antes de a regra existir | [[exam_prep_deep]] |

## Por que isso importa

- **Lojas sem sinal de tração não deixam um novato se destacar.** A loja do TikTok BR não mostra instalações nem avaliações, então ninguém prova que vende.
- **A vitrine de receita é usada para copiar.** Os termos da API do TrustMRR proíbem "cloning businesses" ([TrustMRR API](https://trustmrr.com/docs/api)), e vencedores recentes já estão à venda poucos meses depois de fundados (P7M.io por US$ 120 mil, Francopass por US$ 100 mil).
- **Votos e prazos sinalizam dor, não comprador alcançável.** Os tickets mais votados da Atlassian viraram apps que ninguém instalou.

## O que a IA não copia em uma tarde

Os relatórios apontam a vantagem que sobra:
- formato normativo correto (laudo NBR 16280, Lite do PL 159/2026);
- conteúdo com citação jurídica verificável (Código de Seguros, 19 CFR);
- idioma e contexto local;
- posição na busca, que leva meses (no TrustMRR, a receita se correlaciona 0,47 com a idade e 0,43 com a autoridade de domínio, mas só 0,25 com seguidores ([TrustMRR stats](https://trustmrr.com/stats))).

## Relacionadas

[[Padrão - saturação]] · [[Padrão - pesquisa de mesa não aprova G1 e G2]] · [[IA no centro do produto]] · [[Portões de aprovação]]
