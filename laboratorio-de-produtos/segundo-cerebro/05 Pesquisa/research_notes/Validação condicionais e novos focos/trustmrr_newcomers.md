# TrustMRR newcomer proofs: recent, low-audience, non-AI products with verified revenue (data as of 2026-10-12)

Method note (applies to every section):
- **Crawl.** On 2026-10-12 I fetched every startup page listed in TrustMRR's startup sitemap: 11,403 profiles, 0 errors. I used polite connection-reusing curl at about 3.5 requests per second in total (80 per minute on each of 3 connections). The `RSC: 1` Next.js payload of each page embeds the full startup object (founded date, 30-day revenue, MRR, total revenue, subscriptions, X handle and follower count, marketing channels, pricing from AI enrichment, traffic, domain rating, for-sale status). I parsed that object. Raw rows are in `trustmrr_newcomers.csv`, next to this file.
- **Verified vs. unverified.** All revenue figures are TrustMRR's payment-processor-verified numbers (Stripe, RevenueCat, Polar and others; the provider is listed in the CSV). Seller messages, traffic claims and AI-enrichment fields are **self-reported or machine-generated**.
- **Screens:**
  - founded on or after 2025-04-01;
  - `currentLast30DaysRevenue` ≥ US$1,000;
  - non-AI: a keyword and category screen, then manual review that rescued false positives such as "insurance **agents**";
  - founder X followers under 2,000, or not shown.
- **Search budget.** I used 3 WebSearch calls. Google Autocomplete was queried directly. Mojeek returned nothing parseable this time.

## How is TrustMRR structured, and how completely can it be crawled?

### Takeaway
TrustMRR is a Next.js app. Its public startup pages carry the complete data object in the RSC payload, so the sitemap plus one request per startup gives a near-complete dataset. Category, channel, "recent" and "acquire" pages only render tiles, or load client-side. The official JSON API needs a key, and its Acceptable Use Policy bans cloning businesses and bulk republication.

### Cited Findings
- **robots.txt** allows everything (`Allow: /`) and lists three sitemaps: `sitemap.xml`, `compete-sitemap.xml` and `startup-sitemap.xml` — [robots.txt](https://trustmrr.com/robots.txt) (2026-10-12)
- **The sitemap index** splits into `sitemap-0.xml` and `sitemap-1.xml` (6,818 URLs combined), `compete-sitemap.xml` (130 URLs) and `startup-sitemap.xml` (11,403 unique startup slugs).
  - sitemap-0/1 contain 6,447 `/founder/` pages, 121 `/country/`, 104 `/tech/`, 39 `/channels/`, 37 `/newsletter/` issues, 32 `/category/` pages and 4 `/special-category/` pages.
  - They also list `/acquire`, `/recent`, `/stats`, `/feed`, `/search`, `/domain-rating`, `/docs/api/*` and `/mcp`.
  - Source: [sitemap.xml](https://trustmrr.com/sitemap.xml)
- **API.** TrustMRR's API (`https://trustmrr.com/api/v1/startups`, `/startups/{slug}`) needs a Bearer key (`tmrr_…`). Standard keys get 10 requests per minute and premium keys 60. Its AUP says "Cloning businesses, rebuilding TrustMRR, bulk republication, unauthorized public SEO pages… are prohibited" — [API docs](https://trustmrr.com/docs/api)
  - The list endpoint filters by `onSale`, `category`, `xHandle`, `teamSize`, `fundingStatus`, `min/maxRevenue` (last 30 days, in cents), `min/maxMrr`, growth and price.
  - Sort options: `revenue-desc` (default), `revenue-asc`, `price-*`, `multiple-*`, `growth-*`, `listed-*` and `best-deal`.
  - Source: [list-startups docs](https://trustmrr.com/docs/api/list-startups)
- **Category pages** show a count and the top 30 by total revenue, with no server-side pagination. For example: "Discover 766 startups with verified revenue" (Utilities) — [category/utilities](https://trustmrr.com/category/utilities). The SEO channel page says "Discover 1753 startups… growing through seo" — [channels/seo](https://trustmrr.com/channels/seo)
- **The /acquire page** (the for-sale marketplace) renders its listings client-side. The page claims "200K monthly visitors" — [acquire](https://trustmrr.com/acquire). The for-sale status and asking price sit in each startup object (`onSale`, `askingPrice`, `askingPriceHistory`, `sellerMessage`).
- **llms.txt** claims "over 15,000 startups listed, over 3,000 startups for sale… more than 115 acquisitions closed over the last six months" — [llms.txt](https://trustmrr.com/llms.txt). This exceeds the 11,403 sitemap slugs, so roughly 3,600 profiles (stealth or noindex) are probably not publicly crawlable.
- **The newsletter archive** (weekly, Dec 2025–Aug 2026) is dominated by AI products. The non-AI exceptions are AutoPrintEmail, Tree Nerd, PayLinks (Romania), WP Critique, Star-Keep, the TOEIC trainer, Opire, a Tesla dashcam app and the TikTok comment export — [newsletter](https://trustmrr.com/newsletter)
- **Base rates** from [stats](https://trustmrr.com/stats) (snapshot 2026-10-12):
  - Revenue distribution: 67.5% of startups at $0–1k, 16.9% at $1k–10k, 10.5% at $10k–100k.
  - Founder X followers: 54.2% have 0–1K, 12.0% have 1K–10K, 31.1% unknown.
  - "Revenue trends higher as founder audience grows, r=0.25, n=5,807", versus "Older startups trend toward higher total revenue, r=0.47" and "Revenue trends higher as Domain Rating increases, r=0.43".

**Funnel from my crawl (dated 2026-10-12)**

| Stage | Startups |
|---|---|
| Unique startup profiles | 11,403 |
| Founded on or after 2025-04-01 | 7,383 |
| …and ≥ $1k revenue in the last 30 days | 681 (vs 1,438 across all founding dates) |
| …and not AI-flagged | 297 |
| …and followers < 2k or not shown | 251 |
| After manually rescuing 16 keyword false positives | **267** |

Of the 267:
- 77 are anonymous or "confidential" profiles, with no name or website.
- 68 are mobile apps (RevenueCat, App Store or Superwall).
- The median follower count, where known (n=158), is 204.
- 116 made $1–3k in 30 days, 94 made $3–10k, and 57 made ≥$10k.
- The 367 AI-flagged rows that met the date and revenue screens had a median 30-day revenue of $3,106, versus $3,311 for the non-AI rows (my computation from the CSV).

### Inferences
- Audience matters less than age and domain authority: r=0.25 for followers vs 0.43 for DR and 0.47 for age. That fits a contact-less entrant who competes on SEO.
- More than half of all recent ≥$1k earners are AI-flagged (56% of the 681), but non-AI products earn just as much at the median. "Not AI" is not a revenue handicap on TrustMRR.
- About 29% of the qualifying set is anonymous, so a large share of the proofs cannot be inspected or replicated. The usable set is roughly 190 named products.

### Gaps
- About 3,600 profiles claimed in llms.txt are not in the sitemap, so they were not crawled.
- I used no API key, so I could not query TrustMRR's churn fields.
- `marketingChannels` is empty for 164 of the 267 qualifying products, so channel statistics are biased toward founders who filled it in.

## Which qualifying startups are the strongest newcomer proofs (ranked)?

### Takeaway
The strongest *new* proofs are boring, regulation- or document-driven tools:
- a viewer for Italy's mandatory .p7m signature files (P7M.io);
- field intervention-report and compliance-certificate SaaS (Valideo, FireCert, BasinCheck);
- prep for immigration and civic exams (FreeTCF, Francopass, KPSS);
- mandatory food-handler training (Spain);
- public-records aggregators (LandBankSearch).

Round-1 proofs still hold, with the numbers below re-dated 2026-10-12.

### Cited Findings
**Ranked newcomer proofs.** All rows are TrustMRR-verified, fetched 2026-10-12, and link to `https://trustmrr.com/startup/{slug}`. The ranking weighs recency, low audience, verified 30-day revenue, how inspectable and replicable the product is, and fit with the client.

| # | Product (slug) | Founded | Rev. 30d | MRR | Total | Subs | X followers | Channel (TrustMRR tag) | Price | Why it is a proof |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | P7M.io, Italy ([confidential-startup-70](https://trustmrr.com/startup/confidential-startup-70)) | 2026-03-28 | $4,627 | $460 | $20,798 | 261 | none shown | ASO, SEO | €3.99 single; €12.99/yr unlimited | Regulation-forced file format that no OS opens natively; solo build; for sale at $120,000 |
| 2 | Valideo, France ([valideo](https://trustmrr.com/startup/valideo)) | 2025-05-24 | $5,287 | $4,106 | $29,489 | 63 | 355 | ASO, blog, SEO, Facebook | Free 5 reports; €30/€69/€99 per month | Field intervention reports for technicians |
| 3 | FireCert, UK ([firecert](https://trustmrr.com/startup/firecert)) | 2026-02-24 | $5,003 | $4,896 | $18,138 | 42 | none | not given | £79/£129 per month | Fire-safety certificate and asset compliance for contractors |
| 4 | FreeTCF, Canada ([freetcf](https://trustmrr.com/startup/freetcf)) | 2025-07-01 | $23,640 | $23,887 | $184,412 | 1,247 | 57 | not given (RevenueCat, so mobile) | not shown | TCF Canada French exam prep (immigration) |
| 5 | Food-handler training, Spain ([startup-a66a92db7a72](https://trustmrr.com/startup/startup-a66a92db7a72), X @alimentiaes) | 2026-04-09 | $37,333 | $0 | $167,388 | — | 1 | SEO, Google Ads, Instagram | not shown | Mandatory "manipulación de alimentos" course; one-time sales |
| 6 | Francopass, France ([francopass](https://trustmrr.com/startup/francopass)) | 2025-10-01 | $3,756 | $1,695 | $16,392 | 132 | none | not given | from €4.99 | French naturalization interview and civic exam prep; for sale at $100,000 |
| 7 | Tifox, France ([tifox](https://trustmrr.com/startup/tifox)) | 2026-03-15 | $1,586 | $106 | $4,170 | 57 | 0 | SEO, content, blog, Instagram, Facebook | €12–25 per class per year | Digital "cahier de réussite" against the 2026 kindergarten curriculum; 9,007 visitors in 30 days |
| 8 | LandBankSearch, US ([landbanksearch-com](https://trustmrr.com/startup/landbanksearch-com)) | 2026-07-03 | $1,219 | $0 | $1,390 | — | none | SEO, blog, TikTok | Free; Pro $19/month | Aggregates 354 US land banks' off-MLS listings; 12,864 visitors in 30 days; DR 5; for sale at $45,000 |
| 9 | BasinCheck, Poland, sells to the US ([basincheck](https://trustmrr.com/startup/basincheck)) | 2025-12-21 | $2,235 | $895 | $5,576 | 5 | 113 | not given | $125/$250/$500 per month | Oil & gas safety audits with OSHA 300/300A exports |
| 10 | Play Designer Pro, UK ([play-designer-pro](https://trustmrr.com/startup/play-designer-pro)) | 2025-06-26 | $7,182 | $5,878 | $29,208 | 257 | 260 | not given | 14-day trial | Football playbook design plus auto-generated quizzes for players |
| 11 | 3dplotter, Greece ([3dplotter](https://trustmrr.com/startup/3dplotter)) | 2025-12-26 | $2,333 | $0 | $14,259 | — | 2 | not given | €29.90 one-time | Software that turns a 3D printer into a pen plotter |
| 12 | KPSS prep, Turkey ([hidden-business-71](https://trustmrr.com/startup/hidden-business-71)) | 2026-03-01 | $1,721 | $1,311 | $5,771 | 465 | 133 | ASO (Apple Search Ads at "~$0.14 CPA", self-reported) | subscription | Civil-service exam prep, "~2M+ candidates/yr" (self-reported); for sale at $8,000 |
| 13 | Tree Nerd Academy, round 1 ([tree-nerd-academy](https://trustmrr.com/startup/tree-nerd-academy)) | 2025-12-04 | $34,768 | $0 | $220,593 | — | 106 | not given | $60–229 one-time | Expert-built certification prep |
| 14 | Send Letters Online UK, round 1 ([send-letters-online-uk](https://trustmrr.com/startup/send-letters-online-uk)) | 2026-05-14 | $4,348 | $0 | $21,244 | — | none | not given | per letter | Physical-mail bridge |
| 15 | TruckerDB, round 1 ([truckerdb](https://trustmrr.com/startup/truckerdb)) | 2026-04-01 | $1,565 | $1,580 | $8,030 | 20 | none | SEO | $49/$99 per month | Public FMCSA records delivered as leads |

**Other round-1 items, as of 2026-10-12** (in the CSV):
- Subbasta (founded 2025-12-25): $5,368 in 30 days, $3,681 MRR.
- Harper (2025-09-01): $3,499 in 30 days, $2,575 MRR.
- FixMyExport (2025-11-01): $1,090 in 30 days.
- Contact Sheet Maker (2025-09-29): $1,204 in 30 days, $1,036 MRR, SEO.
- DownConvert SketchUp (2025-12-05): $5,395 in 30 days.
- PostalForm: $6,380 in 30 days, but it was founded 2024-10-01, outside the window.
- WCMultiShipping (2021) and the probate-leads product "b2bsaas" (2010; $62,393 in 30 days, $70,334 MRR): also outside the window; kept for reference.

**Primary-site evidence for the top new finds (fetched 2026-10-12)**
- **P7M.io:**
  - The TrustMRR description says: "Italy mandates CAdES digital signatures (.p7m) for public-sector invoices, contracts and court filings — and nothing on Windows, macOS, iOS or Android opens them natively… Ranked #3 on Google for the core queries, 40,000 organic clicks a month, zero paid acquisition, zero staff" (self-reported) — [TrustMRR](https://trustmrr.com/startup/confidential-startup-70)
  - The seller's note: "the Romanian market is localised but untouched" — same page.
  - The site processes files locally: "Nessun file viene caricato su server esterni". It also reads XML e-invoices — [p7m.io](https://p7m.io)
- **Valideo:** the site claims "4,9/5 sur +1000 téléchargements". It has SEO pages per trade (for example "Rapports d'intervention pour la recherche de fuite") and a "Modèles" (templates) section — [valideo.app](https://www.valideo.app)
- **LandBankSearch:** "Tracking 71 of 354 U.S. land banks… 79,529 properties for sale… land bank inventory lives on municipal websites, PDF lists, and legacy county portals" — [landbanksearch.com](https://landbanksearch.com)
- **FireCert:** the AI-enrichment target persona is "UK Fire Contractors, Security Engineers, Commercial Sites, HMOs & Housing", and the problem is managing certificates, assets and servicing in one system — [TrustMRR](https://trustmrr.com/startup/firecert). Its homepage renders client-side and gave no extra text — [firecert.uk](https://firecert.uk)

**Excluded or killed despite revenue (adversarial screen)**
- **VendPlacer** ($12,389 in 30 days, 122 subscriptions at $69/month, founded 2026-04-08) — [TrustMRR](https://trustmrr.com/startup/vendplacer). Its site claims "22,876 listed locations across 420 cities", with near-identical counts per city: Kabul 113, Shenyang 116, Dhaka 117, Belo Horizonte 119 — [vendplacer.com](https://vendplacer.com). That pattern suggests generated or scraped listings rather than vetted property owners, so I treat it as a deception and ToS risk, not as a proof.
- **coldcaller.pro** ($13,740 in 30 days): lists built from Google Maps ("Stop scrolling Google Maps. 500 companies to call") — [TrustMRR](https://trustmrr.com/startup/coldcallerpro). This carries Maps ToS and GDPR risk.
- **InstaTrack, OmegleWeb, the "lc" leaks community, GetXAPI, Social Fetch, ZocialComment and BettrBot:** ToS, piracy or gambling risk.
- **Services rather than software:** Altitude Cleaning Crew, Blizzard Wizard snow removal, Get Brazil Visa ("every application personally reviewed by a licensed Brazilian immigration lawyer", $599 — [TrustMRR](https://trustmrr.com/startup/get-brazil-visa)) and LegalOne (a French legal-notice broker).
- **Consumer mobile apps distributed through TikTok, ASO or Meta ads:** the Apple fee and creative budget fall outside the client's constraints, per round 1.

### Inferences
- Five of the top 12 new proofs are compliance or document tools sold to professionals: P7M.io, Valideo, FireCert, BasinCheck and Tifox. Their buyers must produce or read a specific artifact (a signed file, an intervention report, a certificate, a curriculum booklet). The value comes from the format and the workflow, not from AI.
- Exam prep shows up again, but the new winners are **immigration and civic exams** (TCF Canada, French naturalization, Turkey's KPSS), not professional certifications. The pass-or-fail stakes give the urgency, and an official syllabus replaces the need for a domain expert.
- Several newcomers are **for sale** within months of founding (P7M.io at $120k, Francopass at $100k, LandBankSearch at $45k, KPSS at $8k). The sellers describe these as "runs itself" assets, which matches low-moat SEO utilities.

### Gaps
- The Spanish food-handler business and FreeTCF hide their name or website, so I could not inspect their product, pricing or channel beyond the X handle.
- FireCert's and Play Designer Pro's acquisition channels are not tagged.
- I found no churn data for any product.

## For the top 10–15: competitor density, replicability from Brazil, blockers

### Takeaway
Most of these proofs are local niches with free or cheap alternatives. A Brazil-based developer can replicate the software, but each has a structural catch:
- **.p7m/.p7s:** free official viewers exist.
- **Food-handler training:** "gratuito/homologado" intent dominates in Brazil.
- **Civic tests:** Portugal's test is not yet regulated.
- **Field reports:** big incumbents exist in English, and Brazilian vistoria apps are saturated (round 1).

The best fits for this client are a CAdES/.p7m-style viewer (Italy or Romania), Portugal nationality and CIPLE A2 prep (the client is a native Portuguese speaker), and per-trade report templates in Brazil (feeding round 1's laudos idea).

### Cited Findings
**Demand signals (Google Autocomplete, queried 2026-10-12; suggestion lists only, not volumes)**
- Italy, "p7m": "p7m to pdf", "p7m viewer", "p7m viewer online", "p7m to pdf online", "p7m reader".
- Italy, "aprire file p7m": "…online", "**…online gratis**", "…gratis", "…aruba download", "…poste", "…android".
- Source: [suggestqueries it/it](https://suggestqueries.google.com/complete/search?client=firefox&hl=it&gl=it&q=aprire%20file%20p7m)
- Romania, "fisier p7m": only 3 suggestions ("deschidere fisier p7m", "fisier p7s p7m"), so demand is thin — [suggestqueries ro](https://suggestqueries.google.com/complete/search?client=firefox&hl=ro&gl=ro&q=fisier%20p7m)
- Brazil, "arquivo p7s": "…para pdf", "…como abrir", "…serpro", "visualizar arquivo p7s online", "abrir arquivo p7s online", "converter arquivo p7s em pdf", "app para abrir arquivo p7s" — [suggestqueries pt-BR](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=arquivo%20p7s)
- Portugal, in English: "portuguese citizenship test practice", "…practice pdf", "…exam", "…questions", "…language test sample". For "ciple a2": "…practice test", "…test examples", "…exam dates 2026", "…pdf". The Portuguese-language queries "exame cultura portuguesa nacionalidade" and "teste conhecimento nacionalidade portuguesa" returned **no suggestions** — [suggestqueries en-PT](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=pt&q=portuguese%20citizenship%20test)
- Brazil, "curso manipulador de alimentos": "…anvisa", "**curso gratuito** manipulador de alimentos", "…online **gratis homologado**", "sepe…". Spain, "carnet manipulador de alimentos": "…gratis", "…online homologado", "…sepe", "…oficial" — [suggestqueries pt-BR](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=curso%20manipulador%20de%20alimentos)
- Brazil, "relatório de visita técnica": "…pronto pdf", "…word", "…modelo", "…faculdade", "…escolar", "…abnt" (template and student intent). France, "rapport d'intervention": "…exemple word", "…pdf", "…maintenance" — [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=relat%C3%B3rio%20de%20visita%20t%C3%A9cnica)
- US, "vending machine locations": dominated by game queries (Fortnite and others) and "for sale near me".

**Competitors**
- **.p7m in Italy:**
  - Free tools named by guides: amministrazionicomunali.it's online viewer, CoolUtils' P7M-to-PDF converter, the P7Matic Google Drive add-on (in-browser, "not valid for legal verification"), and the certifiers' free desktop software (DiKe, ArubaSign, InfoCert). AgID's list of p7m software "is not updated" — [partitaiva.it](https://www.partitaiva.it/file-p7m/), [Workspace P7Matic](https://workspace.google.com/marketplace/app/p7matic/939303881041), [smartworld.it](https://www.smartworld.it/guide/come-aprire-file-p7m.html)
  - Despite these free options, P7M.io earns $4,627 in 30 days (verified, see above).
- **CIPLE A2 / Portuguese citizenship prep:**
  - Prep2go covers CIPLE, DELE, DELF A2 and CELI with "AI scoring"; AlternativeTo lists it as a one-time $300–500 licence — [AlternativeTo](https://alternativeto.net/software/prep2go/about)
  - PracticePortuguese is an A1/A2 European Portuguese course — [practiceportuguese.com](https://www.practiceportuguese.com/?p=194220)
  - An indie "a2ciple" practice app is being built in public — [wip.co](https://wip.co/projects/a2ciple)
  - Guides: [Portugalist](https://www.portugalist.com/a2-portuguese-courses/)
  - I found no product for Portugal's new civic test, which is expected because the test is not yet regulated.
- **Field reports:** in English, big incumbents exist (SafetyCulture, GoCanvas and others; my knowledge, not verified this round). In Brazil, round 1 documented the vistoria-app saturation (Devolus 10+ years, Vistortec and others) — see [[Armadilhas e ideias mortas]].

**Regulation (Portugal)**
- Lei Orgânica n.º 1/2026, of 18 May, added a "teste de cultura e valores democráticos" for naturalization. Topics: history, culture, political organization, symbols, rights and duties.
- **It cannot be required until a portaria regulates it** (format, pass mark, fees, venues). As of 2026-08-22 nothing was published, and one estimate puts it operational "between the end of 2026 and early 2027" (speculative).
- Brazilians must take it. Applications filed before the law follow the old rules. Minimum residence rose to 7 years (CPLP and EU) and 10 years (others).
- Source: [Eurodicas, 2026-08-22](https://eurodicas.com.br/teste-de-cultura-e-valores-democraticos-para-cidadania-portuguesa); law-firm and news summaries agree — [Cidadania e Visto](https://www.cidadaniaevisto.com.br/blog/nova-lei-nacionalidade-portuguesa-2026). These are secondary sources; I could not retrieve the Diário da República text (its search page is client-side).

**Replicability and blockers (my assessment, from the evidence above)**

| # | Proof | Competitor density | Same-market replication from Brazil | Localized BR/PT/LatAm version | Blockers |
|---|---|---|---|---|---|
| 1 | P7M.io | Many free tools; few paid ones | Yes. Browser-side CMS/CAdES parsing; sell through a merchant of record | Brazil .p7s: demand exists, but the government's ITI validator is free (not fetched this round) | "gratis" intent; needs SEO rank; the legal-verification claim must be avoided |
| 2 | Valideo | High in English; medium in France | Weak: French trades, need a French SEO footprint | Brazil: per-trade "relatório/laudo" templates (round-1 laudos) | Template-download intent; Brazilian WTP unproven |
| 3 | FireCert | UK contractor software exists (not counted) | Weak: UK fire standards knowledge, B2B trust | Brazil AVCB/PPCI: not researched | Domain expertise; sales trust |
| 4 | FreeTCF | Many TCF apps (not counted) | Possible, but mobile (Apple fee) | — | Apple $99/yr; content quality |
| 5 | Food-handler, Spain | High: "gratis/homologado/SEPE" | No (Spanish accreditation rules unverified) | Brazil: free SEPE/SENAC-type courses dominate the suggestions | Certificate acceptance and accreditation rules |
| 6 | Francopass | Few apps (not counted) | n/a (French) | **Portugal civic test + CIPLE A2**: native-speaker advantage | Test not yet regulated; CAPLE exam copyright |
| 7 | Tifox | Unknown | No (French curriculum) | Brazil: "parecer descritivo" in early-childhood education (not researched) | Teachers' low WTP in Brazil; AI generators |
| 8 | LandBankSearch | Low (claims the keyword) | Yes: public data and scraping of municipal sites | Brazil: leilão aggregators are crowded (my knowledge) | Data upkeep; already ranked |
| 9 | BasinCheck | Medium (EHS software) | Weak: OSHA domain, B2B sales | — | Domain |
| 10 | Play Designer Pro | Unknown | Possible (US coaches) | — | Domain; seasonality |
| 11 | 3dplotter | Low, but a tiny market | A direct clone would be parasitic | — | Small pool |
| 12 | KPSS | Many apps | n/a | — | Mobile |

### Inferences
- Across these proofs, a free alternative usually exists, but a paid product still wins with privacy, convenience and SEO rank (P7M.io against DiKe and Aruba; Francopass against the official booklet). The round-1 rule "the government gives it away free" is a pricing ceiling, not always a kill. It kills only when the free tool also ranks for the commercial query.
- The client's language edge points to **Portugal's naturalization test and CIPLE A2**. Brazilian CIPLE demand is nil (native speakers are exempt from the language test; my knowledge, unverified), but the civic test applies to Brazilians too (per the Eurodicas source above).

### Gaps
- I have no keyword volumes or CPCs for any query (no tool available).
- The official ITI validator (validar.iti.gov.br) was not fetched, so the Brazil .p7s competition is unverified.
- The number of naturalization applications in Portugal per year, and whether CIPLE A2 is also needed for permanent residence, were not found.
- Food-handler course accreditation rules in Spain and Brazil were not checked.

## Deep validation of the top 3 through gates G1–G8

### Takeaway
None is APPROVED. All three are CONDITIONAL, each with one cheap test. Ranking:
1. A signed-document (CAdES .p7m) viewer for Italy and Romania, sold per file and per year.
2. Portugal nationality civic-test and CIPLE A2 prep (English plus Portuguese).
3. Per-trade intervention-report generator for Brazil, which reinforces round 1's [[Gerador de laudos de vistoria e inspeção]].

### Cited Findings
**Candidate A: P7M/CAdES viewer and converter (Italy first, then Romania)**
- **Definition:** an in-browser, no-upload viewer for .p7m/.p7s files and XML e-invoices, with PDF extraction and signer details. One file free, then €3.99 per file or €12.99 a year. This mirrors P7M.io's pricing — [TrustMRR](https://trustmrr.com/startup/confidential-startup-70)
- **Buyer:** Italian professionals, PEC users and small firms receiving signed PA documents and e-invoices — [p7m.io](https://p7m.io). Pool size: gap.

| Gate | Verdict | Evidence |
|---|---|---|
| G1 WTP | **Weak pass** | P7M.io is verified at $4,627 in 30 days and 261 subscriptions. I found no second *paid* verified product; the alternatives are free tools (DiKe, ArubaSign, P7Matic) — [partitaiva.it](https://www.partitaiva.it/file-p7m/) |
| G2 Saturation / newcomer win | Pass for the newcomer proof; fail on clutter | P7M.io went from founding (2026-03) to #3 on Google (self-reported), but the market has many free tools |
| G3 Buyer power | Pass (low ticket) | Italian businesses; €3.99–12.99 |
| G4 Distribution | Conditional | Strong suggestions, but "gratis" intent dominates; Romania is thin — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=it&gl=it&q=aprire%20file%20p7m) |
| G5 Build ≤4 weeks | Pass | Browser CMS parsing; P7M.io was built solo in six months across three codebases (web, iOS, Android); the web-only scope is far smaller (inference) |
| G6 Not AI-core | Pass | — |
| G7 Legal / ToS / payments | Pass with caveats | No licence needed. Must not claim legally valid signature verification (P7Matic's own disclaimer). EU B2C VAT means using a merchant of record |
| G8 Unit economics | Doubtful | P7M.io reached about $4.6k on a claimed 40,000 clicks a month. The client would need a similar rank. $5k/month means about 1,250 single sales or about 385 yearly plans a month |

- **Score (1–5):** WTP 3, low saturation 2, buyer power 3, distribution 3, buildability 5, speed 4, low risk 4 = **24/35**.
- **Cheapest test:** ship the web viewer (≤7 days) plus five Italian landing pages ("aprire file p7m", "p7m in pdf", "fattura elettronica p7m"), then spend €40 on Google Ads in Italy.
  - **Pass:** CPC ≤ €0.40 and ≥1 paid conversion per 80 paid clicks.
  - **Fail:** zero sales on €40, or CPC above €0.80.

**Candidate B: Portugal nationality civic test and CIPLE A2 prep (web, EN and PT)**
- **Definition:** a question bank and mock tests covering the topics the law lists (history, institutions, symbols, rights and duties), plus CIPLE A2 practice exams written from scratch. Pricing would be €9–29 one-time, on the model of Francopass (from €4.99, $3,756 in 30 days) — [TrustMRR Francopass](https://trustmrr.com/startup/francopass)
- **Buyer:** naturalization applicants in Portugal, including Brazilians for the civic test and non-CPLP immigrants for CIPLE. Pool size: gap.

| Gate | Verdict | Evidence |
|---|---|---|
| G1 WTP | Pass (analogues) | Verified: FreeTCF $23,640, Francopass $3,756 and KPSS $1,721 in 30 days — [FreeTCF](https://trustmrr.com/startup/freetcf), [KPSS](https://trustmrr.com/startup/hidden-business-71). Paid CIPLE products exist (Prep2go, PracticePortuguese; self-reported) |
| G2 Saturation | Pass for the civic test (no product, since there is no test yet); medium for CIPLE | — |
| G3 Buyer power | Medium | Immigrants in an EU country; Francopass sells at €4.99+ |
| G4 Distribution | Conditional | English suggestions exist; Portuguese civic-test queries return no suggestions yet |
| G5 Build | Pass | A content platform; the client is a native speaker. Questions must be original, not copied from CAPLE exams |
| G6 Not AI-core | Pass | — |
| G7 Legal | Pass with caveats | No licence. The test's format and timing are undefined until a portaria is published — [Eurodicas](https://eurodicas.com.br/teste-de-cultura-e-valores-democraticos-para-cidadania-portuguesa). Do not imply official endorsement |
| G8 Unit economics | Unknown | $5k/month at €19 means about 240 sales a month. The pool is unknown, and the longer 7- and 10-year residence rule shrinks new eligibility |

- **Score:** WTP 4, low saturation 4, buyer power 3, distribution 3, buildability 4, speed 2, low risk 2 = **22/35**.
- **Cheapest test:** a bilingual landing page with a free 30-question CIPLE A2 mock plus a waitlist for the civic test, and €30 of Google Ads in Portugal on "ciple a2 practice test" / "portuguese citizenship test practice".
  - **Pass:** ≥10% of visitors give an email, and ≥3 pre-sales of a €19 CIPLE pack within 14 days.
  - **Fail:** <4% give an email, or zero pre-sales.
  - Re-check the Diário da República monthly for the portaria.

**Candidate C: per-trade intervention and inspection report generator (Brazil); evidence for round 1's laudos idea**
- **Definition:** a mobile-first web app with report templates per trade (leak detection, HVAC/PMOC visits, electrical, inspection), photos, signature and a branded PDF. Freemium, then a monthly plan. This copies Valideo's model: free for 5 reports a month, then €30–99 a month, with SEO pages per trade — [TrustMRR Valideo](https://trustmrr.com/startup/valideo), [valideo.app](https://www.valideo.app)

| Gate | Verdict | Evidence |
|---|---|---|
| G1 WTP | Pass abroad, unproven in Brazil | Verified: Valideo $5,287, FireCert $5,003, BasinCheck $2,235 in 30 days — [FireCert](https://trustmrr.com/startup/firecert), [BasinCheck](https://trustmrr.com/startup/basincheck). Brazilian WTP unverified (round 1) |
| G2 Saturation | Fail for generic vistoria in Brazil; possible for narrow engineering trades | Round 1 |
| G3 Buyer power | Medium | Brazilian technicians and small firms |
| G4 Distribution | Weak | Brazilian suggestions are template and student oriented ("modelo", "word", "pdf", "faculdade") — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=relat%C3%B3rio%20de%20visita%20t%C3%A9cnica) |
| G5 Build | Pass | — |
| G6 Not AI-core | Pass | — |
| G7 Legal | Pass | For engineering reports, the ART stays with the client (round 1) |
| G8 Unit economics | Unknown | — |

- **Score:** WTP 3, low saturation 2, buyer power 3, distribution 2, buildability 5, speed 3, low risk 4 = **22/35**.
- **Cheapest test:** the same one the round-1 laudos note specifies. The new evidence is that Valideo, FireCert and BasinCheck show non-AI field-report and compliance SaaS acquiring customers without an audience in 2025–2026.

### Inferences
- A is the fastest to test and the most self-contained, since there is no content risk and an MVP ships in a week. B has the best structural fit for the client (language, and no product exists yet), but it is blocked by regulatory timing. C adds evidence to an existing round-1 candidate rather than creating a new one.
- Adversarially: A's only verified earner may already hold the top organic slots and is for sale at $120k. A newcomer depends on paid search economics that I have not measured.

### Gaps
- I have no CPC or volume data for any of the three; the tests above are designed to measure it.
- Portugal's naturalization volume and the portaria date are unknown.
- Brazilian WTP for report generators is still unverified.

## Is there a pattern in which niches produce newcomer winners in 2025–2026?

### Takeaway
Non-AI newcomer wins cluster in three groups:
1. **Artifact-forced tools:** a regulation or a platform forces a file, report or certificate (.p7m, intervention reports, fire certificates, curriculum booklets, export repairs).
2. **High-stakes test prep** with an official syllabus (immigration and civic exams, food-handler cards).
3. **Public or scattered data aggregated into a search or alert product** (land banks, FMCSA, judicial auctions, Companies House).

SEO is the most-tagged channel. Revenue concentrates in mobile and B2C, which the client's budget excludes.

### Cited Findings
- Among the 267 qualifying products, the top categories are Mobile Apps 34, SaaS 27, Productivity 19, Software 18, Education 17, Health & Fitness 17, Marketing 15, Utilities 10 and Developer Tools 10 (my computation from the [CSV](trustmrr_newcomers.csv), source: [TrustMRR](https://trustmrr.com) pages, 2026-10-12).
- Channel tags: SEO 55, TikTok 33, Instagram 33, blog 29, Twitter 26, ASO 23, Facebook 22, Reddit 16, content marketing 16, YouTube 16, Meta ads 15, LinkedIn 14. 164 of the 267 have no tag.
- Payment providers: Stripe 170, RevenueCat 49, Superwall 18, Polar 10, Dodo 8. So 68 of 267 (25%) are mobile apps.
- Countries: US 72, unknown 53, FR 25, GB 17, CA 10, ES 8, DE 7, BG 6, BR 6. French-language local niches are over-represented: Valideo, Tifox, Francopass, LegalOne, coldcaller, MyFrank, Apogee.
- TrustMRR's stats correlations: followers r=0.25, domain rating r=0.43, startup age r=0.47 — [stats](https://trustmrr.com/stats)

### Inferences
- **By category:** compliance and document niches (Legal, Productivity, Utilities, B2B "SaaS") produce the inspectable, replicable non-AI winners. Mobile, Health and Entertainment produce larger but audience- or ads-driven winners.
- **By channel:** SEO is the channel most often tagged among replicable winners (P7M.io, Tifox, LandBankSearch, TruckerDB, Contact Sheet Maker, FixMyExport). The second pattern is ASO paired with an exam (KPSS, FreeTCF), which needs the Apple fee.
- **Local-language niches** in France, Italy, Spain and Malta repeatedly produce newcomer wins that English-first indie makers ignore. That supports a Portuguese-language play, in Portugal more than in Brazil, given Brazil's "gratuito" search intent.

### Gaps
- Channel data is self-declared and missing for 61% of the qualifying products.
- I could not measure seasonality or time to first revenue per product (TrustMRR's daily revenue series were not parsed).
