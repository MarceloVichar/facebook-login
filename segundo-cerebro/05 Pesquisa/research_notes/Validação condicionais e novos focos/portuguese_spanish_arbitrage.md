# Portuguese/Spanish local-language arbitrage: SMB, compliance and professional tools for Portugal, Spain and Latin America (research date 2026-10-12)

Method note for the report writer. Research was done on 2026-10-12, and every data point below was accessed that day unless another date is shown.

- **Revenue figures.** These come from TrustMRR pages fetched with curl. TrustMRR pulls revenue from the founder's Stripe or RevenueCat account, so they count as **verified**. The "insights" fields on those pages (user counts, channels, pricing) are self-reported or machine-generated.
- **Demand signals.** These are Google Autocomplete suggestions (`suggestqueries.google.com`, `hl=pt-PT&gl=pt` unless stated). Autocomplete shows that a query exists, **not its volume**. No keyword-volume tool was available.
- **App Store counts.** These come from the iTunes Search API (`country=pt/es/fr`). Plugin counts come from the WordPress.org plugin API.
- **Search budget.** 9 WebSearch calls were used, against a cap of 15.
- **Blocked sources.** Mojeek returned 403. Several Portuguese sites failed TLS or proxy checks (gecond.com, condoroo.pt, idealista.pt). diariodarepublica.pt and livroreclamacoes.pt need JavaScript, and Playwright was not used. Claims that depend on these pages are flagged.
- **Round-1 kills respected.** EU e-invoicing, GPSR, cookie consent, generic AI exam prep and BR landlord-app clones stay dead unless the evidence below is new.

---

## 1. Which French, Spanish and Portuguese local tools have verified revenue, and what problem does each solve?

### Takeaway
The local-language winners on TrustMRR are mostly **not** compliance-certificate tools. They are:
- trade workflow apps (Khosmos, Mon Atelier, Valideo);
- Google-review collectors (MyFrank, Coucou);
- **law-triggered exam prep for immigrants (Francopass, US$1.7k MRR eight months after the French civic exam became mandatory).**

Portuguese-market products on TrustMRR are young (founded 2025–2026) and small: SmartCondo US$695 MRR, Fidbo US$151, Artur US$30, finpacto US$22. They prove that a newcomer *can* get first payments in Portugal, not that the market is large.

### Cited Findings
**France**
- **Khosmos.** Mobile app for building-trade artisans: quotes, invoices, reduced-VAT certificates and intervention reports.
  - Revenue: US$21,784 MRR, 834 active subscriptions, US$364,766 all-time. Founded March 2023; Stripe-verified.
  - Price: €23.99/month TTC or €199.99/year.
  - Channels: SEO, ASO, Facebook, Instagram and TikTok (self-reported). Its stated problem is "comply with mandatory electronic billing."
  - Source: [TrustMRR Khosmos](https://trustmrr.com/startup/khosmos)
- **Francopass.** Web and mobile prep for the French naturalization interview and civic exam.
  - Revenue: US$1,695 MRR, 132 active subscriptions, US$3,756 in the last 30 days. Founded October 2025; tracked since 2026-03-06; verified via RevenueCat.
  - Price and users: "Free demo, then from €4.99"; "~14,000 users" (self-reported).
  - Source: [TrustMRR Francopass](https://trustmrr.com/startup/francopass)
- **The French civic exam.** It has been mandatory since 1 Jan 2026 for a first multi-year residence card, a 10-year card or naturalization; renewals are exempt. It has 40 multiple-choice questions, a 45-minute limit and an 80% pass mark. These details come from commercial guides, which cite France Éducation International.
  - Sources: [franceaccueil.com](https://franceaccueil.com/examen-civique-naturalisation-2026/); [France Éducation International manual](https://www.france-education-international.fr/document/manuelcandidatexamencivique)
  - A Gumroad seller also sells prep for it: [naturalisationfacile.gumroad.com](https://naturalisationfacile.gumroad.com/l/examencivique)
- **French civic-exam app saturation.** At least 10 iOS apps released between 2025-11 and 2026-05 are all free to download. One ("Examen Civique 2026", Maison Logiciels, released 2026-01-07) has 1,172 ratings; others have 1–138. — [iTunes Search API, country=fr, "examen civique"](https://itunes.apple.com/search?term=examen%20civique&country=fr&entity=software&limit=15)
- **Other French local-SMB tools with verified revenue:**
  - MyFrank (Google-review collection), US$10k MRR
  - Coucou (Google reviews for salons on Planity), US$5.9k MRR
  - Valideo ("intervention report in less than 1 min"), US$4.1k MRR
  - Mon Atelier (repair-shop ERP), US$2.6k MRR
  - WCMultiShipping (WooCommerce plugin for French carriers), US$2.8k MRR
  - LegalOne (French legal notices), US$97k all-time
  - LocManage (French-law rental management), US$23 MRR
  - Conforme Pro (construction document compliance), US$55 MRR
  - Source: [TrustMRR France country page](https://trustmrr.com/country/fr)

**Spain**
- **Gestor de Certificados.** Windows/macOS manager for digital certificates; the problem is "blocked procedures with tax authorities due to expired certificates."
  - Revenue: US$574 MRR, 63 subscriptions, US$51,090 all-time. Founded September 2021; Stripe-verified.
  - Price: €72–90 per license per year.
  - Source: [TrustMRR Gestor de Certificados](https://trustmrr.com/startup/gestor-de-certificados)
- **Other Spanish local tools:**
  - Private-clinic management software, US$4.6k MRR
  - A food-handler training provider ("formación en manipulación de alimentos"), US$37k in 30 days and US$167k all-time
  - TicketingTracker (restaurant app with Verifactu), US$45 MRR
  - VinoVeo (EU wine-label QR compliance), US$79 MRR
  - Source: [TrustMRR Spain country page](https://trustmrr.com/country/es)

**Portugal**
- **SmartCondo.** Condominium-management SaaS for administration companies.
  - Revenue: US$695 MRR, 5 active subscriptions, US$1,114 all-time. Founded **March 2026**; Stripe-verified.
  - Price: "From €0.45/unit/month".
  - Channels: "Cold email, Cold calling". Domain Rating 0.
  - Source: [TrustMRR SmartCondo](https://trustmrr.com/startup/smartcondo)
- **Fidbo.** Google-review requests for Portuguese clinics and barbershops.
  - Revenue: US$151 MRR, 3 subscriptions. Founded May 2026.
  - Price: €45/month or €135/quarter.
  - Source: [TrustMRR Fidbo](https://trustmrr.com/startup/fidbo)
- **Artur.** Web and macOS app for Portuguese freelancers: green receipts, VAT, Social Security and IRS deadlines.
  - Revenue: US$30 MRR, 5 subscriptions, US$318 all-time. Founded May 2026.
  - Price: €6.99/month or €59.99/year.
  - Channels: Reddit, word of mouth, SEO.
  - Source: [TrustMRR Artur](https://trustmrr.com/startup/artur)
- **finpacto.** Converts bank statements and invoices to Excel or TOConline format for Portuguese accountants.
  - Revenue: US$22 MRR, 1 subscription. Founded October 2025.
  - Price: €19.90–99.90/month.
  - Source: [TrustMRR finpacto](https://trustmrr.com/startup/finpacto)
- **The rest of the Portugal page.** It lists 107 startups. Most of the revenue is from global English products (food tech US$9.2k MRR, a directory-submission service, an SAP course), not Portugal-specific tools. — [TrustMRR Portugal country page](https://trustmrr.com/country/pt)

### Inferences
- **Two transferable patterns emerge from France:**
  - (a) a trade workflow app in the local language and tax context (Khosmos). In Portugal, the invoicing core requires AT-certified software, so this pattern only works as a quote or report layer on top of a certified invoicer. That was not verified here.
  - (b) **a new law that forces a large immigrant population to pass a test** (Francopass). Pattern (b) has a direct Portuguese analogue (section 2.7).
- **Francopass is the clearest "newcomer still wins" proof (G2) in this dataset.** It earns verified recurring revenue despite 10+ free competing apps, launched within weeks of the mandate.
- **The Google-review pattern** (MyFrank, Coucou, Fidbo) has verified revenue, but Paddle explicitly forbids it (section 5). It is also not compliance.
- **Portuguese TrustMRR entries show that Portuguese SMBs pay for local SaaS, but only in small numbers so far.** SmartCondo's 5 accounts at about US$139 each came through outbound sales.

### Gaps
- Pagination of the TrustMRR country pages was not checked; the cards shown may be only the first page. No TrustMRR "language" page was found.
- European maker communities (Indie Hackers FR/ES, Reddit) were not searched: Mojeek returned 403, and the search budget was conserved.

---

## 2. Portugal-specific SMB, self-employed and immigrant pains, 2025–2027 (excluding certified invoicing)

### Takeaway
Most Portuguese obligations fall into one of two traps:
- **the state already does the job for free:** the Livro de Reclamações platform, rent receipts on the Portal das Finanças, and Segurança Social and Doutor Finanças simulators;
- **a local incumbent bundles the work cheaply:** Hostkit covers SIBA, tourist tax, INE and Modelo 30 for AL from €4.50 for the first unit.

Two pains survive:
- **(1) the new nationality "test of language, culture, history and symbols"** (law in force 2026-05-19, regulation still pending);
- **(2) software for self-managed and small-administrator condominiums** (proven WTP; a 2026 newcomer with verified revenue).

### 2.1 Alojamento Local (AL): guest registration with AIMA/SIBA, tourist tax, compliance

**Cited Findings**
- **Buyer pool.** RNAL lists **120,379** registered AL establishments (counter on the RNT page, accessed 2026-10-12). The same page lists 6,110 tourist developments (RNET). — [Turismo de Portugal RNT](https://rnt.turismodeportugal.pt/RNT/RNAL.aspx)
- **Hostkit (Portugal).** It automates invoicing, **automatic SIBA submission**, the tourist-tax agent ("Agente TMT: cálculo, faturação e envio automático de declarações aos municípios"), Modelo 30 XML, INE and Banco de Portugal reports, and rental contracts to the AT. It claims 90 integrations and 4.9 on Trustpilot. — [hostkit.pt](https://hostkit.pt/)
- **Hostkit pricing.** "A partir de 4,50€ pela primeira unidade e 0,25€ por cada unidade seguinte." The Lite tier includes automatic SIBA bulletins, SIBA history, the TMT agent and the INE report. — [Hostkit planos](https://hostkit.pt/planos/)
- **Chekin (Spain, multi-country).**
  - Basic from €3.95, Premium €5.95, Enterprise €7.95 per property per month. These per-property prices are annual-plan prices for 1–2 properties.
  - Monthly plans require at least 3 units. The Basic plan includes "Online Check-in, Legal Compliance, iCals, Tourist Taxes."
  - Source: [Chekin pricing](https://chekin.com/en/pricing/)
- **Demand signals.**
  - "boletim de alojamento" → "...para imprimir", "...sef", "...aima", "...pdf", "...siba"
  - "registo de hóspedes" → "...aima", "...legislação", "folha de registo de hóspedes"
  - "software alojamento local" → "...gratuito", "melhor software para alojamento local"
  - "hostkit" → "hostkit preço", "hostkit planos"
  - Source: Google Autocomplete pt-PT, 2026-10-12

**Inferences**
- **Verdict: KILL.** The compliance job is fully commoditized by a Portuguese incumbent at about €4.50/month and by a funded Spanish player at €3.95–5.95/property. "Para imprimir" and "pdf" queries show the residual demand is free and paper-based.

### 2.2 Recibos verdes (self-employed): Social Security quarterly declaration, VAT threshold, IRS

**Cited Findings**
- **Deadlines and fines.** The quarterly Social Security declaration is due in January, April, July and October. Missing it carries a fine of €50–250. The annual declaration corrects the quarterly ones. — [Pplware](https://pplware.sapo.pt/?p=1034598); [gov.pt guide](https://www2.gov.pt/en/guias/trabalhar-por-conta-propria-guia-para-trabalhadores-independentes/obrigacoes-fiscais-e-pagamentos-impostos-e-contribuicoes)
- **VAT.** The quarterly VAT return applies above €15,000 of annual gross income. Fines are 15–200% of the tax due. DECO's example deadline conflicts with the "20th of the second month" rule, so check before relying on it. — [DECO Proteste](https://www.deco.proteste.pt/dinheiro/impostos/dicas/declaracao-trimestral-iva-como-preencher)
- **Demand signals.**
  - "simulador recibos verdes" → "...2026", "...doutor finanças", "...segurança social", "...valor líquido"
  - "declaração trimestral segurança social" → "...datas 2026", "...fora de prazo", "...simulador", "...isenção"
  - "app recibos verdes" → only "app finanças recibos verdes"
  - Source: Google Autocomplete pt-PT
- **The direct comparable earns almost nothing.** Artur, the only dedicated paid product found, has US$30 MRR five months after launch. — [TrustMRR Artur](https://trustmrr.com/startup/artur)
- **Certified invoicers already cover the receipt itself.** InvoiceXpress markets issuing "recibo verde ou fatura." — [InvoiceXpress blog](https://invoicexpress.com/blog/fatura-recibo-verde/)

**Inferences**
- **Verdict: KILL.**
  - The demand signal is dominated by a free brand (Doutor Finanças) and by the official portals.
  - The only verified comparable earns US$30 MRR.
  - Receipts must go through the AT portal or a certified invoicer anyway.

### 2.3 Condominium administration

Deep-validated in section 6 (candidate B).

**Cited Findings**
- **Buyer pool (sector estimate, not official).** APEGAC, the condo administrators' association, estimates about 250,000 condominiums in horizontal property, half of them professionally administered, and more than 4 million people living in condominiums. The article date was not confirmed because idealista returned 403. — [idealista.pt (search extract)](https://www.idealista.pt/news/node/31929)
- **Price of human administration:** €5–15 per fraction per month, about €7 on average. — [Zaask](https://www.zaask.pt/quanto-custa/gestao-de-condominios)
- **Software competitors and prices:**
  - **Gecond (Improxy):** GIA 100 plan €86/month for 100 fractions (€0.86/fraction); GIA 500 plan €225/month (€0.45/fraction). It advertises "soluções dedicadas a empresas e condomínios em auto gestão." — [Improxy Gecond plans](https://www.improxy.com/software-de-gestao-de-condominios-gecond/planos-gecond/)
  - **Gecond's resident app:** 37 ratings on the PT App Store. — [iTunes Search API, "condomínio", PT](https://itunes.apple.com/search?term=condom%C3%ADnio&country=pt&entity=software&limit=15)
  - **SmartCondo:** from €0.45/unit/month; 5 paying accounts since March 2026. — [TrustMRR SmartCondo](https://trustmrr.com/startup/smartcondo)
  - **Condoroo:** software plus management, launched in Lisbon in 2023, "a partir de 6,50 euros por fração" (2023 figure). — [ECO, 2023-10-24](https://eco.sapo.pt/2023/10/24/chatgpt-para-gerir-condominios-condoroo-arranca-em-lisboa-e-mira-expansao-em-2024/)
  - **Odoo module:** a condo module claims compliance with Lei 8/2022. — [Odoo apps](https://apps.odoo.com/apps/modules/19.0/pt_condominio_gestao)
- **Demand signals.**
  - "software condomínio" → "...excel grátis", "...grátis", "...grátis download", "software gestão de condomínios gratuito portugal"
  - "app condomínio" → "app condomínio gratuito"
  - "gestão de condomínios" → "...preços", "**...vai ter novas regras**", "gestão de condomínio novas regras"
  - "declaração de não dívida condomínio" → "...minuta", "...lei", "...escritura"
  - "ata assembleia condomínio" → "...modelo", "...prazo", "...titulo executivo"
  - Source: Google Autocomplete pt-PT
- **The PT App Store is crowded with Brazilian apps.** Superlógica, Condomob and uCondo show 0–66 ratings each, so local Portuguese competition in apps is thin. — [iTunes Search API](https://itunes.apple.com/search?term=condom%C3%ADnio&country=pt&entity=software&limit=15)

### 2.4 Livro de Reclamações Eletrónico

**Cited Findings**
- **Only a logo/link need exists.** The only dedicated WordPress plugin ("Naked Cat Logo for Livro de Reclamações Eletrónico") has about 20 active installs. — [WordPress.org plugin API](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[search]=kuantokusta)
- **Demand is for the official platform.** Autocomplete returns "livro de reclamações online login", "...é obrigatório", "...comprar". — Google Autocomplete pt-PT

**Inferences**
- **Verdict: KILL.** The obligation is met on the state platform (livroreclamacoes.pt), plus a logo or link on the website.
  - The cost claim ("free platform") could not be verified because the page needs JavaScript; treat it as unverified.

### 2.5 RGPD (GDPR)

**Inferences**
- **Verdict: KILL, with no new evidence.** Round 1 already found cookie and consent tools saturated (Pandectes about 2,690 and Consentmo about 1,751 reviews; see [[Consentimento de cookies e GPC]]). No Portugal-specific paid RGPD SaaS with verified revenue was found.

### 2.6 Restaurant and shop licensing and HACCP records

**Cited Findings**
- **App Store.** A PT App Store search for "haccp" returns foreign apps (Bureau de Wit, Hygie, traqfood, BackResto, Flowtify, Octopus, HACCP-OK, Komia), almost all with 0–1 ratings. — [iTunes Search API, PT, "haccp"](https://itunes.apple.com/search?term=haccp&country=pt&entity=software&limit=15)
- **Demand is mostly for templates.**
  - "manual haccp" → "...exemplo", "...pdf", "...para restaurantes pdf", "...2026"
  - "registos haccp" → "...restauração"
  - "haccp" → "...formação", "...curso", "haccp digital"
  - Source: Google Autocomplete pt-PT
- **The closest verified revenue is training, not software.** A Spanish food-handler course provider made US$37k in 30 days. — [TrustMRR Spain](https://trustmrr.com/country/es)

**Inferences**
- **Verdict: KILL for software.** There is no verified revenue for HACCP record apps, demand is for free templates, and 0-rating apps suggest weak pull.
- **The training angle needs a licence.** Mandatory continuous training in Portugal typically has to come from a DGERT-certified entity (not verified here), which fails G5.

### 2.7 Immigrant bureaucracy: AIMA and the new nationality test

Deep-validated in section 6 (candidate A).

**Cited Findings**
- **Buyer pool.**
  - AIMA's *Relatório de Migrações e Asilo 2025* (published 2026-09-22) counts 1,585,854 foreign residents, of whom 493,622 are Brazilian (31.1%).
  - 115,709 residence titles were granted to Brazilians in 2025.
  - The count includes pending regularizations.
  - Sources: [postal.pt](https://postal.pt/edicaopapel/faro-e-o-quarto-distrito-com-mais-residentes-estrangeiros/); [DN Brasil](https://dnbrasil.dn.pt/brasileiros-receberam-115709-novas-autorizaes-de-residncia-em-portugal-em-2025); [e-konomista](https://www.e-konomista.pt/estrangeiros-jovens-em-idade-ativa/)
- **The foreign population quadrupled in seven years to about 1.5 million in 2024**, so most residents are recent arrivals. — [DN](https://www.dn.pt/sociedade/estrangeiros-a-residir-em-portugal-quadruplicaram-em-sete-anos-com-15-milhes-em-2024)
- **Lei Orgânica n.º 1/2026 (18 May 2026), Art. 6:**
  - Naturalization now requires 7 years of legal residence for CPLP and EU nationals, or 10 years for others.
  - Applicants must "comprovarem, através de **teste ou de certificado**, conhecer suficientemente a língua e a cultura portuguesas, a história e os símbolos nacionais," and know the fundamental rights and duties and the political organization of the State.
  - The Government must amend the Regulamento da Nacionalidade "no prazo de 90 dias."
  - Applications already pending keep the old law.
  - The law was approved 2026-04-01, promulgated 2026-05-03, and took effect the day after publication.
  - Source: [Lei Orgânica 1/2026 PDF (Madeira gov copy)](https://www.madeira.gov.pt/Portals/25/Documentos/Legislacao/Lei_Organica_1_2026.pdf)
- **IRN's own page (accessed 2026-10-12) still says** "Algumas destas alterações dependem de regulamentação complementar... no prazo de 90 dias." Online submission is reserved for lawyers and solicitors. — [IRN Nacionalidade](https://irn.justica.gov.pt/Nacionalidade)
- **Has the regulation been published?** No source found as of 2026-10-12. A Brazilian guide says the format is undefined and the test may become operational "entre o final de 2026 e o início de 2027" (speculative). — [Euro Dicas](https://eurodicas.com.br/teste-de-cultura-e-valores-democraticos-para-cidadania-portuguesa); [Migalhas](https://www.migalhas.com.br/depeso/459450/nova-lei-da-nacionalidade-de-2026-o-que-realmente-mudou)
- **Early entrants already exist (PT App Store):**
  - CitizHub (formerly "Minha Nacionalidade"), an application tracker and document organizer: 368 ratings, 4.76★, updated 2026-04-28
  - "Cidadania Portuguesa QCM" (FLY SKY PTY, 2026-06-19), which claims questions "baseadas em exames reais" although no exam exists yet: 0 ratings
  - "Cidadania Portuguesa A2 CIPLE" (2026-07-27): 0 ratings
  - "CIPLE Prep" (€2.99, 2026-08-13): 0 ratings
  - PTracker (8 ratings)
  - Sources: [iTunes "cidadania portuguesa" PT](https://itunes.apple.com/search?term=cidadania%20portuguesa&country=pt&entity=software&limit=15); [iTunes "nacionalidade portuguesa" PT](https://itunes.apple.com/search?term=nacionalidade%20portuguesa&country=pt&entity=software&limit=15)
- **Demand signals.**
  - pt-PT: "teste nacionalidade portuguesa" → "teste lingua portuguesa nacionalidade"; "nacionalidade portuguesa 7 anos" → "lei nacionalidade portuguesa 7 anos", "...5 ou 7 anos"
  - pt-BR: "teste cidadania portuguesa" → "teste para cidadania portuguesa"
  - "renovação autorização de residência aima" and "aima agendamento" each return about 10 suggestions (CPLP, online, reagrupamento familiar).
  - Source: Google Autocomplete
- **The Spanish analogue is saturated.** CCSE (the Spanish nationality civic test) has 10+ free iOS apps, including the official Instituto Cervantes app (343 ratings) and a third-party app with 4,728 ratings. Autocomplete shows "examen ccse 300 preguntas pdf 2026", meaning an official free question bank. — [iTunes "CCSE" ES](https://itunes.apple.com/search?term=CCSE&country=es&entity=software&limit=15); Google Autocomplete es-ES
- **AIMA appointment pains are real** (see the autocomplete above).

**Inferences**
- **Exclude appointment-sniping bots** (ToS and legal risk). Paddle also bans "Government Services" (section 5).

### 2.8 Rental contracts and AT communication (arrendamento)

**Cited Findings**
- **Demand is for official procedures and free letter templates.**
  - "recibos de renda eletrónicos" → "...irs", "...herança indivisa", "emitir...", "quem está dispensado de emitir..."
  - "comunicação contrato arrendamento finanças" → "prazo...", "...cessação"
  - "carta atualização renda" → "...2026", "minuta carta atualização rendas 2026"
  - "programa gestão arrendamento" → only "programa de gestão de arrendamentos"
  - Source: Google Autocomplete pt-PT
- **Professional tools exist with prices.**
  - Gesar (Improxy): €40/month for 25 contracts + €80 setup, up to €180/month for 1,000 contracts. — [Gesar pricing](https://www.improxy.com/gesar-software-gestao-arrendamentos/planos-e-precos-gesar/)
  - Hostkit also generates and sends rental contracts to the AT. — [hostkit.pt](https://hostkit.pt/)

**Inferences**
- **Verdict: KILL for small landlords.** Demand is for templates and the free AT portal, and round 1 already killed the BR landlord-app clone pattern.
- **The professional segment is served** (Gesar).

### 2.9 IRS automático gaps

**Inferences**
- **Verdict: KILL, with no evidence gathered.** The AT pre-fills the return and offers its own simulator, and round 1 found the same "government provides it free" pattern in Brazil. No paid Portuguese IRS tool with verified revenue was found.

### 2.10 Portugal-local e-commerce plugins (a Khosmos/WCMultiShipping analogue)

**Cited Findings**
- **One developer owns the niche.** Naked Cat Plugins (formerly Webdados) publishes "Portugal States" (5,000 installs), the NIF field (5,000), Multibanco/MB WAY (7,000), CTT tracking (500), DPD pickup (200), the KuantoKusta feed (100) and InvoiceXpress invoicing (100). All were updated in August–September 2026. — [WordPress.org plugin API, "portugal"](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[search]=portugal)

**Inferences**
- **Verdict: KILL.** One incumbent covers the niche, and the largest Portugal-only plugin has 7,000 installs, which means a small total market.

### Gaps
- The Lei 8/2022 condo-law text (e.g., the 10-day debt-declaration duty) could not be read on diariodarepublica.pt (JavaScript).
- The origin of the "gestão de condomínios vai ter novas regras" suggestion was not traced; it may refer to a 2026 bill regulating condo administrators.
- No official count of self-employed workers or condominiums was retrieved (INE or Segurança Social).
- Lisbon and Porto tourist-tax rates and the platforms' collection rules were not re-verified. They do not matter given the AL kill.
- No Portuguese Reddit or Facebook-group threads were read.

---

## 3. Spain: Verifactu, Kit Digital, autónomos tools

### Takeaway
Spain does not offer a cheap entry for a solo Brazilian.
- **Verifactu** is an invoicing-software obligation. Producers had to comply from 29 Jul 2025, and users from 1 Jan 2027 (corporate-tax payers) or 1 Jul 2027 (everyone else). Funded incumbents (Holded, Billin, Quipu and others) are already selling it.
- **SES.Hospedajes guest registration** is covered by Chekin and others.
- **The CCSE civic test** is saturated with free apps.

### Cited Findings
- **Verifactu dates.** RDL 15/2025 (BOE 3 Dec 2025) is the second delay: 1 Jan 2027 for companies subject to corporate tax and 1 Jul 2027 for autónomos and other SMEs. Software producers get no extension and have been obliged since 29 Jul 2025 (per a July 2026 guide). No newer postponement was found for September 2026. — [Legal Today, 2025-12-04](https://www.legaltoday.com/actualidad-juridica/noticias-de-derecho/nueva-prorroga-verifactu-no-sera-obligatorio-hasta-2027-para-sociedades-y-otros-contribuyentes-2025-12-04/); [Infoautónomos](https://www.infoautonomos.com/blog/verifactu-cuando-es-obligatorio-a-quien-afecta/); [Billin](https://www.billin.net/blog/hacienda-retrasa-verifactu-a-2027/); [Holded](https://www.holded.com/es/blog/hacienda-retrasa-entrada-vigor-verifactu)
- **Round 1 found a conflicting report of October 2028** (unconfirmed). — see `us_eu_regulatory_demand.md` §5, citing [Fiscal Requirements](https://www.fiscal-requirements.com/news/6062-spain-announces-verifactu-postponement-until-october-2028-to-align-with-mandatory-e-invoicing)
- **Verifactu restaurant newcomer.** TicketingTracker (restaurant management with Verifactu) has US$45 MRR. — [TrustMRR Spain](https://trustmrr.com/country/es)
- **SES.Hospedajes.** Autocomplete returns "registro de viajeros ses hospedajes" → "tutorial...", "como hacer..." (es-ES). Chekin publishes SES.HOSPEDAJES FAQs and prices from €3.95/property. — [Chekin pricing](https://chekin.com/en/pricing/)
- **CCSE is saturated** (section 2.7).

### Inferences
- **Verifactu: KILL.** It is invoicing software, explicitly excluded by the brief. Producers carry "declaración responsable" liability, and suites with large budgets dominate. Round 1's e-invoicing kill stands.
- **The autónomos tools market** (Holded, Quipu, Infoautónomos and others) is presumed saturated. Only the names above were checked.

### Gaps
- **Kit Digital** (2026 status, and whether a non-Spanish entity can become an "agente digitalizador") was not researched, to save the search budget. Treat it as unknown.
- **Verifactu certification.** Whether it requires certification (vs self-declaration) was not re-verified on AEAT pages.

---

## 4. Latin America (Mexico, Colombia, Chile, Argentina): niches without certification

### Takeaway
A brief look found only weak openings. The obvious compliance mandates have free official or quasi-official supply:
- Chile's Ley Karin protocols come from the "mutuales" (ACHS, IST, Mutual);
- Mexico's NOM-035 has free questionnaires (searches add "gratis" and "pdf");
- Colombia's SG-SST searches add "gratis".

These mirror round 1's NR-1 saturation kill in Brazil.

### Cited Findings
- **Chile.** "ley karin protocolo" → "mutual ley karin protocolo", "ist ley karin protocolo", "...de investigacion"; "ley karin software" → only "software ley karin"; "ley 40 horas" → "...2026", "...como se aplica" (es-CL). — Google Autocomplete
- **Mexico.** "nom-035 software" → "software nom 035 gratis"; "nom 035 cuestionario" → "...pdf", "...excel" (es-MX). — Google Autocomplete
- **Colombia.** "software sg-sst" → "...colombia", "...gratis"; "sg-sst gratis" → "curso 50 horas sg sst gratis" (es-CO). — Google Autocomplete
- **Spain (registro horario).** "registro horario app" → "...gratis", "registro horario digital app gratis" (es-ES). — Google Autocomplete

### Inferences
- **Verdict: KILL or deprioritize for LatAm compliance SaaS.** Free-intent queries dominate, the quasi-official bodies supply templates, and purchasing power and currency risk are worse than in Portugal.

### Gaps
- Chile's attendance-control systems under the 40-hour law may need authorization from the Dirección del Trabajo. This is recalled, not verified in this session.
- Argentina was not examined.

---

## 5. Payment route and legal limits for a Brazil-based seller selling to EU buyers

### Takeaway
**Paddle works for SaaS** such as condo software: it supports Brazil, charges 5% + 50¢, and handles EU VAT as Merchant of Record. **Paddle's AUP bans "Certifications and exam preparation services," "Government Services," automated review and engagement tools, and outbound telemarketing.** So:
- the nationality-test prep must use **Gumroad** or the app stores;
- the Google-review pattern is off-limits on Paddle;
- condo SaaS cannot copy SmartCondo's cold-calling channel while billing through Paddle.

### Cited Findings
- **Paddle basics.** It supports Brazil-based software sellers at 5% + 50¢ per transaction, including global tax compliance. — round-1 note `gtm_economics_payments.md` §6, citing [Paddle pricing](https://www.paddle.com/pricing) and [Paddle supported countries](https://www.paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle)
- **Paddle AUP (last updated 13 April 2026).**
  - "If your company's primary offering is human services... Paddle is not a good fit."
  - Restricted: any offering "marketed through the use of outbound telemarketing."
  - Prohibited categories include "Government Services, including but not limited to embassies and foreign consulates"; "**Certifications and exam preparation services**"; "Automated Social Media Marketing... (posts, clicks, likes, views, **reviews**)"; and "Investment or financial advice."
  - Source: [Paddle: What am I not allowed to sell](https://paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle)
- **Gumroad.** It acts as Merchant of Record (since 2025-01-01) at 10% + US$0.50 per sale and supports memberships. — round-1 `gtm_economics_payments.md`, citing [Gumroad pricing](https://gumroad.com/pricing)
- **A naturalization-exam prep seller already uses Gumroad.** — [naturalisationfacile.gumroad.com](https://naturalisationfacile.gumroad.com/l/examencivique)
- **Francopass bills through RevenueCat** (app-store subscriptions). — [TrustMRR Francopass](https://trustmrr.com/startup/francopass)
- **Polar and Stripe Managed Payments are unavailable** to Brazil-based sellers. Lemon Squeezy pays Brazil only via PayPal. — round-1 `gtm_economics_payments.md` §6
- **Legal limit on nationality filing.** Online submission is reserved for lawyers and solicitors. — [IRN](https://irn.justica.gov.pt/Nacionalidade)

### Inferences
- **Nationality-test prep:**
  - Sell through Gumroad on the web (an MoR that handles EU VAT), plus Google Play (US$25 one-off) later.
  - Apple's US$99/year is about 76% of the budget, so defer iOS.
  - Never sell document-filing services or legal advice: that is procuradoria ilícita risk in Portugal (Lei 49/2004, not re-verified), and Paddle bans human and legal services.
  - Never claim "official" or "real exam" questions before the exam exists.
- **Condo SaaS:**
  - Paddle is fine. Acquisition must be inbound (SEO, Google Ads, Facebook groups), not telemarketing.
  - Cold email is not named in the AUP, but "outbound telemarketing" is. Treat outbound sales as a risk to the Paddle account.
- **Selling directly with Stripe Brasil** to EU consumers would make the founder liable for EU VAT on B2C digital services (non-Union OSS). An MoR avoids this.

### Gaps
- Whether Paddle onboards an individual (CPF) without a CNPJ is still unverified (same gap as round 1).
- Gumroad's own prohibited list for exam prep was not re-checked.

---

## 6. Candidate scorecards, deep validation of the top 3, and gate verdicts

### Takeaway
**No candidate passes all eight gates (no APPROVED).**

Two are **CONDITIONAL** and worth a cheap test:
- **A. Portuguese nationality-test prep (web/PWA)**, the strongest analogue to a verified newcomer (Francopass). It is blocked by a regulation that has not yet been published, and the early copycat apps are already there.
- **B. Condominium software for self-managed buildings and micro-administrators (Portugal)**. WTP is proven and a 2026 newcomer has verified revenue, but distribution without contacts is weak, because free-intent searches dominate.

**Killed:**
- AL compliance;
- recibos verdes;
- Livro de Reclamações;
- small-landlord tools;
- HACCP records;
- Portugal Woo plugins;
- Verifactu;
- CCSE prep;
- LatAm compliance;
- the Google-review collector (Paddle-banned).

### Cited Findings (the decisive evidence per candidate is in sections 1–5; summarized here)

#### Candidate A: "Teste de Nacionalidade PT" prep (deep-validated)
- **Product.** A web/PWA course and quiz bank for the new nationality test: language, culture, history, national symbols, rights and duties, and the political organization of the State (Art. 6(1)(c)–(d)).
  - It would include timed mock exams, tracking by topic, an audio mode, and a module explaining the documents and process (informational only).
  - It ships the day the regulation defines the format. Before that, it runs a waitlist plus free content.
  - AI could help draft the question bank, but the value is curated, accurate content, not AI.
- **Buyer and pool.**
  - 1,585,854 foreign residents, 493,622 Brazilian (2025). — [postal.pt](https://postal.pt/edicaopapel/faro-e-o-quarto-distrito-com-mais-residentes-estrangeiros/)
  - Eligible applicants are those with 7 years' residence (CPLP/EU) or 10 years (others). — [Lei Orgânica 1/2026](https://www.madeira.gov.pt/Portals/25/Documentos/Legislacao/Lei_Organica_1_2026.pdf)
  - The yearly number of applicants is unknown (gap).
- **Pain evidence.** It is a statutory requirement, and the regulation was due within 90 days but is still pending on IRN's page. — [IRN](https://irn.justica.gov.pt/Nacionalidade)
- **Competitors.**
  - CitizHub tracks applications (368 ratings) and is not a test prep app.
  - Three or more test-prep apps with 0 ratings were launched in June–August 2026 before the exam format exists; one is paid at €2.99. — [iTunes PT](https://itunes.apple.com/search?term=cidadania%20portuguesa&country=pt&entity=software&limit=15)
  - **Weaknesses:** they are generic, made by app factories, and make false "real exam" claims.
- **WTP proof.**
  - Francopass: US$1,695 MRR, verified, founded October 2025. — [TrustMRR](https://trustmrr.com/startup/francopass)
  - A Gumroad prep product for the French exam. — [Gumroad](https://naturalisationfacile.gumroad.com/l/examencivique)
  - **This is foreign-market proof.** No Portuguese test-prep revenue exists yet, because the test does not exist.
- **Demand signals.**
  - Small but present: "teste nacionalidade portuguesa", "teste lingua portuguesa nacionalidade", "lei nacionalidade portuguesa 7 anos" (pt-PT); "teste para cidadania portuguesa" (pt-BR).
  - France shows what happens after a mandate starts: autocomplete returns "examen civique naturalisation 2026 / test gratuit / prix / inscription" (fr-FR).
- **Channel.**
  - SEO in pt-PT and pt-BR (the founder is a native speaker of the buyers' language).
  - Brazilian-diaspora Facebook and Instagram groups, plus YouTube Shorts.
  - Small Google Ads tests.
  - Gumroad checkout.
- **Build.** A Next.js/PWA quiz engine, content CMS, Gumroad license or webhook gate, and a cheap TTS audio mode: about 2–3 weeks. Content quality is the real work.
- **Time to first revenue.** Gated by the regulation.
  - The law said 90 days from 18 May 2026, so the deadline was about 16 Aug 2026 and has already slipped.
  - Revenue could start within days of publication if the waitlist and content are ready. Otherwise it is unknown.
- **Risks.**
  - (1) The regulation is delayed further or exempts CPLP nationals in practice (e.g., by accepting school certificates).
  - (2) The state publishes a free official question bank and app, as Spain's Cervantes did, and free apps saturate the market (the CCSE pattern).
  - (3) Paddle bans the category, so the business depends on Gumroad or the app stores.
  - (4) Content must be accurate; there is reputational and legal risk if it implies official affiliation.
  - (5) There is no recurring use: buyers churn after passing, so price it as a one-time pass of €14.90–24.90 or a 3-month plan.

#### Candidate B: Condo software for self-managed buildings and micro-administrators, Portugal (deep-validated)
- **Product.** Quota billing and reminders, MB WAY/Multibanco payment references, a debtor list, notices of meetings and minutes (actas) from templates, document archive, maintenance calendar (elevators, insurance, gas), the "declaração de (não) dívida" generator, and a residents' portal.
  - Pricing: flat €9.90–19.90 per building per month for self-managed buildings, or €0.35/fraction for micro-administrators. It undercuts Gecond's €86 entry tier.
- **Buyer and pool.** About 250k condominiums, half professionally administered (APEGAC estimate, undated). That implies about 125k self-managed buildings plus the small administration firms. — [idealista extract](https://www.idealista.pt/news/node/31929)
- **Pain evidence.**
  - Searches for minutes, debt-declaration templates and "novas regras"; Lei 8/2022 obligations (per the Odoo module page). — Google Autocomplete; [Odoo](https://apps.odoo.com/apps/modules/19.0/pt_condominio_gestao)
  - Human administration costs €5–15 per fraction per month. — [Zaask](https://www.zaask.pt/quanto-custa/gestao-de-condominios)
- **Competitors:**
  - Gecond: €86/month for 100 fractions, €225 for 500. — [Improxy](https://www.improxy.com/software-de-gestao-de-condominios-gecond/planos-gecond/)
  - SmartCondo: from €0.45/unit, verified US$695 MRR. — [TrustMRR](https://trustmrr.com/startup/smartcondo)
  - Condoroo: €6.50/fraction including management (2023). — [ECO](https://eco.sapo.pt/2023/10/24/chatgpt-para-gerir-condominios-condoroo-arranca-em-lisboa-e-mira-expansao-em-2024/)
  - Odoo module; Brazilian apps in the PT store.
  - **Weaknesses:** the incumbents target professional administrators with "pedir demonstração" sales, and their entry price is too high for a 10-fraction self-managed building.
- **WTP proof (G1).**
  - Gecond, SmartCondo (verified) and Condoroo are three or more independent paid products.
  - Professional administration at €5–15 per fraction is a costly substitute.
- **Newcomer proof (G2).** SmartCondo went from founding in March 2026 to 5 paying accounts and US$695 MRR by October 2026. — [TrustMRR](https://trustmrr.com/startup/smartcondo)
- **Demand signals.** Commercial intent is mixed and free intent dominates: "software condomínio grátis", "software gestão de condomínios gratuito portugal", "app condomínio gratuito", "gestão de condomínios preços". — Google Autocomplete pt-PT
- **Channel.**
  - SEO on templates ("ata assembleia condomínio modelo", "declaração de não dívida condomínio minuta") feeding a freemium tool.
  - Google Ads on "software condomínio".
  - The tool's own outputs: every resident in a self-managed building receives the notices and minutes, which spreads the brand.
  - **SmartCondo's cold calling cannot be copied if billing through Paddle** (AUP).
- **Build.** A multi-tenant CRUD app, PDF templates, email/SMS, and payment-reference integration: 3–4 weeks for an MVP. It needs no certification, **provided it does not issue invoices or receipts with fiscal value** (condominiums are generally not VAT-registered; not verified).
- **Time to first revenue.** Probably 1–3 months; SmartCondo's first revenue timing is not known.
- **Risks.**
  - Slow SEO.
  - Self-managed buildings have low WTP and rotating administrators, which drives churn.
  - Gecond may launch a cheap self-managed tier.
  - A possible 2026 law regulating administrators is untraced; it could help or hurt.

#### Candidate C: AL guest registration (SIBA), tourist tax and compliance (deep-validated, then killed)
- **Pool.** 120,379 RNAL registrations. — [RNT](https://rnt.turismodeportugal.pt/RNT/RNAL.aspx)
- **Pain.** It is real: SIBA bulletins, the municipal tourist tax, INE and Modelo 30. — [Hostkit](https://hostkit.pt/)
- **Competitors.**
  - Hostkit Lite from €4.50 for the first unit + €0.25 per extra unit, including SIBA, the TMT agent and INE reports. — [Hostkit planos](https://hostkit.pt/planos/)
  - Chekin from €3.95/property. — [Chekin](https://chekin.com/en/pricing/)
- **Demand.** Mostly free and print intent ("boletim de alojamento para imprimir / pdf").
- **Verdict.** G2 fails: a strong local incumbent and a funded foreign player price at about €4–6.
- **G8 fails too.** At about €5 per unit, US$5k MRR needs about 900–1,000 paying units won from Hostkit and Chekin.

#### Other candidates (brief)
- **D. Recibos verdes companion.** Artur makes US$30 MRR at €6.99; demand belongs to Doutor Finanças and the official simulators. → KILL (G1 weak, G4 fails).
- **E. Small-landlord tool** (rent-update letters, receipts, AT communication). Demand is for templates and the free AT portal; Gesar (€40/month) serves professionals. → KILL (G1 weak for individuals, G4).
- **F. HACCP digital records (PT/ES).** No verified software revenue, apps with 0 ratings, and demand for PDF templates. → KILL (G1).
- **G. Google-review collector for Portuguese SMBs** (MyFrank, Coucou, Fidbo pattern).
  - It has verified revenue in France, which passes G1. But Paddle bans automated review tools, which fails G7.
  - Review gating also risks Google policy (not verified). It is not compliance.
  - → KILL on the Paddle route. It could be CONDITIONAL only through a different MoR, and none is verified for Brazil.
- **H. Livro de Reclamações.** → KILL (official platform; a logo plugin with about 20 installs).
- **I. Portugal WooCommerce local plugins.** → KILL (Naked Cat incumbent, small market).
- **J. Spain Verifactu / CCSE / SES.Hospedajes.** → KILL (excluded invoicing; saturated).
- **K. LatAm compliance (Ley Karin, NOM-035, SG-SST).** → KILL (free supply, free intent).

### Gate-by-gate verdicts (top 3)

| Gate | A. Nationality-test prep (PT) | B. Condo software, self-managed (PT) | C. AL SIBA/tax (PT) |
|---|---|---|---|
| G1 WTP (≥2 paid) | PASS by analogy: Francopass (verified) and a Gumroad seller in France. **No Portuguese revenue yet** | PASS: Gecond, SmartCondo (verified), Condoroo | PASS: Hostkit, Chekin |
| G2 not saturated + newcomer wins | PASS (provisional): no exam yet, only 0-rating apps. Francopass won among 10+ French apps. Risk of the CCSE pattern | PARTIAL: incumbents exist, but SmartCondo (2026) shows a newcomer can win; the self-managed tier is underserved | **FAIL**: Hostkit at €4.50, Chekin at €3.95 |
| G3 buyer power | PASS (moderate): employed immigrants paying €15–25 one-off | PASS: households already pay €5–15 per fraction for human administration | PASS |
| G4 distribution without contacts | PARTIAL: queries exist but are small until the mandate starts; the founder is a member of the Brazilian diaspora | **WEAK**: "grátis" dominates; SEO on templates is slow | FAIL (free/print intent) |
| G5 MVP ≤4 weeks, no licence | PASS | PASS (no fiscal invoicing) | PASS |
| G6 not AI-core | PASS | PASS | PASS |
| G7 legal/ToS/payment | PARTIAL: **Paddle bans exam prep**, so use Gumroad or Play; no legal advice; no "official" claims | PASS with Paddle, if no outbound telemarketing | PASS |
| G8 path to US$5k/month | UNCERTAIN: at about €17 net per pass, needs about 300 sales/month. Plausible only if the test applies to tens of thousands of applicants a year (unknown) | PLAUSIBLE: about 360 buildings at €12/month, or about 11k fractions via micro-administrators, is ~0.3% of about 125k self-managed buildings. Churn is the risk | FAIL: about 1,000 units at about €5 against entrenched players |
| **Verdict** | **CONDITIONAL** | **CONDITIONAL** | **KILL** |

### Scores (1–5; criteria: WTP evidence / low saturation / buyer power / distribution without contacts / buildability / speed to first revenue / low risk)

| Candidate | WTP | Sat. | Power | Distr. | Build | Speed | Risk | Total /35 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| A. Nationality-test prep (PT) | 3 | 4 | 3 | 3 | 5 | 2 | 2 | **22** | CONDITIONAL |
| B. Condo software, self-managed (PT) | 4 | 3 | 3 | 2 | 4 | 3 | 3 | **22** | CONDITIONAL |
| C. AL SIBA/tourist tax (PT) | 4 | 1 | 4 | 2 | 3 | 2 | 3 | 19 | KILL |
| G. Google-review collector (PT) | 4 | 2 | 3 | 2 | 4 | 3 | 1 | 19 | KILL (Paddle AUP) |
| D. Recibos verdes companion (PT) | 1 | 3 | 3 | 2 | 5 | 3 | 3 | 20 | KILL |
| E. Small-landlord tool (PT) | 2 | 3 | 3 | 2 | 4 | 2 | 3 | 19 | KILL |
| F. HACCP records (PT/ES) | 1 | 3 | 3 | 2 | 4 | 2 | 3 | 18 | KILL |
| I. Portugal Woo plugins | 3 | 1 | 3 | 3 | 4 | 2 | 3 | 19 | KILL |
| J. Spain Verifactu / CCSE | 3 | 1 | 3 | 2 | 2 | 2 | 2 | 15 | KILL |
| K. LatAm compliance | 2 | 2 | 2 | 2 | 4 | 2 | 3 | 17 | KILL |

### Cheapest real-world tests (pass/fail thresholds)
- **A. Nationality-test prep.**
  - (1) Set a weekly watch on Diário da República and the IRN page for the amended Regulamento da Nacionalidade. **Kill trigger:** the regulation exempts CPLP nationals from the culture/civic test, or the state publishes a free official app with its question bank.
  - (2) Now, for about €40: a pt-BR/pt-PT landing page ("Prepare-se para o novo teste de nacionalidade") with a waitlist. Drive traffic with Google Ads on "teste nacionalidade portuguesa / lei nacionalidade 7 anos" and with posts in 3–5 Brazilian-in-Portugal Facebook groups.
  - **PASS:** ≥300 waitlist signups in 21 days, and ≥15 Gumroad pre-orders at €9.90 ("founder price, delivered when the format is published"). **FAIL:** <100 signups or <5 pre-orders.
- **B. Condo software.**
  - Ship a free "ata e convocatória de assembleia + declaração de não dívida" generator (1 week). Then run €40 of Google Ads on "software condomínio" / "gestão de condomínio app" plus template SEO, with a €9.90/month paid tier (quotas, reminders, MB references).
  - **PASS:** ≥40 generator users and ≥5 paying buildings within 45 days. **FAIL:** <2 paying buildings, which means G4 and G8 fail.

### Inferences
- **The local-language arbitrage Round 1 hoped for exists in a narrower form than "compliance certificates":**
  - In France, a new mandatory test for immigrants produced verified revenue within months, even among 10+ free apps.
  - Portugal has an identical trigger with a Portuguese-speaking pool the founder belongs to. **That is the founder's distinctive edge.**
  - Its timing is uncontrollable, and the Paddle ban forces Gumroad or app-store billing.
- **Condo software is the "boring SaaS" option.** It has real WTP and a 2026 newcomer with verified revenue, but the self-managed segment's free intent makes distribution the binding constraint.
- **Portugal's bureaucratic pains are mostly absorbed by the state** (Portal das Finanças, Segurança Social Direta, livroreclamacoes.pt) **or by one strong local incumbent per vertical** (Hostkit for AL, Gecond for condos, Naked Cat for Woo). The Portuguese market is small enough that one incumbent per niche is usually enough to close it.

### Gaps
- **Missing data for candidate A:**
  - the annual number of naturalization applications by residence;
  - how many Brazilians reach 7 years' legal residence in 2026–2028;
  - whether CPLP nationals keep the language-proof presumption under the new regulation.
- **Missing data for candidate B:**
  - an official count of buildings in horizontal property (INE Censos 2021 table not retrieved);
  - SmartCondo's acquisition cost.
- **Unverified checks:**
  - whether condominium quota receipts need certified software or count as fiscal documents;
  - Gumroad's acceptable-use stance on exam prep;
  - Paddle onboarding without a CNPJ.
