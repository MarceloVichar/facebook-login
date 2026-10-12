# US & EU regulatory deadlines (2025–2027) that push SMBs, online sellers and Brazilian exporters to buy simple software: status on 12 Oct 2026, tools, gaps and product candidates for a solo developer

*Method note for the report writer: research done on 12 Oct 2026. The page-fetch tool returned DNS errors for every domain tried (apps.shopify.com, help.shopify.com, europa.eu, wikipedia.org, law-firm sites). Every finding below therefore comes from search-engine extracts of the cited pages, not from reading the pages in full. I did not open EUR-Lex, Official Journal or Federal Register texts directly; where a claim rests only on a vendor or law-firm summary, it is flagged. The web-search budget shared by all agents ran out before the last checks (the Wix App Market gap, the TRACES API and operator counts, the wording of GPSR Art. 19/44, the first EmpCo warning letters); these are listed under Gaps. I could not collect keyword volumes or Google Trends data (the Ahrefs and Similarweb connectors failed to connect), so "demand signals" rest on app-review counts, forum threads and how much content vendors publish. Shopify review counts are search-engine snapshots and may be out of date; prices are as vendors publish them (self-reported). I found no verified competitor revenue figure anywhere.*

---

## 1. EU GPSR (applies since December 2024): small-seller obligations, marketplace enforcement, tools and pricing, room for a cheap generator or tracker

### Takeaway
GPSR is in force and unchanged; I found no omnibus amendment to it. Marketplaces enforce it through mandatory listing fields and listing suppression. Sellers comply inside Etsy, Amazon and eBay for free and pay a third party for an EU Responsible Person (RP) at roughly €150–500 per year. The Shopify app niche is crowded: about 15 GPSR apps charge $0–29 a month, and only one has a meaningful review count (~29). There is no room for another cheap GPSR generator or tracker. **Trap.**

### Cited Findings
- **Etsy rules.** GPSR replaced the General Product Safety Directive and came into force across the EU in December 2024. Etsy sellers with EU customers must add manufacturer details and an RP to every applicable listing. Etsy has enforced this since the rules took effect and added shop-wide RP settings in April 2025. — [Craftybase](https://craftybase.com/blog/what-is-gpsr)
- **Etsy's official position.** Products sold into the EU need an EU-based economic operator; a non-EU maker can appoint an authorised representative. Etsy partners with Cert-Rep and International Associates to supply RPs. Shops can instead opt out of EEA and Northern Ireland sales. — [Etsy Help Center](https://help.etsy.com/hc/en-in/articles/28211364687383-What-is-the-General-Product-Safety-Regulation-GPSR)
- **Etsy enforcement trigger (sources conflict).** One vendor says non-compliant listings can be removed without notice and EU sales suspended. Another says Etsy acts only after a notification from EU or Northern Ireland authorities. — [24hour-ar](https://www.24hour-ar.com/the-hidden-risks-of-non-compliance-with-gpsr-on-amazon-etsy-ebay); [Craftybase](https://craftybase.com/blog/what-is-gpsr)
- **Delisting anecdote.** An established Etsy seller woke up to a delisted catalogue. This is a single story, not data. — [GetTransport blog](https://blog.gettransport.com/logistics-guide/gpsr-eu-product-safety-2026-non-eu-seller-guide/)
- **Amazon's process.** Sellers use the "Add compliance information" widget in the Manage Your Compliance dashboard. RP, manufacturer details and safety documents appear on product pages within 24 hours. Sellers leaving EU sales should remove affected products. — [Amazon Seller Forums (EU)](https://sellercentral-europe.amazon.com/seller-forums/discussions/t/0b73e2e0-991d-470f-87d4-4118fd8b5b1d)
- **Amazon seller pain.** A thread titled "GPSR Exit from EU Selling" reports that the RP entry page would not save details, with the same error on 3,900 listings. — [Amazon Seller Forums (EU)](https://sellercentral-europe.amazon.com/seller-forums/discussions/t/ef772626-6707-481f-8ab4-7863a338affe)
- **Amazon suspensions (vendor claim).** Amazon reportedly suspended listings without a valid EU RP in a wave in early 2025. Vendors also say the RP's contact details should appear on the product or its packaging, not only on the listing. — [24hour-ar](https://www.24hour-ar.com/the-hidden-risks-of-non-compliance-with-gpsr-on-amazon-etsy-ebay)
- **RP service prices (vendor guides, self-reported).**
  - About €150–500 per year for a dedicated service; another guide says €30–150 per year per product category.
  - Etsy partner providers run about $200–600 per year.
  - Flat offers include "€150/yr unlimited SKUs" and "from €199/yr", sometimes with €50–300 setup fees.
  - Running your own EU entity costs about €3,000–15,000 per year.
  - Sources: [EUverify](https://euverify.com/resource/eu-responsible-person-under-gpsr/); [eugpsr.eu](https://eugpsr.eu/blog/gpsr-cost-pricing-guide); [ShieldMyShop](https://www.shieldmyshop.com/blog/2026-03-23-etsy-gpsr-compliance-eu-sellers-2026); [Easecert](https://easecert.com/pages/understand-the-gpsr-cost-and-responsible-person-cost-for-your-products); [EU Compliance Partner](https://eucompliancepartner.com/eu-responsible-person-service)
- **Shopify GPSR apps (prices self-reported; review counts are snapshots).**
  - Meetanshi: $9.99/mo or $99/yr, 0 reviews — [Shopify](https://apps.shopify.com/meetanshi-eu-gpsr-compliance)
  - GPSReady: free for 10 products, then $7.99 or $14.99/mo — [Shopify](https://apps.shopify.com/gpsready)
  - GPSR Suite: free, Pro $12.90/mo — [Shopify](https://apps.shopify.com/gpsr-suite)
  - Safix: free, $12.90 or $24.90/mo, 0 reviews — [Shopify](https://apps.shopify.com/safix)
  - Alnage: free, $9.95 or $24.95/mo, 0 reviews — [Shopify](https://apps.shopify.com/gpsr-compliance-hub)
  - Kedalion: $29/mo — [Shopify](https://apps.shopify.com/kedalion-gpsr)
  - ShopCompliance: free, $29/mo, or $199/mo agency tier; covers GPSR plus other EU rules — [Shopify](https://apps.shopify.com/shopcompliance)
  - Roundup of these apps — [Meetanshi blog](https://meetanshi.com/blog/eu-gpsr-apps-shopify/)
- **Shopify GPSR traction.** Only GCM GPSR Compliance Manager has meaningful reviews (about 29, rated 4.9, mostly German merchants). GPSR Product Safety Info, GPSR Kit, GPSR Ready, GPSRReady, GPSR Safety Sync and GPSRKit all showed 0 reviews, and several list launch dates in mid-2026. — [GCM reviews](https://apps.shopify.com/gpsr/reviews); [GPSR Kit](https://apps.shopify.com/gpsr-kit); [GPSR Safety Sync](https://apps.shopify.com/gpsr-safety-sync); [GPSR Product Safety Info](https://apps.shopify.com/priceproof-gpsr)
- **No GPSR omnibus found.** The 2026 product-labelling omnibus covers energy and tyre labelling (procedure 2026/0169(COD), 24 June 2026). A separate CLP/chemicals omnibus covers chemical labels. I found nothing amending GPSR. — [EP Legislative Observatory](https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1906822); [Council document](https://data.consilium.europa.eu/doc/document/WK-9706-2025-INIT/en/pdf)
- **Who is exposed: Etsy.** Etsy had about 5.6 million active sellers in 2025 and 5.706 million in Q2 2026 (secondary sources). The figure conflicts with a Marketplace Pulse estimate of 5.4 million (Q2 2025) and a Yaguara figure of 8.1 million. — [Branvas](https://branvas.com/blogs/news/etsy-statistics-sellers-buyers-gms-fees); [Appfigures](https://appfigures.com/resources/insights/20251107/2-etsys-marketplace-has-how-many-sellers); [Printful](https://www.printful.com/uk/blog/etsy-statistics)
- **Who is exposed: Shopify in the EU.** Germany had 121,343 active Shopify stores (June 2026) and France about 117,900. The five largest EU markets (DE, FR, NL, ES, IT) hold about 446,000 live stores (Storeleads data via a secondary blog). — [EightX DE](https://eightx.co/blog/germany-shopify-landscape); [EightX EU](https://eightx.co/blog/eu-shopify-landscape)

### Inferences
- **Who pays for what.** Small sellers mostly self-serve inside the marketplace UIs at no cost. The money goes to RP services, and an RP must be an EU-established operator. A Brazilian solo developer cannot legally be the RP and could only refer or resell, which is an affiliate model, not software.
- **Little willingness to pay for display apps.** Fifteen or more Shopify apps with near-zero reviews after up to 18 months suggests little demand for "show GPSR info" apps; theme metafields cover it. A free GPSR safety-text and label PDF generator could work as an SEO lead magnet for another product, but not as a business.
- **Self-serve behaviour.** Sellers search and fill fields themselves, and many non-EU sellers opt out of the EU instead (Etsy offers the opt-out; the Amazon "exit" threads).

### Gaps
- The exact wording of GPSR Art. 19 (online information duties: manufacturer, RP, product identification, warnings) and Art. 44 (penalties) was not verified on EUR-Lex: fetching failed and the search budget ran out.
- No statistics on enforcement against small sellers (Safety Gate, national market surveillance).
- No search-volume or Trends data.

---

## 2. EU packaging: EPR registrations for online sellers (Germany LUCID/VerpackG, France, Spain) and the PPWR (applies from 12 Aug 2026). What sellers need and what services charge

### Takeaway
Selling packaged goods to consumers requires a separate registration in each country:
- **Germany:** LUCID registration is free, but a paid dual-system licence is also needed; marketplaces must verify both.
- **France:** a unique identifier (UID) per waste stream; marketplaces verify it and suspend listings without it.
- **Spain:** a separate registry (not researched).

The PPWR has applied since 12 Aug 2026 with no adopted delay, but harmonised labels slip to at least Aug 2028. The live 2026 pain is Art. 45: a producer selling into a Member State where it is not established must appoint an authorised representative (AR) there. The Council (24 June 2026) dropped the Commission's omnibus proposal to suspend that duty; Parliament's committee position was pending (vote planned 1 Oct 2026, outcome unverified).

The market is service-heavy (licences, AR mandates), and providers' calculators are free. The software-only gap is thin.

### Cited Findings
- **Germany: LUCID and marketplaces.**
  - LUCID registration is free, and every "manufacturer" of packaging, domestic or foreign, must register individually. — [Reverb Help](https://help.reverb.com/hc/en-us/articles/41988368280731-VerpackG-Packaging-Act-requirements-impacting-shops-selling-to-Germany)
  - Marketplaces must verify a valid LUCID registration and, where applicable, dual-system participation before any sales into Germany. — [Reverb Help](https://help.reverb.com/hc/en-us/articles/41988368280731-VerpackG-Packaging-Act-requirements-impacting-shops-selling-to-Germany)
  - Amazon is legally required to check LUCID registration. — [Sonko Consulting](https://www.sonko-consulting.com/guides/lucid-packaging-register-germany)
- **Germany: who and what it costs.**
  - For direct shipments to German consumers, the foreign seller is the producer, and the obligation starts with the first item sold (no minimum quantity). — [Sonko Consulting](https://www.sonko-consulting.com/guides/lucid-packaging-register-germany); [NXT Milestone](https://nxtmilestone.com/en/blog/lucid-packaging-register-and-dual-system-operators/lucid-for-online-retailers/)
  - The licence contract with a dual system is priced per kilogram of packaging material. — [NXT Milestone](https://nxtmilestone.com/en/blog/lucid-packaging-register-and-dual-system-operators/lucid-for-online-retailers/)
- **Germany: fines.** Most sources cite fines of up to €200,000. One splits them into up to €100,000 for missing registration and up to €200,000 for missing system participation. — [Deutsche Recycling](https://deutsche-recycling.com/blog/how-to-register-service-packaging-in-germany/); [PPWR Copilot](https://ppwrcopilot.com/ppwr-de-lucid-registration-guide)
- **Germany: non-EU sellers.** Sellers without an EU establishment who ship directly to German consumers reportedly must also name a Germany-based AR; the LUCID registration stays in the seller's own name (single vendor source). — [EU Compliance Partner](https://eucompliancepartner.com/epr-packaging)
- **Germany: licence prices.** A commission-based comparison site lists a Lizenzero licence at about €39 per year (€35.88 with voucher) and calls Reclay "Activate" the cheapest for very small quantities. Lizenzero's own calculator prices by annual kilograms per material. — [verpackungslizenz24](https://verpackungslizenz24.de/en/lizenzero-packaging-license/); [Interzero/Lizenzero](https://alliance.interzero.de/en/packaging-licensing/lizenzero-online-shop/)
- **France.**
  - Since January 2022, marketplaces must ensure third-party sellers comply. Producers get a UID for each waste stream from ADEME through a compliance scheme and give it to the marketplace. — [Reverb Help (France EPR)](https://help.reverb.com/hc/en-us/articles/4415573615891-Extended-Producer-Responsibility-EPR-in-France)
  - Amazon, eBay, ManoMano and Cdiscount must check EPR numbers (art. L.541-10-9) and suspend listings without them. — [Regsurance](https://regsurance.com/france-extended-producer-responsibility-epr-service-guide-registration-data-reporting/); [Circular Pro FAQ](https://circular-pro.com/faq/france/)
  - France required non-EU producers to appoint an AR before the PPWR made it uniform (vendor claim). — [EPR Representative FAQ](https://eprrepresentative.com/faq)
- **PPWR application date.** It applies from 12 Aug 2026. No amendment, Council decision or Commission proposal delaying the core date has been adopted. — [Packa fact-check (July 2026)](https://contenthub.packa.com/ppwr-postponement-fact-check-2026); [ppwr-packaging.com](https://ppwr-packaging.com/articles/ppwr-delayed/)
- **PPWR labelling timing.**
  - The harmonised Art. 12 label applies from 12 Aug 2028, or 24 months after the implementing acts, whichever is later. The implementing act due by 12 Aug 2026 was missed. — [Envirotec (19 Aug 2026)](https://envirotecmagazine.com/2026/08/19/eu-misses-deadline-for-ppwr-labelling-rules/); [ComplianceGate](https://www.compliancegate.com/ppwr-timeline-and-dates/)
  - Only the ban on misleading recyclability, recycled-content, compostability and reusability claims (Art. 12(8)) applies now. — [ppwr-packaging.com](https://ppwr-packaging.com/articles/ppwr-delayed/)
- **Old stock.** A summary of the Commission's second FAQ edition (3 Aug 2026) says packaging produced before 12 Aug 2026 need not be relabelled. — [Latham & Watkins](https://www.lw.com/en/insights/european-packaging-and-packaging-waste-regulation-summary-of-provisions-and-new-guidance)
- **Art. 45 authorised representative.** Since 12 Aug 2026, the AR must be appointed by written mandate in every country where a producer makes packaged products available without being established there. There is no single EU-wide representative and no one-stop mechanism. One source says the duty also covers EU producers selling cross-border. — [Coolset](https://www.coolset.com/academy/ppwr-authorised-representative); [Ecosistant](https://www.ecosistant.eu/en/epr-authorized-representative-guide/); [EPR Representative](https://eprrepresentative.com/guides/ppwr-article-45)
- **Environmental omnibus: Council.** The 10 Dec 2025 package proposed suspending the AR duty (reported as until 2035 for EU-based companies). The Council's 24 June 2026 mandate did not proceed with the suspension, which a large majority of Member States opposed, and deleted the proposed 12-month maximum reporting frequency. — [ERP (Aug 2026)](https://erp-recycling.org/news-and-events/2026/08/environmental-omnibus-council-adopts-position-and-envi-drafts-epr-simplification-reports/)
- **Environmental omnibus: Parliament.** The ENVI rapporteur's draft (Ingeborg ter Laak) would limit the suspension to micro and small enterprises, with a sunset at the Circular Economy Act or 1 Jan 2035, and delete the option for Member States to require an AR from third-country producers. The committee vote was planned for 1 Oct 2026, with plenary in October. — [ERP (June 2026)](https://erp-recycling.org/news-and-events/2026/06/environmental-omnibus/); [ERP (Aug 2026)](https://erp-recycling.org/news-and-events/2026/08/environmental-omnibus-council-adopts-position-and-envi-drafts-epr-simplification-reports/); [Afera](https://afera.com/news/ppwr-unpacked-–-part-12-envi-decides-on-amendments-to-e.u.-packaging-regulation/)
- **Crowded supply side.** Many AR and EPR service firms and AI-branded newcomers target marketplace sellers. — [EU Compliance Partner](https://eucompliancepartner.com/epr-packaging); [Ecosistant](https://www.ecosistant.eu/en/eu-packaging-regulation-e-commerce/); [EPR Representative](https://eprrepresentative.com/ppwr-2026-compliance); [Regsurance](https://regsurance.com/france-extended-producer-responsibility-epr-service-guide-registration-data-reporting/); [Valpak](https://www.valpak.co.uk/?p=5536); [ppwrcopilot.com](https://ppwrcopilot.com/ppwr-de-lucid-registration-guide); [epr.eldris.ai](https://epr.eldris.ai/ppwr/); [Manageit](https://manageit.io/en/blog/ppwr-online-sellers-producer/)

### Inferences
- **What sellers need:**
  1. per-country registration (DE LUCID, FR UID per stream, ES registry);
  2. paid licences or eco-fees by weight;
  3. periodic quantity reports;
  4. since Aug 2026, a local AR in each country where they are not established (the heaviest burden for non-EU sellers such as Brazilians).
- **Why software can't capture this.** Items 2 and 4 are services that require local legal entities. Software can only add an obligation tracker or a weight calculator, and providers already give these away. Low opportunity; at most an affiliate comparison site, since commission-based partner programs exist (verpackungslizenz24 discloses one).
- **Prices.** German licensing starts very low (about €39 per year). The pain is the number of registrations, the reporting and the AR fees, not the price of the licence itself.

### Gaps
- Spain (registro de productores de envases) was not covered by any result.
- AR service prices per country were not found.
- The outcome of the 1 Oct 2026 ENVI vote is unverified.
- Etsy-specific LUCID enforcement is unverified.

---

## 3. EUDR: latest dates and simplifications, operator and trader duties, what Brazilian exporters must supply, tools and prices, room for a cheap tool for small Brazilian coffee or cocoa producers

### Takeaway
- **Dates are final.** Regulation (EU) 2025/2650 (OJ, 23 Dec 2025) fixes 30 Dec 2026 for large and medium operators and 30 Jun 2027 for micro and small ones. The Commission's review of 4 May 2026 proposed no further legislative simplification and no further postponement.
- **Who files.** Downstream operators and traders no longer file due diligence statements (DDS); they keep upstream reference numbers. Only micro and small primary operators in low-risk countries get a simplified declaration. Brazil is "standard risk", so full due diligence applies to EU operators sourcing from Brazil.
- **Brazilian producers.** They have no direct legal obligation but must give buyers plot geolocation (polygons, or points for plots under 4 ha) and legality data. For coffee this is largely solved for free or at the industry level:
  - the Cecafé–Serasa platform covers more than 50 exporters, almost all EU-bound coffee;
  - Conab's free Parque Cafeeiro platform;
  - the Ministry of Agriculture's (MAPA) free Agro Brasil + Sustentável.
- **Where the gap is.** A paid tool for Brazilian smallholders has little room. The real price gap is on the EU side: micro and small operators face either the free manual TRACES interface or platforms costing €3,000–4,000+ per year.

### Cited Findings
- **Dates.**
  - Large and medium operators apply from 30 Dec 2026; micro and small operators (and natural persons) from 30 Jun 2027, under Regulation (EU) 2025/2650. — [EC Access2Markets](https://trade.ec.europa.eu/access-to-markets/en/news/delay-until-december-2026-and-other-developments-implementation-eudr-regulation); [Stibbe](https://www.stibbe.com/publications-and-insights/the-amended-eudr-what-has-changed-and-what-has-remained); [EUSTAFOR](https://eustafor.eu/eudr-amendment-parliament-and-council-align-on-delay-and-simplifications/)
  - The regulation was published in the Official Journal on 23 Dec 2025. — [Coolset timeline](https://www.coolset.com/academy/eudr-delay-2025-explained)
- **May 2026 review.**
  - Published 4 May 2026 (some outlets say 3 May). The Commission does not consider further legislative simplification appropriate "to preserve legal certainty", and there will be no postponement. — [IntegrityNext](https://www.integritynext.com/resources/blog/article/eudr-review-out-now-minor-simplifications-same-deadline); [Global ELR (May 2026)](https://www.globalelr.com/2026/05/european-commission-releases-new-eu-deforestation-regulation-measures/); [HLC](https://www.hlc.com/en/publications/eu-deforestation-regulation-commission-publishes-simplification-package-ahead-of-december-2026); [Cattwyk](https://www.cattwyk.com/en/news/eudr-update-vereinfachungspaket-veroeffentlicht)
  - The package adds a draft delegated act on product scope, updated guidance and FAQs, and an updated implementing act on the Information System. — same sources
  - The Commission projects about 75% lower annual compliance costs than the original EUDR (secondary coverage; a projection, not a measured outcome). — [TraceX](https://tracextech.com/eudr-simplification-package-2026/)
- **Downstream operators and traders.** They no longer submit their own DDS but collect and keep upstream reference numbers. Non-SME downstream operators and traders must still register in the Information System. Secondary sources add that only the first downstream operator must keep the reference numbers. — [EC Access2Markets](https://trade.ec.europa.eu/access-to-markets/en/news/delay-until-december-2026-and-other-developments-implementation-eudr-regulation); [Coolset](https://www.coolset.com/academy/the-eu-deforestation-regulation-eudr-what-businesses-need-to-know-and-do)
- **Simplified declaration.** Micro and small primary operators in low-risk countries file a single simplified declaration (new Annex III) instead of a DDS. Secondary sources say postal codes can replace precise geolocation. Coolset's own guides contradict each other ("not yet legally binding" vs "now in force") and cite an Implementing Regulation (EU) 2026/1565 of 13 July 2026 that I could not verify. — [EC Access2Markets](https://trade.ec.europa.eu/access-to-markets/en/news/delay-until-december-2026-and-other-developments-implementation-eudr-regulation); [Coolset SME guide](https://www.coolset.com/academy/eudr-reporting-guide-for-smes)
- **Brazil is standard risk.** The May 2025 implementing regulation lists only Russia, Belarus, Myanmar and North Korea as high risk. All others, including Brazil, Peru, Colombia and DR Congo, are standard risk. — [Fieldfisher](https://www.fieldfisher.com/en/insights/the-eu-deforestation-regulation-european-commission-classifies-countries-as-high-low-or-standard-risk)
- **Micro/small definition and date.** Two of three criteria: under 50 employees, turnover under €10M, balance sheet under €10M. Products already covered by the EU Timber Regulation (EUTR) keep the 30 Dec 2026 date. — [osapiens](https://osapiens.com/?p=20476)
- **What Brazil must supply (Cecafé, Sept 2026).**
  - Producers outside the EU have no direct obligation, but EU operators will ask suppliers for the information their due diligence needs, including geolocation of the plots (talhões) where the coffee grew. — [Campo Vivo (8 Sep 2026)](https://campovivo.com.br/apresentado-por-prime-cafe/2026/09/08/rastreabilidade-passa-a-definir-o-acesso-do-cafe-brasileiro-ao-mercado-europeu/); [Canal Rural](https://www.canalrural.com.br/agricultura/cecafe-destaca-rastreabilidade-para-atender-exigencias-do-mercado-externo/); [Cecafé EUDR page](https://www.cecafe.com.br/assuntos/eudr/)
  - Smallholders struggle most, because of technical limits and land-tenure irregularity. — [Campo Vivo](https://campovivo.com.br/apresentado-por-prime-cafe/2026/09/08/rastreabilidade-passa-a-definir-o-acesso-do-cafe-brasileiro-ao-mercado-europeu/)
- **Existing Brazilian platforms.**
  - The Cecafé "Plataforma de Monitoramento Socioambiental Cafés do Brasil", built with Serasa Experian, traces coffee to the production polygon and produces auditable documentation. More than 50 exporting companies and cooperatives use it, covering nearly all coffee shipments to the EU. — [Campo Vivo](https://campovivo.com.br/apresentado-por-prime-cafe/2026/09/08/rastreabilidade-passa-a-definir-o-acesso-do-cafe-brasileiro-ao-mercado-europeu/)
  - Conab's "Plataforma Parque Cafeeiro" (AI plus satellite imagery) lets producers issue non-deforestation declarations directly and exporters obtain lot-regularity proofs. — [IT Show](https://itshow.com.br/plataforma-rastreabilidade-cafe-ia-satelites-eudr/)
  - In April 2026, Cecafé asked the Commission to recognise Brazil's official data for operators' due diligence. — [Cecafé](https://www.cecafe.com.br/assuntos/eudr/)
- **MAPA's Agro Brasil + Sustentável.** Built by MAPA and Serpro with Embrapa, free and voluntary. It integrates identity, property-registry, labour and environmental systems. It was not originally designed for traceability, and its acceptance by EU importers is unconfirmed. — [O Presente Rural](https://opresenterural.com.br/agro-em-codigo-2025-debate-rastreabilidade-e-preparo-do-brasil-para-atender-a-lei-europeia/); [AgFeed](https://agfeed.com.br/esg/governo-lanca-plataforma-digital-do-agro-sustentavel-com-pendencias-pelo-caminho); [Agrolink](https://www.agrolink.com.br/noticias/produtores-contribuem-para-aperfeicoamento-da-plataforma-agrobrasil-sustentavel_514126.html)
- **Geolocation format and limits.**
  - TRACES requires GeoJSON. — [Qarma](https://www.qarmainspect.com/blog/how-to-submit-geolocation-data-geojson-for-eudr-compliance)
  - One vendor's reading of TRACES: polygons or multi-polygons, no self-intersections, CRS84, 2D only, 10 MB upload limit. — [LiveEO TradeAware docs](https://docs.live-eo.com/tradeaware/using-the-tradeaware-web-app/plot-upload-and-analysis-trouble-shooting)
  - Plots under 4 ha may use a single GPS point. — [osapiens docs](https://docs.osapiens.com/supplier-portal/docs/en/small-land-plots-guide)
  - Common errors are unclosed rings, syntax errors and invalid coordinates. — [TraceX](https://tracextech.com/geojson-file-errors/)
- **Free tools.** geojson.io is the most recommended free option. The European Forest Institute's GeoRoots Editor (Feb 2026) is an open-source browser tool to create, clean, verify and export plot GeoJSON. I found no standalone free validator. — [Qarma](https://www.qarmainspect.com/blog/how-to-submit-geolocation-data-geojson-for-eudr-compliance); [EFI](https://efi.int/news/georoots-editor-accessible-secure-and-eudr-ready-geodata-editing-directly-your-browser-2026-02)
- **Paid tool prices (self-reported).**
  - LiveEO TradeAware Professional, "for SME operators": €399/mo or €3,990/yr, including DDS creation and auto-submission to TRACES for 50 DDS a year. A free Lite tier only consumes reference numbers. — [TradeAware pricing](https://www.live-eo.com/tradeaware-pricing)
  - Polygon One from about €3,000 per year; most other providers publish no price. — [Polygon One comparison](https://polygon-one.com/en/article-eudr-software-comparison)
  - Enterprise quotes of about €10,000–50,000 per year. — [Qelvyn](https://qelvyn.co/en/blog/eudr/farm-plot-mapping-cost-cooperatives-eudr)
  - Tracebud charges buyers and keeps its field app free for farmers. — [Tracebud](https://www.tracebud.com/en/resources/evaluate-eudr-due-diligence-tools-sme-supply-chains)
  - osapiens offers an "Easy Start" SME package (no price found). — [osapiens](https://osapiens.com/?p=20476)
- **Field-mapping costs.**
  - About $4 per farm in an Ethiopian cooperative programme (no named source). — [Qelvyn](https://qelvyn.co/en/blog/eudr/farm-plot-mapping-cost-cooperatives-eudr)
  - About $6–14 per plot in Indonesia. — [EUDR Indonesia](https://eudrindonesia.com/eudr-smallholder-mapping-service-indonesia/)
  - Offline collection apps for cocoa cooperatives at €15,000–43,000. — [Kolonell](https://kolonell.com/en/blog/cocoa-cooperative-traceability-software-eudr-cost-amsterdam-2026)
  - Free NGO apps also exist. — [TechnoServe](https://www.technoserve.org/blog/eu-deforestation-regulation-mobile-app/)

### Inferences
- **Brazilian producers and cooperatives (the brief's idea).** Weak. Large exporters and cooperatives already use the Cecafé–Serasa platform; the government offers free tools (Conab, MAPA); and the farmer is not the legal filer. Willingness to pay at the smallholder level is low, and Brazilian farms are lower-purchasing-power buyers than EU firms. **Exclude.**
- **Better EUDR niche: EU micro and small operators.** Examples are specialty-coffee importers and roasters buying direct, craft chocolate makers, and small importers of wooden goods or leather. They face a clear price gap between the free manual TRACES interface or geojson.io and platforms at €3,000–4,000 a year. A €29–99/month self-serve kit could fit: supplier data-collection links in Portuguese and Spanish, GeoJSON build, validation and fixing to TRACES constraints, a due-diligence file and a 5-year archive. A Brazilian, Portuguese-speaking developer has a real edge on the supplier side, since Brazil is a top coffee origin.
- **Timing.** Medium and large operators face 30 Dec 2026, so selling can start in Q4 2026. Micro and small operators face 30 Jun 2027, so their demand peaks in H1 2027.
- **Self-serve demand (inferred).** SMEs appear to be searching: vendors publish heavy, recently updated SEO content ("GeoJSON errors", "SME reporting guide", updated June–Sept 2026). This is indirect; no search-volume data was gathered.

### Gaps
- The number of EU operators and traders registered in TRACES/EUDR IS was not found.
- Whether a public API for third-party DDS submission exists (TradeAware's "auto-submit" implies one) is unverified.
- The EUDR penalty provisions (Art. 25) were not re-verified this session.
- The content of the draft delegated act on scope was not checked (for example, whether printed products leave scope).
- Cocoa readiness (CNC, Bahia, Pará), cattle/leather, soy, rubber and palm specifics were not researched; Embrapa and Notícias Agrícolas were not reached.

---

## 4. CBAM: the definitive regime from 2026 and the 50-tonne de minimis threshold. SMB opportunity or enterprise only?

### Takeaway
The definitive period started on 1 Jan 2026. Omnibus I (Regulation (EU) 2025/2083) set a single cumulative threshold of 50 tonnes per importer per year, which exempts about 90% of importers (about 182,000) while keeping about 99% of embedded emissions in scope. Importers above it must be authorised CBAM declarants. Certificates go on sale in Feb 2027, and the first annual declaration (covering 2026) is due 30 Sept 2027. The remaining importers are mostly mid-sized or large metals, fertiliser and cement buyers. Free and €2,000+/year tools exist, and the rest sell through demos. **Enterprise-ish; exclude.**

### Cited Findings
- **Definitive period.** A single 50-tonne yearly threshold replaced the €150 per-consignment exemption. Importers above it must hold authorised-declarant status; those who applied by 31 Mar 2026 could keep importing while their application was processed. — [Bird & Bird (2026)](https://cm.twobirds.com/en/insights/2026/italy/cbam-lavvio-del-periodo-definitivo-e-lobbligo-di-ottenere-lo-status-di-dichiarante-cbam-autorizzato); [CargoLinked](https://cargolinked.com/guides/cbam-definitive-period-2026-importer-guide); [BSI](https://www.bsigroup.com/en-GB/insights-and-media/insights/blogs/preparing-for-eu-cbam-the-20262027-transition-explained)
- **Timeline.** First annual declaration 30 Sept 2027; certificates sold from Feb 2027. Under Regulation (EU) 2025/2083, the certificate-holding requirement fell from 80% to 50% of embedded emissions. — [Customs Support](https://www.customssupport.com/cbam-changes-in-2026/); [BSI](https://www.bsigroup.com/en-GB/insights-and-media/insights/blogs/preparing-for-eu-cbam-the-20262027-transition-explained)
- **Who is exempt.** The 50-tonne threshold exempts about 90% of importers (about 182,000; one source says 91%) while keeping about 99% of emissions in scope. It covers iron and steel, aluminium, cement and fertilisers. Sources conflict on whether hydrogen and electricity are inside the exemption. — [MHA](https://mha.co.uk/insights/eu-announces-major-cbam-simplifications-reduced-compliance-burden-for-smes); [A&L Goodbody](https://www.algoodbody.com/insights-publications/omnibus-package-amendments-proposed-to-the-carbon-border-adjustment-mechanism); [Malta Climate Action](https://climateaction.gov.mt/cbam/)
- **Status.** Proposed 26 Feb 2025, provisionally agreed June 2025, adopted by the Council in late Sept 2025, effective 1 Jan 2026. The threshold is reviewed annually to keep 99% coverage. — [SGS](https://ecustoms.sgs.com/?p=14354); [Cassidy Levy](https://www.cassidylevy.com/?p=2746); [UABIO](https://uabio.org/en/news/17569/)
- **Non-EU producers.** A producer exporting under 50 tonnes may still have to report data to an EU customer whose total imports exceed the threshold. — [Mondaq](https://www.mondaq.com/india/oil-gas-electricity/1648112/eu-simplifies-cbam-but-does-not-address-the-underlying-issues)
- **Tools and prices.**
  - The Sustainability Cloud: €0 importer plan, with add-ons such as €50 for a monthly bundle of 5 imports. — [Sustainability Cloud](https://www.thesustainabilitycloud.com/eu-cbam-for-importers-pricing/)
  - Dubrink: €1,990/yr up to 1,000 t, €2,990/yr up to 15,000 t. — [CBAM Guide: Dubrink](https://cbamguide.com/software/dubrink/)
  - CBAMBOO: reportedly €9,000–19,000/yr (unconfirmed). — [CBAM Guide: CBAMBOO](https://cbamguide.com/software/cbamboo/)
  - CarbonChain: quote only, with a free cost estimator. — [CBAM Guide: CarbonChain](https://cbamguide.com/software/carbonchain/)
  - Only one of ten vendors publishes a price list. — [CBAM Guide pricing](https://cbamguide.com/software/pricing/)
  - Certificate reference price: €75.28/tCO₂e for Q2 2026. — [CBAM Guide pricing](https://cbamguide.com/software/pricing/)

### Inferences
- **SMB opportunity: minimal.** Sub-50-tonne importers are exempt and need at most a cumulative tonnage tracker, which is a spreadsheet. Importers above the threshold need emissions data from suppliers and verifiers; free and €2,000+ tools already serve them, and buying is consultative.
- **Brazilian exporters.** Steel, pig-iron and aluminium exporters are large firms. **Exclude: enterprise sale.**

### Gaps
- The official Commission figures were not opened; they were confirmed only through law-firm summaries.
- No data on how many authorised-declarant applications were filed or approved.
- CBAM penalties were not checked.

---

## 5. E-invoicing mandates (Germany, Belgium, Poland KSeF, France, Croatia, others): is a small freelancer/SMB generator, validator or converter viable without certification?

### Takeaway
The mandates are confirmed and staggered:
- **Germany:** receiving since 1 Jan 2025; issuing from 1 Jan 2027 if prior-year turnover exceeds €800,000; everyone from 1 Jan 2028.
- **Belgium:** Peppol B2B since 1 Jan 2026; tolerance ended 31 Mar 2026.
- **Poland (KSeF):** 1 Feb 2026 and 1 Apr 2026; micro firms from 1 Jan 2027. The penalty start may slip to 1 Jan 2028 (draft only).
- **France:** all companies must receive from 1 Sept 2026; SMEs issue from 1 Sept 2027, through 101–149 state-approved platforms.
- **Croatia:** VAT-registered B2B from 1 Jan 2026; non-VAT entities from 1 Jan 2027.
- **Spain:** Verifactu delayed to 2027, with a conflicting report of Oct 2028.

Every market already has free generators, bundled accounting suites and certified platforms. France and Belgium route invoices through approved or accredited intermediaries. A non-certified solo tool would be a commoditised converter or validator. **Trap.**

### Cited Findings
- **Germany: dates.** All domestic B2B businesses must be able to receive e-invoices since 1 Jan 2025. Those with prior-year (2026) total turnover above €800,000 must issue them from 1 Jan 2027; everyone else from 1 Jan 2028. — [kostenlose-erechnung.de](https://kostenlose-erechnung.de/ratgeber/e-rechnungspflicht-2027-versandpflicht/); [ETL](https://www.etl.de/aktuelles/e-rechnung-erste-uebergangsfrist-laeuft-aus-2026/); [Börse Express](https://www.boerse-express.com/news/articles/e-rechnung-pflicht-ab-januar-2027-fuer-unternehmen-ueber-800000-euro-929362)
- **Germany: small-business exemption (sources conflict).** Some say Kleinunternehmer (§19 UStG) are permanently exempt from issuing (§34a UStDV); others say they must issue from 2028. All agree they must be able to receive. — [kostenlose-erechnung FAQ 2026](https://kostenlose-erechnung.de/ratgeber/e-rechnung-pflicht-faq-2026/); [Qonto](https://qonto.com/de/blog/kmu/management-buchhaltung/e-rechnungspflicht-welche-regeln-gelten-ab-wann)
- **Germany: other exemptions, push-back and fines.**
  - Exempt: small-amount invoices up to €250 gross, invoices to consumers and certain tax-exempt supplies. — [ETL](https://www.etl.de/aktuelles/e-rechnung-erste-uebergangsfrist-laeuft-aus-2026/)
  - The German crafts federation (ZDH) asks to move the 2027 stage to 2028; no law found. — [Börse Express](https://www.boerse-express.com/news/articles/e-rechnung-pflicht-ab-januar-2027-fuer-unternehmen-ueber-800000-euro-929362)
  - Fines up to €5,000 (§26a(3) UStG). — [kostenlose-erechnung FAQ](https://kostenlose-erechnung.de/ratgeber/e-rechnung-pflicht-faq-2026/)
- **Germany: free tools.** A free e-invoice generator site and accounting suites (sevDesk and others) already serve freelancers. — [kostenlose-erechnung.de](https://kostenlose-erechnung.de/ratgeber/e-rechnungspflicht-bin-ich-betroffen/); [sevDesk](https://sevdesk.de/blog/e-rechnung-update/)
- **Belgium: mandate and penalties.**
  - Since 1 Jan 2026, all Belgian VAT-registered companies must send and receive structured B2B e-invoices via Peppol. — [Marosa](https://marosavat.com/vat-news/e-invoicing-b2b-belgium-complete-guide-january-2026)
  - No sanctions from 1 Jan to 31 Mar 2026 if reasonable steps were taken; no general postponement. — [Orbitax](https://orbitax.com/news/country/article/Belgium-Provides-Three-Month-P-60564); [Accountable](https://www.accountable.eu/en-be/blog/e-invoicing-tolerance-period/)
  - Grace period ended 1 Apr 2026. Fines reported as €1,500, €3,000 and €5,000 for first, second and subsequent offences. — [Innovate Tax](https://innovatetax.com/blog/belgian-einvoicing-penalties/)
  - One provider offers Peppol registration free "in 2 minutes". — [e-invoice.app](https://e-invoice.app/guides/belgium-e-invoicing)
- **Poland (KSeF).**
  - Mandatory from 1 Feb 2026 for businesses with 2024 sales above PLN 200M and from 1 Apr 2026 for the rest. Businesses invoicing up to PLN 10,000 gross a month have until 1 Jan 2027.
  - Penalties under Art. 106ni VAT Act start 1 Jan 2027. On 16 Sept 2026 the Ministry of Finance announced it would extend penalty relief to 31 Dec 2027; a draft (2 Oct 2026) would postpone penalties to 1 Jan 2028. Not yet adopted, and the KSeF obligation itself is unchanged.
  - Sources: [Sovos (2 Oct 2026)](https://sovos.com/regulatory-updates/global-vat/poland-draft-law-published-to-postpone-ksef-penalties-until-2028/); [Sovos](https://sovos.com/regulatory-updates/vat/poland-ministry-of-finance-extends-ksef-penalty-relief-until-end-of-2027/); [Fiscal Requirements](https://www.fiscal-requirements.com/news/6020-e-invoicing-in-poland-penalty-deadline-proposed-to-be-extended-until-2028)
- **France.**
  - Since 1 Sept 2026 every company must be able to receive e-invoices; large companies and mid-caps (ETI) must also issue. SMEs, very small firms and micro-entrepreneurs issue from 1 Sept 2027. — [Previssima](https://www.previssima.fr/actualite/facturation-electronique-ce-qui-change-pour-les-entreprises-des-le-1er-septembre-2026.html)
  - Flows go through DGFiP-approved platforms (PA/PDP). The tax authority published the first 101 on 16 Jan 2026; one article counts 149 at go-live. — [CAPEB](https://www.capeb.fr/actualites/facturation-electronique-la-liste-des-101-premieres-plateformes-agreees-est-disponible); [Presse-citron](https://www.presse-citron.net/facturation-electronique-entre-vigueur-aujourdhui-voici-149-plateformes-agreees-france/); [Ecosio](https://ecosio.com/fr/blog/e-invoicing-and-e-reporting-in-france/)
- **Croatia.** Mandatory B2B and B2G e-invoicing plus real-time e-reporting for VAT-registered taxpayers from 1 Jan 2026; non-VAT businesses and public bodies from 1 Jan 2027; intra-EU supplies from 1 Jul 2030. — [VATCalc](https://www.vatcalc.com/croatia/croatia-mandates-b2b-e-invoicing-2025/); [e-invoice.app HR](https://www.e-invoice.app/country/HR)
- **Spain (sources conflict).** Royal Decree-law 15/2025 (2 Dec 2025) delayed Verifactu to 1 Jan 2027 for corporate-tax payers and 1 Jul 2027 for the rest; the Ministerial Order activating the "Crea y Crece" B2B mandate was still pending in mid-2026. A conflicting report says Oct 2028 (unconfirmed). — [Tradeshift](https://tradeshift.com/?p=71104); [VATCalc](https://www.vatcalc.com/spain/spain-verifactu-delay-till-jan-2027-for-certified-e-invoicing/); [Fiscal Requirements](https://www.fiscal-requirements.com/news/6062-spain-announces-verifactu-postponement-until-october-2028-to-align-with-mandatory-e-invoicing)
- **Other countries (tables, partly "to be confirmed").** Greece, Feb 2026 (unverified); Estonia, 1 Jan 2027; Latvia and Luxembourg, Jan 2028. — [Marosa overview](https://marosavat.com/e-invoicing-in-europe-overview-and-dates/); [VATupdate (31 Jul 2026)](https://www.vatupdate.com/wp-content/uploads/2026/07/2026-07-31-Worldwide_E-Invoicing_Mandates_By_Region.pdf)

### Inferences
- **Germany.** No software certification is needed to create XRechnung or ZUGFeRD (training knowledge; not re-verified). That is exactly why free generators and every accounting suite already cover it, so willingness to pay is captured by incumbents.
- **France and Belgium.** France requires a state-approved platform (verified), so a solo tool could only be a front-end feeding a PA. Belgium uses accredited Peppol access points (accreditation from training knowledge, unverified), so a tool would sit on top of an access point's API. Both are commodity positions with free tiers.
- **Poland and Spain.** Local-language markets with strong domestic vendors. Poland's micro firms have lower purchasing power. Spain's dates are unstable.
- **Self-serve behaviour.** Freelancers and SMBs self-serve through their accounting software, so a standalone converter or validator has weak, price-sensitive demand. **Trap.**

### Gaps
- Counts of affected companies per country were not found.
- Greece is unverified; Spain's final Verifactu date is in conflict.
- Peppol access-point accreditation and Verifactu's "declaración responsable" (software self-declaration) mechanics were not re-verified this session.

---

## 6. Accessibility: EAA (since June 2025), ADA Title III suits and demand letters against small e-commerce, ADA Title II deadlines and DOJ changes, overlays, saturation of audit and monitoring tools

### Takeaway
- **EAA.** No confirmed EAA fine by mid-2026, but supervision has started (Sweden, Netherlands) and French disability associations are suing retailers.
- **ADA Title III.** Website suits rose in 2025 to 3,117 federal filings (Seyfarth) or 5,114 counting state courts (UsableNet); about 70% target e-commerce.
- **ADA Title II.** It covers only state and local governments. A DOJ interim final rule (20 Apr 2026) moved its deadlines to 26 Apr 2027 and 26 Apr 2028. That is government procurement: **exclude**.
- **Overlays are a trap.** The FTC fined accessiBe $1M, and widget users were named more than 1,400 times in 2025 lawsuits.
- **Audit and monitoring tools are saturated:** dozens of vendors, many of them indie. **Trap.**

### Cited Findings
- **EAA enforcement.**
  - No fine had been issued under any national EAA law as of a July 2026 review (Auditsu). A DisabilityWorld article claims a first German BFSG penalty in Q1 2026, which conflicts with the other sources. — [Auditsu](https://auditsu.com/resources/european-accessibility-act-fines); [DisabilityWorld](https://www.disabilityworld.org/articles/eaa-first-year-enforcement-report/)
  - Sweden's telecoms regulator (PTS) had opened 28 supervision cases into online shops by Mar 2026. The Dutch regulator (ACM) found 61% of the largest webshops it checked could not take an order with assistive technology. — [Atyantik](https://atyantik.com/blog/european-accessibility-act-enforcement/); [GetWCAG](https://getwcag.com/en/blog/european-accessibility-act-whats-next-in-2026)
  - French associations took four grocers to court; one case produced an order with a daily penalty, and an E.Leclerc hearing was set for 22 Sept 2026. — [Atyantik](https://atyantik.com/blog/european-accessibility-act-enforcement/)
  - Penalty ceilings vary by country (for example, Spain up to €1M; France €250k for repeat violations; vendor figures). — [WebYes](https://www.webyes.com/blogs/eaa-fines/); [Web Accessibility Checker](https://web-accessibility-checker.com/en/blog/eaa-fines-by-country)
- **ADA Title III suits.**
  - Seyfarth counted 3,117 federal website-accessibility suits in 2025, up 27% from 2,452 in 2024. — [UsableNet blog](https://blog.usablenet.com/ada-web-lawsuit-trends-2026); [TestParty](https://testparty.ai/blog/ada-lawsuit-trends-ecommerce-2025-2026-data)
  - UsableNet counted 5,114 digital suits in federal and state courts (3,195 federal). E-commerce was about 70% of all ADA web suits in 2025 (about 77% the year before), and 1,427 suits (45% of federal cases) hit repeat defendants. — [UsableNet 2025 Year-End Report](https://info.usablenet.com/hubfs/Remediated%20-%202025_Year-End_Digital_Accessibility_Lawsuit_Report_FINAL.pdf); [UsableNet midyear](https://blog.usablenet.com/2025-midyear-accessibility-lawsuit-report-key-legal-trends)
  - A tracker cites 5,006 federal filings across all Title III in H1 2026, not only websites (unconfirmed). — [Accessibility.build](https://accessibility.build/research/accessibility-lawsuits)
- **ADA Title II rule change.**
  - The DOJ interim final rule (published 20 Apr 2026, effective immediately) moves deadlines to 26 Apr 2027 for entities serving 50,000+ people and 26 Apr 2028 for smaller ones and special districts. WCAG 2.1 AA is unchanged; comments closed 22 Jun 2026; DOJ signals further review. — [Reed Smith](https://www.reedsmith.com/articles/doj-extends-digital-accessibility-compliance-dates-under-title-ii-of-the-ada/); [CFS Law Monitor](https://www.consumerfinancialserviceslawmonitor.com/2026/04/doj-extends-title-ii-ada-web-accessibility-rule-compliance-deadlines-for-state-and-local-governments/); [ADA Title III blog](https://www.adatitleiii.com/2026/04/doj-extends-ada-title-ii-website-accessibility-deadlines-for-governmental-entities-but-litigation-and-compliance-risks-remain/)
  - The separate HHS Section 504 deadlines (May 2026 / May 2027) remain. — [Jackson Lewis](https://www.jacksonlewis.com/insights/doj-extends-public-entities-compliance-deadline-ada-related-website-accessibility-hhss-may-2026-deadline-still-looms)
- **Overlays.**
  - The FTC final order requires accessiBe to pay $1M over claims that its widget could make any site WCAG-compliant and over undisclosed paid reviews. The complaint was announced Jan 2025; sources say the final order came around April 2025. — [TestParty](https://testparty.ai/blog/are-accessibility-overlays-legal)
  - UsableNet's 2025 data reportedly shows suits naming widget users more than 1,400 times. No federal decision holds that an overlay alone satisfies Title III. More than 700 professionals signed the Overlay Fact Sheet. These figures come via TestParty, a competitor of overlay vendors. — [TestParty data](https://testparty.ai/blog/accessibility-overlay-lawsuits-data); [TestParty](https://testparty.ai/blog/why-800-businesses-with-accessibe-were-still-sued); [A11y Collective](https://www.a11y-collective.com/blog/accessibility-overlays/)
- **Saturation.** A large set of SMB-oriented audit, monitor and "EAA checker" products publish competing guides. — [WebYes](https://www.webyes.com/blogs/eaa-fines/); [GetWCAG](https://getwcag.com/en/blog/european-accessibility-act-whats-next-in-2026); [TrustYourWebsite](https://trustyourwebsite.com/eu/en/guides/eaa-penalties); [Auditsu](https://auditsu.com/resources/european-accessibility-act-fines); [Web Accessibility Checker](https://web-accessibility-checker.com/en/eaa-compliance); [Level Access](https://www.levelaccess.com/blog/eu-accessibility-requirements-and-eaa-compliance/); [TestParty](https://testparty.ai/blog/ada-lawsuit-trends-ecommerce-2025-2026-data); [Abledly](https://abledly.com/blog/website-accessibility-lawsuits.html)

### Inferences
- **Why overlays are a trap.** They do not fix source code. Plaintiffs keep suing sites that use them. The FTC has already punished "instant compliance" marketing. Selling an overlay creates exposure to deceptive-claims liability and leaves clients exposed.
- **Audit and monitoring tools.** Willingness to pay is proven (fear of suits), but saturation is extreme. An automated scan catches only part of WCAG issues (general industry knowledge, not verified here) and cannot prevent suits, so churn and liability are high. Small e-commerce self-serves (installs widgets or scanners), but differentiation is near-impossible for a newcomer. **Trap.**
- **Title II.** Buyers are public entities, which means a government or enterprise sales cycle. **Exclude.**

### Gaps
- The EAA microenterprise exemption for services (under 10 staff and turnover or balance sheet ≤€2M, from training knowledge) was not verified in this session's results.
- UsableNet and Seyfarth 2026 midyear website figures were not found.
- No demand-letter statistics, separate from lawsuits, were found.

---

## 7. US state privacy laws 2025–2026, Global Privacy Control and cookie/consent: is the SMB consent-tool market saturated?

### Takeaway
New state laws keep arriving (Indiana, Kentucky and Rhode Island took effect 1 Jan 2026), and about 12 states reportedly require honouring Global Privacy Control (GPC). But the SMB consent market is saturated: Shopify leaders have about 2,700 and about 1,750 reviews, alongside Cookiebot-class vendors. EU cookie rules are also in flux: the Council has deleted the digital omnibus browser-signal articles. **Trap.**

### Cited Findings
- **New laws.** Indiana, Kentucky and Rhode Island took effect 1 Jan 2026. Rhode Island does not require processing universal opt-out mechanisms and must disclose third parties to which it sells personal data. Cure periods are sunsetting in several states (CT, DE, KY, MN, MT). — [Hunton](https://www.hunton.com/privacy-and-information-security-law/new-u-s-state-privacy-social-media-and-ai-laws-take-effect-in-january-2026); [BakerHostetler Q1 2026](https://www.bakerlaw.com/insights/state-privacy-in-brief-q1-2026/); [McGuireWoods (28 Jan 2026)](https://blogs.mcguirewoods.com/2026/01/28/data-privacy-day-2026-what-changed-on-jan-1-and-what-to-watch-next/)
- **GPC.** Twelve states now require sites to honour GPC (the list is not verified). — [Enzuzo tracker](https://www.enzuzo.com/blog/us-state-privacy-laws)
- **Shopify consent leaders.** Pandectes GDPR Compliance has about 2,679–2,690 reviews (98% five-star). Consentmo is listed at 5.0 with 1,751 reviews, from $9/mo. — [Shopify: Pandectes reviews](https://apps.shopify.com/gdpr-cookie-consent/reviews); [Growave roundup](https://www.growave.io/best-shopify-apps/gdpr-apps)
- **EU digital omnibus on cookies.**
  - The Commission's Nov 2025 proposal (COM(2025) 837) would add GDPR Arts. 88a and 88b, including mandatory respect for browser signals within 24 months.
  - Council texts of 18 Jun and 3 Sept 2026 deleted both articles and moved the rules back to ePrivacy Art. 5(3); the 2 Oct 2026 text keeps that.
  - Nineteen organisations asked on 10 Sept 2026 to restore the browser-signal article. Parliament's position is not found.
  - Sources: [PPC Land](https://ppc.land/19-groups-ask-eu-to-re-insert-the-cookie-banner-fix-google-lobbied-out/); [PPC Land](https://ppc.land/eu-council-draft-cuts-cookie-re-prompt-wait-from-6-months-to-4/); [Freshfields](https://technologyquotient.freshfields.com/post/102m196/how-the-eu-commissions-digital-omnibus-could-reshape-cookie-compliance-in-europe)

### Inferences
- Thousands of reviews on the leading Shopify apps, plus enterprise CMPs (consent-management platforms), mean a newcomer has no distribution edge.
- Regulatory flux in the EU (the omnibus) and state-by-state US changes favour incumbents with legal teams. SMBs clearly self-serve here, but the space is taken. **Trap.**

### Gaps
- The list of the 12 GPC states is unverified.
- Applicability thresholds of state laws (revenue or consumer counts) were not checked; they mean many small sites are not covered.

---

## 8. PCI DSS 4.0.1 payment-page script requirements (6.4.3, 11.6.1) for small e-commerce, including the SAQ A changes

### Takeaway
The January 2025 SAQ A revision removed 6.4.3, 11.6.1 and 12.3.1 for SAQ A merchants: most small shops on hosted or iframe checkout (Shopify, Stripe, Adyen). It replaced them with an eligibility criterion that the site is "not susceptible to attacks from scripts". The requirements still apply to SAQ D merchants and onsite assessments. Free tiers and acquirer-bundled monitors exist. Small-merchant demand is therefore limited. **Trap.**

### Cited Findings
- **SAQ A change.** SAQ A v4.0.1 (Jan 2025) dropped 6.4.3, 11.6.1 and 12.3.1 and added the script-attack eligibility criterion; 6.4.3 and 11.6.1 remain for SAQ D merchants and onsite assessments. — [Adyen docs](https://docs.adyen.com/development-resources/pci-dss-compliance-guide/saq-a-eligibility); [usd AG](https://www.usd.de/update-pci-saq-a-2025/)
- **Commentators split** on how much changes in practice: one says the criterion effectively requires the principles anyway; another calls it "kind of" a removal. — [AccessIT Group](https://www.accessitgroup.com/tag/saq-a); [Report URI](https://blog.report-uri.com/pci-dss-4-0-1-saq-a-and-client-side-security-a-plain-english-faq/)
- **Prices.**
  - cside: free plan (no card), paid from $99/mo, priced by payment-page views. — [cside pricing](https://cside.com/en/pricing); [cside blog](https://cside.com/blog/comply-with-pci-dss-6-4-3-and-11-6-1-for-free)
  - Market range $99/mo to $50k+/yr (vendor). — [cside comparison](https://cside.com/blog/solution-comparison-pci-dss-6-4-3-and-11-6-1)
  - Mid-market ranges of $5k–20k/yr for dedicated platforms and $3k–10k/yr for WAF add-ons. — [Cipherssecurity (Aug 2026)](https://cipherssecurity.com/pci-dss-4-0-1-compliance-cost-2026-mid-market/)
  - Aperia's payment-script monitor is sold through merchant service providers (bundled). — [Aperia](https://aperiacompliance.ixopay.com/assets/aperia-payment-script-monitor.pdf)
  - SecurityMetrics and Feroot also target small business. — [SecurityMetrics](https://www.securitymetrics.com/blog/solutions-for-small-businesses); [Feroot](https://feroot.com/blog/the-cheapest-way-to-comply-with-pci-dss-requirements)

### Inferences
- Most small e-commerce merchants qualify for SAQ A and no longer need a paid monitor. The rest (SAQ A-EP or D, self-hosted checkouts) are served by free tiers and acquirer bundles.
- It is also a security product where a solo vendor's credibility is hard to establish. **Trap.**

### Gaps
- The exact 31 Mar 2025 effective date of the future-dated requirements was not re-verified (training knowledge).
- The PCI SSC's official SAQ A wording was not opened.

---

## 9. Email bulk-sender rules (Google, Yahoo, Microsoft: DMARC, one-click unsubscribe) and DMARC tool saturation

### Takeaway
Microsoft began enforcing on 5 May 2025 for senders of 5,000+ messages a day to consumer domains (error 550 5.7.515). Gmail reportedly moved from warnings to permanent rejections in Nov 2025 (vendor reports). DMARC tooling is saturated with generous free tiers. **Trap.**

### Cited Findings
- **Microsoft.** Enforcement from 5 May 2025 for 5,000+ messages a day to outlook.com, hotmail.com and live.com. The error is "550; 5.7.515 Access denied…". Sources differ on when junk-foldering turns into full rejection. — [Resend](https://resend.com/blog/microsoft-bulk-sending-requirements-2025); [URIports](https://mta-sts.uriports.com/blog/outlook-error-550-5-7-515-and-how-to-fix-it/)
- **Gmail.** From Nov 2025, non-compliant traffic is said to get permanent 550 rejections, and Postmaster Tools v2 replaces reputation tiers with a pass/fail compliance status (vendor claims; Google's primary page not found). — [PowerDMARC](https://powerdmarc.com/gmail-enforcement-email-rejection/); [Red Sift](https://redsift.com/guides/bulk-email-sender-requirements)
- **Free DMARC tiers.**
  - Cloudflare DMARC Management: free for domains on Cloudflare DNS.
  - Valimail Monitor: free, unlimited volume and domains.
  - dmarcian: free, about 1,250 messages a month.
  - EasyDMARC: free, 1,000 emails a month, 1 domain.
  - Postmark: free weekly DMARC digests.
  - DMARC Report: free for 10,000 reports and 1 domain; paid from $25/mo.
  - Sources: [DMARC Report (vendor)](https://dmarcreport.com/blog/best-free-dmarc-monitoring-tools-2026-guide-without-budget-approval/); [EmailVendorSelection](https://www.emailvendorselection.com/best-dmarc-monitoring-tools/); [Red Sift](https://redsift.com/guides/6-best-free-dmarc-tools); [PowerDMARC](https://powerdmarc.com/free-dmarc-tools/)

### Inferences
- The pain is real but one-time (set up SPF, DKIM, DMARC and one-click unsubscribe once). Email service providers bake compliance in, and good free monitoring exists. **Trap.**

### Gaps
- Google's and Yahoo's primary 2024 requirement pages and the Nov 2025 Gmail enforcement note were not found in the results.

---

## 10. FTC rules (junk fees for tickets and lodging; click-to-cancel) and US sales-tax and 1099 changes for small sellers

### Takeaway
None of these is a solo-developer product opportunity:
- **Fees rule** (effective 12 May 2025): enforced against big platforms ($10M ticket-resale settlement; a reported $35M Hopper settlement).
- **Click-to-cancel:** vacated by the 8th Circuit on 8 Jul 2025. The FTC restarted with an advance notice of proposed rulemaking (ANPRM) in Mar 2026 (comments due 13 Apr 2026); no new rule yet, though state and city rules continue (New York City from Oct 2026).
- **1099s:** reporting burdens fell. The 1099-K threshold is back to $20,000 and 200 transactions; the 1099-NEC/MISC threshold is $2,000 from tax year 2026.
- **Sales tax:** more states dropped the 200-transaction nexus test (Illinois 1 Jan 2026; Kentucky reportedly 1 Aug 2026). The space is served by funded incumbents.

### Cited Findings
- **Fees rule enforcement.** The rule requires up-front total prices for live-event tickets and short-term lodging (effective 12 May 2025). The FTC reached a $10M settlement with the largest ticket-resale platform (reported 10 Apr 2026). A Hopper settlement partly based on the rule is reported at $35M. Warning letters went to 13 property-management software providers and 97 auto dealers. — [Hudson Cook](https://hudsoncook.com/article/enforcement-alert-from-hudson-cook-ftc-announces-10-million-settlement-with-ticket-sale-website-for-failing-to-provide-all-in-price-disclosures/); [Frankfurt Kurnit](https://advertisinglaw.fkks.com/post/102kbar/junk-fees-under-fire-ftc-signals-new-era-of-price-transparency-enforcement); [Simpson Thacher (Feb 2026)](https://www.stblaw.com/about-us/publications/view/2026/02/05/the-ad-standard-monthly-update---february-2026)
- **Click-to-cancel.** Vacated 8 Jul 2025. A draft ANPRM went to the Office of Management and Budget (OMB) in early 2026 and the notice issued in Mar 2026, with comments due 13 Apr. Enforcement under the Restore Online Shoppers' Confidence Act (ROSCA) continues (for example, JustAnswer). — [MediaPost (12 Mar 2026)](https://www.mediapost.com/publications/article/413412/ftc-revisits-click-to-cancel-rules.html); [Sidley (Feb 2026)](https://www.sidley.com/en/insights/newsupdates/2026/02/us-ftc-signals-renewed-interest-in-click-to-cancel-rulemaking); [Jones Day (May 2026)](https://www.jonesday.com/en/insights/2026/05/ftc-revives-clicktocancel-rule-new-risks-for-subscription-businesses); [Arnold & Porter](https://www.arnoldporter.com/en/perspectives/advisories/2026/02/ftc-and-state-ags-continue-to-scrutinize-subscription-practices)
- **New York City.** Its click-to-cancel rule took effect around 1 Oct 2026, joining states with similar laws. — [CNBC (1 Oct 2026)](https://www.cnbc.com/2026/10/01/new-york-city-click-to-cancel-subscription-rule-in-effect.html)
- **1099 thresholds.** The One Big Beautiful Bill Act (OBBBA) restored the 1099-K threshold to $20,000 and 200 transactions, replacing the planned $2,500 (2025) and $600 (2026). The 1099-NEC and most 1099-MISC thresholds rise to $2,000 from tax year 2026 and are inflation-indexed from 2027. — [Patriot Software](https://www.patriotsoftware.com/blog/accounting/1099-reporting-threshold/); [OnPay](https://onpay.com/insights/1099-reporting-threshold-updates/); [AAFCPA](https://aafcpa.com/2025/09/09/businesses-see-relief-as-1099-thresholds-increase-prepare-now-for-year-end-deadlines/)
- **Sales-tax nexus.**
  - Illinois dropped the transaction count from 1 Jan 2026 (HB 2755); a reported voluntary-disclosure window ran 1 Aug–31 Oct 2026 (unofficial). — [Beancount (10 Jul 2026)](https://beancount.io/blog/2026/07/10/illinois-200-transaction-sales-tax-nexus-repeal-guide)
  - Kentucky dropped it from 1 Aug 2026; Utah and Alaska in 2025; Indiana since 1 Jan 2024. About 15 jurisdictions still use a 200-transaction test as of Oct 2026 (counts conflict). — [Taxually](https://www.taxually.com/blog/economic-nexus-by-state); [Zamp](https://zamp.com/blog/economic-nexus-statistics)

### Inferences
- **Junk fees.** Enforcement hits large platforms; small hosts sell through Airbnb or booking engines that handle display.
- **Click-to-cancel.** No federal mandate at present; subscription platforms implement cancellation flows themselves.
- **Taxes.** Rising thresholds reduce small-seller filing pain, and nexus tools are crowded. All **exclude/trap**.

### Gaps
- The Hopper settlement's date and court status were not checked.
- No FTC primary documents were opened.

---

## 11. Other 2026–2027 obligations hitting large numbers of SMBs or online sellers

### Takeaway
Four important 2026 obligations were missing from the original list:

**(a) The EU "withdrawal button" (from 19 June 2026, Art. 11a of the Consumer Rights Directive).** It applies to every B2C online contract that carries a withdrawal right, including services and non-EU traders targeting the EU. The playbook clearly worked: Shopify apps reached about 2,160, 465 and 275 reviews within months. The Shopify niche is now **saturated**. Underserved platforms and online-service sellers are the remaining gap, but that gap is unverified.

**(b) The EmpCo/ECGT green-claims rules (from 27 Sept 2026).** They ban generic environmental claims. In Germany they were implemented through the UWG, which means competitors and associations can send warning letters (Abmahnungen). The tool market is early: 2 Shopify apps with no reviews, so willingness to pay is unproven.

**(c) The EU's €3 duty per item on parcels under €150 (from 1 Jul 2026)**, with a handling fee of about €2 still being negotiated.

**(d) The indefinite US de minimis suspension** across all modes (new postal entry from 24 Jul 2026; statutory end 1 Jul 2027).

(c) and (d) hit Brazilian cross-border sellers, but carriers and marketplaces handle them.

### Cited Findings
- **Withdrawal button: legal basis and design.**
  - Directive (EU) 2023/2673 inserted Art. 11a into the Consumer Rights Directive and applies from 19 Jun 2026. It requires a clearly labelled withdrawal function (for example "withdraw from contract here"), then a "confirm withdrawal" step, plus an acknowledgement on a durable medium. — [Winston Taylor](https://www.winstontaylor.com/insights/eu-withdrawal-buttons-required-for-consumer-online-contracts-from-june-19-2026-are-you-ready); [Loyens & Loeff](https://www.loyensloeff.com/insights/news--events/news/new-eu-rules-on-withdrawing-from-online-contracts/); [nShift](https://nshift.com/blog/eu-withdrawal-function-more-than-a-button); [Greenberg Traurig (May 2026)](https://www.gtlaw.com/en/insights/2026/5/eu-consumer-law-new-withdrawal-button-requirements-for-online-contracts)
  - It applies to non-EU businesses targeting EU consumers. Bespoke, perishable and sealed hygiene goods are excluded. — [Crowell](https://www.crowell.com/en/insights/client-alerts/from-checkout-to-opt-out-the-eu-withdrawal-button-is-here-what-e-commerce-businesses-need-to-know)
- **Withdrawal button: national laws and scope.**
  - Germany: §356a BGB. Netherlands: Art. 6:230oa BW. Guides say it may also reach service providers. — [Jimdo](https://www.jimdo.com/blog/eu-withdrawal-button-from-19-june-2026-what-you-need-to-know/); [Returnless](https://www.returnless.com/knowledge-base/eu-withdrawal-button); [Montonio](https://www.montonio.com/blog/eu-mandatory-withdrawal-button)
  - France: ordonnance n°2026-2. The function must sit in the sales interface itself (site, app or marketplace); a PDF form or an after-sales email no longer suffices. — [E-commerce Nation](https://www.ecommerce-nation.fr/e-commerce-le-bouton-de-retractation-devient-obligatoire-le-19-juin-2026/); [ShippyPro FR](https://www.shippypro.com/blog/fr/bouton-retractation-obligatoire-ue-marchands-19-juin-2026)
  - The German rule covers online contracts for goods and services. — [eRecht24](https://www.e-recht24.de/ecommerce/13472-widerrufsbutton.html)
- **Withdrawal button: enforcement and penalties.**
  - It counts as a market-conduct rule, so competitors and associations can send warning letters. — [Dr. Schwenke FAQ](https://drschwenke.de/widerrufsbutton-grosse-faq/); [Datenschutz-Generator](https://datenschutz-generator.de/widerrufsbutton/)
  - A first documented warning letter targeted an *insufficient* button. — [IT-Recht Kanzlei](https://www.it-recht-kanzlei.de/abmahnung-widerrufsbutton-unzureichend.html)
  - One German guide says a missing function extends the 14-day withdrawal period to 12 months and 14 days. — [e-rechtsanwälte](https://www.e-rechtsanwaelte.de/gesetz-und-recht/widerrufsbutton-pflicht-ab-19-juni-2026-was-sich-aendert/); [next-levels](https://next-levels.de/wiki/widerrufsbutton)
  - Shopify says fines of up to 4% of annual turnover may apply in some Member States. — [Shopify Help Center](https://help.shopify.com/en/manual/compliance/legal/eu-right-of-withdrawal)
- **Withdrawal button: Shopify native support.**
  - Shopify points merchants to its return and cancellation rules (self-serve cancellations up to 14 days after the last delivery). It says using them does not automatically make a store compliant. Managed Markets applies compliant policies automatically. — [Shopify Help Center](https://help.shopify.com/en/manual/compliance/legal/eu-right-of-withdrawal); [Shopify Changelog](https://changelog.shopify.com/posts/self-serve-returns-now-support-cancellations)
  - Forum users note the native flow runs through customer accounts with login, while guests should be able to withdraw without logging in. — [Shopify Community](https://community.shopify.com/t/eu-withdrawal-button-requirement-starts-june-19-2026/637624); [Shopify Dev Community](https://community.shopify.dev/t/new-eu-withdrawal-button-required-by-june-19-2026/35121); [Shopify Community (digital products)](https://community.shopify.com/t/eu-withdrawal-button-for-stores-with-digital-products-for-eu-directive-2023-2673/636370)
- **Withdrawal button: Shopify app traction (snapshots; prices self-reported).**
  - "EU Withdrawal Button": about 2,160 reviews at 4.9, with recent one-star complaints about support. It is unclear which exact listing this is. — [AppNavigator reviews](https://appnavigator.io/app/eu-widerrufsbutton/reviews/?rating=1); [Shopify listing](https://apps.shopify.com/eu-widerrufsbutton)
  - Revoq / "Revoco" (no-login flow; probably the same app): 465 reviews at 4.9. — [Shopify reviews](https://apps.shopify.com/reviews/2176513); [Shopify: Revoco](https://apps.shopify.com/revoco)
  - "EU Withdrawal Button Pro": 275 reviews at 5.0, Premium from $17.99/mo or $174.99/yr. — [Shopify](https://apps.shopify.com/eu-widerruf-pro)
  - Another "EU Withdrawal Button": 27 reviews, from $9.99/mo. — [Shopify](https://apps.shopify.com/eu-withdrawal-button)
  - "EU Widerrufsbutton Pro": 45 reviews, free plan. — [Shopify](https://apps.shopify.com/eu-widerrufsbutton-1)
  - Rückruf: free, $9.99 or $29.99/mo, 4 reviews. — [Shopify](https://apps.shopify.com/widerrufsbutton-2)
  - WiderrufButton: $19.99 per shop or $49.99 for agencies; a third-party listing shows Free, Solo $6.99, Shop $19.99 and Agency $49.99, multi-platform across Shopify, Shopware and WooCommerce. — [Shopify](https://apps.shopify.com/widerrufbutton); [PickYourApp](https://pickyourapp.com/products/widerrufbutton)
  - HexWhite: free or $5/mo. — [Shopify](https://apps.shopify.com/widerruf-app-356a-bgb)
  - D-MIT-S: $2.99/mo. — [Shopify](https://apps.shopify.com/eu-widerrufsformular)
  - Händlerbund: free, members only, 5 reviews. — [Shopify](https://apps.shopify.com/handlerbund-widerruf-manager)
  - e-Widerruf: free. — [Shopify](https://apps.shopify.com/e-widerruf)
- **Withdrawal button: other platforms.**
  - A free WordPress/WooCommerce plugin "Widerrufsbutton" offers a two-step flow, shortcodes and a confirmation email, with Pro add-ons; the vendor says it is no substitute for legal advice. — [WordPress.org](https://wordpress.org/plugins/widerrufsbutton/)
  - A Shopware store plugin exists. — [Shopware Store](https://store.shopware.com/en/fript64540696853m/withdrawal-button-legally-compliant-withdrawal-with-flexible-flows.html)
  - eRecht24 gives members an HTML-embed button plus a "Widerrufsbutton Manager". — [eRecht24 members](https://www.e-recht24.de/mitglieder/widerrufsbutton-lp/)
  - Händlerbund includes it in its membership. — [Händlerbund](https://www.haendlerbund.de/de/leistungen/rechtssicherheit/agb-service/widerrufsbelehrung/widerrufsbutton)
  - Platform-level implementations exist, for example Tentary. — [Tentary support](https://support.tentary.com/hc/de/articles/47661179662225)
- **Withdrawal button: website builders (sources conflict).** eRecht24's table lists Jimdo as yes, Wix as no and Squarespace as yes with documentation. Ecom-tools says Jimdo enabled a free button automatically in the footer, Wix had no native or app-store solution (custom code only), and Squarespace documents a manual form block. A Wix App Market listing surfaced in search, but its content was not seen. — [eRecht24 overview](https://www.e-recht24.de/ecommerce/13472-widerrufsbutton.html); [ecom-tools](https://ecom-tools.de/widerrufsbutton-pflicht/); [Wix App Market listing](https://cs.wix.com/app-market/fde5e854-ecfc-4fe5-b754-52c6eaf88edf)
- **ECGT/EmpCo: what changed.**
  - Directive (EU) 2024/825: transposition by 27 Mar 2026; the rules apply from 27 Sept 2026. — [Irish Dept. of Enterprise](https://enterprise.gov.ie/en/what-we-do/the-business-environment/empowering-consumers-for-the-green-transition/); [empcodirective.eu](https://empcodirective.eu/)
  - Banned: generic claims ("eco-friendly", "green", "sustainable") without recognised excellent environmental performance; offset-based "climate neutral" product claims; sustainability labels not based on certification schemes; whole-product claims that concern one aspect. Durability and repairability information is also required. — [Coslaw](https://coslaw.eu/directive-eu-2024-825-generic-environmental-claims-and-practices-banned-in-the-eu-from-27-september-2026/); [Regonance](https://regonance.com/knowledge/empco/green-claims-september-2026); [Tappr](https://www.usetappr.com/regulation/empowering-consumers-directive/)
  - No transition period: existing pages must comply. — [Certivo](https://www.certivo.com/blog-details/eu-empowering-consumers-directive-green-claims-rules-from-september-2026)
- **ECGT/EmpCo in Germany.** Implemented through the UWG, passed Dec 2025 and published in the Federal Law Gazette (BGBl.) on 19 Feb 2026, applying from 27 Sept 2026 with no transition for goods already on the market. Warning letters and fines are expected for unsubstantiated claims, and the crafts federation flags higher warning-letter risk for green claims and seals. — [TÜV Consulting](https://consulting.tuv.com/aktuelles/nachhaltigkeit/empco-richtlinie-green-claims); [Ecovis](https://ecovis-kso.com/blog/die-empco-richtlinie-tritt-in-kraft/); [ZDH](https://www.zdh.de/ueber-uns/fachbereich-organisation-und-recht/wirtschaftsrecht/empco-richtlinie/)
- **ECGT/EmpCo tools.**
  - "EU Green Claims & EmpCo Check" (Appsentials): 9 languages, risk ratings, rewording suggestions, audit PDF; free plan and trial; no reviews. — [Shopify](https://apps.shopify.com/eu-green-claims-greenwashing); [AppNavigator](https://appnavigator.io/app/eu-green-claims-greenwashing/)
  - "GreenScan": free (3 scans a month), $9.99 or $29.99/mo (OpenAI-based rewrites). — [Shopify](https://apps.shopify.com/green-scanner?locale=it); [PickYourApp](https://pickyourapp.com/products/green-scanner)
- **EU €3 parcel duty.** From 1 Jul 2026, €3 per goods item on non-EU online purchases up to €150 (Finnish Customs, May 2026). It covers IOSS-registered sellers, about 93% of e-commerce imports, as a stopgap until the 2028 reform. A handling fee of about €2 per parcel is planned for around Nov 2026 but is still under negotiation; some states (RO, IT, FR) already charge national fees. No post-July confirmation was found. — [Finnish Customs](https://tulli.fi/en/-/a-3-customs-duty-to-be-introduced-to-curb-low-value-import-consignments); [Royal Mail](https://www.royalmail.com/europeantradeinsights); [RSM](https://www.rsm.global/belgium/en/insights/eu-introduces-new-charges-low-value-imports); [Value Added Resource](https://www.valueaddedresource.net/eu-flat-customs-duty-fee-low-value-imports)
- **US de minimis.**
  - Customs and Border Protection (CBP) published interim final rules on 24 Jun 2026 suspending de minimis indefinitely across all modes, with a new postal informal-entry process from 24 Jul 2026. — [Federal Register (24 Jun 2026)](https://www.federalregister.gov/documents/2026/06/24/2026-12669/indefinite-suspension-of-the-de-minimis-exemption-for-mail-shipments-and-new-postal-informal-entry)
  - The Supreme Court's IEEPA tariff ruling did not restore de minimis (EO 14388 continued the suspension). OBBBA ends it by statute on 1 Jul 2027. Postal duty rates are now tied to the 20 Feb 2026 temporary import surcharge proclamation. — [Greenberg Traurig (June 2026)](https://www.gtlaw.com/ar/insights/2026/6/us-trade-developments-ieepa-refund-processing-de-minimis-suspension-and-section-301-investigation-against-germany); [Supply Chain Dive](https://www.supplychaindive.com/news/de-minimis-status-supreme-court-trump/812785/); [Thomson Reuters (25 Feb 2026)](https://www.thomsonreuters.com/en-us/help/onesource-global-trade/regulatory-insights/2026/february-25th/de-min-suspension-means-global-trade-prof.html)

### Inferences
- **The withdrawal button is the clearest proof in this dataset** that "EU deadline → simple app → mass self-serve adoption" works. Hundreds to about 2,000 reviews within about 4–6 months of the deadline is far above GPSR apps (≤29). The likely reason: it is a binary must-have for nearly every EU B2C shop, warning letters are enforceable, and the extended withdrawal period is a costly penalty.
- **By Oct 2026 Shopify is a red ocean.** The remaining gaps are probably:
  1. builders without native or app solutions (Wix per two sources; Webflow not found; Squarespace manual);
  2. online-service sellers (courses, coaching, memberships, B2C SaaS, Stripe Payment Links) who have no "shop" platform;
  3. non-German EU languages (FR, NL, IT, ES, PL), since most apps are German-first;
  4. non-EU traders targeting EU consumers.
  All four need validation.
- **ECGT is earlier in the cycle.** Only 2 apps, no reviews, and green claims affect only a subset of shops. Demand may materialise as German warning-letter waves hit, but willingness to pay is unproven today.
- **€3 duty and de minimis.** Real costs for Brazilian Etsy and DTC exporters, but collection runs through carriers, IOSS intermediaries and marketplaces. There is no simple-software wedge for a solo developer (competitor landscape not checked).

### Gaps
- The Wix App Market gap is unverified (the search budget ran out).
- Stripe App Marketplace offerings were not checked.
- The number of EU B2C websites outside Shopify was not found.
- No search-volume data for "Widerrufsbutton", "bouton de rétractation" or "herroepingsknop".
- No evidence yet of EmpCo warning letters after 27 Sept 2026.
- Other 2026–2027 items not researched: the AI Act Art. 50 transparency duties and digital-omnibus delays, the Battery Regulation labelling dates, EU textile EPR, the right-to-repair directive, the Data Act design obligations, COPPA amendments.

---

## 12. Legal-liability risk of selling compliance tools, and where a disclaimer is enough

### Takeaway
In Germany, standardised question-and-answer generators are not "legal services" (BGH, *Smartlaw*, 9 Sept 2021, I ZR 113/20), so a solo developer can sell rule-based tools. Two things still matter: advertising claims (OLG Köln banned "cheaper and faster than a lawyer") and, above all, tools whose output *is* the compliance mechanism. A defective withdrawal button can itself draw a warning letter. Disclaimers suffice for validators, calculators and checklists. They do not suffice for "functional" compliance components, which need a careful spec, logs and cautious marketing.

### Cited Findings
- **Smartlaw ruling.** The BGH held that a digital contract-document generator, which assembles standardised clauses from user answers, is not a legal service under §2(1) RDG. — [LTO](https://www.lto.de/recht/juristen/b/bgh-urteil-izr11320-vertragsgenerator-smartlaw-keine-unzulaessige-rechtsdienstleistung-rak-hamburg-rdg-legal-tech); [WBS Legal](https://www.wbs.legal/it-und-internet-recht/bgh-zu-legal-techdigitaler-vertragsdokumete-generator-smartlaw-ist-zulaessig-56819/); [DATEV Magazin](https://www.datev-magazin.de/nachrichten-steuern-recht/recht/zulaessigkeit-eines-digitalen-vertragsdokumentengenerators-62145)
- **Advertising limit.** The OLG Köln ban on Smartlaw advertising it was "cheaper and faster than a lawyer" is final. — [LTO](https://www.lto.de/recht/juristen/b/bgh-urteil-izr11320-vertragsgenerator-smartlaw-keine-unzulaessige-rechtsdienstleistung-rak-hamburg-rdg-legal-tech)
- **Defective functions draw warning letters.** A warning letter targeted a withdrawal button that existed but did not meet §356a BGB. — [IT-Recht Kanzlei](https://www.it-recht-kanzlei.de/abmahnung-widerrufsbutton-unzureichend.html)
- **Vendors disclaim.** Shopify says using its tools does not automatically make a store compliant. The WordPress plugin vendor says the plugin does not replace legal advice. — [Shopify Help Center](https://help.shopify.com/en/manual/compliance/legal/eu-right-of-withdrawal); [WordPress.org](https://wordpress.org/plugins/widerrufsbutton/)
- **Overpromising is punished.** The FTC's $1M accessiBe order was about overstated "compliance" claims and undisclosed paid reviews. — [TestParty](https://testparty.ai/blog/are-accessibility-overlays-legal)

### Inferences
- **Disclaimer is enough:** GeoJSON or e-invoice validators, packaging-weight calculators, checklists, document generators with standard text, and "risk scanners" that flag rather than certify.
- **Disclaimer is not enough on its own:**
  - Withdrawal functions and consent banners, where defects create violations. These need conformance to the legal spec (two-step flow, labelling, durable-medium confirmation, availability through the whole withdrawal period), audit logs, uptime, a liability cap in the terms (German standard-terms law limits exclusions for gross negligence; training knowledge, unverified) and wording such as "helps implement §356a BGB", never "guaranteed compliant".
  - Overlays: avoid completely.
- **Never act as a legal party.** Acting as the EU RP (GPSR) or an EPR AR requires an EU establishment and means taking on legal liability. Not a software play for a Brazilian solo developer.
- **Keep logic standardised** and avoid individual legal assessments (RDG risk in Germany).

### Gaps
- Cost of professional-liability or E&O insurance for a Brazilian solo developer selling into the EU, not researched.
- EU VAT and OSS handling for selling SaaS to EU merchants from Brazil, not researched (app marketplaces may handle billing).
- Payout support for Brazilian developers on Wix, Shopify or Stripe, not researched.

---

## 13. Candidate products: definitions, evidence, competitors, channels, build effort, risks and scores

### Takeaway
After filtering for proven willingness to pay, low saturation, buyer purchasing power, contact-free distribution and a days-to-weeks build, three candidates survive:

| Rank | Candidate | Score | Note |
|---|---|---|---|
| 1 | C1: universal EU withdrawal function outside Shopify | 26/35 | Proven demand; the platform gap still needs checking |
| 2 | C3: EUDR micro-operator GeoJSON/DDS kit with a Portuguese supplier portal | 21/35 | Proven pricing gap, but slower |
| Runner-up | C2: EmpCo green-claims scanner | 23/35 | Early market; willingness to pay unproven, which breaks the brief's requirement (g) |

All others are saturated, enterprise sales, or legally unworkable.

### Cited Findings
- **Demand and willingness to pay (withdrawal button).** Leading Shopify apps have about 2,160, 465 and 275 reviews, with paid tiers of $2.99–$49.99/mo, against far weaker GPSR apps (≤29 reviews) and early EmpCo apps (0 reviews). — [AppNavigator](https://appnavigator.io/app/eu-widerrufsbutton/reviews/?rating=1); [Revoq reviews](https://apps.shopify.com/reviews/2176513); [EU Withdrawal Button Pro](https://apps.shopify.com/eu-widerruf-pro); [PickYourApp: WiderrufButton](https://pickyourapp.com/products/widerrufbutton); [GCM reviews](https://apps.shopify.com/gpsr/reviews); [EmpCo Check](https://apps.shopify.com/eu-green-claims-greenwashing)
- **EUDR price anchors.** TradeAware Professional €399/mo with 50 DDS a year; Polygon One from about €3,000/yr; enterprise €10,000–50,000/yr; free geojson.io and GeoRoots Editor; free Brazilian platforms. — [TradeAware](https://www.live-eo.com/tradeaware-pricing); [Polygon One](https://polygon-one.com/en/article-eudr-software-comparison); [Qelvyn](https://qelvyn.co/en/blog/eudr/farm-plot-mapping-cost-cooperatives-eudr); [EFI GeoRoots](https://efi.int/news/georoots-editor-accessible-secure-and-eudr-ready-geodata-editing-directly-your-browser-2026-02); [Campo Vivo](https://campovivo.com.br/apresentado-por-prime-cafe/2026/09/08/rastreabilidade-passa-a-definir-o-acesso-do-cafe-brasileiro-ao-mercado-europeu/)
- **Market size proxy.** About 446,000 live Shopify stores in the five largest EU markets; 121,343 in Germany. — [EightX](https://eightx.co/blog/eu-shopify-landscape)
- **Revenue evidence.** No verified competitor revenue was found for any candidate. All counts are public listing metrics (snapshots) and all prices are self-reported.

### Inferences

#### Scoring table
Scores run 1–5; 5 is best. "Low saturation" and "Low risk" are scored so that 5 means least saturated and least risky.

| # | Candidate | Willingness to pay | Low saturation | Buyer power | No-contact distribution | Buildability | Speed to revenue | Low risk | Total /35 | Exclusion flags |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Universal EU withdrawal function (non-Shopify platforms and services, multi-language) | 4 | 2 | 4 | 4 | 5 | 4 | 3 | **26** | none (validate platform gap) |
| C1-S | Another Shopify withdrawal-button app | 4 | 1 | 4 | 3 | 5 | 2 | 3 | 22 | **TRAP: saturated** |
| C2 | EmpCo/ECGT green-claims scanner (Shopify app plus URL scanner) | 2 | 4 | 4 | 4 | 4 | 3 | 2 | 23 | AI-wrapper risk if built on LLM rewrites; keep rule-based |
| C3 | EUDR micro-operator kit (GeoJSON build/validate/fix, PT/ES supplier portal, DDS-ready pack) | 3 | 3 | 4 | 3 | 4 | 2 | 2 | **21** | none (regulatory-change risk) |
| C4 | EUDR polygon and report tool for Brazilian smallholders and cooperatives | 1 | 2 | 2 | 2 | 4 | 2 | 2 | 15 | low purchasing power; free government and industry incumbents |
| C5 | GPSR info and label generator or RP tracker | 2 | 1 | 3 | 3 | 5 | 2 | 3 | 19 | **TRAP** |
| C6 | Multi-country EPR obligation tracker and packaging-kg calculator | 2 | 2 | 3 | 3 | 4 | 2 | 3 | 19 | services dominate; affiliate at best |
| C7 | E-invoice generator, validator or converter (XRechnung/ZUGFeRD/Peppol/KSeF) | 4 | 1 | 4 | 2 | 3 | 2 | 2 | 18 | **TRAP**; certification needed for French PA and Peppol access-point roles |
| C8 | SMB accessibility audit or monitor | 4 | 1 | 4 | 2 | 3 | 2 | 1 | 17 | **TRAP** (overlay variant: legal problem) |
| C9 | Cookie consent / GPC tool | 5 | 1 | 4 | 2 | 3 | 1 | 2 | 18 | **TRAP** |
| C10 | PCI payment-page script monitor | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 17 | **TRAP** |
| C11 | DMARC monitor | 3 | 1 | 3 | 2 | 4 | 2 | 3 | 18 | **TRAP** |
| C12 | CBAM threshold tracker or report tool | 3 | 2 | 4 | 2 | 3 | 1 | 2 | 17 | **Enterprise sale** |
| C13 | FTC all-in-pricing (junk fee) checker | 1 | 3 | 3 | 2 | 4 | 2 | 3 | 18 | low SMB willingness to pay |
| C14 | Click-to-cancel compliance kit | 1 | 3 | 3 | 2 | 4 | 1 | 2 | 16 | no federal rule in force |
| C15 | Sales-tax nexus or 1099 tool | 4 | 1 | 4 | 2 | 2 | 1 | 2 | 16 | **TRAP** (funded incumbents; thresholds rising) |
| C16 | Landed-cost calculator for €3 duty and US de minimis (Brazilian sellers) | 2 | 2 | 2 | 2 | 4 | 2 | 3 | 17 | handled by carriers and marketplaces (unverified) |
| C17 | ADA Title II accessibility for local governments | 4 | 2 | 5 | 1 | 3 | 1 | 2 | 18 | **Enterprise/government sale; needs contacts** |

#### C1: Universal EU withdrawal function (top pick)
- **Product.** A hosted, two-step withdrawal function for sites and online services *not* on Shopify. It includes an embeddable button, a no-login form, optional order verification through the platform or Stripe API, an automatic confirmation on a durable medium, a merchant inbox and an exportable audit log, in DE, FR, NL, IT, ES, PL and EN.
- **Buyer and size.**
  - EU B2C sellers on Wix, Squarespace, Webflow or custom sites; online-service sellers (courses, coaching, memberships, B2C SaaS on Stripe Checkout or Payment Links); non-German EU markets; non-EU traders targeting the EU.
  - The count outside Shopify is unknown. For scale, Shopify alone has about 446,000 live stores in the five largest EU markets ([EightX](https://eightx.co/blog/eu-shopify-landscape)).
- **Pain and evidence.**
  - Mandatory since 19 Jun 2026 ([Winston Taylor](https://www.winstontaylor.com/insights/eu-withdrawal-buttons-required-for-consumer-online-contracts-from-june-19-2026-are-you-ready)).
  - German warning letters already target *insufficient* implementations ([IT-Recht Kanzlei](https://www.it-recht-kanzlei.de/abmahnung-widerrufsbutton-unzureichend.html)).
  - A missing function reportedly extends the withdrawal period to 12 months and 14 days ([e-rechtsanwälte](https://www.e-rechtsanwaelte.de/gesetz-und-recht/widerrufsbutton-pflicht-ab-19-juni-2026-was-sich-aendert/)).
  - Fines of up to 4% of turnover are possible in some Member States ([Shopify Help](https://help.shopify.com/en/manual/compliance/legal/eu-right-of-withdrawal)).
- **Competitors (pricing self-reported; counts are snapshots).**
  - Shopify apps with large review bases (about 2,160, 465 and 275).
  - WiderrufButton, multi-platform (Shopify, Shopware, WooCommerce), Free / $6.99 / $19.99 / $49.99 ([PickYourApp](https://pickyourapp.com/products/widerrufbutton)).
  - Free WordPress plugin ([WordPress.org](https://wordpress.org/plugins/widerrufsbutton/)) and Shopware plugin ([Shopware](https://store.shopware.com/en/fript64540696853m/withdrawal-button-legally-compliant-withdrawal-with-flexible-flows.html)).
  - eRecht24 HTML embed for members ([eRecht24](https://www.e-recht24.de/mitglieder/widerrufsbutton-lp/)); Händlerbund for members ([Händlerbund](https://www.haendlerbund.de/de/leistungen/rechtssicherheit/agb-service/widerrufsbelehrung/widerrufsbutton)).
  - Jimdo native and free ([ecom-tools](https://ecom-tools.de/widerrufsbutton-pflicht/)).
  - No competitor revenue data found.
- **Competitors' weaknesses.** Most are German-first and tied to one platform. eRecht24 and Händlerbund lock the feature into a legal-text membership. Shopify's native flow needs a customer login. The leading app's recent one-star reviews mention unresponsive support ([AppNavigator](https://appnavigator.io/app/eu-widerrufsbutton/reviews/?rating=1)).
- **Demand signals.** Large Shopify review counts within months; several Shopify Community threads ([1](https://community.shopify.com/t/eu-withdrawal-button-requirement-starts-june-19-2026/637624), [2](https://community.shopify.dev/t/new-eu-withdrawal-button-required-by-june-19-2026/35121), [3](https://community.shopify.com/t/eu-withdrawal-button-for-stores-with-digital-products-for-eu-directive-2023-2673/636370)); dense content in German and French. No search-volume data.
- **Acquisition without contacts.** Wix App Market (if the gap holds), a freemium plugin on WordPress.org, the Stripe App Marketplace (not verified), local-language SEO ("Widerrufsbutton Wix/Squarespace/Webflow", "bouton de rétractation Wix", "herroepingsknop"), and warning-letter explainer content. A small Google Ads test on high-intent long-tail terms fits a ~US$130 budget, though costs were not checked.
- **Build effort.** Low: a one-to-two-week MVP (embed script, hosted form, email, dashboard, logs, multilingual texts). Each platform integration adds a few days.
- **Time to first revenue.** About 2–6 weeks, depending on marketplace review lag (not verified).
- **Path to about $5k/month (inference).** Roughly 500–600 paying sites at about $9/mo, or about 250 at about $19/mo (agency or multi-site tier). Ambitious but consistent with the install volumes the Shopify leaders show.
- **Main risks.**
  - Late entry: the deadline passed four months ago, so the most motivated buyers already solved it.
  - Platform-native features (Jimdo did it; Wix or Squarespace may follow).
  - The gap may already be filled (the Wix listing was unverified).
  - Low price ceiling.
  - Liability for defective implementations.
  - Exemptions (bespoke goods) shrink the addressable market.

#### C3: EUDR micro-operator kit (second pick)
- **Product.** A self-serve web app for EU micro and small operators:
  1. a supplier link (PT, ES, EN, FR) to capture plots on a map or upload KML, SHP, CSV or CAR files;
  2. GeoJSON validation and auto-fix to TRACES constraints (CRS84, closed rings, no self-intersection, 2D, ≤10 MB, the 4-ha point rule);
  3. a due-diligence file generator (risk-assessment template, legality-document checklist) with a 5-year archive;
  4. GeoJSON export plus DDS field mapping for manual TRACES entry, with an API later if one exists.
- **Free lead magnet.** A public GeoJSON validator and fixer.
- **Buyer and size.** EU micro and small operators first placing coffee, cocoa, wood products, leather, rubber, soy or palm products: specialty-coffee importers and roasters buying direct, craft chocolate makers, small importers of furniture or wooden goods. The count is unknown.
- **Pain and evidence.** DDS with plot geolocation from 30 Dec 2026 (medium and large) or 30 Jun 2027 (micro and small); Brazil is standard risk, so full due diligence applies ([EC](https://trade.ec.europa.eu/access-to-markets/en/news/delay-until-december-2026-and-other-developments-implementation-eudr-regulation); [Fieldfisher](https://www.fieldfisher.com/en/insights/the-eu-deforestation-regulation-european-commission-classifies-countries-as-high-low-or-standard-risk)).
- **Competitors.** TradeAware €399/mo (SME tier, self-reported); Polygon One from about €3,000/yr; enterprise €10,000–50,000/yr; Tracebud (buyer-paid); osapiens Easy Start (no price); free geojson.io and GeoRoots Editor ([TradeAware](https://www.live-eo.com/tradeaware-pricing); [Polygon One](https://polygon-one.com/en/article-eudr-software-comparison); [Qarma](https://www.qarmainspect.com/blog/how-to-submit-geolocation-data-geojson-for-eudr-compliance); [EFI](https://efi.int/news/georoots-editor-accessible-secure-and-eudr-ready-geodata-editing-directly-your-browser-2026-02)). No revenue data.
- **Competitors' weaknesses.** Prices aimed at mid-market buyers, sales through demos, many with no public price. Free tools validate shapes but do not manage the supplier workflow or the dossier.
- **Demand signals (indirect).** Heavy, recently updated vendor SEO on GeoJSON errors and SME guides ([TraceX](https://tracextech.com/geojson-file-errors/); [Coolset](https://www.coolset.com/academy/eudr-reporting-guide-for-smes)).
- **Acquisition.** SEO on technical pain ("EUDR GeoJSON error", "TRACES upload"), the free validator, specialty-coffee and craft-chocolate communities, and LinkedIn content. The developer's Portuguese fluency and Brazil knowledge are a differentiator for Brazil-origin supply chains.
- **Build effort.** Medium: two to four weeks with GIS libraries, a map UI, file conversions, PDF output and multi-tenant supplier links.
- **Time to first revenue.** About 4–12 weeks; seasonal peaks before 30 Dec 2026 and 30 Jun 2027.
- **Path to about $5k/month (inference).** About 50–100 customers at €49–99/mo, or per-shipment pricing.
- **Main risks.**
  - Regulatory change: two past delays, although the Commission's May 2026 review proposed no further changes.
  - Downstream and trader exemptions shrink the number of filers.
  - Free tools and vendors' free tiers.
  - Unknown buyer count.
  - Liability: due diligence stays with the operator, so the tool must be positioned as data preparation.

#### C2: EmpCo green-claims scanner (runner-up and experiment)
- **Product.** A rule-based, multi-language scanner for product pages and packaging copy. It flags generic environmental claims, offset-based "climate neutral" claims, self-made seals and whole-product claims, plus PPWR Art. 12(8) misleading packaging claims. It produces a PDF audit and monitors new products.
- **Buyer.** EU fashion, cosmetics, home and cleaning brands, a subset of about 446,000 big-five-EU Shopify stores ([EightX](https://eightx.co/blog/eu-shopify-landscape)).
- **Pain.** Rules apply since 27 Sept 2026 with no transition, and German warning-letter risk is high ([TÜV](https://consulting.tuv.com/aktuelles/nachhaltigkeit/empco-richtlinie-green-claims); [ZDH](https://www.zdh.de/ueber-uns/fachbereich-organisation-und-recht/wirtschaftsrecht/empco-richtlinie/)).
- **Competitors.** Two Shopify apps, $0–29.99, no reviews ([EmpCo Check](https://apps.shopify.com/eu-green-claims-greenwashing); [GreenScan](https://apps.shopify.com/green-scanner?locale=it)).
- **Weaknesses.** New, unproven, AI-rewrite-centric.
- **Demand.** Unproven.
- **Channel.** Shopify App Store and SEO ("EmpCo Check", "Greenwashing prüfen").
- **Build effort.** One to two weeks, plus legal research per language.
- **Time to first revenue.** 3–8 weeks.
- **Main risks.** No proven willingness to pay; false negatives; easy to copy; drift into an AI wrapper.

#### Short notes on the rejected candidates
Evidence is in sections 1–11.
- **C4:** free Cecafé–Serasa, Conab and MAPA platforms; the producer is not the legal filer.
- **C5:** about 15 apps with near-zero reviews; marketplaces have native fields.
- **C6:** registrations and AR mandates are services; free calculators exist.
- **C7:** free generators, accounting suites, and 101–149 approved French platforms.
- **C8:** dozens of vendors; overlays are an FTC/lawsuit trap.
- **C9:** Pandectes about 2,690 and Consentmo about 1,751 reviews.
- **C10:** SAQ A relief plus free tiers.
- **C11:** free DMARC tiers.
- **C12:** 90% of importers exempt; enterprise.
- **C13 and C14:** enforcement aimed at large platforms; no federal click-to-cancel rule.
- **C15:** funded incumbents and rising thresholds.
- **C16:** carrier and marketplace territory.
- **C17:** government procurement.

### Gaps
- **Search volume, Google Trends and autocomplete** data could not be collected for any candidate (tooling failure). Before building, check Google Keyword Planner and Trends for "Widerrufsbutton", "bouton de rétractation", "herroepingsknop", "EUDR GeoJSON" and "EmpCo".
- **Wix App Market, Stripe App Marketplace and PrestaShop Addons** were not checked for withdrawal apps; this is the key validation for C1.
- **The number of EU operators** in TRACES (for C3) is unknown.
- **No verified competitor revenue or customer counts** were found; only review counts and self-reported prices.

---

## 14. Top 2 candidates and traps (popular-sounding but saturated or unworkable)

### Takeaway
**Top 1: C1, the universal EU withdrawal function outside Shopify.** It has the strongest evidence of mass self-serve adoption under a live legal obligation, it can be built in days, and it can be sold through app marketplaces and local-language SEO without contacts. Its decisive weakness is lateness and possible gap closure, so validate the Wix, Webflow, Squarespace and Stripe gap within 48 hours before building.

**Top 2: C3, the EUDR micro-operator kit.** It has a clear price gap (free manual work versus about €3,000–4,000/yr platforms), a deadline runway (Dec 2026 / Jun 2027) and a genuine Brazil edge, but revenue comes slower and regulatory risk is higher.

The EmpCo scanner (C2) is the fallback experiment if C1's gap check fails.

Traps (evidence below): another Shopify withdrawal or GPSR app, EU RP or EPR AR "services", cookie consent, overlays, accessibility scanners, DMARC, PCI script monitors, e-invoicing converters, CBAM, EUDR tools for Brazilian smallholders, sales-tax and 1099 tools.

### Cited Findings
- **Shopify withdrawal-button apps are saturated:** about 2,160, 465 and 275 reviews, plus at least 9 more apps and Shopify's partial native flow. — [AppNavigator](https://appnavigator.io/app/eu-widerrufsbutton/reviews/?rating=1); [Revoq](https://apps.shopify.com/reviews/2176513); [EU Withdrawal Button Pro](https://apps.shopify.com/eu-widerruf-pro); [Shopify Changelog](https://changelog.shopify.com/posts/self-serve-returns-now-support-cancellations)
- **GPSR apps:** about 15 listings, only one with about 29 reviews; marketplaces have native fields; RP services cost €150–500/yr and require an EU entity. — [GCM reviews](https://apps.shopify.com/gpsr/reviews); [Etsy Help](https://help.etsy.com/hc/en-in/articles/28211364687383-What-is-the-General-Product-Safety-Regulation-GPSR); [EUverify](https://euverify.com/resource/eu-responsible-person-under-gpsr/)
- **Cookie consent:** Pandectes about 2,690 reviews and Consentmo 1,751, with EU rules in flux. — [Pandectes](https://apps.shopify.com/gdpr-cookie-consent/reviews); [Growave](https://www.growave.io/best-shopify-apps/gdpr-apps); [PPC Land](https://ppc.land/19-groups-ask-eu-to-re-insert-the-cookie-banner-fix-google-lobbied-out/)
- **Accessibility overlays:** the FTC's $1M accessiBe order and more than 1,400 suits naming widget users in 2025. — [TestParty](https://testparty.ai/blog/are-accessibility-overlays-legal); [TestParty data](https://testparty.ai/blog/accessibility-overlay-lawsuits-data)
- **Accessibility audits:** dozens of SMB tools while suits keep rising (3,117 federal in 2025). — [UsableNet](https://blog.usablenet.com/ada-web-lawsuit-trends-2026); [WebYes](https://www.webyes.com/blogs/eaa-fines/)
- **DMARC:** free unlimited or near-unlimited tiers (Cloudflare, Valimail, dmarcian, EasyDMARC, Postmark). — [EmailVendorSelection](https://www.emailvendorselection.com/best-dmarc-monitoring-tools/)
- **PCI script monitoring:** SAQ A removal (Jan 2025), a free cside tier, Aperia bundled through merchant service providers. — [Adyen](https://docs.adyen.com/development-resources/pci-dss-compliance-guide/saq-a-eligibility); [cside](https://cside.com/en/pricing); [Aperia](https://aperiacompliance.ixopay.com/assets/aperia-payment-script-monitor.pdf)
- **E-invoicing:** free generators, accounting suites, 149 approved French platforms, Belgian Peppol registration offered free. — [kostenlose-erechnung.de](https://kostenlose-erechnung.de/ratgeber/e-rechnungspflicht-bin-ich-betroffen/); [Presse-citron](https://www.presse-citron.net/facturation-electronique-entre-vigueur-aujourdhui-voici-149-plateformes-agreees-france/); [e-invoice.app](https://e-invoice.app/guides/belgium-e-invoicing)
- **CBAM:** about 90% of importers exempt, a free tool, others €1,990+/yr. — [MHA](https://mha.co.uk/insights/eu-announces-major-cbam-simplifications-reduced-compliance-burden-for-smes); [Sustainability Cloud](https://www.thesustainabilitycloud.com/eu-cbam-for-importers-pricing/); [CBAM Guide: Dubrink](https://cbamguide.com/software/dubrink/)
- **EUDR for Brazilian smallholders:** the Cecafé–Serasa platform (more than 50 exporters, almost all EU coffee), Conab's free platform, MAPA's free platform. — [Campo Vivo](https://campovivo.com.br/apresentado-por-prime-cafe/2026/09/08/rastreabilidade-passa-a-definir-o-acesso-do-cafe-brasileiro-ao-mercado-europeu/); [IT Show](https://itshow.com.br/plataforma-rastreabilidade-cafe-ia-satelites-eudr/); [AgFeed](https://agfeed.com.br/esg/governo-lanca-plataforma-digital-do-agro-sustentavel-com-pendencias-pelo-caminho)
- **1099 and sales tax:** thresholds raised ($20,000/200 for 1099-K; $2,000 for 1099-NEC); nexus tools crowded. — [Patriot Software](https://www.patriotsoftware.com/blog/accounting/1099-reporting-threshold/); [Zamp](https://zamp.com/blog/economic-nexus-statistics)

### Inferences
- **Why C1 first.**
  - It is the only candidate where willingness to pay *and* self-serve behaviour are proven at scale under a legal obligation that is enforced through private warning letters, not slow regulators.
  - The buyer (EU merchants and online-service businesses) has purchasing power, and the build fits the developer's skills and budget.
  - **Validation before building:**
    1. search the Wix App Market, Webflow Marketplace, Squarespace extensions, Stripe App Marketplace and PrestaShop Addons for withdrawal apps;
    2. run Keyword Planner and Trends on local-language terms;
    3. spend about US$50 on Google Ads to a landing page with a waitlist and pre-sale.
  - If one of those platforms is open, ship there first. Otherwise, target online-service sellers through a universal embed plus Stripe or Paddle order lookup.
- **Why C3 second.**
  - Willingness to pay is shown by published SME pricing (€399/mo), and the €0-versus-€3,000/yr gap is wide. The developer's Portuguese and Brazil knowledge are a moat on the supplier side.
  - But the market is B2B and seasonal, the buyer count is unknown, and EUDR has been delayed twice.
  - Start with a free GeoJSON validator and fixer as an SEO asset, then sell the supplier-collection and dossier workflow.
- **Why not C2 first.** It fails the brief's "proven willingness to pay" requirement today (0 reviews on both apps), even though it is quick to build and the market is unsaturated. It could become an add-on module to C1, an "EU consumer-law compliance widget", once demand shows up.
- **Traps:**
  1. Another Shopify withdrawal or GPSR app (red ocean or weak demand).
  2. EU RP or EPR AR "as a service" (needs an EU legal entity and assumes liability).
  3. Cookie or GPC consent (incumbents with thousands of reviews; regulation in flux).
  4. Accessibility overlays (FTC action, lawsuits) and scanners (saturated, liability).
  5. DMARC monitors (free tiers).
  6. PCI script monitors for small merchants (SAQ A relief, free tiers, acquirer bundles).
  7. E-invoicing converters (free tools, certified intermediaries).
  8. CBAM tools (90% exempt; enterprise).
  9. EUDR tools for Brazilian smallholders (free incumbents, low willingness to pay).
  10. Sales-tax, nexus and 1099 tools (funded incumbents; falling need).
  11. ADA Title II for governments (procurement).
  12. Click-to-cancel kits (no federal rule).

### Gaps
- The C1 platform-gap check (Wix, Webflow, Squarespace, Stripe, PrestaShop) and keyword volumes could not be completed because the search budget ran out and page fetching failed. These are the first validation steps before any build.
- No verified competitor revenue exists for any candidate; review counts are snapshots and may be inflated or stale.
