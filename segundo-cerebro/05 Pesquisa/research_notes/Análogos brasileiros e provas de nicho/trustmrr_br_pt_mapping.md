# TrustMRR newcomers mapped to Brazil and Portugal: screen of 267 non-AI products and deep validation of the top 3 (data as of 2026-10-12)

Method note:
- **Input.** The round-2 dataset (`trustmrr_newcomers.csv`, rows with `passes_all_screens=True`): founded on or after 2025-04-01, at least US$1k of verified 30-day revenue, non-AI, founder followers under 2k. That gives 267 rows. Details per product came from the raw crawl (`startups.jsonl`, fetched 2026-10-12), which holds each startup's TrustMRR object: description, AI enrichment, seller message and pricing.
- **Skipped.** These items are covered by a parallel researcher, so they were not screened: P7M.io, Valideo/laudos, FireCert, the Spanish food-handler course, Tifox, FreeTCF/Francopass/exam prep, and certified mail (Send Letters Online UK).
- **Demand check.** Google Autocomplete, queried 2026-10-12, with `hl=pt-BR&gl=br`, `hl=pt-PT&gl=pt`, `hl=es` (`gl=mx/es/ar`) and `hl=en&gl=us`. These are suggestion lists, not volumes. Caveat: the `gl=pt` suggestions often contain Brazilian phrasing (for example "vender empresa com cnpj"), so the PT-PT signal is noisy.
- **Competitors.** Checked with curl fetches of the competitor sites, plus 13 WebSearch calls (a US-only index). Google SERPs triggered a CAPTCHA in headless Chrome, and Bing returned irrelevant results, so I have **no rank data**.
- **Prior work honoured.** Ideas killed in [[Armadilhas e ideias mortas]] were not re-proposed without new evidence: consultório software, landlord apps, vistoria apps, job boards, lead scraping, Gmail-scope tools, Chrome extensions as a core business, and mobile apps under the Apple fee.

## For each of the 267 products: what it does, the Brazilian or Portuguese equivalent need, local competition, and keep or kill

### Takeaway
Of 267 products, 7 were skipped as out of scope. 64 more are anonymous or stealth profiles that cannot be inspected. About 45 are consumer mobile apps, and most of the rest are services, ToS-risky scrapers, global Mac utilities or saturated horizontal SaaS with no local angle. Only **three mappings survived the quick screen**:
- a Portuguese- and Spanish-language **SketchUp version downconverter** (analogue of DownConvert);
- a **carimbo CNPJ/profissional generator** (analogue of StampDy);
- a **Portugal judicial and tax auction aggregator** (analogue of Subbasta).

The deep validation below kills the second and third. Every other Brazil analogue I checked already has a paid local incumbent or a free substitute that dominates the commercial query.

### Cited Findings
**Screen summary (my computation from the CSV and annotations, 2026-10-12).**

| Verdict | Count |
|---|---|
| SKIP (parallel researcher) | 7 |
| KILL: uninspectable (anonymous or stealth, no product info) | 64 |
| KILL: already Brazilian (SMSGo, Videx) | 2 |
| KILL: other reasons | 191 |
| KEEP → deep-validated | 3 |

**Quick-check evidence behind the main kills (Autocomplete pt-BR/pt-PT, 2026-10-12, unless stated):**
- **QuoteDeck → corretores de plano de saúde:** saturated.
  - Agger Painel do Corretor costs R$79 per licence per month, with 750 operadoras — [Agger](https://agger.com.br/produtos/painel-do-corretor/)
  - Simulador Online starts at R$30 per month — [simuladoronline.com](https://www.simuladoronline.com/)
  - Cotador de Plano de Saúde costs R$77.90 per month, or R$41.41 per month on the annual plan — [Cotador](https://lp.cotadordeplanodesaude.com.br/)
  - Approvita — [Approvita](https://approvita.com.br/)
  - Baeta's multicálculo is free for partners — [Baeta](https://www.baeta.com.br/blog/multicalculo-gratis-conheca-o-simulador-online-da-baeta)
  - "simulador plano de saúde corretor" returned **0 suggestions**.
- **TruckerDB → new-company leads in Brazil:** the top suggestion is "lista de empresas abertas recentemente **grátis**" — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=lista%20de%20empresas%20abertas)
- **MyFrank → "qr code avaliação google":** the suggestions are about generating codes or buying placas, including "gerar qr code avaliação google **gratis**" — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=qr%20code%20avalia%C3%A7%C3%A3o%20google)
- **Passport Photo Ready → "foto 3x4 online":** the suggestions include "…grátis", "…fundo branco grátis", "…grátis sem marca d'água" and "…grátis canva". PT "fotografia tipo passe online" also shows "…gratuito" and "…online grátis" — [autocomplete BR](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=foto%203x4%20online)
- **Safeonward → "reserva de voo para visto":** only 2 suggestions in both BR and PT ("…", "como fazer…"), so demand is thin — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=reserva%20de%20voo%20para%20visto)
- **Attivita24 → "trespasse" (PT) and "passo o ponto" (BR):** the suggestions are local and classified-style ("passo o ponto em santos", "trespasse restaurante", "trespasse porto"), which is OLX and idealista territory. No platform-intent query appeared — [autocomplete PT](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-PT&gl=pt&q=trespasse)
- **Easy Moving Permits → "autorização de mudança":** the need is municipal (EMDEC, Transerp, CMTU, Curitiba, Niterói) — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=autoriza%C3%A7%C3%A3o%20de%20mudan%C3%A7a). The US original also posts physical no-parking signs: "We handle the permit, post the No Parking signs, and send photo proof" — [TrustMRR](https://trustmrr.com/startup/easy-moving-permits)
- **DrohnenAtlas → ANAC:** the suggestions point to official systems ("anac drone sisant", "drone anac cadastro") — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=drone%20anac)
- **Brazilian auctions (LandBankSearch analogue):** the suggestions are dominated by Caixa and the banks ("leilão de imóveis caixa", "…itaú", "…bradesco") — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=leil%C3%A3o%20de%20im%C3%B3veis)
- **Portugal-specific signals found:**
  - Stealth PT-founded software (`stealth-company-80`): founded 2026-08-19, $4,564 in 30 days, 33 subscriptions, SEO channel. It cannot be inspected — [TrustMRR](https://trustmrr.com/startup/stealth-company-80)
  - "ciple" suggestions include "ciple exame 2026" and "ciplemaster", but exam prep is out of scope (parallel researcher).

**Full screen of the 267 (sorted by verified 30-day revenue, USD; all rows link to their TrustMRR page, fetched 2026-10-12).** Columns: what it does / who pays · BR/PT equivalent need · local competitor quick check · verdict.

| # | Product | CC | Founded | Rev 30d | What / who pays | BR/PT need | Local competition (quick check) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | [Private Enterprise](https://trustmrr.com/startup/private-enterprise-67) | DE | 2026-06-28 | 208069 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 2 | [Anonymous Startup](https://trustmrr.com/startup/tro-kik) | US | 2025-10-04 | 202916 | Anonymous entertainment | — | — | KILL |
| 3 | [Private Venture](https://trustmrr.com/startup/private-venture-85) | US | 2025-07-15 | 115825 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 4 | [Stealth Company](https://trustmrr.com/startup/stealth-company-9) | ? | 2025-05-01 | 110714 | Generic/unclear: Social network tool with advanced features | — | — | KILL |
| 5 | [OmegleWeb](https://trustmrr.com/startup/omegleweb) | US | 2026-02-23 | 103027 | Random video chat | — | Trust & safety | KILL |
| 6 | [mobile app](https://trustmrr.com/startup/mobile-app-6) | IN | 2026-05-05 | 65391 | Consumer mobile app | — | Mobile/ASO/Apple fee outside constraints | KILL |
| 7 | [Private Venture](https://trustmrr.com/startup/private-venture-73) | US | 2025-11-09 | 65142 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 8 | [VirtualJK](https://trustmrr.com/startup/virtualjk) | SG | 2026-01-01 | 61843 | Consulting persona (AI) | — | AI/service | KILL |
| 9 | [Private Venture](https://trustmrr.com/startup/fast-scaling-saas) | ? | 2025-07-23 | 56875 | Generic/unclear: Non funded, 0 to $2m ARR (soon), quickest ever? | — | — | KILL |
| 10 | [PMSuite](https://trustmrr.com/startup/pmsuite) | ? | 2026-03-07 | 43149 | All-in-one business suite | Global | Crowded | KILL |
| 11 | [Private Venture](https://trustmrr.com/startup/anonymous-startup-95) | ES | 2025-11-11 | 41252 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 12 | [Stealth Venture](https://trustmrr.com/startup/anonymous-startup-2) | AU | 2025-06-02 | 40658 | Generic/unclear: One form to rule them all. | — | — | KILL |
| 13 | [Private Enterprise](https://trustmrr.com/startup/private-enterprise-76) | AE | 2026-06-11 | 39922 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 14 | [Unnamed Company](https://trustmrr.com/startup/depuff-ai) | ? | 2025-06-01 | 39683 | Mobile (AI-named) | — | Mobile | KILL |
| 15 | [Confidential Startup](https://trustmrr.com/startup/startup-a66a92db7a72) | ES | 2026-04-09 | 37333 | Excluded: parallel researcher (food-handler course, Spain) |  |  | SKIP |
| 16 | [uhoh.com](https://trustmrr.com/startup/uhoh-com) | CA | 2025-06-18 | 37213 | IT help desk service | — | Service | KILL |
| 17 | [Tree Nerd Academy](https://trustmrr.com/startup/tree-nerd-academy) | SE | 2025-12-04 | 34768 | Arborist cert prep $60–229 | — | Needs domain expert (round-1 kill) | KILL |
| 18 | [GoTall](https://trustmrr.com/startup/gotall) | ? | 2025-07-10 | 31747 | Height app (iOS) | — | Mobile consumer | KILL |
| 19 | [ACSPerf'](https://trustmrr.com/startup/acsperf) | FR | 2025-08-19 | 31295 | Engine remapping | — | Service | KILL |
| 20 | [Stealth Company](https://trustmrr.com/startup/popular-link-in-bio) | PL | 2025-05-01 | 31050 | Generic/unclear: Self growth link in bio. Feature social analytics for instag | — | — | KILL |
| 21 | [Festejar](https://trustmrr.com/startup/festejar) | ES | 2026-03-12 | 31003 | Ticketing for Catalan clubs | BR eventos | Sympla et al. | KILL |
| 22 | [3AK Track & Field](https://trustmrr.com/startup/3ak-track-field) | US | 2025-12-16 | 30883 | Track & field app | — | Mobile consumer | KILL |
| 23 | [Stealth Venture](https://trustmrr.com/startup/stealth-venture-27) | US | 2026-09-04 | 30668 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 24 | [Anonymous Startup](https://trustmrr.com/startup/anonymous-startup-19) | ? | 2026-03-27 | 30424 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 25 | [Private Enterprise](https://trustmrr.com/startup/private-enterprise-68) | US | 2025-07-23 | 29491 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 26 | [Stealth Company](https://trustmrr.com/startup/stealth-company-68) | FR | 2026-03-25 | 28413 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 27 | [Low Tide and Sunset, LLC](https://trustmrr.com/startup/low-tide-and-sunset-llc) | US | 2025-07-16 | 25246 | Hospitality services | — | Service | KILL |
| 28 | [Telestars](https://trustmrr.com/startup/telestars) | FR | 2025-11-23 | 24385 | Telegram creator monetisation | — | AI + creator | KILL |
| 29 | [Stealth Venture](https://trustmrr.com/startup/freetcf) | CA | 2025-07-01 | 23640 | Excluded: parallel researcher (exam prep) |  |  | SKIP |
| 30 | [ForYouGaming Inc.](https://trustmrr.com/startup/foryougaming-inc) | US | 2025-08-22 | 23071 | Online games | — | Games | KILL |
| 31 | [Unnamed Company](https://trustmrr.com/startup/unnamed-company-25) | ES | 2025-11-01 | 22837 | Social network app | — | Mobile | KILL |
| 32 | [Private Enterprise](https://trustmrr.com/startup/private-enterprise-35) | CH | 2025-11-18 | 22735 | Swiss fintech stealth | — | Uninspectable | KILL (uninspectable) |
| 33 | [Xagio Inc](https://trustmrr.com/startup/xagio-inc) | CA | 2025-05-13 | 22349 | SEO software | Global | Crowded | KILL |
| 34 | [Anonymous Startup](https://trustmrr.com/startup/anonymous-startup-20) | CA | 2025-08-01 | 22236 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 35 | [THE BLIZZARD WIZARD - Snow Removal Compa](https://trustmrr.com/startup/the-blizzard-wizard-snow-removal-company) | CA | 2025-10-26 | 20506 | Snow removal | — | Service | KILL |
| 36 | [Hidden Business](https://trustmrr.com/startup/stealth-app-1) | ? | 2026-01-02 | 19750 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 37 | [Plutocracy](https://trustmrr.com/startup/plutocracy) | AU | 2025-04-16 | 19154 | Shopify funnels $349+ | Global | Agency-style | KILL |
| 38 | [Cosmo](https://trustmrr.com/startup/cosmo) | US | 2025-11-21 | 19099 | Discord commerce | Global | Audience | KILL |
| 39 | [Stealth Company](https://trustmrr.com/startup/stealth-company-3) | US | 2025-05-01 | 18409 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 40 | [Anonymous Startup](https://trustmrr.com/startup/anonymous-startup-57) | FR | 2026-01-17 | 17710 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 41 | [JourneyFuse](https://trustmrr.com/startup/journeyfuse) | US | 2026-03-07 | 17699 | CRM for travel agents $25/mo | BR agências de viagem | Incumbent agency systems (not counted) | KILL |
| 42 | [Stealth Company](https://trustmrr.com/startup/stealth-company-63) | ES | 2026-06-25 | 17368 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 43 | [Anonymous Startup](https://trustmrr.com/startup/anonymous-startup-52) | FR | 2026-08-01 | 17331 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 44 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-9) | ES | 2025-09-10 | 17152 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 45 | [BreadSync](https://trustmrr.com/startup/breadsync) | US | 2026-03-07 | 15823 | Portfolio P&L dashboard | BR "controle de investimentos" | Kinvo/Gorila/free trackers | KILL |
| 46 | [Altitude Cleaning Crew](https://trustmrr.com/startup/altitude-cleaning-crew) | US | 2025-05-31 | 14956 | House cleaning | — | Service | KILL |
| 47 | [Sandimax](https://trustmrr.com/startup/sandimax) | CZ | 2025-05-15 | 13767 | Desktop wallpapers | Global | Mac/desktop utility, no local need | KILL |
| 48 | [coldcaller.pro](https://trustmrr.com/startup/coldcallerpro) | FR | 2026-04-01 | 13740 | Leads from Google Maps | — | Maps ToS (round-2 exclusion) | KILL |
| 49 | [Private Venture](https://trustmrr.com/startup/private-venture-59) | US | 2026-08-17 | 13354 | Consumer mobile app | — | Mobile/ASO/Apple fee outside constraints | KILL |
| 50 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-59) | FR | 2025-09-04 | 13266 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 51 | [Attivita24](https://trustmrr.com/startup/attivita24) | IT | 2025-10-13 | 12765 | Italian SME-for-sale marketplace; sellers pay €37+ listing | BR "passo o ponto"/"vender empresa"; PT "trespasse" | OLX/idealista trespasse categories free; two-sided cold start | KILL |
| 52 | [VendPlacer](https://trustmrr.com/startup/vendplacer) | US | 2026-04-08 | 12389 | Vending locations (suspect data) | — | Deception risk (round 2) | KILL |
| 53 | [Spool - Save your Thread](https://trustmrr.com/startup/spool-save-your-thread) | US | 2025-11-19 | 11997 | Screen-time app | — | Mobile consumer | KILL |
| 54 | [Venue visitor patterns worldwide - API p](https://trustmrr.com/startup/private-location-intelligence-api-platform) | SG | 2025-05-01 | 11637 | Foot-traffic API | — | Data | KILL |
| 55 | [LegalOne](https://trustmrr.com/startup/legalone) | FR | 2025-10-14 | 11364 | French legal-notice publication broker | BR: editais/balanços in jornais; PT: publicações online free | Service + regulated publication; PT publications free | KILL |
| 56 | [Getlead](https://trustmrr.com/startup/getlead) | PL | 2025-10-28 | 11363 | Lead scraping | — | ToS/LGPD | KILL |
| 57 | [Fundlyhub](https://trustmrr.com/startup/fundlyhub) | US | 2025-09-20 | 10741 | Fundraising platform | BR vaquinhas | Vakinha dominates | KILL |
| 58 | [Private Venture](https://trustmrr.com/startup/private-venture-80) | DE | 2026-08-01 | 9541 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 59 | [Private Venture](https://trustmrr.com/startup/private-venture-61) | FR | 2026-02-25 | 9375 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 60 | [Willo](https://trustmrr.com/startup/willo) | US | 2026-03-22 | 9327 | AI business builder | — | AI-core | KILL |
| 61 | [MyFrank](https://trustmrr.com/startup/myfrank) | FR | 2025-06-01 | 9294 | Google-review collection via employee QR codes | BR "qr code avaliação google" | Intent is "gerar … grátis"/placas; free QR generators | KILL |
| 62 | [Fast Corp Ltd.](https://trustmrr.com/startup/fast-corp-ltd) | BG | 2025-07-19 | 8645 | Bulgarian company formation + accounting (service) | PT: "abrir empresa em Portugal" | Contabilistas/services; needs licence | KILL |
| 63 | [Stealth Company](https://trustmrr.com/startup/stealth-company-37) | US | 2026-03-03 | 8544 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 64 | [InstaTrack](https://trustmrr.com/startup/instatrack) | ? | 2026-01-14 | 8517 | Instagram follower tracking | — | ToS | KILL |
| 65 | [Dashla](https://trustmrr.com/startup/dashla) | ? | 2026-03-11 | 8346 | Tesla dashboard iOS | — | Mobile; small BR Tesla base | KILL |
| 66 | [LC](https://trustmrr.com/startup/lc) | BR | 2025-11-14 | 8220 | Leaks community | — | Piracy/illegal | KILL |
| 67 | [Confidential Startup](https://trustmrr.com/startup/startup-b28a4b6ee235) | GB | 2026-09-28 | 8175 | Meta ad spy tool EU | — | ToS/AI | KILL |
| 68 | [Private Enterprise](https://trustmrr.com/startup/mobile-app) | XK | 2025-11-01 | 8158 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 69 | [Zero G Trading](https://trustmrr.com/startup/zero-g) | US | 2025-09-25 | 8084 | Trading algos | — | Regulatory (CVM) + crowded | KILL |
| 70 | [Private Enterprise](https://trustmrr.com/startup/medical-ai) | ? | 2025-12-26 | 8072 | Mobile health | — | Mobile | KILL |
| 71 | [Private Venture](https://trustmrr.com/startup/private-venture-71) | US | 2025-11-02 | 8071 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 72 | [Hidden Business](https://trustmrr.com/startup/confidential-startup-with-tj-atkinson) | ? | 2025-04-01 | 8041 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 73 | [GeoSpoof](https://trustmrr.com/startup/geospoof) | US | 2026-05-01 | 8007 | GPS spoofing | — | ToS | KILL |
| 74 | [Private Venture](https://trustmrr.com/startup/private-venture-50) | FR | 2025-11-25 | 7910 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 75 | [Werewolf : Undercover](https://trustmrr.com/startup/werewolf-undercover) | FR | 2025-09-01 | 7861 | Party game app | — | Mobile consumer | KILL |
| 76 | [PostPeer](https://trustmrr.com/startup/postpeer) | ? | 2026-04-01 | 7846 | Social posting API | Global | Platform risk | KILL |
| 77 | [Quantt](https://trustmrr.com/startup/quantt) | GB | 2025-12-16 | 7827 | Coding/finance education UK | — | Content business | KILL |
| 78 | [Bali Villa Hub](https://trustmrr.com/startup/bali-villa-hub) | IE | 2025-06-19 | 7636 | Bali long-term rental platform | — | Marketplace cold start | KILL |
| 79 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-45) | AU | 2025-12-27 | 7540 | Generic/unclear: Australia based saas business in education field. Easy to op | — | — | KILL |
| 80 | [Stealth Company](https://trustmrr.com/startup/stealth-company-48) | ? | 2026-06-05 | 7527 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 81 | [BambooVPN](https://trustmrr.com/startup/bamboovpn) | ? | 2025-09-01 | 7446 | VPN | — | Mobile consumer | KILL |
| 82 | [YoutubeToText](https://trustmrr.com/startup/youtubetotext) | NL | 2025-08-08 | 7407 | YouTube transcripts | Global | AI/commodity | KILL |
| 83 | [Crawlbyte](https://trustmrr.com/startup/crawlbyte) | US | 2025-05-25 | 7246 | Scraping API | — | ToS | KILL |
| 84 | [Play Designer Pro](https://trustmrr.com/startup/play-designer-pro) | GB | 2025-06-26 | 7182 | American-football playbooks | BR futebol coaches | Low WTP; domain | KILL |
| 85 | [DodgePrint](https://trustmrr.com/startup/dodgeprint) | US | 2025-07-15 | 7114 | Multichannel listing SaaS | BR: Bling/Olist incumbents | Crowded | KILL |
| 86 | [TollTracker](https://trustmrr.com/startup/tolltracker) | BG | 2025-09-01 | 6694 | Bulgaria average-speed camera alerts (iOS) | PT has average-speed sections (unverified this round) | Waze free; mobile/Apple fee | KILL |
| 87 | [Private Enterprise](https://trustmrr.com/startup/private-enterprise-39) | ? | 2026-07-09 | 6665 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 88 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-60) | MM | 2025-07-11 | 6569 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 89 | [Social Fetch](https://trustmrr.com/startup/social-fetch) | GB | 2026-03-31 | 6332 | Social scraping API | — | ToS | KILL |
| 90 | [Anonymous Startup](https://trustmrr.com/startup/anonymous-startup-40) | ? | 2026-05-02 | 6051 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 91 | [Hidden Business](https://trustmrr.com/startup/hidden-business-32) | ? | 2026-06-25 | 6049 | Consumer mobile app | — | Mobile/ASO/Apple fee outside constraints | KILL |
| 92 | [Hidden Business](https://trustmrr.com/startup/startup-af15723456d9) | US | 2025-08-17 | 5975 | Hotel booking resale | — | Travel ops | KILL |
| 93 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-64) | GB | 2025-11-21 | 5772 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 94 | [dal-app-1](https://trustmrr.com/startup/dal-app-1) | US | 2025-10-01 | 5728 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 95 | [DOWNCONVERT SKETCHUP FILES](https://trustmrr.com/startup/digital-natives-services-fz-llc) | AE | 2025-12-05 | 5395 | Converts newer .skp files to older SketchUp versions; architects/designers pay per file ($3.90) or $24.90 one-time | BR/PT-speaking SketchUp users stuck on 2017 Make (last free desktop) or older licences | No PT-BR converter found; free workarounds (3D Warehouse, Eneroth extension, Save As), Fiverr ~$10; DownConvert itself (EN, ES blog) | KEEP → deep-validated (A) |
| 96 | [Hidden Business](https://trustmrr.com/startup/hidden-business-62) | US | 2026-06-16 | 5368 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 97 | [Subbasta](https://trustmrr.com/startup/subbasta) | MT | 2025-12-25 | 5368 | Malta judicial-auction aggregator with translations; investors pay subscription + €249 POA | PT: e-leilões (OSAE), Finanças "venda eletrónica de bens penhorados", banks REO | Martelo (free), Bidizi (€9.90/mo), Licito (€9/report), PesquisaBensPenhorados, leiloeiras.pt | KEEP → deep-validated (C) |
| 98 | [Valideo](https://trustmrr.com/startup/valideo) | FR | 2025-05-24 | 5287 | Excluded: parallel researcher (laudos/Valideo) |  |  | SKIP |
| 99 | [StudyScout](https://trustmrr.com/startup/studyscout) | US | 2026-01-11 | 5276 | Paid studies aggregator | BR "pesquisas remuneradas" | Scam-heavy niche; UGC channel | KILL |
| 100 | [Private Venture](https://trustmrr.com/startup/private-venture-75) | US | 2025-04-30 | 5262 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 101 | [Stealth Venture](https://trustmrr.com/startup/stealth-app-2) | BR | 2026-02-02 | 5193 | Brazilian health app (stealth) | Already BR | Mobile | KILL |
| 102 | [Private Venture](https://trustmrr.com/startup/hrcn) | ? | 2025-04-01 | 5177 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 103 | [Steady - Fear of Flying](https://trustmrr.com/startup/steady-fear-of-flying) | ? | 2026-06-01 | 5042 | Fear of flying app | — | Mobile consumer | KILL |
| 104 | [FireCert](https://trustmrr.com/startup/firecert) | GB | 2026-02-24 | 5003 | Excluded: parallel researcher (FireCert) |  |  | SKIP |
| 105 | [Anonymous Startup](https://trustmrr.com/startup/anonymous-startup-3) | US | 2026-03-02 | 5000 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 106 | [BLOXG — Roblox Marketing Agency](https://trustmrr.com/startup/bloxg) | GB | 2026-04-27 | 4722 | Roblox influencer marketplace | — | Audience | KILL |
| 107 | [Anonymous Startup](https://trustmrr.com/startup/mathmpv-s-startup) | FR | 2025-12-23 | 4645 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 108 | [Anonymous Startup](https://trustmrr.com/startup/anonymous-mobile-app) | TR | 2025-12-17 | 4638 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 109 | [P7M.io — Italian digital signature reade](https://trustmrr.com/startup/confidential-startup-70) | IT | 2026-03-28 | 4627 | Excluded: covered by parallel researcher (P7M.io) |  |  | SKIP |
| 110 | [Stealth Company](https://trustmrr.com/startup/stealth-company-80) | PT | 2026-08-19 | 4564 | Portuguese-founded (PT) software, founded 2026-08-19, SEO, 33 subs, $4,564/30d | Unknown — stealth | Uninspectable; worth watching as a PT-market signal | KILL (uninspectable) |
| 111 | [Private Venture](https://trustmrr.com/startup/anonymous-startup-6a307f) | ? | 2025-11-30 | 4562 | Consumer mobile app | — | Mobile/ASO/Apple fee outside constraints | KILL |
| 112 | [Divine Widgets](https://trustmrr.com/startup/divine-widgets) | ? | 2026-03-03 | 4512 | Bible widget | BR evangelical market large | Mobile + Meta ads | KILL |
| 113 | [SportsApi Pro](https://trustmrr.com/startup/sportsapi-pro) | ? | 2025-12-16 | 4421 | Sports data API | — | Data licensing | KILL |
| 114 | [FiveML LTD](https://trustmrr.com/startup/fiveml-ltd) | CY | 2025-04-07 | 4378 | LinkedIn automation | — | ToS | KILL |
| 115 | [Nooze](https://trustmrr.com/startup/stealth-venture-46) | US | 2026-02-23 | 4358 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 116 | [Send Letters Online UK](https://trustmrr.com/startup/send-letters-online-uk) | GB | 2026-05-14 | 4348 | Excluded: parallel researcher (certified mail) |  |  | SKIP |
| 117 | [Private Venture](https://trustmrr.com/startup/startup-c1b5867bf083) | ? | 2026-06-04 | 4316 | TikTok repost remover | — | ToS; global | KILL |
| 118 | [GetXAPI - Cheapest Twitter API](https://trustmrr.com/startup/getxapi-cheapest-twitter-api) | ? | 2026-02-08 | 4265 | Unofficial X API | — | ToS | KILL |
| 119 | [Vermieter1.de](https://trustmrr.com/startup/vermieter1-de) | DE | 2025-11-11 | 4211 | German landlord tools | BR locador PF | 6+ BR apps (round 1) | KILL |
| 120 | [dal-saas-1](https://trustmrr.com/startup/dal-saas-1) | US | 2025-06-01 | 4143 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 121 | [BillionVerify](https://trustmrr.com/startup/billionverify) | HK | 2026-01-01 | 3983 | Email verification | Global | Commodity | KILL |
| 122 | [Sonar - ASO tool](https://trustmrr.com/startup/sonar-aso-tool) | SK | 2026-03-12 | 3876 | ASO tool | Global | Dev niche | KILL |
| 123 | [zocialcomment.com](https://trustmrr.com/startup/zocialcomment-com) | TH | 2026-03-29 | 3872 | TikTok comment export | — | ToS | KILL |
| 124 | [AppLaunchFlow](https://trustmrr.com/startup/applaunchflow) | DE | 2025-12-18 | 3867 | App store assets | Global | Dev niche | KILL |
| 125 | [Cooldock](https://trustmrr.com/startup/cooldock) | BG | 2026-06-22 | 3761 | Mac dock widgets | Global | Same | KILL |
| 126 | [MacWall](https://trustmrr.com/startup/macwall) | US | 2026-07-05 | 3700 | Mac wallpapers | Global | Same | KILL |
| 127 | [Formflow](https://trustmrr.com/startup/formflow) | US | 2025-07-29 | 3624 | Form builder | Global | Crowded | KILL |
| 128 | [Apogee](https://trustmrr.com/startup/apogee) | FR | 2026-02-01 | 3575 | Meta ads bulk uploader | Global | Platform risk | KILL |
| 129 | [ThreadCam](https://trustmrr.com/startup/threadcam) | ? | 2025-12-03 | 3553 | T-shirt mockups iOS | — | Mobile | KILL |
| 130 | [Renmory](https://trustmrr.com/startup/renmory) | TW | 2026-01-20 | 3527 | "Kahoot for weddings" one-time | BR casamentos | "jogo para casamento" suggestions are TV-show noise | KILL |
| 131 | [goundetected LLC](https://trustmrr.com/startup/goundetected-llc) | US | 2025-07-21 | 3487 | Multi-account browser | — | ToS | KILL |
| 132 | [artkit.cc](https://trustmrr.com/startup/artkit-cc) | HK | 2025-08-04 | 3425 | Collections app | Global | Consumer | KILL |
| 133 | [Promatic](https://trustmrr.com/startup/promatic) | US | 2025-05-29 | 3320 | HVAC permit ops for US contractors, $99/project | BR alvarás/ART: different system | Service-heavy; domain | KILL |
| 134 | [Unnamed Company](https://trustmrr.com/startup/unnamed-company-23) | ? | 2026-01-01 | 3311 | Budget app iOS | — | Mobile | KILL |
| 135 | [DISPOO](https://trustmrr.com/startup/dispoo) | FR | 2025-07-18 | 3307 | Cleaning-business academy (FR); entrepreneurs pay | BR: "como abrir empresa de limpeza" courses | Infoproduct market (Hotmart) crowded; needs a domain expert | KILL |
| 136 | [Leadbomb](https://trustmrr.com/startup/leadbomb) | US | 2026-03-30 | 3294 | Lead scraping (Maps, LinkedIn) | — | ToS/LGPD | KILL |
| 137 | [RareRoles](https://trustmrr.com/startup/rareroles) | US | 2026-03-21 | 3262 | Remote job list | BR "vagas remotas" | Free lists; job-board trap (round 1) | KILL |
| 138 | [TwoSquares](https://trustmrr.com/startup/twosquares) | GB | 2026-01-05 | 3244 | Agency hosting | — | Service | KILL |
| 139 | [QuoteDeck](https://trustmrr.com/startup/quotedeck-llc) | US | 2025-11-03 | 3230 | Health/life insurance quote decks for agents, $59.99/mo | BR corretores de planos de saúde need multicotação | Agger R$79/mo, Simulador Online from R$30, Cotador R$77.90, Approvita, Baeta free for partners | KILL |
| 140 | [CNG/OFL](https://trustmrr.com/startup/fof) | BR | 2026-03-31 | 3190 | Adult streaming | — | Excluded | KILL |
| 141 | [Private Enterprise](https://trustmrr.com/startup/private-enterprise-72) | ? | 2026-08-22 | 3190 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 142 | [OmniNotch](https://trustmrr.com/startup/omninotch) | ? | 2026-09-20 | 3183 | Mac notch app | Global | Same | KILL |
| 143 | [Terapi365](https://trustmrr.com/startup/terapi365) | CA | 2025-06-28 | 3182 | Therapist practice mgmt | BR psicólogos | Consultório software saturated (round 1) | KILL |
| 144 | [Private Enterprise](https://trustmrr.com/startup/startup-8dfc2d0ef703) | ? | 2025-11-19 | 3172 | Hidden camera scanner | — | Mobile | KILL |
| 145 | [Get Brazil Visa](https://trustmrr.com/startup/get-brazil-visa) | BR | 2025-12-15 | 3167 | Brazil visa help, lawyer-reviewed (service) | PT D7/D8 visa for Brazilians | Consultancies/lawyers; service not software | KILL |
| 146 | [Bibly](https://trustmrr.com/startup/bibly) | FR | 2025-12-20 | 3166 | Bible companion | Same | Mobile | KILL |
| 147 | [Krato](https://trustmrr.com/startup/krato) | ? | 2026-06-01 | 3159 | Workout tracker | — | Mobile | KILL |
| 148 | [SalesGenie](https://trustmrr.com/startup/salesgenie) | GB | 2025-11-01 | 3054 | Discord onboarding bot | Global | Audience | KILL |
| 149 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-35) | LT | 2025-12-06 | 3043 | Unnamed "generator" SaaS, LT, SEO, 182 subs | Unknown | Uninspectable | KILL (uninspectable) |
| 150 | [Stealth Company](https://trustmrr.com/startup/solodevmaxxing-stealth-app-01) | FR | 2026-03-01 | 3029 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 151 | [Voltage Learning](https://trustmrr.com/startup/voltage-learning) | US | 2025-06-25 | 3020 | Hardware interview prep | — | Niche content | KILL |
| 152 | [ExtraDock](https://trustmrr.com/startup/extradock) | BG | 2025-11-07 | 2978 | Mac docks | Global | Same | KILL |
| 153 | [StoreRadar](https://trustmrr.com/startup/storeradar) | FR | 2025-12-29 | 2933 | Shopify store lead lists $149 | BR Nuvemshop lists | Scraping/LGPD | KILL |
| 154 | [Resurf - One place for your ideas, refer](https://trustmrr.com/startup/resurf) | ? | 2025-12-25 | 2896 | Idea library Mac | Global | Consumer | KILL |
| 155 | [Hidden Business](https://trustmrr.com/startup/paireeo-inc) | CA | 2026-04-13 | 2872 | Event content curation | — | Unclear | KILL |
| 156 | [Study Guard](https://trustmrr.com/startup/study-guard) | ? | 2025-06-08 | 2840 | Flashcard app blocker | — | Mobile | KILL |
| 157 | [Safeonward - Onward flight ticket](https://trustmrr.com/startup/safeonward-onward-flight-ticket) | ? | 2026-06-01 | 2816 | Onward/visa flight reservation $11.90 | BR/PT travellers needing "reserva de voo para visto" | Only 2 PT suggestions; needs airline-booking backend | KILL |
| 158 | [Private Enterprise](https://trustmrr.com/startup/private-enterprise-47) | NL | 2025-04-07 | 2744 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 159 | [Profile Tracer](https://trustmrr.com/startup/profile-tracer) | BE | 2025-05-16 | 2731 | Trump-news alerts for traders | — | No equivalent | KILL |
| 160 | [NADefense](https://trustmrr.com/startup/nadefense) | US | 2025-08-01 | 2715 | Supplement | — | Physical/ANVISA | KILL |
| 161 | [DirectB2BLeads](https://trustmrr.com/startup/directb2bleads) | US | 2025-11-02 | 2649 | Done-for-you leads | — | Service | KILL |
| 162 | [Stealth Company](https://trustmrr.com/startup/stealth-company-24) | ? | 2026-03-26 | 2617 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 163 | [sellapis.xyz](https://trustmrr.com/startup/sellapis-xyz) | RO | 2025-09-29 | 2552 | Coding course | — | Creator business | KILL |
| 164 | [Stealth Company](https://trustmrr.com/startup/stealth-company-7392) | PL | 2026-09-16 | 2411 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 165 | [Confidential Startup](https://trustmrr.com/startup/to-20k-mrr) | ? | 2026-04-01 | 2385 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 166 | [Redsim eSIM](https://trustmrr.com/startup/redsim-esim) | EE | 2026-06-02 | 2383 | eSIM resale | BR travellers | Crowded resale; telecom partner | KILL |
| 167 | [3dplotter](https://trustmrr.com/startup/3dplotter) | GR | 2025-12-26 | 2333 | 3D printer → pen plotter software | Global hobby | Clone would be parasitic; tiny pool | KILL |
| 168 | [Omakase Design](https://trustmrr.com/startup/omakase-design) | US | 2025-05-21 | 2271 | Framer assets | Global | Design assets | KILL |
| 169 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-56) | ? | 2026-04-26 | 2257 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 170 | [BasinCheck](https://trustmrr.com/startup/basincheck) | PL | 2025-12-21 | 2235 | Oil&gas safety audits, OSHA exports | BR NR checklists (SST) | SST/PGR saturated (round 1) | KILL |
| 171 | [20-0](https://trustmrr.com/startup/20-0) | US | 2026-06-04 | 2190 | NFL fantasy game | — | No local need | KILL |
| 172 | [Streamloop](https://trustmrr.com/startup/streamloop) | ? | 2026-03-29 | 2181 | 24/7 prerecorded live streams | Global | Infra cost | KILL |
| 173 | [MEGAESIM.US](https://trustmrr.com/startup/megaesim-us) | RO | 2025-10-25 | 2142 | eSIM supply | — | Same | KILL |
| 174 | [Efferd](https://trustmrr.com/startup/efferd) | PK | 2025-09-26 | 2132 | shadcn blocks | Global | Dev assets | KILL |
| 175 | [Recipe One](https://trustmrr.com/startup/recipe-one) | ? | 2025-06-01 | 2086 | Recipe saver | — | Mobile | KILL |
| 176 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-65) | PL | 2025-04-22 | 2082 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 177 | [Sublo](https://trustmrr.com/startup/sublo) | DE | 2026-03-17 | 2069 | Dual-subtitle Chrome extension | Global | Extension economics (round-1 trap) | KILL |
| 178 | [Legal Tech](https://trustmrr.com/startup/legal-tech) | BG | 2025-10-17 | 2051 | Bulgarian lawyer cloud €19–79 | BR advogados | Astrea/ADVBOX entrenched (round 1) | KILL |
| 179 | [Ritmo](https://trustmrr.com/startup/ritmoapp) | ? | 2026-09-01 | 2031 | Dating app | — | Mobile | KILL |
| 180 | [Stealth Venture](https://trustmrr.com/startup/startup-dc384319ddd4) | US | 2026-01-10 | 2021 | Unnamed health web+app, 82K Google clicks/90d (self-reported) | Unknown | Uninspectable | KILL (uninspectable) |
| 181 | [Private Enterprise](https://trustmrr.com/startup/recrua) | US | 2026-09-07 | 2000 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 182 | [PolyScout](https://trustmrr.com/startup/polyscout) | GB | 2026-03-12 | 1989 | Polymarket tracker | — | Gambling-adjacent | KILL |
| 183 | [Tesla-Wrap](https://trustmrr.com/startup/tesla-wrap) | CH | 2025-12-22 | 1983 | Tesla wrap designs | — | No local need | KILL |
| 184 | [Dialvia](https://trustmrr.com/startup/dialvia-limited) | GB | 2025-04-05 | 1982 | Web calling credits | — | Telecom | KILL |
| 185 | [Private Venture](https://trustmrr.com/startup/startup-0f4ad90dad74) | TR | 2026-05-01 | 1961 | 24/7 prerecorded live streams | Global | Infra cost | KILL |
| 186 | [SubScene](https://trustmrr.com/startup/subscene) | US | 2025-10-09 | 1960 | AI long-form video | — | AI-core | KILL |
| 187 | [Videx](https://trustmrr.com/startup/videx) | US | 2026-07-08 | 1944 | Already Brazilian (video hosting) | — | Panda Video etc. | KILL (already local) |
| 188 | [StampDy](https://trustmrr.com/startup/stampdy) | HK | 2025-06-25 | 1940 | Online stamp/seal image maker; small businesses pay $2.5–3.5 per HD export | BR: "carimbo CNPJ digital", carimbo de psicólogo/médico for PDFs | Hanko Maker (free, PT-BR, CNPJ field), Sealgenerator PT (CNPJ template, freemium Pro), Stampdy /pt, physical carimbo R$23.69 | KEEP → deep-validated (B) |
| 189 | [Zenit - Wellness Habits](https://trustmrr.com/startup/zenit-wellness-habits) | ES | 2026-03-10 | 1931 | Wellness habits | — | Mobile | KILL |
| 190 | [Reelfolio](https://trustmrr.com/startup/reelfolio) | ? | 2025-11-16 | 1890 | Showreel maker | Global | Design-tool niche | KILL |
| 191 | [Private Enterprise](https://trustmrr.com/startup/private-enterprise-40) | US | 2025-07-16 | 1887 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 192 | [FluoTest](https://trustmrr.com/startup/fluotest) | NL | 2026-02-16 | 1882 | Decision scoring | Global | Vague | KILL |
| 193 | [Easy Moving Permits](https://trustmrr.com/startup/easy-moving-permits) | US | 2025-11-11 | 1819 | US moving-truck curb permits + physical no-parking signs | BR "autorização de mudança" (municipal: EMDEC, CET, Transerp) | Municipal, free/cheap; physical sign posting | KILL |
| 194 | [Private Enterprise](https://trustmrr.com/startup/private-enterprise-43) | FR | 2026-02-02 | 1811 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 195 | [The Travelling Technicians](https://trustmrr.com/startup/the-travelling-technicians) | CA | 2026-02-10 | 1811 | On-site repair | — | Service | KILL |
| 196 | [Xelio Technologies Inc.](https://trustmrr.com/startup/xelio-technologies-inc) | US | 2025-07-31 | 1798 | US LLC formation for emerging markets (service) | "abrir LLC nos EUA" for Brazilians | Service; agent/registered-agent ops | KILL |
| 197 | [ApexVol](https://trustmrr.com/startup/apexvol) | GB | 2025-09-30 | 1783 | Options analytics | BR B3 options | Nelogica/Profit incumbents | KILL |
| 198 | [Anonymous Startup](https://trustmrr.com/startup/godfather-venture) | ? | 2026-05-01 | 1759 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 199 | [Hidden Business](https://trustmrr.com/startup/hidden-business-58) | ? | 2026-02-02 | 1734 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 200 | [Hidden Business](https://trustmrr.com/startup/hidden-business-71) | TR | 2026-03-01 | 1721 | KPSS civil-service exam prep (iOS) | BR concursos públicos | Qconcursos/Estratégia/Gran giants | KILL |
| 201 | [Bubbly Phone](https://trustmrr.com/startup/bubbly-phone) | GB | 2025-10-19 | 1664 | Web calling | — | Telecom | KILL |
| 202 | [Clear Food](https://trustmrr.com/startup/clear-food) | DE | 2026-06-16 | 1651 | Food app | — | Mobile | KILL |
| 203 | [AutoPrintEmail](https://trustmrr.com/startup/autoprintemail) | AE | 2025-12-03 | 1640 | Auto-print emails/attachments | Global | "imprimir email automaticamente" no suggestions | KILL |
| 204 | [Private Enterprise](https://trustmrr.com/startup/private-enterprise-33) | ? | 2026-05-20 | 1639 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 205 | [SMSVia](https://trustmrr.com/startup/smsvia) | ? | 2026-01-16 | 1631 | Virtual numbers for verification | — | Telecom/ToS | KILL |
| 206 | [SMSGo](https://trustmrr.com/startup/smsgo) | BR | 2026-06-01 | 1625 | Already Brazilian (SMS API) | — | Already BR | KILL (already local) |
| 207 | [Winner: Sports Confidence](https://trustmrr.com/startup/winner) | CA | 2026-09-12 | 1624 | Athlete visualisation audio | — | Mobile/AI | KILL |
| 208 | [Tifox](https://trustmrr.com/startup/tifox) | FR | 2026-03-15 | 1586 | Excluded: parallel researcher (Tifox) |  |  | SKIP |
| 209 | [TruckerDB](https://trustmrr.com/startup/truckerdb) | US | 2026-04-01 | 1565 | FMCSA new-carrier leads; trucking-adjacent firms pay $49–99/mo | BR: new CNPJs / RNTRC | "lista de empresas abertas recentemente grátis" — free lists dominate | KILL |
| 210 | [Car Dealer Tracker](https://trustmrr.com/startup/car-dealer-tracker) | AE | 2025-07-02 | 1535 | Car dealer app | BR revendas | Revenda-system incumbents (not counted) | KILL |
| 211 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-69) | US | 2026-08-26 | 1506 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 212 | [Tap.Giving](https://trustmrr.com/startup/tap-giving) | US | 2025-11-23 | 1475 | Tap-to-pay donations for churches | BR dízimo via Pix | Church apps exist; payments/PSP | KILL |
| 213 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-21) | ? | 2025-06-01 | 1469 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 214 | [Hadal](https://trustmrr.com/startup/hadal) | US | 2026-03-05 | 1455 | Somali language app | Diaspora PT for kids | Mobile; tiny | KILL |
| 215 | [YG Coaching](https://trustmrr.com/startup/yg-coaching) | GB | 2025-09-26 | 1453 | Fitness coaching | — | Service | KILL |
| 216 | [SoftPxl](https://trustmrr.com/startup/unnamed-company-40) | CH | 2026-06-22 | 1442 | Wallpaper packs | Global | Same | KILL |
| 217 | [Pingo](https://trustmrr.com/startup/pingo) | US | 2025-11-16 | 1400 | Unclear | — | — | KILL |
| 218 | [SupaSidebar](https://trustmrr.com/startup/supasidebar) | ? | 2025-08-01 | 1396 | Mac sidebar | Global | Same | KILL |
| 219 | [Hidden Business](https://trustmrr.com/startup/hidden-business-27) | FR | 2026-02-01 | 1373 | French "Legal" stealth product, SEO/blog/Reddit/TikTok | Unknown | Uninspectable | KILL (uninspectable) |
| 220 | [Private Venture](https://trustmrr.com/startup/private-venture-72) | ? | 2026-05-26 | 1370 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 221 | [Margot](https://trustmrr.com/startup/margot) | FR | 2026-06-07 | 1366 | Wardrobe stylist | — | Mobile/AI | KILL |
| 222 | [Dilutracker](https://trustmrr.com/startup/dilutracker) | US | 2026-01-10 | 1342 | Stock dilution monitor | B3 has little dilution-trading culture | No equivalent | KILL |
| 223 | [LaunchPact](https://trustmrr.com/startup/launchpact) | AE | 2026-05-24 | 1341 | Product Hunt upvote swaps | — | ToS | KILL |
| 224 | [Freelance Writing Club](https://trustmrr.com/startup/freelance-writing-club) | US | 2026-04-07 | 1330 | Newsletter for freelance writers | — | Audience business | KILL |
| 225 | [Passport Photo Ready](https://trustmrr.com/startup/passport-photo-ready) | US | 2026-02-06 | 1308 | US passport photo editor $8.99 | BR "foto 3x4 online", "foto para visto americano"; PT "fotografia tipo passe online" | "grátis/fundo branco/sem marca d'água" intent; AI background removal core | KILL |
| 226 | [Schedulala](https://trustmrr.com/startup/schedulala) | CA | 2026-01-31 | 1293 | Social scheduler | Global | Crowded (mLabs in BR) | KILL |
| 227 | [Bidder iQ](https://trustmrr.com/startup/bidder-iq) | US | 2025-05-18 | 1284 | Collector-car comps | — | No BR data source | KILL |
| 228 | [HeyDoc Health](https://trustmrr.com/startup/heydoc-health) | AU | 2025-07-17 | 1268 | Telehealth referrals | BR telemedicina | CFM-regulated | KILL |
| 229 | [Mastros.online](https://trustmrr.com/startup/mastros) | IT | 2026-03-05 | 1248 | Export WhatsApp/Telegram members | — | ToS/LGPD | KILL |
| 230 | [Hidden Business](https://trustmrr.com/startup/pinsuite) | US | 2025-06-03 | 1245 | Image library | Global | Consumer | KILL |
| 231 | [Loggd․life](https://trustmrr.com/startup/loggd-life) | RO | 2025-12-07 | 1235 | Gamified habits | — | Mobile | KILL |
| 232 | [Gold List](https://trustmrr.com/startup/gold-list) | ? | 2025-12-12 | 1227 | Vocabulary app | — | Mobile | KILL |
| 233 | [Private Enterprise](https://trustmrr.com/startup/startup-e4ea585cabb2) | US | 2025-05-01 | 1225 | Local-service leads, flat fee | BR | GetNinjas dominates | KILL |
| 234 | [Viralcade](https://trustmrr.com/startup/viralcade) | TH | 2026-07-30 | 1225 | AI video | — | AI-core | KILL |
| 235 | [LandBankSearch.com](https://trustmrr.com/startup/landbanksearch-com) | US | 2026-07-03 | 1219 | US land-bank listing aggregator; investors pay $19/mo | BR: imóveis Caixa/leilões; PT: see Subbasta | BR aggregators crowded (round-1 note); "imóveis caixa venda direta" dominated by Caixa | KILL |
| 236 | [AntForms](https://trustmrr.com/startup/antforms) | IN | 2026-01-01 | 1206 | Form builder | Global | Crowded | KILL |
| 237 | [Unnamed Company](https://trustmrr.com/startup/contact-sheet-maker) | ? | 2025-09-29 | 1204 | Contact sheets for photographers (SEO) | Global; "folha de contato fotografia" has 1 suggestion | No PT demand | KILL |
| 238 | [iTechGuides](https://trustmrr.com/startup/itechguides) | ? | 2026-06-19 | 1183 | Software directory | — | SEO asset | KILL |
| 239 | [Lucky Dangle](https://trustmrr.com/startup/lucky-dangle) | NL | 2026-08-15 | 1181 | Screen charm Mac | Global | Same | KILL |
| 240 | [DrohnenAtlas](https://trustmrr.com/startup/drohnenatlas) | DE | 2026-05-01 | 1173 | German drone-rules app | BR ANAC/DECEA (SISANT, SARPAS) | Official free systems; mobile | KILL |
| 241 | [Embers](https://trustmrr.com/startup/embers) | ? | 2026-03-01 | 1164 | LinkedIn engagement leads | — | ToS | KILL |
| 242 | [Shotomatic](https://trustmrr.com/startup/shotomatic) | KR | 2025-04-20 | 1160 | Mac screenshots | Global | Same | KILL |
| 243 | [Dog Walker Central](https://trustmrr.com/startup/dog-walker-central) | US | 2025-09-25 | 1158 | Pet-care business software | BR pet sitters | Small, low WTP | KILL |
| 244 | [Stealth Venture](https://trustmrr.com/startup/stealth-venture-473) | NO | 2026-08-01 | 1144 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 245 | [Private Venture](https://trustmrr.com/startup/private-venture-13) | US | 2025-09-01 | 1142 | Consumer mobile app | — | Mobile/ASO/Apple fee outside constraints | KILL |
| 246 | [Glance Switch](https://trustmrr.com/startup/glance-switch) | IN | 2026-09-26 | 1139 | Gaze focus switch Mac | Global | Same | KILL |
| 247 | [esimNB](https://trustmrr.com/startup/esimnb) | US | 2026-05-14 | 1133 | eSIM resale | — | Same | KILL |
| 248 | [Confidential Startup](https://trustmrr.com/startup/confidential-startup-49) | ES | 2026-06-01 | 1128 | eSIM marketplace | — | Same | KILL |
| 249 | [Perfect HOA](https://trustmrr.com/startup/perfect-hoa) | US | 2025-06-07 | 1123 | HOA management $49/mo | BR condomínios | Superlógica-type incumbents; síndico tools (round 1) | KILL |
| 250 | [Magic Marketer](https://trustmrr.com/startup/magic-marketer-app) | AU | 2025-05-01 | 1119 | Social content generator | — | AI-core | KILL |
| 251 | [Private Venture](https://trustmrr.com/startup/aerolaunch) | ? | 2026-06-01 | 1105 | Astro themes | Global | Dev assets | KILL |
| 252 | [Hidden Business](https://trustmrr.com/startup/rentevo) | IT | 2026-01-05 | 1104 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 253 | [Private Venture](https://trustmrr.com/startup/private-venture-42) | FR | 2026-07-05 | 1102 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 254 | [Hidden Business](https://trustmrr.com/startup/hidden-business-66) | FR | 2026-02-04 | 1099 | Anonymous/stealth profile, no product info | Unknown | Uninspectable | KILL (uninspectable) |
| 255 | [FixMyExport](https://trustmrr.com/startup/fixmyexport) | IN | 2025-11-01 | 1090 | Restores Snapchat export metadata | Global; PT "recuperar fotos snapchat" is a different need | No local angle | KILL |
| 256 | [Smooth Capture](https://trustmrr.com/startup/smooth-capture) | ? | 2025-07-16 | 1085 | App demo videos (Mac) | Global | Mac utility | KILL |
| 257 | [divinetalk](https://trustmrr.com/startup/divinetalk) | BR | 2025-05-01 | 1076 | Scripture chat (BR) | Already BR | AI + mobile | KILL |
| 258 | [Ring Widget - Oura Ring widgets](https://trustmrr.com/startup/ring-widget-widgets-for-oura-ring) | CZ | 2026-01-16 | 1073 | Oura widgets | — | Mobile | KILL |
| 259 | [DockFlow](https://trustmrr.com/startup/dockflow) | BG | 2025-11-08 | 1068 | Mac workflow docks | Global | Same | KILL |
| 260 | [Klyk](https://trustmrr.com/startup/klyk) | US | 2026-07-09 | 1065 | AI test writing | — | AI-core | KILL |
| 261 | [TradeCopier.cloud](https://trustmrr.com/startup/tradecopier-cloud) | ID | 2026-01-01 | 1058 | Trade copier | — | Same | KILL |
| 262 | [Codelivly - Learn Cybersecurity](https://trustmrr.com/startup/codelivly-learn-cybersecurity) | GB | 2026-05-28 | 1047 | Cyber education | — | Content; crowded | KILL |
| 263 | [Kicksy](https://trustmrr.com/startup/kicksy) | US | 2025-06-01 | 1038 | Pregnancy kick counter | — | Mobile | KILL |
| 264 | [TaterCam](https://trustmrr.com/startup/tatercam) | US | 2026-04-24 | 1035 | Webcam AR avatar | Global | Creator niche | KILL |
| 265 | [eSIM Panel](https://trustmrr.com/startup/esim-panel) | GB | 2025-09-09 | 1028 | White-label eSIM store | — | Same | KILL |
| 266 | [Save Bulk Gmail Attachments](https://trustmrr.com/startup/save-bulk-gmail-attachments) | CZ | 2025-05-10 | 1028 | Bulk Gmail attachment saver $9/mo | "baixar anexos gmail" 4 suggestions | Gmail restricted scopes/CASA (round-1 trap) | KILL |
| 267 | [Dovey](https://trustmrr.com/startup/dovey) | US | 2026-02-21 | 1023 | Couples card game | — | Mobile | KILL |
### Inferences
- The local-language effect seen in round 2 (French, Italian and Maltese niches) **mostly does not carry over to Brazil**. In every Brazilian mapping I checked, either a paid local incumbent already exists (multicálculo, condomínio, consultório, revenda, concursos) or "grátis" dominates the query (3x4 photo, empresa lists, QR codes, carimbo).
- The proofs that do translate are **format- or version-forced utilities that are language-agnostic in function but English-first in marketing**. SketchUp downconversion is the clearest case: the original serves English, and since July 2026 Spanish through a content site, but not Portuguese.
- Portugal's market is small, and the one forced-need category with investor money (auctions) has already been aggregated by at least four local players in 2026.

### Gaps
- 64 anonymous or stealth rows (24%) cannot be mapped, including the PT-founded `stealth-company-80`. Their products are unknown.
- I have no search volumes or SERP ranks: Google returned a CAPTCHA in headless Chrome, and Bing returned irrelevant results.
- The quick competitor checks for low-priority kills (agency systems, revenda software, church apps) used my own knowledge plus round-1 notes, not fresh fetches. Those rows say "not counted".

## Which mappings keep the original's strengths: a verified payer type, a search-driven channel, and a forced or recurring need?

### Takeaway
Only the SketchUp downconverter keeps all three:
- a verified paying professional user;
- query-driven discovery with "online" intent in PT-BR, PT-PT and ES;
- a forced need, because SketchUp files cannot be opened in older versions.

The carimbo generator keeps search and a weak forced need, but loses the payer to free tools. The PT auction aggregator keeps the payer and search, but the gap has already been filled.

### Cited Findings
| Mapping | Verified payer (original) | Search-driven channel in BR/PT | Forced or recurring need | Strengths kept |
|---|---|---|---|---|
| **A. SketchUp downconverter, PT-BR + ES** | DownConvert: $5,395 in 30 days, $36,089 total since 2025-12-05 — [TrustMRR](https://trustmrr.com/startup/digital-natives-services-fz-llc). Paid substitutes: Fiverr gigs at ~$10 — [Fiverr](https://www.fiverr.com/sketchup3d/convert-your-sketchup-file-to-older-version) | pt-BR: "converter sketchup versão anterior online", "salvar sketchup em versao anterior online", "salvar sketchup 2026 em versao anterior", "abrir arquivo sketchup em versão anterior", "plugin salvar sketchup versao anterior" — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=salvar%20sketchup). The same appear in pt-PT and in es-MX/ES/AR ("convertir sketchup a versión anterior online", "bajar version sketchup online") — [autocomplete es](https://suggestqueries.google.com/complete/search?client=firefox&hl=es&gl=es&q=convertir%20sketchup) | Forced: "SketchUp files are not backward compatible" (AI enrichment) — [TrustMRR](https://trustmrr.com/startup/digital-natives-services-fz-llc). "sketchup 2017 make", "sketchup 2017 gratis" and "sketchup 2017 download mega" show a user base on old or free versions — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=sketchup%202017). Recurring per project, but bought one-off | **3/3** |
| **B. Carimbo CNPJ/profissional generator** | StampDy: $1,940 in 30 days, $12,797 total; its API key expired, and revenue was last synced 2026-09-29 — [TrustMRR](https://trustmrr.com/startup/stampdy) | pt-BR: "carimbo digital cnpj", "gerador de carimbo cnpj online", "carimbo online psicologo", "gerador de carimbo medico", but also "…gratis" and "…online grátis" — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=gerador%20de%20carimbo) | Custom, not legally mandated (no source found that says it is mandatory) | 1.5/3 (search kept; payer lost to free tools) |
| **C. Portugal auction aggregator** | Subbasta: $5,368 in 30 days, 130 subscriptions, but the pricing mixes services (POA €249, viewing €150, legal research €199+, 1% success fee) — [TrustMRR](https://trustmrr.com/startup/subbasta) | pt-PT: "leilões imóveis finanças", "e-leilões imóveis", "imóveis penhorados pelos bancos", "portal das finanças venda de bens penhorados" — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-PT&gl=pt&q=leil%C3%B5es%20finan%C3%A7as) | Recurring: investors check new listings weekly | 3/3 in principle, but the gap is already filled (see below) |

### Inferences
- What survives is not "the Brazilian version of a local regulation". It is **"the Portuguese-language version of a global, version-forced file utility"**. That is a different shape from round 1's regulated-artifact thesis. Its moat is SEO in an unserved language, not regulatory knowledge.

### Gaps
- I could not see whether DownConvert or its how-to-sketchup.com blog ranks for the Portuguese queries. The query "downconvert sketchup files" does appear as a pt-BR suggestion, so some Brazilians already search for the brand by name — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=downconvert)

## Deep validation of the top 3 through gates G1–G8

### Takeaway
- **A. SketchUp downconverter for PT-BR/ES: CONDITIONAL.** Two things block it:
  - Trimble now gates access to the C SDK, which a server-side converter needs, behind a request form (since May 2026). The SDK terms for a hosted commercial service are unverified.
  - The verified proof is contested by its own seller, who reports an average of $464/month against TrustMRR's $5.4k. The proof's Stripe account may also cover sister converter sites.
- **B. Carimbo generator: KILL.** At least three Portuguese-language generators are already live, two of them free with a CNPJ field. The ticket is too low for US$5k/month, and doctor or psychologist stamps carry a forgery-enablement risk.
- **C. Portugal auction aggregator: KILL.** Martelo is free with alerts. Bidizi charges €9.90/month, Licito €9 per report, and PesquisaBensPenhorados and leiloeiras.pt also exist, all live in 2026. Subbasta's revenue is partly services.

### Cited Findings

#### A. SketchUp version downconverter (PT-BR first, then ES-LatAm): CONDITIONAL
- **Product definition:** upload a .skp file and pick a target version (2017–2025). Get the converted file back in under 60 seconds, with files deleted after 7 days. PT-BR UI and checkout (Pix and card), and an ES version second. Pricing on the original's model: first file free, then a per-file price or a one-time unlimited licence.
  - The original charges $3.90 per file, or $24.90 one-time for unlimited (shown discounted from $49.90). Its claims: "13,000+ architects", 4.9/5 "by 2k+ designers", "Files auto-deleted after 7 days" (self-reported) — [DownConvert pricing](https://downconvert-sketchup-files.com/pricing)
- **Buyer and pool:**
  - Architects, interior designers, 3D freelancers and marceneiros (AI-enrichment persona: "Architects, Interior Designers, Freelance 3D Artists, BIM Managers") — [TrustMRR](https://trustmrr.com/startup/digital-natives-services-fz-llc)
  - Brazil's architect council had "more than 200 thousand" professionals expected to vote in 2023 (secondary; ArchDaily via search, not the CAU portal, which returned a WAF 403) — [ArchDaily tag CAU/BR](https://www.archdaily.com/pt/tag/cau-br)
  - I found no official count of SketchUp users in Brazil (gap). Students and marceneiros are an unknown share.
- **Pain evidence:**
  - pt-BR suggestions for the error and its workaround ("arquivo skp não abre", "abrir arquivo sketchup em versão anterior", "salvar sketchup 2026 em versao anterior") — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=arquivo%20skp)
  - SketchUp forum threads on downconverting run from 2017 to 2022 — [forum](https://forums.sketchup.com/t/conversion-to-older-sketchup-version/213816)
- **Competitors and substitutes (2026-10-12):**
  - **DownConvert** (EN): verified $5,395 in 30 days, $36,089 total, DR 28, for sale at $17,900. Two conflicts:
    - The seller writes: "DISCLAIMER TRUSTMRR TOOK RANDOM NUMBERS FROM MY STRIPE… 464 $/M AVERAGE REVENUE… 12K visitors/m" (self-reported).
    - The site footer links sister tools: Rhino File Converter, a GLB-to-glTF converter and how-to-sketchup.com.
    - So the verified figure may cover a network of sites — [TrustMRR](https://trustmrr.com/startup/digital-natives-services-fz-llc); [downconvert-sketchup-files.com](https://downconvert-sketchup-files.com/)
    - No /pt page exists (HTTP 404, 2026-10-12).
  - **how-to-sketchup.com** (same network): a Spanish article, "Bajar Versión de SketchUp: Convertir 2024 a 2017 Online (Gratis)", dated July 16, 2026, funnels to DownConvert. No /pt section exists (404) — [how-to-sketchup](https://how-to-sketchup.com/bajar-version-sketchup)
  - **Free substitutes:**
    - SketchUp desktop "Save As" an older version (needs a licence).
    - Uploading to 3D Warehouse and downloading an older version (reported to work, but not always; a YouTube guide says "hasta 2022").
    - The Eneroth "Open Newer Version" extension (Windows only).
    - Sources: [SketchUp forum](https://forums.sketchup.com/t/conversion-to-older-sketchup-version/213816); [YouTube](https://www.youtube.com/watch?v=EM_2Fkx5CMU)
  - **Paid substitutes:** Fiverr gigs at ~$10 per file ([Fiverr](https://www.fiverr.com/sketchup3d/convert-your-sketchup-file-to-older-version)), and a Spanish Patreon extension (OldSave) ([Patreon](https://www.patreon.com/arqMANES/posts/nueva-extension-102557553)).
  - **Format converters that do not downgrade versions:** AnyConv and InnerScene (SKP → FBX/GLB/OBJ/STL) — [AnyConv](https://anyconv.com/skp-converter/)
- **Weaknesses:**
  - The original's verified revenue is disputed by its seller and may include sister sites.
  - DownConvert has a content-site moat (DR 28, a how-to blog).
  - It is a one-time purchase with no recurring revenue.
  - Trimble could add free downsaving to SketchUp for Web, which would close the gap (speculative).
- **Demand signals:** strong suggestion coverage with "online" modifiers in pt-BR, pt-PT, es-MX, es-ES and es-AR (cited above). There is no "comprar" or price modifier. The intent is utility-plus-"online", and the Spanish lists include "free".
- **Channel:** SEO on 10–20 PT and ES pages (one per version pair, such as "salvar sketchup 2026 em 2017"), YouTube Shorts showing the fix, and Google Ads on the exact error queries.
- **Build complexity:**
  - The SketchUp C API "is an interface for reading and writing data to and from SketchUp models". The Windows library is "built using Microsoft Visual Studio 2022 (v143)… only 64-bit binaries" — [SketchUp C API docs](https://extensions.sketchup.com/developers/sketchup_c_api/sketchup/index.html)
  - So the converter needs a **Windows worker** (inference). The macOS C SDK was "not available for public download" in May 2026, and Trimble staff said "we are also implementing a short form so that people can officially request access to the SDK… so that we can understand more about who is using the C SDK and how". One user later reported filing a request with "no confirmation" (2026-05-27) — [SketchUp forum](https://forums.sketchup.com/t/sketchup-c-sdk-2026-macos-unavailable/346672)
  - The MVP is buildable in ≤4 weeks **if** SDK access is granted: a Next.js front end, a queue, and a Windows VM running a small C++ CLI (inference).
- **Time to first revenue:** 2–4 weeks after SDK approval via Google Ads; SEO takes months (inference).
- **Risks:**
  - SDK access refused, or terms that forbid hosted conversion (unverified).
  - Trimble product changes.
  - Windows VM cost against the R$700 budget (not priced this round).
  - Liability for corrupted files.
- **Unit economics (inference):**
  - At R$19.90 per file and R$97 one-time unlimited, US$5k/month (about R$27–28k, at an assumed ~R$5.5/US$, unverified) needs about 280 unlimited sales a month, or about 1,400 single files a month.
  - DownConvert reports 12k visitors a month (self-reported). Even taking the verified $5.4k at face value, matching it in PT+ES would need comparable traffic in two smaller languages.
  - A realistic PT-only ceiling looks like US$500–1,500/month. That is speculative, but it does not reach $5k without ES plus EN long-tail pages.
- **Legal and payment feasibility:**
  - No professional licence is involved.
  - The SDK licence terms were not retrievable (the developer.sketchup.com SDK page returned 404, and WebSearch did not surface the "API Terms of Service" text). **G7 is unverified.**
  - Payments for a Brazil-based seller (Stripe Brasil, Pix via a PSP, or a merchant of record for ES buyers) were not re-verified on primary sources this round (gap).

| Gate | Verdict | Evidence |
|---|---|---|
| G1 WTP (≥2 paid) | Weak pass | DownConvert verified, but the seller disputes the number; Fiverr gigs at ~$10 and the OldSave Patreon are paid substitutes |
| G2 Not saturated + newcomer could win | Pass on saturation (no PT-BR converter found); newcomer proof qualified | DownConvert was founded 2025-12, but probably rode an existing content site |
| G3 Buyer power | Pass (medium) | Professionals who are billing clients; low ticket |
| G4 Distribution without contacts | Pass (suggestions); volume unmeasured | Autocomplete PT-BR/PT-PT/ES |
| G5 MVP ≤4 weeks, no certification | **Conditional** | Depends on Trimble granting SDK access; needs a Windows worker |
| G6 Not AI-core | Pass | Deterministic file conversion |
| G7 Legal/ToS/payments verified | **Not verified** | SDK terms not retrieved; payments not re-checked |
| G8 Path to $5k/month | Doubtful | PT-only ceiling is likely below $5k; needs ES and EN as well |

- **Scores (1–5):** WTP 3, low saturation 4, buyer power 3, distribution 4, buildability 3, speed 3, low risk 2 = **22/35**.
- **Cheapest real-world test** (≈R$200, 21 days):
  1. **Day 0:** submit Trimble's C SDK access request and read the terms.
     - **Fail** and stop if there is no approval within 14 days, or the terms forbid a hosted service.
  2. **In parallel:** a PT-BR landing page on "converter sketchup versão anterior online" with checkout at R$19.90 per file (Pix and card). Fulfil manually during the test with a legitimately licensed SketchUp copy or the 3D Warehouse route, and disclose a turnaround of up to 2 hours. Spend R$150 of Google Ads on 5 exact queries.
     - **Pass:** CPC ≤ R$1.00 and ≥5 paid orders from ≤250 clicks.
     - **Fail:** ≤1 paid order, or CPC > R$2.00.

#### B. Carimbo CNPJ / professional stamp generator: KILL
- **Product definition:** a PT-BR generator for the Brazilian rectangular carimbo CNPJ (razão social, CNPJ, endereço, auto-filled from public CNPJ data) and for professional stamps, exported as transparent PNG/SVG for PDFs. Per-export pricing on StampDy's model: $2.5 PNG, $2.9 PNG+SVG+EPS, $3.5 all formats — [StampDy pricing](https://stampdy.com/pricing)
- **Buyer and pool:** small firms, MEIs and liberal professionals. Active companies were reported at ~25.4 million in July 2026, but that is a secondary blog figure without a primary source and conflicts with other secondary figures — [viniensina](https://viniensina.com.br/?p=4056). The official Mapa de Empresas panel loads client-side and gave no number (gap).
- **Pain and demand:** "carimbo digital cnpj", "carimbo cnpj digital", "gerador de carimbo cnpj online", "carimbo online psicologo", "gerador de carimbo medico", alongside "…gratis", "…online grátis" and "carimbo digital cnpj gratuito" — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=carimbo%20cnpj)
- **Competitors (2026-10-12):**
  - **Hanko Maker:** PT-BR, free, in-browser, with a field for "CNPJ, registro ou linha de apoio", PNG/SVG, and an optional $5 donation — [Hanko Maker](https://hankomaker.com/pt-br/carimbo-digital/)
  - **Sealgenerator:** PT version with a "Gerador de carimbo CNPJ online" template; free downloads carry a light watermark, and Pro removes it — [Sealgenerator](https://www.sealgenerator.com/pt)
  - **StampDy:** has a /pt locale ("Criar Carimbos Personalizados Online") — [StampDy PT](https://stampdy.com/pt)
  - **Physical carimbo CNPJ:** R$23.69 — [360imprimir](https://www.360imprimir.com.br/carimbo-cnpj)
- **Weaknesses and risks:**
  - The ticket is around R$10. US$5k/month would need ~2,700 exports a month (inference).
  - A tool generating "carimbo médico/psicólogo" images without verifying the council registration could enable fake medical certificates (my legal knowledge, not verified on a primary source this round).

| Gate | Verdict |
|---|---|
| G1 | Weak (StampDy verified; Sealgenerator Pro unverified) |
| G2 | **Fail**: 3+ Portuguese-language generators live, 2 free with CNPJ |
| G3 | Fail/weak: MEIs, low ticket |
| G4 | Pass (suggestions), but "grátis" intent |
| G5 | Pass |
| G6 | Pass (without the "AI stamp" features) |
| G7 | Risky (forgery enablement for professional stamps) |
| G8 | **Fail** |

- **Scores:** WTP 2, low saturation 1, buyer power 2, distribution 3, buildability 5, speed 5, low risk 2 = **20/35**.

#### C. Portugal judicial and tax auction aggregator (Subbasta analogue): KILL
- **Product definition:** one search and alert feed across e-leilões (OSAE), the Portal das Finanças "venda eletrónica de bens penhorados", Citius, bank REO portals and auction houses. Subscription plus due-diligence add-ons.
- **Buyer and pool:**
  - Investors with a Portuguese NIF; e-leilões participation is free for anyone with a NIF — [Montepio via search](https://www.montepio.org/?p=255732)
  - The idealista headline reports "Vendidos quase 9.000 imóveis penhorados no portal e-leilões desde 2016" — [idealista](https://www.idealista.pt/news/node/38490)
  - The number of active bidders is unknown (gap).
- **Demand:** "leilões imóveis finanças", "e-leilões imóveis", "imóveis penhorados pelos bancos", "casas penhoradas pelo banco caixa geral de depósitos", "portal das finanças venda de bens penhorados" — [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-PT&gl=pt&q=im%C3%B3veis%20penhorados). There is no "alertas leilões" suggestion (0).
- **Competitors (2026-10-12):**
  - **Martelo:** "O Martelo é gratuito? Sim, completamente… pesquisa, mapa, favoritos, alertas… 100% grátis", with email and Telegram alerts and a Pro tier for AT and Citius access — [Martelo](https://martelo.pt/)
  - **Licito:** free feed and alerts, then a "Relatório Licito 9 €", 5 for €39 or 15 for €99 (AI-generated due diligence) — [Licito](https://licito.pt/)
  - **Bidizi:** Bronze plan at €9.90/month (via search; the site returned a Vercel checkpoint, 429) — [Bidizi](https://bidizi.pt/)
  - **PesquisaBensPenhorados:** "3215 anúncios" of Finanças and e-leilões lots — [PesquisaBensPenhorados](https://www.pesquisabenspenhorados.com/)
  - **Leiloeiras Portuguesas** aggregator — [leiloeiras.pt](https://www.leiloeiras.pt/)
- **Weaknesses:**
  - The original's revenue includes services: POA onboarding €249, viewings €150, legal research €199+, a 1% success fee — [TrustMRR](https://trustmrr.com/startup/subbasta)
  - A Brazil-based solo developer cannot do viewings.
  - e-leiloes.pt did not respond from this sandbox, so its terms and API were not checked.

| Gate | Verdict |
|---|---|
| G1 | Pass (Subbasta verified; Bidizi and Licito paid) |
| G2 | **Fail**: 4–5 PT aggregators in 2026, one free with alerts |
| G3 | Pass |
| G4 | Pass |
| G5 | Pass (scrapers), but data upkeep |
| G6 | Pass |
| G7 | Unverified (source-site terms; EU database right, my knowledge) |
| G8 | Fail (the free incumbent caps price) |

- **Scores:** WTP 3, low saturation 1, buyer power 4, distribution 4, buildability 3, speed 3, low risk 2 = **20/35**.

### Inferences
- **None of the three is APPROVED.** A is the only live candidate. Its decisive unknown is **cheap and fast to resolve**: a Trimble SDK access request plus R$150 of PT-BR ads on the exact error queries.
- Adversarially, A's best-case outcome looks like a **side asset worth US$500–1,500 a month**, not a US$5k business, unless it expands into ES and EN long-tail pages and adjacent version and format converters (Rhino, Revit families, Promob). The original's owner already runs that network play, which suggests the format-converter niche is a portfolio game.
- Brazil analogues of TrustMRR newcomers repeatedly hit a pre-existing local SaaS at R$30–80/month (multicálculo, condomínio, consultório). That supports round 1's rule: new Brazil plays must find a gap that the local incumbents ignore. A fresh foreign proof does not guarantee one.

### Gaps
- No CPC or volume data for any query; test A is designed to measure them.
- Trimble's C SDK licence and API terms of service were not retrieved, so it is unknown whether hosted commercial conversion is allowed.
- The cost of a Windows worker (VM pricing) and Brazilian payment rails were not verified on primary sources this round.
- No official count of SketchUp users or of active CAU registrants for 2026; the CAU portal returned a WAF 403.
- I could not verify DownConvert's true revenue split between the SketchUp converter and its sister sites.
