# Marketplace and App-Store Gaps for a Solo Brazilian Developer (data collected 2026-10-12)

*Method note: most numbers below come from my own crawls of the marketplaces' public pages and APIs on 2026-10-12. These were the Nuvemshop App Store category pages, the Atlassian Marketplace REST API, the WordPress.org plugins API, Google Workspace Marketplace search pages, Shopify App Store search and the Chrome Web Store listings. Third-party store counts come from Store Leads, whose pages are dated 2026-10-09. The session's shared web-search quota ran out partway through. After that I only fetched known primary URLs directly; I ran no search-engine queries. Some secondary marketplaces (Zoho, Webflow, Squarespace, Figma, Airtable, Zapier) are therefore thin; see the Gaps sections. Revenue claims are labelled VERIFIED (platform or official data) or SELF-REPORTED.*

---

## 1. Nuvemshop App Store: size, thin categories, top apps, approval and billing, store count, and the 2026 NubeSDK change

### Takeaway
Nuvemshop is the largest and fastest-growing Brazilian platform, with about 126k live BR stores (+24% YoY per Store Leads; Nuvemshop itself claims 180k+ merchants). Its store has only 647 listed apps. The median app has 3 reviews and just 57 apps have 100 or more reviews, so competition is shallow. Developers can bill merchants directly with no GMV commission. A forced migration is under way right now: script-injecting apps without NubeSDK were delisted on 30 Sep 2026, and progressive uninstall from stores starts on 30 Oct 2026. Several sub-niches are nearly empty, including wholesale/B2B, search and filters, NF-e, subscriptions, gift cards and quotes. Willingness-to-pay evidence per niche is thin, and buyers are BRL-paying SMBs.

### Cited Findings
**Size and store count**
- The App Store home page says "Descubra mais de 700 apps para potencializar as vendas de +180 mil lojistas" (page fetched 2026-10-12) — [Nuvemshop Loja de Aplicativos](https://www.nuvemshop.com.br/loja-aplicativos-nuvem)
- My crawl of all 10 BR categories, paginating every page on 2026-10-12, found **647 unique listed apps** — [Marketing](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/marketing), [Recursos extras](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/recursos-extras), [Comunicação](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/comunicacao), [Gestão](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/gestao), [Logística](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/logistica), [Segurança](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/seguranca), [Estatísticas](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/estatisticas), [Dropshipping](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/dropshipping), [Canais de vendas](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/canais-de-vendas), [Pagamentos](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/pagamentos)
  - Apps per category: Marketing 226, Recursos extras 157, Comunicação 57, Gestão 52, Logística 41, Segurança 30, Estatísticas 28, Dropshipping 24, Canais de vendas 17, Pagamentos 15. Reviews per category: Dropshipping 6,979, Marketing 6,086, Comunicação 2,703, Logística 2,546, Recursos extras 1,736, Pagamentos 1,481, Segurança 1,405, Gestão 1,169, Canais de vendas 1,089, Estatísticas 433.
  - Review depth across all 647 apps: 25,627 reviews in total; median 3 reviews per app; mean 39.6; 90th percentile 85. 184 apps (28%) have zero reviews. Only 212 have 10 or more, 57 have 100 or more, 7 have 500 or more and 3 have 1,000 or more.
  - Price labels: "Compras no app" 496 (77%), "Pago" 95, "Grátis" 56.
- Conflicting app counts: the store page says "700+". My crawl found 647 listed. The search summary of a 2026 Nuvemshop blog post said "300+ integrações" (not fetched) — [Nuvemshop blog](https://www.nuvemshop.com.br/blog/aplicativos-nuvemshop/)
- Store Leads (updated Oct 9, 2026) counts **126,358 live Tiendanube/Nuvemshop stores in Brazil, up 24% YoY in 2026 Q3**. Its breakdown: 38.5% sell apparel, 8.3% beauty and fitness, 7.0% home and garden, and 84.8% ship by Correios — [Store Leads – Tiendanube BR](https://storeleads.app/reports/tiendanube/BR/top-stores)

**Top apps (rating, review count, price), crawl of 2026-10-12**
- The 15 apps with the most reviews:

  | App | Rating | Reviews |
  |---|---|---|
  | AliExpress by Dropi | 4.9 | 4,467 |
  | Drop Nacional by Dropi | 4.9 | 1,636 |
  | WhatsApp Marketing | 4.8 | 1,003 |
  | JivoChat (free) | 4.8 | 729 |
  | Marketplaces by HubNoov | 4.5 | 671 |
  | Manda Bem | 5.0 | 633 |
  | Melhor Envio | 4.5 | 572 |
  | Appmax | 4.5 | 497 |
  | Cashing | 4.8 | 489 |
  | Bling | 4.6 | 469 |
  | Mercado Pago | 4.5 | 468 |
  | Lily Reviews | 5.0 | 411 |
  | Super Frete | 4.9 | 398 |
  | Nuvem Marketing | 4.7 | 339 |
  | Smartbis | 4.7 | 334 |

  Sources: [store home](https://www.nuvemshop.com.br/loja-aplicativos-nuvem) and the category pages above.
- Prices shown on app pages (fetched 2026-10-12):
  - Cashing: R$29.90 / R$49.90 / R$99.90 — [Cashing](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/cashing)
  - Lily Reviews: tiers at R$249/month and R$549/month — [Lily Reviews](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/lily-reviews)
  - Compre por Grade Pro (Huapps): R$59.90/month
  - HintUP: R$99
  - Cliqenvio: R$49 to R$199/month
- Ratings are uniformly high. Median ratings, counting only apps with 10 or more reviews, run from 4.2 (Pagamentos) to 5.0 (Estatísticas). Only 22 apps with 10+ reviews are rated below 4.0, and they are mostly payment, logistics and ERP integrations:
  - Olist 3.7 (163), PagBank 3.9 (127), Cielo 3.3 (32)
  - Lalamove 2.6 (27), ASAP Log 2.2 (17), Sigep App – Gadol 1.6 (14)
  - ClearSale Total V2 3.0 (12), Elogiou 2.4 (13), MagicShare 2.8 (33)

  Source: crawl of the category pages above.

**Thin sub-niches (keyword scan of the 647 app names and descriptions, 2026-10-12)**
- **B2B / atacado / revenda:** 3 apps, 15 reviews in total. They are Compre por Grade Pro – Huapps 4.9 (10) at R$59.90/month, Backchannel 5.0 (3) and Solicitar Orçamento 5.0 (2) — [Recursos extras](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/recursos-extras)
- **Search and filters:** 6 apps, 24 reviews in total. HintUP 4.5 (18) costs R$99; Busca Inteligente is 5.0 (4) — [Marketing](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/marketing)
- **NF-e / fiscal:** 3 apps (Notazz 4.8 with 19 reviews, plus two with no reviews) — [Gestão](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/gestao)
- **Subscriptions / recurrence:** about 1 real subscription app (Cliqenvio, 0 reviews). Smartbis matched the keyword but is a cashback tool.
- **Other thin niches:**
  - Gift cards: 3 apps, 73 reviews
  - Quotes (orçamento): 3 apps, 8 reviews
  - LGPD cookie bar: 1 dedicated app with 7 reviews
  - Antifraud: 2 apps, 13 reviews (ClearSale rated 3.0)
  - Pixel/CAPI tracking: 4 apps, 0 reviews
  - Translation / multi-currency: 2 apps, 0 reviews
- **Crowded sub-niches:**
  - WhatsApp: 68 apps, 3,953 reviews
  - Email / abandoned cart: 59 apps, 3,600 reviews
  - Reviews: 36 apps, 1,594 reviews
  - Pre-sale / back-in-stock: 37 apps
  - Product personalization: 50 apps
  - Checkout / order bump: 13 apps, 1,075 reviews
- **Analytics and profit (Estatísticas):** 28 apps. The established ones are Escalafy 5.0 (150), Dash Analytics 5.0 (107), Nuvem Stats 4.9 (74) and Prax 5.0 (50). "Lucro: custos e preço de venda" is 5.0 with 5 reviews — [Estatísticas](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/estatisticas)

**Billing and revenue share**
- Two ways to get paid (help article updated 15/01/2026):
  - **Partner billing:** the app is listed as "Gratuito" with "Possui vendas no aplicativo" ticked, and "o lojista ... faz o pagamento diretamente ao desenvolvedor".
  - **Nuvemshop billing:** one-time or monthly charges, withdrawn "já com o desconto das taxas do meio de pagamento escolhido pelo lojista e o imposto da nota fiscal".
  - After a trial, "a Nuvemshop não irá realizar a cobranças automáticas do lojista. Ele deve efetuar o pagamento manualmente... O modelo de cobrança automática é opcional e depende da ativação do lojista."
  - Source: [Nuvemshop – Como eu recebo pelo uso do meu aplicativo](https://atendimento.nuvemshop.com.br/pt_BR/parceiros-tecnologicos/como-eu-recebo-pelo-uso-do-meu-aplicativo-criado-na-nuvemshop)
- The docs say: "Publicar um app não gera automaticamente uma comissão sobre o volume de vendas da loja (GMV)". Billing mode is chosen per country. Monthly billing uses the Billing API. Publication data is locked while the app is "Em aprovação" — [nuvemshop.dev – Preços & Cobrança](https://nuvemshop.dev/apps/publish/pricing-billing)
- App partners "recebem pela cobrança de mensalidade dos apps e não por comissão". Apps that are "gratuitos para o plano Next" are paid an agreed per-use amount negotiated with Nuvemshop commercial staff. Partner support responds in "até 1 hora". The guide was updated 02/07/2025 — [Guia Parceiros Tecnológicos](https://atendimento.nuvemshop.com.br/pt_BR/parceiros-tecnologicos/guia-detalhes-do-programa-de-parceiros-tecnologicos)

**Approval (homologação)**
- Every app goes through homologation.
  - ERP, Payments and Shipping apps get a "roteiro" of required steps. The partner records a video demonstration, and fixes are tracked in an "Action Plan".
  - Other apps (marketing, tools) get a lighter review.
  - Any rejected item is fixed and resubmitted until it passes.
  - No duration or SLA is given.
  - Source: [nuvemshop.dev – Homologação](https://nuvemshop.dev/apps/publish/homologation/overview)
- Publication has two steps: submit the artefacts, then fill in the app data in the Partner Portal. Homologation "somente inicia-se após o envio de todos os artefatos" — [nuvemshop.dev – Publicação](https://nuvemshop.dev/apps/publish/app-publication/overview)

**Forced platform change: NubeSDK is mandatory**
- "Todo app que injeta scripts no storefront ou no checkout precisa do NubeSDK." API-only apps (ERP, CRM, backend analytics) and Admin-only apps are exempt.
  - Timeline: **5 June 2026**, new homologation requests for script-injecting apps require NubeSDK validation. **30 September 2026** (postponed from 30 Aug), non-migrated apps "são retirados da Loja de Aplicativos". **30 October 2026**, "começa a desinstalação progressiva desses apps".
  - "O checkout já exige NubeSDK para scripts de apps."
  - Sources: [nuvemshop.dev – Admin overview / Prazo de adoção do NubeSDK](https://nuvemshop.dev/apps/admin/overview), [nuvemshop.dev – Homologação](https://nuvemshop.dev/apps/publish/homologation/overview)
- NubeSDK works through events (e.g., `cart:update`, `shipping:select`) and offers 40+ insertion slots across storefront and checkout. It uses TypeScript/JSX with theme tokens instead of DOM manipulation — [nuvemshop.dev – NubeSDK](https://nuvemshop.dev/apps/nube-sdk/overview)

### Inferences
- Rough demand-to-competition: about 126k live BR stores across 647 apps is roughly 195 stores per app. That is about the same ratio as Shopify (see §8), but per-app review depth is about 10–100× lower than on Shopify. Incumbents are therefore beatable on SEO-in-Portuguese and listing quality, not only on features.
- The 30 Oct 2026 uninstall wave will strip merchants of storefront functions whose apps did not migrate. Those merchants will look for replacements in the store from late Oct 2026 into 2027. A new app built natively on NubeSDK lands in a store that has just been thinned. Caveat: I have no before/after list showing which niches lost apps.
- 77% of apps show "Compras no app", which per the help article is the partner-billing option. External billing (Pix/boleto/card via a Brazilian PSP) is evidently the norm and keeps 100% of revenue, minus PSP fees.
- Apparel is 38.5% of stores, which is roughly 48.6k apparel stores (inference). Size guides, grade (size/colour matrix) ordering and wholesale (atacado) are natural needs, yet only 3 B2B apps exist.
- Low review counts can mean either low demand or poor review collection. The thin niches carry real willingness-to-pay uncertainty.

### Gaps
- No public install counts. Reviews are the only demand proxy, and Nuvemshop's review prompting may differ from Shopify's.
- No published homologation duration. I could not confirm whether Nuvemshop has native wholesale/B2B price lists or native faceted search (the help-centre search URL returned 404). This is the key risk for the B2B and search candidates.
- No before/after data on how many apps were delisted on 30 Sep 2026.
- No developer revenue data for any Nuvemshop app.

---

## 2. Mercado Livre developer ecosystem: what sellers pay for, saturation, and 2026 changes

### Takeaway
ML has no open app store a newcomer can rank in. Its certified-partner program (DPP) needs US$2.5M of monthly GMV from your users in Brazil and is closed to new applications in Q4 2026. ML keeps shipping native features that undercut third parties: native price automation, which has blocked third-party API price edits since 18 Mar 2026, and the native "Faturador" NF-e with IBS/CBS rules. Proven demand is visible through Chrome extensions: Avantpro has 100,000 users and charges R$59.90/month. That niche is crowded, though, and carries ToS and front-end-scraping risk.

### Cited Findings
- **DPP status:** "Neste Q4 (último trimestre de 2026), não estamos aceitando novas inscrições devido a uma reestruturação interna." The page was updated 06/10/2026.
  - Requirements: monthly GMVe from active users of **US$2,500,000 for Brazil** (Argentina 1.5M, Mexico 1.0M, Chile/Uruguay/Colombia 200k, Peru 100k), a security assessment scored at 65% or more, and initiatives assigned by an "Integration Expert".
  - Source: [ML Developer Partner Program](https://developers.mercadolivre.com.br/pt_br/developer-partner-program)
- The ML API documentation covers Q&A (Perguntas e respostas), reputation, trends, visits, Mercado Ads (Product/Brand/Display Ads), Full replenishment planning, quantity/B2B pricing, size charts, claims/returns and the official "Mercado Livre MCP Server" — [ML API docs index (same page nav)](https://developers.mercadolivre.com.br/pt_br/developer-partner-program)
- **Native price automation (doc updated 01/10/2026):** "A partir de 18 de março de 2026, os itens com Automatização de Preços ativa terão a edição de preço bloqueada via API". PUT requests carrying price changes return HTTP 400 ("Cannot modify price on items with dynamic pricing") — [ML – Automatizações de preços](https://developers.mercadolivre.com.br/pt_br/automatizacoes-de-precos)
- **Native NF-e with tax reform:** the ML "Faturador" API takes IBS/CBS tax-rule configurations (CST/cClassTrib templates). The doc was updated 03/12/2025 — [ML – Configurações do IBS e CBS](https://developers.mercadolivre.com.br/pt_br/configuracoesibscbs)
- **2026 fee changes (secondary source, dated 03 Feb 2026):** from March 2026 the fixed fee for items under R$79 is replaced by a variable operating cost based on weight, cubage and price. Full, Coleta, Agências and Correios shipping and storage costs now use real weight and dimensions instead of category estimates — [Tecnospeed blog](https://blog.tecnospeed.com.br/tarifas-do-mercado-livre/)
- **Chrome Web Store metrics for ML seller tools (fetched 2026-10-12):**

  | Extension | Users | Rating (ratings) | Last updated | Source |
  |---|---|---|---|---|
  | Avantpro ML | 100,000 | 4.4 (452) | Oct 9, 2026 | [CWS](https://chromewebstore.google.com/detail/avantpro-ml/jdefnfmbnchmnjkcknaadaddgjbgephh) |
  | Hunter Spy | 9,000 | 4.9 (47) | Aug 25, 2026 | [CWS](https://chromewebstore.google.com/detail/hunter-spy-ferramenta-esp/kgdhkchjcdgbgnhfdhdoimllgjjanfmp) |
  | Cargoos | 5,000 | 5.0 (27) | Oct 10, 2026 | [CWS](https://chromewebstore.google.com/detail/cargoos-%E2%80%94-intelig%C3%AAncia-pa/hhpmjdebejnbpidgokkeikoainkcmlgi) |
  | Seller Analytics by Lexos | 3,000 | 3.4 (27) | Apr 1, 2024 (stale) | [CWS](https://chromewebstore.google.com/detail/seller-analytics-by-lexos/ehekfipbgkpjgljpfaigabeggglfinak) |
  | ML TrueSort | 3,000 | 4.0 (128) | — | [CWS](https://chromewebstore.google.com/detail/mercado-livre-truesort-a/ihhogidnfaalhknbpnoahmopliehocng) |
  | Seller Pro Analytics | 2,000 | 3.4 (7) | — | [CWS](https://chromewebstore.google.com/detail/seller-pro-analytics/jengodbfljjhgafbimgofjpjjfnikaha) |
  | GoSmarter | 1,000 | 4.6 (10) | — | [CWS](https://chromewebstore.google.com/detail/gosmarter-mercado-livre/jndiacccgpndehhgaddlpldnepkacblm) |
  | ML Ad Inspect | 990 | 4.2 (21) | Nov 2023 (stale) | [CWS](https://chromewebstore.google.com/detail/mercado-livre-ad-inspect/ebpgpolcjelpldmigjdnmicmjokcpjcl) |
  | Calculadora de Preço ML | 917 | 5.0 (2) | Jul 2023 (stale) | [CWS](https://chromewebstore.google.com/detail/calculadora-de-pre%C3%A7o-merc/ehdoppainepibpodfamimaofmemenofl) |
  | Nubimetrics Validador | 224 | — | — | [CWS](https://chromewebstore.google.com/detail/nubimetrics-validador-de/ceaillnednallicinelejbafokbphkbe) |

- **Avantpro pricing (official site, 2026-10-12):** "Plano Mensal R$ 59,90" per marketplace extension (ML, Shopee or Amazon). The annual plan is R$599 (R$49.92/month). The combo of all three is R$99.90/month, or R$999/year — [Avantpro](https://avantpro.com.br/). Conflict: a competitor's blog (GoSmarter) puts Avantpro at R$99–249, seen via search summary only and not fetched — [GoSmarter blog](https://gosmarter.com.br/melhores-extensoes-mercado-livre-2026-ranking/)
- From a search summary (not fetched): ML offers automatic answers for frequent questions through its own chat, and Nubimetrics' Pack 360 has a 14-day free trial — [Nubimetrics academia](https://academia.nubimetrics.com/br/responder-perguntas-marketplaces), [Hunter Hub blog](https://hunterhub.com.br/blog/ferramentas-para-mercado-livre-vender-mais-2/)
- **Shopee seller extensions (CWS, 2026-10-12):**
  - Shopee Fans: 30,000 users, 4.6 (122) — [CWS](https://chromewebstore.google.com/detail/shopee-fans-shopee-seller/lholmjphdehllbpdoiejoolbejkjcpba)
  - Shopdora: 10,000 users, 4.6 (11) — [CWS](https://chromewebstore.google.com/detail/shopdora-shopee-keyword-a/fbkkmbebblifoifknelgfijhbpodmlmo)
  - "Auto Responder Shopee" (a Brazilian extension): 49 users — [CWS](https://chromewebstore.google.com/detail/auto-responder-shopee-edu/jolbggkaaedkdjmmdobldclicibkikbc)

### Inferences
- Category saturation, my assessment:
  - **Repricing:** hostile, because ML's native automation wins any API conflict.
  - **NF-e:** hostile, because of Faturador and Bling.
  - **Market and competitor analytics (Chrome):** proven willingness to pay but crowded (Avantpro plus at least 6 others).
  - **Q&A auto-answer:** either an AI wrapper (excluded) or rule-based against an ML native feature.
  - **Ads (Mercado Ads API) and Full replenishment planning:** APIs exist and I found no clear dominant third-party extension, but I lack competitor data. Treat these as unvalidated.
  - **Reputation monitoring:** API exists; no competitor data.
- Back-of-envelope (inference only): if 3–5% of Avantpro's 100k users pay R$59.90, that is roughly R$180–300k/month. Price-sensitive BR sellers clearly pay for ML tools sold through Chrome, YouTube and TikTok content.
- The March 2026 fee change creates a real need for per-SKU margin recalculation by weight and dimensions. Free calculators exist, and the CWS calculator has only 917 users and was last updated in 2023, so willingness to pay for a standalone calculator is unproven.

### Gaps
- No official ML fee page fetched. The March 2026 fee details come from Tecnospeed (secondary).
- I could not count third-party vendors per ML category (Q&A, ads, Full, reputation) or confirm their prices, because search was unavailable.
- ML API terms for scraping-based Chrome extensions were not reviewed. ToS risk is flagged, not quantified.
- I found no Shopee Open Platform requirements or Shopee BR 2025–2026 fee changes.

---

## 3. Other Brazilian platforms (Tray, Loja Integrada, VTEX, Bling, Shopee, Hotmart/Kiwify)

### Takeaway
Store Leads (Oct 9, 2026) counts live BR stores as follows: Nuvemshop 126,358 (+24%), WooCommerce 77,598 (−20%), Wix 49,182 (+28%), Shopify 30,336 (−7%), Tray 29,663 (+32%), Loja Integrada 17,945 (−29%) and VTEX 2,745 (−8%). Tray is growing, but its store has 738 apps, 552 of them ERP connectors, and shows no ratings or installs, so discovery signals are weak. Loja Integrada is shrinking. VTEX is enterprise. Bling is a dominant ERP but its official third-party connectors are weak outside Nuvemshop. Hotmart and Kiwify have APIs but no app store.

### Cited Findings
- Store Leads live-store counts for Brazil (all updated Oct 9, 2026):

  | Platform | Live BR stores | YoY (2026 Q3) | Source |
  |---|---|---|---|
  | WooCommerce | 77,598 | −20% | [Store Leads](https://storeleads.app/reports/woocommerce/BR/top-stores) |
  | Wix | 49,182 | +28% | [Store Leads](https://storeleads.app/reports/wix/BR/top-stores) |
  | Tray Commerce | 29,663 | +32% | [Store Leads](https://storeleads.app/reports/tray/BR/top-stores) |
  | Loja Integrada | 17,945 | −29% | [Store Leads](https://storeleads.app/reports/lojaintegrada/BR/top-stores) |
  | VTEX | 2,745 | −8% | [Store Leads](https://storeleads.app/reports/vtex/BR/top-stores) |
  | Shopify | 30,336 | −7% | [Store Leads](https://storeleads.app/reports/shopify/BR/top-stores) |

  Shopify BR also has 431 Shopify Plus stores and 2,794 stores shipping by Correios.
- **Tray App Store:** its JSON API, queried 2026-10-12, returns **738 unique apps**:
  - Sistema de ERP 552, Integradores 85, Marketing 82, Vendas 81, Logística 69, Tray 33, Marketplaces 21, Produtos 17, Pós-vendas 15, Comunicação 12, Atendimento 10, Layout 7, Clientes 6. Only 43 are flagged free.
  - The API exposes no ratings or install counts.
  - Source: [Tray Aplicativos](https://aplicativos.tray.com.br/) (category endpoint `https://aplicativos.tray.com.br/api/category/{slug}`)
- **Loja Integrada:** its app store lists categories (Pagamentos, Gestão, Logística, Comunicação, Marketing e Vendas, Hubs Marketplace, Dropshipping, Domínios, Crédito) and featured partners such as ANYMARKET, Bling and Sizebay. Plans start at R$54/month — [Loja Integrada – Loja de aplicativos](https://lojaintegrada.com.br/loja-aplicativos/)
- **VTEX App Store:** apps are VTEX IO apps; billing options are free or subscription plans with optional usage-based variable fees — [VTEX – billing options](https://developers.vtex.com/docs/guides/vtex-io-documentation-billing-options), [VTEX App Store guide](https://developers.vtex.com/docs/guides/vtex-app-store)
- **Bling's official apps on other platforms:**
  - On Nuvemshop: 4.6 with 469 reviews — [Nuvemshop – Bling](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/bling)
  - On Shopify: **2.4 with 5 reviews**, from Shopify search on 2026-10-12 — [Shopify search "bling"](https://apps.shopify.com/search?q=bling)
  - Bling's help centre marks its Kangu logistics integration "[DESCONTINUADA]" (Apr 2025) — [Bling Ajuda](https://ajuda.bling.com.br/hc/pt-br/articles/4422745447319--DESCONTINUADA-Imprimir-etiqueta-da-log%C3%ADstica-Kangu)
- **Kiwify** has a public API reference ("API Pública") — [Kiwify API](https://docs.kiwify.com.br/api-reference/general). **Hotmart** has a developer portal — [Hotmart Developers](https://developers.hotmart.com/docs/pt-BR/)

### Inferences
- Tray is the second-best Brazilian platform by growth (+32% YoY). But 75% of its "apps" are ERP connectors, and with no ratings or installs a newcomer cannot gauge demand or build review-based credibility. Non-ERP Tray niches (about 186 apps) may be thin, but are unmeasurable.
- Hotmart and Kiwify offer API and webhook integrations but no discovery surface: no app store with search. Distribution would rely on content and SEO, the creator community and YouTube. They are not recommended as a marketplace play.
- VTEX's 2,745 BR stores are enterprise merchants, which implies enterprise sales cycles. Excluded under constraint (c).

### Gaps
- I found no published revenue share or approval timeline for Tray, Loja Integrada or VTEX.
- I could not verify whether Bling discontinued API v2: the help-centre search turned up no shutdown notice.
- No Shopee Open Platform ISV requirements or Shopee BR 2025–2026 fee changes were found (search budget exhausted).

---

## 4. Global marketplaces: high-demand categories with weak incumbents (real metrics)

### Takeaway
The clearest weak-incumbent pockets backed by hard numbers are three:
- **Atlassian Cloud:** popular paid apps still on Connect and stale, plus 3–3.5★ Gantt apps charging $180–2,090/year.
- **Google Workspace Marketplace:** add-ons with millions of installs and ratings of 2.5–3.4★, e.g., Sheets→Calendar sync.
- **Brazil-specific Shopify apps:** official Bling 2.4★, Olist Tiny 1.6★, Correios SIGEP 1.5★, but in a small, shrinking base of 30k stores.

The big US-centric Shopify and WordPress categories are saturated. Low-rated WordPress giants are mostly official corporate integrations.

### Cited Findings
**Atlassian Marketplace (REST API, 2026-10-12)**
- **6,623 cloud apps** are listed (API `count`) — [Atlassian Marketplace API](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&limit=5&sort=popularity&withVersion=true). Atlassian reports "300,000+ customers" — [Atlassian company](https://www.atlassian.com/company)
- In the **top 1,000 cloud apps by popularity**, 116 are still on Connect and 92 of those are paid via Atlassian. **83 Connect apps have shipped no release in over 12 months.** Examples:

  | App | Installs | Stars (reviews) | Last release | Billing |
  |---|---|---|---|---|
  | Open API (Swagger) Integration | 2,869 | 4.40 (31) | 2024-09 | paid; individual vendor "Toshihiro Sato" |
  | Slack Connector for Jira | 1,153 | 3.38 (57) | 2021 | paid |
  | Gantt Cloud | 916 | 2.96 (85) | 2021 | paid |
  | Gantt-Chart for Jira | 477 | 3.45 (129) | 2022 | paid |
  | Mermaid for Confluence | 803 | — | 2024-12 | paid |
  | CRM for Jira | 625 | 3.53 (102) | 2024 | paid |
  | Render Markdown | 3,855 | 3.46 | 2021 | free |
  | Google Chat for Jira Cloud | 11,007 | 2.30 (109) | 2021 | free |

  Source: [Atlassian Marketplace API – top cloud apps](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&limit=50&offset=0&sort=popularity&withVersion=true)
- **Gantt niche:** search returns 95 results, of which 37 Forge and 13 Connect appear in the top 50. Live cloud prices, annual USD:

  | App | Vendor | Installs | Stars (reviews) | Platform / last release | 15 users | 100 users |
  |---|---|---|---|---|---|---|
  | BigGantt | Appfire | 5,548 | 3.46 (273) | Forge | $313.5 | $2,090 |
  | WBS Gantt-Chart | Ricksoft | 5,293 | 3.48 (160) | Connect, 2019 | $198 | $1,320 |
  | Gantt Charts for Structure | Tempo | 6,306 | 4.20 (61) | Connect, 2021 | $219 | $1,460 |
  | Gantt-Chart for Jira | Werkstack | 477 | 3.45 (129) | Connect, 2022 | $180 | $1,200 |
  | Gantt Cloud | WISOFT | 916 | 2.96 (85) | Connect, 2021 | $67.5 | $450 |
  | GanttTable | DevSamurai | 1,300 | 4.69 (16) | — | $225 | $1,500 |

  Sources: [API search "gantt"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=gantt&limit=50&withVersion=true) and the pricing endpoint `https://marketplace.atlassian.com/rest/2/addons/{key}/pricing/cloud/live`.
- **Mermaid / diagrams-as-code (Confluence):** 93 results for "mermaid".

  | App | Vendor / status | Installs | Stars (reviews) | Price (annual) |
  |---|---|---|---|---|
  | Mermaid diagrams viewer | Atlassian Labs, free, Forge | 7,600 | 2.99 (26) | free |
  | Mermaid Diagrams for Confluence | Stratus; Connect, last release 2023 | 6,302 | 4.02 (23) | $60 @15 users, $400 @100 |
  | Mermaid Chart for Confluence | Mermaid Chart Inc, free | 4,105 | 2.94 (20) | free |
  | Mermaid Charts & Diagrams | weweave | 2,178 | 4.58 (15) | $34.5 @15 |
  | Just Add+ Embed Markdown, Diagrams | Forge, paid | 8,072 | 4.25 (50) | — |
  | PlantUML Diagrams for Confluence | Connect, 2020 | 5,299 | 4.30 (50) | — |

  Sources: [API search "mermaid"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=mermaid&limit=50&withVersion=true), [API search "plantuml"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=plantuml&limit=50&withVersion=true)
- **OpenAPI/Swagger viewers (Confluence):** 37 results. Open API (Swagger) Integration (Connect, 2,869 installs, 4.40) and Visualize OpenAPI (Connect, 1,211, 4.35) are both stale since 2024. Open API Documentation for Confluence is on Forge (1,802 installs, 3.68) — [API search "swagger"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=swagger&limit=50&withVersion=true)
- **Saturated niches:** "planning poker" returns 1,076 results with incumbents at 4.5–4.6★ (Planning Poker® 3,506 installs). "Time in status" returns 2,782 results; Tempo Timesheets has 26,369 installs — [API search "planning poker"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=planning%20poker&limit=50&withVersion=true)
- **DC→Cloud lead list (heuristic):** of the top 400 Data Center apps, 60 had no cloud listing that matched by key or by name prefix plus vendor. Examples: Announcement Banner for Confluence (772 DC installs; vendor has no cloud apps), Page View Tracker (854), JEditor (733), Survey and Vote Macros (558). Many are DC-only by nature (SSO, admin) — [API hosting=datacenter](https://marketplace.atlassian.com/rest/2/addons?hosting=datacenter&limit=50&offset=0&sort=popularity)

**Google Workspace Marketplace (search pages fetched 2026-10-12; the page states "Google doesn't verify reviews or ratings")**
- **High-install, low-rated add-ons:**

  | Add-on | Vendor | Rating | Users | Source |
  |---|---|---|---|---|
  | Sheets2GCal | — | 3.2 | 8M+ | [listing](https://workspace.google.com/marketplace/app/sheets2gcal/137564231775) |
  | Calendar Events Creator | — | 2.5 | 3M+ | [listing](https://workspace.google.com/marketplace/app/calendar_events_creator/101859618418) |
  | Form to Calendar | — | 3.4 | 1M+ | [listing](https://workspace.google.com/marketplace/app/form_to_calendar/210797006292) |
  | Form to Calendar Events | — | 2.9 | 73K+ | — |
  | Mail merge for Google Docs | — | 3.5 | 4M+ | — |
  | Doc Tools | Ablebits | 3.4 | 5M+ | — |
  | Remove Duplicates | Ablebits | 3.3 | 3M+ | — |
  | Save Emails and Attachments | Digital Inspiration | 3.7 | 2M+ | — |
  | Gmail to Notion | — | 2.9 | 2M+ | — |
  | Free Appointment Booking for Google Calendar | — | 3.8 | 1M+ | — |
  | Booking Calendar | — | 3.9 | 1M+ | — |
  | Lumin PDF | — | 3.7 | 22M+ | — |
  | PDF Converter | — | 3.1 | 6M+ | — |
  | Docusign | — | 3.6 | 4M+ | — |
  | Zoho CRM | — | 3.4 | 1M+ | — |

  Search pages used: [Workspace search "email tracking"](https://workspace.google.com/marketplace/search/email%20tracking), [search "calendar booking"](https://workspace.google.com/marketplace/search/calendar%20booking), [search "backup"](https://workspace.google.com/marketplace/search/backup), [search "pdf"](https://workspace.google.com/marketplace/search/pdf)
- These incumbents are maintained, just poorly rated. Sheets2GCal's listing was updated August 10, 2026 and is "Free of charge with paid features". Calendar Events Creator and Form to Calendar were updated May 28, 2026, and Remove Duplicates May 11, 2026 — see the listings above and [Remove Duplicates](https://workspace.google.com/marketplace/app/remove_duplicates/347814268012)
- **Sheets2GCal pricing (vendor site, 2026-10-12):** the free tier covers 200 updates/day and 100 auto-syncs/day. "S2GCal Monthly Personal €5.00 per Month", €48/year, plus €59/year and €299/year tiers — [Sheets2GCal](https://www.sheets2gcal.com/)
- **Saturated categories:**
  - Mail merge: YAMM 4.7, 16M+; Mail Merge (Quicklution) 4.9, 12M+; Mailmeteor 4.9, 7M+; Mail Merge with Attachments 4.3, 9M+
  - Forms: Form Publisher 4.6, 24M+
  - Source: [Workspace search "mail merge"](https://workspace.google.com/marketplace/search/mail%20merge)

**Shopify App Store (search via the app store's own results frame, 2026-10-12)**
- **Brazil-localized integrations are weak:**

  | App | Rating (reviews) | Price | Search |
  |---|---|---|---|
  | Bling (official) | 2.4 (5) | — | [bling](https://apps.shopify.com/search?q=bling) |
  | Sistema ERP da Olist (Tiny) | 1.6 (10) | — | [tiny erp](https://apps.shopify.com/search?q=tiny+erp) |
  | Correios – SIGEP – Etiquetas | 1.5 (14) | — | [correios](https://apps.shopify.com/search?q=correios) |
  | Correios – SEDEX – PAC | 3.6 (79) | — | [correios](https://apps.shopify.com/search?q=correios) |
  | Envios (Melhor Envio) | 1.0 (4) | — | [melhor envio](https://apps.shopify.com/search?q=melhor+envio) |
  | Frenet | 4.0 (62) | — | [correios](https://apps.shopify.com/search?q=correios) |
  | Cotei | 4.9 (23) | — | [correios](https://apps.shopify.com/search?q=correios) |
  | UpSeller ERP | 2.8 (6) | — | [mercado livre](https://apps.shopify.com/search?q=mercado+livre) |
  | Notasy – Notas Fiscais | 5.0 (4) | from $5/month | [nota fiscal](https://apps.shopify.com/search?q=nota+fiscal) |
  | Scala Payment Method Discount (Pix/boleto) | 5.0 (78) | free | [pix](https://apps.shopify.com/search?q=pix) |

- **Store Leads, Shopify Brazil:** 30,336 live stores (−7% YoY). The top apps among Brazilian stores are Judge.me (4,998 stores), Product Reviews (4,611), Ryviu (3,266), Areviews (3,053), 17TRACK (2,679), Loox (2,622) and DSers (2,352) — [Store Leads – Shopify BR](https://storeleads.app/reports/shopify/BR/top-stores)
- **Generic Shopify categories are deep.** In the Store design category, Section Store has 2,975 reviews, EComposer 3,483 and Booster AI SEO 5,477; most leaders are "Built for Shopify" — [Shopify – Store design](https://apps.shopify.com/categories/store-design). TikTok has 16,016 reviews ([search "pix"](https://apps.shopify.com/search?q=pix)) and Shopify Flow 14,681 ([search "boleto"](https://apps.shopify.com/search?q=boleto)).
- **Post-Scripts payment and shipping rules already have strong incumbents:** ETP Sort Hide Payment Methods 5.0 (571), HidePay 4.8 (392), HideShip 5.0 (91), Melon Minimum Order Quantity 5.0 (385) — [search "melhor envio"](https://apps.shopify.com/search?q=melhor+envio)

**WordPress.org (official plugins API, top 1,000 "popular", 2026-10-12)**
- The directory holds **71,295 plugins** (API `info.results`) — [WordPress.org plugins API](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[browse]=popular&request[per_page]=250)
- **Stale plugins with 100k+ installs:** 18 of them, including Limit Login Attempts (300k, last updated 2023-04-04), Health Check & Troubleshooting (200k, 2024-07-25, 3.6★), Layout Grid Block (200k, 2023), Search & Replace (100k, 2024-08), YARPP (100k, 2024-11) and WooSidebars (100k, 2024-04, 3.9★).
- **Active alternatives already dominate:** Limit Login Attempts Reloaded has 1M installs (4.8★), Wordfence 5M (4.7★), Loginizer 1M (4.8★) and Better Search Replace 1M — same API.
- **Low-rated plugins with 100k+ installs are mostly official integrations:** Meta for WooCommerce 2.1★ (400k), Google for WooCommerce 2.7★ (800k), WooCommerce PayPal Payments 2.9★ (800k), WooCommerce Tax 2.0★ (500k), ExactMetrics 2.5★ (300k), Mercado Pago for WooCommerce 3.9★ (100k) — same API.

**Other global marketplaces (policy pages; no category metrics collected)**
- **HubSpot:** listing requires "at least three active, unique installs" in production accounts unaffiliated with the developer, active within 30 days. Listings are manually reviewed by the Ecosystem Quality team — [HubSpot listing requirements](https://developers.hubspot.com/docs/apps/developer-platform/list-apps/listing-your-app/app-marketplace-listing-requirements)
- **monday.com:** "All new marketplace apps must be monetized by monday rather than an external monetization system." Pricing is seat-based or feature-based — [monday monetization](https://developer.monday.com/apps/docs/monetization), [monday plans & pricing](https://developer.monday.com/apps/docs/plans-and-pricing). monday's June 2024 pricing report gives example seat plans from $10/month (up to 5 seats) to $140/month (up to 120 seats) — [monday Developer Pricing Report (PDF)](https://dapulse-res.cloudinary.com/image/upload/v1718300307/remote_mondaycom_static/uploads/DiproBhowmik/App%20Pricing%20Document%20-%20Untapped/v2/monday.com_-_Developer_Pricing_Report_-_FINAL4_June_2024.pdf)

### Inferences
- **Atlassian** combines four things the client needs: businesses paying in USD, marketplace search distribution, billing handled by Atlassian, and a dated forced-change window (Connect end of support, Q4 2026). Concrete stale or low-rated paid incumbents exist in the Gantt, OpenAPI and Mermaid/Markdown niches.
- **Google Workspace** has the strongest raw demand signal: millions of installs on 2.5–3.4★ products. Low ARPU (€5/month), heavy free and education usage, and Google's OAuth verification are the trade-offs.
- **Shopify BR localization** is a real quality gap. Official ERP and carrier apps sit at 1–2.4★. But the 30k-store base is shrinking (−7%) and review counts are tiny, which suggests limited demand. Many BR Shopify stores are dropshippers using DSers and Areviews, per the top-apps list.
- **WordPress.org**: stale big plugins already have dominant active substitutes. A new plugin would have to fight 71k incumbents for freemium conversions. Not recommended.

### Gaps
- Chrome Web Store totals and per-category counts were not collected; only spot checks were made (see §2 and §5).
- No category-level metrics were collected for HubSpot, monday, Zoho, Wix, Webflow, Squarespace, Canva, Figma, Notion, Airtable, Zapier or Microsoft AppSource. Their pages are JS-heavy, and search was unavailable to find their stats pages.
- The Atlassian `deployment.connect` flag sometimes differed between API queries for the same app (e.g., "PlantUML, Swagger, drawio.xml, Mermaid" showed Connect in one query and Forge in another), so treat Connect/Forge labels as approximate.
- Workspace Marketplace "users" figures are the displayed install counters, not active users. I could not see review counts or reviews, which are loaded by JS.

---

## 5. 2025–2026 platform changes that force merchants or users to look for new apps (exact dates)

### Takeaway
The live, still-open windows in October 2026 are four:
1. **Nuvemshop NubeSDK:** delisting on 30 Sep 2026; progressive uninstall from **30 Oct 2026**.
2. **Atlassian Connect end of support:** Q4 2026.
3. **Atlassian Data Center:** new sales stopped 30 Mar 2026; end of life 28 Mar 2029.
4. **HubSpot classic CRM cards sunset:** 31 Oct 2026.

Shopify Scripts (30 Jun 2026) and Chrome MV2 (disabled 24 Jul 2025; Web Store removal 31 Aug 2026) have already passed, and their replacement demand was largely absorbed. Mercado Livre's March 2026 changes favour its own native tools.

### Cited Findings
- **Nuvemshop:**
  - 5 Jun 2026: NubeSDK is required for new homologation of script-injecting apps.
  - 30 Sep 2026: non-migrated apps are removed from the App Store (postponed from 30 Aug).
  - 30 Oct 2026: progressive uninstall begins.
  - Checkout already requires NubeSDK.
  - Source: [nuvemshop.dev – Prazo de adoção do NubeSDK](https://nuvemshop.dev/apps/admin/overview)
- **Shopify Scripts:** "April 15, 2026—Editing and publishing new Shopify Scripts will no longer be possible. June 30, 2026—All Shopify Scripts will cease to execute entirely." The replacement is Shopify Functions (discounts, shipping, payments). Changelog post dated April 9, 2026 — [Shopify changelog](https://shopify.dev/changelog/shopify-scripts-will-be-deprecated-on-june-30-2026)
- **Chrome Manifest V2 (official timeline, last updated 2026-09-09):**
  - June 3, 2024: phase-out begins.
  - March 31, 2025: MV2 disabled, with an option to re-enable.
  - **July 24, 2025:** with Chrome 138, MV2 is disabled for all users, and the enterprise policy is removed in Chrome 139.
  - **Aug 31, 2026:** "All remaining Manifest V2 extensions removed from the Chrome Web Store". Existing installs on Chrome 138 or earlier keep running but cannot update or be reinstalled.
  - Source: [Chrome MV2 timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline)
- Big MV2 extensions were absorbed by MV3 successors: uBlock Origin Lite has **21,000,000 users** (updated Oct 7, 2026), while the original uBlock Origin listing no longer renders item data — [uBO Lite](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh), [uBlock Origin](https://chromewebstore.google.com/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm). Hover Zoom+ has 300,000 users (updated Sep 10, 2026) — [Hover Zoom+](https://chromewebstore.google.com/detail/hover-zoom+/pccckmaobkjjboncdfnnofkonhgpceea)
- **Atlassian Connect end of support (blog dated March 17, 2025):**
  - Phase One, **Sep 17, 2025:** "all new apps published on Atlassian's Marketplace must be created on Forge".
  - Phase Two, **March 2026:** Connect-descriptor apps can no longer be updated.
  - Phase Three, **Q4 CY2026:** Connect enters end of support, meaning "use at your own risk". Atlassian "will message accordingly to customers on the Marketplace".
  - Source: [Atlassian blog](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps)
- **Atlassian Data Center (via search summary of Atlassian's page; not fetched):**
  - March 30, 2026: new customers can no longer buy DC subscriptions or DC Marketplace apps.
  - March 30, 2028: existing customers can no longer buy.
  - **March 28, 2029:** end of life; products go read-only.
  - Source: [Atlassian DC end of life](https://www.atlassian.com/licensing/data-center-end-of-life)
- **Atlassian revenue-share change (verified page):** Forge partners keep 84% and Connect partners 80% from 1 Apr 2026. From **1 Oct 2026**, Forge partners keep 83% and Connect and DC partners 75%. From 1 Jan 2026, partners receive 100% of Forge revenue up to $1M lifetime — [Atlassian pricing, payment and billing](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/)
- **HubSpot (via search summary; not fetched):** from June 16, 2025, no new Marketplace apps with Classic CRM cards can be listed. Existing apps must migrate to App Cards by **October 31, 2026** — [HubSpot changelog](https://developers.hubspot.com/changelog/deprecating-support-for-classic-crm-cards)
- **Microsoft Outlook add-ins:** legacy Exchange Online user identity and callback tokens "are no longer supported and turned off across all Microsoft 365 tenants". Use MSAL with nested app authentication — [Microsoft Learn FAQ](https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/faq-nested-app-auth-outlook-legacy-tokens). "Sharepoint Add-ins were deprecated and can no longer be sold on Microsoft Marketplace" — [Microsoft Learn – monetize add-ins](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/monetize-addins-through-microsoft-commercial-marketplace)
- **Google Apps Script (via search summary of Google's sunset page; not fetched):** the Rhino runtime stopped on Jan 31, 2026 (migration to V8 required), and `setAuthentication(clientId, signingKey)` sunset on June 1, 2026 — [Apps Script sunset schedule](https://developers.google.com/apps-script/guides/support/sunset)
- **Mercado Livre:**
  - From 18 Mar 2026, API price edits are blocked on items using native price automation — [ML docs](https://developers.mercadolivre.com.br/pt_br/automatizacoes-de-precos)
  - From March 2026, fee and logistics cost changes for items under R$79 and for Full (secondary source) — [Tecnospeed](https://blog.tecnospeed.com.br/tarifas-do-mercado-livre/)
  - DPP closed to new entrants in Q4 2026 — [ML DPP](https://developers.mercadolivre.com.br/pt_br/developer-partner-program)

### Inferences
- **Best-timed forced-demand window for a newcomer: Nuvemshop.** It is Brazilian and Portuguese-language, uninstalls start in 18 days, and new NubeSDK-native apps face little competition. Second: **Atlassian Connect end of support** (Q4 2026), combined with DC→Cloud migrations through 2029.
- **Shopify Scripts and Chrome MV2 are traps for 2026 entrants.** The deadlines have passed and Built-for-Shopify incumbents, or the MV3 successors of big extensions, already hold the demand.
- **HubSpot's CRM-card deadline mainly creates agency and dev-services work**, which needs contacts. Excluded.

### Gaps
- I could not confirm the date of Shopify's checkout.liquid Thank-you/Order-status upgrade for non-Plus stores.
- No WordPress platform policy changes for 2025–2026 were researched (search exhausted).
- No list of popular, abandoned MV2 extensions with 10k–500k users (the realistic replacement niche) could be compiled without search.
- I did not fetch Shopee or Nuvemshop API policy pages beyond NubeSDK.

---

## 6. Evidence of solo or small developers earning in each marketplace (verified vs self-reported)

### Takeaway
There are credible SELF-REPORTED solo outcomes on Google Workspace (Sync2Sheets: 1 founder, 0 employees, about $9k/month), Shopify (Analyzify: $12k MRR in 7 months) and Chrome ($12k–31k/year small extensions). The VERIFIED platform-level data are Shopify paying out more than $1B to developers in 2024 and ExtensionPay's own claim of only $800k earned by all its developers since 2021. I found no solo revenue data for Nuvemshop, Atlassian, WordPress or Mercado Livre tools.

### Cited Findings
- **Shopify (VERIFIED, company statement):** "merchants have more than 16,000 apps to choose from, and we paid out more than $1B to developers last year" (post dated April 24, 2025, so the payout figure refers to 2024) — [Shopify changelog](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share)
- **Google Workspace (SELF-REPORTED, Starter Story, May 7, 2024):**
  - Sync2Sheets (Notion↔Google Sheets), by Leandro Zubrezki of Buenos Aires: "$9,000 revenue/mo, 1 Founders, 0 Employees", started May 2021, 400+ paying customers.
  - "It took me 2 weeks between getting started and submitting to the store", after OAuth review.
  - Sources: [Starter Story – Sync2Sheets](https://www.starterstory.com/stories/sync2sheets-give-notion-the-superpowers-of-google-sheets), [Starter Story Chrome/extension list](https://www.starterstory.com/ideas/chrome-extension/success-stories)
- **Shopify (SELF-REPORTED, Starter Story):**
  - Analyzify: "$12K MRR in just 7 months"; 1 founder and 3 employees, Tallinn; story dated Nov 8, 2021 — [Starter Story – Analyzify](https://www.starterstory.com/stories/our-analytics-app-for-shopify-reached-12k-mrr-in-just-7-months)
  - Rush (order tracking): $20K/month; 2 founders and 9 employees; Apr 27, 2022 — [Starter Story – Rush](https://www.starterstory.com/stories/this-dropshipper-built-a-20k-month-shopify-order-tracking-app)
  - SuperLemon ($348K/year) found its idea by browsing every app in the 3,000+-app store "especially ones that had poor reviews", targeting at least $3k MRR. The founders cite "a friend who built a $20k/mo Shopify app without any employees" (anecdote).
  - Larger team examples: Growave $1.32M/year, TxtCart $1.02M/year.
  - Source: [Starter Story – Shopify app success stories](https://www.starterstory.com/ideas/shopify-app/success-stories)
- **Chrome (SELF-REPORTED, Starter Story):** Blurweb $18K/year (solo creator; [story](https://www.starterstory.com/stories/i-built-a-tool-that-helps-blur-sensitive-information-with-just-5)), T.LY $31.2K/year and Baxter $12K/year. GMass is the big outlier at $5.4M/year, with $200K MRR and a team — [Starter Story – Chrome extension success stories](https://www.starterstory.com/ideas/chrome-extension/success-stories)
- **Chrome payments platform (SELF-REPORTED aggregate):** "Developers have now made over $800,000" with ExtensionPay since 2021 — [ExtensionPay](https://extensionpay.com/)
- **WordPress commerce platform (SELF-REPORTED):** "3,000+ makers building and scaling with Freemius" — [Freemius](https://freemius.com/)
- **Atlassian (VERIFIED metadata, no revenue):** an individual vendor, "Toshihiro Sato", has paid cloud apps with 2,869 installs (Open API (Swagger) Integration) and 559 installs (Mermaid Integration, $30/year at 15 users) — [Atlassian API search "swagger"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=swagger&limit=50&withVersion=true), [Atlassian API search "mermaid"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=mermaid&limit=50&withVersion=true)
- **Mercado Livre tools (VERIFIED users and price, revenue unknown):** Avantpro has 100,000 CWS users at R$59.90/month — [CWS](https://chromewebstore.google.com/detail/avantpro-ml/jdefnfmbnchmnjkcknaadaddgjbgephh), [Avantpro](https://avantpro.com.br/)

### Inferences
- ExtensionPay's $800k across all its developers over about 5 years implies a median Chrome extension using it earns very little. Chrome monetization is winner-take-most, and distribution of a paid extension needs content or SEO beyond store search.
- Sync2Sheets is the closest analog to this client: a LatAm solo developer, a Workspace add-on built in about 2 weeks, an integration-type product and $9k/month.
- Shopify's payout averages about $62k per app per year ($1B ÷ 16k), but the distribution is extremely skewed (inference).

### Gaps
- No solo-developer revenue figures for Nuvemshop, Atlassian, WordPress, HubSpot, monday, Wix, Canva, Figma or Notion. Indie Hackers and Reddit could not be searched.
- Starter Story figures are self-reported and dated 2021–2024; current revenues are unknown.

---

## 7. Fees, approval timelines and policy risks per marketplace

### Takeaway
The cheapest economics for a newcomer are Nuvemshop (external billing, 0% GMV commission), Shopify (0% on the first $1M lifetime, then 15%), Atlassian Forge (100% of revenue up to $1M lifetime, then 83%), Wix (100% in year one, then 80%) and Microsoft (3%). Policy friction is highest at Google (OAuth verification; annual security assessment for restricted scopes), Atlassian (security requirements) and Mercado Livre (DPP closed, GMV threshold). Almost no marketplace publishes review SLAs.

### Cited Findings

| Marketplace | Fee / revenue share | Approval and policy facts |
|---|---|---|
| Nuvemshop | Partner billing: 0%. Nuvemshop billing: payment-method fees and invoice tax deducted. "não gera ... comissão sobre ... GMV". Sources: [help](https://atendimento.nuvemshop.com.br/pt_BR/parceiros-tecnologicos/como-eu-recebo-pelo-uso-do-meu-aplicativo-criado-na-nuvemshop), [docs](https://nuvemshop.dev/apps/publish/pricing-billing) | Homologation required; ERP, payment and shipping apps need a video demo checklist; NubeSDK mandatory for script apps; no SLA published ([docs](https://nuvemshop.dev/apps/publish/homologation/overview)). Merchant auto-pay is optional, which is a collection risk ([help](https://atendimento.nuvemshop.com.br/pt_BR/parceiros-tecnologicos/como-eu-recebo-pelo-uso-do-meu-aplicativo-criado-na-nuvemshop)) |
| Shopify | 0% on the first $1M of lifetime revenue (earnings before 2025 don't count), 15% above, aggregated per partner; effective June 16, 2025 ([changelog](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share)) | Review duration not verified |
| Atlassian | 100% of Forge revenue up to $1M lifetime (from Jan 1, 2026). After that, Forge 84%→83% (Oct 1, 2026), Connect 80%→75%, DC 75% ([Atlassian](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/)) | New apps must be Forge-only (Sep 17, 2025). "Runs on Atlassian" badge requires customer-controllable egress, verifiable through the Forge CLI ([Runs on Atlassian](https://developer.atlassian.com/platform/marketplace/runs-on-atlassian/)). A Marketplace Bug Bounty program with Bugcrowd exists ([bug bounty](https://developer.atlassian.com/platform/marketplace/marketplace-security-bug-bounty-program/)); whether it is mandatory for small paid apps was not confirmed |
| Chrome Web Store | One-time registration fee ([register](https://developer.chrome.com/docs/webstore/register)); CWS payments are deprecated, so billing must be external (e.g., ExtensionPay) | Policy risk for sites' ToS (e.g., scraping ML) |
| Google Workspace Marketplace | No marketplace billing observed: Sheets2GCal sells on its own site ([site](https://www.sheets2gcal.com/)) | Restricted-scope apps need annual re-verification and a security assessment ([Google Cloud help](https://support.google.com/cloud/answer/13463073)) |
| HubSpot | Not verified | At least 3 active unaffiliated installs needed to list; manual review ([HubSpot](https://developers.hubspot.com/docs/apps/developer-platform/list-apps/listing-your-app/app-marketplace-listing-requirements)) |
| monday.com | monday billing mandatory for new apps ([monday](https://developer.monday.com/apps/docs/monetization)); percentage not found | — |
| Wix | "In your first year, you receive 100% of all sales revenue. After that, you keep 80%", after a 2.5% transaction fee and sales tax; payout net 30 EOM ([Wix](https://dev.wix.com/docs/build-apps/launch-your-app/pricing-and-billing/about-monetizing-your-app)) | — |
| Canva | Premium Apps Program: Canva pays "based on how often your app is used"; grants for apps in development; Canva decides the access model ([Canva](https://www.canva.dev/docs/apps/premium-apps.md)). External payment links only where `canAcceptPayments` allows ([Canva](https://www.canva.dev/docs/apps/accepting-payments.md)) | Review duration "not practical ... to provide" ([Canva](https://www.canva.dev/docs/apps/app-review-process.md)) |
| Notion (templates) | "8% fee plus 40 cents per transaction"; payments through Stripe ([Notion](https://www.notion.com/help/selling-on-marketplace)) | Waitlist and approval needed |
| Microsoft Marketplace | "Microsoft charges a 3% standard store service fee" on transactable offers ([Microsoft](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/marketplace-commercial-transaction-capabilities-and-considerations)) | Add-ins are free to install and sold as SaaS offers, purchasable only with work or school accounts ([Microsoft](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/monetize-addins-through-microsoft-commercial-marketplace)) |
| Mercado Livre DPP | — | Closed in Q4 2026; Brazil needs US$2.5M monthly GMV and a security assessment of 65% or more ([ML](https://developers.mercadolivre.com.br/pt_br/developer-partner-program)) |

### Inferences
- With R$700, zero-upfront-fee marketplaces matter. Nuvemshop, Atlassian and Workspace have no listing fee observed. Chrome's one-time fee is small.
- Billing is the hidden constraint:
  - Atlassian and Shopify handle billing and pay in USD, which suits a Brazilian solo developer.
  - Nuvemshop external billing needs a Brazilian PSP (Pix, boleto) and the client's CNPJ/MEI invoicing. This is an assumption to verify with the client.
  - Chrome and Workspace need Stripe or Paddle-type billing.

### Gaps
- I did not verify: Shopify's partner registration fee, HubSpot's revenue share, monday's revenue share, Zoho, Webflow, Squarespace, Figma, Airtable and Zapier terms, or the exact Chrome fee amount (widely cited as US$5; unverified here).
- I did not verify approval timelines for any marketplace.
- I did not verify whether Atlassian pays out to Brazil-based individuals, or the tax-form requirements.
- I did not verify whether Google Calendar scopes are "sensitive" rather than "restricted". The fetched Calendar auth page lists scopes without a classification. My working assumption is sensitive (verification but no CASA assessment), which needs confirmation.

---

## 8. Ranking of marketplaces by demand-to-competition ratio for a newcomer

### Takeaway
For this client the ranking is: (1) Atlassian Cloud (Forge), (2) Nuvemshop, (3) Google Workspace Marketplace, (4) Shopify (Brazil-localized niche only), (5) Chrome Web Store (BR marketplace-seller tools), (6) Wix, monday, HubSpot and Canva (not measured), (7) Tray, (8) WordPress.org, (9) Mercado Livre's own ecosystem, (10) VTEX and Loja Integrada.

### Cited Findings
- Ratio inputs (see §§1–4 for sources):

  | Marketplace | Buyer base | Listings | Approx. buyers per listing |
  |---|---|---|---|
  | Nuvemshop | 126,358 live BR stores ([Store Leads](https://storeleads.app/reports/tiendanube/BR/top-stores)) | 647 apps (crawl) | ~195 stores; median app has 3 reviews |
  | Shopify | 3,143,979 live stores, +15% YoY, 80,600 Plus; that sentence was truncated in the fetch ([Store Leads](https://storeleads.app/reports/shopify)) | 16,000+ apps (Apr 2025) ([Shopify](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share)) | ~196 stores; category leaders have thousands of reviews |
  | Atlassian | 300,000+ customers ([Atlassian](https://www.atlassian.com/company)) | 6,623 cloud apps ([API](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&limit=5&sort=popularity)) | ~45 customers, but multi-seat organizations |
  | Tray | 29,663 stores ([Store Leads](https://storeleads.app/reports/tray/BR/top-stores)) | 738 apps, 552 of them ERP ([Tray](https://aplicativos.tray.com.br/)) | ~40 stores (~160 if ERP excluded); no ratings |
  | WooCommerce | 4,002,439 live stores, −10% YoY ([Store Leads](https://storeleads.app/reports/woocommerce)) | 71,295 WP plugins ([API](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[browse]=popular&request[per_page]=250)) | — |
  | Mercado Livre | — | DPP closed; native tools ([ML](https://developers.mercadolivre.com.br/pt_br/developer-partner-program)) | — |

### Inferences
- Ranked with reasons:

| Rank | Marketplace | Demand | Competition quality | Buyer power | Forced-change tailwind | Verdict |
|---|---|---|---|---|---|---|
| 1 | Atlassian Cloud (Forge) | Medium-high (paid niches with 1k–6k installs) | Weak in specific niches (stale Connect, 3–3.5★) | High (USD, per-seat) | Connect end of support Q4 2026; DC end of life 2029 | Best global fit |
| 2 | Nuvemshop | Medium (126k stores, +24%) | Very weak (median 3 reviews) | Low-medium (BRL SMBs) | NubeSDK uninstall from 30 Oct 2026 | Best Brazilian fit |
| 3 | Google Workspace | Very high (millions of installs) | Weak ratings but entrenched | Medium (edu, SMB, prosumer) | None in particular | Fast to build; low ARPU |
| 4 | Shopify (BR niche) | Low-medium (30k BR stores, −7%) | Very weak (1–2.4★ official apps) | Medium | Scripts already passed | Niche only |
| 5 | Chrome (BR seller tools) | High (Avantpro 100k) | Strong leader | Low-medium | ML fee changes | Crowded, ToS risk |
| 6 | Wix, monday, HubSpot, Canva | Unmeasured | Unmeasured | Medium-high | HubSpot cards (services) | Need data |
| 7 | Tray | Medium (+32%) | Unknown (no ratings) | Low-medium | — | No discovery signal |
| 8 | WordPress.org | High | Saturated (71k plugins) | Mixed | — | Avoid |
| 9 | Mercado Livre ecosystem | High | ML native tools; DPP closed | Low-medium | Changes favour ML | Avoid except via Chrome |
| 10 | VTEX, Loja Integrada | Low (2.7k stores; −29%) | — | VTEX enterprise | — | Avoid |

### Gaps
- Per-listing ratios are crude. App counts differ by date: Shopify's 16k is from Apr 2025. Store Leads counts differ from platform claims (Nuvemshop's 180k vs 126k).

---

## 9. Candidate app ideas: records, 1–5 scores and exclusions

### Takeaway
Eight candidates survive the constraints; two of them (C5, C8) are kept only as weak options. The strongest are C1, a Forge Gantt/timeline app for Jira replacing stale Connect Gantt apps, and C2, a Google Sheets ⇄ Google Calendar sync add-on. The best Brazil-native option is C3, a NubeSDK-native wholesale/B2B app for Nuvemshop, which has very low competition but thin willingness-to-pay evidence. AI-led ideas are excluded.

### Cited Findings
- All metrics in the records below are cited inline, and come from the sources in §§1–7.

### Inferences
Scores run 1–5, where 5 is best. Low saturation and low risk are scored so that 5 means least saturated and least risky.

**C1. "Forge Gantt & Timeline for Jira" (Runs on Atlassian; drop-in replacement for stale Connect Gantt apps)**
- **One-liner:** a Forge-native Gantt chart for Jira issues, with dependencies (issue links), baselines and drag-to-reschedule, sold through Atlassian billing.
- **Buyer and count:** Jira Cloud teams (Atlassian has 300,000+ customers, all products). The top seven Gantt apps (BigGantt, WBS, Structure Gantt, Portfolio by HeroCoders, GanttTable, Gantt Cloud, Gantt-Chart) sum to about 24.8k installs, an upper bound with possible overlap — [API search "gantt"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=gantt&limit=50&withVersion=true)
- **Pain and evidence:** incumbents are poorly rated (BigGantt 3.46★ from 273 reviews; WBS Gantt-Chart 3.48★ from 160; Gantt-Chart for Jira 3.45★ from 129; Gantt Cloud 2.96★ from 85). Several are on Connect with last releases in 2019–2022, and Connect enters end of support in Q4 2026 with customer messaging on the Marketplace — [Atlassian blog](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps)
- **Competitors and pricing (live API, annual):** BigGantt $313.5 at 15 users and $2,090 at 100. WBS Gantt-Chart $198 / $1,320. Structure Gantt (Tempo) $219 / $1,460. Gantt-Chart for Jira $180 / $1,200. Gantt Cloud $67.5 / $450. Revenue figures are not public.
- **Weaknesses:** low ratings; stale Connect codebases; high prices.
- **Demand signals:** about 24.8k installs across the leading apps; 95 search results.
- **Acquisition:** Marketplace search for "gantt"; a "Runs on Atlassian" badge; SEO comparison pages ("BigGantt alternative", "WBS Gantt migration"); Atlassian Community answers. No contacts needed.
- **Build complexity:** medium. Forge Custom UI, the Jira REST API and an open-source Gantt library; MVP in 2–4 weeks with AI.
- **Time to first revenue:** about 6–10 weeks (build, Atlassian listing, trial) — estimate.
- **Path to US$5k/month:** about 100–200 paying sites at $300–600/year (inference). Forge keeps 100% up to $1M lifetime — [Atlassian](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/)
- **Risks:** Jira's native Timeline and Plans; strong vendors (Appfire, Tempo); Atlassian security review; per-user free tier under 10 users; unverified payout logistics to Brazil.
- **Scores:** WTP 5 · Low saturation 3 · Purchasing power 5 · Distribution 4 · Buildability 3 · Speed 3 · Low risk 3 = **26/35**. No exclusion flags.

**C2. "Sheets ⇄ Calendar Sync" (Google Workspace add-on)**
- **One-liner:** turn spreadsheet rows (or Form responses) into Google Calendar events and keep them in two-way sync, with recurring events, attendees, colours and conflict-safe updates.
- **Buyer and count:** schools, SMB operations staff, event and shift planners. Incumbents show Sheets2GCal 8M+, Calendar Events Creator 3M+ and Form to Calendar 1M+ installs, roughly 12M+ cumulative with overlap — [Sheets2GCal](https://workspace.google.com/marketplace/app/sheets2gcal/137564231775), [Calendar Events Creator](https://workspace.google.com/marketplace/app/calendar_events_creator/101859618418), [Form to Calendar](https://workspace.google.com/marketplace/app/form_to_calendar/210797006292)
- **Pain and evidence:** the incumbents are rated 3.2★, 2.5★ and 3.4★ despite being updated in 2026 (Aug 10 and May 28, 2026).
- **Competitors and pricing:** Sheets2GCal is free up to 200 updates/day, then €5/month, €48/year, €59/year or €299/year — [Sheets2GCal](https://www.sheets2gcal.com/). Others' prices were not collected.
- **Analog revenue (SELF-REPORTED):** Sync2Sheets, a solo Workspace add-on built in 2 weeks, reports $9k/month — [Starter Story](https://www.starterstory.com/stories/sync2sheets-give-notion-the-superpowers-of-google-sheets)
- **Weaknesses:** low ratings; usage caps.
- **Demand signals:** installs as above.
- **Acquisition:** Workspace Marketplace search; SEO ("google sheets to google calendar"); templates; YouTube how-tos.
- **Build complexity:** low (Apps Script or a Workspace add-on); about 1–2 weeks.
- **Time to first revenue:** about 3–8 weeks, depending on OAuth verification time (unverified).
- **Path to US$5k/month:** about 1,000 subscribers at €5/month, or about 200 business plans at €299/year (inference).
- **Risks:** Google adds native features; OAuth verification delays; low ARPU and education-heavy users; reviews aren't verified, so incumbents' poor ratings may partly reflect free users.
- **Scores:** WTP 3 · Low saturation 3 · Purchasing power 3 · Distribution 4 · Buildability 5 · Speed 4 · Low risk 3 = **25/35**. No exclusion flags. Avoid Gmail and Drive restricted scopes.

**C3. "Atacado & B2B para Nuvemshop" (NubeSDK-native)**
- **One-liner:** wholesale mode for Nuvemshop: customer groups (CNPJ approval), price tables per group, minimum order or quantity, and grade (size/colour matrix) ordering, built on NubeSDK slots.
- **Buyer and count:** BR apparel and beauty brands. Nuvemshop has 126,358 live BR stores, 38.5% of them apparel (about 48.6k by inference) — [Store Leads](https://storeleads.app/reports/tiendanube/BR/top-stores)
- **Pain and evidence:** only 3 B2B-related apps with 15 reviews in total. Compre por Grade Pro – Huapps is 4.9 (10) at R$59.90/month, Backchannel (3) and Solicitar Orçamento (2) — [Recursos extras](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/recursos-extras)
- **Forced demand:** legacy script apps are delisted (30 Sep 2026) and progressively uninstalled (30 Oct 2026) — [nuvemshop.dev](https://nuvemshop.dev/apps/admin/overview)
- **Competitors' weaknesses:** too few reviews to judge.
- **Acquisition:** Nuvemshop app store search in Portuguese; SEO ("atacado nuvemshop", "vender no atacado e varejo"); YouTube; Nuvemshop community.
- **Build complexity:** medium. Pricing logic must be enforced at checkout, and NubeSDK slot limits are unknown.
- **Time to first revenue:** about 4–8 weeks, depending on the homologation SLA (unknown).
- **Path to US$5k/month:** about 450 stores at R$59.90/month (inference), which is about 0.9% of apparel stores.
- **Risks:** Nuvemshop may have or add native B2B (unverified); low proven willingness to pay; collection friction ("pagamento manual" unless the merchant enables auto-pay, if Nuvemshop billing is used); BRL buyers.
- **Scores:** WTP 2 · Low saturation 5 · Purchasing power 2 · Distribution 4 · Buildability 3 · Speed 3 · Low risk 3 = **22/35**. No exclusion flags.

**C4. "Busca + Filtros Inteligentes para Nuvemshop" (NubeSDK)**
- **One-liner:** faceted search and filters by size, colour, price and stock, with synonyms ("tênis/sapatilha"), for apparel-heavy stores.
- **Evidence:** 6 search/filter apps with 24 reviews in total. HintUP is 4.5 (18) at R$99, and Busca Inteligente 5.0 (4) — [Marketing](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/marketing)
- **Buyers:** the same 126k-store base.
- **Acquisition:** app store search and SEO.
- **Build:** medium-high (indexing through the API plus storefront slot UI).
- **Risks:** NubeSDK may not allow replacing the native search page (unverified); native theme filters may exist (unverified).
- **Scores:** WTP 2 · Low saturation 5 · Purchasing power 2 · Distribution 4 · Buildability 2 · Speed 2 · Low risk 2 = **19/35**.

**C5. "Docs-as-Code Macros for Confluence" (Forge: Mermaid + PlantUML + OpenAPI + Markdown)**
- **One-liner:** one Forge app that renders Mermaid, PlantUML, OpenAPI/Swagger and Markdown from page source or Git URLs, positioned as safe from Connect end of support.
- **Evidence:**
  - Mermaid incumbents: Stratus (Connect, last release 2023), 4.02★, 6,302 installs, $60/year at 15 users. Mermaid Chart (free), 2.94★, 4,105. Atlassian Labs free viewer, 2.99★, 7,600.
  - OpenAPI incumbents are Connect and stale since 2024 (2,869 and 1,211 installs).
  - Sources: [API "mermaid"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=mermaid&limit=50&withVersion=true), [API "swagger"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=swagger&limit=50&withVersion=true)
- **Strong existing competitor:** Just Add+ (Forge, paid), 4.25★, 8,072 installs.
- **Build:** low (days).
- **Revenue ceiling:** low, at $30–60/year for 15 users and $200–400 for 100 users.
- **Scores:** WTP 3 · Low saturation 2 · Purchasing power 5 · Distribution 4 · Buildability 5 · Speed 4 · Low risk 2 = **25/35**, but with a low revenue ceiling. Better as a quick second product, or as a portfolio app beside C1.

**C6. "Kit Brasil para Shopify" (Correios / Melhor Envio labels + Bling/Tiny NF-e sync)**
- **Evidence:** Bling 2.4★ (5), Olist Tiny 1.6★ (10), Correios SIGEP 1.5★ (14), Correios SEDEX PAC 3.6★ (79), Melhor Envio "Envios" 1.0★ (4) — see the [Shopify searches](https://apps.shopify.com/search?q=correios) in §4.
- **Buyer count:** 30,336 BR Shopify stores (−7% YoY), of which 2,794 ship by Correios — [Store Leads](https://storeleads.app/reports/shopify/BR/top-stores)
- **Pricing evidence:** Notasy from $5/month; Frenet free to install.
- **Build:** medium-high (ERP edge cases, carrier contracts).
- **Scores:** WTP 2 · Low saturation 4 · Purchasing power 3 · Distribution 3 · Buildability 2 · Speed 3 · Low risk 3 = **20/35**.

**C7. "Margem ML 2026" Chrome extension (per-listing margin after the March 2026 fee and Full changes, plus listing diagnostics)**
- **Evidence:** ML's March 2026 fee model is based on weight, cubage and price ([Tecnospeed](https://blog.tecnospeed.com.br/tarifas-do-mercado-livre/)). Avantpro has 100k users at R$59.90/month ([CWS](https://chromewebstore.google.com/detail/avantpro-ml/jdefnfmbnchmnjkcknaadaddgjbgephh), [Avantpro](https://avantpro.com.br/)). The existing calculator extension is stale, with 917 users and a 2023 update ([CWS](https://chromewebstore.google.com/detail/calculadora-de-pre%C3%A7o-merc/ehdoppainepibpodfamimaofmemenofl)).
- **Acquisition:** CWS search in Portuguese, YouTube and TikTok content, ML seller groups (low-contact).
- **Risks:** crowded (Avantpro, Hunter Spy 9k, Cargoos 5k, GoSmarter, Nubimetrics); ML ToS and DOM changes; ML native tools.
- **Scores:** WTP 4 · Low saturation 2 · Purchasing power 3 · Distribution 3 · Buildability 4 · Speed 4 · Low risk 2 = **22/35**.

**C8. "Lucro Real por Pedido" for Nuvemshop (API-only, so exempt from NubeSDK)**
- **Evidence:** the analytics category has 28 apps with Escalafy 5.0 (150), Dash Analytics 5.0 (107), Nuvem Stats 4.9 (74), Prax 5.0 (50), and "Lucro: custos e preço de venda" 5.0 (5) — [Estatísticas](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/estatisticas). API-only apps are exempt from NubeSDK — [nuvemshop.dev](https://nuvemshop.dev/apps/admin/overview)
- **Scores:** WTP 3 · Low saturation 2 · Purchasing power 2 · Distribution 4 · Buildability 4 · Speed 4 · Low risk 4 = **23/35**. Moderately crowded already.

**Score table**

| # | Candidate | WTP | Low sat. | Buyer power | Distribution | Build | Speed | Low risk | Total | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Forge Gantt for Jira | 5 | 3 | 5 | 4 | 3 | 3 | 3 | **26** | – |
| C2 | Sheets ⇄ Calendar add-on | 3 | 3 | 3 | 4 | 5 | 4 | 3 | **25** | – |
| C5 | Confluence docs-as-code macros | 3 | 2 | 5 | 4 | 5 | 4 | 2 | **25** | low revenue ceiling |
| C8 | Nuvemshop profit dashboard | 3 | 2 | 2 | 4 | 4 | 4 | 4 | **23** | – |
| C3 | Nuvemshop Atacado/B2B (NubeSDK) | 2 | 5 | 2 | 4 | 3 | 3 | 3 | **22** | verify native B2B |
| C7 | ML margin Chrome extension | 4 | 2 | 3 | 3 | 4 | 4 | 2 | **22** | ToS risk |
| C6 | Kit Brasil for Shopify | 2 | 4 | 3 | 3 | 2 | 3 | 3 | **20** | – |
| C4 | Nuvemshop search and filters | 2 | 5 | 2 | 4 | 2 | 2 | 2 | **19** | verify NubeSDK slots |

**Excluded or flagged under the constraints**
- **AI-wrapper, excluded:**
  - Shopify "ChatGPT Ads", 2.3★ (19) — [Shopify search "pix"](https://apps.shopify.com/search?q=pix)
  - Workspace "GPT for Sheets™ and Docs™", 4.8, 7M+ — [Workspace search "crm"](https://workspace.google.com/marketplace/search/crm)
  - Nuvemshop "Performa.AI – A infraestrutura de IA" — [Nuvemshop store](https://www.nuvemshop.com.br/loja-aplicativos-nuvem)
  - AI auto-answer bots for ML questions.
- **Needs contacts or services:** HubSpot classic-CRM-card migration work (deadline Oct 31, 2026); Atlassian DC→Cloud migration consulting.
- **Enterprise sale:** VTEX apps (2,745 BR stores).
- **ToS or legal:** scraping-heavy ML/Shopee spy tools (C7 is borderline); NF-e emission (fiscal liability, A1 certificate handling).

### Gaps
- Willingness to pay for C3 and C4 rests on 1–2 thin competitors. A 2-week smoke test (landing page, ads, waitlist) is needed before building.
- Approval timelines (Atlassian, Google OAuth, Nuvemshop homologation) were not verified, so time-to-revenue figures are estimates.
- Search volume and Google Trends were not collected (search budget exhausted).

---

## 10. Top 2 candidates, why, and the "traps"

### Takeaway
**Top 1: C1, a Forge Gantt/Timeline for Jira.** It has the highest proven willingness to pay ($180–2,090/year per site), USD business buyers, Atlassian-handled billing, 0% revenue share up to $1M lifetime, and incumbents at 3–3.5★, several on Connect, which reaches end of support in Q4 2026.

**Top 2: C2, a Sheets ⇄ Calendar sync add-on.** It has massive demand (12M+ cumulative installs across 2.5–3.4★ incumbents), the cheapest and fastest build, and a proven solo analog (Sync2Sheets, $9k/month, self-reported).

**Brazil-first alternate: C3, Atacado/B2B for Nuvemshop on NubeSDK.** Validate it first, because willingness-to-pay evidence is thin.

### Cited Findings
- **C1 and C5 evidence:**
  - Gantt incumbents' ratings and prices — [API search "gantt"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=gantt&limit=50&withVersion=true)
  - Connect end-of-support phases — [Atlassian blog](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps)
  - 100% of Forge revenue up to $1M — [Atlassian billing](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/)
- **C2 evidence:**
  - Incumbents' installs and ratings — [Workspace search "calendar booking"](https://workspace.google.com/marketplace/search/calendar%20booking), [Sheets2GCal listing](https://workspace.google.com/marketplace/app/sheets2gcal/137564231775)
  - Pricing — [Sheets2GCal](https://www.sheets2gcal.com/)
  - Solo analog — [Starter Story – Sync2Sheets](https://www.starterstory.com/stories/sync2sheets-give-notion-the-superpowers-of-google-sheets)
- **Traps (popular-sounding but saturated or unworkable):**
  1. **Shopify Scripts→Functions "migration" apps.** The deadline passed on June 30, 2026 ([Shopify](https://shopify.dev/changelog/shopify-scripts-will-be-deprecated-on-june-30-2026)), and incumbents are entrenched: ETP Sort Hide Payment Methods 5.0 (571), HidePay 4.8 (392), Melon MOQ 5.0 (385) — [Shopify search](https://apps.shopify.com/search?q=melhor+envio)
  2. **Chrome MV2-replacement clones of famous extensions.** MV2 was disabled on Jul 24, 2025 and the remaining listings were removed on Aug 31, 2026 ([Chrome](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline)). Successors already dominate: uBO Lite 21M users ([CWS](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh)) and Hover Zoom+ 300k ([CWS](https://chromewebstore.google.com/detail/hover-zoom+/pccckmaobkjjboncdfnnofkonhgpceea)).
  3. **Mercado Livre repricers.** API price edits have been blocked on natively automated items since 18 Mar 2026 ([ML](https://developers.mercadolivre.com.br/pt_br/automatizacoes-de-precos)), and the DPP is closed with a US$2.5M GMV bar ([ML](https://developers.mercadolivre.com.br/pt_br/developer-partner-program)).
  4. **NF-e emitter apps.** ML has a native Faturador with IBS/CBS ([ML](https://developers.mercadolivre.com.br/pt_br/configuracoesibscbs)), Bling dominates on Nuvemshop with 469 reviews ([Nuvemshop](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/bling)), and the fiscal and certificate complexity is high.
  5. **Gmail mail merge and email add-ons.** Leaders include YAMM (16M+), Mail Merge (12M+) and Mailmeteor (7M+) ([Workspace](https://workspace.google.com/marketplace/search/mail%20merge)). GMass reports $5.4M/year ([Starter Story](https://www.starterstory.com/ideas/chrome-extension/success-stories)). Restricted Gmail scopes require annual security reassessment ([Google](https://support.google.com/cloud/answer/13463073)).
  6. **Reviews apps.** On Shopify Brazil, Judge.me runs on 4,998 BR stores ([Store Leads](https://storeleads.app/reports/shopify/BR/top-stores)). On Nuvemshop there are 36 review apps, led by Lily Reviews with 411 reviews (crawl).
  7. **WhatsApp apps on Nuvemshop.** There are 68 apps with 3,953 reviews; WhatsApp Marketing alone has 1,003 ([Comunicação](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/comunicacao)).
  8. **Replacing "abandoned" WordPress plugins.** Limit Login Attempts (300k installs, last updated 2023) is already displaced by Limit Login Attempts Reloaded (1M installs, 4.8★), Wordfence (5M) and Loginizer (1M) ([WP API](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[browse]=popular&request[per_page]=250)).
  9. **Atlassian planning poker and time tracking.** Searches return 1,076 and 2,782 results respectively, and Tempo Timesheets has 26,369 installs ([API](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=planning%20poker&limit=50&withVersion=true)).
  10. **A Mermaid-only Confluence macro.** Atlassian Labs offers a free viewer (7,600 installs), Just Add+ is a strong Forge competitor (8,072 installs), and paid prices run about $30–60/year for 15 users ([API](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&text=mermaid&limit=50&withVersion=true)).
  11. **A me-too ML spy or analytics Chrome extension.** Avantpro leads with 100k users at R$59.90/month, ahead of Hunter Spy (9k) and Cargoos (5k) ([CWS](https://chromewebstore.google.com/detail/avantpro-ml/jdefnfmbnchmnjkcknaadaddgjbgephh)).
  12. **Tray, Loja Integrada and VTEX app stores.** Tray shows no ratings or installs and 552 of its 738 apps are ERP connectors ([Tray](https://aplicativos.tray.com.br/)). Loja Integrada fell 29% YoY ([Store Leads](https://storeleads.app/reports/lojaintegrada/BR/top-stores)). VTEX is enterprise, with 2,745 BR stores ([Store Leads](https://storeleads.app/reports/vtex/BR/top-stores)).
  13. **Chrome extensions as the main business.** ExtensionPay's developers have earned only $800k in aggregate since 2021 ([ExtensionPay](https://extensionpay.com/)).

### Inferences
- **Why C1 first.** It is the only candidate where every hard constraint scores well at once: proven willingness to pay with list prices, business buyers in USD, marketplace distribution with no contacts, and a dated forced-change tailwind.
  - Its weaknesses are a longer build (2–4 weeks) and big-vendor competition.
  - Suggested mitigation: launch a narrow MVP (read-only Gantt plus dependencies plus CSV/PNG export). Target customers of stale Connect Gantt apps through comparison SEO.
  - Optionally ship C5 as a quick second Forge app to learn the Atlassian review process.
- **Why C2 second.** It is the fastest to first revenue (about 1–2 weeks to build) and has the strongest raw demand. The R$700 budget covers a domain and landing page plus a small Google Ads test on "sheets to calendar" keywords. Its weaknesses are lower ARPU and Google's verification process.
- **Brazil-first path.** Nuvemshop's NubeSDK purge (Oct 30, 2026 uninstall) is the most time-sensitive Brazilian opportunity, but buyer purchasing power and willingness-to-pay evidence are weaker.
  - Recommended approach: a 1–2 week validation of C3 (or of whichever niche loses apps in the purge) before building. Use a Portuguese landing page, the R$700 ads test, and a direct check with Nuvemshop partner support (SLA up to 1 hour) on native B2B features and NubeSDK slot capabilities.

### Gaps
- I did not verify approval SLAs (Atlassian, Google OAuth, Nuvemshop homologation), Atlassian payouts to Brazil, Calendar scope sensitivity, or whether Nuvemshop has native B2B or faceted search. These are the first things to confirm before committing.
- No Google Trends or keyword-volume data was collected, because the search budget ran out.
