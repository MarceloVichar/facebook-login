# Validation round 2: deterministic field-inspection report generator for Brazilian engineers and architects (laudos de inspeção predial/autovistoria, vistoria cautelar, vistoria de recebimento, laudo/plano de reforma NBR 16280)

All data points were collected on **2026-10-12** unless another date is given. The round-1 notes ([[finalists_brazil_verification]], [[brazil_professional_niches]]) are the baseline and are not repeated here. Method notes: Google Autocomplete (hl=pt-BR, gl=br) was queried 302 times. Google Play was scraped directly. Hotmart's marketplace JSON (`__NEXT_DATA__`) and its checkout pages were read with headless Chrome. Udemy course pages were rendered with headless Chrome. Mojeek, the iTunes API, Mercado Livre (login wall), Elo7 (closed) and Instagram (HTTP 429) could not be read. Hotmart checkout prices were shown in **US$** because the egress IP is in the US. BRL equivalents use the PTAX rate of **R$ 4.99/US$ on 2026-10-09** ([BCB PTAX](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='10-01-2026'&@dataFinalCotacao='10-12-2026'&$format=json)). They are approximations, because Hotmart applies its own FX conversion from the producer's BRL price.

## 1. How large is the practitioner pool?

### Takeaway
No official count of professionals who issue these laudos exists in public data. Confea/CREA do not publish ART counts by activity, and CAU does not publish RRT counts by activity. Every behavioural proxy points to an online-active specialist pool of **low thousands**, not tens of thousands: IBAPE has ~2,000 members, the top YouTube channels have 3–4k subscribers, the best Udemy course has 400 students and the most-reviewed Hotmart courses have 14–69 reviews. The registered base is huge (~1.2M Confea registrants, 300k+ civil engineers, 200k+ architects), but it says little about how many people buy tools.

### Cited Findings
- **Registered base (from round 1, not re-verified):**
  - ~1.2M Confea-system registrants (May 2025 census) — [Confea](https://www.confea.org.br/node/232061)
  - "mais de 300 mil" civil engineers (2019, search summary) — [CREA-SC](https://portal.crea-sc.org.br/abenc-promove-25o-congresso-brasileiro-de-engenheiros-civis-em-florianopolis/?print=pdf)
  - 200k+ architects — [ArchDaily/CAU](https://www.archdaily.com/pt/tag/cau-br)
- **ART/RRT statistics by activity: not public.**
  - A WebSearch for Confea ART statistics by activity found no national breakdown. A Confea/CREA-SC article describes a planned "Cadastro Nacional de ARTs" for statistics by activity, with its status undated — [CREA-SC](https://portal.crea-sc.org.br/cadastro-nacional-de-arts-de-proposta-a-uma-realidade/?print=pdf)
  - CREA-SC's statistics page publishes only "Total de ART's pagas por Inspetoria" (updated 24/05/2026), with no split by activity — [CREA-SC estatísticos](https://portal.crea-sc.org.br/divulgacao/estatisticos/)
  - CAU's Resolução 9/2012 lists vistoria, perícia, avaliação, laudo and parecer técnico as RRT activities, but no RRT counts by activity were found — [Res. CAU/BR 9](https://www.legisweb.com.br/legislacao/?id=116087)
- **IBAPE:**
  - Founded 1957, "Possui mais de 2.000 associados" (2025 presentation) — [IBAPE/Benvenho 2025](https://biblioteca.ibape-nacional.com.br/wp-content/uploads/2025/02/Brazil_s-regulation-qualification-and-certification-in-valuation-Agnaldo-Benvenho.pdf)
  - IBAPE-SP does not publish a member count on its site — [IBAPE-SP](https://ibape-sp.org.br/)
- **Udemy (pt-BR courses; students, ratings and last update):**
  - Inspeção Predial e Plano de Manutenção para Condomínios: **400 students**, 119 ratings, updated 8/2026 — [Udemy](https://www.udemy.com/course/inspecao-predial-e-plano-de-manutencao-para-condominios/)
  - Patologia das Construções: 825 students, 123 ratings — [Udemy](https://www.udemy.com/course/patologia-das-construcoes-e-laudos-tecnicos/)
  - Laudos de Patologia das Construções: 38 students — [Udemy](https://www.udemy.com/course/laudos-de-patologia-das-construcoes/)
  - Laudo Técnico de Reforma: **54 students**, 14 ratings — [Udemy](https://www.udemy.com/course/laudo-tecnico-de-reforma/)
  - Como Realizar Vistoria de Imóveis Urbanos: 269 students — [Udemy](https://www.udemy.com/course/como-realizar-vistoria-de-imoveis-urbanos/)
  - Perícia Judicial em Engenharia – Módulo III (Laudo Pericial): 543 students — [Udemy](https://www.udemy.com/course/pericia-judicial-em-engenharia-modulo-iii-laudo-pericial/)
  - "Inspeções em Condomínios – Situações Práticas" 1.0–4.0: **1 student each** (launched 2026) — [Udemy](https://www.udemy.com/course/inspecoes-em-condominios-situacoes-praticas-10/)
  - A Udemy search for "vistoria cautelar" returned no vizinhança course among its course links (search pages rendered 2026-10-12) — [Udemy search](https://www.udemy.com/courses/search/?q=vistoria%20cautelar&lang=pt)
- **Hotmart (the main course marketplace for this niche; review counts are lower bounds on buyers):**
  - Dominando a Patologia (Eng. Marília Araújo): 69 reviews — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/curso-de-patologia/U46378780H)
  - Curso: Laudo Técnico de Reforma (Avance Engenharia): 44 reviews — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/curso-laudo-tecnico-de-reforma/U5001560T)
  - Combo Inspeção Predial: 27 reviews (since 2021-11) — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/combo-inspecao-predial-na-pratica/A62836289H)
  - LAUDO DE VISTORIA CAUTELAR (Eng. Giovanni Cremonezi): 25 reviews — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/hagsxd-laudo-de-vistoria-cautelar-qdtxi/H12589109O)
  - Inspeção predial na prática (Realizar Engenharia): 17 reviews (since 2020-03) — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/inspecao-predial-na-pratica-do-zero-a-excelencia/K13563309D)
  - Fórmula Laudos Técnicos (Karine Baptista): 14 reviews — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/laudos-tecnicos-de-engenharia-civil-nivel-1-veja-tudo-o-que-precisa-para-comecar-nesse-nicho/C50172855E)
  - Across 16 marketplace queries, I classified 158 products as relevant (engineering laudos, vistorias, perícias, patologia, reforma). The 64 courses or events among them carry 562 reviews in total, and the 94 ebook/template/software items carry 13 — [Hotmart search](https://hotmart.com/pt-br/marketplace/produtos?q=inspe%C3%A7%C3%A3o%20predial)
- **YouTube (view counts as of 2026-10-12):**
  - Top results for "como fazer laudo de inspeção predial" have 64–5,841 views over 4–6 years: 3,777 — [video](https://youtu.be/pcNx2ThOJF4); 3,454 — [video](https://youtu.be/iB7oKcOPFCc); 5,841 — [video](https://youtu.be/5Mzk52JGkc0)
  - Vistoria cautelar de vizinhança videos: 222–4,362 views — [video](https://youtu.be/OuuPmXNaJ1A), [video](https://youtu.be/TIb3Q7co3MY)
  - Laudo de reforma NBR 16280 videos reach 8.4k–12.7k views: 12,094 — [video](https://youtu.be/YNx3eSk99kU); 12,708 "Como Elaborar o Laudo Técnico de Reforma" — [video](https://youtu.be/KyUl6lKqW_4); 8,414 — [video](https://youtu.be/9nCfq03dSj4)
  - Consumer content on vistoria de entrega de chaves is much larger: 197,703 — [video](https://youtu.be/d_Sf13Iu640); 68,402 — [video](https://youtu.be/GO2DMtzDZtM)
  - Engineering "laudo técnico" explainer: 69,782 views in 2 months — [video](https://youtu.be/QcNYZRZwDOY)
  - Channels: Engenheira Karine Baptista **3 mil inscritos**, 75 videos — [YouTube](https://www.youtube.com/@EngenheiraKarineBaptista); Realizar Engenharia **3,82 mil inscritos**, 262 videos — [YouTube](https://www.youtube.com/@RealizarEngenharia)
- **Self-reported throughput:** Onlaine claims "+3000 laudos / mês" and "+15 anos de atuação" — [Onlaine](https://www.onlaine.com.br/onlaine-inspecao.html)
- **Facebook and LinkedIn group sizes:** two WebSearches found no group pages, and Facebook requires login — [WebSearch result context: Sindiconet](https://www.sindiconet.com.br/informese/inspecao-predial-noticias-eventos/amp)

### Inferences
- **Triangulation (inference):** about 2,000 IBAPE members form the core of specialists. The top creators reach 3–4k YouTube subscribers. The best course on any platform has under 1,000 visible buyers or students. The niche's online learning audience therefore looks like **~3k–15k professionals**, of whom a subset sells laudos regularly. The laudo-de-reforma sub-topic draws 2–4× the YouTube views of inspeção predial. It is the most-reviewed engineering-laudo course on Hotmart (44 reviews), which suggests it is the **highest-frequency** document in this family.
- **Onlaine as a back-check (inference):** if Onlaine's self-reported 3,000 laudos/month were real and users averaged 5–20 laudos/month, it would have roughly 150–600 paying users. That is the same order as the 170–360 subscribers this project needs (section 6), but Onlaine took 15 years.
- The "1% of 1.4M registrants = 14k" estimate from round 1 is plausible as an upper bound for professionals who ever issue such laudos. It overstates the number who would pay for software.

### Gaps
- Official ART/RRT counts by activity type (laudo, vistoria, inspeção, perícia) are unavailable. A LAI (Lei de Acesso à Informação) request to Confea or CAU/BR would close this gap but takes 20–30 days.
- IBAPE-SP and state institutes' member counts are not published.
- Facebook and LinkedIn group sizes could not be read (login walls; WebSearch returned none).
- Hotmart does not show student counts on marketplace pages, so review counts are only a lower bound on buyers.

## 2. Is there willingness to pay (templates, courses, per-laudo fees)?

### Takeaway
WTP for **training** is proven at R$ 300–1,000+ per course, with 14–69 reviews on the leaders. WTP for **service fees** is high: IBAPE-SP sets R$ 625/h and a R$ 6,875 minimum per contract, and the 2026 market range for a vistoria de recebimento is R$ 500–3,500. WTP for **templates** is unproven. Since 2025, 66 template/ebook kits were dated on Hotmart in this niche, priced at about US$ 7–42 (≈R$ 35–210), and only 1 has any review. WTP for **software** sits at R$ 70–219/user/month (Howse, Onlaine), but no revenue is verified anywhere.

### Cited Findings
- **Professional fees (primary source):**
  - The IBAPE-SP Regulamento de Honorários (approved 08/04/2025) sets a technical hour of **R$ 625** and a minimum fee of **R$ 6.875 per contract**. For vistoria cautelar the minimum applies "independentemente da quantidade de imóveis" — [IBAPE-SP PDF](https://www.ibape-sp.org.br/wp-content/uploads/2025/11/1744630330-regulamento-de-honorarios-2025-aprovado.pdf), [IBAPE-SP page](https://www.ibape-sp.org.br/regulamento-de-honorarios/)
  - Quadro 01 hours per property:
    - Building unit <100 m²: cautelar 2 h (≈R$ 1,250); entrega/recebimento 3 h (≈R$ 1,875)
    - House <100 m²: 2.5 h (≈R$ 1,562) and 4.4 h (≈R$ 2,750)
    - Per floor of a building's common areas: 1–2 h (cautelar) and 2–3.5 h (entrega)
    - Source: [IBAPE-SP PDF](https://www.ibape-sp.org.br/wp-content/uploads/2025/11/1744630330-regulamento-de-honorarios-2025-aprovado.pdf)
  - The same regulation references a "Norma de Vistoria Cautelar de Vizinhança no IBAPE-SP - 2025" (nível 2) — [IBAPE-SP PDF](https://www.ibape-sp.org.br/wp-content/uploads/2025/11/1744630330-regulamento-de-honorarios-2025-aprovado.pdf)
  - IBAPE-SP states it will not revise the fee table "neste momento" — [IBAPE-SP page](https://www.ibape-sp.org.br/regulamento-de-honorarios/)
- **Market prices for apartment vistoria in 2026:** R$ 500 (visual), ~R$ 1,200 (intermediate), up to ~R$ 3,500 (full laudo with ART/RRT). Tiers: R$ 500–900, R$ 900–1,800 and R$ 1,800–3,500 — [Monitor do Mercado 2026](https://monitordomercado.com.br/noticias/409181-quanto-custa-contratar-uma-vistoria-profissional-antes-de-receber-as-chaves-do-apartamento/)
- **Course prices** (Hotmart checkout read from a US IP, in US$, ≈BRL at 4.99):
  - Inspeção predial na prática (Realizar): US$ 209 (≈R$ 1,040) — [checkout](https://pay.hotmart.com/K13563309D)
  - Fórmula Laudos Técnicos: US$ 169 (≈R$ 843) — [checkout](https://pay.hotmart.com/C50172855E)
  - Laudo de Vistoria Cautelar (Cremonezi): US$ 107 (≈R$ 534) — [checkout](https://pay.hotmart.com/H12589109O)
  - Laudo Técnico de Reforma (Avance): US$ 107 (≈R$ 534) — [checkout](https://pay.hotmart.com/U5001560T)
  - Laudo de Reforma com Cálculo de Acréscimo de Cargas: US$ 107 — [checkout](https://pay.hotmart.com/O11564517G)
  - Combo Vistoria de Recebimento: US$ 84 (≈R$ 419) — [checkout](https://pay.hotmart.com/W99186080E)
  - Laudo de Inspeção Predial: do escopo ao laudo assinado (NBR 16747), launched 2026-10-04: US$ 64 — [checkout](https://pay.hotmart.com/D107867678G)
  - Combo Inspeção Predial: US$ 42 — [checkout](https://pay.hotmart.com/A62836289H)
- **Template and kit prices (Hotmart; review counts in parentheses):**
  - Kit Inspeção Predial NBR 16747 — Checklist, Laudo e Matriz GUT (2026-07-20): US$ 22 (0 reviews) — [checkout](https://pay.hotmart.com/N106801039J), [listing](https://hotmart.com/pt-br/marketplace/produtos/kit-inspecao-predial-nbr-16747-checklist-laudo-e-matriz-gut/N106801039J)
  - Kit Profissional de Inspeção Predial (2026-03-09): US$ 22 (0) — [checkout](https://pay.hotmart.com/S104817119L)
  - Modelo de Laudo Cautelar de Vizinhança (2026-09-01): US$ 7 (0) — [checkout](https://pay.hotmart.com/M107419015S)
  - Kit Laudo de Reforma – NBR 16280 (2026-02-17): US$ 7 (0) — [checkout](https://pay.hotmart.com/X104493542F)
  - Modelo Editável Plano Reforma NBR 16280 (2026-03-04): US$ 14 (0) — [checkout](https://pay.hotmart.com/C104742253F)
  - LAUDO DE REFORMA (ART) – Modelo 100% Pronto (2024-02): US$ 12 (2 reviews) — [checkout](https://pay.hotmart.com/U90931890P)
  - Plano de reforma + ART (2024-03): **US$ 127 (≈R$ 634)** (0) — [checkout](https://pay.hotmart.com/G91854671A)
  - Pacote de Modelos de Laudos Técnicos de Engenharia Civil: US$ 42 (4 reviews) — [checkout](https://pay.hotmart.com/S82189718W)
  - Kit de Modelos de Laudos Técnicos – Engenharia Civil (2026-02): US$ 42 (0) — [checkout](https://pay.hotmart.com/L104285793J)
  - Modelo de Laudo para Vistoria de Recebimento das Áreas Comuns (2025-06): US$ 15 (0) — [checkout](https://pay.hotmart.com/A100194047H)
  - Relatório Fotográfico Automático (2026-02): US$ 4 (0) — [checkout](https://pay.hotmart.com/C104321554P)
  - Mentoria "Vivendo de Plano de Reforma": US$ 42 — [checkout](https://pay.hotmart.com/W95886789A)
- **Template market depth (my count from the Hotmart JSON of 16 queries):** 158 relevant products. Of the 82 dated 2025-01-01 or later, only 2 have any review. Of the 66 ebook/template/software items dated since 2025, only 1 has a review. 55 relevant products were dated in 2026 alone — [Hotmart search](https://hotmart.com/pt-br/marketplace/produtos?q=nbr%2016280)
- **Software price anchors:**
  - Howse "De R$ 70/mês", 20% off annual — [Howse](https://howseapp.com/)
  - Onlaine: Essencial R$ 89/user/month (2 inspeções/month, 500 photos per inspection); Profissional R$ 139 (5/month); Avançado **R$ 219/user/month with a minimum of 5 users** (20/month); "Sem fidelidade. Sem taxa de implantação." — [Onlaine planos](https://www.onlaine.com.br/onlaine-inspecao.html)
  - Inspeção Pro: "a partir de R$ 334,00/mês" (teams) — [Inspeção Pro planos](https://inspecao.pro/planos-e-valores/)
  - Devolus (rental): free for 2 vistorias/month; R$ 79.90 (5); R$ 139.90 (10); "Mais de 10 mil profissionais" (self-reported) — [Devolus](https://www.aplicativodevistoria.com.br/)
  - FotoGeo (photo reports): modules "a partir de R$ 9,90 (Semestrais)" per the developer's 2023 reply on Play — [Play FotoGeo](https://play.google.com/store/apps/details?id=fotogeo.com.br.app)
- **Other marketplaces:**
  - **Elo7 is closing:** "O Elo7 está encerrando suas atividades e, a partir de agora, não é possível fazer novas compras e vendas" — [Elo7](https://www.elo7.com.br/lista/modelo-de-laudo)
  - Mercado Livre listing pages redirected to a login wall (account-verification) from this environment — [Mercado Livre](https://lista.mercadolivre.com.br/modelo-laudo-inspecao-predial)

### Inferences
- **Fees support a software price.** A single unit vistoria de recebimento is worth ~R$ 1,200–1,875 (market median and IBAPE hours), and a cautelar contract is ≥R$ 6,875. A tool at R$ 50–150/month costs less than 10% of one job. The value argument is time saved on writing and photo layout.
- **The template market is flooded and probably non-converting.** Dozens of cheap kits (US$ 7–42) appeared in 2025–2026 with zero reviews, consistent with AI-assisted ebook spam. Template seekers pay little, and "premium template pack" as first revenue will compete at a ~R$ 35–110 price point against free and US$ 7 alternatives. The only outlier is "Plano de reforma + ART" at US$ 127 (0 reviews), so a high template price is unproven.
- **Training buyers are the proven payers.** Course leaders charge R$ 400–1,000 and have dozens of reviews each. That makes course creators potential affiliates or partners, and the learners (new entrants who want to "começar nesse nicho") a likely early-adopter segment.

### Gaps
- No verified revenue for any software tool, template seller or course (Hotmart hides sales; review-to-sale ratio unknown).
- BRL list prices of Hotmart products (only USD conversions were visible).
- Mercado Livre template listings and "vendidos" counts (login wall). Kiwify has no public marketplace search.

## 3. What drives demand: inspection laws, NBR 16280, entrega de chaves, cautelar duties?

### Takeaway
The biggest new fact is a pending federal law. **PL 159/2026** would require a **Laudo de Inspeção Técnica de Edificação (Lite)** with ART for every building except single-family homes, dams and stadiums: first at 10 years after the habite-se, then every 10 years. It has been "PRONTO PARA DELIBERAÇÃO DO PLENÁRIO" in the Senate since 2026-04-09 and would take effect 180 days after publication. Today's drivers are fragmented and weakly enforced: 41 municipal and 5 state laws exist, covering ~31M people in the cities IBAPE lists, and Rio's compliance was 11.7% in 2015. NBR 16280 reformas and new-apartment handovers are the **high-frequency** drivers: CBIC counts 426k units sold and 453k launched in 2025. Cautelar duties derive from NBR 12722 plus the CDC rather than from municipal permit rules.

### Cited Findings
- **Federal bill PL 159/2026** (Câmara substitute to PLS 491/2011 / PL 6.014/2013):
  - Approved by the Câmara on 4 Dec 2025 (signed by Hugo Motta) — [bill text PDF](https://legis.senado.gov.br/sdleg-getter/dadosabertos/documento/24d183db-0325-41b0-8993-83cb907dd560)
  - Approved by the Senate CDR on 7 Apr 2026; it "segue agora para o plenário" — [Confea 07/04/2026](https://www.confea.org.br/comissao-do-senado-aprova-inspecao-predial-periodica-e-criacao-do-lite)
  - Status as of 2026-10-12: "PRONTO PARA DELIBERAÇÃO DO PLENÁRIO", "Aguardando inclusão em Ordem do Dia", situação dated 2026-04-09 — [Senado dados abertos](https://legis.senado.leg.br/dadosabertos/processo?codigoMateria=172470), [movimentações](https://legis.senado.leg.br/dadosabertos/materia/movimentacoes/172470)
  - The Senate is reviewing a Câmara substitute ("nos termos do caput do art. 65 da Constituição"), so a plenary approval would send it to sanction — [bill text PDF](https://legis.senado.gov.br/sdleg-getter/dadosabertos/documento/24d183db-0325-41b0-8993-83cb907dd560)
  - Content, from the same PDF:
    - Art. 3: all buildings except dams, football stadiums and "residências unifamiliares"
    - Art. 5: first inspection after 10 years from the habite-se, then every 10 years; the municipal authority may shorten intervals
    - Art. 6: the Lite must contain 13 items. They include identification, technical description, inspection date, a list of documents requested and provided, methodology, systems inspected and not inspected, "descrição das anomalias… e registro fotográfico de cada uma delas", priority classification, maintenance evaluation per ABNT norms, recommendations, date, signature with council registration, and ART
    - Art. 7: a qualified professional issues the Lite with an ART or equivalent
    - Art. 8: free Lites for temples and non-profits (via CREA agreements)
    - Art. 10: the owner or administrator must contract the Lite and archive it for 20 years
    - Penalties are municipal fines, activity suspension and licence cancellation
    - Art. 11: in force 180 days after publication
  - In Oct 2025 Confea framed the bill as a priority after the CCJC approval — [Confea 15/10/2025](https://www.confea.org.br/node/232590)
- **Existing laws:**
  - IBAPE's 2026 survey counts 41 municipal and 5 state laws; only 9 municipal and 1 state law are regulated. Listed cities include Rio, Niterói, Duque de Caxias, Nova Iguaçu, Campos, Cabo Frio, Santos, Guarujá, São Vicente, Guarulhos, Jundiaí, Mogi das Cruzes, Ribeirão Preto, Bauru, Caraguatatuba, Arujá, Maringá, Balneário Camboriú, Porto Alegre, Canoas, Bagé, Torres, Capão da Canoa, Cidreira, Xangri-lá and Salvador (from round 1) — [IBAPE 2026](https://biblioteca.ibape-nacional.com.br/wp-content/uploads/2026/01/adrian1.pdf)
  - **IBGE 2025 population of those 26 cities: 31,482,121.** Largest: Rio 6,730,729; Salvador 2,564,204; Porto Alegre 1,388,794; Guarulhos 1,349,100; Duque de Caxias 866,225; Nova Iguaçu 843,220; Ribeirão Preto 731,639. Fortaleza (2,578,483) and João Pessoa (897,633) also appear in autocomplete ("lei de inspeção predial fortaleza", "…joao pessoa") — [IBGE SIDRA 6579, 2025 estimates](https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2025/variaveis/9324?localidades=N6[3304557,3303302,3301702,3303500,3301009,3300704,3548500,3518701,3551009,3518800,3525904,3530607,3543402,3506003,3510500,3503901,4115200,4202008,4314902,4304606,4301602,4321501,4304630,4305454,4323804,2927408,2304400,2507507,3550308])
  - **São Vicente (SP)** Lei 4.666/2025 (sanctioned 15/08/2025): buildings over 10 years old, periodicity by age, higher fines (search summary) — [Sindiconet](https://www.sindiconet.com.br/informese/inspecao-predial-obrigatoria-sao-vicente-noticias-manutencao)
  - **São Paulo state** PL 723/2025 (Aug 2025) would require periodic technical inspection referencing NBR 16747 and NBR 16280. It was still a bill in April 2026 (search summary) — [Alesp propositura](https://www.al.sp.gov.br/spl/2025/08/Propositura/1000619304_1000768388_Propositura.pdf), [Sindiconet](https://www.sindiconet.com.br/informese/projeto-lei-oab-inspecao-tecnica-edificios-sao-paulo-noticias-juridico)
  - No law for the city of São Paulo (11,904,961 people) was found — [IBGE](https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2025/variaveis/9324?localidades=N6[3550308])
  - **Rio:** 270k buildings obliged in 2014, <5% compliant at the deadline and 11.7% one year later. No 2024–2026 compliance data was found (WebSearch, 2026-10-12) — [JB 2014](https://www.jb.com.br/rio/noticias/2014/06/24/amp/prazo-para-autovistoria-em-predios-do-rio-termina-dia-1o-julho.html), [Sindiconet](https://www.sindiconet.com.br/informese/autovistorias-noticias-manutencao-1/amp)
- **NBR 16280 (reformas):**
  - In force since 2014. Every renovation in a unit must be communicated to the síndico before work starts, and the síndico can fine or block workers (search summary of the condo press) — [Condomínios SC](https://condominiosc.com.br/jornal-dos-condominios/manutencao/5813-nbr-16-280-seguranca-para-as-reformas-e-obras-em-condominios)
  - Autocomplete: "laudo de reforma" [10] ("…de apartamento", "…modelo", "…preço", "…é obrigatório"); "art de reforma" [10] ("…de apartamento valor", "…como preencher", "emitir art de reforma"); "plano de reforma nbr 16280" [3] ("…modelo", "…pdf") — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=art%20de%20reforma)
  - A CBIC-cited stat says 13.3M addresses (1 in 8 households) are in condominiums (Censo 2022, via a search summary whose exact source page is unclear) — [Portas](https://portas.com.br/noticias/inadimplencia-condominial-bate-recorde-e-estimula-solucoes/)
- **New-unit handovers (vistoria de recebimento/entrega de chaves):**
  - CBIC 2025: 453,005 units launched (+10.6%) and 426,260 sold (record). Abrainc: deliveries up 13.7% in 2025 vs 2024 (search summary of CBIC/Abrainc releases) — [InfoMoney](https://www.infomoney.com.br/?p=3217679), [Abrainc release](https://cdn.abrainc.org.br/files/2026/3/Release_Indicadores_202602.pdf)
  - Autocomplete: "vistoria entrega de chaves" [10] (city-specific, "valor", "curso"); "vistoria de entrega de apartamento" [10] ("…quanto cobrar", "…curso"); "vistoria apartamento novo" [10] ("…engenheiro", "check list pdf") — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=vistoria%20de%20entrega%20de%20apartamento)
- **Vistoria cautelar duties:**
  - Instituto de Engenharia (June 2026) states the vistoria de vizinhança "é um procedimento obrigatório exigido do construtor antes do início das obras". It grounds this in CDC art. 39 VIII (selling services contrary to ABNT norms) and NBR 12722/2002 item 4.1.10 (vistoria preliminar whenever neighbours' interests need protection) — [IE 2026 PDF](https://www.institutodeengenharia.org.br/site/wp-content/uploads/2026/06/VISTORIA-CAUTELAR-IE-2026.pdf)
  - No municipal law making it a permit condition was found (WebSearch, 2026-10-12). Courts impose it in litigation — [TJMG via Legjur](https://www.legjur.com/jurisprudencia/eme/824.6239.3615.8507)
  - NBR 13752 (perícias na construção civil) has a 2024 revision per autocomplete ("nbr 13752 pdf 2024"), and a 2026 webinar teaches cautelar "de acordo com a NBR 13752" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=nbr%2013752), [YouTube](https://youtu.be/vGXhdJw-AJM)

### Inferences
- **PL 159/2026 is a binary option, not a base case.** If it passes, the Lite's 13 mandated items (including per-anomaly photos and priority classification) are exactly what a deterministic generator would produce, and the "Lite" keyword would be new and uncontested. But the bill has waited six months for a plenary slot. It includes a 180-day vacatio legis, and enforcement is municipal: the Rio precedent was 11.7% compliance. Plan the business so that it works without the law.
- **Frequency ranking (inference from search, YouTube and Hotmart signals):**
  1. Laudo/plano de reforma NBR 16280: per renovation in any condo, small ticket, highest content demand
  2. Vistoria de recebimento: per new unit, ~400k+ units/year, consumer-paid R$ 500–3,500
  3. Inspeção predial/autovistoria: per building every 5–10 years, large ticket, legally fragmented
  4. Cautelar: per construction project, batch of neighbours, ≥R$ 6,875 contracts, specialist firms
- The first two are where a solo product sees repeated monthly use. The last two are higher-value but rarer, and their buyers are concentrated among specialists (IBAPE members).

### Gaps
- Number of residential condominium buildings in Brazil, and of renovations per year that trigger NBR 16280. No authoritative count was found.
- Annual units delivered (CBIC counts launches and sales; Abrainc reports growth rates for 20 firms only).
- Current Rio and Porto Alegre compliance or LTIP filing counts.
- Whether any municipality requires vistoria cautelar for building permits.

## 4. Who competes, and how much traction do they have? (deep census)

### Takeaway
The engineering-specific segment is thinly occupied but **not empty**, and round 1 under-weighted it. **Onlaine** is a 15-year incumbent with public prices of R$ 89–219/user/month and a self-reported 3,000 laudos/month. **Howse** has negligible traction: its Android app "Howseapp" has **100+ downloads and 8 ratings**. Generic tools dominate installs: Checklist Fácil 500k+, Produttivo 100k+. A cheap photo-report app, FotoGeo (100k+ downloads, R$ 9.90/semester modules), is the de facto substitute. 2026 newcomers (Inspekio, InspectWrite, Hotmart "geradores") have no traction yet.

### Cited Findings
| Tool | Focus | Price (2026-10-12) | Traction proxy | Source |
|---|---|---|---|---|
| **Onlaine Inspeção** | Engineering inspections, perícias, laudos; condos, public bodies | R$ 89 / 139 / 219 per user/month (Avançado min. 5 users) | "+3000 laudos / mês", "+15 anos", "Nota 5.0" Google/App Store (all self-reported); no Play listing found under "onlaine" | [Onlaine](https://www.onlaine.com.br/onlaine-inspecao.html) |
| **Howse** (Howse Técnicas Aplicadas Ltda., RS) | Vistorias and laudos prediais with AI conclusions; PDF/Word export; checklists for entrega/recebimento | "De R$ 70/mês", 20% off annual | **Play "Howseapp" (com.leonelgregioauler.vistorias): 100+ downloads, 8 ratings, updated 18 Sep 2026**; Instagram @howseapp unreadable (HTTP 429) | [Howse](https://howseapp.com/), [Play](https://play.google.com/store/apps/details?id=com.leonelgregioauler.vistorias) |
| Inspect App (InMediam) | Generic smart forms + laudo templates | Demo/free trial | "10 mil usuários ativos", "2.500+ formulários… todos os meses" (self-reported); Play 1k+, 11 ratings | [Inspect](https://inspectapp.com.br/), [Play](https://play.google.com/store/apps/details?id=br.com.inmediam.inspect) |
| Inspeção Pro | FSM/inspection with automatic laudos | "a partir de R$ 334,00/mês" | Subscriber app 100+ downloads; 2018 demo video 32,885 views | [Planos](https://inspecao.pro/planos-e-valores/), [Play](https://play.google.com/store/apps/details?id=com.inspecaomobile), [YouTube](https://youtu.be/yrqjIHR3H9s) |
| Checklist Fácil | Enterprise checklists (has Construção Civil vertical) | Plans start "Até 5" users; prices not public | Play **500k+ downloads, 26.4k ratings** | [Planos](https://checklistfacil.com/planos/), [Play](https://play.google.com/store/apps/details?id=br.com.rz2.checklistfacil) |
| Produttivo | Generic FSM/OS; publishes relatório fotográfico templates | Not public (`/precos` returns 404) | Play **100k+, 423 ratings**; YouTube "Como fazer um relatório fotográfico" 22,993 views | [Play](https://play.google.com/store/apps/details?id=br.com.agivis.formapp_android), [YouTube](https://youtu.be/pGTjVBFzFIo) |
| **FotoGeo** (CronoRally) | "Relatórios Fotográficos em PDF ou Word… ideal para engenheiros e inspeções"; checklists, RDO | Freemium; modules from R$ 9.90/semester | **Play 100k+, 341 ratings**; tutorial video **428,234 views** | [Play](https://play.google.com/store/apps/details?id=fotogeo.com.br.app), [Site](https://fotogeo.com.br/), [YouTube](https://youtu.be/UAM2moJ-SRg) |
| Relatório Fotográfico de Obras (ATNM Engenharia) | Photo reports, atas de vistoria, RDO | IAP | Play 1k+, updated 10 Oct 2026 | [Play](https://play.google.com/store/apps/details?id=br.com.atnm.atadigital) |
| Diário de Obra Online | RDO/site diary | n/a | Play 100k+, 504 ratings | [Play](https://play.google.com/store/apps/details?id=br.com.updatedigital.sistemaDiarioDeObrasOnline) |
| Report & Run (BlixtBit, AU) | Generic photo-to-PDF reports | IAP | Play 500k+, 6.86k ratings | [Play](https://play.google.com/store/apps/details?id=com.jtt.reportandrun) |
| Inspekio (GoStart Lab) | "OS e Laudo Técnico" for maintenance teams | n/a | **Play 10+ downloads, updated 3 Oct 2026** (newcomer) | [Play](https://play.google.com/store/apps/details?id=com.inspekio.app) |
| "Relatório de Inspeção Predial" / InspectWrite (ClearStack Apps) | Offline home-inspection report writer (US-style sections) | IAP | **Play 1+ download, updated 23 Sep 2026** (newcomer) | [Play](https://play.google.com/store/apps/details?id=com.clearstackapps.inspectwrite) |
| Laudo Tech | Criminal-perito laudo generator (DOCX from PDFs) | Free | Play 500+ | [Play](https://play.google.com/store/apps/details?id=com.waldirdev01.laudo_tech) |
| e-Laudo (OKDS) | Agronomy field laudos, offline | IAP | Play 10k+, 55 ratings | [Play](https://play.google.com/store/apps/details?id=br.com.okds.elaudo) |
| Hotmart "Gerador de Relatório de Vistoria de Recebimento de Imóveis" (EGX Engenharia Diagnóstica) | Report generator sold as a digital product | US$ 7 | Listed 2026-09-15, 0 reviews | [Listing](https://hotmart.com/pt-br/marketplace/produtos/hagsxd-controle-de-patologias-engenharia-diagnostica-yrak8/I107453381Q), [checkout](https://pay.hotmart.com/I107453381Q) |
| Hotmart "TERMO DE VISTORIA DE IMÓVEIS PRO" | Software-format product (rental) | US$ 2 | Listed 2026-07-17, 0 reviews | [checkout](https://pay.hotmart.com/Y106784335N) |
| Rental apps (BeSoft, Pleno, Hauseful, VistoHouse, Vistortec, Rede Vistorias) | Locação | R$ 59.90–299/month (round 1) | Play 100k+/668; 10k+/431; 1k+/128; 1k+/89; 500+/11; 5k+/73 | [BeSoft](https://play.google.com/store/apps/details?id=br.com.besoft.bevistoria), [Pleno](https://play.google.com/store/apps/details?id=br.com.plenosoftware.vistoria), [Hauseful](https://play.google.com/store/apps/details?id=com.hauseful.fhost.app) |

- Play searches for "laudo de inspeção predial", "inspeção predial", "vistoria cautelar", "laudo técnico engenharia", "laudo de reforma" and "laudo cautelar vizinhança" surface mostly vehicle, rental and condo-management apps. No engineering laudo app with more than 1k downloads appeared besides the generic tools above — [Play search](https://play.google.com/store/search?q=laudo%20de%20inspe%C3%A7%C3%A3o%20predial&c=apps&hl=pt_BR&gl=BR)
- App Store data could not be read: the iTunes Search API returned HTTP 403, and apps.apple.com has no web search — [iTunes API](https://itunes.apple.com/search?term=howse&country=br&entity=software)
- Inspeção Pro's subscriber app and Onlaine both target teams and firms. Onlaine's top tier requires 5 users — [Onlaine](https://www.onlaine.com.br/onlaine-inspecao.html)

### Inferences
- **Howse is not proof of demand.** After at least one public release cycle, 100+ Android downloads and 8 ratings means very few users, whatever its pricing. A newcomer with a similar pitch (AI conclusions, R$ 70) has not visibly won customers. This is evidence *against* G2's "a recent newcomer could still win revenue" clause.
- **Onlaine is the real incumbent, and its weaknesses are exploitable:**
  - Per-user pricing with inspection caps (2 or 5/month at R$ 89/139) is expensive for a solo professional who does 10–30 small laudos/month (reformas, recebimentos)
  - Its web page has no Play app under its name
  - It sells to firms and public bodies
  - A per-report or flat solo plan for high-frequency, small documents is the gap
- **The practical substitute is Word plus a photo-report app.** FotoGeo has 100k+ installs at R$ 9.90/semester, and "relatório fotográfico" was the only query family where autocomplete showed tool intent ("aplicativo relatorio fotografico", "software relatorio fotografico"). The product must beat "FotoGeo + Word template" on normative structure (NBR 16280 plan fields, Lite/NBR 16747 sections, GUT priority, ART block), not on photos.
- **Hotmart is filling with "geradores" at US$ 2–7.** This anchors template and generator prices low on that marketplace. Selling there gives exposure but sets a cheap reference price.

### Gaps
- Real customer counts and revenue for Onlaine, Howse, Inspect, Inspeção Pro and FotoGeo (none publish them; no CNPJ or Receita data was pulled).
- FotoGeo's full current price list (only the 2023 developer reply was visible).
- App Store ratings for all tools.
- Howse's Instagram follower count.

## 5. What do Google Autocomplete signals show? (extensive scan)

### Takeaway
Across **302 autocomplete queries** (hl=pt-BR, gl=br, 2026-10-12), demand is rich for documents and norms ("modelo", "pdf", "word", "nbr … pdf") and for service prices ("valor", "quanto custa"). Demand is near zero for software. Of **96 software-type probes** ("<seed> app/software/programa/gerador/aplicativo/sistema"), only 11 returned anything new, and the only relevant tool intent was around **relatório fotográfico** ("aplicativo relatorio fotografico", "software relatorio fotografico", "app relatório fotográfico grátis") plus "app vistoria predial" and "app autovistoria".

### Cited Findings
Source for every line: the Google Autocomplete endpoint, with the seed swapped into q= — e.g. [laudo de reforma](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=laudo%20de%20reforma), [vistoria cautelar de vizinhança](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=vistoria%20cautelar%20de%20vizinhan%C3%A7a), [relatório fotográfico app](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=relat%C3%B3rio%20fotogr%C3%A1fico%20app). The number of suggestions is in brackets.

- **Scan design:** 75 base seeds plus 192 modifier probes (16 core seeds × 12 modifiers: app, software, programa, gerador, aplicativo, preço, sistema, modelo, word, pdf, grátis, valor) plus 35 follow-up seeds. 43 of the 75 base seeds returned the maximum 10 suggestions; 3 returned 0.
- **Modifier results:**
  - Software-type (6 modifiers × 16 seeds = 96 probes): 11 with any new suggestion, 22 suggestions in total
  - Of those 22, the relevant ones were: "software vistoria cautelar", "sistema vistoria cautelar" (likely vehicle), "relatorio fotografico app", "app relatório fotográfico grátis", "software relatorio fotografico", "aplicativo relatorio fotografico", "app autovistoria", "app vistoria predial". The rest were noise ("laudo técnico grupo gerador", "…sistema fotovoltaico")
  - Price (preço/valor): 16 of 32 probes returned 62 suggestions, mostly consumer service-price queries (e.g. "vistoria cautelar valor sp", which is the vehicle sense)
  - Document (modelo/word/pdf): 34 of 48 returned 141 suggestions
  - "grátis": 3 of 16 returned 10 ("relatório fotográfico excel grátis", "laudo de vistoria de imóvel para locação word grátis")
- **Zero suggestions:**
  - "software de inspeção predial", "programa para fazer laudo", "reforma em condomínio nbr 16280", "planilha gut inspeção predial", "modelo laudo editável", "laudo técnico com ia", "chatgpt laudo técnico", "pl 159/2026", "quanto cobrar vistoria cautelar de vizinhança", "como fazer laudo de vistoria cautelar", "laudo de vistoria de vizinhança modelo word"
  - Every app/software/programa/gerador/aplicativo/sistema/grátis variant of "laudo de inspeção predial", "vistoria de recebimento de imóvel", "vistoria entrega de chaves", "laudo nbr 16280", "plano de reforma", "laudo de reforma" and "laudo técnico de engenharia"
- **Rich document and norm seeds [10 each]:**
  - "nbr 16747" ("pdf", "atualizada", "download", "comentada"); "nbr 16280" ("atualizada", "pdf", "pdf free download"); "nbr 13752" ("pdf 2024", "atualizada")
  - "laudo de vistoria cautelar" ("…de vizinhança pdf", "…modelo", "…doc", "…valor")
  - "relatório fotográfico" and "relatório fotográfico de obra" ("word download", "excel grátis", "modelo")
  - "laudo técnico de engenharia" ("…civil como fazer", "…modelo", "…word")
  - "laudo de patologia", "laudo de infiltração", "laudo estrutural", "laudo predial", "tabela de honorários ibape" ("…sp 2026", "…pr 2026")
- **Practitioner-intent strings (people who sell the service):** "vistoria de entrega de apartamento quanto cobrar"; "quanto cobrar por um laudo de inspeção predial"; "quanto cobrar por um laudo técnico de engenharia"; "como cobrar por um laudo técnico"; "curso vistoria entrega de chaves"; "curso de vistoria de entrega e recebimento de obra"; "modelo proposta de laudo de inspeção predial"; "laudo técnico de vistoria acompanhado de art ou rrt"; "art de reforma como preencher"; "emitir art de reforma"
- **Consumer and local strings:** "vistoria entrega de chaves joinville/curitiba"; "vistoria apartamento novo sp/campinas/sorocaba"; "laudo de inspeção predial guarulhos"; "…com art em goiania"; "autovistoria predial rj/niteroi"; "lei de inspeção predial fortaleza/joao pessoa/salvador/pará"
- **Ambiguity trap:** "vistoria cautelar" alone is dominated by vehicle inspections ("…perto de mim", "…dekra", "…moto", "laudo cautelar veicular"). Only "…de vizinhança" strings are engineering.
- **Brand checks:** "howse" → "howseapp" appears only among game names; "produttivo" [10] ("login", "app", "preço"); "checklist fácil" [10] ("preço", "grátis"); "fotogeo" → "fotogeo app", "fotogeo web"
- **New-law strings:** "laudo de inspeção técnica de edificação (lite)" and "lite laudo de inspeção" exist [2 each]; "lei federal inspeção predial" [1]

### Inferences
- **G4 is weak on commercial intent.** People search for the document and the norm, not for a tool. The realistic funnel is "template or norm-guide search → free sample → paid generator". That funnel converts poorly (freebie seekers), which is exactly what round 1 feared. The scan **confirms rather than resolves** that fear.
- **The best paid-search targets are practitioner strings** ("modelo de laudo de vistoria de recebimento de imóvel", "plano de reforma nbr 16280 modelo", "laudo de reforma modelo", "modelo de laudo técnico de inspeção predial", "quanto cobrar…", "art de reforma como preencher"). They should be bought on **exact match** with consumer and vehicle negatives.
- "relatório fotográfico" is the one family with tool intent, but it is generic (FotoGeo/Produttivo territory) and free-leaning. It works as a top-of-funnel keyword, not as the core positioning.

### Gaps
- Absolute search volumes and CPCs: autocomplete gives no volume, and Keyword Planner requires an Ads account. This is the first measurement step of the plan in section 7.

## 6. Does the idea pass G1–G8 on desk evidence alone? (full candidate record)

### Takeaway
**Verdict: CONDITIONAL. It does not pass all gates on desk evidence, and it should not be killed on desk evidence.**

| Gate | Result | Basis |
|---|---|---|
| G3 buyer power | Pass | Fees of R$ 625/h and R$ 500–3,500 per vistoria |
| G5 buildability | Pass | No licence needed |
| G6 not AI-core | Pass | Deterministic generator |
| G1 WTP | Weak pass | Paid tools and substitutes exist (Onlaine 15 years, Checklist Fácil, Produttivo, FotoGeo), but every number is self-reported or a proxy |
| G7 feasibility | Pass with care | Asaas on CPF; Hotmart allows templates; ABNT copyright is contested, so do not reproduce norm text |
| G8 unit economics | Conditional | Needs 170–360 subscribers out of an online-active pool of ~3k–15k |
| **G2 saturation and newcomer evidence** | **Fails** | Onlaine incumbent; flood of 2025–26 Hotmart kits with no reviews; Howse at 100+ downloads |
| **G4 commercial-intent distribution** | **Fails** | 0 relevant software suggestions outside relatório fotográfico |

The gaps in G1, G2, G4 and G8 can only be closed by strangers paying. A **21-day paid test** (section 7) resolves all four. The recommended wedge changes from inspeção predial/cautelar to **laudo/plano de reforma NBR 16280 + vistoria de recebimento**, the high-frequency documents, with the Lite (PL 159/2026) as upside.

### Cited Findings
Evidence is cited in sections 1–5. Gate-specific primary sources:
- **G7, payments:** Asaas accepts CPF accounts, has native subscriptions, Pix R$ 1.99 and card 2.99% + R$ 0.49, from round 1 — [Asaas](https://www.asaas.com/precos-e-taxas). Hotmart lists "templates" and "software"-format products in this niche, e.g. "TERMO DE VISTORIA DE IMÓVEIS PRO" (format software) — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/hagsxd-termo-de-vistoria-de-imoveis-pro-ai97n/Y106784335N)
- **G7, Elo7:** not viable; the marketplace is shutting down — [Elo7](https://www.elo7.com.br/lista/modelo-de-laudo)
- **G7, ABNT copyright is contested:**
  - Courts have held that normative procedures are excluded from copyright under Lei 9.610/98, art. 8 (Justiça Federal/TRF-3; STJ AgInt no REsp 1.621.370-SP per search summary) — [Migalhas](https://www.migalhas.com.br/depeso/198566/justica-federal-confirma-que-normas-tecnicas-da-abnt-nao-sao-objeto-de-direitos-de-autor), [Sedep](https://www.sedep.com.br/?p=71493)
  - In Sept 2025 ABNT nonetheless stated that NBRs are protected works and that any total or partial reproduction requires authorisation — [CFF 10/09/2025](https://site.cff.org.br/noticia/Noticias-gerais/10/09/2025/abnt-alerta-para-distribuicao-nao-autorizada-de-norma-tecnica-sobre-exame-de-urina)
- **G5:** the Lite's required items are public law text, so the template structure can follow them without reproducing ABNT text — [PL 159/2026 text](https://legis.senado.gov.br/sdleg-getter/dadosabertos/documento/24d183db-0325-41b0-8993-83cb907dd560). The professional, not the tool, signs and issues the ART (art. 7 of the bill) — same source
- **G8, FX and target:** US$ 5k ≈ **R$ 24,950/month** at PTAX R$ 4.99 (2026-10-09) — [BCB PTAX](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='10-01-2026'&@dataFinalCotacao='10-12-2026'&$format=json)

### Inferences

#### Candidate record
- **Product definition (refined):** a mobile-first web app (PWA, offline photo capture) in which a CREA/CAU professional fills a normative form, attaches photos per room/system/anomaly, rates priority (GUT or NBR 16747 classes) and exports a branded **DOCX + PDF** with numbered photo grids, an ART/RRT block and signature fields.
  - **Wedge templates:**
    1. Laudo técnico / plano de reforma NBR 16280 (unit renovation in a condo)
    2. Vistoria de recebimento / entrega de chaves (new unit, also áreas comuns)
  - **Phase-2 templates:**
    3. Inspeção predial / autovistoria / **Lite** (13 items of PL 159/2026 art. 6)
    4. Vistoria cautelar de vizinhança in batch (one job → N neighbour reports)
  - No AI in the value proposition. Optional text snippets come from a curated phrase library, not an LLM.
- **Buyer:** solo civil engineers, architects and small diagnostic-engineering firms who issue 5–30 small laudos/month (reformas, recebimentos), plus learners coming out of Hotmart courses.
  - Online-active pool ~3k–15k (inference, section 1)
  - Registered base 1.2M (Confea) + 200k (CAU)
- **Pain evidence:**
  - Search demand for "modelo/word/pdf" versions of every document (section 5)
  - "relatório fotográfico de obra excel grátis" and "word download" show manual photo layout
  - Content creators sell the know-how at R$ 400–1,000 (section 2)
  - IBAPE prices a unit recebimento at 3 h (≈R$ 1,875), so writing time is a large share of the job (inference)
- **Competitors (verified vs self-reported):**
  - Onlaine R$ 89–219/user (self-reported 3,000 laudos/month, 15 years)
  - Howse R$ 70 (Play 100+, verified Play metric)
  - Inspeção Pro R$ 334+
  - Inspect (self-reported 10k users)
  - Checklist Fácil (verified Play 500k+/26.4k ratings)
  - Produttivo (Play 100k+)
  - FotoGeo (Play 100k+, R$ 9.90/semester modules)
  - Hotmart template kits US$ 7–42 and generators US$ 2–7
  - **No verified revenue anywhere.**
- **Their weaknesses:**
  - Onlaine: per-user caps of 2–5 inspections at R$ 89–139 penalise high-frequency solos; firm/public-sector focus
  - Howse: AI-first positioning, negligible adoption
  - Generic tools: no normative structure for NBR 16280/16747/Lite, no ART block
  - FotoGeo: photo grid only
  - Hotmart kits: static Word files, no photo automation
- **Demand signals:** strong for documents and norms, zero for software (section 5). YouTube interest is highest for laudo de reforma (8–12k views per video) and consumer entrega de chaves (68k–198k).
- **Acquisition channel:**
  - Exact-match Google Ads on practitioner document queries (test only)
  - SEO pages for "modelo de laudo de reforma", "plano de reforma NBR 16280 modelo", "modelo de laudo de vistoria de recebimento", "Lite modelo" (slow)
  - Hotmart listing for exposure
  - Affiliate deals with course creators
  - 1:1 outreach
- **Build complexity:** medium-low. Form engine, IndexedDB photo queue with compression, DOCX templating, PDF conversion (server-side LibreOffice or docx-to-pdf), Asaas billing. **2–3 weeks** for the two wedge templates; +1 week per extra template.
- **Time to first revenue:** template pack in **1–2 weeks** (if it sells); generator pre-sale in 2–3 weeks; subscriptions in 5–7 weeks.
- **Risks:**
  1. Template seekers do not pay (the core risk)
  2. Onlaine adds a cheap solo plan
  3. Hotmart price anchoring at US$ 7
  4. Clone risk from AI-built micro-SaaS
  5. ABNT copyright claims if norm text is copied
  6. LGPD: neighbours' and owners' photos are personal data; the tool is the operator and the engineer the controller
  7. Photo-storage cost
  8. PL 159/2026 may stall indefinitely
  9. Professional-liability perception (the tool must not "conclude" anything)

#### Gate-by-gate verdict
- **G1 WTP — weak PASS.** At least 2 independent paid products and substitutes exist with multi-year operation (Onlaine, Checklist Fácil, Produttivo, FotoGeo IAP, Inspeção Pro). All revenue is unverified. Template WTP is unproven: only 1 of 66 kits dated since 2025 has a review.
- **G2 not saturated + newcomer can win — FAIL on desk evidence.** No dominant engineering incumbent with verified scale exists, which is good. But Onlaine has a 15-year head start at a similar price. The 2025–26 template and "gerador" flood shows supply chasing the niche without visible buyers, and the closest recent software newcomer (Howse) shows ~no adoption. No evidence was found that a newcomer has won revenue.
- **G3 buyer power — PASS.** R$ 625/h technical hour (IBAPE-SP 2025); R$ 500–3,500 per apartment vistoria (2026); ≥R$ 6,875 per cautelar contract.
- **G4 distribution without contacts — FAIL on commercial intent; PASS on measurable demand.** Measurable search exists, but intent is "free document". This must be proven with paid conversion.
- **G5 buildable solo ≤4 weeks, no licences — PASS.** The engineer holds the CREA/CAU and signs the ART; the tool does not need certification. ICP-Brasil digital signature is optional (gov.br signature or the professional's own certificate).
- **G6 not AI-core — PASS.** Deterministic templates; a phrase library instead of an LLM.
- **G7 legal/ToS/payments — PASS with conditions.**
  - Asaas on CPF for the test, then an ME company
  - Hotmart permits templates
  - Elo7 is unavailable
  - Do not reproduce NBR text: structure templates from PL 159 art. 6, IBAPE public material and the professional's own wording
  - Add a DPA clause and LGPD notice for photo data
- **G8 unit economics — CONDITIONAL.**
  - R$ 24,950 MRR needs ~252 subscribers at R$ 99, ~168 at R$ 149 or ~362 at R$ 69. That is **1–12% of a ~3k–15k online-active pool**: plausible only over 12–24 months.
  - Margin is positive: payment fees ~4%, Simples Anexo III ~6% (round-1 notes), and storage is cheap with image compression.
  - CAC is unknown until CPC is measured.
  - Per-report pricing (R$ 19–29) needs ~860–1,300 reports/month, which only works with heavy users.
- **Overall: CONDITIONAL.** The single cheapest test that resolves G1, G2, G4 and G8 is in section 7.

#### Scores (1–5)
| Criterion | Score | Change vs final round 1 | Why |
|---|---|---|---|
| WTP evidence | 3 | = | Real fees, paid tools and course WTP; no verified revenue; template WTP unproven |
| Low saturation | 2 | −1 | Onlaine incumbent at R$ 89–219; 55 Hotmart products dated in 2026; generic giants; FotoGeo at R$ 9.90/semester |
| Buyer power | 4 | = | R$ 625/h; R$ 500–3,500 per vistoria |
| Distribution without contacts | 2 | −1 | Zero software intent across 96 probes; YouTube creators at 3–4k subscribers |
| Buildability | 4 | +1 | Two wedge templates in 2–3 weeks; Lite items are public law text |
| Speed to first revenue | 3 | +1 | Template pack and per-report generator can be sold in 1–2 weeks |
| Low risk | 3 | = | Upside from PL 159/2026; downside from freebie demand and the ABNT stance |
| **Total** | **21/35** | = | |

### Gaps
- Verified revenue of any competitor, plus Brazilian CPC and search volumes (Keyword Planner), would move G1, G4 and G8 on desk evidence. None were obtainable.
- Whether the Senate will schedule PL 159/2026.

## 7. What is the ready-to-execute go/no-go plan (with a cheaper first-revenue variant)?

### Takeaway
Run a **21-day "kit now + generator pre-sale" test** for ≤R$ 400 of Google Ads plus ≤R$ 100 of fixed costs, targeting practitioner document queries in three clusters on exact match. The clusters are reforma NBR 16280, vistoria de recebimento, and inspeção predial/cautelar/relatório fotográfico. The kit produces real revenue in the first week, and the founder pre-sale tests subscription WTP. **GO** requires ≥10 paid kit orders **and** ≥3 founder pre-sales (or ≥5 report-credit packs) from strangers within 21 days. **KILL** if ≤2 kit orders and 0 pre-sales after ≥250 qualified clicks and ≥20 one-to-one conversations.

### Cited Findings
- **Benchmarks that set the thresholds** (from the round-1 notes): planning for the lower quartile (≤2.5% paid conversion) is prudent, and with zero conversions in n tries the true rate is below 3/n (rule of three) — [ChartMogul](https://chartmogul.com/reports/saas-conversion-report/), [Rule of three](https://en.wikipedia.org/wiki/Rule_of_three_(statistics))
- **CPC is unknown for Brazil.**
  - The global Google Search average is US$ 5.26 (2025) and "Home & Home Improvement" is US$ 7.85 (WordStream, via Sender, search summary) — [Sender](https://www.sender.net/marketing-glossary/cost-per-click-cpc/statistics/)
  - The Brazil-by-industry CPC table is paywalled — [Statista](https://www.statista.com/statistics/1115426/brazil-search-advertising-cpc)
- **Price anchors:**
  - Howse R$ 70/month — [Howse](https://howseapp.com/)
  - Onlaine R$ 89/139/219 per user/month — [Onlaine](https://www.onlaine.com.br/onlaine-inspecao.html)
  - Hotmart kits US$ 7–42 and "Plano de reforma + ART" US$ 127 — [checkout](https://pay.hotmart.com/G91854671A)
  - PTAM per-report credits R$ 49.97–179.90 (round 1) — [LaudoImóvel](https://laudoimovel.com/para-corretores)
- **Payment and refund:** Asaas payment links with Pix and card, no monthly fee (round 1) — [Asaas](https://www.asaas.com/precos-e-taxas). The CDC art. 49 gives a 7-day right of withdrawal online — [CDC](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm)
- **Communities with verified sizes:**
  - YouTube: Engenheira Karine Baptista 3k subscribers — [YouTube](https://www.youtube.com/@EngenheiraKarineBaptista); Realizar Engenharia 3.82k — [YouTube](https://www.youtube.com/@RealizarEngenharia)
  - IBAPE >2,000 members — [IBAPE](https://biblioteca.ibape-nacional.com.br/wp-content/uploads/2025/02/Brazil_s-regulation-qualification-and-certification-in-valuation-Agnaldo-Benvenho.pdf)
  - Hotmart course audiences (lower bounds): Avance Engenharia "Laudo Técnico de Reforma" 44 reviews — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/curso-laudo-tecnico-de-reforma/U5001560T); Cremonezi "Laudo de Vistoria Cautelar" 25 — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/hagsxd-laudo-de-vistoria-cautelar-qdtxi/H12589109O); Matheus Leoni combos 27 — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/combo-inspecao-predial-na-pratica/A62836289H)
  - Facebook and LinkedIn group sizes could not be verified (section 1)

### Inferences

#### A. Offer and landing pages (build days 0–4)
Build three landing pages, one per cluster, on one domain. Each page has:
- a 15-second GIF of the generator turning a form + photos into a DOCX
- a sample PDF (watermarked)
- "você assina e emite sua ART; a ferramenta só monta o documento"
- an LGPD note
- price, two CTAs and a FAQ

**Product 1: instant-delivery kit (real revenue in week 1).**

| Item | Price | Contents |
|---|---|---|
| Kit Laudo/Plano de Reforma NBR 16280 | R$ 47 | DOCX template with fields for memorial, systems affected, responsibilities, ART/RRT block and photo grid; síndico checklist; "como preencher a ART de reforma" guide written in own words |
| Kit Vistoria de Recebimento (unit + áreas comuns) | R$ 47 | DOCX with room-by-room checklist, non-conformity table, photo grid and re-vistoria form |
| Kit Inspeção Predial / Lite | R$ 67 | Sections following PL 159/2026 art. 6 (13 items), GUT matrix (XLSX) and photo-numbering macro |
| Bundle of all three | R$ 97 | All of the above |

Price rationale: above the Hotmart floor (US$ 7–22), below "Plano de reforma + ART" (US$ 127).

**Product 2: generator founder pre-sale (tests subscription WTP).**
- "Gerador de Laudos – Plano Fundador": **R$ 390/year**, locked for life. Compare a list price of R$ 79/month or R$ 790/year: below Howse's R$ 70/month and Onlaine's R$ 89–139/user.
- **Or** "5 laudos por R$ 99" (R$ 19.80 each), credits valid 12 months.
- Delivery date stated (e.g., "acesso em até 30 dias"). An automatic 100% refund if access is not delivered by that date, plus the 7-day CDC withdrawal right.
- Kit buyers get the kit price credited toward the founder plan (upsell on the thank-you page and by email on day 2).

**Mechanics:**
- **Asaas payment links** on a CPF account: Pix and card, 2× installments allowed on the annual plan.
- The checkout form asks for name, e-mail, WhatsApp and an optional CREA/CAU number (qualification signal).
- The Asaas webhook triggers the thank-you page and the kit download link.
- The same kits are mirrored on **Hotmart** for marketplace exposure. Hotmart fees are higher (≈9–15% per round 1), so it is not the primary checkout.
- Refunds are issued by Pix within 48 h of the request.
- Track the events view → click "Comprar" → checkout started → paid, with UTMs per ad group.

#### B. Google Ads structure (R$ 350 over 14 days ≈ R$ 25/day; R$ 50 kept in reserve)
- **Before launch (day 4):** open Google Ads and read **Keyword Planner** CPC and volume for every keyword below.
  - Drop any keyword whose top-of-page bid is above R$ 5.
  - If the median core CPC is above R$ 4, cut cluster C and put its budget into A.
- **Settings:**
  - Search network only (no Display or search partners); Brazil; Portuguese
  - Manual CPC with a max of R$ 2.50, raised to R$ 3.50 only if impression share is below 30%
  - Schedule Monday–Saturday 07–22h
  - Three RSAs per ad group with the price in a headline ("Modelo + Gerador de Laudo de Reforma – R$ 47"); sitelinks to the sample PDF and pricing
  - Conversion = Asaas paid (thank-you page)
- **Shared negatives:** veicular, automotiva, carro, moto, dekra, detran, transferência, locação, aluguel, alugado, locatário, inquilino, perto de mim, preço, valor, quanto custa, lei, é obrigatório, o que é, livro, concurso, abnt pdf, free, download, coffee
  - "valor/preço" are consumers buying the service, not the tool. The exception is the "quanto cobrar" keywords, which are practitioners.

| Campaign (budget) | Ad group | Exact-match keywords (all observed in autocomplete on 2026-10-12) |
|---|---|---|
| **A. Reforma NBR 16280 (R$ 140)** | A1 Modelo laudo de reforma | [modelo de laudo de reforma de apartamento], [laudo de reforma modelo], [laudo técnico de reforma modelo], [laudo técnico para reforma de apartamento pdf], [laudo de reforma de apartamento pdf] |
| | A2 Plano de reforma | [plano de reforma nbr 16280 modelo], [plano de reforma nbr 16280], [plano de reforma nbr 16280 pdf], [laudo de reforma nbr 16280], [laudo nbr 16280] |
| | A3 ART / como fazer | [art de reforma modelo], [art de reforma como preencher], [como fazer um laudo de reforma], [como fazer um laudo para reforma de apartamento], [laudo de engenheiro para reforma em apartamento] |
| **B. Vistoria de recebimento (R$ 110)** | B1 Recebimento de imóvel | [modelo de laudo de vistoria de recebimento de imovel], [laudo de vistoria de recebimento de imovel pdf], [laudo de vistoria de recebimento de imovel novo], [modelo de vistoria de recebimento de imovel] |
| | B2 Entrega de obra / áreas comuns | [laudo de vistoria de entrega de obra], [laudo de entrega de obra modelo], [relatório de vistoria de entrega de obra], [laudo de vistoria de recebimento de obra] |
| | B3 Practitioner pricing | [vistoria de entrega de apartamento quanto cobrar], [curso vistoria entrega de chaves] (only to measure; pause if CTR <3%) |
| **C. Inspeção/cautelar/fotos (R$ 100)** | C1 Inspeção predial | [modelo de laudo de inspeção predial], [laudo de inspeção predial modelo], [laudo de inspeção predial word], [modelo de laudo técnico de inspeção predial], [quanto cobrar por um laudo de inspeção predial], [laudo de inspeção técnica de edificação (lite)] |
| | C2 Cautelar de vizinhança | [modelo laudo de vistoria cautelar de vizinhança], [laudo de vistoria cautelar de vizinhança doc], [laudo cautelar de vizinhança modelo], [modelo de relatório de vistoria cautelar] |
| | C3 Relatório fotográfico | [modelo de relatório fotográfico de obra word], [relatório fotográfico de obra modelo], [aplicativo relatorio fotografico], [software relatorio fotografico] |

- **Ad-health thresholds:** CTR ≥4% on exact match, avg. CPC ≤R$ 3 and **≥250 qualified clicks** in total (≥100 on cluster A). If CTR is below 2% after 300 impressions, rewrite the ads once.

#### C. Organic and 1:1 channel (parallel, R$ 0)
- **Day 1:** search Facebook, LinkedIn and Telegram for groups using "inspeção predial", "perícias de engenharia", "engenharia diagnóstica", "vistoria cautelar", "NBR 16280", "engenheiros civis autônomos". Log member counts and posts in the last 7 days. Use only groups with ≥5k members and recent activity. (Sizes are unverified today; do not assume any group exists until it is logged.)
- **20–40 one-to-one conversations:** offer the free sample PDF and ask two questions: "quantos laudos de reforma/recebimento você emite por mês?" and "quanto tempo leva para montar?"
- **Creator affiliates:** cold-email 5 Hotmart creators (Avance Engenharia, Eng. Giovanni Cremonezi, Realizar Engenharia, Karine Baptista, Matheus Leoni) offering a 40% commission on the kit and founder plan via an Asaas split or coupon. One yes is a distribution channel. Zero yeses after 5 is an informative signal, not a kill criterion.
- **SEO seed:** publish the three landing pages plus one free, genuinely useful article each ("Plano de reforma NBR 16280: o que precisa conter", "Checklist de vistoria de recebimento", "O que muda com o Lite (PL 159/2026)"). This is for the long term only; it will not affect the 21-day result.

#### D. Pass/fail thresholds and timeline
| Day | Action |
|---|---|
| 0–4 | Domain (estimated R$ 40–100/year, not re-quoted), three landing pages, three kits (DOCX/XLSX), Asaas account and links, Ads account, Keyword Planner check |
| 5 | Launch Ads; start 1:1 outreach and creator e-mails |
| 12 | Midpoint review: cut ad groups with CTR <2% or zero checkout starts after 40 clicks; move budget to the best cluster |
| 19 | Ads off |
| 21 | Decision |

| Decision | Condition (strangers only; friends and family excluded) |
|---|---|
| **GO** (build the MVP for buyers in weeks 4–7) | ≥10 paid kit orders (≥~R$ 470) **and** ≥3 founder pre-sales (≥R$ 1,170) or ≥5 credit packs; **or** paid conversion ≥3% of ad clicks with ≥1 pre-sale |
| **ITERATE** (one 7-day cycle with the R$ 50 reserve plus organic) | 3–9 kit orders, or 1–2 pre-sales, or ≥8% of visitors downloading the free sample |
| **KILL** | ≤2 kit orders **and** 0 pre-sales after ≥250 qualified clicks **and** ≥20 conversations; **or** median CPC >R$ 5, which makes CAC for a R$ 47 kit unrecoverable |

- **Rule-of-three reading:** 0 sales in 250 clicks means a true conversion below 1.2%. At R$ 2.50 CPC that implies a CAC above R$ 208, so a R$ 390/year plan would barely break even and a R$ 47 kit would lose money.
- **Cluster-level decision:** if only cluster A (reforma) passes, build only the reforma generator first. It is the highest-frequency document.

#### E. Cheaper first-revenue variant (proves WTP in 7–14 days for ≤R$ 150)
- **Option 1: kit only.** Ship the R$ 47 reforma kit on Asaas and Hotmart, plus ads on cluster A only (R$ 10/day × 10 days = R$ 100).
  - Pass: ≥5 paid orders from strangers in 10 days. Fail: 0–1.
  - It proves only template WTP, which is the weakest form of WTP.
- **Option 2 (preferred): per-report generator as a plain web form.** No app and no offline mode. The user fills the NBR 16280 reforma form, uploads up to 30 photos and pays **R$ 19 by Pix (Asaas)**; a branded DOCX + PDF is generated server-side.
  - Buildable in 5–7 days with Claude Code (docxtemplater or python-docx, image resize, Asaas checkout webhook).
  - Pass: ≥5 paid reports in 14 days, or ≥2 buyers who return for a second report.
  - It proves per-use WTP for the actual product mechanic, not for a static file, and it doubles as the MVP core.
- Either option can run in week 1 of the main plan and feed the GO decision.

#### F. Unit economics to check against the test
- **Target:** R$ 24,950 MRR ≈ 252 subscribers at R$ 99, 168 at R$ 149 or 362 at R$ 69; or a mix, e.g. 150 subscribers at R$ 99 + 300 credit packs of R$ 99/year.
- **Costs per R$ 99 subscriber/month (estimates):**
  - Asaas card fee ≈ R$ 3.45 (2.99% + R$ 0.49)
  - Simples Anexo III ≈ 6% once on an ME
  - Storage: 20 laudos × 40 photos × 250 KB ≈ 200 MB/month per user, cents per month on object storage
  - Gross margin above 85%
- **Acceptable CAC** ≤ R$ 300 (≈3 months of payback at R$ 99). The test's measured CPC × (1 / paid conversion) must be at or under this number to scale with ads; otherwise the business depends on SEO and affiliates, which take 6–12 months.

### Gaps
- Real Brazilian CPCs and search volumes for the keywords above: the day-4 Keyword Planner step closes this.
- Facebook, LinkedIn and Telegram group names and sizes: the day-1 manual census closes this.
- Whether Google Ads restricts ads for downloadable templates (no policy issue is known, but it was not checked against current Google Ads policies).
- Domain price at registro.br was not re-quoted in this round.
