# Paid data products on free public records (lead lists, alerts, monitoring, enrichment): US and Brazil, gate-tested for a solo Brazilian developer (data as of 2026-10-12)

Method note (applies to every section):
- All pages, APIs and files were fetched with curl on **2026-10-12** unless another date is given. Dataset counts come from my own queries of the official APIs and files on that date.
- "Verified" revenue means TrustMRR, which reads revenue from the founder's payment processor. Everything else (vendor pages, press releases, Apify listings) is **self-reported**.
- **Google Autocomplete** was queried at `https://suggestqueries.google.com/complete/search?client=firefox&hl=LANG&gl=CC&q=QUERY`. A suggestion means the query has some volume; it does not give a volume number.
- **Mojeek** returned HTTP 403 ("automated queries"). I used 15 WebSearch calls, which is the cap. Facts that come only from a WebSearch summary, and not from a page I fetched, are marked "(search result)".
- **Apify Store competitor counts** come from the public Store API (`https://api.apify.com/v2/store?search=QUERY`). They count actors matching the keyword, so some actors are only loosely related. User counts are Apify's own `totalUsers` and 30-day users.
- **Exchange rate:** R$ 5.40 per US$1, the rate the vault's [[Pagamentos e impostos]] note uses (US$1k = R$ 5,400).

## Key question 1: US datasets. For each: source and terms, update frequency, buyer, competitors and prices, and legal limits. How many competitors sell FMCSA new-carrier leads?

### Takeaway
- **Every US dataset in scope is free and works, but the raw "new registrations" layer is now commoditised.**
  - In 2026, Apify Store filled up with pay-per-use actors for every dataset: FMCSA 67, NPI 213, building permits 578, new business filings 276, SAM.gov 204, probate 45, FAA 33, liquor licences 35. Typical prices are US$1–20 per 1,000 records.
  - SaaS feeds sit on top of that layer at US$29–249/month.
- **FMCSA new-carrier leads are saturated.** I count at least 8 SaaS sellers (TruckerDB, TruckingLists, Carrier Signal, DOT Leads, RigDig/FleetSeek, Truckr, Carrier Network, truckingleads.com), plus 67 Apify actors.
- **Least crowded:**
  - NPPES weekly "new practices" (no dedicated SaaS found, but no proof of willingness to pay either).
  - Restaurant and liquor-licence openings (few vendors, priced at US$200–999/month, but the data is fragmented by state and has no contact fields).
- **Court records and tax-lien or pre-foreclosure data are either legally loaded or locked behind county-by-county access.** Examples: tenant screening counts as a consumer report under the FCRA, and county subscriptions or court approval are required in some places. Pre-foreclosure is already sold by PropStream at US$99/month.

### Cited Findings

**FMCSA new carrier registrations (data.transportation.gov)**
- **Source.** The live dataset is the "Company Census File" (az4n-8mr2), updated 2026-10-12 17:29 UTC. It covers active, inactive and pending FMCSA entities. Its fields include `add_date`, `dot_number`, `legal_name`, `phone`, `cell_phone`, `email_address`, `company_officer_1`, `power_units`, `carrier_operation` and docket fields. — [DOT metadata az4n-8mr2](https://data.transportation.gov/api/views/az4n-8mr2.json)
- **The census dataset round 1 cited is stale.** "Motor Carrier Registrations – Census Files" (4a2k-zf79) was last updated 2018-12-17. — [DOT metadata 4a2k-zf79](https://data.transportation.gov/api/views/4a2k-zf79.json)
- **New USDOT registrations per month (my count by `add_date`):**
  - 2026: Jan 14,782 · Feb 14,590 · Mar 17,494 · Apr 16,836 · May 16,934 · Jun 17,198 · Jul 16,187 · Aug 15,329 · Sep 14,656.
  - For comparison, Sep 2025 was 13,994.
  - The latest `add_date` is 20261011, and the file holds 4,516,324 records in total. — [Socrata API az4n-8mr2](https://data.transportation.gov/resource/az4n-8mr2.json)
- **September 2026 registrants (14,656 in total):**
  - Contact fields: 14,655 have an email, 14,656 a phone, 4,755 a cell phone and 14,545 a company officer name.
  - Type: 8,374 are active interstate and 5,781 active intrastate.
  - Docket: 1,801 have an MC docket in `docket1prefix`.
  - Source: [Socrata API az4n-8mr2](https://data.transportation.gov/resource/az4n-8mr2.json)
- **Alert datasets beside the census are refreshed daily.** As of 2026-10-12 these include ActPendInsur, InsHist, Insur, AuthHist, Revocation, BOC3 and the new "Motus" series. Together they support insurance and authority-change alerts. — [Socrata catalog, FMCSA](https://api.us.socrata.com/api/catalog/v1?search_context=data.transportation.gov&domains=data.transportation.gov&q=FMCSA&limit=40)
- **Motus migration.** One Apify actor says "FMCSA retired its legacy L&I 'Register' report in May 2026 (the Motus migration)", so tools that scrape li-public.fmcsa.dot.gov "no longer see new grants" (self-reported). It also says "FMCSA grants authority to 100–200 carriers and brokers every business day." — [Apify jobito/fmcsa-new-authority-feed](https://apify.com/jobito/fmcsa-new-authority-feed)
- **Motus rollout problems (search result).** Motus launched in May 2026. Carriers reported long holds, and FMCSA paused enforcement of biennial updates. FMCSA also warns that "third-party marketers" send urgent emails to carriers. — [TT News](https://www.ttnews.com/articles/fmcsa-motus-registration); [CCJ](https://www.ccjdigital.com/regulations/safety-compliance/article/15834781/motus-system-glitches-delays-fmcsa-addresses-carrier-frustrations); [HDT](https://www.truckinginfo.com/news/fmcsa-pauses-biennial-update-enforcement-amid-motus-transition)
- **FMCSA competitor census (prices fetched 2026-10-12):**
  - **TruckerDB.** US$49/month for the daily list ("15,000+ leads per month", delivered at 7am); Pro adds an insurance-renewal engine — [truckerdb.com](https://www.truckerdb.com/). TrustMRR verifies US$1,580 MRR, 20 subscriptions, US$8,030 all-time, founded April 2026, SEO as the only channel and domain rating 25. Its description says "$129/month" and "A buyer with any sales motion is sitting on an obvious growth lever" — [TrustMRR TruckerDB](https://trustmrr.com/startup/truckerdb)
  - **TruckingLists.** Daily feed at State US$29, Regional US$59, Nationwide US$99 and Team US$199 per month. One-time packs cost US$149 per state or US$699 for the nationwide file (2,213,034 records, of which 1,671,283 have an email). Checkout is via Creem, a merchant of record. — [truckinglists.com/pricing](https://truckinglists.com/pricing)
  - **Carrier Signal (newauthorityleads.com).** "Launching soon". Starter US$79 (1 state), Pro US$149 (5 states), Nationwide US$249 per month. It covers new and reinstated authorities, pending applications, insurance cancellations (X-dates) and suspensions. It is run by Cognitive Global, San Diego. — [newauthorityleads.com](https://newauthorityleads.com/)
  - **DOT Leads.** "Search 2.1M+ motor carriers with 30+ filters… new venture leads updated to the minute" (pricing page returned 404) — [dotleads.com](https://dotleads.com/)
  - **RigDig (FleetSeek domain).** "Find Trucking Leads Before Your Competitors" (price not extracted; page is JavaScript) — [fleetseek.com](https://fleetseek.com/)
  - **truckingleads.com.** "Real-time trucking insurance leads for agents" — [truckingleads.com](https://truckingleads.com/)
  - **Truckr.** A Product Hunt launch that "monitors FMCSA public records continuously and alerts you the moment a carrier becomes a buyer" — [hunted.space Truckr](https://hunted.space/dashboard/truckr)
  - **Carrier Network.** A trucking-insurance lead platform with a "New Authority" stream, per a March 2026 press release (search result) — [WBOC press release](https://www.wboc.com/online_features/press_releases/growing-usa-trucking-insurance-lead-platform-helping-agents-quote-faster/article_ef0a260a-66e9-5238-88b8-707d7f8d6e68.html)
  - **Highway.** carrierlists.com redirects to "Highway – It all starts with Carrier Identity", a carrier-verification product, not a lead list — [carrierlists.com](https://carrierlists.com/)
  - **Apify.** 67 actors match "fmcsa". The top ones have 127, 113, 55 and 50 total users, and only 3–13 users in the last 30 days — [Apify Store API "fmcsa"](https://api.apify.com/v2/store?search=fmcsa&limit=40). The jobito actor costs "from $20.00 / 1,000 carrier lead delivereds" and has 2 total users. It claims "comparable 'new MC authority' lead lists sell for $0.10–$1.00+ per lead" — [Apify jobito](https://apify.com/jobito/fmcsa-new-authority-feed)
- **FMCSA demand (Google Autocomplete, en-US):**
  - "new authority list" → "new mc authority list", "fmcsa new authority list", "new authority brokers list", "fmcsa new authority list pdf"
  - "trucking leads" → "trucking leads for sale", "trucking leads list", "buy trucking leads", "trucking insurance leads", "hotshot trucking leads"
  - "fmcsa data download" → "fmcsa census data download"
  - "new trucking authority leads" and "new carrier leads" return no suggestions.
  - Source: [Autocomplete "new authority list"](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=new%20authority%20list)

**NPI new providers (NPPES weekly files)**
- **Source and terms.** CMS publishes a full monthly file, a weekly incremental file and a deactivation file. The data is "disclosable under the Freedom of Information Act" and "There is no charge to download the data." — [CMS NPPES data dissemination](https://www.cms.gov/regulations-and-guidance/administrative-simplification/nationalprovidentstand/datadissemination)
- **Latest file.** The weekly V.2 file for 2026-10-05 to 2026-10-11 was posted on the download page. — [NPPES files](https://download.cms.gov/nppes/NPI_Files.html)
- **My test of that file (6.7 MB zip, 330 columns, 32,641 rows):**
  - 10,036 newly enumerated individuals (Type 1) and 2,763 organisations (Type 2).
  - Almost all have a practice-location phone (10,033 and 2,762).
  - There is no email column.
  - Top practice states: CA 1,746, TX 871, FL 842, NY 778, IL 606.
  - Top primary taxonomy codes: 106S00000X 2,157 · 163W00000X 724 · 390200000X 645 · 101YM0800X 615.
  - Source: [NPPES weekly file](https://download.cms.gov/nppes/NPPES_Data_Dissemination_100526_101126_Weekly_V2.zip)
- **Competitors.** Apify has 213 actors for "npi" and 132 for "nppes". The top ones have 130, 78, 78 and 76 total users — [Apify Store API "npi"](https://api.apify.com/v2/store?search=npi&limit=40). Specific feeds:
  - A "New US Healthcare Organizations — Weekly NPI Feed" sells US$9 per state edition or US$29 nationwide — [Apify fixmyerrorcode](https://apify.com/fixmyerrorcode/newly-enumerated-us-healthcare-organizations-weekly-npi-feed)
  - A behavioural-health weekly feed costs "from $9,000.00 / 1,000 full weekly editions" (search result) — [Apify actablesite](https://apify.com/actablesite/new-behavioral-health-practices-actor)
  - A registry monitor costs "from $1.00 / 1,000 provider results" (search result) — [Apify shrid5](https://apify.com/shrid5/npi-provider-leads)
  - No dedicated SaaS with a monthly price for "new practice" leads turned up (search result) — [WebSearch summary citing Apify and AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-6hrha5c7pe3am)
  - newpracticeleads.com returns "Service Suspended" — [newpracticeleads.com](https://www.newpracticeleads.com/)
- **Demand (Autocomplete):**
  - "medical billing leads" → "medical billing leads list", "medical billing leads usa", "buy medical billing leads", "medical billing client leads"
  - "npi database download" → "nppes npi data download"
  - "new npi list" and "new medical practices list" → no suggestions
  - Source: [Autocomplete "medical billing leads"](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=medical%20billing%20leads)

**SAM.gov registrants and USAspending awards**
- **SAM.gov public data** "constitutes… name, UEI, registration details, physical and mailing addresses, business types, PSC, NAICS and points of contact name and address". POC email and phone sit in FOUO/CUI tiers, and an API key is required. — [GSA Entity Management API](https://open.gsa.gov/api/entity-api/)
- **USAspending** answered an unauthenticated POST to `spending_by_award` with award, recipient, amount, agency and NAICS (tested 2026-10-12). — [USAspending API](https://api.usaspending.gov/api/v2/search/spending_by_award/)
- **Apify** has 204 actors for "sam.gov" (top: 172 and 118 users). — [Apify Store API "sam.gov"](https://api.apify.com/v2/store?search=sam.gov&limit=40)
- **Autocomplete:** "sam.gov new registrations list" and "new government contractors list" → no suggestions. — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=sam.gov%20new%20registrations%20list)

**New LLC and corporation filings**
- **Apify actors (search result):**
  - US$10 per 1,000 rows for CO, CT and NY, claiming lead services sell "the same public data for $50 to $200 a month".
  - US$3 per 1,000 for 8 states. This listing says the other states "sell their data ($500–$5,000/yr), gate it behind logins, or block programmatic access".
  - Sources: [Apify great_pistachio](https://apify.com/great_pistachio/us-new-business-filings); [Apify scrapemint](https://apify.com/scrapemint/new-business-registration-leads)
- **Texas SOS fee schedule (search result):** "Daily Filing Update/Replacement (Subscription): $60.00" and "Weekly Subscription New Filings… $20.00". — [Texas SOS bulk data](https://direct.sos.state.tx.us/help/help-corp.asp?pg=bulk)
- **Apify** has 276 actors for "new business filings". — [Apify Store API](https://api.apify.com/v2/store?search=new%20business%20filings&limit=40)
- **Autocomplete:** "new llc leads" and "new business filings list" return no commercial suggestions. — [Autocomplete "new llc leads"](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=new%20llc%20leads)

**Building permits**
- **Construction Monitor** (an article from about 2012, historical): US$96 for one month in Los Angeles, US$540 for six months, US$960 for a year — [JLC](https://www.jlconline.com/business/sales-marketing/pulled-permits-as-a-source-of-leads/)
- **PermitGrab** positions itself as flat-rate, against BuildZoom and Shovels, which it calls "priced for enterprise" (vendor positioning, search result) — [SaaSHub PermitGrab](https://www.saashub.com/permitgrab)
- **Apify** has 578 actors for "building permit" (top: 139 and 109 users). — [Apify Store API](https://api.apify.com/v2/store?search=building%20permit&limit=40)
- **Autocomplete:** "building permit leads" and "construction permit leads". — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=building%20permit%20leads)

**UCC filings**
- **Price levels (search result):**
  - List brokers sell fresh UCC leads at US$0.20–0.75 and aged ones at US$0.05–0.50, per an Apify actor's claim. The same actor sells them at US$0.02 per lead — [Apify deadwood UCC](https://apify.com/deadwood_data_solutions/ucc-filing-leads)
  - Fiverr MCA-lead sellers charge US$0.50 down to US$0.15 per lead. One buyer review says the leads were "recycled and resold at least 30 times" — [Fiverr](https://fiverr.com/leadsofglory/provide-fresh-mca-packages)
- **Autocomplete:** "ucc leads for sale", "ucc leads mca", "free ucc leads", "ucc filing leads". — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=ucc%20leads)
- **Apify** has 39 actors for "ucc" (lien scrapers for FL, NJ, NY). — [Apify Store API](https://api.apify.com/v2/store?search=ucc&limit=40)

**Liquor and health/restaurant permits**
- **NY State Liquor Authority "Current SLA Pending Licenses"** (f8i8-k2gm) is updated daily (2026-10-12).
  - Fields: application_id, type/class/description, legal name, DBA, premises address, received_date and status. No phone or email.
  - Pending applications received per month: Apr 188, May 273, Jun 289, Jul 540, Aug 415, Sep 405.
  - In September: 129 restaurants, 140 grocery stores, 54 food and beverage businesses and 20 liquor stores.
  - Source: [data.ny.gov f8i8-k2gm](https://data.ny.gov/resource/f8i8-k2gm.json)
- **Texas TABC "License Information"** (7hf9-qc9f) is updated daily (2026-10-12).
  - New original issues per month: May 758, Jun 816, Jul 837, Aug 725, Sep 912.
  - The `phone` field is empty for all 912 September records.
  - Source: [data.texas.gov 7hf9-qc9f](https://data.texas.gov/resource/7hf9-qc9f.json)
- **Chicago "Business Licenses"** (r5kz-chrr) is updated 2026-10-10. In September 2026 there were 61 new "Retail Food Establishment" issues. — [data.cityofchicago.org r5kz-chrr](https://data.cityofchicago.org/resource/r5kz-chrr.json)
- **Paid competitors for new-restaurant leads:**
  - Open Soon: "beginning at USD 500 per month", weekly updates for the whole US (search result; opensoon.com returned a near-empty page to curl) — [Springwise](https://springwise.com/uncategorized/sales-prospect-platform-lists-thousands-restaurants-open)
  - Starfleet "Preopening Restaurants Resource": under US$200/month (2021); twice-weekly reports; free trial added in January 2026 (search result) — [Starfleet 2021](https://starfleetmedia.com/2021/04/04/starfleet-media-launches-new-website-for-preopening-restaurants-resource-as-the-industry-gets-back-on-track/); [RTN 2026-01](https://restauranttechnologynews.com/2026/01/preopening-restaurant-leads-introduces-free-trial-no-credit-card-required/)
  - CSVFirst NYC newly licensed restaurants: US$999 (page says "$999/month with daily updates") — [CSVFirst](https://csvfirst.pythonanywhere.com/csv/nyc-newly-licensed-restaurant-dataset/)
  - What Now: "up to 40+ Pre-Opening B2B Sales Leads per month" (search result) — [whatnow.com](https://whatnow.com/montreal/pre-opening-restaurant-b2b-sales-leads)
  - Apify: 35 "liquor license" actors, all with 7 or fewer users — [Apify Store API](https://api.apify.com/v2/store?search=liquor%20license&limit=40)
- **Demand (Autocomplete):** "merchant services leads" → "merchant account leads", "buy merchant services leads"; "pending liquor license" → "pending liquor license ny", "nys sla pending liquor license"; "new restaurant leads" (exact only). "liquor license leads" → none. — [Autocomplete "merchant services leads"](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=merchant%20services%20leads)

**Court filings (evictions, divorce, probate), pre-foreclosure and tax liens**
- **FCRA.** A "consumer report" is any communication by a consumer reporting agency bearing on a consumer's "character, general reputation, personal characteristics, or mode of living" used for eligibility for credit, insurance, employment "or any other purpose authorized under section 1681b". Selling eviction records for tenant screening therefore puts the seller in consumer-reporting-agency territory. — [15 U.S.C. §1681a (LII)](https://www.law.cornell.edu/uscode/text/15/1681a)
- **CAN-SPAM** requires every commercial email to carry identification as an advertisement, an opt-out notice and a valid physical postal address. This is the buyer's outreach constraint. — [15 U.S.C. §7704 (LII)](https://www.law.cornell.edu/uscode/text/15/7704)
- **Probate:**
  - Verified: "b2bsaas" sells probate leads to real-estate investors and agents. It shows US$70,334 MRR, 629 subscriptions, US$990,295 all-time, founded March 2010 — [TrustMRR b2bsaas](https://trustmrr.com/startup/b2bsaas)
  - Realeflow: US$165, 220 or 320 per month for 250, 500 or 1,000 credits; 10 credits per lead under a month old; counties updated weekly (search result) — [Realeflow FAQ](https://realeflow.kayako.com/article/218-probate-leads-faq)
- **County access is gated (search result):**
  - Lake County, FL: US$60 setup plus US$180 per year — [Lake County Clerk](https://lakecountyclerk.org/subscribers)
  - Snohomish County, WA: US$100 per year — [Snohomish](https://snohomishcountywa.gov/5563/101772/Odyssey-Portal-Subscription)
  - Richland County, SC: probate access "requires approval from the court" — [Richland County](https://www.richlandcountysc.gov/Online-Services/Online-Data-Services)
- **Pre-foreclosure and tax liens:** PropStream costs US$99/month (US$81/month billed annually) — [PropStream pricing](https://www.propstream.com/pricing). Apify has 199 "foreclosure" and 45 "probate" actors — [Apify Store API](https://api.apify.com/v2/store?search=foreclosure&limit=40)
- **Autocomplete:**
  - "probate leads" → "for realtors", "for sale", "florida" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=probate%20leads)
  - "pre foreclosure leads" → "with phone number" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=pre%20foreclosure%20leads)
  - "divorce leads" → almost all memes — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=divorce%20leads)

**New business licences**
- City portals publish them, for example Chicago's r5kz-chrr, updated 2026-10-10. — [data.cityofchicago.org](https://data.cityofchicago.org/resource/r5kz-chrr.json)
- **Autocomplete:** "new business license listings", "clark county new business license list". — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=new%20business%20license%20list)

**FAA aircraft registrations**
- The FAA's free "Recent Registration Inquiry" shows registrations from the last 30 days, and the downloadable database updates "each Federal Working Day at Midnight" (search result) — [FAA Recent Registration Inquiry](https://registry.faa.gov/AircraftInquiry/Search/RecentRegistrationInquiry)
- A direct curl of ReleasableAircraft.zip returned HTTP 403 (Akamai) from this environment — [FAA registry zip](https://registry.faa.gov/database/ReleasableAircraft.zip)
- **Apify:** 33 "faa aircraft" actors, with 6 total users at most. Listed prices are US$5 and US$2 per 1,000 records — [Apify Store API](https://api.apify.com/v2/store?search=faa%20aircraft&limit=40); [Apify scrapesage FAA](https://apify.com/scrapesage/faa-aircraft-registry-scraper); [Apify jobito FAA](https://apify.com/jobito/faa-aircraft-registry-feed)
- **Autocomplete:** "aircraft owners mailing list" → none; "aircraft owner list" → "how do i find out who owns a private plane". — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=aircraft%20owner%20list)

**Analogues (verified on TrustMRR, 2026-10-12)**
- Harper (UK) links Companies House charges with Land Registry titles and flags borrowers "14–27 months into a bridging loan". It charges £300–£3,152/month and shows US$2,575 MRR from 10 subscriptions. — [TrustMRR Harper](https://trustmrr.com/startup/harper)
- Subbasta (Malta judicial auctions): US$3,681 MRR, 130 subscriptions, US$60,131 all-time, founded December 2025. — [TrustMRR Subbasta](https://trustmrr.com/startup/subbasta)

### Inferences
- **FMCSA: 8+ SaaS sellers and 67 Apify actors on the same free census, several launched in 2026.** TruckerDB (April 2026), TruckingLists, Carrier Signal (pre-launch) and Truckr all appeared this year. Saturation is accelerating, and price compression has started (US$29/month per state at TruckingLists).
  - TruckerDB's growth (zero to US$1,580 MRR in about 6 months) shows a newcomer could still win in **mid-2026**. That window is closing.
  - The TrustMRR description reads like a sale pitch ("A buyer with any sales motion…").
- **The verified winners sell derived signals or curated niches, not raw new-registration lists.** Harper's refinance-timing signal and b2bsaas's 16-year probate operation are examples. The raw-list layer is being driven toward US$1–20 per 1,000 records by Apify sellers, whose top actors have under 150 users each, which suggests little revenue per actor.
- **Low Apify user counts across all datasets suggest the real buyers (insurance agents, billing companies, POS reps) don't shop on Apify.** They buy finished SaaS with filters and email digests. The opportunity, if any, is in workflow and UX for non-technical buyers.
- **Legal map (US):**
  - Marketing uses of probate, permits, licences, carriers and NPIs are legal under federal law as far as I found. The buyer still carries CAN-SPAM and TCPA obligations.
  - Eviction records sold for tenant screening fall under the FCRA, which effectively excludes a solo developer.
  - Divorce leads have no commercial search demand and carry reputational risk.
  - Probate and divorce data sit in county portals that are often paid or approval-gated, so they are not a "free bulk dataset".
- **FMCSA contact data is unusually rich (about 100% email and phone).** NPPES has phone but no email; NY and TX liquor licences have no contact fields. So lead value per record is highest in trucking, and that is exactly why it is crowded.

### Gaps
- No search-volume numbers (no keyword tool). Autocomplete only shows that a query exists.
- Prices for RigDig/FleetSeek, DOT Leads, Carrier Network and Truckr were not extracted (JavaScript pages or none published). Open Soon's current pricing is unverified (2021–2026 secondary sources only).
- I did not fetch prices for established GovCon tools (HigherGov, GovTribe, GovSpend, Deltek) or permit-data incumbents (Shovels, BuildZoom, ConstructConnect).
- Not verified:
  - State-specific limits on eviction-record use (for example, California's masking of unlawful-detainer records; leginfo returned HTTP 403).
  - Whether FMCSA plans to mask contact fields after the Motus migration.
  - The number of US medical billing companies (the NPPES buyer pool).
  - How many September 2026 FMCSA registrants hold an MC number under Motus (only `docket1prefix='MC'` was counted).
- NUCC labels for the NPPES taxonomy codes are from my own knowledge and were not fetched: 106S00000X behaviour technician, 163W00000X registered nurse, 390200000X student, 101YM0800X mental-health counsellor.

## Key question 2: Brazilian datasets (CNPJ, PNCP, Querido Diário, leilões and Caixa, INPI, Anatel/ANVISA/CVM), their resellers and prices, and LGPD limits

### Takeaway
- **All the data sources work from a script, with three exceptions:**
  - INPI's RPI portal was "em manutenção" (HTTP 503), but INPI's open-data portal works and is current to RPI 2909 (2026-10-06).
  - Caixa's property CSV is behind a Radware CAPTCHA.
  - Querido Diário's API moved hosts and covers only 510 of 5,570 municipalities.
- **The resale markets are crowded at the low end:**
  - CNPJ lists: Speedio R$ 719+/month, EmpresAqui from R$ 139.90/month, Casa dos Dados, Econodata, CNPJ.biz, and 194 Apify actors.
  - Licitação alerts: Alerta Licitação at R$ 44.90/month covers all states and 6,441 portals. The government's free Contrata+Brasil sends WhatsApp alerts to MEIs.
  - Auctions: Mapa do Leilão claims 44,180 users at R$ 74.90/month.
  - Trademark watch: MonitoraMarca already sells self-serve INPI collision alerts at R$ 19.90–149/month.
- **LGPD allows processing public data only with regard to "a finalidade, a boa-fé e o interesse público"** that justified its publication. That constrains marketing use of MEI and individual (CPF) records.

### Cited Findings

**Receita Federal CNPJ open data and its resellers**
- **Dump.** The 2026-09 dump was published 2026-09-14 on a Nextcloud share. It contains Empresas0–9, Estabelecimentos0–9 (Estabelecimentos0 is 2.24 GB; the others are about 340 MB each), Socios0–9, Simples and lookup tables. Folders run monthly up to 2026-09; 2026-10 is not yet posted as of 2026-10-12. — [Receita CNPJ share (WebDAV listing)](https://arquivos.receitafederal.gov.br/index.php/s/YggdBLfdninEJX9)
- **Old URL is gone.** `arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/` returned 404. — [old path](https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/)
- **My test of shard Estabelecimentos1** (4,753,435 rows) found only 27 establishments opened in 2026. New companies therefore concentrate in another shard, so a "newly opened" pipeline must process the 2.24 GB Estabelecimentos0 each month. — [Receita share](https://arquivos.receitafederal.gov.br/index.php/s/YggdBLfdninEJX9)
- **Resellers (prices fetched 2026-10-12):**
  - Speedio: R$ 719, R$ 1,079 and R$ 1,379 per month (12-month commitment on the top tier) — [Speedio planos](https://www.speedio.com.br/planos)
  - EmpresAqui: R$ 299.90 to R$ 599.90 list per month, or from 12× R$ 139.90 — [EmpresAqui planos](https://www.empresaqui.com.br/planos)
  - cnpjnovos.com.br: "EcoBigData D0 · Empresas nascendo agora" — [cnpjnovos.com.br](https://www.cnpjnovos.com.br/)
  - Casa dos Dados (Cloudflare "Just a moment"), Econodata ("Você atingiu o limite de consultas") and CNPJ.biz ("Acesso Bloqueado") were not readable by curl — [Casa dos Dados](https://casadosdados.com.br/); [Econodata](https://www.econodata.com.br/planos); [CNPJ.biz](https://cnpj.biz/)
  - Apify: 194 "cnpj" actors (top: 311, 180, 164 and 151 users) — [Apify Store API "cnpj"](https://api.apify.com/v2/store?search=cnpj&limit=40)
- **Demand (Autocomplete, pt-BR):** "lista de empresas abertas recentemente grátis" (first suggestion), "leads de empresas gratuito", "comprar leads de empresas", "lista de cnpj ativos". — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=lista%20de%20empresas%20abertas)
- **LGPD art. 7:**
  - §3: "O tratamento de dados pessoais cujo acesso é público deve considerar a finalidade, a boa-fé e o interesse público que justificaram sua disponibilização."
  - §6: waiving consent "não desobriga os agentes de tratamento das demais obrigações".
  - Source: [Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)

**PNCP open API and licitação-alert tools**
- **API test (2026-10-12).** `/api/consulta/v1/contratacoes/publicacao` works without a key, and Brazil geoblocking did not apply from this environment.
  - Volume: 1,666 pregões eletrônicos were published on 2026-10-09 alone.
  - Fields include objetoCompra, valorTotalEstimado, órgão, município/UF, dataEncerramentoProposta and linkSistemaOrigem.
  - The item endpoint `/api/pncp/v1/.../itens` timed out at 60 s.
  - Source: [PNCP consulta API](https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao?dataInicial=20261009&dataFinal=20261009&codigoModalidadeContratacao=6&pagina=1&tamanhoPagina=10)
- **One week (2026-10-05 to 09):**
  - 7,904 pregões eletrônicos (modality 6), 1,218 concorrências eletrônicas (4), 14,050 dispensas (8) and 5,150 inexigibilidades (9) — [PNCP API](https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao?dataInicial=20261005&dataFinal=20261009&codigoModalidadeContratacao=6&pagina=1&tamanhoPagina=10)
  - 41,030 contracts — [PNCP contratos API](https://pncp.gov.br/api/consulta/v1/contratos?dataInicial=20261005&dataFinal=20261009&pagina=1&tamanhoPagina=50)
- **Alert-tool prices (fetched 2026-10-12):**
  - Alerta Licitação: "Alerta Individual" R$ 44.90/month (R$ 239.90 for 6 months, R$ 369.90 per year). All states, "6.441 portais e fontes oficiais", 2 alerts a day, search by state, distance, modality and items, Excel export. "Alerta Corporativo" is R$ 54.90/month — [alertalicitacao.com.br](https://alertalicitacao.com.br/)
  - LicitaJá: Essencial R$ 235, Profissional R$ 263.20, team of 5 R$ 736.96 per month — [LicitaJá planos](https://www.licitaja.com.br/planos)
  - Licitei: Plano Busca R$ 101/month ("Aviso Diário de Licitação"), Premium R$ 393, Multiempresas R$ 1,179 — [licitei.com.br](https://licitei.com.br/)
  - SIGA Pregão: Basic R$ 397/month; R$ 2,800 and R$ 6,000 packages — [sigapregao.com.br](https://www.sigapregao.com.br/)
  - Effecti claims "R$ 82 bilhões arrematados com o robô de lances em 2024" (no public price) — [effecti.com.br](https://effecti.com.br/). ConLicitação publishes no price — [conlicitacao.com.br](https://conlicitacao.com.br/)
- **Free government substitute for small suppliers (search result).** Contrata+Brasil is a federal platform for MEIs: SICAF registration is free, MEIs get WhatsApp notifications of matching opportunities, and each contract is capped at R$ 13,098.41. It has about 11k registered businesses, more than 6k opportunities and 141 eligible occupations. — [Jornal Contábil](https://jornalcontabil.com.br/noticia/contratabrasil-amplia-participacao-do-mei-com-34-novas-ocupacoes/); [Fenacon](https://fenacon.org.br/noticias/contratabrasil-facilita-e-amplia-oportunidades-para-meis-nas-contratacoes-publicas/)
- **Planned "busca ativa" (search result).** As of August 2026, the government planned active outreach to MEIs. Sebrae data: 51.6% of MEIs want to sell to government, but only 13.6% have done so. — [Movimento Econômico 2026-08-12](https://movimentoeconomico.com.br/governo/2026/08/12/governo-federal-fara-busca-ativa-de-mei-para-oferecer-oportunidades-de-trabalho/)
- **Demand (Autocomplete):**
  - "alerta de licitação" → "alerta de licitação gratuito", "alerta licitação reclame aqui", "alerta licitação é confiável"
  - "buscador de licitações" → "buscador de licitações grátis" (first)
  - Segment queries with the year: "licitação ar condicionado 2026", "licitação produtos de limpeza 2026", "licitação transporte escolar 2026", "licitação uniforme escolar 2026", "licitação para cantina escolar 2026", "licitação para mei 2026"
  - Source: [Autocomplete "alerta de licitação"](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=alerta%20de%20licita%C3%A7%C3%A3o)
- **Apify:** 65 actors match "pncp" and 85 match "licitacao", nearly all with under 40 users. — [Apify Store API "licitacao"](https://api.apify.com/v2/store?search=licitacao&limit=40)

**Querido Diário (Open Knowledge Brasil)**
- **New host.** The API moved: `queridodiario.ok.org.br/api/*` now 302-redirects to `api.queridodiario.org.br`, and the old `api.queridodiario.ok.org.br` failed the TLS handshake.
  - Coverage: `/cities` lists 5,570 territories, but only **510** have an `availability_date` (all "level 3"). The largest groups are SP 112, AL 94 and BA 66.
  - Since 2026-10-01 there are 1,924 gazettes. A full-text search for "licenca" returned 413 gazettes, and the first excerpt was a public servant's "Licença Prêmio", which is noise for business use.
  - Sources: [QD cities](https://api.queridodiario.org.br/cities); [QD gazettes](https://api.queridodiario.org.br/gazettes?querystring=licenca&published_since=2026-10-01&size=2)
- **Demand (Autocomplete):** "alerta diário oficial" → "alerta nome diario oficial", "criar alerta diario oficial", "alerta diário oficial da união"; "monitoramento diario oficial" (exact only). — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=alerta%20di%C3%A1rio%20oficial)
- **Apify:** 51 "diario oficial" actors, including DOU monitors with 24 and 10 users. — [Apify Store API](https://api.apify.com/v2/store?search=diario%20oficial&limit=40)

**Judicial and extrajudicial auctions, including Caixa properties**
- **Caixa list blocked.** Caixa's `Lista_imoveis_SP.csv` returned a "Radware Bot Manager CAPTCHA" page to curl. — [Caixa CSV](https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.csv)
- **Mapa do Leilão** claims "Mais de 44.180 pessoas usando, #1 em Busca de Leilões no Brasil", with plans at R$ 74.90/month or R$ 41.64/month billed R$ 499.70 a year (self-reported). — [mapadoleilao.com.br](https://www.mapadoleilao.com.br/)
- **Arremate 360** (portfolio, ROI and payables for arrematantes) costs R$ 99/month. — [arremate360.com.br](https://www.arremate360.com.br/)
- **Leilão Imóvel** (Cloudflare-protected), **Leilões Judiciais** and **Zuk** are free aggregators or leiloeiros. — [leilaoimovel.com.br](https://www.leilaoimovel.com.br/); [leiloesjudiciais.com.br](https://www.leiloesjudiciais.com.br/); [zuk.com.br](https://www.zuk.com.br/)
- **Apify:** 24 "leilao" actors, including Caixa scrapers (60 and 43 users). — [Apify Store API](https://api.apify.com/v2/store?search=leilao&limit=40)
- **Demand (Autocomplete):** large consumer-intent volume, for example "leilão caixa imóveis lista 2026", "imóveis caixa venda direta online", and bank-specific auctions. — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=leil%C3%A3o%20caixa)

**INPI (trademarks) and the trademark-watch market**
- **RPI portal down.** `revistas.inpi.gov.br/rpi/` and `/txt/RM29xx.zip` returned HTTP 503 with an "INPI - Página em manutenção" page on 2026-10-12. — [INPI revistas](https://revistas.inpi.gov.br/rpi/)
- **The open-data portal works.** The trademark tables were refreshed on 10/10/2026: marcas.zip 2.4 GB, dados_bibliográficos 938 MB, depositantes 855 MB, despachos 5.9 GB, plus Nice and Vienna classes. The site states "Todo o conteúdo deste site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0." — [dadosabertos.inpi.gov.br/index/marcas](https://dadosabertos.inpi.gov.br/index/marcas/); [dadosabertos.inpi.gov.br](https://dadosabertos.inpi.gov.br/)
- **The despachos table already contains RPI 2909 (2026-10-06)**, with codes such as "IPAS009 Publicação de pedido de registro para oposição". The depositantes table includes `cnpj_cpf_titular`, which means individual titulares' CPF is present. — [MARCAS_DESPACHOS.csv](https://dadosabertos.inpi.gov.br/download/marcas/MARCAS_DESPACHOS.csv); [MARCAS_DEPOSITANTES.csv](https://dadosabertos.inpi.gov.br/download/marcas/MARCAS_DEPOSITANTES.csv)
- **My full count of MARCAS_DADOS_BIBLIOGRAFICOS.csv:**
  - 6,656,335 process records.
  - Applications by filing month: 2025 total ≈ 489,516 (peak Sep 2025, 60,257); 2026 Jan–Aug ≈ 274,220 (28.5k–38.7k a month).
  - Status: 2,320,024 "Registro de marca em vigor" and 515,519 "Aguardando prazo de apresentação de oposição".
  - Source: [MARCAS_DADOS_BIBLIOGRAFICOS.csv](https://dadosabertos.inpi.gov.br/download/marcas/MARCAS_DADOS_BIBLIOGRAFICOS.csv)
- **Copyright law.** Lei 9.610 art. 8 IV excludes from copyright "os textos de tratados ou convenções, leis, decretos, regulamentos, decisões judiciais e demais atos oficiais". — [Lei 9.610/1998](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm)
- **Direct self-serve competitor: MonitoraMarca** (fetched 2026-10-12).
  - It "Colidência de marcas na RPI, toda semana", alerting by email and WhatsApp with process, titular, classes and opposition deadline. It detects identical names, contained marks, similar spelling, same pronunciation ("PHARMA e FARMA") and common roots, weighted by Nice class. It also offers a free search.
  - Plans: Essencial R$ 19.90/month or R$ 199/year (3 marks); Profissional R$ 49.90/month or R$ 499/year (25 marks); Escritório R$ 149/month or R$ 1,490/year (500 marks, 30-day trial).
  - It says it processed RPI 2909 and that "10.691 pedidos publicados para oposição na RPI nº 2909".
  - Its sitemap index lists 5 process sitemaps, and the first alone has 10,000 `/processo/…` pages, so this is programmatic SEO.
  - Sources: [monitoramarca.com.br](https://monitoramarca.com.br/); [MonitoraMarca sobre](https://monitoramarca.com.br/sobre); [MonitoraMarca sitemap](https://monitoramarca.com.br/sitemap-processos-1.xml)
- **Other competitors:**
  - LDSoft (IP-office software): "monitoramos a RPI em várias versões… validamos prazos" — [ldsoft.com.br](https://www.ldsoft.com.br/)
  - Agencies bundle monitoring: Marca Protegida ("Monitoramento processos no INPI… colidências"), Vigia Marca ("Monitoramos o andamento do pedido na RPI"), Remarca ("mais de 30.000 processos, de mais de 5.000 clientes") and Vilage — [Marca Protegida](https://www.marcaprotegida.com.br/); [Vigia Marca](https://www.vigiamarca.com.br/); [Remarca](https://www.remarca.com.br/); [Vilage](https://www.vilage.com.br/)
  - Markify (global trademark watch) — [markify.com](https://www.markify.com/)
  - Apify "Brazil Trademark Watch — INPI/RPI Monitor & Deadline Alerts", "from $150.00 / 1,000 monitor runs" — [Apify paulovitor18](https://apify.com/paulovitor18/inpi-trademark-watch)
- **Price anchor (oHub's aggregated supplier table).** "Acompanhamento do processo de registro e monitoramento da marca (anual)" runs from R$ 250/year (lowest) through R$ 672–677/year (median) to R$ 1,200/year (highest). — [oHub preços registro de marca](https://www.ohub.com.br/precos/registro-de-marca)
- **Opposition (search result).** Opposition must be filed within 60 days of RPI publication, and one source says the opposition fee rose to R$ 520. — [Âmbito Jurídico](https://ambitojuridico.com.br/como-monitorar-minha-marca-registrada/)
- **Demand (Autocomplete):** "monitoramento de marca" → "monitoramento de marca inpi"; "oposição de marca inpi" → "prazo para oposição de marca inpi", "modelo de oposição de marca inpi"; "colidência de marcas". — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=monitoramento%20de%20marca)

**Anatel, ANVISA and CVM**
- **Autocomplete is dominated by free official lookups:**
  - "consulta registro anvisa" (+ "produtos para saude", "saneantes", "empresa")
  - "afe anvisa consulta cnpj", "consulta afe anvisa diario oficial"
  - "homologação anatel consulta", "certificado anatel celular"
  - "fato relevante cvm alerta" → no suggestions
  - Source: [Autocomplete "afe anvisa consulta"](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=afe%20anvisa%20consulta)
- **Apify** lists a "CVM Fundos de Investimento" actor with 7 users. — [Apify Store API](https://api.apify.com/v2/store?search=diario%20oficial&limit=40)

### Inferences
- **No per-segment niche gap in licitações for small suppliers that a newcomer can monetise:**
  - The floor is already R$ 44.90/month for all-state, item-level search.
  - MEIs get free WhatsApp notifications from Contrata+Brasil.
  - Autocomplete is led by "grátis" and "gratuito".
  - The only visible opening is SEO capture of "licitação + segmento + 2026" queries, which is a content play with low average revenue per user, not a validated product.
- **Trademark watch is the most "TruckerDB-like" Brazilian candidate**: a weekly official publication, a 60-day deadline creating urgency, and paying buyers.
  - However, MonitoraMarca has already built the exact product (WhatsApp alerts, phonetic matching, office plan, programmatic SEO) at R$ 19.90–149, which anchors the price very low.
  - LDSoft serves the IP-office segment.
- **CNPJ lead lists, auctions and Querido Diário fall to the "saturation" or "government gives it free" patterns in the vault's [[Armadilhas e ideias mortas]].** On top of that:
  - Querido Diário's 9% municipal coverage makes "monitor every municipality" products impossible on that source alone.
  - The Caixa CAPTCHA adds pipeline fragility.
- **LGPD:**
  - CNPJ data for MEIs often includes the owner's name inside the company name, and INPI depositantes include individual CPF.
  - Marketing reuse must match the purpose of publication (art. 7 §3), which favours B2B uses tied to the registry's purpose (protecting one's own trademark, supplying government) over cold outreach to individuals.
- **INPI data licence.** CC BY-ND 3.0 on the portal versus Lei 9.610 art. 8 IV (official acts carry no copyright) suggests alert services on RPI facts are defensible. Redistributing modified INPI datasets is the grey area.

### Gaps
- Casa dos Dados, Econodata and CNPJ.biz prices were not retrieved (bot protection). Effecti and ConLicitação publish no prices.
- Not verified:
  - MonitoraMarca's revenue, launch date and traction (RDAP lookup failed).
  - Siga Sua Marca's price (domain did not resolve).
  - INPI's own weekly publication volume (only MonitoraMarca's figure of 10,691 for RPI 2909).
- The number of new CNPJs opened per month was not computed: it needs the 2.24 GB Estabelecimentos0 shard.
- Not verified:
  - Querido Diário's data licence (the /sobre page rendered no licence text).
  - Whether Caixa offers an official machine-readable feed.
- No ANPD decision on reusing CNPJ open data for marketing was found this round.

## Key question 3: Which candidates pass gates G1–G8? Full record per candidate, gate verdicts and 1–5 scores

### Takeaway
**No candidate is APPROVED.**
- **KILL** (saturation, legal exposure, or the government gives it free):
  - FMCSA new-carrier feed, INPI trademark watch, PNCP licitação alerts, CNPJ new-company lists, auctions and Caixa, Querido Diário monitoring.
  - US probate, eviction and divorce, pre-foreclosure and tax liens, UCC, building permits, new LLCs, SAM.gov/USAspending, FAA, and Anatel/ANVISA/CVM.
- **Survive as CONDITIONAL:**
  - **NPPES weekly "new practices" feed for medical-billing and credentialing firms** (gap: no proof anyone pays).
  - **New restaurant and liquor-licence openings feed** (gap: fragmented data with no contact fields, and weak search demand).
  - **PNCP contract winners for seguro-garantia brokers** (gap: no proof of willingness to pay and no searchable demand from brokers).
  - Each has a cheap test with pass/fail thresholds below.

### Cited Findings

**Platform and payment facts that affect G7 for every lead or data product**
- **Paddle** (the vault's planned merchant of record for foreign sales) prohibits "Advertising and marketing… Telemarketing… Mass Marketing Products, including but not limited to SMS marketing and Message App marketing", plus "Any product or service that enables unauthorized access to data belonging to another party". — [Paddle: what am I not allowed to sell](https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle)
- **Stripe's list** (updated 2026-09-22) includes "Telemarketing" among its unfair or predatory practices. — [Stripe restricted businesses](https://stripe.com/legal/restricted-businesses)
- **TruckingLists sells FMCSA lead packs with "Secure checkout by Creem"**, so at least one merchant of record accepted this product type as of 2026-10-12. — [truckinglists.com/pricing](https://truckinglists.com/pricing)
- **Paddle supports Brazil-based sellers** (5% + 50¢). Stripe Managed Payments is unavailable to companies in Brazil. Polar does not pay out to Brazil. — vault note [[Pagamentos e impostos]], citing [Paddle pricing](https://www.paddle.com/pricing) and [Stripe eligibility](https://docs.stripe.com/payments/managed-payments/eligibility)

**C1. FMCSA new-carrier and insurance-alert feed (US)**
- **Product:** a daily email or CSV of new USDOT and MC registrants, filtered by state and operation, plus insurance-cancellation and authority-change alerts.
- **Buyer and pool:** trucking insurance agents, factoring firms, dispatchers and compliance vendors. Supply side: about 14.6–17.5k new registrations a month in 2026 ([DOT API](https://data.transportation.gov/resource/az4n-8mr2.json)). The number of buyers was not found.
- **Pain:** "getting in front of them — with the right contact information — is a grind" — [truckerdb.com](https://www.truckerdb.com/)
- **Competitors:** at least 8 SaaS plus 67 Apify actors (Key question 1). Prices run US$29–249/month. The only verified revenue is TruckerDB's US$1,580 MRR from 20 subscriptions — [TrustMRR](https://trustmrr.com/startup/truckerdb)
- **Weaknesses:** raw lists and similar features across sellers. Differentiation now means X-date and insurance alerts, which TruckerDB Pro, Carrier Signal and Truckr already claim.
- **Demand:** "new mc authority list", "fmcsa new authority list (pdf)", "trucking leads for sale", "buy trucking leads" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=new%20authority%20list)
- **Channel:** SEO plus a free sample (TruckerDB's model).
- **Build:** about 1 week.
- **Time to first revenue:** 4–10 weeks.
- **Risks:** Motus data changes; Paddle's telemarketing ban; churn; price war.
- **Gates:**
  - G1 PASS
  - G2 **FAIL** (8+ SaaS, 4+ launched in 2026)
  - G3 PASS
  - G4 PASS (autocomplete), but the SERP is contested
  - G5 PASS
  - G6 PASS
  - G7 CONDITIONAL (merchant of record must accept lead lists; Creem precedent)
  - G8 FAIL under realistic share (51–102 subscriptions needed at US$49–99)
- **Verdict: KILL.**

**C2. NPPES weekly "new practices" feed for medical-billing, credentialing and RCM firms (US)**
- **Product:** every Monday, the new Type-2 organisations (and optionally Type-1 providers), filtered by state and taxonomy, with phone and address, a CSV, and a CRM webhook.
- **Buyer and pool:** medical-billing and credentialing companies, malpractice brokers and EHR resellers. Supply side: 2,763 new organisations and 10,036 individuals in one week ([NPPES weekly](https://download.cms.gov/nppes/NPPES_Data_Dissemination_100526_101126_Weekly_V2.zip)). The number of buyers is a gap.
- **Pain proxy:** "medical billing leads", "buy medical billing leads", "medical billing leads list" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=medical%20billing%20leads)
- **Competitors:**
  - Apify weekly editions at US$9 per state or US$29 nationwide — [Apify](https://apify.com/fixmyerrorcode/newly-enumerated-us-healthcare-organizations-weekly-npi-feed)
  - 213 NPI actors with at most 130 users each — [Apify Store API](https://api.apify.com/v2/store?search=npi&limit=40)
  - No dedicated SaaS found (search result)
  - No verified revenue anywhere.
- **Weakness of the incumbents:** raw-data tools aimed at developers.
- **Channel:** SEO pages per state and specialty, plus a Google Ads test on "buy medical billing leads".
- **Build:** about 1 week (6.7 MB weekly zip).
- **Time to first revenue:** 3–8 weeks.
- **Risks:**
  - Enumeration does not mean an operating practice, which the Apify seller itself warns about.
  - No emails in the data.
  - Paddle's telemarketing clause.
- **Gates:**
  - G1 **UNPROVEN**
  - G2 PASS
  - G3 PASS
  - G4 PARTIAL
  - G5 PASS
  - G6 PASS
  - G7 PASS: the data is FOIA-disclosable at no charge ([CMS](https://www.cms.gov/regulations-and-guidance/administrative-simplification/nationalprovidentstand/datadissemination)), but the merchant of record must accept it
  - G8 plausible: 51–102 subscriptions at US$49–99
- **Verdict: CONDITIONAL.**

**C3. New restaurant and liquor-licence openings feed (US: NY pending SLA, TX TABC, Chicago, then other states)**
- **Product:** a weekly pre-opening list of restaurants and bars (pending liquor licences, new food licences), filtered by metro.
- **Buyers:** merchant-services and POS agents, beverage and food distributors, insurance, linen and pest control.
- **Pain:** vendors pay US$200–999/month today (Open Soon, Starfleet, CSVFirst; self-reported, Key question 1).
- **Data:**
  - NY: about 400 pending applications a month (129 restaurants in September).
  - TX: about 800–900 new issues a month.
  - Chicago: 61 retail-food licences a month.
  - No phone or email in NY or TX ([data.ny.gov](https://data.ny.gov/resource/f8i8-k2gm.json); [data.texas.gov](https://data.texas.gov/resource/7hf9-qc9f.json)).
- **Demand:** "merchant services leads", "buy merchant services leads", "pending liquor license ny"; "liquor license leads" → none — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=merchant%20services%20leads)
- **Build:** 3–5 states in about 3–4 weeks; each state is its own parser.
- **Time to first revenue:** 6–12 weeks.
- **Risks:** low volume per state, no contacts, enrichment cost and ToS.
- **Gates:**
  - G1 PARTIAL (self-reported prices only)
  - G2 PASS
  - G3 PASS
  - G4 WEAK
  - G5 BORDERLINE
  - G6 PASS
  - G7 PASS
  - G8 plausible at US$99–199 × 25–50 subscriptions
- **Verdict: CONDITIONAL.**

**C4. INPI trademark-collision watch (BR)**
- **Product:** weekly RPI matching for phonetic and spelling similarity by Nice class, with the opposition deadline.
- **Buyer and pool:** 2.32M marks in force; about 34k applications a month in 2026 ([INPI open data](https://dadosabertos.inpi.gov.br/download/marcas/MARCAS_DADOS_BIBLIOGRAFICOS.csv)); IP agencies.
- **Pain:** the 60-day opposition window. "O INPI não avisa os titulares de marcas parecidas" — [MonitoraMarca sobre](https://monitoramarca.com.br/sobre)
- **Competitors:** MonitoraMarca R$ 19.90/49.90/149 (identical feature set); LDSoft; agencies at R$ 250–1,200/year ([oHub](https://www.ohub.com.br/precos/registro-de-marca)); Apify; Markify.
- **Demand:** "monitoramento de marca inpi", "prazo para oposição de marca inpi" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=monitoramento%20de%20marca)
- **Build:** 2–3 weeks.
- **Risks:**
  - The RPI portal was in maintenance (503) on 2026-10-12.
  - The CC BY-ND licence.
  - CPF fields under the LGPD.
- **Gates:**
  - G1 PASS (agencies charge for it)
  - G2 **FAIL** (a same-shape, cheaper, SEO-built incumbent)
  - G3 PARTIAL (SMEs)
  - G4 PASS
  - G5 PASS
  - G6 PASS
  - G7 PASS (BRL via Asaas or Mercado Pago)
  - G8 **FAIL**: US$5k = R$ 27,000 needs about 181 office plans at R$ 149 or about 1,357 subscriptions at R$ 19.90, against a price anchor already set by MonitoraMarca
- **Verdict: KILL**, unless new evidence shows MonitoraMarca failing or a segment it ignores, such as figurative and logo marks, which would drift toward AI-core.

**C5. PNCP per-segment licitação alerts (BR)**
- **Data:** PASS. 7,904 pregões and 14,050 dispensas a week ([PNCP](https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao?dataInicial=20261005&dataFinal=20261009&codigoModalidadeContratacao=6&pagina=1&tamanhoPagina=10)).
- **Competitors:** Alerta Licitação R$ 44.90, Licitei R$ 101, LicitaJá R$ 235, SIGA R$ 397, Effecti, ConLicitação, plus free Contrata+Brasil.
- **Demand:** "alerta de licitação gratuito" and "buscador de licitações grátis".
- **Gates:**
  - G1 PASS
  - G2 FAIL
  - G3 PARTIAL
  - G4 PASS (with free intent)
  - G5 PASS
  - G6 PASS
  - G7 PASS
  - G8 FAIL (about 600 subscriptions at R$ 44.90 for US$5k)
- **Verdict: KILL.**

**C6. PNCP contract winners for seguro-garantia brokers and receivables lenders (BR)**
- **Data:** PASS. 41,030 contracts a week, with supplier CNPJ, value and term ([PNCP contratos](https://pncp.gov.br/api/consulta/v1/contratos?dataInicial=20261005&dataFinal=20261009&pagina=1&tamanhoPagina=50)).
- **Demand from buyers:** "leads seguro garantia" → none; "corretor seguro garantia" (exact only); end-customer queries such as "seguro garantia licitação lei 14133" exist — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=seguro%20garantia%20licita%C3%A7%C3%A3o)
- **Competitors:** none found, but no evidence of willingness to pay either.
- **Gates:**
  - G1 **UNPROVEN**
  - G2 PASS
  - G3 PASS
  - G4 FAIL (no searchable buyer demand)
  - G5 PASS
  - G6 PASS
  - G7 PASS (company data; MEIs carry an LGPD caveat)
  - G8 unknown
- **Verdict: CONDITIONAL (weak).**

**C7–C19. Killed quickly** (evidence in Key questions 1–2)

| # | Candidate | Main failing gate(s) | Decisive evidence |
|---|---|---|---|
| C7 | CNPJ new-company lists (BR) | G2, G4 (demand for free lists), G7 (LGPD art. 7 §3) | Speedio R$ 719+, EmpresAqui from R$ 139.90, 194 Apify actors, "grátis" first in autocomplete |
| C8 | Auctions and Caixa aggregator (BR) | G2, G5 (Caixa CAPTCHA) | Mapa do Leilão: 44,180 users, R$ 74.90; Radware block |
| C9 | Querido Diário monitoring (BR) | G5 (data coverage), G3 (name alerts are B2C) | 510 of 5,570 municipalities |
| C10 | Anatel / ANVISA / CVM alerts (BR) | G1, G4 | Queries are free official lookups; no CVM alert suggestions |
| C11 | Probate leads (US) | G5 (county-by-county access, paid portals, court approval), G2 | b2bsaas US$70k MRR after 16 years; Realeflow; county fees |
| C12 | Eviction leads (US) | G7 (FCRA if used for screening) | 15 U.S.C. §1681a |
| C13 | Divorce leads (US) | G4, G7 (reputational) | Autocomplete is mostly memes |
| C14 | Pre-foreclosure and tax liens (US) | G2 | PropStream US$99/month; 199 Apify actors |
| C15 | UCC / MCA leads (US) | G2, G7 (MCA reputation, merchant-of-record risk) | US$0.02–0.75 per lead; "resold at least 30 times" |
| C16 | Building permits (US) | G2, G5 (city-by-city) | 578 Apify actors; enterprise incumbents |
| C17 | New LLC filings (US) | G2, G5 (states sell or gate data) | 276 Apify actors; TX US$20/week subscription |
| C18 | SAM.gov / USAspending (US) | G2, G5 (POC contacts are FOUO) | 204 Apify actors; SAM public tier lacks email and phone |
| C19 | FAA aircraft registrations (US) | G1, G4 | 33 Apify actors with 6 users or fewer; no lead-intent autocomplete |

### Inferences

**Scores (1 = worst, 5 = best).** These are my estimates from the evidence above. Criteria: WTP = willingness-to-pay evidence; Sat. = low saturation; Power = buyer purchasing power; Dist. = distribution without contacts; Build = buildability; Speed = speed to first revenue; Risk = low risk.

| # | Candidate | WTP | Sat. | Power | Dist. | Build | Speed | Risk | Total /35 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | FMCSA new-carrier feed | 5 | 1 | 4 | 3 | 5 | 3 | 2 | 23 | KILL |
| C2 | NPPES new practices feed | 2 | 4 | 4 | 3 | 5 | 2 | 3 | 23 | CONDITIONAL |
| C4 | INPI trademark watch | 3 | 2 | 3 | 3 | 4 | 3 | 3 | 21 | KILL |
| C5 | PNCP per-segment alerts | 4 | 1 | 3 | 3 | 4 | 3 | 3 | 21 | KILL |
| C3 | Restaurant / liquor openings | 3 | 4 | 4 | 2 | 2 | 2 | 3 | 20 | CONDITIONAL |
| C18 | SAM.gov / USAspending | 4 | 1 | 4 | 2 | 4 | 2 | 3 | 20 | KILL |
| C19 | FAA registrations | 2 | 4 | 4 | 1 | 4 | 2 | 3 | 20 | KILL |
| C6 | PNCP winners → seguro garantia | 1 | 4 | 4 | 1 | 4 | 2 | 3 | 19 | CONDITIONAL (weak) |
| C11 | Probate | 5 | 2 | 4 | 4 | 1 | 1 | 2 | 19 | KILL |
| C16 | Building permits | 4 | 1 | 4 | 3 | 2 | 2 | 3 | 19 | KILL |
| C7 | CNPJ new companies | 4 | 1 | 3 | 2 | 3 | 3 | 2 | 18 | KILL |
| C14 | Pre-foreclosure / liens | 5 | 1 | 4 | 3 | 1 | 2 | 2 | 18 | KILL |
| C15 | UCC | 4 | 1 | 3 | 3 | 2 | 3 | 1 | 17 | KILL |
| C17 | New LLC filings | 3 | 1 | 3 | 2 | 2 | 3 | 3 | 17 | KILL |
| C9 | Querido Diário monitoring | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 17 | KILL |
| C10 | Anatel / ANVISA / CVM | 1 | 3 | 3 | 2 | 3 | 2 | 3 | 17 | KILL |
| C8 | Auctions / Caixa | 3 | 1 | 3 | 3 | 2 | 2 | 2 | 16 | KILL |
| C12 | Evictions | 3 | 2 | 3 | 2 | 1 | 1 | 1 | 13 | KILL |
| C13 | Divorce | 2 | 3 | 3 | 1 | 1 | 1 | 1 | 12 | KILL |

**Cheapest real-world tests for the CONDITIONALs**
- **C2 (NPPES):** a landing page with a free sample of last week's new organisations in one state, a US$49/month Pro tier, and US$50 of Google Ads on "buy medical billing leads", "medical billing leads list" and "credentialing leads".
  - **Pass:** at least 2 paid sign-ups, or at least 15 sample downloads at a cost per lead under US$4, within 14 days.
  - **Fail:** zero paid sign-ups and fewer than 5 sample downloads.
- **C3 (restaurant / liquor):** a free weekly "NYC + Texas pending/new liquor licences" email (data is ready on the NY and TX portals), with a US$99/month upgrade for CSV and filters. Promote it via 40 hand-written cold emails to merchant-services ISOs found on public directories (allowed under CAN-SPAM with opt-out and physical address).
  - **Pass:** at least 10 free subscribers and at least 1 paid within 21 days.
  - **Fail:** fewer than 3 free subscribers.
- **C6 (PNCP winners):** email 30 publicly listed seguro-garantia brokers a free CSV of last week's contracts above R$ 500k in their state.
  - **Pass:** at least 3 replies asking for more and at least 1 who will pay R$ 199/month.
  - **Fail:** no paid intent.

**Patterns**
- **Raw public-records lead lists are a strong pattern in principle** (b2bsaas, TruckerDB, Harper, Subbasta are all verified). But in 2026 every attractive US dataset has a long tail of Apify sellers and 2–10 SaaS wrappers. The survivors are datasets where:
  - (a) contacts are missing, so incumbents ignore them (NPPES organisations, liquor licences), or
  - (b) the signal is derived from several registers (Harper's model).
- **For the client's constraints (no contacts, about US$130), the FMCSA plan in the vault ("plan C") should be downgraded to KILL.** NPPES (C2) is the best replacement test because the pipeline is a 7 MB weekly file and the ad test fits the budget.

### Gaps
- No search-volume or cost-per-click data, so the Google Ads test thresholds are judgement calls.
- No verified revenue exists for any US competitor except TruckerDB and b2bsaas, or for any Brazilian competitor in these categories (no Brazilian public-records products were found on TrustMRR this round).
- Not verified:
  - Whether Creem or Paddle would accept a Brazil-based lead-list seller (Paddle's text bans telemarketing and mass-marketing products, but not data feeds explicitly).
  - Buyer-pool counts: US medical-billing firms, merchant-services ISOs, Brazilian IP agencies, seguro-garantia brokers.

## Key question 4: Deep validation of the top 3 (demand via Autocomplete, competitor census, data-pipeline test, pricing and unit economics)

### Takeaway
I deep-validated the three candidates with the strongest pre-validation case, using each dataset's real API or file:
1. **FMCSA new-carrier feed (US).** The pipeline works (about 100% email and phone coverage, daily updates). Demand exists. The census finds at least 8 SaaS sellers and 67 Apify actors. → **KILL**.
2. **INPI trademark watch (BR).** The pipeline works through INPI open data (RPI 2909 included). Demand exists. A same-shape incumbent, MonitoraMarca, charges R$ 19.90–149. → **KILL**.
3. **PNCP licitação alerts (BR).** The pipeline works (about 28k notices a week). Demand is "grátis"-led. The market has paid tools from R$ 44.90 plus a free government channel. → **KILL**.

The NPPES feed got the same pipeline, autocomplete and census checks and is the best surviving **CONDITIONAL**.

### Cited Findings

**Deep validation 1: FMCSA**
- **Pipeline:**
  - SoQL queries on az4n-8mr2 return new registrations by `add_date` (text YYYYMMDD) with phone, email, officer and fleet fields. In September 2026, 14,655 of 14,656 had an email.
  - The dataset updated 2026-10-12 and the latest `add_date` is 20261011.
  - Source: [DOT API](https://data.transportation.gov/resource/az4n-8mr2.json)
  - Insurance and authority-history datasets are updated daily — [Socrata catalog](https://api.us.socrata.com/api/catalog/v1?search_context=data.transportation.gov&domains=data.transportation.gov&q=FMCSA&limit=40)
- **Demand:** "fmcsa new authority list", "new mc authority list pdf", "buy trucking leads", "trucking leads for sale" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=trucking%20leads)
- **Census:**
  - SaaS: TruckerDB (US$49 / Pro), TruckingLists (US$29–199), Carrier Signal (US$79–249), DOT Leads, RigDig, Truckr, Carrier Network, truckingleads.com.
  - Apify: 67 actors.
  - Sources: [TruckerDB](https://www.truckerdb.com/); [TruckingLists](https://truckinglists.com/pricing); [Carrier Signal](https://newauthorityleads.com/); [Apify Store API](https://api.apify.com/v2/store?search=fmcsa&limit=40)
- **Verified revenue:** US$1,580 MRR from 20 subscriptions, after about 6 months, with 192 visits a month — [TrustMRR TruckerDB](https://trustmrr.com/startup/truckerdb) (round-1 traffic figure from the same page)

**Deep validation 2: INPI trademark watch**
- **Pipeline:**
  - The RPI portal returned 503 "manutenção" — [revistas.inpi.gov.br](https://revistas.inpi.gov.br/rpi/)
  - The open-data CSVs are refreshed weekly (10/10/2026) and contain RPI 2909 despachos — [dadosabertos.inpi.gov.br](https://dadosabertos.inpi.gov.br/index/marcas/)
  - Range requests and streaming work; the 938 MB bibliographic file was processed in full.
- **Demand:** "monitoramento de marca inpi", "prazo para oposição de marca inpi", "modelo de oposição de marca inpi" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=oposi%C3%A7%C3%A3o%20de%20marca%20inpi)
- **Census:** MonitoraMarca (R$ 19.90 / 49.90 / 149; WhatsApp; 500-mark office plan; programmatic SEO), LDSoft, agencies (R$ 250–1,200/year), Apify actor, Markify — [MonitoraMarca](https://monitoramarca.com.br/); [oHub](https://www.ohub.com.br/precos/registro-de-marca); [LDSoft](https://www.ldsoft.com.br/); [Apify](https://apify.com/paulovitor18/inpi-trademark-watch)
- **Scale:** about 10,691 applications published for opposition per weekly RPI (MonitoraMarca's figure); 2.32M marks in force (my count) — [MonitoraMarca](https://monitoramarca.com.br/); [INPI CSV](https://dadosabertos.inpi.gov.br/download/marcas/MARCAS_DADOS_BIBLIOGRAFICOS.csv)

**Deep validation 3: PNCP licitação alerts**
- **Pipeline:** the open consultation API requires no key and responded from outside Brazil. One week (5–9 October 2026) held 7,904 pregões, 1,218 concorrências, 14,050 dispensas and 5,150 inexigibilidades. The item-level endpoint timed out once at 60 s. — [PNCP API](https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao?dataInicial=20261005&dataFinal=20261009&codigoModalidadeContratacao=6&pagina=1&tamanhoPagina=10)
- **Demand:** "alerta de licitação gratuito", "buscador de licitações grátis", segment+year queries — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt&gl=br&q=buscador%20de%20licita%C3%A7%C3%B5es)
- **Census:** Alerta Licitação (R$ 44.90 / 54.90; 6,441 portals), Licitei (R$ 101+), LicitaJá (R$ 235+), SIGA Pregão (R$ 397+), Effecti, ConLicitação, Apify (85 actors), Contrata+Brasil (free) — [Alerta Licitação](https://alertalicitacao.com.br/); [Licitei](https://licitei.com.br/); [LicitaJá](https://www.licitaja.com.br/planos); [SIGA](https://www.sigapregao.com.br/); [Jornal Contábil](https://jornalcontabil.com.br/noticia/contratabrasil-amplia-participacao-do-mei-com-34-novas-ocupacoes/)

**Runner-up check: NPPES**
- **Pipeline:** the weekly V.2 zip (6.7 MB) downloaded and parsed. It held 2,763 new organisations and 10,036 new individuals for 5–11 October 2026, with practice phone and no email. — [NPPES weekly](https://download.cms.gov/nppes/NPPES_Data_Dissemination_100526_101126_Weekly_V2.zip)
- **Census:** Apify only (US$9–29 per edition; 213 actors); no SaaS found. — [Apify](https://apify.com/fixmyerrorcode/newly-enumerated-us-healthcare-organizations-weekly-npi-feed)

### Inferences

**Unit economics** (at R$ 5.40 per US$; payment fees from the vault: Paddle 5% + 50¢, Asaas about 4%)

| Candidate | Price point (anchor) | Customers for US$5k/month | Data and infra cost | Realistic share vs pool | Margin |
|---|---|---|---|---|---|
| FMCSA feed | US$49–99 (TruckerDB, TruckingLists) | 51–102 | Free data; about US$20–40/month VPS and email (estimate) | TruckerDB, the earliest SEO entrant, has 20 after 6 months; a 2027 entrant against 8+ SaaS likely gets fewer | High per sale, but not reachable |
| INPI watch | R$ 19.90–149 (MonitoraMarca) | 181 office plans or about 1,357 SME plans | Free data; 2.4–5.9 GB weekly ingestion | The IP-agency pool is unknown; prices are anchored by an incumbent | High, but low ARPU |
| PNCP alerts | R$ 44.90–235 | 115–601 | Free API; heavy polling | Competing with 6+ paid tools and a free government channel | Low ARPU |
| NPPES (conditional) | US$49–99 (no anchor; Apify US$29 per edition) | 51–102 | Free 7 MB weekly file | Unknown buyer pool (gap) | High if willingness to pay exists |

- **Recommendation for the vault:**
  - Mark [[Feed de transportadoras recém-registradas (FMCSA)]] **KILL** (saturation; Motus data risk; Paddle telemarketing clause).
  - Add INPI watch, PNCP alerts, CNPJ lists, auctions and Querido Diário to [[Armadilhas e ideias mortas]] under "Padrão – saturação" or "Padrão – governo entrega de graça".
  - Keep NPPES new practices (C2) and restaurant / liquor openings (C3) as CONDITIONAL, with the tests in Key question 3.
- **Adversarial note:** even the CONDITIONALs fail G1 on current evidence. No one with verified revenue sells exactly these feeds. Treat the US$50 ad test as the gate, not the build.

### Gaps
- Not verified for MonitoraMarca, TruckingLists or Carrier Signal: revenue, subscriber counts and launch dates. A newcomer-wins test (G2) therefore relies on TruckerDB alone.
- No CPC or volume data to size the Google Ads tests.
- The PNCP item endpoint was too slow to test item-level (per-product) alert matching.
