# Brazil's emerging selling platforms: seller-tool gaps for a solo developer (data collected 2026-10-12)

*Method note: the current date is 2026-10-12. "Crawl" means I fetched it myself that day.*

*TikTok Shop App Store (BR):*
- *I rendered `seller-br.tiktok.com/appstore/br/` in headless Chrome (Playwright with `--no-sandbox`) and captured the store's own JSON API, `/api/v2/open/bso/portal/service/search`.*
- *I paged through "All apps" and opened about 100 app detail pages.*
- *I estimated app creation dates by decoding the top 32 bits of each `service_id` as a Unix timestamp. ByteDance IDs embed the creation second this way. This is an inference, not a published field.*

*Other sources:*
- *TikTok Partner Center docs: the public `partner.tiktokshop.com/api/v1/document/detail` endpoint.*
- *Shopee Open Platform docs: the `open.shopee.com/opservice/api/v1/developer_guide/detail` endpoint.*
- *YouTube search pages (titles and view counts), Google Autocomplete (hl=pt-BR, gl=br), and Reclame Aqui (one page before a bot check blocked further queries).*
- *About 14 WebSearch calls.*

*Blocked or not reached:*
- *Momentum Works' report and Reclame Aqui's per-term searches were blocked by Cloudflare or bot checks. Numbers from them come from search summaries only and are flagged.*
- *Mojeek returned 403. I fetched no Facebook groups.*

*Round-1 material read first:*
- *[[Ranking]], [[Armadilhas e ideias mortas]] and [[marketplace_gaps]].*
- *Round 1 killed or trapped these: NF-e emitter apps, the NFS-e Nacional emitter, ML repricers, ML spy extensions, and WhatsApp apps on Nuvemshop.*
- *Round 1 left these conditional: the "Margem ML" and "Lucro real Nuvemshop" ideas.*
- *Anything below that touches those ideas is flagged, with the new evidence that justifies looking again.*

---

## 1. TikTok Shop Brasil: launch, sellers and GMV

### Takeaway
TikTok Shop opened in Brazil on 8 May 2025. By its first anniversary in May 2026, average daily GMV per month had grown 102×, and live-stream GMV 161×. TikTok publishes multiples, not absolutes. A third-party estimate (unverified) puts H1 2026 GMV at about R$5.3 bn across about 110k stores and 2.3 M active affiliate creators. On 15 July 2026, TikTok raised fees for items under R$50 from 6% to 10% plus R$4, and for items of R$50 or more from 6% + R$4 to 6% + R$6. Sellers with money are clearly arriving. Whether the tool ecosystem is still "immature" is a different question, answered in §2.

### Cited Findings
- The shop function was released in Brazil on Thursday 8 May 2025 with a gradual rollout. Live shops were included — [Banda B / Folhapress, 2025-05-08](https://www.bandab.com.br/nacional/tiktok-shop-comeca-operar-brasil/amp/)
- **Official first-year figures (TikTok newsroom, 2026-06-04):**
  - Average daily GMV per month grew 102× since launch.
  - The average number of active affiliate creators (those with at least one sale per day) grew 46×.
  - In an in-app survey of 17,000 users, 57.8% complete purchases inside TikTok Shop after discovering a product on TikTok.
  - From May 2025 to May 2026, daily lives grew 20× and live daily GMV per month grew 161×. Top live categories are cosmetics and kitchen.
  - Riachuelo had 130k+ orders in 12 months. Natura ran 52k lives in 2025, 60% of them by its consultants.
  - Source: [TikTok Newsroom](https://newsroom.tiktok.com/tiktok-shop-cresce-102-vezes-em-seu-primeiro-ano-no-brasil?lang=pt-BR)
- 134 million users on the platform in Brazil (headline, 2026-06-02) — [Central do Varejo](https://centraldovarejo.com.br/tiktok-shop-completa-um-ano-no-brasil-com-gmv-102-vezes-maior-e-134-milhoes-de-usuarios-na-plataforma/?amp=1)
- **Third-party estimate (UNVERIFIED, search summary only; the page was Cloudflare-blocked on 2026-10-12):**
  - H1 2026 GMV of about R$5.3 bn (about US$1.0 bn), and June 2026 monthly GMV of R$1.58 bn.
  - 110,200 stores and 2.3 M influencers active in H1 2026.
  - Based on Momentum's own Tabcut data, not TikTok's.
  - Source: [Momentum Works – TikTok Shop in Brazil H1 2026](https://momentum.asia/insights/detail/tiktok-shop-in-brazil-h1-2026)
- **Fee change effective 15 July 2026:**
  - Below R$50: 10% + R$4 per item (was 6% + R$4).
  - From R$50: 6% + R$6 per item (was 6% + R$4).
  - The band is decided by the price after seller-funded discounts. Platform-funded discounts don't count.
  - The Shipping Fee Program charges a 6% service fee capped at R$50 per product.
  - Source: [Economic News Brasil, 2026-09-30](https://economicnewsbrasil.com.br/2026/09/30/taxas-tiktok-shop-black-friday-lojistas/); same figures in [Seu Crédito Digital, 2026-07-11](https://seucreditodigital.com.br/shopee-muda-regras-tiktok/)
- Black Friday 2026: R$100 million in coupons, with discounts of up to 70% — [Economic News Brasil, 2026-09-30](https://economicnewsbrasil.com.br/2026/09/30/taxas-tiktok-shop-black-friday-lojistas/). A headline on Central do Varejo says the campaign runs from 27 Oct to 12 Dec 2026 — [Central do Varejo, page dated 2026-09-24](https://centraldovarejo.com.br/?p=46184)

### Inferences
- TikTok Shop BR is real money and growing fast. Two of its seller patterns differ from ML and Shopee: creator-affiliate commissions and live commerce. If the estimate is right, about 110k stores is roughly the size of Nuvemshop's 126k live BR stores from round 1. That is a buyer pool large enough for a niche SaaS.
- The July 2026 fee change hit low-ticket items (under R$50) hardest. It created a burst of demand for "lucro real" calculators. §2–§3 show that this demand was met within weeks.

### Gaps
- TikTok has published no official absolute GMV or seller count for Brazil. The 110,200-store and R$5.3 bn figures are unverified third-party estimates.
- I did not fetch the official TikTok Seller Academy fee page; the fee figures come from two consistent secondary outlets.

---

## 2. TikTok Shop Partner Center / App Store: is it open to developers in Brazil, and what does it require?

### Takeaway
Yes. A Brazil-specific App Store is live at `seller-br.tiktok.com/appstore/br`, and an ISV can list a public app with external billing.

Listing as an ISV takes four things:
- **A registered company:** business license, registration number, owner ID and possibly UBO documents. A CPF won't do, and MEI can't legally cover programming.
- **A registration review**, then a language/listing review and an app review.
- **Sandbox testing.**
- **A compliance review, case by case**, for markets other than the US and UK. It can take 3+ weeks.

The ecosystem is **not immature anymore**. On 2026-10-12 the BR store listed **297 apps**. About 57% of the apps I captured were created in 2026, and 127 in April–August 2026 alone. Many are solo-dev or AI-built; one listing's developer name is literally "claude code". The gold rush has already happened.

### Cited Findings
- **The BR store is live.** The store's region API lists Brazil as a local market, with full URL `https://seller-br.tiktok.com/appstore/br` — [region API, 2026-10-12](https://seller-br.tiktok.com/api/v1/open/bso/common/get_region_info)
  - The BR store home shows these categories: Catalog, Content Management, Creator Collaborations, Customer Engagement, Customer Service, E-commerce Management, Finance, Marketing, Merchandising and Shipping & Fulfillment.
  - It shows 14 "popular platforms" (Shopify, Mercado Shops, WooCommerce, Nuvem Shop, Loja Integrada, Tray, VTEX and others) and one badge, "Free Sample Invoicing".
  - Source: [TikTok Shop App Store BR, rendered 2026-10-12](https://seller-br.tiktok.com/appstore/br/)
- "297 app(s) found in All apps" — [BR App Store search page, rendered 2026-10-12](https://seller-br.tiktok.com/appstore/br/search?category_id=1&dtc=&fromRecommendation=&page=1&sort=3)
- **My crawl:** 273 unique apps were captured. The listing order shifts between pages, so about 24 were missed. Main category tags (one app can carry several):

  | Category tag | Apps |
  |---|---|
  | E-commerce Management | 120 |
  | Connectors | 49 |
  | ERP | 38 |
  | Shipping & Fulfillment | 27 |
  | Catalog | 26 |
  | Product Listing | 25 |
  | OMS/WMS | 24 |
  | Finance | 22 |
  | Customer Service | 21 |
  | Multi-Channel | 21 |
  | Accounting | 20 |
  | Creator Collaborations | 20 |
  | Analytics & Reporting | 17 |
  | Marketing | 17 |
  | Video Shopping | 17 |
  | Content Management | 17 |
  | Dropshipping | 7 |
  | Print on Demand | 5 |
  | Merchandising | 3 |
  | Optimization | 3 |
  | Returns | 1 |
  | Customer Reviews | 1 |
  | Customer Engagement | 1 |

  Source: [service/search API via the store page, 2026-10-12](https://seller-br.tiktok.com/appstore/br/search?category_id=1&page=1)
- **Arrival curve (inferred from service_id timestamps):**

  | Period | Apps created |
  |---|---|
  | Before 2025 | 26 |
  | 2025 | 90 (peak Mar–Jun: 14, 10, 11, 10) |
  | Jan–Oct 2026 | 157 |

  - 2026 by month: Jan 7, Feb 4, Mar 14, **Apr 25, May 17, Jun 23, Jul 32, Aug 30**, Sep 3, Oct 2.
  - Two apps created on 2026-10-02 (TF Collab) and 2026-10-06 (Desh) were already listed on 2026-10-12.
  - Source: same crawl. Examples: [TF Collab](https://seller-br.tiktok.com/appstore/br/7691909941623555861), [Desh](https://seller-br.tiktok.com/appstore/br/7693406175647893268)
- One reconciliation app's developer is named "claude code": "Charme Marketplace Reconciliation | by claude code", created 2026-05-22 — [listing](https://seller-br.tiktok.com/appstore/br/7642635725993248530). An individual is also named as the developer of [Gaia Creator (Gabriel Mello)](https://seller-br.tiktok.com/appstore/br/7644811643152008981) and [MarketDock (Renan Santos)](https://seller-br.tiktok.com/appstore/br/7651800144350136080).
- **No installs or reviews are shown.** BR listings show no install counts, ratings or reviews. This was checked on about 100 detail pages and in the detail API, `/api/v2/open/bso/portal/service/detail` — e.g., [Bling listing](https://seller-br.tiktok.com/appstore/br/7488656928959235846)
- **External billing is allowed.** The store disclaimer says: "Some partners may charge users fees for providing services, and these fees will be paid directly to the partner organization. TikTok Shop doesn't determine service pricing" — [any BR listing, e.g., UpSeller](https://seller-br.tiktok.com/appstore/br/7362953095749388037). The Developer doc lists "monetization in the form of one-time or subscription based pricing" — [Partner Center – Developer, updated 2026-08-03](https://partner.tiktokshop.com/docv2/page/developer)
- **Developer types** — [Partner Center – Developer](https://partner.tiktokshop.com/docv2/page/developer)
  - **Seller developer:** builds a custom app for its own shop only. It needs an activated shop with an assigned Account Manager.
  - **System integrator:** builds custom or public apps.
  - **App developer:** builds custom or public apps.
- **ISV onboarding** — [Developer onboarding, updated 2026-08-11](https://partner.tiktokshop.com/docv2/page/developer-onboarding)
  - Non-US developers register at partner.tiktokshop.com. The registration region "must be consistent with your company's business certification". Local partners "should choose only their local market".
  - You upload "your company's business certificate and registration information". An app created before certification "can't publish until certification is complete".
  - A compliance and legal review "can take three or more weeks". It is always required for US and UK partners and decided "case-by-case for others".
- Common qualification fields are:
  - full company name as on the business license;
  - date of registration;
  - company registration number;
  - company document;
  - business owner ID;
  - possibly UBO documents.

  Source: [Partner registration application requirement, updated 2026-09-14](https://partner.tiktokshop.com/docv2/page/64f19899cb677b0286e75d67)
- **Public app launch path** — [App development overview, updated 2026-07-06](https://partner.tiktokshop.com/docv2/page/64f198e74830a5028854bf8f)
  1. Registration review.
  2. Language listing review, for each market.
  3. App review.
  4. Compliance and legal review "when required".
  5. Listing.
  - Sandbox testing is required, an App Requirement Document (ARD) may be requested, and a go-to-market plan and beta are "usually required … when requested".
  - Custom apps can launch privately by authorization link. They need review only if they are Connector apps or reach 25+ seller authorizations.
- **BR-specific API facts:**
  - "In the Brazil market, marketplace sellers are required to upload invoices to marketplace before they can fulfill the order." The API added `need_upload_invoice`, CPF fields and an A6 `INVOICE_LABEL` — [Changelog, 2025-03-07](https://partner.tiktokshop.com/docv2/page/br-market-updated-api-workflow-to-support-order-invoice-and-warehouse)
  - `POST /fulfillment/202502/invoice/upload` is "Applicable only for local sellers in the Brazil market" — [Upload Invoice, updated 2026-10-10](https://partner.tiktokshop.com/docv2/page/upload-invoice-202502)
- **Affiliate and LIVE APIs:**
  - Affiliate APIs "are currently not available in the UK and EU markets". Availability depends on the app category per market — [Affiliate Seller API overview, updated 2026-09-21](https://partner.tiktokshop.com/docv2/page/affiliate-seller-api-overview)
  - A weekly creator-outreach quota is tied to the shop's GMV tier — [Get Weekly Creator Outreach Quota (202607)](https://partner.tiktokshop.com/docv2/page/get-weekly-creator-outreach-quota-202607)
  - The docs tree also lists LIVE analytics endpoints (`Get Shop LIVE Minute Performance` 202510, `LIVE Products Performance` 202512, `LIVE Performance List/Overview` 202609) and SPS shop-health endpoints (202606) — [Partner Center document tree, 2026-10-12](https://partner.tiktokshop.com/api/v1/document/tree?workspace_id=3&aid=359713&locale=pt-BR)
- **The "Free Sample Invoicing" badge** says sellers "podem fazer a emissão massiva de Notas Fiscais de Amostras pelo sistema do integrador". The badge was created 2025-04-24 and updated 2026-03-23 — [search_condition API, 2026-10-12](https://seller-br.tiktok.com/api/v2/open/bso/portal/service/search_condition?service_business_type=2&locale=en&language=en&shop_region=BR&seller_type=2)
- The client's own vault says "MEI não serve: programação não é atividade permitida". The bill to allow it (PLP 25/2026) had only passed one committee by 30/06/2026 — [[Pagamentos e impostos]], citing [Fenacon](https://fenacon.org.br/noticias/comissao-aprova-inclusao-de-programadores-e-desenvolvedores-de-software-no-mei/)

### Inferences
- **The gating fact for every TikTok, Shopee and Temu app candidate is the company requirement (G7).** The client planned to start on CPF and open an ME later. A public marketplace app forces the ME first, plus accounting costs, which strains a R$700 budget. It also adds the review queue before the first sale. My estimate is ≥3–6 weeks from start to the first possible paid install.
- **The store has no installs, reviews or ratings.** A newcomer can't prove traction, and buyers can't tell good apps from bad. Ranking appears to be curated ("Recommended for you" showed only Bling, UpSeller, Tray, Olist, Magis5 and ChatPlusAI). Listing may not produce discovery at all. Distribution would still lean on YouTube and SEO.
- **The time-to-listing appears short** (days) for some apps (the TF Collab and Desh examples). This is weak evidence, because the ID may be minted at draft creation.

### Gaps
- Whether TikTok accepts a MEI/ME CNPJ, and which Brazilian document types it takes (the guidance link is an internal Feishu doc). No published review SLA for BR public apps.
- No install, revenue or ranking data for any BR app, so G2's "a newcomer can still win revenue" can't be verified on this store.

---

## 3. Which tools already serve Brazilian TikTok Shop sellers, and at what prices?

### Takeaway
Every big Brazilian ERP or hub is listed:
- Bling, UpSeller (free), the Olist ERP (Tiny), Tray and Magis5;
- HUB2B, ANYMARKET, Plugg.to, Precode, HubNoov, Notazz and VTEX Sync.

Four of them hold the free-sample NF-e badge. On top of that sits a fresh layer of 2026 point tools, each category crowded:
- about 20 "lucro real / conciliação" apps at R$47–R$690/month;
- 20 creator-affiliate tools, from Chinese bulk-inviters to Euka at US$199–599/month;
- 21 customer-service inboxes, many of them AI;
- 17 AI-video generators.

Ideris wasn't found in the store.

### Cited Findings
**ERPs and hubs (listing dates decoded from IDs; prices from vendors' sites, 2026-10-12)**

| Tool | In BR store since | Price evidence | Source |
|---|---|---|---|
| Bling | 2025-04 | Listing: "90 dias grátis utilizando o cupom #tiktok", "mais de 300 mil usuários". Price page: Cobalto R$60/mo (up to 200 orders), Titânio R$96–120/mo | [listing](https://seller-br.tiktok.com/appstore/br/7488656928959235846); [Bling preços](https://www.bling.com.br/planos-e-precos) |
| UpSeller ERP | 2024-04 | "Sistema grátis de gestão OminiChannel … compatível emissão de NF-e"; holds the sample-NF badge | [listing](https://seller-br.tiktok.com/appstore/br/7362953095749388037) |
| Olist ERP (Tiny) | 2025-03 | Holds the sample-NF badge | [listing](https://seller-br.tiktok.com/appstore/br/7486381187866281734) |
| Tray Commerce | 2025-02 | Holds the sample-NF badge | [listing](https://seller-br.tiktok.com/appstore/br/7470419499608262406) |
| Magis5 | 2025-02 | Price page shows no prices | [listing](https://seller-br.tiktok.com/appstore/br/7467820655632271110) |
| HUB2B | 2025-03 | R$199 / R$299 / R$599 / R$999 per month **+ per-order fee** | [HUB2B planos](https://hub2b.com.br/planos) |
| Ideris | not in store | Overage of R$0.60 / R$0.55 / R$0.40 per extra order (500 / 1,000 / 3,000 orders included) | [Ideris planos](https://www.ideris.com.br/planos) |
| ANYMARKET, Plugg.to, Precode, VOLT ERP, HubNoov, Notazz, NotaFlow, Dnotas | 2025–2026 | not collected | e.g., [ANYMARKET](https://seller-br.tiktok.com/appstore/br/7480080490495772422), [Dnotas](https://seller-br.tiktok.com/appstore/br/7634657104092481287) |

**"Lucro real" and reconciliation (all created 2025-12 to 2026-10, except Koncili 2025-05)**

| App | Created (decoded) | Price | Source |
|---|---|---|---|
| Quati | 2026-08-23 | "a partir de R$ 97/mês", 7-day trial. Claims "lucro … por SKU, por creator e por live", repasse reconciliation | [usequati.com.br](https://usequati.com.br/); [listing](https://seller-br.tiktok.com/appstore/br/7677194011107280641) |
| Lucro Por Pedido | 2026-07-05 | "até 200 vendas por mês, por R$ 47" | [lucroporpedido.com.br](https://lucroporpedido.com.br) |
| Lucro ON | 2026-04-08 | R$49 (≤R$25k/mo sales), R$149, R$329, R$690 | [lucroon.com.br](https://lucroon.com.br) |
| Oquesobra | 2026-04 / 2026-07 | R$99 (500 sales), R$149 (1,000), R$289 (2,500), R$399 (5,000) | [oquesobra.com.br](https://oquesobra.com.br) |
| Desh | 2026-10-06 | Bronze R$99, Prata R$149, Ouro R$199 | [desh.app.br](https://desh.app.br) |
| GB Intelligence, MaxGainer | 2026-08 / 2026-06 | "Sistema grátis" / "Ferramenta … gratuita" | [GB](https://seller-br.tiktok.com/appstore/br/7674714557458269973), [MaxGainer](https://seller-br.tiktok.com/appstore/br/7647745996591597313) |

Also listed: TikYn, Uply, 7Seller, Kixmon (UK), Charme (by "claude code"), WebConcilia, Koncili, Confery, IP Finanças, GE.Finance, MR Seller, Seller GWB, Alphametrics, Dash (Empreender), Seven Data and Dashboardly — [crawl](https://seller-br.tiktok.com/appstore/br/search?category_id=1&page=1)

**Creator and affiliate tools (20)**
- **Euka**, "nº 1 … Mais de 1.000 marcas" (self-reported). Starter **US$199/mo** for shops under US$2k GMV; recommended plan **US$599/mo** per workspace — [Euka pricing](https://www.euka.ai/pricing); [listing](https://seller-br.tiktok.com/appstore/br/7511917702673418040)
- **Cruva, Crevideo Reach, ProBoost.AI, BigVIRALS, Dagents**: AI outreach.
- **Chinese mass-invite tools**: "Mass KOL" claims "+100 mil usuários"; DAMI-KOL; HuaYoung; Seesail; Daimai; TIDEUP.
- **TF Collab (Brazilian, 2026-10-02):** creator search, CRM, targeted invites with free samples, weekly-quota check, inbox, sample approval and content tracking — [listing](https://seller-br.tiktok.com/appstore/br/7691909941623555861)
- **Creator-side tools:**
  - Gaia Creator: Free, Pro **R$79/mo** and Studio **R$149/mo** — [listing](https://seller-br.tiktok.com/appstore/br/7644811643152008981)
  - Naper Creator (credits model), Owra, TikTally Creator and ViralTTK Pro.

**Other categories**
- **Customer service (21 apps):** Duoke, Predize, GoBots, SmartReply, Responso, Hiifans, Adstart Inbox, HelpyGo (Precode) and several AI chatbots — [crawl](https://seller-br.tiktok.com/appstore/br/search?category_id=1&page=1)
- **AI video (17):** a dedicated live-commerce AI "digital human" from ByteDance itself, BytePlus Live, which offers "análise post-mortem abrangente do comércio LIVE" — [listing](https://seller-br.tiktok.com/appstore/br/7673049873335568149)
- **Thin categories:** Returns has 1 app (CSM Aquarius, an ERP-sync tool) and Customer Reviews has 1 (Judge.me) — [crawl](https://seller-br.tiktok.com/appstore/br/search?category_id=1&page=1)

### Inferences
- **Saturation by category on the BR store:**
  - Profit/reconciliation: saturated (20+, including free ones).
  - Creator CRM: saturated (20, including a US$599/mo leader and free Chinese tools).
  - Customer service: saturated.
  - AI video: saturated, and excluded anyway as AI-core.
  - Sample NF-e: owned by ERPs, one of them free.
- **Still thin:** returns workflow, reviews, a dedicated LIVE-ops/P&L tool (only Quati's "por live" feature and ByteDance's own BytePlus Live) and SPS shop-health. "Thin" here means few listings, not proven demand (§4).
- **Willingness to pay is proven in principle.** Several Brazilian apps state prices of R$47–R$690/month, and Euka sells at US$199–599. But none shows revenue, so all of this is self-reported, and a lot of it may be vibe-coded supply chasing the same buyers.

### Gaps
- No verified revenue for any TikTok Shop BR tool. TrustMRR's cached dataset (from round 1) had no Brazilian marketplace tools.
- Pricing for Magis5, Plugg.to, ANYMARKET and Olist wasn't collected (JS pages or quote-only).

---

## 4. What Brazilian TikTok Shop sellers struggle with: pain evidence

### Takeaway
The loudest seller-side pains fall into three groups:
1. **Fiscal and operational:** NF-e per order and per free sample, labels, ERP integration.
2. **Margin after the July 2026 fees and payout timing:** repasse delays and retentions.
3. **Account health:** video blocks, restrictions, appeals.

There's also strong interest in affiliate recruitment. Groups 1 and 2 are already served by the tools in §3. Group 3 is a platform decision, not a tool gap.

### Cited Findings
- **Google Autocomplete (pt-BR/BR, 2026-10-12):**
  - "tiktok shop nota fiscal" expands to "emite nota fiscal", "sem nota fiscal", "exige nota fiscal", "tem emissor de nota fiscal" and "como vender no tiktok shop sem nota fiscal".
  - "tiktok shop integração" expands to "integração tiktok shop bling / e nuvemshop / tiny".
  - Price and margin: "calculadora tiktok shop 2026", "planilha tiktok shop", "repasse tiktok shop".
  - Account health: "tiktok shop sps score", "conta suspensa tiktok shop", "penalidade tiktok shop".
  - Affiliates: "tiktok shop afiliados", "requisitos afiliados tiktok shop".
  - Source: [Google Suggest endpoint](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=tiktok%20shop%20nota%20fiscal)
- **YouTube (views at 2026-10-12; the ages are YouTube's relative dates):**
  - "Como gerar Envio e Imprimir etiqueta do Tik Tok Shop em 2025": 46,709 views (1 year).
  - "Como gerar nota fiscal NF dos seus pedidos do Tiktok Shop…": 6,834 (1 month).
  - "Como emitir nota fiscal para pedidos de amostras da TikTokShop?" (UpSeller channel): 4,073 (1 year).
  - "Nota Fiscal de Amostra Grátis no TikTok Shop": 874 (4 months).
  - "(NOVAS TAXAS 2026) Quanto Custa Vender no TikTok SHOP": 11,086 (2 months).
  - "Como vender todos os dias com os Afiliados do TikTok Shop": 22,409 (1 year).
  - "AFILIADO TIKTOK SHOP: O Que É…" (creator-side): 186,721 (4 months).
  - Source: [YouTube search "tiktok shop amostra grátis nota fiscal"](https://www.youtube.com/results?search_query=tiktok+shop+amostra+gr%C3%A1tis+nota+fiscal), [YouTube search "lucro tiktok shop planilha"](https://www.youtube.com/results?search_query=lucro+tiktok+shop+planilha), [YouTube search "tiktok shop afiliados vendedor como chamar criadores"](https://www.youtube.com/results?search_query=tiktok+shop+afiliados+vendedor+como+chamar+criadores)
- **Reclame Aqui, TikTok Shop page (01/04–30/09/2026):**
  - 16,359 complaints; reputation "Boa"; 76.9% resolved; average consumer score 6.35.
  - Most complaints are from buyers. Seller-type titles visible on 2026-10-12 include "TikTok Shop bloqueia meus vídeos e nega recursos sem revisão adequada" and "Minha conta foi restringida indevidamente…".
  - Source: [Reclame Aqui – TikTok Shop](https://www.reclameaqui.com.br/empresa/tiktok-shop/lista-reclamacoes/?busca=vendedor)
- **Platform-imposed operational load:**
  - NF-e upload is mandatory before fulfillment in BR — [TikTok changelog 2025-03-07](https://partner.tiktokshop.com/docv2/page/br-market-updated-api-workflow-to-support-order-invoice-and-warehouse)
  - The free-sample invoicing badge exists — [search_condition API](https://seller-br.tiktok.com/api/v2/open/bso/portal/service/search_condition?service_business_type=2&locale=en&language=en&shop_region=BR&seller_type=2)
  - The weekly creator outreach quota is tiered by GMV — [API doc](https://partner.tiktokshop.com/docv2/page/get-weekly-creator-outreach-quota-202607)
- A vendor (self-interested) describes the payout pain as "Repasses que levam 30, 40 dias. Valores retidos sem aviso. Extrato que não bate com a venda" — [Quati](https://usequati.com.br/)

### Inferences
- **NF-e, labels and integration** are the highest-volume searches, but the market answer is the free or cheap ERPs (UpSeller free; Bling R$60 with a 90-day TikTok coupon). This matches the round-1 trap "Apps de emissão de NF-e", reinforced.
- **Margin and repasse** pain is real and recent (15/07/2026), but it produced 20+ apps by October.
- **Account-health complaints** (blocked videos, restrictions) are appeals against platform decisions. An SPS monitor could warn earlier, but TikTok's Seller Center already exposes SPS. I found no evidence that anyone pays for a third-party monitor.
- **Live commerce** is the fastest-growing behaviour (161×), yet no non-AI Brazilian live-ops tool exists in the store. That is the only thin spot with an obvious demand driver (§11, C5).

### Gaps
- Reclame Aqui per-term counts ("repasse", "amostra", "nota fiscal") were blocked by a bot check after the first page. Seller-only complaint volume is unknown.
- I didn't access Facebook or WhatsApp seller groups (login required) or Reddit.

---

## 5. Shein marketplace, Temu Brasil and Kwai Shop: status and developer access

### Takeaway
- **Temu:** opened to local Brazilian sellers on 30 Oct 2025. It added an ANYMARKET integration around July 2026 and a seller-training programme in Sep 2026. Its Partner Platform covers Brazil, but online registration is only for ERP, OMS, WMS, multichannel-management (MCM) and connector developers.
- **Shein:** has a Portuguese open platform for product and order integrations, dominated by Bling, UpSeller and Omie since 2023.
- **Kwai Shop:** launched in late 2024 with high seller entry thresholds. I found no public developer platform.
- **For a solo developer, none of the three is a fit:** small or unknown seller pools, ERP-only app types, or no API.

### Cited Findings
- **Temu:**
  - Entered Brazil in June 2024 and "abriu sua plataforma para vendedores locais no Brasil", with deliveries in up to 2 business days — [Mercado & Consumo, 2025-10-30](https://mercadoeconsumo.com.br/30/10/2025/ecommerce/temu-abre-marketplace-para-vendedores-brasileiros/)
  - Partnered with ANYMARKET so sellers can manage stock, listings and sales from the ANYMARKET panel (portal post dated about 2026-07-28, citing TI Inside) — [Descubre.vc](https://www.descubre.vc/noticia/temu-se-al-a-con-anymarket-para-impulsar-a-vendedores-locales-en-brasil-2026-07-28)
  - Launched a monthly training programme for selected local sellers (5 areas, 18 topics) — [Central do Varejo, 2026-09-24](https://centraldovarejo.com.br/?p=46184)
  - **Partner Platform:**
    - Lists a Brazil seller site (`br.seller.temu.com`) and an app store reached through the seller center — [Temu Partner Platform, rendered 2026-10-12](https://partner.temu.com/)
    - "Currently, only Developer type is supported for online registration". Developers "typically offer … ERP systems, OMS systems or WMS systems, as well as MCM and Connectors". Service providers are handled offline via partner@temu.com (doc updated 2025-08-15) — [Temu Partner Guide – Registration Overview](https://partner.temu.com/documentation?menu_code=52ef88bdef1d4527b15f6d303b173e48)
- **Shein:**
  - Its open platform, in Portuguese, offers OpenAPI and webhooks for product management and order fulfilment (by Shein logistics or the seller). Process: account request, then create app, app review, integration authorization — [SHEIN Developer Platform, rendered 2026-10-12](https://open.sheincorp.com/)
  - Bling was Shein's first Brazilian ERP partner (10/05/2023) — [Startups](https://startups.com.br/negocios/shein-escolhe-bling-como-1a-parceiro-de-erp-no-brasil/)
  - Per a search summary (not re-fetched): Omie connects via Omie.Hub, UpSeller is integrated with SHEIN local stores, and Shein has required NF-e from Brazilian sellers since June 2023 — [ABES](https://abes.org.br/en/?p=85707), [UpSeller blog](https://upseller.com/pt/blog-article-94)
- **Kwai Shop:**
  - Launched in Brazil at the end of 2024 (search summary of Mercado & Consumo, 01/11/2024) — [Mercado & Consumo](https://mercadoeconsumo.com.br/01/11/2024/ecommerce/kwai-lanca-no-brasil-sua-plataforma-de-e-commerce-kwai-shop/amp/)
  - Seller requirements (secondary, may be outdated): more than R$20k in sales over the last 30 days or a 4.5 rating on Shopee/Amazon; above R$100k for wholesalers and brands; NF-e on every product — [Ecommerce na Prática](https://ecommercenapratica.com/blog/como-vender-no-kwai/)
- **Demand signals (YouTube, 2026-10-12):**
  - "Como Vender na Temu Brasil… (Taxa 0% e Sem Convite)": 7,067 views (10 months); ANYMARKET's own Temu guide: 1,278 (2 months) — [YouTube search](https://www.youtube.com/results?search_query=vender+na+temu+brasil+vendedor)
  - Shein how-to videos: 5k–48k views, mostly 1–2 years old — [YouTube search](https://www.youtube.com/results?search_query=vender+na+shein+marketplace+brasil)
  - Autocomplete includes "vender na temu precisa de cnpj", "vender na shein com cpf" and "kwai shop reclame aqui" — [Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=vender%20na%20temu)

### Inferences
- **Temu is the newest open marketplace with a BR partner programme**, which makes it the genuinely immature ecosystem. But it only accepts ERP-type developers online, and hubs (ANYMARKET, UpSeller) are already in. A solo developer can't build an ERP or OMS in 4 weeks. Kill.
- **Shein:** an incumbent-ERP-owned integration surface. Kill.
- **Kwai Shop:** no API surface found, and a small, gated seller base. Kill (or a gap if an API appears).

### Gaps
- Seller counts for Temu BR, Shein BR and Kwai Shop. Whether Temu's BR app store has non-ERP categories. Kwai's developer access (no source found).

---

## 6. Mercado Livre and Shopee Brasil: 2026 rule and fee changes, and the Shopee Open Platform rules for Brazil

### Takeaway
Three things happened in 2026:
1. **Shopee restructured its fees in March 2026.** Price bands now carry big fixed fees: 20% + R$4 up to R$79.99, then 14% + R$16 at R$80. Free shipping became mandatory, and CPF sellers pay +R$3 per item.
2. **Shopee changed the tax handling of Comissão Extra from 1 Aug 2026.** PJ affiliates must issue one NFS-e per paying brand, and PF affiliates' extra commission becomes a seller–affiliate matter, with RPA. This is the clearest new compliance pain of 2026, and the market answered it within weeks (§11, C1).
3. **ML's changes** (round 1) stand: a March 2026 operating-cost model, the API price-edit lock since 18/03/2026, and the DPP closed in Q4 2026.

Shopee's Open Platform in Brazil accepts only "Registered Business Seller" and "Third-party Partner (ISV)" accounts, both requiring a registered business. It has **no Brazilian app store**; the "Service Market" is a China cross-border site.

### Cited Findings
- **Shopee fee table (updated 2026-07-28):**

  | Item value | Commission | Pix subsidy |
  |---|---|---|
  | Up to R$79.99 | 20% + R$4 | — |
  | R$80–99.99 | 14% + R$16 | 5% |
  | R$100–199.99 | 14% + R$20 | 5% |
  | R$200–499.99 | 14% + R$26 | 5% |
  | Above R$500 | 14% + R$26 | up to 8% |

  - CPF sellers pay R$3 more per item.
  - Since March 2026 every seller is automatically in the Free Shipping Program.
  - The publication warns that "um produto de R$85 paga comissão efetiva próxima de 33% — enquanto um produto de R$79,99 paga cerca de 25%".
  - Source: [Ecommerce na Prática](https://ecommercenapratica.com/blog/taxa-shopee/)
- Same direction (updated 2026-08-17): the commission now varies by price band, the R$100 cap was removed, the fixed fee rose from about R$5 to about R$7 and reaches R$26, free shipping became mandatory, a Pix subsidy was added, and high-volume CPF sellers pay more — [Actana blog](https://actana.com.br/blog/mudancas-na-shopee-em-2026). **Conflict:** Tributei says the percentage commission is capped at R$100 per product (search summary, not fetched) — [Tributei](https://tributei.net/blog/como-precificar-na-shopee/)
- **Comissão Extra rule from 01/08/2026:**
  - The PJ affiliate keeps one monthly NFS-e to SHPS Serviços Administrativos Ltda for the standard commission, and **issues one NFS-e per seller** that paid extra commission.
  - PF affiliates "não emite NFS-e"; the RPA for extra commission becomes "tratativa direta com cada vendedor".
  - Shopee provides a monthly NF/RPA report. A R$30 floor applies, and the first payments may take up to 60 days.
  - Source: [Actana, 2026-07-29](https://actana.com.br/blog/shopee-comissao-extra-novo-modelo-fiscal-nfs-e-por-marca); [Actana product page](https://actana.com.br/nota-fiscal-afiliado-shopee)
- **An accountant's forum post (2026-07-16)** — [Contábeis fórum](https://www.contabeis.com.br/forum/tributos-estaduais-municipais/414911/comissao-extra-shopee-nfs-e-por-vendedor-a-partir-de-01-08-o-que-estamos-orientando-duvidas/)
  - The basis is LC 214/2025, and the report lists each seller's CNPJ, company name, address, e-mail and amount.
  - CNAE 7490-1/04 "NÃO é permitida no MEI".
  - "cliente com 100 a 300 marcas vira uma pequena fábrica de notas … cerca de 6 min por nota; automatizando … 200 notas em cerca de 9 minutos".
  - "a Shopee NÃO bloqueia o pagamento de quem não emite".
  - **Conflict:** Actana says "Sem emissão da nota, o pagamento do ciclo não é liberado" — [Actana](https://actana.com.br/blog/shopee-comissao-extra-novo-modelo-fiscal-nfs-e-por-marca)
  - Caveat: the same forum user also opened the RPA thread below and links to "um guia aberto". It may be vendor-seeded.
- **Seller-side RPA:** an accountant asks how to run "RPA em lote" for dozens of PF affiliates per month in eSocial S-1200/S-1210, and about INSS ceilings (2026-08-02; 2,169 views) — [Contábeis fórum](https://www.contabeis.com.br/forum/Tributos%20Federais/415123/rpa-em-lote-para-afiliado-pf-comissao-extra-shopee-periodicidade-certa-no-esocial-s-1200-s-2500/)
- Shopee also cut some video-campaign affiliate commissions and boosted Shopee Live (2026-07-11) — [Seu Crédito Digital](https://seucreditodigital.com.br/shopee-muda-regras-tiktok/)
- **Shopee pool size (search summary):** 3 million+ registered sellers in Brazil, and Brazilian sellers make up 90%+ of sales — [Mercado & Consumo, 2026-01-30](https://mercadoeconsumo.com.br/30/01/2026/ecommerce/shopee-planeja-capacitar-mais-de-100-mil-vendedores-brasileiros-em-2026/)
- **Shopee Open Platform (BR):**
  - "Localmente, no Brasil, atuamos apenas com: Registered Business Seller [e] Third-party Partner". The profile "precisa ser aprovado antes da criação de Apps", based on internal criteria (released 2026-07-19) — [Crie a conta de desenvolvedor](https://open.shopee.com/developer-guide/738)
  - Individual Seller is "Closed for BR"; ISV means "businesses with registered licenses providing services to sellers" — [Developer account registration](https://open.shopee.com/developer-guide/12)
  - The app category decides every API permission: "não existem liberações adicionais" — [Perguntas Frequentes](https://open.shopee.com/developer-guide/735)
  - Go-live requires a live product URL, a test user, an IP whitelist and an infrastructure declaration (2026-07-20) — [Publique seu App](https://open.shopee.com/developer-guide/741)
  - NF is mandatory for CNPJ sellers, and buyer data is masked by order status — [Dados Sensíveis](https://open.shopee.com/developer-guide/743)
  - The Service Market points to `service.shopeecb.cn`, reached from the "中国卖家中心", i.e., China cross-border (doc released 2026-09-18) — [Service Market](https://open.shopee.com/developer-guide/753)
  - BR SPI apps exist: Seller Logistics, plus whitelist-only Swarm ERP, Brand Membership and Auto Parts (2026-08-14) — [BR SPI App Creation](https://open.shopee.com/developer-guide/749)
  - An AMS affiliate-campaign API exists (2025-10-22) — [Shopee AMS API](https://open.shopee.com/developer-guide/702)
- **Mercado Livre (round-1 primary sources, fetched 2026-10-12):**
  - DPP: "Neste Q4 … não estamos aceitando novas inscrições", with a US$2.5M monthly GMV bar for Brazil — [ML DPP](https://developers.mercadolivre.com.br/pt_br/developer-partner-program)
  - Price edits blocked via API on auto-priced items since 18/03/2026 — [ML automatizações](https://developers.mercadolivre.com.br/pt_br/automatizacoes-de-precos)
  - Faturador with IBS/CBS — [ML IBS/CBS](https://developers.mercadolivre.com.br/pt_br/configuracoesibscbs)
  - Operating cost by weight, cubage and price from March 2026 — [Tecnospeed](https://blog.tecnospeed.com.br/tarifas-do-mercado-livre/)
- **IBS/CBS on marketplace invoices** is drawing attention: "🚨 IBS/CBS na Shopee: NOVA FORMA de Emitir Nota Fiscal Shopee" got 23,306 views (1 month) — [YouTube search](https://www.youtube.com/results?search_query=IBS+CBS+nota+fiscal+shopee)

### Inferences
- **Shopee's band structure creates "cliff" prices.** R$80–88 nets less than R$79.99, and similar steps appear at R$100 and R$200. Free calculators and the profit apps' simulators already cover this, so as a standalone product it matches round 1's "Margem ML" pattern (§10, C6).
- **The Comissão Extra rule is the strongest new forced change found.** It also shows how fast Brazilian vendors and accountants react: Conta Azul shipped in about 3 weeks (§11, C1).
- **Shopee and ML both lack a BR app-store discovery surface.** ML's partner programme is closed and Shopee's Service Market is China-only. Shopee's ISV route needs a registered business and Shopee approval.

### Gaps
- No official Shopee announcement was fetched (seller and affiliate centers need a login). The rule details come from vendors, accountants and Sebrae.
- No count of Shopee PJ affiliates or of sellers paying Comissão Extra.

---

## 7. Magalu, Amazon.com.br SP-API and Americanas: gaps

### Takeaway
- **Magalu** offers a modern self-serve API: create an app via the ID Magalu CLI, then OAuth 2.0, webhooks, catalog, orders, SAC, Q&A and chat. There is no public app store.
- **Amazon.com.br** has a Portuguese Selling Partner Appstore, led by global suites (Helium 10, LINGXING, the free ERP Dianxiaomi).
- **Americanas** wasn't researched.
- For a solo developer, none showed a thin, discoverable niche. Distribution would be content-only (Magalu), or the developer would face global incumbents (Amazon).

### Cited Findings
- Magalu developer portal: "Crie sua aplicação pelo CLI do ID Magalu e gere seu Client ID e Client Secret". APIs for "Catálogo de Produtos, Fluxo de Pedidos, SAC, Perguntas & Respostas e Chat com o Cliente", plus webhooks and OAuth 2.0 with renewable tokens "de integradoras e sellers" — [developers.magalu.com, rendered 2026-10-12](https://developers.magalu.com/)
- Amazon BR Appstore: categories are Ofertas de produtos, Inventário e envio, Marketing, Engajamento do cliente, Finanças and Gerenciamento de comércio eletrônico. "Aplicativos populares": LINGXING, Helium 10 and 店小秘/Dianxiaomi, the last described as a "serviço de ERP … gratuito que serve mais de 1,2 milhão de vendedores" — [Selling Partner Appstore BR, rendered 2026-10-12](https://sellercentral.amazon.com.br/selling-partner-appstore/)

### Inferences
- Magalu's self-serve API lowers the access barrier. With no app store, though, an app would be sold only through search and YouTube, against hubs that already integrate Magalu (round 1: ANYMARKET, Bling, etc.). Low priority.
- Amazon BR: global tools plus free Chinese ERPs. No Brazil-specific gap was evident without deeper work.

### Gaps
- Americanas marketplace API access and seller trends weren't researched (budget). Magalu seller counts and Amazon BR Appstore listing counts weren't collected.

---

## 8. WhatsApp Business Platform: per-message pricing (since July 2025), 2026 changes, and SMB tools that aren't chatbots

### Takeaway
Meta's pricing changed in three steps:
- **Since 1 July 2025:** Meta charges per delivered message, by category and market.
- **Since 1 July 2026:** a fifth category, "Meta Business Agent", Meta's own AI agent at US$2.00 per 1M tokens (about 4–5 US cents per message).
- **Since 1 October 2026:** Meta charges for **service messages** again, with 1,000 free per business phone number per month.

The change is producing big Brazilian YouTube interest. But Meta's own AI agent absorbs the chatbot layer, and BSPs own billing. I found no paid standalone "cost-monitor" product to prove willingness to pay.

### Cited Findings
- Page "Updated: 30 de set de 2026":
  - "Em vigor a partir de 1º de julho de 2025: a Meta cobra por mensagem … por categoria e mercado, e apenas por mensagens de empresas para usuários".
  - Five categories: marketing, utilidade, autenticação, serviço and Meta Business Agent (from 1 July 2026).
  - Meta Business Agent costs "uma taxa global de US$ 2,00 por 1 milhão (M) de tokens … aproximadamente 4 a 5 centavos de dólar por mensagem".
  - "a partir da meia-noite … em 1º de outubro de 2026. A Meta retomou a cobrança pelas mensagens de serviço, oferecendo a cada número de telefone comercial um nível gratuito de mil mensagens desse tipo por mês".
  - The free-entry-point window (click-to-WhatsApp ads) stays free.
  - From 1 Oct 2026 there are 47 rate-card markets, Brazil among them.
  - Source: [Meta – Preços na plataforma do WhatsApp Business, rendered 2026-10-12](https://developers.facebook.com/docs/whatsapp/pricing/)
- **Brazilian YouTube interest (2026-10-12):**
  - "Cobrança De Mensagens no WhatsApp | Entenda TUDO O QUE MUDA em 2026": 233,729 views (2 weeks).
  - "Meta vai cobrar por resposta no WhatsApp…" (HelenaCRM): 12,894 (3 months).
  - "[URGENTE] Meta VOLTA ATRÁS na cobrança da API OFICIAL": 33,542 (1 month).
  - Source: [YouTube search](https://www.youtube.com/results?search_query=whatsapp+api+oficial+cobran%C3%A7a+mensagem+2026)
- Autocomplete for "whatsapp api preço" includes "whatsapp api preço por mensagem", "whatsapp cloud api preço", "evolution api whatsapp preço" and "z api whatsapp preço" (the last two are unofficial APIs) — [Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=whatsapp%20api%20pre%C3%A7o)
- Round 1: WhatsApp apps on Nuvemshop number 68, with 3,953 reviews — [[marketplace_gaps]]

### Inferences
- **Buyers are confused by the pricing** (the "volta atrás" video against Meta's doc). That favours BSP and CRM vendors who explain costs, not a new standalone tool.
- **A "WhatsApp cost auditor" (non-AI) would need Meta Tech Provider status**, with business verification and app review. It would compete with Meta's free WhatsApp Manager analytics and the BSPs' dashboards, and Meta reprices quarterly. Kill (§10, C8).
- Catalog and payment features in Brazil weren't verified (see Gaps).

### Gaps
- The Brazilian per-category USD rates weren't extracted (the rate-card CSV wasn't fetched). The status of WhatsApp catalog and Pix payments in Brazil in 2026 is unverified.

---

## 9. Creator-economy platforms (Hotmart, Kiwify, Eduzz): API- or webhook-based tools that creators pay for

### Takeaway
Hotmart presents integrations as free and built in, with a "request an integration" flow. It keeps adding first-party tools (recovery, AI sales agent, members area, Smart Studio), which is the "platform absorbs the feature" pattern. Kiwify has a public API but no integrations page at the obvious URL. Eduzz wasn't verified. Round 1 already judged these as having no app-store discovery. Nothing new changes that.

### Cited Findings
- Hotmart's integrations page:
  - "as integrações padrão da Hotmart são gratuitas para produtores cadastrados".
  - "Com a API e Webhooks da Hotmart, você pode desenvolver integrações personalizadas"; "Se precisar de alguma integração que ainda não existe, clique em 'Solicite uma integração'".
  - The menu lists first-party tools: "Ferramenta de recuperação", "Agente de vendas", "Área de membros", "Tutor" and "Meu Agente de IA".
  - Source: [Hotmart – Integrações, fetched 2026-10-12](https://hotmart.com/pt-br/integracoes)
- `kiwify.com.br/integracoes` and `eduzz.com/integracoes` return 404 — [Kiwify 404](https://kiwify.com.br/integracoes), [Eduzz 404](https://www.eduzz.com/integracoes). Kiwify's public API exists (round 1) — [Kiwify API](https://docs.kiwify.com.br/api-reference/general)
- Autocomplete: "hotmart emite nota fiscal", "kiwify emissão de nota fiscal", "utmify preço", "automação whatsapp kiwify" — [Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=utmify). Notazz, an NF tool for creators, also sits in TikTok's BR store — [Notazz listing](https://seller-br.tiktok.com/appstore/br/7493801365443184389)

### Inferences
- The obvious creator tools are taken by platform features or incumbents: NF automation (Notazz, eNotas), UTM and sales tracking (Utmify, which drew strong branded autocomplete), and WhatsApp recovery. Not pursued further (budget).

### Gaps
- No verified competitor counts or prices for Hotmart, Kiwify or Eduzz add-ons. Eduzz's API and integration list weren't checked.

---

## 10. Candidate tools: records, gate verdicts and 1–5 scores

### Takeaway
I recorded ten candidates. **None is APPROVED.**
- **The adversarial reading:** by October 2026 the "immature ecosystem" window on TikTok Shop BR had closed. AI-assisted builders, many of them solo, filled every obvious category from April to August 2026.
- **The newly forced compliance niches fill just as fast.** The 2026 changes (Shopee Comissão Extra, the TikTok fee rise, WhatsApp's service-message billing) drew paid competitors within weeks.
- **One candidate is CONDITIONAL:** C5, TikTok Shop LIVE P&L and host commissions. The rest are KILL.

### Cited Findings
- All evidence is cited in §§1–9. The key items per candidate are repeated inline in the records below.

### Inferences
Scores run 1–5, where 5 is best; "low saturation" and "low risk" are scored so 5 means least saturated and least risky. US$5k/month ≈ R$27k/month at the project's reference rate ([[Objetivo e restrições]]).

**Cross-cutting G7 issue for every marketplace-app idea (C2–C6, C9):** TikTok, Shopee and Temu developer registration needs a registered company. MEI can't legally cover programming ([TikTok requirement doc](https://partner.tiktokshop.com/docv2/page/64f19899cb677b0286e75d67); [Shopee](https://open.shopee.com/developer-guide/12); [[Pagamentos e impostos]]). So the client must open an ME before the first sale, against the plan to "start on CPF".

---

**C1. "Notas do Afiliado": bulk NFS-e for Shopee Comissão Extra, for PJ affiliates** *(re-opens round-1 kill "Emissor de NFS-e Nacional" on new evidence: the 01/08/2026 rule)*
Deep-validated in §11.

| Item | Detail |
|---|---|
| Product | Import Shopee's monthly NF/RPA report, then emit one NFS-e per brand, e-mail the PDF and XML to each brand, and track which are done. |
| Buyer and pool | PJ Shopee affiliates (ME/SLU; MEI not allowed per accountants). Pool unknown; some issue 700–2,831 notes a month. |
| Verdict | **KILL**: fails G2 (saturation) and is borderline on G5 and G7. |
| Scores | WTP 4 · Low sat 1 · Buyer power 2 · Distribution 4 · Build 2 · Speed 3 · Low risk 2 = **18/35** |

**C2. "Lucro real + conciliação de repasses" for TikTok Shop BR (public app)** *(analog of round-1 "Lucro real Nuvemshop" and "Margem ML")*
Deep-validated in §11.

| Item | Detail |
|---|---|
| Product | Per-order, per-SKU and per-creator net profit after the July 2026 fees, affiliate commission and tax regime; repasse-vs-statement reconciliation. |
| Buyer and pool | TikTok Shop BR sellers with CNPJ (about 110k stores, estimate). |
| Verdict | **KILL**: fails G2. |
| Scores | WTP 4 · Low sat 1 · Buyer power 3 · Distribution 3 · Build 4 · Speed 2 · Low risk 3 = **20/35** |

**C3. Creator, affiliate and sample CRM for TikTok Shop BR sellers**

| Item | Detail |
|---|---|
| Product | Creator search and lists, targeted invites with samples, quota-aware outreach, sample approval, post-delivery content follow-up. |
| Evidence of WTP | Euka US$199–599/mo ([pricing](https://www.euka.ai/pricing)); Gaia Creator R$79–149 (creator side). |
| Competitors | 20 apps, including TF Collab (BR, Oct 2026), Cruva, Crevideo, Chinese mass-inviters claiming "+100 mil usuários" ([crawl](https://seller-br.tiktok.com/appstore/br/search?category_id=1&page=1)). |
| Weakness | Most competitors are AI-led and Chinese-built, so a non-AI, Portuguese-native CRM is a positioning angle. |
| Platform cap | TikTok's weekly outreach quota by GMV tier limits the "automation" value ([doc](https://partner.tiktokshop.com/docv2/page/get-weekly-creator-outreach-quota-202607)). |
| Demand | YouTube "afiliados TikTok Shop" seller videos get 4k–22k views (§4). |
| Gates | G1 PASS · G2 FAIL · G3 PASS · G4 PARTIAL · G5 PASS · G6 RISK (the category sells AI matching) · G7 needs ME · G8 unproven |
| Verdict | **KILL** |
| Scores | WTP 4 · Low sat 1 · Buyer power 3 · Distribution 3 · Build 3 · Speed 2 · Low risk 2 = **18/35** |

**C4. Bulk free-sample NF-e (remessa de amostra grátis) for TikTok Shop BR** *(touches round-1 trap "Apps de emissão de NF-e")*

| Item | Detail |
|---|---|
| Evidence | The badge exists (2025-04-24); videos on sample NF-e (874–4,073 views); autocomplete "nota fiscal de amostra grátis cfop / simples nacional" (§2, §4). |
| Competitors | Bling, **UpSeller (free)**, Tray and the Olist ERP all hold the badge ([BR store](https://seller-br.tiktok.com/appstore/br/)). |
| Risk | Fiscal liability and A1 certificate handling. |
| Verdict | **KILL**: G2 fails against free incumbents; G5 and G7 fiscal risk. |
| Scores | WTP 3 · Low sat 1 · Buyer power 3 · Distribution 2 · Build 2 · Speed 2 · Low risk 2 = **15/35** |

**C5. "Live P&L e comissão de host" for TikTok Shop BR sellers** (non-AI)
Deep-validated in §11.

| Item | Detail |
|---|---|
| Product | After each LIVE, automatically: GMV, refunds and net profit per live and per product; host commission and payroll statement (fixed + % of net); minute-by-minute product performance to plan the run-of-show; and comparison across hosts and time slots. |
| Verdict | **CONDITIONAL** (G1 unproven). |
| Scores | WTP 2 · Low sat 3 · Buyer power 3 · Distribution 2 · Build 3 · Speed 2 · Low risk 2 = **17/35** |

**C6. "Cliff auditor": bulk check of listings sitting just above Shopee, TikTok or ML fee bands**

| Item | Detail |
|---|---|
| Evidence | Shopee's R$80 band adds R$12 of fixed fee, and "R$85 paga comissão efetiva próxima de 33%" ([Ecommerce na Prática](https://ecommercenapratica.com/blog/taxa-shopee/)). TikTok's R$50 band depends on the price after seller discount ([Economic News](https://economicnewsbrasil.com.br/2026/09/30/taxas-tiktok-shop-black-friday-lojistas/)). |
| Demand | Autocomplete "calculadora shopee taxa 2026", "taxa shopee março 2026", "calculadora tiktok shop 2026" ([Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=shopee%20taxa%202026)). |
| Competitors | Free calculators; price simulators inside paid profit apps (Lucro Por Pedido "Simulador de preço", Quante pricing automation); round-1 ML extensions. |
| Access | Shopee ISV requires a company and Shopee approval, with no BR store. A Chrome-extension variant carries ToS risk (round 1). |
| Verdict | **KILL**: G1 rests on free calculators, G2 fails because the job is a feature of existing apps, G4's search intent is for free tools. |
| Scores | WTP 2 · Low sat 2 · Buyer power 3 · Distribution 3 · Build 4 · Speed 3 · Low risk 3 = **20/35** |

**C7. Batch RPA for PF affiliates (seller side, Shopee Comissão Extra)**

| Item | Detail |
|---|---|
| Evidence | Accountants are asking about "RPA em lote", eSocial S-1200/S-1210 and INSS ceilings ([Contábeis](https://www.contabeis.com.br/forum/Tributos%20Federais/415123/rpa-em-lote-para-afiliado-pf-comissao-extra-shopee-periodicidade-certa-no-esocial-s-1200-s-2500/)). YouTube "Como Gerar os RPAs para os Afiliados na Shopee!" has 3,238 views ([YouTube](https://www.youtube.com/results?search_query=rpa+afiliado+shopee+vendedor)). |
| Verdict | **KILL**: G5 and G7 fail (payroll and eSocial territory, INSS and IRRF liability, accountant-sold). |
| Scores | WTP 2 · Low sat 3 · Buyer power 3 · Distribution 2 · Build 1 · Speed 1 · Low risk 1 = **13/35** |

**C8. WhatsApp Cloud API cost monitor (post 01/10/2026)**

| Item | Detail |
|---|---|
| Evidence | Service messages are billable beyond 1,000 per number per month ([Meta](https://developers.facebook.com/docs/whatsapp/pricing/)); 233k-view explainer (§8). |
| Verdict | **KILL**: G1 fails (no standalone paid product found), G2 fails (BSP dashboards and Meta's WhatsApp Manager), and platform risk is high (Tech Provider review; quarterly repricing). |
| Scores | WTP 1 · Low sat 3 · Buyer power 3 · Distribution 3 · Build 3 · Speed 2 · Low risk 1 = **16/35** |

**C9. Connectors or tools for Temu BR, Shein BR or Kwai Shop**

| Item | Detail |
|---|---|
| Verdict | **KILL**: Temu online registration only for ERP/OMS/WMS/MCM/connector developers ([Temu](https://partner.temu.com/documentation?menu_code=52ef88bdef1d4527b15f6d303b173e48)); hubs already in (ANYMARKET, UpSeller); Shein owned by Bling, UpSeller and Omie; Kwai has no API found. |
| Scores | WTP 3 · Low sat 2 · Buyer power 3 · Distribution 1 · Build 1 · Speed 1 · Low risk 2 = **13/35** |

**C10. Hotmart, Kiwify or Eduzz add-ons (light check only)**

| Item | Detail |
|---|---|
| Verdict | **KILL**: platform absorbs (Hotmart integrations free plus native recovery and AI agent, [Hotmart](https://hotmart.com/pt-br/integracoes)); incumbents (Utmify, Notazz); round-1 "no discovery surface". |
| Scores | WTP 3 · Low sat 1 · Buyer power 3 · Distribution 2 · Build 4 · Speed 3 · Low risk 2 = **18/35** |

**Score table**

| # | Candidate | WTP | Low sat. | Buyer | Distrib. | Build | Speed | Low risk | Total | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| C2 | TikTok lucro real + repasse | 4 | 1 | 3 | 3 | 4 | 2 | 3 | **20** | KILL |
| C6 | Fee-band cliff auditor | 2 | 2 | 3 | 3 | 4 | 3 | 3 | **20** | KILL |
| C1 | Shopee affiliate bulk NFS-e | 4 | 1 | 2 | 4 | 2 | 3 | 2 | **18** | KILL |
| C3 | TikTok creator/sample CRM | 4 | 1 | 3 | 3 | 3 | 2 | 2 | **18** | KILL |
| C10 | Hotmart/Kiwify add-ons | 3 | 1 | 3 | 2 | 4 | 3 | 2 | **18** | KILL |
| C5 | TikTok LIVE P&L + host pay | 2 | 3 | 3 | 2 | 3 | 2 | 2 | **17** | CONDITIONAL |
| C8 | WhatsApp API cost monitor | 1 | 3 | 3 | 3 | 3 | 2 | 1 | **16** | KILL |
| C4 | TikTok sample NF-e | 3 | 1 | 3 | 2 | 2 | 2 | 2 | **15** | KILL |
| C7 | Seller batch RPA | 2 | 3 | 3 | 2 | 1 | 1 | 1 | **13** | KILL |
| C9 | Temu/Shein/Kwai connectors | 3 | 2 | 3 | 1 | 1 | 1 | 2 | **13** | KILL |

- These totals sit below every round-1 finalist (21–22) and are not competitive with the vault's current recommendations.

### Gaps
- No install or revenue data on any BR marketplace store, so G2's newcomer test and G8 can't be verified for C2, C3 or C5.
- Pool sizes for PJ affiliates (C1) and live-selling shops (C5) are unknown.

---

## 11. Deep validation of the top 3 (C1, C2, C5)

### Takeaway
I picked these three for the strongest forced change (C1), the strongest willingness-to-pay evidence with app-store distribution (C2), and the only low-saturation spot (C5).
- **C1 dies on saturation.** At least six paid or announced offerings appeared within about 10 weeks of the rule, including Conta Azul, and NFS-e coverage across municipalities is hard for one person.
- **C2 dies on saturation.** About 20 apps exist, a dozen of them created between April and August 2026, some free.
- **C5 survives only as CONDITIONAL.** Live commerce is the fastest-growing behaviour and the store has no non-AI Brazilian live-ops tool. But I found no one paying for this job as a standalone product, and ByteDance's own BytePlus Live and Quati's "lucro por live" overlap.

### Cited Findings
**C1: bulk NFS-e for Shopee Comissão Extra**
- **Rule and pain:**
  - One NFS-e per paying brand from 01/08/2026 ([Actana](https://actana.com.br/blog/shopee-comissao-extra-novo-modelo-fiscal-nfs-e-por-marca)).
  - "100 a 300 marcas … 6 min por nota" ([Contábeis](https://www.contabeis.com.br/forum/tributos-estaduais-municipais/414911/comissao-extra-shopee-nfs-e-por-vendedor-a-partir-de-01-08-o-que-estamos-orientando-duvidas/)).
  - Sebrae PR warns MEI affiliates (2026-09-01) — [Sebrae PR](https://sebraepr.com.br/comunidade/artigo/programa-de-afiliados-e-nota-fiscal-o-que-muda-a-partir-de-agosto-de-2026)
- **Demand signals:**
  - Autocomplete: "emissor nota fiscal afiliado shopee", "emitir nota fiscal afiliado shopee", "comissão extra shopee como funciona" — [Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=nota%20fiscal%20afiliado%20shopee)
  - YouTube: "Gerando +700 Notas Fiscais Shopee Afiliado - NF em massa para cada vendedor": **230,824 views** (2 months). "2.831 Notas Fiscais de Comissão Extra da Shopee — emissão em massa NFS-e": **193,123** (2 months). "SHOPEE MUDOU: Afiliados Precisam Fazer Isso P/ Receber Comissões! Emitindo Notas": 7,319 (2 weeks) — [YouTube search](https://www.youtube.com/results?search_query=comiss%C3%A3o+extra+shopee+nota+fiscal+v%C3%A1rias+marcas), [YouTube search](https://www.youtube.com/results?search_query=nota+fiscal+afiliado+shopee)
- **Competitors:**
  - **Conta Azul Pro** launched batch emission from the Shopee CSV on 2026-07-24. It works by upload, WhatsApp or e-mail, with "imposto calculado para o município", e-mail delivery to each seller, and "até 10 mil notas por mês" — [Conta Azul](https://contaazul.com/blog/como-emitir-nota-fiscal-afiliado-shopee-na-conta-azul/). Plans are R$179.90–929.90/month on promotion (list R$289.90–1,029.90) — [Conta Azul planos](https://contaazul.com/planos/)
  - **Actana NFS / "EmissorAfiliados"** offers batch emission from the report, plans "a partir de R$49,90" — [Actana](https://actana.com.br/nota-fiscal-afiliado-shopee), [Actana home](https://actana.com.br/)
  - **Other YouTube sellers of mass-emission tools (2 months):** "DIGISAN - Emissor de Nota" (790 views), "Ripply" (+500 notas; 511), "Wallace Alves Expert" ("AUTOMATIZADA e CUSTO BAIXO"; 697), "Faz Teu Futuro" (+1,000 notas em 3 minutos; 78) — [YouTube search](https://www.youtube.com/results?search_query=comiss%C3%A3o+extra+shopee+nota+fiscal+v%C3%A1rias+marcas)
- **Build reality:**
  - Conta Azul highlights that "alíquotas e retenções variam por município" and service codes 17.06/17.25 — [Conta Azul](https://contaazul.com/blog/como-emitir-nota-fiscal-afiliado-shopee-na-conta-azul/)
  - The accountant asks how to emit in volume in "municípios que ainda não aderiram ao Padrão Nacional" — [Contábeis](https://www.contabeis.com.br/forum/tributos-estaduais-municipais/414911/comissao-extra-shopee-nfs-e-por-vendedor-a-partir-de-01-08-o-que-estamos-orientando-duvidas/)
  - The vault records the NFS-e Nacional mandatory date for Simples ME/EPP as **1/9/2026 or 1/11/2026, sources conflicting** — [[Pagamentos e impostos]]

**C2: TikTok Shop BR lucro real + repasse**
- **Paid substitutes:** Quati R$97+, Lucro Por Pedido R$47, Lucro ON R$49–690, Oquesobra R$99–399, Desh R$99–199 (all self-published prices, 2026-10-12; §3).
- **Free substitutes:** GB Intelligence, MaxGainer, UpSeller ERP (§3).
- **Saturation:** at least 12 profit or reconciliation apps were created April–August 2026 (decoded IDs; §2–§3).
- **Distribution surface:** no installs, reviews or ranking signals (§2). The search intent is mostly for free calculators: "calculadora tiktok shop gratis" — [Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=tiktok%20shop%20calculadora)
- **API feasibility:** read-only order, finance and affiliate-order APIs exist; Quati says "100% API oficial — sem scraping" — [Quati](https://usequati.com.br/)

**C5: TikTok Shop BR LIVE P&L and host commissions**
- **Demand driver:** daily lives grew 20× and live GMV 161× from May 2025 to May 2026; Natura ran 52k lives in 2025 — [TikTok Newsroom](https://newsroom.tiktok.com/tiktok-shop-cresce-102-vezes-em-seu-primeiro-ano-no-brasil?lang=pt-BR). A headline on 2026-09-24 reports a brand (Via Uno) planning 12-hour lives with 200 creators for Black Friday — [Central do Varejo](https://centraldovarejo.com.br/?p=46184)
- **APIs:** `Get Shop LIVE Minute Performance` (202510), `Get Shop LIVE Products Performance List` (202512), `Get Shop LIVE Performance List/Overview` (202609) and the Live Room core stats endpoints (202502) — [Partner Center tree](https://partner.tiktokshop.com/api/v1/document/tree?workspace_id=3&aid=359713&locale=pt-BR)
- **Overlapping supply:**
  - Quati computes "lucro … por live" from R$97 — [Quati](https://usequati.com.br/)
  - BytePlus Live (ByteDance) offers AI digital-human lives and "análise post-mortem abrangente do comércio LIVE" — [listing](https://seller-br.tiktok.com/appstore/br/7673049873335568149)
  - TikTok Shop Partners (TSPs) sell "LIVE Management" as a service category — [Partner service categories](https://partner.tiktokshop.com/docv2/page/64f1989064ed2e0295f3c1b5)
  - The BR store has no dedicated LIVE category (§2).
- **Search demand is weak:** "tiktok shop live" autocomplete returns only TikTok's own tools: "live studio", "live manager", "live center" — [Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=tiktok%20shop%20live)

### Inferences
**C1: gate by gate**
- **G1 PASS:** ≥2 paid substitutes (Conta Azul Pro, Actana), revenue unverified.
- **G2 FAIL:** at least 6 offerings in about 10 weeks, including a large incumbent with municipal tax logic and 10k notes a month.
- **G3 WEAK:** affiliates are micro-businesses, though power users exist.
- **G4 PASS:** autocomplete plus 200k-view videos.
- **G5 BORDERLINE:** NFS-e Nacional only where municipalities adhere; elsewhere municipal integrations or a paid API (round 1: Focus NFe R$62.90–657.90/month), plus A1 certificate custody.
- **G6 PASS.**
- **G7 RISK:** fiscal liability for wrong notes. The "payment blocked?" urgency is disputed.
- **G8:** at R$49.90 the target needs about 540 customers; at R$99, about 270. The paid-API cost per note squeezes margin.
- **Verdict: KILL.** The window opened on 01/08/2026 and closed within the same quarter. The round-1 NFS-e kill is reinforced, not reversed.

**C2: gate by gate**
- **G1 PASS** (self-reported prices).
- **G2 FAIL:** about 20 apps, free tiers, ERPs bundling, and no way to show traction.
- **G3 MODERATE.**
- **G4 PARTIAL:** app store presence plus free-calculator searches.
- **G5 PASS.**
- **G6 PASS.**
- **G7 needs an ME.**
- **G8:** about 280 customers at R$97 (0.25% of about 110k stores) is plausible on pool size but implausible in a 20-way race without a distribution edge.
- **Verdict: KILL.**

**C5: gate by gate**
- **G1 FAIL / unproven:** no standalone paid product for this job found in Brazil; the overlaps are a feature of Quati and a ByteDance AI product.
- **G2 PARTIAL PASS:** no dedicated non-AI listing.
- **G3 PASS:** brands and sellers who run lives pay hosts.
- **G4 WEAK:** no commercial-intent searches.
- **G5 PASS:** read-only analytics APIs; a 3–4 week MVP: per-live P&L, host-commission rules, a PDF or WhatsApp report.
- **G6 PASS.**
- **G7:** needs an ME and TikTok public-app review, or a custom app shared by authorization link, which needs review only at 25+ sellers ([doc](https://partner.tiktokshop.com/docv2/page/64f198e74830a5028854bf8f)).
- **G8:** at R$147/month, about 185 customers. Plausible only if more than about 2% of live-selling shops pay, and that count is unknown.
- **Verdict: CONDITIONAL.**

**C5's single cheapest real-world test (about R$350, 14 days, CPF via Asaas)**
- **Asset:** a Portuguese landing page, "Relatório pós-live com lucro e comissão do host, automático", offering a free Google Sheets "Fechamento de live + comissão de host" template in exchange for e-mail or WhatsApp.
- **Traffic:**
  - R$300 of Meta/TikTok ads targeting TikTok Shop seller and live-commerce interests in Brazil.
  - One YouTube Short and one TikTok video explaining host-commission math after the July 2026 fees.
- **Offer:** a founding-customer **pre-sale at R$97 for the first month**, paid by Pix, delivered within 4 weeks, with a refund if not delivered.
- **PASS** (all within 14 days):
  - **≥5 paid pre-orders** from distinct CNPJ sellers;
  - **≥40 template downloads**;
  - at least 3 of the pre-orders say they run **≥8 lives/month**.
- **FAIL:** **≤1 pre-order**, or fewer than 15 downloads. Kill C5 and stop pursuing TikTok Shop tools.
- **In between** (2–4 pre-orders): run one more week of paid traffic before building.
- **Pre-sales only:** don't build or open the ME until the test passes.

### Gaps
- **C1:** the number of PJ affiliates receiving Comissão Extra; whether any newcomer (DIGISAN, Ripply and the others) has paying customers; the official Shopee wording on whether payment is blocked.
- **C2:** any install or revenue figure for the 2026 entrants.
- **C5:** how many BR shops run lives weekly; how hosts are paid in practice (fixed, %, per hour); whether TikTok's own LIVE Center already exports per-live settlement data that makes the tool unnecessary. None were found in public sources.
