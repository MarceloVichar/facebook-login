# Niche licensing-exam prep built on official or public-domain material (US and Brazil), round 2

Method and dating: every page below was accessed on **2026-10-12** unless another date is given. Revenue figures marked "verified" come from TrustMRR pages that pull from the founder's payment processor. Autocomplete comes from `suggestqueries.google.com` (client=firefox; hl=en/gl=us or hl=pt-BR/gl=br) and shows **no volumes**. App counts and installs come from Google Play search and detail pages. Hotmart counts are the first results page (24 items), not the full catalogue.

Some numbers were taken from a search-engine result whose page I could not open (CBP, CQCS, ICPA and Kansas LPA pages were blocked or behind a login). Those are marked "(via search result)".

The exchange rate is R$5.4 per US$, the rate implied by the brief's R$700 ≈ US$130, so US$5k/month ≈ R$27k/month.

Tooling: 15 of the 15 allowed WebSearch calls were used. Mojeek returned 403. Reddit `.json` endpoints returned non-JSON (blocked). Udemy returned a Cloudflare challenge.

## Q1. Which exams pass the screen, and what survives deep validation?

### Takeaway
**No candidate is APPROVED.** Three survive as CONDITIONAL and were deep-validated (Q7–Q9):
1. Brazil's **Exame Nacional de Habilitação de Corretores de Seguros (FGV/ENS)**: high fees, a syllabus built on public law and SUSEP rules, one strong incumbent and almost no marketplace competition. Candidate volume is unknown.
2. The US **Customs Broker License Exam (CBLE)**: the past exams are federal works, the fee is US$390, pass rates are 13–34%, and the competitors are dated. The pool is only about 2.1–2.3k examinees a year, the next window is April 2027, and Paddle bans exam prep.
3. Brazil's **CFC Exame de Suficiência**: large volume (about 39–52k registrants per edition), but the field is crowded and the fee is cheap (R$130).

Every other listed exam is KILL (saturated, free substitutes, course-bundled or expert-dependent) or CONDITIONAL-low (US water/wastewater operators).

### Cited Findings
- Round 1 killed "niche certification prep" because Tree Nerd's moat is an expert author. Tree Nerd: US$220,593 total and US$34,768 in 30 days, founded 2025-12-04, verified via Stripe — [TrustMRR](https://trustmrr.com/startup/tree-nerd-academy)
- **Public question banks attract many cheap or free products, and revenue stays small.** Leben in Deutschland Test (German citizenship test prep): US$4,204 total, US$626 in 30 days, founded 2025-10-16 — [TrustMRR](https://trustmrr.com/startup/leben-in-deutschland-test). Life in the UK Pass Plus: US$26 total — [TrustMRR](https://trustmrr.com/startup/life-in-the-uk-pass-plus)
- **Templated "Exam Prep 2026" app farms already cover almost every US trade exam on Google Play.** Examples: "Water Operator Exam Prep 2026", "Wastewater Treatment Level 1–4", "Pesticide Applicator Exam", "NATE Practice Test 2026", "EPA 608 Exam Prep 2026", "ASE A-Series Test Prep 2026", "NMLS SAFE MLO Test Prep 2026", "Home Inspector Test Prep", "Backflow Tester Exam Prep", "CA/NY/AZ/IL/PA Notary Exam 2026" — [Play search "water treatment operator exam"](https://play.google.com/store/search?q=water%20treatment%20operator%20exam&c=apps&hl=en&gl=US), [Play search "notary exam"](https://play.google.com/store/search?q=notary%20exam&c=apps&hl=en&gl=US), [Play search "ase test prep"](https://play.google.com/store/search?q=ase%20test%20prep&c=apps&hl=en&gl=US)
- Those apps have tiny install counts:
  - com.testprep.awwa: 100+ installs, 7 reviews — [Play](https://play.google.com/store/apps/details?id=com.testprep.awwa)
  - ambitionz Water Treatment Level 1: 500+ — [Play](https://play.google.com/store/apps/details?id=co.ambitionz.app.watertreatmentlevel1practiceexam)
  - Top pesticide app: 1K+ installs, 55 reviews — [Play](https://play.google.com/store/apps/details?id=com.pesticide.applicator.flashcards)
  - NHIE prep app: 100+, 15 reviews — [Play](https://play.google.com/store/apps/details?id=com.testprep.nhie2)
- **The Brazilian insurance-broker exam has no exam-prep app in the top Play results.** All results were broker tools such as Bradesco Seguros Corretor, Corretores SUSEP and Azos — [Play search "corretor de seguros exame"](https://play.google.com/store/search?q=corretor%20de%20seguros%20exame&c=apps&hl=pt-BR&gl=BR)

### Inferences
**Master verdict table.** Scores run 1–5 on seven criteria: WTP evidence, low saturation, buyer power, distribution without contacts, buildability, speed to first revenue, low risk. As in Ranking.md, **the total misleads: the failing gate decides.**

| # | Exam | Mkt | WTP | Low sat. | Buyer | Distrib. | Build | Speed | Low risk | Total | Verdict | Deciding gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Corretor de seguros (FGV/ENS) | BR | 3 | 3 | 3 | 3 | 4 | 4 | 3 | **23** | CONDITIONAL (deep, Q7) | G8 volume unknown; G1 revenue unverified |
| 2 | CBP Customs Broker (CBLE) | US | 4 | 4 | 4 | 4 | 4 | 2 | 2 | **24** | CONDITIONAL (deep, Q8) | G8 small pool; speed (next sitting Apr 2027); G7 Paddle ban |
| 3 | CFC Exame de Suficiência | BR | 3 | 2 | 2 | 4 | 4 | 2 | 3 | **20** | CONDITIONAL-weak, leans KILL (deep, Q9) | G2 crowded; low ticket |
| 4 | Water/wastewater operator | US | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 21 | CONDITIONAL-low | G1 no paid-revenue proof; state fragmentation |
| 5 | Pesticide applicator (state) | US | 2 | 3 | 2 | 4 | 2 | 3 | 3 | 19 | KILL (deprioritized) | G1/G3 weak; 50+ state plans |
| 6 | NHIE (home inspector) | US | 3 | 2 | 3 | 4 | 2 | 3 | 2 | 19 | KILL | Proprietary content (expert again); free InterNACHI test |
| 7 | EPA 608 | US | 1 | 1 | 2 | 4 | 5 | 4 | 4 | 21 | KILL | G1: "free" dominates; 30+ apps |
| 8 | Backflow tester | US | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 18 | KILL (provisional) | Small pool; course/practical-driven (unverified) |
| 9 | Certified Pool Operator | US | 1 | 2 | 3 | 3 | 3 | 2 | 3 | 17 | KILL (provisional) | The credential is sold as a course |
| 10 | State notary exams | US | 2 | 2 | 2 | 4 | 4 | 4 | 4 | 22 | KILL | 28 Play apps; low-stakes exams |
| 11 | Insurance adjuster | US | 3 | 1 | 3 | 3 | 4 | 3 | 3 | 20 | KILL (provisional) | ExamFX brand in autocomplete; pre-licensing incumbents |
| 12 | ASE | US | 3 | 1 | 3 | 4 | 4 | 4 | 4 | 23 | KILL | G2: app saturation; US$62/test |
| 13 | NATE | US | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 19 | KILL (provisional) | App saturation |
| 14 | USPTO Patent Bar | US | 5 | 1 | 5 | 4 | 3 | 3 | 3 | 24 | KILL | G2: Wysebridge entrenched (free tier, 6,000+ students) |
| 15 | Revalida | BR | 5 | 1 | 4 | 4 | 2 | 3 | 3 | 22 | KILL | G2: Medway, MedCof, Estratégia MED, Descomplica |
| 16 | ANBIMA CPA / C-Pro R / C-Pro I | BR | 4 | 1 | 3 | 5 | 4 | 3 | 4 | 24 | KILL | G2: already saturated post-reform |
| 17 | Ancord | BR | 4 | 1 | 3 | 4 | 4 | 3 | 4 | 23 | KILL | G2 |
| 18 | Exame de Ordem (OAB) | BR | 4 | 1 | 2 | 5 | 3 | 3 | 4 | 22 | KILL | G2 (verified quickly) |
| 19 | Medical and other specialist titles | BR | 4 | 2 | 5 | 3 | 1 | 2 | 2 | 19 | KILL | Expert needed; Medway sells "Prova de Título" |
| 20 | CRECI | BR | – | – | – | – | – | – | – | – | N/A | No licensing exam found ("creci prova" means staff concursos) |

- **What reopens the round-1 kill.** Round 1 killed niche prep because content needed a hired expert. That premise holds only for exams whose source is proprietary (ISA, EBPHI, AWS codes). Where the exam is mostly statute and regulation that the public can reproduce (CBLE: 19 CFR and HTSUS; corretor exam: Lei 15.040/2024, DL 73/66, SUSEP circulars), a non-expert can write questions *with a citation per question*. Correctness is then checkable against the official text.
- **The public-material paradox.** A *fully published* question bank (citizenship tests, EPA 608, ham radio) invites free apps, and revenue collapses. The sweet spot is an exam where the **source law is public, but past questions are scarce or unpublished, and the law is long and recently changed.** The corretor exam has those properties; the CBLE has public past exams, but its skill is navigating a 1,000+ page reference under time pressure.
- **"AI exam coaches" stay killed.** The defensible value here is deterministic: the official-format mock engine, scoring rules such as FGV's "70% overall and no zero in any discipline", per-question legal citations, spaced repetition and readiness analytics.

### Gaps
- No search-volume numbers (Keyword Planner was not available); autocomplete shows only that a query exists.
- Install counts don't prove revenue. No verified revenue was found for any product in the three deep-validated niches.

## Q2. US candidates: candidate counts, fees, pass rates, official materials, competitors

### Takeaway
Most US trade exams named in the brief already have low-price app farms. They have cheap or bundled exams and fragmented state regimes, or (NHIE) content that is proprietary rather than public.

The best US structural fit is not on the original list. It is the **CBP Customs Broker exam**, a federal exam in which CBP writes the questions and posts the answer keys, with a US$390 fee. Water/wastewater operator exams are the only listed trade with low pass rates and a possible deterministic angle (math-problem generators), but there is no proof anyone pays.

### Cited Findings
**CBP Customs Broker License Exam (CBLE)**
- Fees and schedule:
  - US$390 exam fee and US$300 individual license application fee — [eCFR 19 CFR 111.96](https://www.ecfr.gov/current/title-19/section-111.96)
  - Given on the fourth Wednesday of April and October, and "prepared by Customs and Border Protection (CBP)" — [eCFR 19 CFR 111.13](https://www.ecfr.gov/current/title-19/section-111.13)
- Pass rates and volume:
  - October 2023: 34% pass rate, 1,141 people took it — [International Trade Today, 2024-02-27](https://internationaltradetoday.com/news/2024/02/27/October-Customs-Broker-Exam-Had-34-Pass-Rate-2402270045)
  - October 2024: seats offered to 1,045 candidates, 24% pass (via search result; PDF returned 403) — [CBP NGF issue paper, Dec 2024](https://cbp.gov/sites/default/files/2024-12/ngf_broker_modernization_issue_paper_-_dec_2024.pdf)
  - May 2024: 13% pass, per COAC (via search result) — [CBP NGF paper, Mar 2024](https://www.cbp.gov/sites/default/files/assets/documents/2024-Feb/NGF%20Broker%20Modernization%20Issue%20Paper%20-%20March%202024.pdf)
  - April 2026: 22% pass. CBP posted the answer key on 2026-05-13, and takers reported answer-recording discrepancies — [NCBFAA / ITT, 2026-05-13](https://ncbfaa.org/news-advocacy/ncbfaa-in-the-news/2026/05/18/cbp-reports-22--april-broker-exam-pass-rate-amid-answer-recording-issues--appeal-concerns)
- Competitors:
  - STR: 40 instructional hours plus 60+ homework hours; next course January 2027 for the April 2027 exam — [STR](https://www.strtrade.com/training/customs-broker-exam-preparation-course). Fee US$1,250 for the October 2026 course, and reference books cost about US$600–700 (via search result) — [STR event](https://www.strtrade.com/training/events/on-demand-webinar/balance-payment-virtual-customs-broker-exam-prep-course-for-the-october-2026-exam)
  - Leaphart CHB Exam Prep eCourse: US$325; remote class plus eCourse US$1,695. It uses PDF lesson guides and timed quizzes, says "Do not register using your phone", and references are bought separately — [Leaphart](https://id34145.securedata.net/leaphart/CHB.php)
  - GISTnet CB10u: US$699, text-based, built from past CBP exam questions; GISTnet claims a 75–85% pass rate for completers (via search result) — [ICPA post](https://www.icpainc.org/?p=104261)
  - A 12-week virtual course at US$995, listed January 2023 (via search result) — [Bigmarker](https://www.bigmarker.com/conferences/c2a64b05ed0b/reviews/new)
  - Google Play shows one relevant app, "Customs Broker Exam Prep" (installs not captured) — [Play](https://play.google.com/store/search?q=customs%20broker%20exam&c=apps&hl=en&gl=US)

**USPTO Patent Bar**
- Format: 100 questions in 6 hours; the electronic MPEP is allowed; historical pass rates 42.8% (2014) to 59.6% (2009) — [Wikipedia](https://en.wikipedia.org/wiki/USPTO_registration_examination)
- Wysebridge reports the national pass rate as 46% in 2025, 49% in 2024 and a 47% average for 2012–2025 — [Wysebridge annual reports](https://www.wysebridge.com/patent-bar-exam-annual-reports)
- Wysebridge itself:
  - Claims 6,000+ students since 2012, 3,000+ questions and an AI tutor — [wysebridge.com](https://www.wysebridge.com/)
  - US$594 one-pay or US$189/month; US$697 for "ONE"; a free tier with "four archived USPTO exam sessions" — [Wysebridge pricing](https://www.wysebridge.com/pricing)
  - Names PassPatentBar as a competitor — [Wysebridge vs PassPatentBar](https://www.wysebridge.com/wysebridge-vs-passpatentbar)
- The Play app "PATLOQ: Patent Bar AI Coach" also exists — [Play](https://play.google.com/store/search?q=patent%20bar%20exam&c=apps&hl=en&gl=US)

**NHIE (home inspector)**
- US$225 in all states except TX, OK, IL, SD and WA; 200 questions (25 pretest); scaled 200–800, pass at 500 (via search result) — [NHIE fee page](https://nationalhomeinspectorexam.org/?p=16551)
- A "55% national pass rate" appears only on boilerplate state pages of a third-party site, so it is unverified — [getlicensemap](https://getlicensemap.com/schools/home-inspector/new-jersey)
- No annual administration count was found.
- Autocomplete includes "internachi nhie practice test", "nhie practice exam free" and "home inspector exam secrets study guide" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=nhie%20practice)

**EPA 608**
- EPA describes Core and Types I, II and III; certification is through EPA-approved certifying programs — [EPA](https://www.epa.gov/section608/section-608-technician-certification-0)
- The second autocomplete suggestion is "epa 608 practice test free" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=epa%20608%20practice)
- Google Play shows 30 results, including "SkillCat: HVAC & EPA 608" — [Play](https://play.google.com/store/search?q=epa%20608%20exam&c=apps&hl=en&gl=US)

**ASE**
- 2026 fees: US$34 registration per order, US$62 per test, US$124 for L1–L4; four registration windows in 2026 (via search result from ase.com) — [ASE register](https://www.ase.com/register-now)
- Google Play has 10+ dedicated ASE prep apps — [Play](https://play.google.com/store/search?q=ase%20test%20prep&c=apps&hl=en&gl=US)

**NATE**
- Google Play shows "NATE Practice Test 2026", "HVAC Exam Prep 2026" and others — [Play](https://play.google.com/store/search?q=nate%20exam%20hvac&c=apps&hl=en&gl=US)
- Autocomplete: "nate practice test free / core / app / heat pump / 2026" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=nate%20practice)

**Water and wastewater operators**
- California wastewater, computer-based tests: H1 2024 had 188 / 202 / 150 / 37 / 79 examinees for Grades 1–5, with pass rates of 55 / 57 / 41 / 27 / 28%. There were about 6,253–6,496 certificate holders in H1 2024 — [CA Water Boards WWOCP stats](https://water.waterboards.ca.gov/water_issues/programs/operator_certification/docs/2024/wwocp-statistics.pdf)
- California wastewater received 465 online exam applications in H1 2026 — [CA WWOCP agenda, 2026-10-08](https://www.waterboards.ca.gov/water_issues/programs/operator_certification/advisory_com/docs/ww-advisory-agenda-092026-es.pdf)
- California drinking water: 20,014 valid distribution and 14,125 valid treatment certificates (Dec 2024). In H2 2023, distribution exams had 396 / 747 / 290 / 142 / 65 examinees for Grades 1–5, with pass rates of 58–67% — [CA DWOCP stats](https://water.waterboards.ca.gov/drinking_water/certlic/advisory_committee/docs/statistics.pdf)
- Kansas: 850 / 745 / 978 examinees in 2022 / 2023 / 2024, with pass rates of 50.7% / 51.5% / 45.5% (via search result) — [Kansas LPA audit](https://www.kslpa.gov/audit-report-library/water-certification-2/)
- Autocomplete: "water operator exam prep / practice test / questions", "wastewater exam cheat sheet pdf / formula sheet" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=wastewater%20exam)

**Pesticide applicators**
- About 489,000 private and 414,000 commercial certified applicators. Certification runs under state, tribal and federal-agency plans approved by EPA under 40 CFR 171. These are EPA October 2015 figures (via search result) — [EPA slides 2015](https://archive.epa.gov/epa/sites/production/files/2015-10/documents/ct-proposed-changes.pdf)
- California DPR examines and licenses many applicator categories and tells candidates to "review study materials before examination" — [CDPR](https://www.cdpr.ca.gov/docs/license/qal.htm)
- Autocomplete includes per-state queries: "pesticide license nc / nj / texas / illinois / florida", "qal exam prep course" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=pesticide%20license)

**Notary, adjuster, backflow and CPO**
- Notary: Google Play has 28 results, mostly state-specific notary exam apps — [Play](https://play.google.com/store/search?q=notary%20exam&c=apps&hl=en&gl=US)
- Adjuster: autocomplete includes "examfx adjuster license" and "adjuster exam pearson vue" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=adjuster%20exam)
- Backflow: Google Play has a single "Backflow Tester Exam Prep" app — [Play](https://play.google.com/store/search?q=backflow%20tester&c=apps&hl=en&gl=US)
- CPO: PHTA routes candidates to "Find a CPO Course" — [PHTA](https://www.phta.org/certifications/certified-pool-operator/)

### Inferences
- **CBLE.** The volume is about 2.1–2.3k examinees a year (two sittings of about 1,045–1,141), with pass rates of 13–34%. That is high stakes, but a small pool (detail in Q8).
- **Patent Bar is KILL.** It has a 13-year incumbent that gives away four archived official exams free and charges US$594–697. A newcomer would need a sharp angle, and no recent newcomer revenue was found.
- **NHIE is KILL.** EBPHI content is proprietary (no public past exams found), and the free InterNACHI practice test and pre-licensing schools absorb demand. It repeats round 1's "expert needed" problem.
- **EPA 608, notary, ASE and NATE are KILL.** They are low-ticket exams (ASE US$62/test), and the app farms are already there.
- **CPO and backflow are KILL (provisional).** The credential is bought as a course or practical, so standalone prep has little role.
- **Water/wastewater is CONDITIONAL-low.** Volumes per state are modest (California, the biggest program, has about 1.2k wastewater and roughly 3–4k drinking-water examinees a year, inferred from half-year counts). Grades 3–5 pass at only 19–41%, and math dominates the exams. A deterministic formula-problem generator is a genuinely non-AI product.
  - Cheapest test: a free "wastewater math drill" page targeting the "formula sheet / cheat sheet" queries, plus about US$50 of Google Ads. Pass: at least 3% email capture and at least 5 pre-orders at US$49 in 14 days. Fail: under 2 pre-orders.
- **Pesticide is KILL (deprioritized).** It has 50+ separate certification plans, a top app with only 1K+ installs, and mostly employer-sponsored, low-wage buyers.

### Gaps
- Annual NHIE, ASE, NATE, EPA 608 and ABC volumes were not found; neither were notary fees (state pages are JavaScript-heavy) or backflow/CPO course prices.
- Copyright status of state extension manuals and Sacramento State OWP manuals was not verified.
- A candidate-confidentiality agreement for EBPHI/ASE/NATE was not checked.
- NMLS SAFE MLO, IRS Enrolled Agent, AWS CWI, NCCCO crane and FAA A&P show strong autocomplete (e.g. "nccco practice test free/app/pdf", "cwi exam questions and answers pdf", "free a&p mechanic practice test") but were **not validated**. They are leads for round 3: [Autocomplete NCCCO](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=nccco%20practice), [Autocomplete CWI](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=cwi%20exam)

## Q3. Brazil candidates: candidates per year, fees, legality of past exams, competitor census

### Takeaway
Brazil has the strongest candidate: the **insurance-broker habilitação exam**. It has R$550–2,200 fees, two exam bodies (FGV and ENS), a 2026 syllabus rewritten around the new insurance code, **near-zero Hotmart and app competition**, and one serious incumbent (TopInvest, R$997).

CFC has real volume (about 39–52k registrants per edition) but is crowded at low prices. Revalida, ANBIMA, Ancord and OAB are saturated, and medical specialist titles need experts.

### Cited Findings
**CFC Exame de Suficiência**
- Registrants per edition, from four CFC regional reports:
  - 51,779 registrants, 42,535 present, 11,382 approved (report posted 2026-09) — [CFC por-REGIAO 2026-09](https://cfc.org.br/wp-content/uploads/2026/09/por-REGIAO.pdf)
  - 47,377 registrants, 37,898 present, 19,078 approved (50.34% of those present) — [CFC por-REGIAO 2026-03](https://cfc.org.br/wp-content/uploads/2026/03/por-REGIAO.pdf)
  - 46,263 registrants, 4,607 approved (12.06% of those present) — [CFC por-REGIAO-2](https://cfc.org.br/wp-content/uploads/2026/03/por-REGIAO-2.pdf)
  - 38,619 registrants, 30,520 present, 9,435 approved (30.91%) — [CFC por-REGIAO-1](https://cfc.org.br/wp-content/uploads/2026/03/por-REGIAO-1.pdf)
  - Reports index — [CFC relatórios estatísticos](https://cfc.org.br/registro/exame-de-suficiencia/relatorios-estatisticos-do-exame-de-suficiencia/)
- Fee, banca and published materials:
  - Fee R$130.00, payable by 10 Aug 2026 — [CFC](https://cfc.org.br/exame-de-suficiencia-anteriores/2o-exame-de-suficiencia-de-2025/); [FGV edital 2026.2](https://conhecimento.fgv.br/sites/default/files/concursos/cfc-edital-2026.2-08.07.2026.pdf)
  - FGV is the board for 2026.2 (written exam 28/09/2026). FGV publishes the question booklets and the answer keys — [FGV CFC 2026.2](https://conhecimento.fgv.br/exames/cfc/2026.2); [booklet tipo 1](https://conhecimento.fgv.br/sites/default/files/concursos/contador-cns001-tipo-1.pdf); [gabaritos](https://conhecimento.fgv.br/sites/default/files/concursos/cfc-20262-gabaritos-para-publicacao.pdf)
- Number of editions: CFC has a page titled "3º Exame de Suficiência de 2026", but its body text refers to "Edição n.º 1/2026", so the count of 2026 editions is unclear. Autocomplete suggests "exame cfc 2026.3" — [CFC](https://cfc.org.br/exame-de-suficiencia-anteriores/3o-exame-de-suficiencia-de-2026/); [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=exame%20cfc)
- Competitors:
  - Hotmart's first page shows 24 CFC products: preparatory courses, "Jornada 10x Exame CFC", "Intensivo CFC 4D", annotated past-exam ebooks, mind maps; R$297 seen — [Hotmart "exame cfc"](https://hotmart.com/pt-br/marketplace/produtos?q=exame%20cfc)
  - "Simulado Suficiência Contábil" has 50K+ installs — [Play](https://play.google.com/store/apps/details?id=com.id.cfcsimulated). "Simulados CFC" has 1K+ installs, 4.8★ and in-app purchases — [Play](https://play.google.com/store/apps/details?id=com.aplicativoslegais.simuladoscfc)
  - Autocomplete surfaces Estratégia Concursos, Gran Cursos, QConcursos, Aprova Concursos and "curso gratuito exame cfc" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=curso%20exame%20cfc)

**Insurance-broker habilitação (FGV and ENS)**
- FGV 2026.2 rules and fees:
  - Areas: Capitalização R$550, Vida e Previdência R$550, Danos R$1,100, all three R$2,200
  - Questions: 50 / 50 / 100
  - Pass: at least 70% across the area's disciplines and no zero in any single discipline
  - Online and remote, monitored by webcam
  - Annex 6 lists the syllabus and its references
  - Source: [FGV regulamento 2026.2](https://conhecimento.fgv.br/sites/default/files/editor_uploads/01.09.2026_regulamento_seguros_2026.2.pdf)
- The Annex 6 references are statutes and regulator texts: "Lei 15.040 de 09 de dezembro de 2024", "Decreto-Lei 73 de 1966", "Circular SUSEP nº 682", 620, 621 and 662/2022, Lei 14.133/2021 and Portaria PGFN 2.044/2024. Lei 15.040/2024 is labelled "Novo Código de Seguros" — [FGV regulamento 2026.2](https://conhecimento.fgv.br/sites/default/files/editor_uploads/01.09.2026_regulamento_seguros_2026.2.pdf)
- The 9th FGV exam: registration until 23 Nov 2026, exams on 5–6 Dec 2026, final result 10 Jan 2027; it is required to practise — [Revista Apólice, 2026-09-30](https://revistaapolice.com.br/?p=142981)
- Past FGV fees, by edition:
  - 8th edition (Dec 2025): R$499 / R$999 / R$1,900, payable in 10 instalments. Its free "Curso de Formação" bonus "não é preparatório para o Exame" — [Revista Apólice, 2025-11-20](https://revistaapolice.com.br/2025/11/ultima-semana-para-inscricao-no-viii-exame-fgv-de-corretores/)
  - 7th edition: July 2025 — [Revista Apólice, 2025-06-24](https://revistaapolice.com.br/?p=122099)
  - 5th edition (2024): R$500 / R$1,000 — [InfoMoney, 2024-04-09](https://www.infomoney.com.br/?p=2426867)
- ENS 2025 fees: R$528 (Capitalização), R$528 (Vida e Previdência), R$1,056 (Danos), R$2,013 (all).
  - ENS and FGV together run exams "três vezes ao ano", and passing one area gives 2 years to pass the rest.
  - TopInvest sells a "Curso SUSEP" at R$997 one-time (12× R$83.08) or R$99.90/month, with 1,290+ questions, 190+ lessons and the promise "Passe em 60 dias", marketed as "Certificação SUSEP / ENS". The blog page was modified 2026-06-30.
  - Sources: [TopInvest blog](https://www.topinvest.com.br/blog/como-e-a-prova-da-susep); [TopInvest curso SUSEP](https://www.topinvest.com.br/cursos/susep/)
- Hotmart census:
  - "corretor de seguros exame" and "habilitação corretor de seguros" return no exam-prep products. The "susep" search surfaces "Simulado Prova SUSEP Corretores de Seguros DAMPS" and "Primeiros passos para se habilitar na SUSEP"; the rest are concursos for SUSEP staff — [Hotmart "susep"](https://hotmart.com/pt-br/marketplace/produtos?q=susep); [Hotmart "corretor de seguros exame"](https://hotmart.com/pt-br/marketplace/produtos?q=corretor%20de%20seguros%20exame)
- Pool:
  - 86,256 active individual (PF) corretores out of 151,568 active registrations, with 65,312 companies, as of 2026-09-22
  - 9,043 registrations in 2026 to that date; "Susep registrou 3,1 mil corretores em 90 dias"
  - The PF series rose from 83,732 (Jan 2026) to 85,005 (22 Jul 2026)
  - A conflicting 88,236 figure appears on 2026-08-03
  - All via search result; CQCS blocked scraping — [CQCS, 2026-09-24](https://cqcs.com.br/noticia/susep-registrou-31-mil-corretores-em-90-dias/); [CQCS, 2026-07-22](https://cqcs.com.br/noticia/mercado-alcanca-marca-inedita-de-85-mil-corretores-pessoas-fisicas/)
- Regulatory change: a CNSP vote of 2026-07-10 approves a consolidated resolution. It revokes 13 CNSP resolutions and keeps habilitação by "curso ou exame" at SUSEP-authorized institutions. It eases entry for new institutions ("fomento à concorrência"), allows "habilitação específica" per segment and takes effect 180 days after publication — [CNSP Voto 2](https://www.gov.br/susep/pt-br/arquivos/arquivos-dos-documentos-e-publicacoes/votos/10-07-2026/voto-2-cnsp-corretores-assinado-1-1.pdf/@@display-file/file)
- Autocomplete:
  - "prova corretor de seguros pdf / 2026 / fgv / ens / susep", "simulado susep corretor de seguros" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=prova%20corretor%20de%20seguros)
  - "curso corretor de seguros susep / ead / fgv / gratuito / ens / valor" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=curso%20corretor%20de%20seguros)
  - "apostila corretor de seguros pdf" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=apostila%20corretor%20de%20seguros)

**Revalida**
- Fees: R$410 for stage 1 and R$4,106.09 for stage 2 (R$4,516.09 minimum). Medway sells Intensivo/Extensivo Revalida and "CRMedway Revalida" — [Medway](https://www.medway.com.br/conteudos/taxas-e-custos-do-revalida/)
- Stage 1 of Revalida 2026.2 used "as mesmas questões utilizadas no Enamed 2026"; the cut-off is 60 points — [MedCof](https://grupomedcof.com.br/blog/edital-do-revalida-inep-2024-2-e-publicado)
- INEP publishes past exams and answer keys for 2011–2026, and gov.br content is under CC BY-ND 3.0 — [INEP provas e gabaritos](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/revalida/provas-e-gabaritos); [INEP Revalida (footer)](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/revalida)
- Competition: Google Play returns 50 results (Revalida Livre, RevalidApp, Revalidei, MedQando, Aprova Revalida…), and Hotmart's first page has 24 products (R$99.90 seen) — [Play](https://play.google.com/store/search?q=revalida&c=apps&hl=pt-BR&gl=BR); [Hotmart](https://hotmart.com/pt-br/marketplace/produtos?q=revalida)

**ANBIMA, Ancord, OAB and specialist titles**
- ANBIMA now lists CPA, C-Pro I and C-Pro R, plus "Transição: CPA-10, CPA-20 e CEA" — [ANBIMA](https://www.anbima.com.br/pt_br/educar/certificacoes.htm). Autocomplete: "cpa 20 agora é cpro r", "cpa 20 mudou de nome" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=cpa%2020)
- ANBIMA competition:
  - Hotmart already lists "C-Pro R Master", "C-Pro R Descomplicada", "C-Pro R Express", "Mentoria Certificação C-Pro R" — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos?q=c-pro%20r)
  - The TopInvest simulator app has 100K+ installs — [Play](https://play.google.com/store/apps/details?id=br.com.deen.stopinvest)
  - TopInvest courses cover CPA, C-Pro R/I, CFG, CGA, CGE, Ancord AI, CNPI, Abecip, Aneps, CFP and SUSEP — [TopInvest](https://www.topinvest.com.br/blog/como-e-a-prova-da-susep)
- Ancord: Hotmart's first page shows 24 products (aai-ancord, combo-cea-ancord, preparatorio-ancord…) — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos?q=ancord)
- OAB: Google Play returns 50 results (OABei, Estratégia OAB, Gabarita OAB…) — [Play](https://play.google.com/store/search?q=exame%20oab&c=apps&hl=pt-BR&gl=BR)
- Specialist titles: Medway's menu lists "Prova de Título | Extensivo TED | Extensivos TPI | Reta Final TECM" — [Medway](https://www.medway.com.br/conteudos/taxas-e-custos-do-revalida/). Autocomplete for "título de especialista" spans psicologia (CRP), fonoaudiologia and fisioterapia — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=t%C3%ADtulo%20de%20especialista)
- CRECI: autocomplete is "creci prova concurso / provas anteriores / prova online" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=creci%20prova)

**Other council and government exams (leads, not validated)**
- Despachante aduaneiro: Hotmart has "Preparatório para o exame de despachante aduaneiro 2026" and "Apostila prova para despachante aduaneiro 2025" — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos?q=despachante%20aduaneiro). Autocomplete: "exame despachante aduaneiro 2025" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=despachante%20aduaneiro%20exame)
- CFC EQT perito contábil: Hotmart has "mentoria coletiva premium EQT perito contábil 2026-2", "e-book EQT perito contábil" and others — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos?q=perito%20cont%C3%A1bil). Autocomplete: "exame perito contabil 2026" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=perito%20cont%C3%A1bil%20exame)

### Inferences
- **CFC volume.** At about 39–52k registrants per edition and at least two editions a year, there are about 80–150k registrations a year, including repeaters. Pass rates swing from 12% to 50% between editions, which feeds candidate anxiety, the pain to sell into.
- **Corretor is the best Brazil fit on paper:**
  - **Stakes:** the R$550–2,200 fee is 4–17× the CFC fee.
  - **Content:** the syllabus is statutes and regulator texts, which the law excludes from copyright (Q4).
  - **Reset:** the syllabus was rewritten around Lei 15.040/2024, so older question banks are likely stale.
  - **Competition:** no Hotmart or Play exam-prep competition; TopInvest is the only visible product, and it is ENS-branded.
  - **Unknowns:** candidate volume and pass rate.
- **Corretor pool, rough inference only.** About 3.1k SUSEP registrations per 90 days suggests about 12k a year (PF plus PJ). Exam candidates probably exceed approvals, so maybe 8–20k a year. Low confidence.
- **Revalida is KILL.** Stage 1 is now literally the ENAMED exam, which puts it inside the residency-prep economy (Medway, MedCof, Estratégia MED).
- **ANBIMA is KILL.** The CPA-10/20/CEA → CPA/C-Pro reform did **not** open a gap: Hotmart already has several C-Pro R products, and TopInvest updated within months.
- **CRECI is N/A.** The CRECI autocomplete points to concursos for council staff, not a licensing exam (inference; not verified against COFECI rules).

### Gaps
- No pass rates or candidate counts for the FGV/ENS broker exams (the FGV results site failed TLS verification; seguros.conhecimento.fgv.br has an incomplete chain) and no list of ENS 2026 dates.
- Revalida registrant counts were not found on INEP news pages.
- Exam counts for the CFC EQT, despachante aduaneiro, CNPI and CFP were not checked.
- CFC competitor revenue is not visible; Hotmart hides sales counts, and Udemy was blocked.

## Q4. Legal, ToS, platform and payment feasibility (G7)

### Takeaway
**Copyright:**
- US federal exam material (CBLE, USPTO) is public domain.
- Brazilian *statutes and regulator acts* are explicitly unprotected (Lei 9.610 art. 8 IV), so a bank of original questions that cite them is safe.
- *Questions written by FGV* are not obviously "atos oficiais". FGV's terms prohibit reproducing its platform content, so don't copy FGV questions verbatim.
- INEP content is CC BY-ND 3.0.

**Payments:** Paddle, round 1's default MoR for selling abroad, now **prohibits "Certifications and exam preparation services"**. A US-facing product needs Lemon Squeezy, Gumroad or Stripe instead. Brazil-facing sales via Hotmart, Kiwify or Asaas are fine.

### Cited Findings
- Lei 9.610/1998 art. 8: "Não são objeto de proteção como direitos autorais… IV - os textos de tratados ou convenções, leis, decretos, regulamentos, decisões judiciais e demais atos oficiais" — [Planalto](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm)
- 17 U.S.C. §105: "Copyright protection under this title is not available for any work of the United States Government" — [Cornell LII](https://www.law.cornell.edu/uscode/text/17/105). The CBLE is "prepared by Customs and Border Protection (CBP)" — [eCFR 111.13](https://www.ecfr.gov/current/title-19/section-111.13)
- gov.br (INEP) footer: "Todo o conteúdo deste site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada" — [INEP](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/revalida)
- FGV Conhecimento terms (2026-01-16): users must "Não reproduzir, duplicar, copiar ou vender qualquer parte da Plataforma…", and use of FGV marks and copyrights is "vedada… sem a expressa autorização" — [FGV termos de uso](https://conhecimento.fgv.br/sites/default/files/2026.01.16-termos-de-uso-fgv-conhecimento.pdf)
- **Paddle AUP, "Last Updated 13 April 2026".** Under "Prohibited Categories" it lists "Certifications and exam preparation services, including but not limited to: essay and paper mills, ghostwriting services; any certifications or courses for which the business is not the owner or creator of the underlying product, or does not have the authority to resell" — [Paddle AUP](https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle)
- Lemon Squeezy allows "digital goods that can be fulfilled through Lemon Squeezy's website", and its prohibited list doesn't name exam prep — [Lemon Squeezy](https://docs.lemonsqueezy.com/help/getting-started/prohibited-products). Gumroad's list (revised 2026-09-16) allows "courses, decks, guidebooks" — [Gumroad](https://gumroad.com/prohibited). Stripe's restricted list has no exam-prep entry — [Stripe](https://stripe.com/legal/restricted-businesses)
- Round 1 found that Lemon Squeezy pays Brazil only via PayPal and is steering users to Stripe Managed Payments, which doesn't serve Brazil. It also found that Asaas, Mercado Pago and Efí accept individuals (CPF) — [round-1 note gtm_economics_payments.md, section 6](../Oportunidade%20de%20produto%20validada%202026/gtm_economics_payments.md)
- Hotmart hosts many exam-prep products (CFC, CPA, OAB, Revalida), so the category is accepted there in practice — [Hotmart "exame cfc"](https://hotmart.com/pt-br/marketplace/produtos?q=exame%20cfc)

### Inferences
- **Safe content pattern for Brazil.** Write original questions, each with a mandatory link to the article of law, SUSEP circular or NBC it tests. NBCs are CFC resolutions, so they count as atos oficiais. Never import FGV or ENS question text, and use "FGV" only descriptively with a non-affiliation disclaimer.
- Whether exam questions written by a private banca under a public council's contract count as "atos oficiais" is **legally unsettled**. QConcursos-style aggregators reproduce them at scale, but that proves the practice, not legality.
- **CBLE is the cleanest legal case in this research.** Verbatim past questions plus their answer keys are federal works.
- **Paddle's ban removes the easiest MoR for US sales.** Lemon Squeezy (via PayPal, with platform-transition risk) or Gumroad are the fallbacks, and their Brazil payout terms are still unverified. This hurts the CBLE more than the Brazilian candidates.

### Gaps
- Gumroad's payout support for Brazil and whether Stripe Brasil accepts CPF accounts with international cards were not verified (the Stripe support page didn't render).
- No Brazilian court precedent on reproducing bancas' questions was found; the one search returned only commented exams.
- Candidate confidentiality and trademark rules of EBPHI, ASE, NATE and ISA were not checked.

## Q5. Verified-revenue exam-prep examples beyond Tree Nerd (TrustMRR)

### Takeaway
Verified exam-prep revenue is concentrated. Tree Nerd (expert content, US$220.6k) and an app whose slug suggests TCF Canada prep (US$184k) dominate. Everything else is under US$10k total, and products built on fully public question catalogues earn the least.

### Cited Findings
- freetcf: US$184,412 total, US$23,640 in 30 days, MRR US$23,887 (RevenueCat), founded 2025-07-01, Canada. TrustMRR shows only "Stealth Company", so the product is unconfirmed — [TrustMRR](https://trustmrr.com/startup/freetcf)
- Prep for Certs (IT certs): US$9,056 total, US$1,022 in 30 days, MRR US$351 — [TrustMRR](https://trustmrr.com/startup/prep-for-certs)
- Utility Arborist Flashcards: US$6,020 total, US$554 in 30 days — [TrustMRR](https://trustmrr.com/startup/utility-arborist-flashcards). Certified Arborist Theory: US$5,303 total, US$211 in 30 days — [TrustMRR](https://trustmrr.com/startup/certified-arborist-theory). TreeNerdAcademia (Spanish): US$2,225 total — [TrustMRR](https://trustmrr.com/startup/treenerdacademia-com). All belong to Tree Nerd's founder (per round 1).
- Passtia (CompTIA simulator, UK, subscription): US$4,731 total, US$469 in 30 days — [TrustMRR](https://trustmrr.com/startup/passtia)
- Leben in Deutschland Test: US$4,204 total, US$626 in 30 days — [TrustMRR](https://trustmrr.com/startup/leben-in-deutschland-test). CCAT Tests: US$2,319 total — [TrustMRR](https://trustmrr.com/startup/ccattests)
- Adjacent categories:
  - Dataford (tech-interview prep): US$196,512 total, US$45,821 in 30 days — [TrustMRR](https://trustmrr.com/startup/dataford-inc)
  - psg-cracked (consulting assessments, Shopify): US$76,951 total, but only US$129 in 30 days — [TrustMRR](https://trustmrr.com/startup/psg-cracked)
- AI-centric study tools are mostly small:
  - TestWhiz: US$11,658 total — [TrustMRR](https://trustmrr.com/startup/test-whiz)
  - QuizPrep: US$1,433 — [TrustMRR](https://trustmrr.com/startup/quizprep)
  - Prépa ECOS IA: US$2,083 — [TrustMRR](https://trustmrr.com/startup/prepa-ecos-ia)
  - PharmaStudy AI: US$737 — [TrustMRR](https://trustmrr.com/startup/pharmastudy-ai)
  - ExamReady (Austria): US$344 — [TrustMRR](https://trustmrr.com/startup/exam-ready)
  - Exam Predictor: US$51 — [TrustMRR](https://trustmrr.com/startup/exam-predictor)
- Excluded: ExamRipper (US$109,651 total) is an AI browser extension for students — [TrustMRR](https://trustmrr.com/startup/exams-online)

### Inferences
- The two big winners have either proprietary expert content (Tree Nerd) or a huge, urgent, immigration-driven pool (TCF, if the slug is accurate). Products on public catalogues with a captive pool (Leben in Deutschland) make about US$600/month.
- So "public material" lowers build cost but also the moat. Revenue needs high stakes, a thin or dated incumbent field, and a structurally hard exam (low pass rate). Of the three finalists, the CBLE and the corretor exam best show those traits.
- No Brazilian exam-prep product with verified revenue was found on TrustMRR.

### Gaps
- TrustMRR's full education category could not be paged (connection resets). The census used an earlier 792-startup dump plus slug pages. Starter Story and Hotmart sales figures were not available.

## Q6. Distribution without contacts: autocomplete demand, marketplaces, communities

### Takeaway
Every finalist shows commercial-intent autocomplete ("prep course", "practice test", "simulado", "2026"), and most also show "free" or "pdf" variants. Hotmart is a real channel in Brazil, judging by the number of products it hosts. App stores show weak paid demand for US trade exams. Communities could not be measured (Reddit was blocked).

### Cited Findings
- CBLE:
  - "customs broker exam prep / practice test / october 2026 / study guide pdf / pass rate / prep course / registration / questions and answers pdf" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=customs%20broker%20exam)
  - "customs broker exam reddit", "customs broker exam october 2025 reddit", "is the customs broker exam open book" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=customs%20broker%20exam%20reddit)
- CFC: "exame cfc 2026.2 / 2026.3 / 2027", "simulado exame cfc 2026", "preparatório exame de suficiência do cfc" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=exame%20cfc)
- Corretor: "prova corretor de seguros fgv / ens / 2026 / pdf", "simulado susep corretor de seguros" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=prova%20corretor%20de%20seguros). By contrast, "questões corretor de seguros" and "preparatório exame fgv corretor de seguros" returned **no** suggestions — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=quest%C3%B5es%20corretor%20de%20seguros)
- Patent Bar: "patent bar exam prep reddit / free / pli / workbook pdf" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=patent%20bar%20exam%20prep). The Wysebridge site links r/PatentBarExam — [wysebridge.com](https://www.wysebridge.com/)
- Old.reddit `about.json` for r/CustomsBroker, r/PatentBarExam, r/WaterTreatment and others returned non-JSON (blocked) on 2026-10-12. Subscriber counts are unknown.

### Inferences
- Corretor autocomplete is thinner than CFC's, a warning on volume. It still includes buying-intent words (simulado, curso, prova 2026) and named bodies (FGV, ENS).
- Contact-free channels per finalist:
  - **Corretor:** Google Ads plus SEO on "simulado/prova corretor de seguros", and Hotmart's affiliate marketplace.
  - **CBLE:** SEO and Ads on "customs broker exam practice test", plus Reddit, marketed to the 66–87% who fail each sitting.
  - **CFC:** SEO, Hotmart affiliates, Instagram study pages.

### Gaps
- No search volumes, CPCs or Reddit community sizes.

## Q7. Deep validation 1: Brazil corretor de seguros habilitação exam (FGV/ENS)

### Takeaway
**CONDITIONAL, and the best next test of all candidates.** Stakes are high, the content can be legally built from public law, prep competition is thin (one strong incumbent), and an exam window falls within weeks (5–6 Dec 2026). Two things are unknown: candidate volume, and whether a cheaper, FGV-specific product can take enough share from TopInvest to reach about R$27k/month.

### Cited Findings
- Fees, format and the scoring rule (70% overall, no zero per discipline): see Q3 — [FGV regulamento 2026.2](https://conhecimento.fgv.br/sites/default/files/editor_uploads/01.09.2026_regulamento_seguros_2026.2.pdf)
- Exam dates and online-remote delivery — [Revista Apólice, 2026-09-30](https://revistaapolice.com.br/?p=142981)
- Competitor prices and positioning:
  - TopInvest: R$997 or R$99.90/month, 1,290+ questions, "Certificação SUSEP / ENS" — [TopInvest](https://www.topinvest.com.br/cursos/susep/)
  - FGV's free bonus course "não é preparatório" — [Revista Apólice, 2025-11-20](https://revistaapolice.com.br/2025/11/ultima-semana-para-inscricao-no-viii-exame-fgv-de-corretores/)
  - Hotmart has 2 marginal products (DAMPS simulator, "Primeiros passos") — [Hotmart "susep"](https://hotmart.com/pt-br/marketplace/produtos?q=susep)
- Pool context: 86,256 active individual brokers and about 3.1k registrations per 90 days (via search result) — [CQCS](https://cqcs.com.br/noticia/susep-registrou-31-mil-corretores-em-90-dias/)
- Regulation: the consolidated CNSP rule comes 180 days after publication and adds segment-specific habilitação — [CNSP Voto 2](https://www.gov.br/susep/pt-br/arquivos/arquivos-dos-documentos-e-publicacoes/votos/10-07-2026/voto-2-cnsp-corretores-assinado-1-1.pdf/@@display-file/file)

### Inferences
- **Product.** A web app ("Simulado Corretor 2026") with:
  - Three area modules, each mapped to Annex 6, with every question citing a law or circular article (DL 73/66, Lei 15.040/2024, SUSEP circulars)
  - Timed mocks in the exact format (50/2h, 50/2h, 100/4h)
  - A scorer that applies FGV's "70% overall, no zero in any discipline" rule
  - Spaced repetition and per-discipline readiness analytics
  - A "Novo Código de Seguros" diff module
  - ENS-format mocks as a second track
- **Buyer.** Career changers and new hires at corretoras, paying R$550–2,200 per attempt. Pool estimate: about 8–20k candidates a year (low-confidence inference from registrations).
- **Pain.** High fee per attempt; two-day remote exam; a 2-year window to pass all areas; a rewritten legal base.
- **Competitor weaknesses.** TopInvest is a generalist finance-certification school selling an ENS-branded course at R$997, about twice what a focused simulator could charge. There is no Hotmart or app alternative, and FGV's own course is "not preparatory".
- **Demand.** Moderate autocomplete; volume unknown.
- **Acquisition.** Google Ads on "simulado/prova corretor de seguros"; a free 20-question Danos diagnostic as lead magnet; Hotmart affiliate listing; SEO pages per SUSEP circular.
- **Build.** Under 4 weeks for the engine. The bottleneck is about 600–900 verified questions; AI helps draft, and each question must pass a citation check against the official text.
- **Time to first revenue.** About 3–5 weeks if live by early November, before the 23 Nov registration deadline and the 5–6 Dec exam.
- **Unit economics (G8).** R$27k/month at about R$397 average one-time price (all-areas bundle R$497, single area R$247) is about 70 sales a month, or about 840 a year: 4–10% of the estimated pool. Margin is positive; Kiwify or Asaas fees run about 1–9% plus a fixed fee (round-1 note), and hosting is negligible. Reaching US$5k/month likely needs the ENS track too, plus a recurring "habilitação específica" refresh after the new CNSP rule.
- **Risks:**
  - Unknown volume
  - TopInvest discounting
  - Legal-accuracy errors (refund and reputation risk)
  - Rule change in 2027 (new segments, new exam providers)
  - FGV trademark use
  - Seasonality around the exam windows

**Gates:**
- **G1 PARTIAL.** Paid substitutes exist (TopInvest R$997, Hotmart simulators), but revenue is unverified.
- **G2 PASS-conditional.** One meaningful competitor; no newcomer revenue evidence.
- **G3 PASS.** Candidates already pay R$550–2,200 in fees.
- **G4 PARTIAL.** Autocomplete exists; volume is unknown.
- **G5 PASS.**
- **G6 PASS.**
- **G7 PASS.** BR seller, BR platforms, atos-oficiais content, no FGV text.
- **G8 UNPROVEN.**

**Cheapest test (about R$150–250, 3 weeks):**
1. File a free LAI request on Fala.BR to SUSEP for new individual habilitações or registrations per year, 2023–2026, by institution. Pass: ≥8,000 a year.
2. Check Keyword Planner volumes. Pass: ≥2,000 searches a month combined for the "simulado / prova / curso corretor de seguros" families.
3. Build a fake-door landing page with a free 20-question Danos diagnostic and a R$197 "Pacote Dezembro 2026" pre-sale (Kiwify), with R$150 of Google Ads before 23 Nov 2026. Pass: ≥10 paid pre-sales and ≥5% visitor-to-email. Fail: <3 sales.

**Scores:** WTP 3, low saturation 3, buyer power 3, distribution 3, buildability 4, speed 4, low risk 3 = **23/35**.

### Gaps
- FGV and ENS pass rates and candidate counts.
- ENS 2026–2027 dates.
- Whether ENS's own "curso de habilitação" path (habilitação without the exam) captures most entrants.
- The effective date of Lei 15.040/2024 (not verified this round).

## Q8. Deep validation 2: US CBP Customs Broker License Exam (CBLE)

### Takeaway
**CONDITIONAL.** Structurally it is the best fit found: federal public-domain questions and references, a US$390 fee, 13–34% pass rates, professional buyers and dated competitors at US$325–1,695. But the pool is about 2.1–2.3k examinees a year in two seasonal spikes. The next exam is 28 Apr 2027, so revenue comes in months, not weeks. And Paddle's ban complicates selling from Brazil.

### Cited Findings
- Fee, schedule and authorship (prepared by CBP) — [eCFR 111.96](https://www.ecfr.gov/current/title-19/section-111.96); [eCFR 111.13](https://www.ecfr.gov/current/title-19/section-111.13)
- Volume and pass rates:
  - Oct 2023: 1,141 takers, 34% pass — [ITT](https://internationaltradetoday.com/news/2024/02/27/October-Customs-Broker-Exam-Had-34-Pass-Rate-2402270045)
  - Oct 2024: 1,045 seats, 24% pass (via search result) — [CBP issue paper](https://cbp.gov/sites/default/files/2024-12/ngf_broker_modernization_issue_paper_-_dec_2024.pdf)
  - Apr 2026: 22% pass; answer key posted 2026-05-13 — [NCBFAA/ITT](https://ncbfaa.org/news-advocacy/ncbfaa-in-the-news/2026/05/18/cbp-reports-22--april-broker-exam-pass-rate-amid-answer-recording-issues--appeal-concerns)
- Competitors:
  - Leaphart US$325 / US$1,695, PDF-based — [Leaphart](https://id34145.securedata.net/leaphart/CHB.php)
  - STR US$1,250 and 100 hours of work — [STR](https://www.strtrade.com/training/customs-broker-exam-preparation-course)
  - GISTnet US$699, text-based (via search result) — [ICPA](https://www.icpainc.org/?p=104261)
- Payments: Paddle bans exam prep — [Paddle AUP](https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle)

### Inferences
- **Product.**
  - A simulator of all public past CBLE exams, with answer keys linked to the exact 19 CFR section or HTSUS heading.
  - A "reference navigation trainer": drills that time how fast you find the governing CFR paragraph or tariff line, the core skill of an open-reference exam.
  - Spaced repetition on missed rules, timed mocks at the official duration (not verified this round), and analytics by exam category.
- **Buyer.** Logistics and forwarding staff who want to become licensed brokers; firms often reimburse (unverified). Pool: about 2.1–2.3k examinees a year, some repeating.
- **Pain.** 66–87% fail each sitting, after paying US$390 and roughly US$600–700 for references.
- **Competitor weaknesses.** PDF and text formats, desktop-only registration, no adaptive review, high prices.
- **Demand.** Rich autocomplete, including "pdf", "reddit" and "october 2026".
- **Acquisition.** SEO for "customs broker exam practice test / questions and answers"; Reddit; Google Ads around the results releases (the April 2026 key was posted 2026-05-13) to target repeaters.
- **Build.** About 3 weeks. The source is public; explanations need care, but citations are deterministic.
- **Time to first revenue.** The October 2026 sitting (28 Oct 2026) closed registration about 30 days earlier, so the first realistic sales window is January–March 2027 for the 28 Apr 2027 exam.
- **Unit economics (G8).** US$5k/month (US$60k/year) at about US$449 is about 134 buyers a year, roughly 6% of all examinees and perhaps 8–10% of unique candidates. That is possible only as the category leader, and revenue would be lumpy (two spikes a year). Margin is positive (digital).
- **Risks:**
  - Small pool
  - CBP format changes (the modernization papers; answer-recording issues in 2026)
  - Payments: Lemon Squeezy via PayPal, or Gumroad
  - US sales-tax handling outside an MoR
  - Slow start

**Gates:**
- **G1 PASS-ish.** Three or more paid courses at US$325–1,695 exist for years; their revenue is unverified.
- **G2 PASS.** Few competitors, all dated; no newcomer revenue evidence.
- **G3 PASS.**
- **G4 PASS.** Autocomplete is rich; volume is unknown.
- **G5 PASS.**
- **G6 PASS.**
- **G7 PARTIAL.** The content is clean; Paddle is closed, alternatives are unverified for Brazilian payouts.
- **G8 BORDERLINE.**

**Cheapest test.** Publish one public past exam as a free timed simulator, with a US$199 "April 2027 full bank" pre-order on Lemon Squeezy or Gumroad. Spend US$100 of Google Ads plus Reddit posts between 15 Jan and 25 Mar 2027.
- Pass: ≥150 free users and ≥8 paid pre-orders.
- Fail: <3 paid.
- Before building, confirm a Brazil payout route (PayPal or Gumroad) in a 1-day account test.

**Scores:** WTP 4, low saturation 4, buyer power 4, distribution 4, buildability 4, speed 2, low risk 2 = **24/35**.

### Gaps
- Exact number of public past CBLE exams on cbp.gov (the site returned "Access Denied"; GISTnet's past-question basis and the posted 2026 answer key suggest they are published).
- Number of examinees in April 2026.
- Employer reimbursement rates.
- Whether CBP's broker continuing-education rules create a second buyer pool of licensed brokers (not checked).

## Q9. Deep validation 3: Brazil CFC Exame de Suficiência

### Takeaway
**CONDITIONAL-weak, leaning KILL.** It is the largest pool in this research (about 39–52k registrants per edition), and the board changed to FGV in 2026.2, a temporary incumbent weakness. But the category is crowded (24+ Hotmart products, a 50K+ install simulator, the big concursos schools). The fee is only R$130, buyers are students, and the next edition's date is unknown.

### Cited Findings
- Registrants and pass-rate swings (12–50%) — [CFC reports](https://cfc.org.br/registro/exame-de-suficiencia/relatorios-estatisticos-do-exame-de-suficiencia/)
- R$130 fee, FGV as board, published booklets and keys — [FGV CFC 2026.2](https://conhecimento.fgv.br/exames/cfc/2026.2)
- Competitors — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos?q=exame%20cfc); [Play](https://play.google.com/store/apps/details?id=com.id.cfcsimulated); [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=curso%20exame%20cfc)
- FGV terms on reproduction — [FGV termos](https://conhecimento.fgv.br/sites/default/files/2026.01.16-termos-de-uso-fgv-conhecimento.pdf)

### Inferences
- **Product.** An "FGV-style CFC simulator": original questions written to FGV's style, each citing NBC resolutions (atos oficiais); timed 50-question mocks; spaced repetition; analytics by syllabus block. Price about R$47–97.
- **Pool and G8.** R$27k/month at about R$97 is about 280 sales a month, or about 3.3k a year: roughly 2–4% of 80–150k annual registrations. The share is plausible, but the ticket is low and the incumbents are many.
- **Competitor weakness.** Many banks were built for the previous board's style; FGV's first CFC exam was 2026.2. That window closes as incumbents add "FGV" content.
- **Risks.** Price war; free QConcursos-type banks; legal ambiguity over FGV questions (avoid them); low buyer power.
- **Time to first revenue.** Months (the 2027.1 date is not published).

**Gates:**
- **G1 PASS.** Many paid products.
- **G2 FAIL-leaning.**
- **G3 WEAK.**
- **G4 PASS.**
- **G5 PASS.**
- **G6 PASS.**
- **G7 PASS** with original questions.
- **G8 PLAUSIBLE but competitive.**

**Cheapest test.** List a R$47 "Simulado FGV-CFC 2027.1" on Hotmart with affiliate commission, plus a free 10-question diagnostic, about 6 weeks before 2027.1.
- Pass: ≥60 sales in the last 30 days before the exam.
- Fail: <15.

**Scores:** WTP 3, low saturation 2, buyer power 2, distribution 4, buildability 4, speed 2, low risk 3 = **20/35**.

### Gaps
- Mapping of each CFC statistics PDF to its edition (the March 2026 uploads lack edition labels in the extracted text).
- Date of the next edition.
- Competitor sales volumes.
