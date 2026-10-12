# First customers, MRR economics, cheap validation, and payment/tax setup for a Brazilian solo software founder (no audience, ~R$700 / US$130 budget)

Compiled 2026-10-12. Reliability tags used below: **[P]** = primary page fetched and read in this session; **[S]** = only a search-engine summary of the page was available (page blocked by Cloudflare/Vercel/DNS, or the shared web-search budget ran out), so treat it as directional; **[V]** = vendor or marketing source with a commercial interest; **[A]** = single-founder anecdote (prone to survivorship bias). Live pricing pages were fetched on 2026-10-12. Currency conversions use the client's implied rate of about R$5.4 per US$ (R$700 ≈ US$130). This is not a market quote.

## 1. Funnel conversion benchmarks that apply across channels (visitor→signup/trial, trial→paid, freemium→paid)

### Takeaway
In 2023–2026 benchmark sets, a self-serve B2B tool typically gets about 3.5–9% of website visitors to sign up. The median is about 8% of signups paying within six months: 3–5% counts as "good" for freemium, 4–6% for trials with no card, and 25–35% for card-required trials. Card-required trials produce the most paying customers per 1,000 visitors (about 10.5, vs 3.6–5.6 for the other models). Organic, referral, social and LLM traffic converts better than paid traffic. These benchmarks come from companies that already have product-market fit, so a brand-new product should plan around bottom-quartile numbers.

### Cited Findings
- **ChartMogul × ProductLed × Growth Unhinged, "The Conversion Report" (survey January 2026, published 2026-02-04; 200 B2B software products; the typical respondent has US$1–10M ARR and an ARPA of US$50–249/month, so the sample skews to established companies) [P].** The median free-to-paid rate within 6 months is 8%, with a 10x gap between the top and bottom 20%. 57% of products lead with a free trial vs 26% with freemium. 14-day trials are the most common (62%). 20% of trial products require a card. — [ChartMogul](https://chartmogul.com/reports/saas-conversion-report/)
- Same report, "good/great" free-to-paid rates: freemium 3–5% / 8–12%; ungated freemium (usable before signup) "good" 7–9%; free trial 4–6% / 10–15%; card-required trial 25–35% / 50–60%. Card-required trials convert at about 30%, more than 5x trials without a card. AI and AI-hybrid products: good 6–8%, great 15–20%. — [ChartMogul](https://chartmogul.com/reports/saas-conversion-report/)
- Same report, results per 1,000 website visitors: freemium gives 90 signups (9%) and 5 paying customers; free trial 45 signups and 3.6 paying; ungated freemium 70 signups and 5.6 paying; card-required trial 35 signups and 10.5 paying. — [ChartMogul](https://chartmogul.com/reports/saas-conversion-report/)
- Same report, distribution for trial products: 20% convert below 2.5%, 30% convert at 2.5–7.5%, and 23% convert above 25%. For freemium: 25% below 2.5%, 29% at 2.5–7.5%, and 25% at 10–15%. — [ChartMogul](https://chartmogul.com/reports/saas-conversion-report/)
- **ChartMogul follow-up report (published 2026-03-18, same dataset) [P].** "Organic signups from search, referral traffic, social media, and LLMs convert at the highest rates… Signups from paid marketing (ex: paid search, display, Meta ads) convert at the lowest rates." At Webflow, ChatGPT traffic converts at 24%, 6x Google. A 1 percentage-point gain in free-to-paid adds roughly 15% new revenue per trial. 43% of participants improved conversion in the last 12 months, usually by 10–25%. — [ChartMogul part 2](https://chartmogul.com/reports/saas-conversion-report-2/)
- **First Page Sage (updated 2025-09-05; data from the agency's own 86 SaaS clients, 71% B2B, Q1 2022–Q3 2025) [V].**

  | Step | Organic | Paid |
  |---|---|---|
  | Visitor → opt-in trial (no card) | 8.5% | 7.1% |
  | Opt-in trial → paid | 18.2% | 17.4% |
  | Visitor → opt-out trial (card required) | 2.5% | 2.2% |
  | Opt-out trial → paid (one paid month counts) | 48.8% | 51% |
  | Visitor → freemium | 13.3% | 15.9% |
  | Freemium → paid | 2.6% | 2.8% |

  By industry, visitor→trial ranges from 5.5% (Enterprise) to 12.6% (IoT), and trial→paid from 18.6% to 29.0% (CRM). — [First Page Sage](https://firstpagesage.com/seo-blog/saas-free-trial-conversion-rate-benchmarks/)
- First Page Sage's numbers are much higher than ChartMogul's. Userpilot attributes the gap to First Page Sage analyzing only its own clients' data [S]. — [Userpilot](https://userpilot.com/blog/free-trial-conversion-rate/)
- **Lenny's Newsletter with OpenView and Pendo (2023-08-01; 1,000+ products, mostly B2B SaaS) [P, partial excerpt before the paywall].** Freemium self-serve: good 3–5%, great 6–8%. Freemium with sales assist: good 5–7%, great 10–15%. Free trial: good 8–12%, great 15–25%. Signup rate is 5% for trial products vs 9% for freemium. 44% of free-trial companies have sales reach out to more than half of signups. — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/what-is-a-good-free-to-paid-conversion)
- **MicroConf State of Independent SaaS 2024 (about 700 mostly bootstrapped SaaS; key takeaways discussed in podcast episode 721) [P, transcript].**
  - 71% of bootstrapped SaaS require a card for trials; across the four surveys from 2020 to 2024 the share went 73% → 78% → 78% → 71%.
  - Card-required trials showed the highest average month-over-month growth (about 14%).
  - Trials without a card were associated with about 2x LTV.
  - Products targeting small businesses averaged about 12% month-over-month growth, vs about 5% for consumer products.
  - Asia Orangio advised very early, first-time founders to require the card as "a really good litmus test", and to consider removing it after 10–50 paying customers.

  — [Startups for the Rest of Us ep. 721](https://www.startupsfortherestofus.com/episodes/episode-721-7-key-takeaways-from-the-2024-state-of-independent-saas-report)
- **Unbounce 2024 Conversion Benchmark Report (57M+ conversions, 41k+ landing pages) [V].** The median landing-page conversion rate across industries is 6.6%, and industry medians range from 3.8% to 12.3%. Average conversion by traffic source: email 19.3%, paid social 12%, paid search 10.9%. — [Unbounce](https://unbounce.com/conversion-benchmark-report/)

### Inferences
- A planning model for a new SMB tool with no card required: 1,000 targeted visitors give about 45–90 signups and about 3–6 paying customers, or about 10 with a card-required trial. At US$20 ARPA, 1,000 visitors are worth roughly US$60–200 of new MRR. Reaching US$1k MRR from cold web traffic therefore needs on the order of 5,000–15,000 targeted visitors. Very high-intent sources (marketplace search, 1:1 conversations) need far fewer.
- The benchmark companies already have product-market fit (ChartMogul's typical respondent has US$1–10M ARR). A first-time founder's new product should assume bottom-quartile rates (≤2.5% free-to-paid) until its own data says otherwise.
- With a tiny budget, a card-required trial (or a paid pilot) is the cheapest way to separate real buyers from curious visitors. This matches the MicroConf discussion and ChartMogul's data showing about 10.5 payers per 1,000 visitors vs about 5.

### Gaps
- No conversion benchmark specific to Brazilian SMB buyers, Pix-paid trials, or Portuguese-language products was found.
- The SaaS-specific Unbounce median could not be read; it sits in a chart image.
- No benchmark ties visitor→paid rates to individual acquisition channels such as Reddit, WhatsApp or YouTube.

## 2. Channel benchmarks for a brand-new product with no audience (time to first customer, cost, conversion)

### Takeaway
No source publishes a rigorous "median time to first customer by channel." What does exist is cost data and harsh base rates:
- The median Chrome extension has 18 users.
- Only 1.74–6.11% of new web pages reach Google's top 10 within a year.
- A Product Hunt launch typically brings 100–2,000 visitors.
- The average cold-email reply rate is about 3.4% and falling.

Channels with built-in intent (marketplace search, high-intent search, 1:1 conversations) can produce a first customer within days or weeks. SEO takes 6–12+ months and AI Overviews have structurally weakened it. Paid social and paid search are affordable as tests in Brazil, but paid signups convert worst.

### Cited Findings

#### Marketplaces and app stores (Shopify, Chrome, WordPress, Nuvemshop)
- **Shopify (changelog, 2025-04-24) [P].** The store has more than 16,000 apps, and Shopify paid more than US$1B to developers in 2024. The revenue-share exemption now covers the first US$1M of lifetime revenue (counting from 2025-01-01) instead of resetting every year; above that, Shopify takes 15%. — [Shopify changelog](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share)
- **Shopify docs (accessed 2026-10-12) [P].** App Store registration is a one-time US$19 fee per Partner account. All app billing carries a 2.9% processing fee plus applicable sales tax. Developers with US$20M+ annual app revenue pay 15% on everything. — [Shopify dev docs](https://shopify.dev/docs/apps/launch/distribution/revenue-share)
- **Indie Hackers anecdote (undated post) [S][A].** A solo Shopify app got its first subscriber on day one and had about 35 paying merchants (>US$4K ARR) roughly 3 months after launch "with very little marketing." Approval took nearly a dozen submissions. — [Indie Hackers](https://www.indiehackers.com/post/building-a-shopify-app-for-my-wife-d412e8b123)
- **Chrome Web Store base rates (Exstats Q1 2026 report using March 2026 store data, via a Konabayev data review published 2026-05-13, updated 2026-08-04) [P of the secondary review].**
  - 178,299 active Chrome extensions.
  - 70.4% have 100 users or fewer, and the median extension has 18 users.
  - Only 2.63% have more than 10,000 users.
  - 49.8% of listings have at least one rating.
  - Chrome listings grew 22.7% year over year.

  — [Konabayev (Exstats data)](https://konabayev.com/blog/extension-monetization-statistics-2026/)
- The Chrome Web Store requires a one-time developer registration fee before publishing; the fetched page did not state the amount. — [Chrome for Developers](https://developer.chrome.com/docs/webstore/register)
- **DEV Community anecdote (published 2026-05-06) [A].** Five freemium Chrome extensions monetized with ExtensionPay reached 0.8% overall free-to-paid; the best was 1.4% and the worst 0.3%. Rewriting the upgrade prompt raised prompt→upgrade from 2% to 8%. The author argues 0.5–2% is realistic for extensions and cites trust problems with an unfamiliar third-party checkout domain. Price points were US$2.99–9.99/month plus one US$3.99 one-time product. — [DEV Community](https://dev.to/_350df62777eb55e1/real-numbers-freemium-chrome-extension-monetization-after-6-months-5hga)
- **WordPress plugins (Freemius blog) [S][V].** Most products using Freemius reach 1–2% free-to-paid, and the top performers about 5%. — [Freemius](https://freemius.com/blog/increase-freemium-upgrades-wordpress-plugin-theme/)
- **Nuvemshop app store (help center, updated 2026-01-15) [P].**
  - Apps can be free, one-time or monthly, with an optional free trial.
  - Billing works one of two ways: (a) the partner bills the merchant directly (the app is listed as free "with in-app sales"), or (b) Nuvemshop bills the merchant and the partner withdraws through the partner portal, net of the merchant's payment-method fees and the invoice tax.
  - After a trial ends, Nuvemshop does not charge automatically. The merchant pays manually unless they turn on automatic billing.
  - Only registered Nuvemshop Partners can create apps.

  — [Nuvemshop](https://atendimento.nuvemshop.com.br/pt_BR/parceiros-tecnologicos/como-eu-recebo-pelo-uso-do-meu-aplicativo-criado-na-nuvemshop)
- **Nuvemshop partner guide (2025-07-02) [S].** App partners are paid through app subscription fees, not commission. (The 2026 help page's intro mentions "desconto da comissão da plataforma," which is ambiguous.) — [Nuvemshop partner guide](https://atendimento.nuvemshop.com.br/parceiros-tecnologicos/guia-detalhes-do-programa-de-parceiros-tecnologicos)

#### Google Search Ads (high-intent long tail)
- **WordStream/LocaliQ 2025 Google Ads benchmarks (16,000+ campaigns, mostly US, April 2024–March 2025) [S].** Average CPC is US$5.26, average CTR 6.66%, and average conversion rate 7.52%. Some outlets report US$5.42, so the headline figure is not settled. — [Search Engine Land](https://searchengineland.com/google-ads-costs-rise-again-but-conversions-improve-report-455663); [Shopifreaks](https://www.shopifreaks.com/google-ads-cpcs-rose-to-5-42-in-2025-with-87-of-industries-seeing-increases-but-conversion-rates-climbed-to-8-18-as-automation-improves/)
- **Business services [S].** Cost per lead is US$103.54 (WordStream, via Search Engine Land). CPC is about US$5.58 (Focus Digital's own study). — [Search Engine Land](https://searchengineland.com/google-ads-costs-rise-again-but-conversions-improve-report-455663); [Focus Digital](https://focus-digital.co/?p=6055)
- No 2025–2026 Brazil-specific Google Ads CPC benchmark for software or B2B was found. Google directs advertisers to Keyword Planner for CPC estimates [S]. — [Google Ads Help pt-BR](https://support.google.com/adwords/answer/14074?hl=pt-BR)
- **Seer Interactive (2025-11-04; 3,119 informational queries across 42 organizations, June 2024–September 2025) [P, via PPC Land].** Paid CTR on informational queries showing AI Overviews fell from 19.7% to 6.34% (−68%). The paid sample was 1.1M impressions. — [PPC Land](https://ppc.land/google-ai-overviews-reduce-organic-ctr-61-paid-traffic-68/)
- ChartMogul (2026): paid-search signups are among the lowest-converting. — [ChartMogul part 2](https://chartmogul.com/reports/saas-conversion-report-2/)

#### Meta ads for B2B/SMB software
- **WordStream 2025 Facebook ads benchmarks [S].** Traffic campaigns: average CPC US$0.70 across industries (down from US$0.77), US$0.75 for Business Services. Lead campaigns: average CPC US$1.92 and average CPL US$27.66 (+21% year over year), vs a comparable Google CPL of US$70.11. — [WordStream](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025); [Search Engine Land](https://searchengineland.com/facebook-ad-costs-jump-beat-google-461690)
- **Superads (January 2025–January 2026; aggregated accounts of its users) [S].** The median Meta CPC in Brazil was about US$0.37 vs about US$1.13 globally. When fetched, the page rendered only the global view, so the Brazil figure could not be confirmed. — [Superads](https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/software-and-it-services/brazil)
- **Superads global series (page text, more than US$3B of spend) [P].** The global median Meta CPC fell from US$1.08 in July 2025 to US$0.77 in July 2026 and averaged about US$1.05. — [Superads](https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/software-and-it-services/brazil)
- ChartMogul (2026): Meta-ads signups are among the lowest-converting. One respondent added: "We invested in paid traffic with the right ICP. It was scary how precise the thing got." — [ChartMogul part 2](https://chartmogul.com/reports/saas-conversion-report-2/)

#### SEO, programmatic SEO and AI search (2025–2026)
- **Ahrefs (2025-05-15) [P].**
  - Of 1M random URLs first seen in September 2023, only 1.74% reached the top 10 within a year (vs 5.7% in 2017).
  - Of 2M non-empty English URLs created in October 2023, 6.11% did; Ahrefs says this "might be a more fair number."
  - 40.82% of the pages that reached the top 10 did so within the first month.
  - 72.9% of top-10 pages are more than 3 years old, and the average #1 page is 5 years old.
  - Ahrefs' advice: "After ~6 months… your chances are pretty low after that unless you make some changes."

  — [Ahrefs](https://ahrefs.com/blog/how-long-does-it-take-to-rank/)
- **Ahrefs AI Overviews re-run (published 2026-02-04, December 2025 data, 300k keywords) [P].** An AI Overview now correlates with a 58% lower CTR for the #1 result, up from 34.5% in the April 2025 study. Position-1 CTR on AI Overview keywords fell from 0.073 (December 2023) to 0.016 (December 2025). — [Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/)
- **Seer Interactive (2025-11-04) [P, via PPC Land].** Organic CTR on informational queries with AI Overviews fell from 1.76% to 0.61% (−61%). Queries without AI Overviews also fell, by 41% to 1.62%. Brands cited in an AI Overview got 35% more organic clicks, though causation is not proven. — [PPC Land](https://ppc.land/google-ai-overviews-reduce-organic-ctr-61-paid-traffic-68/)
- Smaller estimate: Amsive measured a 15.49% CTR drop across 700,000 keywords [S]. — [Search Engine Land](https://searchengineland.com/google-ai-overviews-hurt-click-through-rates-454428)
- An Ahrefs article dated 2025-07-21 is titled "76% of AI Overview Citations Pull From the Top 10" (title only, shown in Ahrefs' related-posts list). — [Ahrefs](https://ahrefs.com/blog/how-long-does-it-take-to-rank/)
- **Google spam policies (last updated 2026-08-28) [P].** "Scaled content abuse is when many pages are generated for the primary purpose of manipulating search rankings and not helping users… no matter how it's created." Examples include "using generative AI tools… to generate many pages without adding value for users" and "creating many pages where the content makes little or no sense to a reader but contains search keywords." — [Google Search Central](https://developers.google.com/search/docs/essentials/spam-policies)
- **ChartMogul 2026 survey examples [P, anecdotal].** "Generating a free template library for legal documents that lawyers use. This made a 40x impact on our organic SEO." "Investing in G2 has lifted all channels" (Kyle Poyar notes that LLMs frequently cite G2 data). Structured-data and technical-SEO work increased AI mentions and qualified organic traffic. — [ChartMogul part 2](https://chartmogul.com/reports/saas-conversion-report-2/)

#### Free tools and calculators as lead magnets
- The only evidence found is anecdotal: the free template library above, which produced a "40x impact on our organic SEO." — [ChartMogul part 2](https://chartmogul.com/reports/saas-conversion-report-2/)

#### Reddit, Facebook groups, WhatsApp communities
- No quantitative benchmark was found. The nearest data point is category-level: signups from social media and referral traffic convert at the highest rates (ChartMogul 2026). — [ChartMogul part 2](https://chartmogul.com/reports/saas-conversion-report-2/)

#### Directories and launch platforms (Product Hunt, G2/Capterra, SaaS directories)
- **MySignature.io survey (published 2024-10-21, updated 2026-07-01; "dozens" of products that reached a daily top 10) [V].**
  - Visitors from Product Hunt: 24.5% of launches got 100–500, 26.5% got 500–1,000, 22.4% got 1,000–2,000, and 10.2% got 2,000–5,000.
  - Registrations: 50% saw some increase, 30% a significant increase, and 16% none.
  - 42% saw some increase in sales.
  - 54% made partnerships or connections.

  — [MySignature](https://mysignature.io/blog/product-hunt-launch/)
- **DEV Community playbook (2026-07-30) [A, low reliability: it cites unverifiable "Product Hunt internal data" and other uncited statistics].** A bootstrapped time-tracking SaaS finished #2 Product of the Day in 2023 with 1,847 upvotes. Traffic fell 84% by the next Wednesday, and the launch yielded 140 signups and 22 paid customers. — [DEV Community](https://dev.to/insightlab/the-product-hunt-playbook-turning-a-one-day-launch-into-months-of-growth-for-bootstrapped-saas-1hl3)
- G2 investment was reported to have "lifted all channels" (ChartMogul survey anecdote). — [ChartMogul part 2](https://chartmogul.com/reports/saas-conversion-report-2/)

#### YouTube and short video
- No credible B2B/SMB benchmark was found. The only figure is from the low-reliability DEV post: a recap YouTube video that "still drives 15–20 signups per month" eight months later. — [DEV Community](https://dev.to/insightlab/the-product-hunt-playbook-turning-a-one-day-launch-into-months-of-growth-for-bootstrapped-saas-1hl3)

#### Cold email (the client prefers not to rely on it)
- **Woodpecker (updated 2026-06-23; 20M+ emails, cross-referenced with external studies) [V].**
  - The platform-wide average reply rate is 3.43% in 2026, down from 5.1% in 2024; 5–10% is "good" and 10%+ excellent.
  - Campaigns to fewer than 50 recipients average 5.8%, vs 2.1% for 1,000+.
  - Sequences with 4–7 steps average 8.3%, vs 4.1% with no follow-ups, and 42% of replies come from follow-ups.
  - Advanced personalization gets about 17–18%, vs about 7–9% for basic templates.

  — [Woodpecker](https://woodpecker.co/blog/cold-email-statistics/)
- **Other 2026 figures [S].** Saleshandy: 3.7% (53M emails, January–June 2026). Boomerang: 1.4% B2B average (vs 3.5% in 2018). Belkins: 0.45% under a strict count that excludes auto-replies. Published benchmarks vary by up to 7.6x depending on methodology. — [Saleshandy](https://saleshandy.com/blog/cold-email-statistics/); [Boomerang](https://www.getboomerang.ai/glossaries/cold-email-reply-rate-benchmarks-2026); [EmailBison](https://emailbison.com/blogs/cold-email-open-rates)

#### Generic time-to-first-customers data
- **Chargebee (2016; about 750 early-stage SaaS) [S, dated].** The top 50% got their first 100 customers in about 72.5 days. — [Chargebee](https://www.chargebee.com/static/resources/downloads/infographics/saas-usinesses-first-100%20customers.pdf)
- **Website Planet interview [S, weak].** The average successful micro-SaaS took 3–9 months from conception to its first dollar. — [URLaunched](https://www.urlaunched.com/blog/micro-saas-interview)

### Inferences
Estimated time to first customer by channel. These are my estimates from channel mechanics and the base rates above, not measured medians:

- **Marketplace listing (Shopify, Nuvemshop, Chrome, WordPress).**
  - First install: days to weeks after approval, if users already search for the job inside the store. Approval itself can take several rounds (Shopify anecdote).
  - Distribution is extremely concentrated: the median extension has 18 users. Pick a niche with visible in-store demand (competitors with reviews, search suggestions).
  - Expected install→paid: 0.5–2% for extensions, 1–2% for WordPress, and probably higher for store apps billed on a card already on file. That last point is unverified.
- **Google Search Ads.**
  - Traffic arrives the same day.
  - At US B2B CPCs of US$5+, US$50–100 buys roughly 10–20 clicks. That is statistically useless for measuring conversion (see section 4), though it can still test CTR and query intent.
  - In Brazil, if the BR/global CPC ratio seen on Meta (about 1/3) also holds for Google, the same money would buy several times more clicks. This is unverified; check Keyword Planner.
- **Meta ads.** Brazilian clicks are cheap (median about US$0.37, unverified), so they are good for testing messages and creatives. They are poor for first B2B revenue at a ~US$100 budget because paid-social signups convert worst.
- **SEO and programmatic SEO.**
  - Expect 3–12+ months; most pages never rank.
  - Programmatic SEO with thin, templated pages now runs straight into Google's scaled-content-abuse policy.
  - Informational queries lose the most clicks to AI Overviews, so the realistic SEO target is transactional or "tool-intent" long-tail queries (e.g., "calculadora de X," "gerador de Y," "modelo de Z") where a working tool is the answer.
- **Free tools.** Same slow timeline as SEO, but they are the most defensible SEO asset and convert better than articles (anecdotal).
- **Communities.** First conversations within days; no benchmarks; must be value-first to avoid bans.
- **Product Hunt.** A one-day spike of about 100–2,000 visitors from a global tech audience. It fits a Brazilian SMB tool poorly, but the backlink and badge have some value.
- **Cold email.** Replies within days at about 3% (≥5% only with small, highly personalized lists). Reply→paid conversion is unknown.
- **AI search.** LLM referrals convert best (Webflow: 24%), and AI Overview citations mostly come from top-10 pages. In practice, the "new SEO" means ranking in the top 10 *and* being mentioned on third-party pages that LLMs cite (G2/directories, community threads).

### Gaps
- No source gives a median time to first customer for any channel.
- No conversion benchmarks were found for Reddit, Facebook groups, WhatsApp communities, YouTube or short video.
- No Brazil Google Ads CPC benchmark; the Superads Brazil Meta figure is unverified.
- No Nuvemshop app-store statistics (merchant count, installs, conversion).
- No G2/Capterra free-listing outcome data.
- Meta's learning-phase requirements could not be verified; the help page was behind a login wall.
- No data on cold-email reply→paid conversion or on how the LGPD treats B2B cold email.
- The Chrome Web Store fee amount is not stated on the fetched page.

## 3. How long micro-SaaS takes to reach US$1k and US$5k MRR, typical SMB churn, and which pricing converts

### Takeaway
Among the minority of indie SaaS that ever reach US$1k MRR, the typical time is about 5–9 months (small, survivorship-biased sample). Most new products never get there: one 2026 dataset reports a median MRR of US$168 for the 2025 cohort, with only 23.5% above US$1k. Going from US$1k to US$5k at a plausible 10–15% net monthly growth takes another 11–17 months. Customer churn for low-ARPA SaaS runs about 6–7% per month, so price level and segment (ARPA ≥ US$20–50) matter more than conversion tweaks. No reliable dataset compares one-time vs subscription pricing for SMB tools.

### Cited Findings
- **Indie Hackers analysis (2022; about 30 products with Stripe-verified revenue) [S].** On average it took 9 months to reach US$1K MRR; the 25th percentile was 5 months and the median 8 months. A later post acknowledged the dataset is small. — [Indie Hackers](https://www.indiehackers.com/post/it-takes-5-months-to-reach-1k-in-mrr-491742f806); [Indie Hackers follow-up](https://www.indiehackers.com/post/whats-new-how-long-does-it-take-to-hit-1k-mrr-35bda788b1)
- **BigIdeasDB, "State of Indie SaaS Revenue 2026" (3,787 bootstrapped SaaS) [S; page blocked, methodology unverified].** The 2025 founding cohort has a median MRR of US$168, and 23.5% are above US$1k. The page itself notes survivorship. — [BigIdeasDB](https://bigideasdb.com/state-of-indie-saas-revenue-2026)
- **BigIdeasDB, analysis of 636 businesses listed for sale [S].** Median revenue is about US$5,167/month in the first year, rising to about US$20,250/month at 9+ years. This is biased toward businesses good enough to sell. — [BigIdeasDB](https://bigideasdb.com/how-long-does-it-take-to-grow-a-saas)
- **MicroConf State of Independent SaaS 2024 (data collected late 2023; respondents already generating revenue) [S].** 17.7% of respondents are under US$1,000 MRR, the largest single band. In the 2021 survey, more than 50% were under US$10K MRR. — [MicroConf](https://microconf.com/saas-this-year); [Indie Hackers on the 2021 report](https://www.indiehackers.com/post/the-2021-state-of-independent-saas-report-d010d8124b)
- **MicroConf 2024 growth (podcast) [P].** Products targeting small businesses averaged about 12% month-over-month growth; consumer products about 5%. — [SFTROU ep. 721](https://www.startupsfortherestofus.com/episodes/episode-721-7-key-takeaways-from-the-2024-state-of-independent-saas-report)
- **BetterLaunch [S, weak].** 50% of active indie hackers make under US$1K/month, and US$0→10K MRR typically takes 12–36 months. — [BetterLaunch](https://www.betterlaunch.co/blog/indie-hacker)
- **ChartMogul (teaser on its report page, accessed 2026-10-12) [P].** Only 13% of startups reach US$10M ARR within 10 years. Below US$1M ARR, startups retain customers equally regardless of funding model. — [ChartMogul](https://chartmogul.com/reports/saas-conversion-report/)
- **ChartMogul churn benchmarks (published 2022-02-23; data November 2021–January 2022) [P].**
  - Median monthly customer churn is 6.1% for ARPA under US$25 vs 2.2% for ARPA over US$500.
  - Companies under US$300k ARR have 6.5% median monthly churn.
  - The best companies target under 2% per month.
  - 5% monthly churn equals 46% annual.
  - Top-quartile customer retention is 64.7% for ARPA under US$25 vs 85.8% for ARPA over US$1k.

  — [ChartMogul](https://chartmogul.com/blog/good-customer-churn-rate/)
- **ChartMogul SaaS Retention Report 2023 (2,100+ SaaS) [S].** Only 2.7% of companies with ARPA under US$10/month had net revenue retention above 100%, vs 41.1% for ARPA over US$500. — [ChartMogul](https://chartmogul.com/saas-retention-report/)
- **ChartMogul help center [S].** A business under US$10 ARPA can expect 6–7% monthly churn, vs 1–2% at US$500+. — [ChartMogul Help](https://help.chartmogul.com/hc/en-us/articles/203359321)
- **Pricing evidence (Kyle Poyar, ChartMogul, 2026-03-18) [P].**
  - "Simply raising or lowering prices tends to not change conversion rates very much"; changing plans, limits, feature gates and trial mechanics matters more.
  - Example: a dual call to action (freemium, or a 14-day card-required premium trial) increased premium trials by 26%.
  - Example: raising the monthly price by US$5 while keeping the annual price (a 16% discount) increased demand and the share of annual subscribers.

  — [ChartMogul part 2](https://chartmogul.com/reports/saas-conversion-report-2/)
- **Fixed fees penalize low prices.** Paddle charges 5% + 50¢, and Hotmart charges a 20% "microtransaction" fee on sales of R$10 or less. — [Paddle](https://www.paddle.com/pricing); [Tactus on Hotmart](https://tactus.com.br/taxas-da-hotmart-para-produtor/)

### Inferences
Realistic expectations for this client (a base-rate view, not a forecast):
- **First sale:** about 2–8 weeks after a usable product reaches high-intent users. The BigIdeasDB median (US$168 MRR for the 2025 cohort) implies that roughly half of new products earn almost nothing in year one.
- **US$1k MRR:** about 5–9 months for those who make it; plan for 6–12 months. The probability is maybe 1 in 4 (23.5% in BigIdeasDB, a survivorship-affected figure), and likely lower for a first product.
- **US$5k MRR:** going from US$1k to US$5k takes ln(5)/ln(1+g) months:

  | Net monthly growth | Months from US$1k to US$5k |
  |---|---|
  | 10% | 16.9 |
  | 12% | 14.2 |
  | 15% | 11.5 |
  | 20% | 8.8 |

  That puts US$5k MRR at about 18–30 months from start, for the minority who sustain 10–15% net growth.
- **Churn arithmetic.** At 6% monthly churn, holding US$5k MRR needs about US$300 of new MRR every month.
  - At US$20 ARPA: 250 customers, and about 15 new customers per month just to stay flat.
  - At US$50 ARPA: 100 customers and about 6 new per month.
  - At US$10 ARPA: 500 customers and about 30 new per month.

  So price SMB tools at roughly US$20–50/month (perhaps R$49–149/month in Brazil, an inference with no Brazilian price data) and avoid sub-US$10 subscriptions.
- **One-time vs subscription (inference).** One-time or "lifetime" offers are useful for early cash (pre-sales, Chrome or WordPress users who resist subscriptions). A US$5k *monthly recurring* goal needs subscriptions, ideally with an annual option, because one-time revenue must be re-won every month.
- **Survivorship.** MicroConf counts only revenue-generating founders, Indie Hackers verified-revenue listings are self-selected, and Starter Story features winners. All three overstate both odds and speed.

### Gaps
- No Starter Story, Baremetrics or ProfitWell/Paddle dataset on time to MRR milestones could be retrieved; the Indie Hackers and MicroConf pages were blocked.
- No distribution of time to US$5k MRR exists in the sources found.
- No Brazil-specific SMB SaaS churn benchmark was found.
- No controlled data compares one-time vs subscription conversion or ideal price points for small SMB tools.
- No 2025 MicroConf report was found; search results showed only the 2024 edition.

## 4. Cheap validation methods (smoke tests, fake doors, pre-sales, small Google Ads tests): sample sizes and signal thresholds

### Takeaway
No authoritative industry thresholds exist. The practical approach combines two things:
- **Benchmark bars.** Median landing-page conversion is about 6.6%, and SaaS visit→signup is about 3.5–9%.
- **Basic statistics.** About 100–200 targeted visitors per variant gives roughly ±3–6 percentage points of precision at a 5–10% conversion rate. Zero conversions from 100 visitors bounds the true rate below about 3%.

Only money (pre-orders, deposits, card-required trials) is a strong signal; email signups are weak.

### Cited Findings
- **Rule of three.** If an event does not occur in n trials, 0 to 3/n is a 95% confidence interval for its rate; this is a good approximation for n > 30. — [Wikipedia](https://en.wikipedia.org/wiki/Rule_of_three_(statistics))
- **Benchmark bars.**
  - Unbounce (2024): median landing-page conversion 6.6%; paid search averages 10.9% and paid social 12%. — [Unbounce](https://unbounce.com/conversion-benchmark-report/)
  - ChartMogul (2026): visit→signup is about 9% for freemium, 4.5% for free trials and 3.5% for card-required trials. — [ChartMogul](https://chartmogul.com/reports/saas-conversion-report/)
  - First Page Sage (2025): visitor→opt-in trial is 8.5% organic and 7.1% paid. — [First Page Sage](https://firstpagesage.com/seo-blog/saas-free-trial-conversion-rate-benchmarks/)
- **Card as a filter.** Requiring a card is recommended as a litmus test for very early, first-time founders (Asia Orangio, MicroConf 2024 discussion). — [SFTROU ep. 721](https://www.startupsfortherestofus.com/episodes/episode-721-7-key-takeaways-from-the-2024-state-of-independent-saas-report)
- **Test-cost inputs.** Google Ads averages US$5.26 CPC (mostly US) [S]. Meta traffic CPC averages US$0.70 globally [S], with a Brazil median of about US$0.37 [S, unverified]. See section 2 for sources. — [Search Engine Land](https://searchengineland.com/google-ads-costs-rise-again-but-conversions-improve-report-455663); [WordStream](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025); [Superads](https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/software-and-it-services/brazil)

### Inferences
- **Precision by sample size** (computed here; normal approximation, 95% confidence):

  | True conversion | n = 100 | n = 200 | n = 400 |
  |---|---|---|---|
  | 5% | ±4.3 pp | ±3.0 pp | ±2.1 pp |
  | 10% | ±5.9 pp | ±4.2 pp | ±2.9 pp |
  | 20% | ±7.8 pp | ±5.5 pp | ±3.9 pp |

  Wilson intervals for small counts: 3/30 → 3.5–25.6%; 5/50 → 4.3–21.4%; 10/100 → 5.5–17.4%. Zero conversions in 30, 50, 100 or 200 visitors bounds the true rate below 10%, 6%, 3% or 1.5% respectively.
- **What this means.** Fewer than about 100 targeted visitors per idea cannot separate a 3% offer from a 10% offer. In the US, US$50–100 of Google Ads (about 10–20 clicks at US$5) is therefore not a conversion test. In Brazil, the same money may plausibly reach 100+ clicks, but CPCs are unverified.
- **Proposed thresholds** (my synthesis, not an industry standard):
  - **Waitlist smoke test** (price shown, email capture): ≥10% of *targeted* visitors means proceed; 3–10% means iterate on copy, offer or segment; <3% after 100–150 targeted visitors means kill or re-target.
  - **Fake-door "Buy / Start trial" at the real price:** ≥2–3% of visitors clicking buy means move to a real pre-sale. Show an honest "launching soon, reserve your spot" message after the click.
  - **Pre-sale or paid pilot:** ≥3 payments (or refundable deposits) from strangers out of about 20–30 qualified conversations, or ≥1–2% of targeted paid-ad visitors paying, means build.
  - **Google Ads test in Brazil:** R$150–300 on 10–30 exact/phrase long-tail keywords, aiming for ≥100 clicks per idea. A CTR ≥5% signals query-intent match; ≥5% click→signup (or ≥1% click→payment) signals a real offer.
- **Observable demand is validation too.** Keyword Planner volume and CPC, app-store search suggestions, and paying competitors with reviews all count; buyers already paying competitors is the strongest pre-build signal.

### Gaps
- No peer-reviewed or industry-standard thresholds were found for smoke tests, fake doors or pre-sales.
- No benchmark exists for pre-sale conversion rates.
- Brazil CPCs could not be verified, so test budgets are estimates.

## 5. Getting paid in Brazil (Pix, card, subscriptions): provider fees and whether a CPF can use them

### Takeaway
For a solo founder, Asaas, Mercado Pago and Efí accept individuals (CPF) and support Pix, card and recurring charges at roughly 1–5% per transaction. Pagar.me (Stone) requires a CNPJ or MEI. Stripe Brasil is the priciest for cards (3.99% + R$0.39, plus 0.7% for Billing), and its Pix is invite-only. Hotmart, Kiwify and Eduzz cost about 9–15% per sale but bring an affiliate network. Pix Automático (recurring Pix with one-time authorization) is spreading, but some providers require a CNPJ older than 6 months.

### Cited Findings
- **Asaas (pricing page accessed 2026-10-12) [P].**
  - No monthly or signup fee.
  - Pix: R$1.99 per received payment (R$0.99 promotional rate for the first 3 months). Boleto: R$1.99 (promo R$0.99).
  - Credit card, one installment and subscription charges: R$0.49 + 2.99% (promo R$0.49 + 1.99%). 2–6 installments: R$0.49 + 3.49%. Debit: R$0.35 + 1.89%.
  - Card funds arrive one installment per 32 days; anticipation costs 1.25%/month.
  - NFS-e issuance: R$0.49 per invoice. WhatsApp dunning notice: R$0.55.
  - Both pessoa física and pessoa jurídica accounts exist (for example, Pix transfers are listed as free for PF accounts).

  — [Asaas](https://www.asaas.com/precos-e-taxas)
- **Asaas docs [S].** "Assinaturas" (Asaas generates recurring boleto, Pix or card charges; recommended for SaaS) is distinct from "Pix Automático" (the payer authorizes once). In May 2026 Asaas added automatic charge creation once the authorization is active. — [Asaas docs](https://docs.asaas.com/docs/pix-automatico)
- **Mercado Pago (payment-link page accessed 2026-10-12) [P].** Credit card: 4.98% if funds are released immediately, 4.48% at 14 days, 3.99% at 30 days. Pix: 0.99%, immediate. Boleto: 3.99%, funds within 3 days. Some new sellers start on 7-day release before immediate release is unlocked [S]. — [Mercado Pago](https://www.mercadopago.com.br/ferramentas-para-vender/link-de-pagamento)
- **Mercado Pago blog [S].** It offers fixed-price "Planos de assinatura." Enabling Pix Automático requires, among other things, a CNPJ active for more than six months. — [Mercado Pago blog](https://www.mercadopago.com.br/blog/pix-automatico-vender-pacotes-assinaturas)
- **Stripe Brasil (pricing accessed 2026-10-12) [P].**
  - Domestic cards: 3.99% + R$0.39; international cards: +2%.
  - Boleto: R$3.45. Pix: 1.19%, by invitation only.
  - Dispute fee: R$55. Billing (subscriptions): 0.7% of volume. Currency conversion: from 2%.
  - No setup or monthly fees.

  — [Stripe BR](https://stripe.com/br/pricing)
- **Stripe + EBANX (announced August 2025) [S].** Stripe businesses, including cross-border ones, can accept Pix from Brazilian customers through EBANX. — [Finextra](https://www.finextra.com/newsarticle/46431/stripe-businesses-can-now-accept-pix-in-brazil)
- **Efí Bank (tariff page accessed 2026-10-12) [P].**
  - Account types: Efí Empresas (with CNPJ), **Efí Pro ("conta para negócios sem CNPJ")** and Efí Para Você (personal).
  - Boleto or carnê paid: R$3.45.
  - Card: one installment 3.49% (funds within 31 days); 2–6x 3.99%; 7–12x 4.39%.
  - Pix received by key, static QR, dynamic QR or API: 1.19%; the app includes 30 free Pix per month.
  - Pix Automático: R$3.50 per settled payment.
  - Recurring payments, payment links, checkout and API are free.

  — [Efí](https://sejaefi.com.br/tarifas)
- **Pagar.me / Stone (accessed 2026-10-12) [P].** Pix 0.99%; credit card, one installment, 4.19%; funds next day; subscriptions supported; **requires an active CNPJ or MEI**. — [Pagar.me](https://pagar.me/precos/)
- **Iugu.** Prices are not shown on the public page (the page fetched 2026-10-12 lists Pix Automático and Bolepix). — [Iugu](https://www.iugu.com/precos)
- **Hotmart (Tactus accounting firm, 2026-08-31) [P, secondary].**
  - 9.9% + R$1.00 per approved sale until 2026-09-20; 9.9% + R$2.49 from 2026-09-21, when the separate video-player fee was folded in.
  - Up to 8.9% above R$500k/year in sales.
  - 20% fee on sales of R$10 or less.
  - The buyer pays 3.49%/month installment interest.
  - Anticipation costs 3.59% for funds in 2 business days or 2.19% for 14 days.

  — [Tactus](https://tactus.com.br/taxas-da-hotmart-para-produtor/)
- **Kiwify [S].** 8.99% + R$2.49 per approved sale and R$3.67 per withdrawal. Pix and boleto balances are released after 2 days, card after 15. Other sources cite 4.99%, which conflicts. — [Tactus](https://tactus.com.br/como-sacar-dinheiro-na-kiwify/); [Freelas em Crise](https://www.freelasemcrise.com.br/blog/hotmart-kiwify-eduzz-comparativo)
- **Eduzz [S].** Direct sales: 4.9% + R$1 (one comparison says + R$2.49). International sales carry an extra 6%. — [Freelas em Crise](https://www.freelasemcrise.com.br/blog/hotmart-kiwify-eduzz-comparativo)
- **Pix rules for individuals [S].** Individuals generally pay nothing to send or receive Pix. Institutions may, however, charge an individual for receiving Pix from sales of goods or services, for dynamic-QR receipts, or above 30 receipts a month. Individual accounts used for strictly commercial purposes can be reclassified and charged. — [Jornal Contábil](https://jornalcontabil.com.br/noticia/em-quais-situacoes-o-pix-sera-cobrado-para-pessoas-fisicas-e-meis/)
- **Pix Automático adoption [S][V].** PagBrasil reported +181% new users and +182% transactions from Q4 2025 to Q1 2026; EBANX claims 38% of all Pix Automático transactions. — [Let's Money (PagBrasil)](https://www.letsmoney.com.br/noticias/pagbrasil-pix-automatico-um-ano-recorrencia/); [Let's Money (EBANX)](https://www.letsmoney.com.br/noticias/pix-automatico-64-novos-usuarios-ebanx/)

### Inferences
- **Fee on a R$49/month subscription** (computed from the published rates):

  | Provider and method | Fee | % of R$49 |
  |---|---|---|
  | Asaas card (standard / promo) | R$1.96 / R$1.47 | 4.0% / 3.0% |
  | Asaas Pix (flat) | R$1.99 | 4.1% |
  | Mercado Pago Pix | R$0.49 | 1.0% |
  | Mercado Pago card, 30-day / immediate release | R$1.96 / R$2.44 | 4.0% / 5.0% |
  | Stripe BR card + Billing | R$2.69 | 5.5% |
  | Efí card | R$1.71 | 3.5% |
  | Efí Pix | R$0.58 | 1.2% |
  | Efí Pix Automático | R$3.50 | 7.1% |
  | Pagar.me Pix / card | R$0.49 / R$2.05 | 1.0% / 4.2% |
  | Hotmart (from 21/09/2026) | R$7.34 | 15.0% |

- **Default choice.** Asaas has native subscriptions (card, Pix, boleto), dunning and NFS-e issuance, and works under a CPF first and a CNPJ later. Efí Pro is an alternative for a CPF business account. Use Mercado Pago when the cheapest Pix and buyer familiarity matter most. Use Stripe BR only if the Stripe API and Billing are worth about 1.5 percentage points more on cards.
- **Flat-fee Pix** (Asaas R$1.99, Efí Pix Automático R$3.50) is expensive on low tickets; percentage Pix (0.99–1.19%) is better under about R$170–200.
- **Infoproduct platforms** (Hotmart, Kiwify, Eduzz) are worth considering only to tap their affiliate marketplaces. For SaaS they need webhook-based access control (an unverified integration detail) and cost 3–4x more per sale.

### Gaps
- It was not verified whether Stripe Brasil accepts CPF (individual) accounts.
- Mercado Pago's subscription-specific fees, Iugu's prices, Asaas's Pix Automático fee and Eduzz's official rates were not retrieved.
- Chargeback rules and fees were not compared across Brazilian providers.

## 6. Selling abroad: Merchant of Record options, Stripe availability for Brazilian entities, and payouts

### Takeaway
As of October 2026, Paddle is the most dependable Merchant of Record for a Brazil-resident seller:
- Brazil is not on its unsupported list.
- It charges 5% + 50¢ all-in.
- It pays out monthly by wire (US$15 SWIFT fee when the currency differs from the bank country's) or through Payoneer.

The other options are weaker:
- **Polar** is effectively unavailable, because Brazil is missing from its Stripe Connect Express payout list.
- **Stripe Managed Payments** only serves businesses in North America, Europe and Asia-Pacific.
- **Lemon Squeezy** pays Brazil only via PayPal and is steering users toward Stripe Managed Payments.
- **Gumroad** works but costs 10% + 50¢.

### Cited Findings
- **Paddle (accessed 2026-10-12) [P].** 5% + 50¢ per transaction, including global tax compliance, fraud protection and chargeback handling. Bespoke pricing is available for products under US$10. Paddle "works with software businesses anywhere in the world" except the listed unsupported countries (sanctioned or high-risk jurisdictions such as Russia, Iran, Cuba and Venezuela); Brazil is not on that list. — [Paddle pricing](https://www.paddle.com/pricing); [Paddle supported countries](https://www.paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle)
- **Paddle payouts [P].**
  - Payouts are monthly: a balance above your threshold (minimum US$100) converts on the 1st and is sent by the 15th, then takes up to 3 working days to arrive.
  - Methods: wire transfer or Payoneer.
  - Paddle adds no fee of its own, but a SWIFT fee of US$/€/£15 applies when the payout currency differs from the bank country's currency.
  - Payout currencies include USD, EUR, GBP, CAD, AUD, CHF and others, but **not BRL**.

  — [Paddle: when and how](https://www.paddle.com/help/manage/get-paid/when-and-how-do-i-get-paid); [Paddle: fees](https://www.paddle.com/help/manage/get-paid/is-there-a-fee-taken-for-payouts); [Paddle: currencies](https://www.paddle.com/help/manage/get-paid/can-i-be-paid-in-my-local-currency)
- **Lemon Squeezy (accessed 2026-10-12) [P].**
  - 5% + 50¢, plus 1.5% for transactions outside the US, 1.5% for PayPal transactions, and 0.5% for subscription payments.
  - Payouts via Stripe cost 1% for banks outside the US; via PayPal, 3% capped at US$30 for accounts outside the US.
  - **Brazil is absent from the bank-payout country list** (which does include Argentina, Chile, Colombia and Mexico). PayPal payouts cover 200+ countries.

  — [LS fees](https://docs.lemonsqueezy.com/help/getting-started/fees); [LS supported countries](https://docs.lemonsqueezy.com/help/getting-started/supported-countries); [LS pricing](https://www.lemonsqueezy.com/pricing)
- **Lemon Squeezy, "2026 Update: Lemon Squeezy + Stripe Managed Payments" [P].** "Stripe Managed Payments is here." Public sign-up without an invite is coming "very soon," and the stated goal is "to provide Lemon Squeezy users an easy way to migrate to Stripe Managed Payments." Early access is through a waitlist. — [LS blog](https://www.lemonsqueezy.com/blog/2026-update)
- **Stripe Managed Payments eligibility (docs accessed 2026-10-12) [P].** The business must be based in a supported location; the locations are grouped as North America, Europe and Asia Pacific, with no Latin American group. Only direct integrations are allowed (no Connect or Express accounts), and only fully automated digital products qualify. A search summary lists Canada, the US, about two dozen European countries, Hong Kong, Japan and Singapore, and describes the product as in private preview [S]. — [Stripe docs](https://docs.stripe.com/payments/managed-payments/eligibility); [Stripe changelog 2026-04-22](https://docs.stripe.com/changelog/dahlia/2026-04-22/managed-payments.md)
- **Polar (fees page accessed 2026-10-12) [P].**
  - Organizations created on or after 2026-05-27 start on Starter at 5% + 50¢. Paid plans: Pro US$20/month at 3.8% + 40¢; Growth US$100/month at 3.6% + 35¢; Scale US$400/month at 3.4% + 30¢.
  - +1.5% for non-US cards; US$15 per dispute.
  - Payouts run through Stripe Connect Express: US$2/month while payouts are active, plus 0.25% + US$0.25 per payout, plus 0.25–1% currency conversion.

  — [Polar fees](https://polar.sh/docs/merchant-of-record/fees)
- **Polar supported payout countries [P].** The list (residents or businesses in Stripe Connect Express countries) includes Argentina, Bolivia, Chile, Colombia, Mexico, Paraguay, Peru and Uruguay, but **not Brazil**. — [Polar countries](https://polar.sh/docs/merchant-of-record/supported-countries)
- **Gumroad (accessed 2026-10-12) [P].** 10% + US$0.50 per sale through your profile or direct links; 30% when customers find you through the Discover marketplace. Gumroad has been the merchant of record since 2025-01-01 and supports SaaS memberships. Payouts go by direct deposit or PayPal, depending on the country. — [Gumroad](https://gumroad.com/pricing)
- **Stripe Brasil for Brazilian entities [P].** Pricing is in BRL; international cards cost 2% extra and currency conversion starts at 2%. Stripe notes that remittances to or from Brazil go exclusively through authorized foreign-exchange channels. — [Stripe BR pricing](https://stripe.com/br/pricing); [Stripe currencies](https://docs.stripe.com/currencies)
- **Payoneer (pricing accessed 2026-10-12) [P].**
  - Receiving USD in a non-USD country: 1%.
  - Card payment requests: up to 3.99% (+US$0.49 in some countries).
  - Withdrawal to a local bank with currency conversion: 1–4%, depending on region and volume.
  - Annual fee of US$29.95 if you receive less than US$6,000 in 12 months.

  — [Payoneer](https://www.payoneer.com/pt/about/pricing/)
- **Wise blog (2024-01-24, dated; Wise Brasil is Banco Central-authorized) [V].** It says PayPal Brazil charges 7.4% plus a fixed fee on international receipts, plus a 4.5% exchange-rate markup. Caixa charges 1% conversion (minimum US$30, maximum US$120), R$40 per SWIFT transfer, plus IOF. — [Wise](https://wise.com/br/blog/receber-dinheiro-exterior-brasil)
- **Wise Business for Brazilian companies [S][V].** It offers a rate close to mid-market, IOF stated as 0.38%, and local account details in up to 18 currencies. A third-party guide lists service fees "from 0.78%." — [Exiap](https://exiap.com.br/guias/abrir-uma-conta-wise-empresas); [Wise PJ taxes](https://wise.com/br/blog/impostos-remessa-internacional-pj)

### Inferences
- **Fees on a US$19/month subscription** (computed):

  | Platform | Fee | % |
  |---|---|---|
  | Paddle | US$1.45 | 7.6% |
  | Lemon Squeezy, US buyer / non-US buyer | US$1.54 / US$1.83 | 8.1% / 9.6% |
  | Gumroad | US$2.40 | 12.6% |

  Lemon Squeezy also adds the 3% PayPal payout fee (cap US$30) and PayPal's exchange spread. At a US$5 price the fees jump to Paddle 15%, Lemon Squeezy 15.5–17% and Gumroad 20%, so international plans should be at least US$9–19.
- **Paddle payout drag.** A US$15 SWIFT fee per monthly USD payout to a Brazilian account (plus the bank's spread) is about 1.5% at US$1k MRR. Raising the payout threshold (e.g., US$500–1,000), or receiving via Payoneer (1–4%) or a Wise Business USD account, dilutes it.
- **Lemon Squeezy is a platform-risk choice** for a Brazil-based seller: PayPal-only payouts, plus a migration path toward a product (Stripe Managed Payments) that excludes Brazil-based businesses.
- **Selling abroad directly through Stripe Brasil** (no Merchant of Record) makes the founder the seller of record. He would then be responsible for foreign VAT and US sales-tax obligations, and pay +2% on international cards plus conversion. A Merchant of Record is simpler at this stage.

### Gaps
- It was not verified whether Paddle onboards individuals without a CNPJ.
- Gumroad's payout method for Brazil, and whether a Stripe Brasil account can present USD prices to foreign buyers, were not verified.
- Wise Business's official receive fees for Brazil could not be read (the page is dynamic).
- It was not verified whether Brazilian banks book Paddle or Payoneer receipts as service-export foreign exchange, which would carry 0% IOF.

## 7. Legal structure and taxes: MEI, ME under Simples Nacional, or individual (Carnê-Leão); foreign revenue and FX; 2026 tax-reform effects

### Takeaway
- **MEI:** software development and licensing are not MEI activities in October 2026. A bill to allow them, PLP 25/2026, has passed only one Câmara committee (2026-06-30).
- **ME under Simples Nacional** is the practical vehicle. Software licensing and development fall under Anexo III (starting at 6%) when payroll, including pró-labore, is at least 28% of revenue (the "Fator R"); otherwise they fall under Anexo V (starting at 15.5%).
- **Export revenue** removes ISS, PIS and COFINS from the Simples payment, leaving about 3.05% effective in Anexo III's first bracket. Foreign-exchange inflows from service exports carry 0% IOF.
- **Selling as an individual (CPF)** is possible, but it gets expensive once income passes the new R$5,000/month income-tax exemption (2026 IR reform).
- **Tax reform:** 2026 is a test year, and its CBS/IBS rates do not apply to Simples companies. Exports of services and intangibles are immune from IBS/CBS.

### Cited Findings
- **MEI bill.** The Câmara's Comissão de Indústria, Comércio e Serviços approved PLP 25/2026 (author: Dep. Kim Kataguiri; rapporteur: Beto Richa) on 2026-06-30. It would allow programming and software development under MEI. It still needs the Finance and Constitution committees, the Câmara plenary and the Senate. — [Fenacon 2026-07-02](https://fenacon.org.br/noticias/comissao-aprova-inclusao-de-programadores-e-desenvolvedores-de-software-no-mei/)
- **Current MEI status [S].** Accounting guides state that programming, systems development and technical IT services are not currently permitted MEI activities. One site says otherwise without citing the official list. — [Meu Contador Online](https://www.meucontadoronline.com.br/blog/mei-em-ti-atividades-permitidas-riscos-fiscais); [Contabilidade Zen](https://www.contabilidadezen.com.br/blog/dev-mei-limites-atividades-2026/)
- **MEI revenue cap.** Still R$81k/year. PLP 67/2025 (to R$150k with IPCA indexation) and PLP 108/21 are under urgency, and a vote is expected after the 2026 elections. — [Fenacon 2026-04-10](https://fenacon.org.br/noticias/parlamentares-esperam-votar-novo-limite-para-o-mei-apos-periodo-eleitoral/)
- **LC 123/2006, art. 18 §5º-D (wording by LC 155/2016) [P].** "IV – elaboração de programas de computadores, inclusive jogos eletrônicos, desde que desenvolvidos em estabelecimento do optante; V – licenciamento ou cessão de direito de uso de programas de computação" are taxed under **Anexo III**. Under §5º-M, when payroll/revenue is below 28%, §5º-D activities are taxed under **Anexo V**. Under §5º-K, the ratio uses the previous 12 months. — [LC 123](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm)
- **Simples rate tables (in force since 2018) [P].**

  | | Anexo III | Anexo V |
  |---|---|---|
  | 1st bracket (12-month revenue ≤ R$180k) | 6.00% | 15.50% |
  | 2nd bracket (≤ R$360k) | 11.20%, minus R$9,360 | 18.00%, minus R$4,500 |
  | 1st-bracket split | IRPJ 4%, CSLL 3.5%, Cofins 12.82%, PIS 2.78%, CPP 43.4%, ISS 33.5% | IRPJ 25%, CSLL 15%, Cofins 14.10%, PIS 3.05%, CPP 28.85%, ISS 14% |

  — [LC 123](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm)
- **Export revenue in Simples [P].** Export revenue is segregated (art. 18 §4º-A, IV). The reduction "corresponderá tão somente aos percentuais relativos à Cofins, à Contribuição para o PIS/Pasep, ao IPI, ao ICMS e ao ISS" (§14). — [LC 123](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm)
- **Cosit Solution of Consultation 160/2024 (linked to 78/2019) [S].** PIS/Cofins non-incidence on service exports under Simples requires a customer resident abroad and an inflow of foreign currency; services whose result occurs in Brazil are excluded. — [Tributo Devido](https://tributodevido.com.br/portal/isencao-pis-cofins-exportacao-servicos-simples-nacional/)
- **ISS on exports [S].** It depends on whether the service's result occurs abroad and on municipal practice. — [Contabilidade.com](https://contabilidade.com/blog/iss-na-exportacao-de-servicos/)
- **CNAE choice [S].** 6203-1/00 (non-customizable software development and licensing) and the related CNAEs 6201-5/01, 6202-3/00 and 6204-0/00 are subject to Fator R. A developer with no pró-labore rarely reaches 28% and lands in Anexo V. — [Agilize](https://agilize.com.br/artigos/?p=4180)
- **IOF (Decreto 6.306/2007, art. 15-B I, as consolidated after Decrees 12.466/2025 and 12.499/2025, Legislative Decree 176/2025 and ADC 96) [P].** The IOF rate is **zero** "nas operações de câmbio relativas ao ingresso no País de receitas de exportação de bens e serviços." — [Decreto 6.306](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6306.htm)
- **Exchange contract [S].** Wise states 0.38% IOF on receipts. Accounting guides say that without an exchange contract, the revenue may lose its export classification and the related exemptions. — [Wise PJ](https://wise.com/br/blog/impostos-remessa-internacional-pj); [Contabilidade.com](https://contabilidade.com/blog/como-receber-pagamento-do-exterior-sendo-pj/)
- **Carnê-Leão [P].** Monthly income tax for residents on income received from individuals or from abroad, due by the last business day of the following month. — [Receita Federal](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao)
- **2026 monthly income-tax table [P].** Exempt up to R$2,428.80, then 7.5%, 15%, 22.5%, and 27.5% above R$4,664.68 (deduction R$908.73). The monthly simplified discount is R$607.20. **Under Lei 15.270/2025, from January 2026 tax is zeroed on monthly taxable income up to R$5,000** (reduction of up to R$312.89), phasing out linearly up to R$7,350. — [Receita 2026 tables](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026); [Lei 15.270/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm)
- **Lei 15.270/2025, other changes [P].** From January 2026, profits or dividends above R$50,000 per month paid by one company to one resident individual are subject to 10% withholding. From calendar year 2026 (filed in 2027), individuals with total income above R$600,000/year face a minimum income tax. — [Lei 15.270/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm)
- **INSS from January 2026 [P].** Contribuinte individual: 20% on income between R$1,621.00 and R$8,475.55 (the ceiling). Simplified plan: 11% on the minimum wage (R$178.31). MEI: 5% (R$81.05). Employees: 7.5–14% progressive. The minimum wage is R$1,621. — [INSS](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-contribuicao-mensal)
- **Lei 10.666/2003, art. 4 [P].** Companies must withhold and pay the social-security contribution of contribuinte-individual providers working for them; this is the mechanism used for pró-labore. — [Lei 10.666](https://www.planalto.gov.br/ccivil_03/leis/2003/l10.666.htm)
- **Minimum wage 2026 [S].** R$1,621 (Decreto 12.797/2025). — [SBT News](https://sbtnews.sbt.com.br/noticia/brasil/lula-assina-decreto-que-estabelece-salario-minimo-em-r-1-621-a-partir-de-1-de-janeiro-de-2026)
- **Tax reform: export immunity (LC 214/2025) [P].** Art. 79: exports of goods and services are immune from IBS and CBS, with credits kept. Art. 80: exporting a service or intangible means supplying a resident abroad with consumption abroad. **§1º-A, added by LC 227/2026,** defines consumption abroad as a supply whose place of operation is not Brazil, or, in other cases, one where "o adquirente e o destinatário sejam residentes ou domiciliados no exterior." Under §5º, only the portion consumed abroad counts as export. — [LC 214](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm)
- **Tax reform: 2026 test year (LC 214/2025, arts. 343, 346, 348) [P].** In 2026, IBS is charged at 0.1% and CBS at 0.9%, offsettable against PIS/Cofins (or offset or refunded otherwise). These rates "não serão aplicadas em relação às operações dos contribuintes optantes pelo Simples Nacional" (art. 348, III, c). Payment is waived for taxpayers who meet the accessory obligations (§1º). — [LC 214](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm)
- **Simples companies and IBS/CBS from 2027 [S].** Simples companies may opt to pay IBS/CBS under the regular regime, outside the Simples payment (CRCMG presentation). Fenacon reported on 2026-09-21, headline only, that Simples companies will be able to revise their IBS/CBS option once the rate is defined. — [CRCMG](https://crcmg.org.br/wp-content/uploads/2025/10/REFORMA-TRIBUTARIA-_OS-DESAFIOS-E-AS-OPORTUNIDADES-DO-CONTADOR-POUSO-ALEGRE.pdf); [Fenacon](https://fenacon.org.br/noticias/empresas-do-simples-poderao-rever-opcao-pelo-recolhimento-de-ibs-e-cbs-apos-definicao-de-aliquota/)

### Inferences
Worked examples (computed from the tables above; ME figures exclude accountant fees):

| Scenario | CPF (Carnê-Leão + INSS) | ME, Anexo III with Fator R | ME, Anexo V, minimum pró-labore |
|---|---|---|---|
| **US$1k MRR (R$5,400/month)** | IR ≈ R$150 (2.8%). If INSS 20% is due: ≈ R$1,117 total (20.7%) | Domestic ≈ R$502 (9.3%). Export ≈ R$343 (6.4%) | Domestic ≈ R$1,015 (18.8%). Export ≈ R$755 (14.0%) |
| **US$5k MRR (R$27,000/month), all export** | IR + INSS ≈ R$7,745 (28.7%) | ≈ R$2,915 (10.8%) | ≈ R$3,132 (11.6%) |

- **CPF route assumptions.** IR uses the simplified discount, and the INSS line assumes the 20% contribuinte-individual rate applies. INSS is likely mandatory for someone running a for-profit activity on their own account, but verify this.
- **US$1k MRR, ME with Fator R.** Pró-labore equals the minimum wage, R$1,621, which is 30% of revenue and meets the 28% rule. Domestic: Simples 6% (R$324) plus 11% INSS on the pró-labore (R$178). Export: Simples about 3.05% (R$165) plus R$178. The 11% pró-labore rate is standard practice but was not verified in primary text.
- **US$5k MRR, ME with Fator R.** Simples about 4.23% on exports (R$1,142), plus INSS (R$832) and IR (R$942) on a R$7,560 pró-labore (28% of revenue). Most of the pró-labore is the founder's own take-home pay.
- **Fator R breakpoint.** A minimum-wage pró-labore satisfies the 28% rule only while monthly revenue stays at or below about R$5,789 (1,621 ÷ 0.28). Above that, the pró-labore must rise with revenue, or the company drops into Anexo V. Run both scenarios monthly with the accountant.
- **Conclusion.** Open an ME under Simples once revenue is recurring and expected to exceed about R$3–5k/month. Do not use an unrelated MEI occupation as a workaround, because it is a compliance risk.
- **Merchant-of-Record nuance.** When selling through Paddle, the Brazilian company's customer is Paddle, a foreign acquirer. Under LC 214, §1º-A, IBS/CBS export immunity from 2027 also requires the *recipient* to be abroad. Sales to Brazilian end users routed through Paddle may therefore not count as exports. Ask the accountant.
- **IOF.** Ask the bank, Wise Business or Payoneer to book receipts as "exportação de serviços" so they get the 0% IOF rate under art. 15-B I rather than a generic 0.38%.

### Gaps
- The client's premise that software development was "removed" from MEI could not be confirmed. The evidence shows only that it is not currently permitted.
- The official MEI occupation list (Anexo XI of Resolução CGSN 140/2018) could not be retrieved. The gov.br page is dynamic, and Receita's normas site did not resolve. Tech-adjacent permitted MEI occupations therefore cannot be listed.
- Not verified in primary text:
  - the 11% INSS rate on pró-labore;
  - whether INSS is mandatory for a CPF selling software abroad;
  - whether the simplified discount applies inside Carnê-Leão.
- Accountant fees and CNPJ opening costs were not researched.
- Whether Siscoserv still applies (mentioned by a 2024 Wise blog) was not verified.
- Municipal ISS rules for SaaS exports vary and were not checked for any specific city.
- Deadlines and mechanics of the 2027 IBS/CBS option for Simples companies were not retrieved.

## 8. Minimum legal hygiene: terms of use, LGPD privacy policy, invoices (NFS-e) for Brazilian customers

### Takeaway
The minimum legal kit has five parts:
- Terms of use.
- An LGPD privacy notice covering the art. 9 disclosures.
- A data-subject contact channel. Small processing agents do not need a DPO.
- For consumer sales: a 7-day withdrawal and refund right, plus seller identification and full offer conditions on the site.
- National-standard NFS-e for every Brazilian sale. This has been mandatory for Simples companies via the Emissor Nacional since 2026-09-01.

### Cited Findings
- **LGPD, art. 9 [P].** Data subjects are entitled to clear, prominent information on: the specific purpose of processing; its form and duration; the controller's identity and contact details; shared use and its purpose; the responsibilities of the processing agents; and their rights, citing art. 18 explicitly. — [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- **ANPD Resolution CD/ANPD 2/2022 [P].** Small processing agents ("agentes de tratamento de pequeno porte") include micro and small companies, startups and natural persons. Under art. 11 they are not required to appoint an encarregado (DPO), but they must provide a communication channel with data subjects. Under art. 6, these exemptions do not waive LGPD principles or legal bases. — [DOU](https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-2-de-27-de-janeiro-de-2022-376562019)
- **Consumer code (CDC), art. 49 [P].** A consumer may withdraw within 7 days from a contract made outside a commercial establishment and must be refunded immediately. — [CDC](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm)
- **Decreto 7.962/2013, art. 2 [P].** E-commerce sites must prominently show: business name and CPF/CNPJ; physical and electronic address; the product's essential characteristics; any additional charges; and the full offer conditions (payment, availability, delivery or service timing). — [Decreto 7.962](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7962.htm)
- **NFS-e [S].** LC 214/2025, art. 62, required municipalities to adopt the national NFS-e standard by 2026-01-01. Resolução CGSN 189/2026 (published April 2026) makes national-standard NFS-e mandatory for Simples ME/EPP from 2026-09-01, issued exclusively through the Emissor Nacional (web or API). MEIs have used the national standard since 2023. — [COAD](https://www.coad.com.br/home/noticias-detalhe/137522/nfs-e-de-padrao-nacional-sera-obrigatoria-para-empresas-do-simples-nacional); [CRCMS](https://crcms.org.br/?p=36397); [Jornal Contábil](https://www.jornalcontabil.com.br/noticia/emissao-da-nfs-e-via-portal-nacional-a-partir-de-1-de-janeiro/)
- **Tooling.** Asaas issues NFS-e at R$0.49 per invoice. Paddle (and Gumroad since 2025-01-01) collect and remit foreign sales tax and VAT as merchant of record. — [Asaas](https://www.asaas.com/precos-e-taxas); [Paddle](https://www.paddle.com/pricing); [Gumroad](https://gumroad.com/pricing)

### Inferences
- **Privacy notice.** Publish short PT-BR and EN terms and privacy notices. List the third parties data is shared with (hosting, payments, analytics, LLM APIs) and give a privacy email as the contact channel.
- **Refunds.** Offer a 7-day no-questions refund on Brazilian sales. It is mandatory for consumers and cheap insurance against disputes (Stripe R$55, Polar US$15 per dispute).
- **Seller details.** Decreto 7.962 requires showing CPF/CNPJ and an address, which is another reason to open a CNPJ early rather than publishing a personal CPF and home address.
- **Invoicing.** Issue an NFS-e for each Brazilian sale (automated through Asaas). For export sales, issue NFS-e flagged as export. For Paddle payouts, invoice Paddle as the foreign customer; confirm with the accountant.

### Gaps
- The text of Resolução CGSN 189/2026 was not read directly.
- It was not verified whether an NFS-e is needed per Merchant-of-Record payout or per end customer.
- LGPD international-transfer rules (art. 33) for using US cloud and AI providers were not researched.
- Cold-email legality under the LGPD was not researched.

## 9. Synthesis for this client: ranked channels, 7–14-day validation protocol, minimum payment/legal/tax setup, realistic timelines

### Takeaway
With no audience and about R$700, the realistic order is:
1. **Distribution that already carries buyer intent:** a marketplace or app-store listing.
2. **Founder-led 1:1 selling** in the communities where the target users already gather.
3. **A free tool targeting long-tail "tool-intent" searches** as the compounding channel, using a small Brazilian Google Ads test as the validation instrument.

Collect money from day one: Pix or card links under the CPF, then an ME under Simples Nacional with Paddle for foreign buyers. Expect a first sale in weeks if validated, US$1k MRR in about 6–12 months, and US$5k MRR in about 18–30 months, for the minority of products that get there.

### Cited Findings
- Organic, referral, social and LLM signups convert best; paid signups convert worst. — [ChartMogul part 2](https://chartmogul.com/reports/saas-conversion-report-2/)
- Distribution in marketplaces is concentrated: the median Chrome extension has 18 users. Shopify has 16k+ apps and paid developers US$1B+ in 2024, takes 0% on the first US$1M of lifetime revenue, and charges a US$19 one-time registration fee. — [Konabayev/Exstats](https://konabayev.com/blog/extension-monetization-statistics-2026/); [Shopify changelog](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share); [Shopify docs](https://shopify.dev/docs/apps/launch/distribution/revenue-share)
- Small, personalized outreach outperforms blasts: lists under 50 recipients get 5.8% replies vs 2.1% for 1,000+, and advanced personalization gets about 17–18%. — [Woodpecker](https://woodpecker.co/blog/cold-email-statistics/)
- New pages rarely rank quickly (1.74–6.11% reach the top 10 within a year), and AI Overviews cut position-1 CTR by about 58%. — [Ahrefs ranking](https://ahrefs.com/blog/how-long-does-it-take-to-rank/); [Ahrefs AIO](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/)
- A free template library produced a "40x impact on our organic SEO" (anecdote). — [ChartMogul part 2](https://chartmogul.com/reports/saas-conversion-report-2/)
- Median time to US$1k MRR is about 8 months among those who reach it; the 2025 cohort's median MRR is US$168 [S]. — [Indie Hackers](https://www.indiehackers.com/post/it-takes-5-months-to-reach-1k-in-mrr-491742f806); [BigIdeasDB](https://bigideasdb.com/state-of-indie-saas-revenue-2026)
- Payment and tax building blocks:
  - Asaas: Pix and card, CPF accepted. — [Asaas](https://www.asaas.com/precos-e-taxas)
  - Paddle: Brazil supported, 5% + 50¢. — [Paddle](https://www.paddle.com/pricing)
  - Polar and Stripe Managed Payments are unavailable to Brazil-based sellers. — [Polar](https://polar.sh/docs/merchant-of-record/supported-countries); [Stripe](https://docs.stripe.com/payments/managed-payments/eligibility)
  - Simples Anexo III/V and the Fator R. — [LC 123](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm)
  - 0% IOF on export-revenue inflows. — [Decreto 6.306](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6306.htm)
  - IR exempt up to R$5k/month from 2026. — [Lei 15.270](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm)
  - National NFS-e mandatory for Simples companies from 2026-09-01 [S]. — [COAD](https://www.coad.com.br/home/noticias-detalhe/137522/nfs-e-de-padrao-nacional-sera-obrigatoria-para-empresas-do-simples-nacional)

### Inferences

**1. Ranked acquisition channels for this client** (my judgment from the evidence; costs are estimates):

1. **Marketplace or app-store-native product.**
   - *Where:* Nuvemshop app store (Portuguese-speaking Brazilian merchants; the developer can bill directly), Shopify App Store (global; US$19 one-time; 0% revenue share up to US$1M), or Chrome Web Store / WordPress.org if the tool is browser- or WordPress-native.
   - *Cost:* about R$0–150 (Shopify fee about R$100; Chrome Web Store one-time fee).
   - *Timeline:* 1–3 weeks to build and pass review (possibly several submissions). First installs within days of listing. First paying customer in about 2–8 weeks if the niche shows in-store demand (competitor apps with reviews, search suggestions).
   - *Expected conversion:* about 0.5–2% install→paid for extensions and WordPress; better with a card-required trial or platform billing.
   - *Main risk:* extreme concentration (median extension: 18 users) and Nuvemshop's manual post-trial billing friction.
2. **Founder-led 1:1 selling in existing communities.** This means Brazilian WhatsApp and Facebook groups of the target profession or SMB segment, plus Reddit, LinkedIn and Indie Hackers for English. It is value-first participation and personal DMs to people who voiced the problem, not cold-email blasts.
   - *Cost:* R$0.
   - *Timeline:* conversations within days; first payment in 1–4 weeks.
   - *Expected yield:* no benchmark exists. Plan on about 20–50 qualified conversations for 1–5 paying pilots. This is consistent with small, personalized outreach drawing 5.8–18% replies.
   - *Role:* the fastest route to the first R$ and to the first testimonials. It does not scale alone.
3. **Free tool or calculator plus long-tail "tool-intent" search, seeded by a small Brazilian Google Ads test.**
   - *Cost:* about R$50–100 for a domain (estimate) plus R$150–300 for the ads test.
   - *Timeline:* ads produce data within 3–7 days. Organic traffic is meaningful only after about 3–9 months (most pages never reach the top 10). Directory, G2-style and community mentions help both Google and LLM citations.
   - *Role:* the compounding channel that can carry the US$1k→5k leg, because organic and LLM signups convert best.
   - *Avoid:* thin programmatic pages, which fall under Google's scaled-content-abuse policy.
   - *Not recommended as primary channels:* Meta ads (cheap clicks in Brazil but lowest-quality signups), Product Hunt (wrong audience for Brazilian SMB; a one-day spike), YouTube and short video (no evidence, slow), and cold email at volume (client preference; replies about 3.4% and falling).

**2. Validation protocol for the first 7–14 days**
- **Days 1–2: demand scan, no code.** For 2–3 candidate problems, collect:
  - in-store demand: competitor apps or extensions with reviews and recent updates, and search-suggestion terms;
  - Keyword Planner volumes and CPCs for 20–50 long-tail pt-BR (and en-US) keywords;
  - 10+ threads or posts where target users complain about the job.

  Kill any idea with no paying competitors *and* no searches.
- **Days 2–4: one PT-BR landing page per surviving idea, built with Claude Code.**
  - Include a concrete promise, a screenshot or prototype, and a **visible price** (e.g., R$49–99/month or a one-time founder price).
  - Two calls to action: "Garantir vaga de fundador (pré-venda)" through a real Asaas or Mercado Pago Pix/card link under the CPF, with a 7-day refund guarantee; and "Entrar na lista."
  - Where feasible, ship the free calculator or generator as the hook.
  - Set up analytics with UTMs.
- **Days 3–10: traffic.**
  - (a) R$150–300 of Google Search Ads on exact- and phrase-match high-intent long-tail keywords in Brazil, aiming for ≥100 clicks per idea.
  - (b) 20–40 personal conversations or DMs in communities, offering the free tool or a short call.
  - (c) If marketplace-native, a minimal listing or "coming soon" page, or a free version, to read install velocity.
- **Days 7–14: pre-sell and decide.**
  - Offer a founding price (e.g., 3 months for the price of 1, or 50% off for life) to everyone who engaged.
  - Read results with the rule of three and Wilson intervals from section 4.
- **Decision rules:**

  | Decision | Condition |
  |---|---|
  | **GO** | ≥3 payments or deposits from strangers (or ≥R$300 collected), **and** ≥10% of targeted visitors joined the list, **or** ≥1–2% of ad clicks paid |
  | **ITERATE** (one more 7-day cycle on copy, segment or price) | 3–10% list conversion and 0–2 payments |
  | **KILL** | <3% list conversion after 100–150 targeted visitors **and** 0 payments after 20+ conversations |

**3. Minimum payment, legal and tax setup**
- **Phase A: validation and first payments (weeks 0–6, CPF).**
  - Open Asaas (or Efí Pro, or Mercado Pago) under the CPF for Pix and card payment links.
  - Publish a terms-of-use page and an LGPD privacy notice with a contact email (ANPD small-agent rule), plus a 7-day refund policy.
  - Report receipts monthly through Carnê-Leão (DARF due by the last business day of the following month). Income tax is zero up to R$5k/month of taxable income in 2026; check the INSS obligation.
  - For any early foreign buyer, use Gumroad (MoR, 10% + 50¢) rather than building tax compliance.
- **Phase B: recurring revenue (by about month 2–3, or before revenue exceeds about R$3–5k/month).**
  - Open an ME under Simples Nacional with an accountant. A likely CNAE is 6203-1/00 for licensing non-customizable software; 6311-9/00 is an option for hosting/SaaS if the accountant prefers it.
  - Set pró-labore at the R$1,621 minimum wage, which meets the 28% Fator R up to about R$5.8k/month of revenue. That puts the company in Anexo III at 6%, or about 3.05% on export revenue. Raise pró-labore or accept Anexo V as revenue grows.
  - Issue NFS-e through the Emissor Nacional (Asaas can automate it at R$0.49 per invoice).
  - Move Asaas, or Stripe BR if its API is wanted, to the CNPJ. Add Pix Automático once the CNPJ is old enough (Mercado Pago requires more than 6 months).
  - MEI is not an option for software, and Lucro Presumido is not needed at this scale.
- **Phase C: international sales (as soon as there is non-Brazilian demand).**
  - Apply to Paddle with the CNPJ: 5% + 50¢ as Merchant of Record, which handles VAT and sales tax.
  - Receive payouts in USD by SWIFT to a Brazilian bank or a Wise Business USD account, or via Payoneer. Set a payout threshold of ≥US$500 so the US$15 wire fee matters less.
  - Ask the receiving institution to book the inflow as service-export foreign exchange (0% IOF). Issue an export NFS-e, so Simples drops ISS, PIS and Cofins.
  - From 2027, IBS/CBS export immunity applies only if both the acquirer and the recipient are abroad. Check this for Brazilian buyers routed through Paddle.
  - Avoid Polar (no payouts to Brazil) and Stripe Managed Payments (no Brazil-based businesses). Treat Lemon Squeezy as risky (PayPal-only payouts to Brazil, and a migration toward Stripe Managed Payments).

**4. Realistic expectations to put in the report**
- **First sale:** about 2–8 weeks after the product reaches high-intent users. Many products never make one.
- **US$1k MRR:** about 6–12 months (the median is about 8 months among the minority who reach it; perhaps 1 in 4 do).
- **US$5k MRR:** about 18–30 months. It requires sustaining 10–15% net monthly growth and about 100–250 customers at US$20–50 ARPA, with about 6–15 new customers every month just to offset roughly 6% churn.
- **Pricing:** SMB tools at about US$20–50/month (R$49–149 in Brazil, inferred) shorten every one of these timelines. Sub-US$10 pricing lengthens them sharply, because of fixed transaction fees and the higher churn at low ARPA.

### Gaps
- No rigorous evidence ranks Brazilian WhatsApp or Facebook communities vs marketplaces vs search for first customers. The ranking above rests on mechanism and indirect data.
- Brazil Google Ads CPCs for the client's eventual niche are unknown until he checks Keyword Planner.
- No Nuvemshop app-store demand data.
- The costs of an accountant, CNPJ opening and a domain were not researched; the R$ amounts above are placeholders.
- The success probabilities cited (1 in 4 reaching US$1k MRR) come from small or self-selected datasets with unverified methodology.
