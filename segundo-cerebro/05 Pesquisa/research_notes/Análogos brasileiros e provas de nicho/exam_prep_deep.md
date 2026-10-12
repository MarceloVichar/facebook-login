# Exam-prep deep validation, round 3: closing the SUSEP, Portugal and CBLE gates, plus a new-lead screen (research date 2026-10-12)

**Method and dating.** Every data point was accessed on **2026-10-12** unless another date is given.

- **SUSEP data.** Broker registration counts were pulled directly from SUSEP's public Power BI "Painel de Corretores de Seguros" (data stamped "Última Atualização: 12/10/2026 06:32:58"). I captured the panel's own `querydata` calls and re-issued them with a person-type and month breakdown.
- **Other sources.** Autocomplete comes from `suggestqueries.google.com` and shows no volumes. App data comes from the iTunes Search/Lookup API and Google Play pages. Hotmart, CBP, Gumroad and the IRN pages were rendered with headless Chrome.
- **Prior work.** This builds on round 2 (`Validação condicionais e novos focos/niche_exam_prep.md`, `portuguese_spanish_arbitrage.md`, `trustmrr_newcomers.md`); facts already established there are not repeated.
- **Currency.** R$5.4 per US$, so US$5k/month ≈ R$27k/month.
- **Search budget.** 12 of the 15 allowed WebSearch calls were used.

---

## Q1. SUSEP corretor exam (FGV/ENS): pool size, exam statistics, the CNSP 2026 rule, competitors and demand

### Takeaway
**The pool gap is closed, and the answer is bad for G8.** SUSEP's own panel shows only about **4,600–4,900 new individual (pessoa natural) broker registrations a year in 2023–2025**. That count covers *every* route to habilitação: the FGV or ENS exam, plus the FGV and ENS habilitação *courses*, which need no exam. Even if every new broker bought prep, about R$27k/month would need roughly 1,000+ sales a year at R$297, **about 20% or more of all new brokers**. That is not plausible against TopInvest. **Verdict: KILL as the US$5k/month bet.** It survives only as a small, fast-cash side test because the December 2026 exam window is close.

### Cited Findings
**Pool: new registrations per year, from the SUSEP panel (primary data)**
- **Panel headline (12 Oct 2026):** 169,370 registrations in total, 152,686 active (86,818 individuals, 65,868 companies). New registrations: **10,073 "No Ano" (2026 to date)**, 373 in the quarter and 373 in the month — [SUSEP Painel de Corretores (Power BI)](https://app.powerbi.com/view?r=eyJrIjoiNWM3OWIyNmQtNWRlNi00Njc3LTllYTctYTkwNjdlNTllNTdkIiwidCI6ImFlZmVkMDQ0LTg4ODctNDI1NS1hNWU5LThkNzgzOTc3MmI4OSJ9), linked from [SUSEP central de painéis](https://www.gov.br/susep/pt-br/central-de-conteudos/central-de-paineis/painel-corretores)
- **New registrations by year and person type.** Measure "Total de Registros (Série Temporal)" split by "Tipo de Pessoa", from the same panel's query API:

| Year | Individual (PF) | Company (PJ) | Total |
|---|---|---|---|
| 2020 | 3,965 | 5,371 | 9,336 |
| 2021 | 5,044 | 5,085 | 10,129 |
| 2022 | 4,749 | 5,038 | 9,787 |
| 2023 | **4,568** | 5,441 | 10,009 |
| 2024 | **4,890** | 5,835 | 10,725 |
| 2025 | **4,784** | 5,970 | 10,754 |
| 2026 (to 12 Oct) | **4,209** | 5,864 | 10,073 |

  Source: [SUSEP Power BI panel](https://app.powerbi.com/view?r=eyJrIjoiNWM3OWIyNmQtNWRlNi00Njc3LTllYTctYTkwNjdlNTllNTdkIiwidCI6ImFlZmVkMDQ0LTg4ODctNDI1NS1hNWU5LThkNzgzOTc3MmI4OSJ9)
- **PF registrations by month.**
  - 2025: Jan 688, Feb 331, Mar 223, Apr 333, May 272, Jun 278, Jul 400, Aug 500, **Sep 741**, Oct 357, Nov 321, Dec 340.
  - 2026: **Jan 649, Feb 563**, Mar 286, Apr 345, May 253, Jun 299, Jul 381, Aug 599, **Sep 667**, Oct (to the 12th) 167.
  - Source: same panel
- **Education of new PF registrants:**
  - 2025: 3,458 with a completed degree, 662 with an incomplete degree, 653 with secondary school.
  - 2026 to date: 3,053 / 591 / 558.
  - Source: same panel
- **Active registrations by line of business:** Seguros de Pessoas 150,604; Previdência 148,388; Capitalização 146,189; Microsseguros 142,341; Danos 117,417. One person can hold several habilitações — same panel
- **Open data.** SUSEP's Plano de Dados Abertos 2026–2028 (published September 2026) lists the "Corretores de Seguros" base as "Disponível no Portal? **Não**", content "(em trabalho)". Cataloguing on dados.gov.br was scheduled for March 2026, so the bulk CSV is still unpublished. The PDA notes the Painel de Corretores is the public window onto this base — [SUSEP PDA 2026-2028](https://www.gov.br/susep/pt-br/arquivos/arquivos-licitacoes-contratos/2026_09_set_pda_2026-2028.pdf/@@display-file/file)
- **dados.gov.br's API returned HTTP 401** without a token — [dados.gov.br API](https://dados.gov.br/dados/api/publico/conjuntos-dados?nomeConjuntoDados=corretores&pagina=1)

**Routes to habilitação besides the exam**
- **FGV runs a fully online "Programa de Habilitação" course.** The basic track is 130 hours across 3 modules and 9 disciplines; the "Basic +" track is 190 hours. Passing needs 70% attendance and 70% on each discipline's final assessment, and the course leads to the SUSEP habilitação certificate. In other words, it is a **course route that does not require the national exam** — [FGV regulamento EAD](https://conhecimento.fgv.br/sites/default/files/concursos/regulamento_do_programa_de_habilitacao_profissionais_do_mercado_de_seguros_-_ead1.pdf)
- **CNSP Resolution 493/2026 keeps both routes.** "A habilitação continua a ser obtida mediante aprovação em exame nacional ou em curso de habilitação promovido por instituições credenciadas" — [Demarest client alert](https://www.demarest.com.br/susep-consolida-marco-regulatorio-dos-corretores-de-seguros-e-reforca-autorregulacao-e-educacao-continuada/)

**FGV/ENS exam statistics**
- **Not published.** No source found gives registrants or pass rates per edition. News coverage gives only dates and rules. — [Revista Apólice, 2026-09-30](https://revistaapolice.com.br/?p=142981); [Legismap on the IX FGV exam](https://legismap.com.br/conteudos/artigos-e-noticias/inscricoes-abertas-para-o-ix-exame-nacional-para-corretores-de-seguros-da-fgv)

**CNSP Resolution 493/2026 (the July 2026 rule)**
- **Publication and effect:** published in the DOU on 21 Jul 2026, in force 180 days later (≈17 Jan 2027, per a law-firm calculation). It consolidates 13 earlier CNSP resolutions — [Lefosse](https://lefosse.com/noticias/alerta/cnsp-consolida-regras-sobre-corretores-de-seguros-entidades-autorreguladoras-e-instituicoes-de-ensino/); [LegisWeb Res. 493](https://www.legisweb.com.br/legislacao/?id=498563); [Monitor Mercantil](https://monitormercantil.com.br/norma-consolida-atuacao-de-corretores-de-seguros-e-entidades-autorreguladoras/)
- **Plena vs específica (art. 4):** it distinguishes "habilitação plena" (all segments) from "habilitação específica" (restricted segments), and allows SUSEP to create habilitações per line of business. The specific segments **still await later SUSEP norms** — [Demarest](https://www.demarest.com.br/susep-consolida-marco-regulatorio-dos-corretores-de-seguros-e-reforca-autorregulacao-e-educacao-continuada/)
- **Registration (art. 5):** a single national registration, which can be granted by SUSEP or by an autorreguladora — same source
- **Teaching institutions (art. 59):** they need a coordinator with at least a master's degree, defined course hours, a 70% minimum per discipline and auditable exams. The course must include Direito, Economia, Técnicas Comerciais, Ética and Gestão Empresarial (art. 64). The rule also requires continuing education — same source

**Competitors**
- **TopInvest:**
  - Price (via search result): R$970/year for the whole platform, or R$119.90/month, with "o maior banco de simulados para SUSEP". This differs from round 2's R$997 / R$99.90/month, so the price has moved — [TopInvest SUSEP](https://www.topinvest.com.br/susep)
  - YouTube: its videos lead the search, at about 7.5k–20k views each and 3–4 years old — [YouTube search "prova susep corretor de seguros"](https://www.youtube.com/results?search_query=prova%20susep%20corretor%20de%20seguros)
- **Other YouTube voices:** Mais Seguro (11.9k views on a 2025 "opções para tirar a SUSEP"), Safety Escola (720 views), beplus (20.8k) — same search
- **Hotmart:**
  - "SIMULADO PROVA SUSEP CORRETORES DE SEGUROS DAMPS" at US$14
  - Safety Escola "SUSEP DANOS" at US$444, with one rating of 3.0
  - Under "corretor de seguros", mostly sales and marketing courses (US$7–630)
  - Sources: [Hotmart "simulado susep"](https://hotmart.com/pt-br/marketplace/produtos?q=simulado%20susep); [Hotmart "corretor de seguros"](https://hotmart.com/pt-br/marketplace/produtos?q=corretor%20de%20seguros)
- **Exam bodies also sell courses:** FGV's own EAD course (above) and ENS's habilitação course (round 2)

**Demand (Google Autocomplete, pt-BR)**
- "simulado susep" → capitalização / demais ramos / vida e previdencia / 2025 / **topinvest** / corretor de seguros / ens
- "prova susep" → 2026 / corretor de seguros 2026 / 2026 valor / fgv 2026
- "exame susep" → 2026 / fgv / ens / valor / simulado
- "certificação susep" → valor / plena / ens / fgv / corretor / 2026
- "apostila corretor de seguros" → pdf / susep / ens
- "questões prova susep" → a single suggestion
- Source: [Autocomplete "simulado susep"](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=simulado%20susep)

### Inferences
- **The monthly peaks fit the exam calendar.** Jan–Feb and Aug–Sep follow the December and July exams. Peak months run about 600–740 PF registrations against a baseline of about 250–350, so the exam-driven excess is roughly 1,500–2,000 a year. That is a rough upper bound on exam *passers*: the baseline also includes course graduates and people who registered late. If candidates are 1.5–3× passers, **the exam-taking pool is about 2.5–6k a year.** This is a low-confidence inference.
- **G8 arithmetic.**
  - R$27k/month is R$324k a year. At a R$297 average ticket that is about 1,090 sales a year, or 20–45% of the estimated exam-taking pool.
  - At R$497 it is about 650 sales a year, or 11–26%.
  - Both shares are implausible against TopInvest's brand plus the free FGV/ENS course routes.
  - **A realistic ceiling is R$3–8k/month (US$0.6–1.5k)**, assuming 5–10% share at R$300–400.
- **CNSP 493 cuts both ways.**
  - (+) New segment-specific habilitações will create new, narrower syllabi that no incumbent covers yet.
  - (−) Segment habilitações will likely be cheaper and shorter, which lowers willingness to pay per buyer.
  - (−) More credentialed institutions will mean more course routes that bypass the exam.
  - (±) The continuing-education requirement opens a recurring market for the 86,818 active PF brokers, but it will probably require credentialed institutions; the detailed rules were not seen.
  - **Net:** neutral to slightly negative for exam prep until SUSEP publishes the segment norms. Those could become a 2027 opening.
- **Buyer power is good (G3).** About 72% of new PF registrants have a completed degree, and exam fees are R$550–2,200.

### Gaps
- FGV/ENS registrants and pass rates per edition. Fix: an LAI request on Fala.BR to SUSEP and FGV.
- The split of new brokers between the exam route and the course route.
- Whether "Total de Registros (Série Temporal)" dates a record by first registration or also counts re-registrations. The measure's DAX was not visible.
- The full text of CNSP Res. 493 (only law-firm summaries were read).
- Udemy was not checked; Cloudflare blocked it in round 2 and it was not retried.

---

## Q2. Portugal nationality test (Lei Orgânica 1/2026) and CIPLE A2: regulation status, who must take it, pool, competitors, payment routes

### Takeaway
- **The regulation is still unpublished on 2026-10-12.** The 90-day deadline lapsed around 17–19 Aug 2026. The IRN page has not changed since 22 May, and lawyers advise not filing until the regulation appears.
- **Brazilians do have to take it.** CPLP nationals are presumed to meet only the *language* half of art. 6(1)(c); the culture, history and symbols half and the rights-and-political-organization requirement (d) still apply.
- **A credible competitor launched in August 2026**: testenacionalidade.com, at €19–39, with 477 cited questions, web plus apps and Stripe. It has almost no traction yet.
- **Near-term pool risk.** The residence requirement rose from 5 to 7 years, which pushes the immigrant cohort out by 2 years.

**Verdict: CONDITIONAL.** Timing is still out of the founder's hands.

### Cited Findings
**Regulation status**
- **IRN (rendered page; "Informação atualizada a 22 maio 2026").** "Algumas destas alterações dependem de regulamentação complementar… tornando necessário proceder à alteração do Regulamento da Nacionalidade Portuguesa no prazo de 90 dias" — [IRN Nacionalidade](https://irn.justica.gov.pt/Nacionalidade)
- **DN Brasil, 19 Aug 2026.** "Já se passaram mais de 90 dias, mas os detalhes práticos… ainda não foram publicados pelo Governo". This covers proof of means of subsistence, of rights and duties, and the solemn declaration. "Questionado pelo DN Brasil, o IRN não respondeu." The previous amendment was *never* regulated either — [DN Brasil](https://dnbrasil.dn.pt/sem-regulamentao-nova-lei-da-nacionalidade-deixa-cidados-sem-saber-como-comprovar-novos-requisitos)
- **O Globo, 28 Aug 2026 (quoted in a forum).** The 90-day deadline "excedeu há quase dez dias", and the Ministério da Presidência did not respond — [O Globo via forum](https://oglobo.globo.com/blogs/portugal-giro/post/2026/08/aperto-na-cidadania-de-portugal-depende-das-regras-do-governo-que-ignora-prazo.ghtml); [Fórum Cidadania Portuguesa p54](https://forum.cidadaniaportuguesa.com/discussion/25893/noticias-sobre-cidadania-portuguesa-e-assuntos-correlatos/p54)
- **Forum, July 2026.** "Atualmente a orientação é não enviar os pedidos até que seja devidamente regulamentada." The new IRN application form already lists "Documento comprovativo do conhecimento suficiente da língua e da cultura portuguesas, da história e dos símbolos nacionais" — [Fórum: Novos formulários](https://forum.cidadaniaportuguesa.com/discussion/29256/novos-formularios-da-nacionalidade-deducoes)
- **No primary source shows a published decree or portaria** as of 2026-10-12. Two searches found none. A September guide says the test format "aguardava publicação em setembro de 2026", which is unconfirmed — [growinportugal, 2026-09-10](https://www.growinportugal.com/pt/news/portugal-s-overhauled-nationality-law-reaches-implementation-2026-09-10)

**Who must take it (law text)**
- **Art. 6(1):**
  - (b) 7 years of legal residence for CPLP and EU nationals, 10 for others;
  - (c) "Comprovarem, através de teste ou de certificado, conhecer suficientemente a língua e a cultura portuguesas, a história e os símbolos nacionais";
  - (d) know "os direitos e deveres fundamentais… e a organização política do Estado português";
  - (e) a solemn declaration.
  - Source: [Lei Orgânica 1/2026](https://www.madeira.gov.pt/Portals/25/Documentos/Legislacao/Lei_Organica_1_2026.pdf)
- **Art. 6(10):** "Presume-se que os nacionais de países de língua oficial portuguesa preenchem o requisito da **primeira parte** da alínea c)", that is, *language only*, unless their lack of command of Portuguese is manifest — same source
- **The competitor's reading agrees.** testenacionalidade.com states the test applies to "Naturalização — incluindo cidadãos brasileiros e da CPLP" and claims "Netos e bisnetos de portugueses: agora também fazem a prova". Applications filed up to 18 May 2026 stay under the old law — [testenacionalidade.com](https://testenacionalidade.com/)

**Pool**
- **Pending stock:** IRN had 515,334 pending applications at the end of H1 2025. In H1 2025, 121,460 applications were filed and 92,257 were granted — [Sábado](https://www.sabado.pt/portugal/detalhe/primeiro-semestre-de-2025-com-515-mil-pedidos-de-nacionalidade-pendentes)
- **Residence share:** 522k pending (September 2025); "entre 2018 e 2024, 16 por cento dos pedidos… diziam respeito a naturalização por residência". The IRN president expects residence-based applications to rise as about 1 million recently regularized immigrants become eligible — [ECO/Lusa, 2025-09-11](https://eco.sapo.pt/2025/09/11/irn-preve-aumento-de-pedidos-de-naturalizacao-nos-proximos-anos/)
- **Mix of filings:**
  - More than 1.5 million applications were filed in 2020–2025, and only 27% came from immigrants.
  - Of the pending stock: 20% residence-based naturalization, 12% grandchildren, 31% Sephardic.
  - Monthly applications fell 12.5% from 2024 to H1 2025.
  - Source: [VamoLáVer (Paulo Querido), 2025-07-09](https://vamolaver.substack.com/p/283-apenas-1-em-cada-5-pedidos-de)
- **Brazilian share:** the IRN says "a maioria dos pedidos de nacionalidade são oriundos de cidadãos brasileiros" (via search result) — [Sábado](https://www.sabado.pt/portugal/detalhe/primeiro-semestre-de-2025-com-515-mil-pedidos-de-nacionalidade-pendentes)
- **Context from round 2:** AIMA counted 493,622 Brazilian residents in 2025 — see `portuguese_spanish_arbitrage.md`

**CIPLE A2 / CAPLE**
- **CAPLE's statistics page shows only 2020:** 3,513 exams across all levels (1,766 in Portugal, 1,747 abroad). No later counts are published — [CAPLE Estatística](https://caple.letras.ulisboa.pt/estatisticas)
- **Autocomplete (pt-PT):** "ciple a2 resultados / exam dates 2026 / practice test / test examples with answers pdf" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-PT&gl=pt&q=ciple%20a2)

**Competitors and prices (fetched 2026-10-12)**
- **testenacionalidade.com (Edouard Baillot):**
  - Content: 477 questions, "cada uma com a explicação e a fonte ao lado"; 44 audio study cards; timed mocks of "40 perguntas em 30 minutos"; PT and EN.
  - Pricing, one-off: **€19 for 1 month, €29 for 3 months, €39 lifetime**, with a promise to update for free once the regulation is out.
  - Stack and press: checkout uses **Stripe**; covered by DN Brasil on 5 Sep 2026; last updated 6 Sep 2026.
  - Source: [testenacionalidade.com](https://testenacionalidade.com/)
  - Apps: the iOS app was released 2026-08-19 with **0 ratings** — [iTunes lookup](https://itunes.apple.com/lookup?id=6799622600&country=pt). Google Play shows **"10+" installs** — [Play](https://play.google.com/store/apps/details?id=com.testenacionalidade.app&hl=pt&gl=PT)
- **Other PT App Store entries, all with 0 ratings:**
  - "Teste Nacionalidade Portugal" (Ghaith Alshehabat, 2026-06-21)
  - "Cidadania Portuguesa QCM" (2026-06-19)
  - "Cidadania Portuguesa A2 CIPLE" (2026-07-27)
  - "CIPLE Prep" (€2.99, 2026-08-13)
  - "Master Cidadania" (2026-05-07)
  - The only app with traction is CitizHub (368 ratings), a tracker rather than prep.
  - Source: [iTunes "cidadania portuguesa" PT](https://itunes.apple.com/search?term=cidadania%20portuguesa&country=pt&entity=software&limit=15)
- **Hotmart sells nationality *process* guides to Brazilians:**
  - "NACIONALIDADE PORTUGUESA – FAÇA SOZINHO" R$197 (11 ratings, 5.0)
  - "GUIA NACIONALIDADE PORTUGUESA" US$167
  - "Tudo sobre o regulamento da Lei da Nacionalidade" US$12
  - Guides for netos and cônjuges US$29–42
  - Consultoria US$424–1,629
  - Source: [Hotmart "nacionalidade portuguesa"](https://hotmart.com/pt-br/marketplace/produtos?q=nacionalidade%20portuguesa)
- **YouTube attention is in the low thousands per video.** Examples: "IMIGRANTES COMPETEM POR NACIONALIDADE PORTUGUESA" (65k views), and "Nacionalidade Portuguesa para netos pode exigir prova de língua, histó…" (508 views) — [YouTube search](https://www.youtube.com/results?search_query=teste%20nacionalidade%20portuguesa)

**Demand (Autocomplete)**
- pt-PT: "teste de nacionalidade portuguesa" → "teste de lingua portuguesa para nacionalidade". "prova nacionalidade portuguesa" → **no suggestions**. "portuguese citizenship test" → practice / practice pdf / language test / without language test / "brazilian citizenship portuguese test"
- pt-BR: "prova cidadania portuguesa" → only "prova de vida"
- Source: [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-PT&gl=pt&q=portuguese%20citizenship%20test)

**Payment routes for EU buyers from a Brazil-based seller**
- **Paddle:** bans "Certifications and exam preparation services" (round 2) — [Paddle AUP](https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle)
- **Gumroad:**
  - Its prohibited list (rendered 2026-10-12) does not ban courses or exam prep, and allows "courses, decks, guidebooks" — [Gumroad prohibited](https://gumroad.com/prohibited)
  - **Brazil is absent from its bank-payout country list** (the list runs "…Bosnia and Herzegovina, Botswana, Brunei…"). For countries without bank deposits, "we offer PayPal transfers as the only payment option" — [Gumroad: Getting paid](https://gumroad.com/help/article/13-getting-paid)
  - Gumroad is the MoR (round 2).
- **Stripe Brasil:** 3.99% + R$0.39 per domestic-card transaction, "+ 2% para transações com cartões internacionais" — [Stripe BR pricing](https://stripe.com/br/pricing). It is not an MoR, so the seller carries EU VAT (round 2). The competitor uses Stripe.
- **Hotmart:** converts prices to the buyer's currency (per an InvoiceXpress guide) — [InvoiceXpress](https://invoicexpress.com/blog/hotmart-o-que-e-e-como-vender-nesta-plataforma/). One Portuguese complaint describes a purchase paid in euros via Multibanco — [Portal da Queixa](https://portaldaqueixa.com/brands/hotmart/complaints/hotmart-hotmart-nao-e-fiavel-1-151316726). No official Hotmart statement on EU VAT handling was found.
- **Lemon Squeezy:** per round 2, it does not list exam prep as prohibited, but it pays Brazil only via PayPal and is migrating to Stripe Managed Payments, which does not serve Brazil.

### Inferences
- **Pool arithmetic (low confidence).**
  - Historically, 16–20% of roughly 250k applications a year were residence-based, about **40–50k a year**. Add grandchildren (12% of pending) if they are also tested.
  - **The 5→7-year shift** (counted from the residence title, per guides) means 2026–2028 filers come from the smaller 2019–2021 arrival cohorts, so near-term filings will probably *fall* before the 2022–2024 regularization wave qualifies around 2029–2031.
  - Pending applications are grandfathered, so they are not buyers.
- **G8:** about €25 net per sale means about 180 sales a month (2,150 a year) for US$5k/month, which is about 4–6% of an assumed 35–50k testable filers a year. That is plausible only once the regulation exists *and* filings resume; before then it is near zero.
- **Competition is real but weak.** testenacionalidade.com did exactly what round 2 proposed, earlier and well (citations, audio, regulation-update promise). It has 10+ Play installs and 0 iOS ratings, so **G2 still passes**: no one has distribution. But the "first mover" edge is gone, and a Brazilian founder now competes on pt-BR SEO and diaspora channels, not on product.
- **CIPLE A2 is not the founder's market.** Its buyers are non-Lusophone (Brazilians are presumed to have the language), and the volume is small (3.5k CAPLE exams a year in 2020). Treat it at most as an add-on.
- **Payment route.** Gumroad works: it is the MoR for EU VAT, exam prep is allowed, and it pays out via PayPal to Brazil. Hotmart is the pt-BR-native alternative (Brazilian buyers already buy nationality guides there).

### Gaps
- The Diário da República search could not be rendered (JS app; an empty result). The "no regulation" finding relies on the IRN page, DN Brasil (19 Aug), O Globo (28 Aug) and a forum (through 28 Aug). **Nothing was found dated after 10 Sep 2026.**
- No Pordata or IRN 2025 annual series by type and nationality was retrieved.
- Whether grandchildren must take the culture test (only the competitor and a YouTube title claim it).
- testenacionalidade.com's revenue (no TrustMRR listing found).
- Gumroad's PayPal-to-Brazil fees and Hotmart's EU tax handling were not verified on primary pages.

---

## Q3. CBLE: pool, past-exam availability, competitors and timing

### Takeaway
**Confirmed on cbp.gov.** CBP posts **past exams with answer keys** (May 2024, Oct 2024, Apr 2025, Oct 2025 and Apr 2026 are on the current page). The exam is 80 questions in 4.5 hours with a 75% pass mark, and a new appeal threshold applies from April 2026. The next sitting is 28 Oct 2026 (registration closed 16 Sep), then April 2027. **Timing is viable:** October failers get results 2–3 weeks after 28 Oct, which gives a sales window from mid-November 2026 through April 2027. The pool, about 1–1.1k examinees per sitting, still caps G8.

### Cited Findings
- **Format:** "80 multiple-choice questions, and a score of 75 percent is required to pass… The exam lasts 4.5 hours… given electronically", at centralized facilities. The reference materials are HTSUS, 19 CFR, ACE CBP Form 7501 instructions, the Right to Make Entry directive and the ACE BRPD. A sample exam is uploaded 10 weeks before exam day — [CBP General CBLE Information](https://www.cbp.gov/trade/programs-administration/customs-brokers/license-examination-notice-examination/general-cble-information) (last modified 2026-01-27)
- **Schedule:**
  - Next exam 28 Oct 2026; registration ran 17 Aug–16 Sep 2026; final withdrawal 26 Oct.
  - "Exam Results Letters are emailed to examinees within two to three weeks."
  - Appeals: from April 2026, examinees within three questions of passing (≥57 of 80) may appeal up to four questions.
  - Source: [CBP CBLE page](https://www.cbp.gov/trade/programs-administration/customs-brokers/license-examination-notice-examination)
- **Past exams and keys posted:** May 2024, Oct 2024, Apr 2025, Oct 2025 and Apr 2026 (posted 05/2026), as PDFs — [CBP Past Exams and Answer Keys](https://www.cbp.gov/document/publications/past-customs-broker-license-examinations-answer-keys)
- **Licensed-broker CE:** "Complete your 20 hours of Continuing Education (CE) credits by January 31, 2027". CE is offered by CBP (free webinars) and by private providers under accreditation standards set by five partner entities — [CBP Continuing Education](https://www.cbp.gov/trade/programs-administration/customs-brokers/continuing-education) (modified 2026-09-28)
- **Competitors (via search results):**
  - STR US$1,250 (about 40 instructional hours + 60 hours of homework)
  - FCBF course US$1,199 for members / US$1,499 for non-members, in person or remote, needing 10 registrations to run
  - NY/NJ associations with a law firm US$550 (April 2026)
  - DB Schenker US$699, past-exam questions
  - Leaphart US$325 / US$1,695
  - Sources: [STR](https://www.strtrade.com/training/events/upcoming-webinars/virtual-customs-broker-exam-prep-course-for-the-october-2026-exam); [FCBF](https://fcbf.starchapter.com/meetinginfo.php?id=211); [GDLSK](https://www.gdlsk.com/prepare-for-the-april-2026-customs-house-broker-license-exam-online/); [DB Schenker](https://ts.dbschenker.com/?p=9322); [Leaphart](https://id34145.securedata.net/leaphart/CHB.php)
- **Pool (round 2):** 1,141 takers in October 2023 (34% pass), 1,045 seats in October 2024 (24%), 22% pass in April 2026 — see `niche_exam_prep.md` Q8
- **Autocomplete (en-US):**
  - "customs broker exam" → 2026 / prep / practice test / october 2026 / study guide pdf / pass rate / prep course / questions and answers pdf
  - "cble" → exam / exam 2026 / exam prep / registration / **past exams**
  - Source: [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=customs%20broker%20exam)

### Inferences
- **Public-domain content is confirmed:** 5 recent exams × 80 = 400 official questions with keys, plus older exams likely on CBP's archive. The value is not the questions, which are free, but **an interactive, timed, explained simulator with reference-lookup drills**. None of the competitors found offers one; they are cohorts, PDFs and text courses at US$325–1,499.
- **Free PDFs cap the price.** A US$149–249 product undercuts every incumbent while staying high-ticket.
- **G8 arithmetic.**
  - Net about US$220 per sale at US$249 after Gumroad's 10% + US$0.50 → about 23 sales a month (≈270 a year) for US$5k/month, **about 12% of about 2.2k examinees a year** (more of the unique candidates).
  - At US$399: about 14 a month (≈170 a year, ≈8%).
  - **This is a stretch; a realistic run-rate is US$1.5–3.5k/month averaged**, with spikes in Nov–Dec and Feb–Apr.
- **CE is not a quick add-on.** It needs accreditation through CBP's partner entities (fails G5 for now), and CBP offers free webinars.

### Gaps
- April 2026 examinee count; the exact list of older archived exams; competitor revenues and reviews (none found).

---

## Q4. New-lead quick screen (Brazil and US)

### Takeaway
**No new lead beats the three finalists.**
- **Brazil's despachante aduaneiro exam exists** (RFB/COANA edital 2026; online exam on 15 Nov 2026), but it has a R$80 fee, is open only to ajudantes with 2+ years' registration, and registration has closed. **KILL**, or at most a tiny timing play.
- **CFC EQT pools are small:** 75 perito approvals and 730 QTG approvals in 2025.2. **KILL.**
- **NMLS, FAA A&P, AWS CWI, NCCCO and EA are saturated or proprietary. KILL.**

### Cited Findings
**Brazil**
- **Despachante aduaneiro (EDITAL/COANA nº 01, 1 Sep 2026; Legalle Concursos):**
  - Eligibility: ajudantes with secondary school and **≥2 years in the Registro de Ajudantes**.
  - Registration 8–30 Sep 2026; fee **R$80** by DARF.
  - Exam **15 Nov 2026**, online and remote with monitoring: 60 questions (10 Portuguese, 5 English, 45 customs legislation and despacho).
  - Passers have 1 year to register.
  - Sources (via search result): [RFB edital PDF](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/setembro/publicado-edital-do-exame-de-qualificacao-tecnica-para-despachante-aduaneiro-2026/1-edital-de-abertura-e-inscricoes-coana-rfb-2026-legalle-concursos.pdf); [SouBrasília](https://soubrasilia.com/exame-despachante-aduaneiro-2026-inscricoes-edital-coana-prova-novembro/)
  - Competition: Hotmart already lists "Preparatório para o exame de despachante aduaneiro 2026" (round 2).
- **CFC EQT (CNAI auditors, perito contábil):**
  - Fee R$260 per exam; FGV is the exam body; booklets and answer keys are published.
  - The 2025.2 final list of approved candidates (21 Jan 2026), counted from the PDF: **QTG 730, CVM 328, perito contábil (QTG-PC) 75, SUSEP 11, PREVIC 8, BCB 7.**
  - Sources: [CFC 29º EQT](https://cfc.org.br/exame-de-qualificacao-tecnica/29o-exame-de-qualificacao-tecnica-e-12o-exame-de-qualificacao-tecnica-para-pericia-contabil/); [EQT 2025.2 aprovados PDF](https://cfc.org.br/wp-content/uploads/2026/01/cfc-eqt-2025.2-resultado-final-de-aprovados_09.01.2026.pdf)
  - 2026 editions (30º/13º and 31º/14º) are listed on the same page.
- **Banco Central certification:** the only BCB-specific professional exam found is the CFC's EQT-BCB module, with **7 approvals in 2025.2** (same PDF).

**US**
- **NMLS SAFE MLO:**
  - Official first-time pass rate **53% (as of 2024-12-31)** — [NMLS Test Performance](https://mortgage.nationwidelicensingsystem.org/knowledge/products/nmls/pubs/testingHbk/education/mlo_testing/mlo_test_faq/mlo_testing_hbk_testPerformanceData.html) (via search result; NMLS pages returned 403)
  - Competitors include Aceable, The CE Shop and estatepass.ai — [Aceable](https://mortgage.aceable.com/resources/pre-license/is-the-nmls-exam-hard-what-to-know-before-you-start-studying/); [CE Shop](https://arei.theceshop.com/blog/why-do-so-many-people-fail-the-mlo-test/); [estatepass.ai](https://www.estatepass.ai/mortgage/pass-rate/)
  - "NMLS SAFE MLO Test Prep 2026" app farms (round 2).
  - Autocomplete: "safe mlo test questions / cost / pass rate / practice / study guide" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=safe%20mlo%20test)
- **FAA A&P:** autocomplete "a&p written test prep / prep free / questions / reddit / codes" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=a%26p%20written%20test)
- **AWS CWI:** autocomplete "cwi exam questions and answers pdf / cost / schedule 2026 / pass rate / practice questions / part a" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=cwi%20exam)

### Inferences
- **Despachante:** a niche, irregular exam for people already in the trade, with a low fee and a pool that is probably in the low thousands at most (unknown). **KILL as a main bet.** A 5-week window to 15 Nov exists, but registration is closed, so only registered candidates can buy.
- **EQT:** about 1,100–1,300 passers per edition across modules, and perito alone is tiny. The R$260 fee and published FGV exams invite low-price competition. **KILL.**
- **BCB, ABNT and INMETRO:** no mass individual licensing exam was found for BCB, so **KILL**. ABNT/INMETRO technical certifications were not researched further (no individual mass-market exam identified) — treat as **KILL, unverified**.
- **NMLS:** saturated, and the mandatory 20-hour pre-licensing course from NMLS-approved providers bundles test prep. **KILL.**
- **FAA A&P:** the "prep free" intent, plus incumbents from memory (ASA Prepware, Dauntless, Gleim; not verified this round). **KILL.**
- **AWS CWI and NCCCO:** content depends on copyrighted codes (AWS D1.1/B5.1) or practical exams, which fails a public-material build. **KILL.**
- **Enrolled Agent:** expected to be saturated (Gleim, Surgent, Fast Forward Academy; not re-verified). **KILL.**

### Gaps
- The despachante candidate count and pass rate (the edital doesn't give them); the previous edition's date.
- FAA question-bank publication status, CWI and NCCCO pools, and EA competitor prices were not verified (search budget).

---

## Q5. Scorecards, gate verdicts, the best two, cheapest tests and MVP spec

### Takeaway
**No candidate is APPROVED.** The **best two are (1) the CBLE simulator and (2) the Portugal nationality-test prep**, both CONDITIONAL.
- **SUSEP is downgraded to KILL as the US$5k/month bet.** The pool is now measured at about 4.8k new PF brokers a year across all routes. It stays optional only as a R$150 cash test before the 23 Nov registration deadline.
- **The CBLE wins on gates now:** public-domain content, Gumroad allows exam prep, and a sales window opens in mid-November. Its ceiling is the pool.
- **Portugal has the larger long-run pool and the founder's language edge,** but it is still blocked by the regulation, and a competitor now exists.

### Cited Findings
(All evidence is in Q1–Q4 above. The tables below synthesize it.)

### Candidate records (concise)

| Field | A. CBLE simulator (US) | B. PT nationality-test prep | C. SUSEP corretor simulator (BR) |
|---|---|---|---|
| Product | Timed replica of the 80-question, 4.5-hour exam built on CBP's public past exams and keys. Reference-lookup drills (find the 19 CFR section or HTSUS heading against the clock). Explanations with citations, spaced repetition, analytics by topic | pt-BR/pt-PT web app and PWA for art. 6(1)(c)(second half) and (d): history, culture, symbols, rights and duties, State organization. Cited questions, audio cards, timed mocks, switch to the official format once regulated | FGV-format mocks (50/50/100 questions; 70% overall and no zero per discipline), questions citing articles of law |
| Buyer and pool | Logistics and forwarding staff; about 1.0–1.1k examinees per sitting, 2 sittings a year | Naturalization filers; historically about 40–50k a year by residence (16–20% of filings), with a near-term dip from the 5→7-year rule; Brazilians are the largest group | About 4.6–4.9k new PF brokers a year across all routes (SUSEP panel); exam-takers estimated at 2.5–6k |
| Pain | 66–78% fail (22% pass in Apr 2026); US$390 fee | €250 IRN fee lost if refused (per competitor); new, unregulated test | R$550–2,200 fee; 2-day remote exam |
| Competitors | STR US$1,250; FCBF US$1,199–1,499; GDLSK US$550; DB Schenker US$699; Leaphart US$325–1,695 | testenacionalidade.com €19/29/39 (Stripe, 10+ installs); about 5 apps with 0 ratings; Hotmart process guides R$197 / US$167 | TopInvest R$970/year or R$119.90/month; Hotmart DAMPS US$14; Safety Escola US$444; FGV/ENS course routes |
| Weakness of competitors | Cohort, PDF or text formats; expensive; no interactive simulator | No distribution yet; pt-PT/EN focus | One dominant brand; generalist |
| Demand signals | "cble past exams", "customs broker exam practice test / prep course / october 2026" | Thin: "teste de nacionalidade portuguesa", "portuguese citizenship test practice"; nothing for "prova…" | Rich: "simulado susep topinvest / ens / capitalização…", "prova susep fgv 2026" |
| Channel | SEO on "past exams / practice test", Google Ads, Reddit, post-results retargeting | pt-BR SEO, diaspora Facebook groups, YouTube, Hotmart affiliates | Google Ads, Hotmart |
| Build | 2–3 weeks | 2–3 weeks (plus content) | 3–4 weeks (600–900 cited questions) |
| Time to first revenue | Mid-November 2026, after October results (2–3 weeks after 28 Oct) | Unknown: days after the regulation, if a waitlist is ready | 3–5 weeks (registration closes 23 Nov; exam 5–6 Dec) |
| Key risks | Small pool; CBP format changes; free official PDFs; PayPal payout friction | Regulation delay; the state publishing free material; lower near-term filings; competitor | Pool cap; TopInvest; course routes; CNSP 493 changes |

### Gate-by-gate verdicts

| Gate | A. CBLE | B. PT nationality test | C. SUSEP |
|---|---|---|---|
| G1 WTP (≥2 paid) | **PASS**: 5+ paid courses at US$325–1,499 (revenue unverified) | **PASS (adjacent and analog)**: competitor at €19–39; Hotmart nationality guides R$197 / US$167; Francopass verified (round 2) | **PASS**: TopInvest, Safety Escola, DAMPS |
| G2 not saturated + newcomer could win | **PASS**: no interactive simulator found; incumbents are cohort- or PDF-based. No newcomer revenue proof | **PASS (weakened)**: the Aug 2026 entrant shows the slot is open but taken; nobody has traction | **PARTIAL**: one dominant brand, plus free course routes |
| G3 buyer power | **PASS** | **PASS (moderate)** | **PASS** (72% degree holders) |
| G4 distribution without contacts | **PASS**: commercial-intent autocomplete | **PARTIAL**: thin until the test is live | **PASS** |
| G5 MVP ≤4 weeks, no certification | **PASS** | **PASS** | **PASS** |
| G6 not AI-core | **PASS** | **PASS** | **PASS** |
| G7 legal/ToS/payment | **PASS (with friction)**: 17 USC §105 public-domain content; Gumroad allows it and pays out via PayPal | **PASS (with friction)**: Gumroad or Hotmart; no "official" claims | **PASS**: Hotmart/Kiwify; cited content only |
| G8 path to US$5k/month | **BORDERLINE**: needs about 8–12% of examinees a year; realistic US$1.5–3.5k | **UNPROVEN**: about 4–6% of an assumed 35–50k filers a year, after regulation | **FAIL**: needs about 20%+ of new brokers; ceiling about US$0.6–1.5k |
| **Verdict** | **CONDITIONAL (#1)** | **CONDITIONAL (#2)** | **KILL as main bet** (optional cash test) |

### Scores (1–5: WTP / low saturation / buyer power / distribution / buildability / speed / low risk)

| Candidate | WTP | Sat | Power | Distr | Build | Speed | Risk | Total /35 |
|---|---|---|---|---|---|---|---|---|
| A. CBLE simulator | 4 | 4 | 4 | 4 | 5 | 3 | 3 | **27** |
| B. PT nationality test | 3 | 3 | 3 | 2 | 5 | 2 | 2 | **20** |
| C. SUSEP corretor | 3 | 3 | 4 | 3 | 4 | 4 | 3 | **24**, but G8 FAIL |
| Despachante aduaneiro | 2 | 3 | 3 | 2 | 4 | 3 | 3 | 20, KILL |
| CFC EQT (CNAI/perito) | 3 | 2 | 4 | 2 | 4 | 2 | 3 | 20, KILL |
| NMLS / FAA A&P / CWI / NCCCO / EA | 4 | 1 | 4 | 2 | 2–4 | 2 | 2 | ≤19, KILL |

### Inferences: unit economics, cheapest tests and MVP spec
**A. CBLE: unit economics**
- Price: US$199 for an "April 2027 pass" and US$299 for the full bundle (all past exams, drills and mocks).
- Gumroad takes 10% + US$0.50, then PayPal payout, so net is about US$180–270.
- Variable costs are near zero; hosting is under US$10/month on a static site plus a small DB. Ads cost about US$1–3 per click (assumption).
- US$5k/month needs about 20–25 sales a month on average. **A realistic year-one target is 80–150 sales (US$18–35k)**, with positive margin.

**A. CBLE: cheapest test**, aligned to the 28 Oct 2026 results (letters around 11–18 Nov) and the April 2027 exam
1. **By 10 Nov 2026**, publish a free timed simulator of the April 2026 public exam with CBP's key. Add a Gumroad pre-order: "April 2027 Simulator – US$149 founder price".
2. **11 Nov–20 Dec 2026**, spend US$80 on Google Ads ("cble past exams", "customs broker exam practice test") plus organic posts in Reddit and LinkedIn broker groups.
3. **PASS:** ≥150 free simulator completions **and** ≥8 paid pre-orders by 31 Dec 2026, or ≥25 paid by 15 Apr 2027.
4. **FAIL:** <3 paid by 31 Dec 2026, which means KILL.
5. **Before building,** confirm the Gumroad→PayPal→Brazil payout with a US$1 self-purchase.

**B. PT nationality test: unit economics**
- Price: €24 one-off (or €19 / €29 / €39 tiers to match the competitor). Net about €21 after Gumroad, or about R$100+ on Hotmart in pt-BR.
- US$5k/month needs about 210 sales a month.

**B. PT nationality test: cheapest test**
1. Set a weekly watch on the IRN page and diariodarepublica.pt (Regulamento da Nacionalidade amendment).
2. Now, for about €40: a pt-BR landing page, a waitlist, a free 20-question diagnostic, and a €9.90 pre-sale through Hotmart or Gumroad. Drive traffic from 3–5 Brazilians-in-Portugal Facebook groups and €25 of Google Ads.
3. **PASS (21 days):** ≥300 waitlist signups **and** ≥15 pre-sales.
4. **FAIL:** <100 signups or <5 pre-sales.
5. **Kill triggers:**
   - the regulation exempts CPLP nationals from the culture/civic test;
   - the State publishes a free official question bank or app;
   - testenacionalidade.com passes 10k Play installs before the client launches.

**C. SUSEP (optional cash test)**
- **20 Oct–23 Nov 2026:** a R$197 "Pacote Dezembro 2026" pre-sale on Hotmart, with R$150 of Google Ads on "simulado susep / prova susep fgv 2026".
- **PASS:** ≥10 sales. **FAIL:** <3.
- Even a PASS does not change the G8 ceiling.

**MVP spec (shared engine, ≤4 weeks)**
- **Content model:**
  - each question has: stem, options, answer, explanation, and a **mandatory citation** (CFR or HTSUS section / article of law) plus source URL;
  - past-exam items carry exam ID and official key;
  - original items carry an "original, not from the official exam" flag.
  - AI may draft items, but each must pass a citation check against the official text before publishing (AI is inside the stack, not the pitch).
- **Study modes:**
  1. Topic drills.
  2. Spaced repetition (FSRS/SM-2 on missed items).
  3. **Timed mocks in the official format** (CBLE 80 questions / 4.5 h with a 75% pass line and a "within 3 questions → appeal-eligible" flag; PT 40 questions / 30 minutes until the official format exists).
  4. CBLE only: **reference-lookup drills** that time how fast the student finds the governing CFR paragraph or HTSUS heading.
- **Analytics:** readiness by topic, pass-probability trend, time per question, weak-citation list.
- **Stack:** Next.js PWA plus SQLite or Supabase; Gumroad license-key or webhook unlock (Hotmart webhook for pt-BR); no accounts needed for the free tier.
- **Effort and cost:** content is the long pole (CBLE: parse 5 official PDFs ≈ 400 items; PT: about 400 cited items). Hosting under US$10/month; total test budget about US$100 (CBLE) plus €40 (PT), within the R$700 limit.

### Gaps
- No verified revenue for any CBLE or Portuguese-test competitor.
- No keyword volumes (no Keyword Planner access).
- Click costs are assumed, not measured.
- The Gumroad PayPal payout to Brazil is not yet tested.
