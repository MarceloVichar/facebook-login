# Brazilian analogs of European "regulation forces a document" newcomer wins (data as of 2026-10-12)

Method note (applies to every section):
- **Inputs read first:** [[Ranking]], [[Armadilhas e ideias mortas]], round-2 `trustmrr_newcomers.md` and `trustmrr_newcomers.csv` (684 rows, 267 passing all screens). The killed list already includes PMOC software, generic condominium software, vistoria apps, dedetização certificates, SST/PGR and NR-1 tools. Round 1 left "Calendário de conformidade para síndicos" CONDITIONAL (23/35, crowded, weak search).
- **Demand:** Google Autocomplete (`client=firefox&hl=pt-BR&gl=br`), queried 2026-10-12. These are suggestion lists, not volumes. "N sugg." means the number of suggestions returned (max 10).
- **Tools:** 14 WebSearch calls; curl for pages; headless Chrome (`--no-sandbox --dump-dom`) for client-rendered pages (Hotmart, Profez, p7m.io); Google Play pages via curl.
- **FX assumption:** R$5.4 = US$1, implied by the brief (R$700 ≈ US$130). US$5k/month ≈ R$27k/month.
- **European proofs, TrustMRR-verified, fetched 2026-10-12 (from the round-2 CSV):**
  - FireCert (UK, founded 2026-02-24): $5,003 in 30 days, $4,896 MRR, 42 subscriptions, £79/£129 per month. Sells to fire contractors for alarms, emergency lighting, extinguishers and security systems.
  - Spanish food-handler training (founded 2026-04-09): $37,333 in 30 days, one-time sales.
  - Tifox (FR, 2026-03-15): $1,586 in 30 days, €12–25 per class per year.
  - BasinCheck (PL→US, 2025-12-21): $2,235 in 30 days, $125–500 per month.
  - P7M.io (IT, 2026-03-28): $4,627 in 30 days; the live site now shows €3.99 per file and **€15.99/yr** (it was €12.99 in the CSV) — [p7m.io](https://p7m.io) (rendered 2026-10-12)
  - Source for all five: [TrustMRR](https://trustmrr.com/startup/firecert)

## Q1. FireCert → Brazil: AVCB/CLCB and fire-safety renewals. Is there demand for a deadline and document tracker, who sells it, and how large is the pool?

### Takeaway
The pain splits into two products, and both fall short of APPROVED:
- **(1a) A building or establishment license tracker** (AVCB, alvará, licença sanitária, SPDA, elevator, brigade). It has almost no commercial search demand. In a forum validation post from July 2026, accountants said they use spreadsheets, already have alerts in their systems, or refuse the job. Where the job is paid for, it comes bundled with consulting or condominium software.
- **(1b) The true FireCert analog: inspection and certificate software for fire-protection service firms.** It is a real B2B pool: 1,776 active Inmetro registrations. But a focused Brazilian incumbent (Inspefire) already sells exactly this at R$24–49 per managed client per month, and commercial search is thin.

Verdict: 1a **KILL** (no new evidence beyond round 1's síndicos calendar; same failure mode). 1b **CONDITIONAL**, deep-validated below.

### Cited Findings
**Demand (Autocomplete, 2026-10-12)**
- Informational AVCB queries are rich:
  - "avcb vencido": "…da multa", "…consequências", "…como renovar", "…o que fazer", "denuncia avcb vencido"
  - "renovação avcb": by state (sp, mg, bahia, pe, sc…) plus "…quanto tempo" and "…é anual"
  - "laudo spda": "…validade", "…preço", "…periodicidade", "…quem pode assinar"
  - Source: [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=avcb%20vencido)
- **Software-intent queries are nearly empty:**
  - "software avcb" 0 sugg.; "sistema avcb" 1; "gestão de avcb" 1; "vencimento avcb" 1
  - "controle de alvarás" 3 ("planilha…", "sistema de controle de alvarás"); "gestão de alvarás" 2
  - "controle de licenças e alvarás" 0; "controle de vencimento de licenças" 0; "sistema de controle de licenças" 1
  - Source: [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=controle%20de%20alvar%C3%A1s)
- Generic deadline-tracking intent is spreadsheet and free intent. "controle de vencimento de documentos" returns "…excel", "planilha… grátis", "programa para…", "sistema de…". "planilha controle de vencimento" returns "…download grátis" variants — [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=controle%20de%20vencimento%20de%20documentos)
- Extinguisher-side demand:
  - "controle de extintores" returns 10 sugg., but they are "…excel", "…planilha", "…grátis", "dashboard… grátis", "planilha… gratis".
  - "inspeção de extintores" returns 10 sugg., including "…por qr code", "…mensal", "…nível 1 2 e 3" and "…pdf".
  - "software de extintores" returns 3 sugg. ("software manutenção extintores"); "sistema de gestão de extintores", "app extintores" and "qr code extintor" return 1 each.
  - "software para empresa de manutenção de extintores" and "sistema para manutenção de extintores" return 0.
  - Source: [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=controle%20de%20extintores)

**Pain evidence (primary, adversarial)**
- On 2026-07-31 someone posted on Fórum Contábeis asking whether a "simple and cheap" AVCB and alvará expiry list per client would solve a real pain. That is someone else validating this exact idea. The four replies:
  - an analyst with 500+ clients keeps a master spreadsheet despite using Domínio and Acessórias;
  - a contador says "Controlamos pelo sistema contábil, que nos notifica… Nunca tivemos problemas";
  - a contador refuses: "isso não é responsabilidade da contabilidade… o cliente até pede, mas negamos";
  - an assistant says the city hall is the reminder, because "maioria dos clientes se nega em deixar atualizado devido o custo".
  - Source: [Fórum Contábeis](https://www.contabeis.com.br/forum/Legaliza%C3%A7%C3%A3o%20de%20Empresas/415115/como-voces-controlam-vencimento-de-alvara-avcb-de-varios-clientes-ao-mesmo-tempo/) (fetched 2026-10-12; 288 views, 4 replies)
- A 2023 SP2 survey found ~87% of buildings on three streets in Brás without a valid AVCB. I saw this only as a secondary snippet, cited by [Saber Tecnologias](https://sabertecnologias.com.br/conteudo/consultar-avcb-como-verificar-a-validade-do-documento), so it is unverified. It signals non-compliance, not a willingness to pay.
- The AVCB itself says the owner or user is responsible for renewing it and keeping the measures maintained, "sob pena de cassação do AVCB" — [AVCB nº 625909 (FUNEP)](https://www.funep.org.br/arquivos/documentos/AVCB_625909_2023_2026.pdf)

**Existing tools and prices (license and deadline tracking)**
- Sanity Consultoria bundles its "Gedot" document and license-validity platform with an audit and consulting service for retail chains (2022 article) — [Mercado & Consumo](https://mercadoeconsumo.com.br/2022/06/15/plataformas-digitais-auxiliam-empresas-no-controle-de-documentos-e-licencas/). No public price.
- A "Gestão de Regularidade Patrimonial" provider advertises AVCB, CLCB and alvará validity control as part of a regularization service — [OHub](https://www.ohub.com.br/anuncio/gestao-de-regularidade-patrimonial-completa-56443). Service, no price.
- Round 1 (condominium side): SindicoPRO R$79–159, SindicosPro R$97–347, MeuSíndico.IA from R$249 — [[Calendário de conformidade para síndicos]].
- I found **no standalone, self-serve, publicly priced AVCB or alvará tracker** for multi-unit retail, clinics or schools. Two searches came back empty — [search 1](https://www.contabeis.com.br/forum/Legaliza%C3%A7%C3%A3o%20de%20Empresas/415115/como-voces-controlam-vencimento-de-alvara-avcb-de-varios-clientes-ao-mesmo-tempo/), [search 2](https://mercadoeconsumo.com.br/2022/06/15/plataformas-digitais-auxiliam-empresas-no-controle-de-documentos-e-licencas/). This is an absence of competitors that matches the absence of demand.

**Existing tools and prices (fire-protection service firms: the FireCert analog)**
- **Inspefire** is the Brazilian equivalent of FireCert:
  - It covers periodic and monthly inspection of extinguishers and other fire equipment "Conforme os requisitos da NBR 12962/2016". It targets "Empresas Prestadoras de Serviço, Profissionais do SESMT, Bombeiros Civis".
  - Prices: START R$49, PLUS R$44 (≤5 accounts), MEGA R$39 (≤10), PRO R$34 (≤15), ULTRA R$29 (≤20), MASTER R$24 (≤30), all **per account/CNPJ per month**. 30-day free trial. Add-on modules: Brigada de Incêndio, LGE, cozinha industrial, WhatsApp notifications, "Inspe IA".
  - Source: [inspefire.com.br](https://www.inspefire.com.br) (fetched 2026-10-12)
  - Google Play: 55 reviews, updated 10 Oct 2026 — [Play](https://play.google.com/store/apps/details?id=br.com.inspfire). It also has an iOS app — [App Store](https://apps.apple.com/mo/app/inspefire/id1565415816). Its brand already gets autocomplete ("inspefire login", "aplicativo inspefire").
- **Generic checklist and field-service apps:**
  - Produttivo publishes a "checklist de extintores" template with QR code, photos and auto reports — [Produttivo](https://www.produttivo.com.br/modelo/checklist-extintores/)
  - Inspeção Pro: a plan is required before download — [Play](https://play.google.com/store/apps/details?id=com.inspecaomobile), [site](https://inspecaopro.com.br)
  - Extinguisher 360 (international, free tier plus pro plan) — [Play](https://play.google.com/store/apps/details?id=xyz.codexia.extinguisher360)
  - Round 1 also lists Auvo, Field Control and Tecniko — [[Armadilhas e ideias mortas]].

**Pool size**
- **Fire-protection service firms:** "1776 registros ativos" of Inmetro-registered extinguisher inspection and maintenance companies as of 2025-07-16, concentrated in the South and Southeast, led by São Paulo.
  - Inmetro says new registrations are falling, "possivelmente por saturação do mercado".
  - Since Portaria 258/2020 removed registration renewal, suspensions and cancellations have dropped to almost zero (0 in 2025).
  - Source: [Inmetro ARR final report, 2026](https://www.gov.br/inmetro/pt-br/assuntos/regulamentacao/avaliacao-de-resultado-regulatorio/2026/inspecao-tecnica-e-manutencao-de-extintores-de-incendio/sei_inmetro-2373600-relatorio-final.pdf)
- A 2020 Belo Horizonte council statement claims "das mais de 110 empresas que prestam serviços na área, pouco mais de 10 possuem cadastro" — [CMBH](https://cmbh.mg.gov.br/print/comunica%C3%A7%C3%A3o/not%C3%ADcias/2020/11/comiss%C3%A3o-ir%C3%A1-propor-pl-para-regulamentar-empresas-do-setor). So the informal pool is larger than the Inmetro count.
- **AVCBs in SP:** I found no official issuance statistics. Via Fácil publishes none that I could find — [search](https://sabertecnologias.com.br/conteudo/consultar-avcb-como-verificar-a-validade-do-documento). Serial numbers give a proxy:

| AVCB nº | Issued | Valid until |
|---|---|---|
| 619188 | Dec 2022 | 20/12/2025 |
| 625909 | about Feb 2023 | 17/02/2026 |
| 833007 | 2026 (file is labelled "2026_2029") | — |

  - Sources: [IPT AVCB](https://ipt.br/wp-content/uploads/2023/09/AVCB_619188_Dez2022_Predios-12_14_16_18_29_30_47A_53_53A_62.pdf), [FUNEP AVCB 625909](https://www.funep.org.br/arquivos/documentos/AVCB_625909_2023_2026.pdf), [FUNEP 833007](https://www.funep.org.br/arquivos/documentos/AVCB_833007_2026_2029.pdf). The 833007 PDF did not parse, so its date comes only from the filename.

### Inferences
- **Serial-number proxy:** about 6,700 AVCBs in about 2 months (Dec 2022 → Feb 2023), and about 207k between early 2023 and 2026. That gives roughly **40–70k AVCBs a year in SP**, so perhaps 150–300k SP buildings hold a valid AVCB at any time. This assumes the numbering is sequential statewide and excludes CLCBs. It is an inference, not an official figure.
- **1a (establishment tracker) is the round-1 síndicos calendar wearing a new hat.** The payer is unclear:
  - accountants refuse the task or already have alerts;
  - small owners let licenses lapse on purpose ("devido o custo");
  - multi-unit chains buy it bundled with consulting (Sanity) or use condominium suites.
  - Search intent is spreadsheet-shaped. That makes **G4 a fail** and **G1 weak** (no standalone paid product found), so the verdict is KILL.
- **1b is FireCert's real shape:** a contractor who services many client sites pays monthly to issue certificates and remind clients. Inspefire's per-managed-client pricing (R$24–49) shows the Brazilian market already pays for this (G1 pass, weakly). A newcomer would have to beat an incumbent that has 55 Play reviews, NBR 12962 positioning and add-on modules. Commercial search is 0–3 suggestions, so it would have to sell by outbound to the public Inmetro registry.
- FireCert's UK price (£79–129 per month, flat) is about 3–5 times what Inspefire charges a small firm. Brazilian price levels compress G8.

### Gaps
- No official SP or national AVCB/CLCB issuance statistics; an LAI request to the CBPMESP would be needed.
- Inspefire's paying-customer count and revenue are not public.
- No search volumes or CPCs; no keyword tool was available.
- The Inmetro ARR's per-state table is an image; I did not extract the SP count.

## Q2. Spanish food-handler training → Brazil (RDC 216 "curso de manipulador de alimentos"): course, certificate or training-record software?

### Takeaway
**KILL.** Spain's carnet is a per-worker job requirement. Brazil's RDC 216 requires a course only for the **responsável** of each establishment. Other handlers need documented "periodic" in-house training, with no certificate format required. The course market is flooded with free official options (Sebrae, Unieducar free tier, city halls). Search intent is "gratuito com certificado". A training-record tracker collapses into the saturated SST "controle de treinamentos" space and spreadsheet intent.

### Cited Findings
- **RDC 216/2004:**
  - 4.6.7: "Os manipuladores de alimentos devem ser supervisionados e capacitados periodicamente… A capacitação deve ser comprovada mediante documentação."
  - 4.11 (Manual de Boas Práticas): the training program must state "carga horária, o conteúdo programático e a freqüência… mantendo-se em arquivo os registros da participação nominal dos funcionários."
  - 4.12.2: "O responsável pelas atividades de manipulação dos alimentos deve ser comprovadamente submetido a curso de capacitação" on four topics.
  - Source: [RDC 216, BVS/MS](https://bvsms.saude.gov.br/bvs/saudelegis/anvisa/2004/res0216_15_09_2004.html)
  - Nothing in the text specifies in-person versus online delivery, or accreditation (my reading of the full text).
- **Online-certificate legality varies locally.** A Fiocruz course plan cites a law (Lei 1.662/1991, apparently a state or municipal rule) requiring training "ministrado por instituições credenciadas pela Vigilância Sanitária / Ministério da Saúde" — [Fiocruz EPSJV](https://www.epsjv.fiocruz.br/sites/default/files/curso/plano/plano_de_curso_manipulador_2024_atualizado.pdf). Praia Grande (SP) runs the course free but requires in-person registration — [Praia Grande](https://praiagrande.sp.gov.br/arquivos/sesap/seg_alimentar/curso_de_boas_praticas.pdf)
- **Prices and saturation:** Unieducar sells a 40-hour online RDC 216 course with certificate ("12x de R$ 40,19" / "R$ 28,16" on the page) and also offers a R$0 version — [Unieducar paid](https://unieducar.org.br/catalogo/curso/boas-praticas-em-servicos-de-alimentacao-descomplicando-a-manipulacao-de-alimentos), [Unieducar free](https://unieducar.org.br/catalogo/curso-gratis/boas-praticas-em-servicos-de-alimentacao-descomplicando-a-manipulacao-de)
- **Demand (Autocomplete, 2026-10-12):**
  - "curso de manipulação de alimentos online": "…gratuito", "…gratuitos sebrae", "…grátis com certificado anvisa", "…sebrae".
  - "curso manipulação de alimentos certificado": 8 of 10 suggestions contain "gratuito/gratis/sebrae".
  - pt-BR results for "curso manipulador de alimentos" are polluted with Spanish ("sepe", "cruz roja", "homologado españa"), which shows Brazilians rarely use the term "manipulador".
  - Source: [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=curso%20manipula%C3%A7%C3%A3o%20de%20alimentos%20certificado)
- **Record-keeping intent is template-shaped:**
  - "registro de treinamento": "…word", "…modelo", "…pdf", "…excel", "…de funcionários drogaria".
  - "controle de treinamentos": "…excel grátis", "…planilha", "…power bi", "…de segurança do trabalho".
  - "manual de boas práticas restaurante": "…pdf", "…pronto word", "…modelo".
  - Source: [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=controle%20de%20treinamentos)

### Inferences
- The Spanish winner's $37k/month comes from mass B2C job seekers who need a carnet to get hired. Brazil has no equivalent per-worker card under RDC 216, so the B2C funnel does not exist at the same scale. Free Sebrae and public options also anchor the price near zero.
- A restaurant compliance pack (training records, POPs, temperature logs, a Manual de Boas Práticas generator) is a real document need. But intent is "pronto/word/pdf/grátis", and nutritionist consultancies (responsável técnico) do this work as a service. Gates fail: G1 (no paid software evidence found), G2 (free saturation) and G4.

### Gaps
- I could not confirm whether RDC 216 has been replaced by a newer ANVISA resolution in 2025–2026. Check before any reuse.
- Municipal requirements for certified handler courses (for example in SP or RJ) were not surveyed one by one.

## Q3. Tifox → Brazil: educação infantil "parecer/relatório descritivo" aligned with the BNCC. Do schools or teachers pay, who competes, and does a deterministic generator fit?

### Takeaway
This is the best Brazilian demand match of the five, and it is deep-validated below as **CONDITIONAL**:
- Strong, recurring, seasonal search demand exists for each age, semester and BNCC variant.
- Teachers do pay: Hotmart template kits at about US$4, and Profez's AI teacher suite at R$17.91–31.58 per month.
- The market is crowded with free templates and AI writers (Profez, ChatGPT). A deterministic, non-AI generator has to win on structure (observation checklist → BNCC-coded report, turma-wide PDF, school standardization, LGPD for children's data), not on prose. That is a hard sell against "IA escreve o parecer em 30s".

### Cited Findings
- **Regulatory anchor:** in Educação Infantil the parecer descritivo is the official assessment instrument under the LDB and BNCC (no grades, no retention). The BNCC organizes the stage into 5 "campos de experiência". Some networks mandate a format: Pelotas requires a "Parecer Descritivo da Educação Infantil (PDEI)" from all schools in its municipal system — [Profez guide](https://profez.com.br/modelos/parecer-descritivo/de-acordo-com-a-bncc), [Profez](https://profez.com.br/parecer-descritivo)
- **Demand (Autocomplete, 2026-10-12): 10 suggestions on nearly every head term.**
  - "parecer descritivo": "…educação infantil", "…pronto", "…de acordo com a bncc", "…5 anos", "…4 anos de acordo com a bncc".
  - "relatório descritivo educação infantil": "…bncc", "…3/4/5 anos", "…segundo semestre", "…1/4 bimestre".
  - "relatório individual educação infantil": "…de acordo com a bncc", by age and by semester.
  - "modelo de relatório educação infantil": "…word", "…segundo semestre", "…para neuropediatra".
  - "frases para parecer descritivo": 8 suggestions ("…para iniciar", "…para finalizar").
  - "portfólio educação infantil": 10 suggestions ("…com fotos", "…pdf para imprimir").
  - **Commercial and tool modifiers return 0–1 suggestions:** "gerador de parecer descritivo" 0, "app parecer descritivo" 0, "site para fazer parecer descritivo" 0, "gerador de relatório educação infantil" 0, "parecer descritivo ia" 1, "relatório educação infantil ia" 1.
  - Source: [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=parecer%20descritivo%20educa%C3%A7%C3%A3o%20infantil)
- **Paid competitors and substitutes:**
  - **Profez** (AI teacher suite):
    - Its parecer page promises "Parecer descritivo pronto em 30 segundos… Descreva a criança, a IA escreve o parecer", with BNCC vocabulary, a whole-class mode and Word/PDF export. It runs SEO template pages for each age and situation (3, 4 and 5 anos, berçário, campos de experiência, educação especial).
    - Pricing: free "Explorador" (5 materials a month); "Professor Pro" R$17.91/month (R$214.90/yr); "Pro+" R$31.58/month (R$379/yr).
    - Apps on [Google Play](https://play.google.com/store/apps/details?id=br.com.profez.app) and iOS.
    - Sources: [profez.com.br/parecer-descritivo](https://profez.com.br/parecer-descritivo), [profez.com.br](https://profez.com.br/) (rendered 2026-10-12)
  - **Hotmart template kits:**
    - "Modelos de Parecer Descritivo Educação Infantil 3º Trimestre 15 alunos" (15 pareceres by campo de experiência) is shown at **$4.00** to a US IP. The seller is a content agency ("Digital Store ANS") — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/modelos-de-parecer-descritivo-educacao-infantil-3o-trimestre-15-alunos/G96187555I)
    - "35 Inspirações de Pareceres Descritivos (3 a 6 anos)", a 104-page e-book — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/35-inspiracoes-de-pareceres-descitivos-criancas-de-3-a-6-anos/Y96455544Q)
    - "100 Frases Pedagógicas + Modelos de Relatórios Prontos" — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/relatorios-educacao-infantil-4-modelos-prontos-100-frases-pedagogicas/P104911385P)
    - Sales counts are not public.
  - **Google Play:** a search for "parecer descritivo" returned no dedicated parecer app among the top results (diary-of-class and general teacher apps instead) — [Play search](https://play.google.com/store/search?q=parecer+descritivo&c=apps&hl=pt_BR&gl=BR)
- **Tifox benchmark:** €12–25 per class per year, free for 3 students. It is a "cahier de réussite" tied to the official 2026 French curriculum, with photos and print-ready PDFs. TrustMRR shows $1,586 in 30 days, 57 subscriptions and 9,007 visitors in 30 days — [TrustMRR Tifox](https://trustmrr.com/startup/tifox)
- **Pool:** "a educação infantil brasileira tem cerca de 687 mil docentes" (Censo Escolar, MEC statement, 2025-09-23) — [Diario de Pernambuco](https://www.diariodepernambuco.com.br/brasil/2025/09/11696464-governo-do-brasil-lanca-ciclo-2025-2026-do-programa-de-formacao-continuada-leitura-e-escrita-na-educacao-infantil.html)
  - Creche enrollment was 4,182,646 in 2025. Private schools lost 2.47% of creche enrollments from 2024 to 2025, and pre-school enrollment fell 3.79% — [Jornal de Brasília](https://jornaldebrasilia.com.br/noticias/brasil/matriculas-na-creche-e-pre-escola-voltam-a-cair-no-brasil-em-2025/)

### Inferences
- **Buyer power:** most of the 687k teachers work in public municipal networks with low pay. The realistic buyer is the individual teacher at about R$15–25 per month (Profez's price point), or private escolas infantis buying per class (Tifox's model). Private school counts are a gap. The private segment is shrinking (−2.47% creche enrollment).
- **Seasonality:** suggestions explicitly include "1º/2º semestre", "1/3/4 bimestre" and "3º trimestre", so demand peaks at the end of each term (roughly June–July and November–December). October 2026 is right before the second-semester peak, which makes a test timely now.
- **The non-AI constraint is the main competitive weakness.** A deterministic generator (a checklist of observable behaviours per campo de experiência and age, mapped to curated phrase banks, then assembled into a per-child PDF) is buildable and avoids hallucination and LGPD exposure from sending children's data to an LLM. But Profez already ranks with AI-written, individualized text, and ChatGPT is free. "Not AI" is a defensible feature for coordenadoras (consistency, auditability), not for the individual teacher.

### Gaps
- Number of private educação infantil schools, and how many use school-management suites with a parecer module (Agenda Edu, ClassApp, Proesc and similar were not checked).
- Profez's paying users and revenue are not public; Hotmart sales counts are not visible.
- No volumes or CPCs.

## Q4. P7M.io → Brazil: .p7s / ICP-Brasil signed files. Is there a pain, given the free official ITI validator?

### Takeaway
**KILL (quick).** "arquivo p7s" demand exists ("como abrir", "para pdf", "online", "serpro"). But the government's free **Validar** (validar.iti.gov.br) validates .p7s/.pdf/.xml ICP-Brasil signatures without storing files. I found no Brazilian paid product for it. Italy's driver (CAdES .p7m envelopes forced on PA invoices and contracts, opened by nobody's OS) has no Brazilian equivalent at that scale: NF-e is XML, and gov.br and most e-signature flows produce PDFs.

### Cited Findings
- **Demand:**
  - "arquivo p7s": "…para pdf", "…como abrir", "…serpro", "…docusign", "visualizar arquivo p7s online", "abrir arquivo p7s online", "converter arquivo p7s em pdf".
  - "abrir arquivo p7s": 8 suggestions (windows, android, iphone, "programa para…").
  - "p7s para pdf": 5 suggestions.
  - "verificador iti" and "validar assinatura digital": 10 suggestions each, many official (gov, iti, serpro, adobe, docusign, zapsign).
  - Source: [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=arquivo%20p7s)
- **Free official tool:** the ITI renamed its verifier to **Validar** (validar.iti.gov.br). It is "gratuito", validates the integrity and authorship of ICP-Brasil-signed documents, recommends the .p7s/.xml/.pdf formats, accepts uploads, URLs and QR codes, reports "Aprovada/Reprovada/Indeterminada" with signer, CPF/CNPJ and AC, and stores no files — [ITI cartilha](https://h-validar.iti.gov.br/Docs/cartilha-de-uso.pdf), [Gupy explainer](https://www.gupy.io/blog/iti-verificador)
- **Google Play** "p7s" search: the only dedicated app at the top is an Italian P7M converter (`it.blindbit.p7m_converter`); the rest are generic PDF readers — [Play search](https://play.google.com/store/search?q=p7s&c=apps&hl=pt_BR&gl=BR)

### Inferences
- The only unmet job is extracting the embedded document from an attached .p7s when the user only wants to read it. That is a free-tool niche, monetizable at best through ads. Gates fail: G1 (no paid Brazilian product found) and G8 (a much smaller file population than Italy).

### Gaps
- Whether Validar can display or extract embedded content from an attached .p7s was not confirmed.

## Q5. Other "regulation forces a document" niches in the TrustMRR dataset, and their Brazilian analogs

### Takeaway
Re-screening the 267 qualifying rows with document and compliance keywords added six more document-driven proofs. None has a Brazilian analog that beats the two candidates above:
- Promatic: HVAC permit operations, $3,320 in 30 days.
- easyMovingPermits: $1,819.
- Passport Photo Ready: $1,308.
- DrohnenAtlas: German drone compliance, $1,173.
- LegalOne: French legal notices, $11,364.
- Stampdy: stamp maker, $1,940.

Each Brazilian analog is either a service or despachante business, or a free government tool.

### Cited Findings
CSV rows are TrustMRR-verified figures, fetched 2026-10-12, from `trustmrr_newcomers.csv`:

| Product (slug) | Founded | 30-day rev. | Analog in Brazil and its problem |
|---|---|---|---|
| Promatic ([promatic](https://trustmrr.com/startup/promatic)) | 2025-05-29 | $3,320 | Permits, inspections and licenses for HVAC and plumbing contractors at $99 per project. The BR analog is AVCB/PPCI and alvará despachante work: a service with a local, in-person component, and it requires contacts |
| easyMovingPermits ([easy-moving-permits](https://trustmrr.com/startup/easy-moving-permits)) | 2025-11-11 | $1,819 | Street and moving permits per city. BR caçamba and street-use permits are municipal, fragmented and handled by service providers |
| LegalOne ([legalone](https://trustmrr.com/startup/legalone)) | 2025-10-14 | $11,364 | French legal-notice broker. BR "publicações legais" (S.A. balance sheets, editais) is a broker or service model, excluded as a service in round 2 |
| Passport Photo Ready ([passport-photo-ready](https://trustmrr.com/startup/passport-photo-ready)) | 2026-02-06 | $1,308 | US passport photos from $8.99. The BR angle would be consumer photos for foreign visas, not a business obligation, so it is out of scope (and AI-image-based) |
| DrohnenAtlas ([drohnenatlas](https://trustmrr.com/startup/drohnenatlas)) | 2026-05-01 | $1,173 | Drone compliance app (mobile, so the Apple fee applies). BR flight authorization runs through DECEA/ANAC government systems; not researched further |
| Stampdy ([stampdy](https://trustmrr.com/startup/stampdy)) | 2025-06-25 | $1,940 | Free stamp maker; generic and not regulation-specific |

### Inferences
- Read with FireCert, Valideo and BasinCheck, the pattern from round 2 holds. The replicable winners are **B2B tools that issue the mandated artifact for a contractor who serves many sites**, not trackers sold to the obligated end business. In Brazil that maps to fire-protection service firms (1b) and, as round 1 already found, engineers' laudos.

### Gaps
- About 3,600 TrustMRR profiles are not in the sitemap (round-2 gap), so more proofs may exist.

## Q6. Deep validation of the best 2: (A) fire-protection service-firm software (FireCert analog) and (B) a deterministic parecer descritivo generator (Tifox analog)

### Takeaway
**Neither is APPROVED. Both are CONDITIONAL.**
- **A** has the better buyer (B2B, monthly, many sites per customer) but fails G4: there is no measurable commercial search, so it must sell by outbound to a public registry. It also faces a focused incumbent at Brazilian price levels.
- **B** has the better distribution (abundant seasonal search) but weak buyer power and crowding from AI and free tools.

Ranking: **B is cheaper and faster to test now** (the second-semester peak is November–December 2026). **A has the higher ceiling per customer.** Neither displaces round 1's [[Gerador de laudos de vistoria e inspeção]].

### Cited Findings

**Candidate A: inspection and certificate SaaS for Brazilian fire-protection service firms**

| Field | Record |
|---|---|
| Product | Mobile-first web app for extinguisher, hydrant, alarm and emergency-light servicing companies. QR tag per asset; NBR 12962 inspection levels; technician checklist with photos; auto-generated certificate/report PDF and service order; client portal showing each site's due dates (recharge every 12 months, hydrostatic test every 5 years, plus AVCB, brigade and SPDA expiry as a free client-retention hook). Billing per managed client site, Inspefire-style |
| Buyer and pool | 1,776 active Inmetro-registered extinguisher maintenance firms (2025-07-16), concentrated in SP — [Inmetro ARR](https://www.gov.br/inmetro/pt-br/assuntos/regulamentacao/avaliacao-de-resultado-regulatorio/2026/inspecao-tecnica-e-manutencao-de-extintores-de-incendio/sei_inmetro-2373600-relatorio-final.pdf); plus unregistered installers and bombeiros civis |
| Pain | Recharge every 12 months and hydrostatic test every 5 years; Inmetro seal, label and control-sheet requirements — [TRE-MS ETP](https://www.tre-ms.jus.br/transparencia-e-prestacao-de-contas/licitacoes/pregao/pregao-2023/arquivos-2023/tre-ms-disp-eletr-05-2023-recarga-extintores-etp), [MPAM TR](https://www.mpam.mp.br/images-j5/SCOMS/PROCESSOS%20DISPENSAS/SEI_2025.026373/SEI_2032042_Termo_de_Referencia_14%202.pdf) (public tenders even demand a per-extinguisher traceability system). Reminders work as a retention tool for these firms — [Beancount article](https://beancount.io/pt/blog/2026/09/09/fire-extinguisher-service-bookkeeping-tag-routes-hydrostatic-test-guide) |
| Competitors | Inspefire R$24–49 per account per month, NBR 12962, 55 Play reviews — [inspefire.com.br](https://www.inspefire.com.br); Produttivo extinguisher template — [Produttivo](https://www.produttivo.com.br/modelo/checklist-extintores/); Inspeção Pro — [site](https://inspecaopro.com.br); Extinguisher 360 — [Play](https://play.google.com/store/apps/details?id=xyz.codexia.extinguisher360); generic FSM tools (Auvo, Field Control, Tecniko; round 1). Revenue of any of them: not public |
| Weaknesses to exploit | Inspefire pushes AI add-ons. Its pricing is per CNPJ, so a firm with 30 clients pays about R$720 a month (inference: 30 × R$24). A flat price per firm could undercut it for large books |
| Demand signals | Software-intent autocomplete 0–3 suggestions; "controle de extintores" is spreadsheet and free intent; "inspeção de extintores por qr code" exists — [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=inspe%C3%A7%C3%A3o%20de%20extintores) |
| Channel | Outbound email or WhatsApp to the public Inmetro registry (registro.inmetro.gov.br, cited by [Condomínio SC](https://condominiosc.com.br/jornal-dos-condominios/seguranca/3514-fabricacao-e-recarga-de-extintor-devem-seguir-regras)); small Google Ads on "software de extintores"; SEO on "relatório de inspeção de extintores", "etiqueta extintor 2026" (10 suggestions) |
| Build | 3–4 weeks: CRUD, QR, offline PWA, PDF. No certification needed (the Inmetro registration belongs to the customer) |
| Time to first revenue | 6–10 weeks (B2B outbound, 30-day trial norm set by Inspefire) |
| Risks | Incumbent with brand search; low Brazilian price level; outbound under LGPD (B2B legitimate interest; use business emails only); customer churn |

| Gate | Verdict | Evidence |
|---|---|---|
| G1 WTP | Pass (weak) | Inspefire publishes paid plans; FireCert $5,003 and BasinCheck $2,235 in 30 days abroad. Only one Brazilian vertical paid product found, plus generic FSM tools as substitutes |
| G2 Not saturated, newcomer can win | Unclear | 1 focused incumbent plus generic FSM tools; Inmetro says the service market is saturated; no Brazilian newcomer win observed |
| G3 Buyer power | Pass | Registered B2B firms selling recurring services to condominiums, retail and industry |
| G4 Distribution without contacts | **Fail on search**; outbound possible | 0–3 commercial suggestions; a public registry of 1,776 firms allows cold outreach |
| G5 MVP ≤4 weeks | Pass | Standard stack |
| G6 Not AI-core | Pass | — |
| G7 Legal, ToS, payment | Pass | No license; reports are the customer's responsibility; Brazilian SaaS billing via Asaas or Stripe BR. Cold email: LGPD legitimate interest (not verified against the ANPD in this round) |
| G8 Path to US$5k/month | Doubtful | R$27k/month ≈ 135 firms at R$199, or about 7.6% of all registered firms. At Inspefire-style per-site pricing: about 900 managed sites at R$30 |

- **Scores (1–5):** WTP 3, low saturation 2, buyer power 3, distribution 2, buildability 4, speed 2, low risk 3 = **19/35**.
- **Cheapest real-world test (about R$150 and 14 days):** scrape nothing. Hand-pick 150 SP and South registered firms from the public Inmetro registry and send a personal email or WhatsApp. Offer a free 30-day pilot of a clickable prototype (QR tag → certificate PDF → client due-date page), with founding pricing at R$149 a month flat.
  - **Pass:** ≥10 replies, ≥5 demos, and ≥2 firms paying R$149 (or prepaying the first month) within 21 days.
  - **Fail:** <3 demos, or every demo answers "já uso o Inspefire/planilha".

**Candidate B: deterministic BNCC parecer descritivo and portfolio generator for educação infantil**

| Field | Record |
|---|---|
| Product | Web app. The teacher creates a class, ticks observable behaviours per child for each of the 5 campos de experiência and age band (bebês, crianças bem pequenas, crianças pequenas), adds photos and short notes, and gets a per-child parecer assembled from curated, editable phrase banks with BNCC codes. Exports a print-ready PDF or Word file for the whole class. School plan lets the coordenação standardize phrases and review. No LLM, so children's data stays private. Pricing: R$19.90 per semester per teacher, or about R$9 per class per year for schools (Tifox model) |
| Buyer and pool | 687k EI teachers (Censo, 2025 MEC statement) — [Diario de Pernambuco](https://www.diariodepernambuco.com.br/brasil/2025/09/11696464-governo-do-brasil-lanca-ciclo-2025-2026-do-programa-de-formacao-continuada-leitura-e-escrita-na-educacao-infantil.html); private school count is a gap |
| Pain | 20–25 pareceres per teacher each semester, and generic copy-paste is noticed by coordination and families — [Profez](https://profez.com.br/parecer-descritivo) (a competitor's claim) |
| Competitors | Profez (AI) free tier, R$17.91–31.58 per month — [profez.com.br](https://profez.com.br/); Hotmart kits about US$4 — [Hotmart](https://hotmart.com/pt-br/marketplace/produtos/modelos-de-parecer-descritivo-educacao-infantil-3o-trimestre-15-alunos/G96187555I); free blog templates; ChatGPT |
| Demand signals | 10 suggestions each for "parecer descritivo educação infantil", "relatório descritivo educação infantil", "relatório individual…", "modelo de relatório…", plus age and semester long-tails; commercial modifiers 0–1 — [suggestqueries](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=relat%C3%B3rio%20individual%20educa%C3%A7%C3%A3o%20infantil) |
| Channel | Programmatic SEO pages by age, semester and campo, each carrying a free sample and the generator; Google Ads in peak weeks; Hotmart as a secondary marketplace; Pinterest and Instagram teacher communities (no audience yet) |
| Build | 2–3 weeks (the phrase-bank content is the main work; the client is a native speaker) |
| Time to first revenue | 2–6 weeks if launched before the November–December peak; otherwise it waits for June 2027 |
| Risks | Strong seasonality; teachers' low willingness to pay and "pronto/grátis" intent; AI incumbents; SEO time to rank; the content must be original (no copying of Hotmart or blog texts) |

| Gate | Verdict | Evidence |
|---|---|---|
| G1 WTP | Pass | Profez's paid plans (AI suite); Hotmart parecer kits; Tifox $1,586 in 30 days (verified) |
| G2 Not saturated, newcomer can win | **Weak** | Profez (founded recently enough to have SEO template pages and new apps; app updated 2026-09-01) shows a newcomer can rank, but it occupies the slot with AI. Free templates abound |
| G3 Buyer power | Weak–medium | Individual teachers at about R$18 per month; shrinking private EI segment |
| G4 Distribution | Pass (informational) / fail (commercial) | Rich long-tail search; tool-intent queries near zero |
| G5 MVP ≤4 weeks | Pass | Deterministic phrase-bank engine plus PDF |
| G6 Not AI-core | Pass by design, but that is the competitive handicap | — |
| G7 Legal, ToS, payment | Pass | No certification; LGPD for children's data (store minimal data, consent from the school); Hotmart, Asaas or Stripe BR |
| G8 Path to US$5k/month | Doubtful | R$27k/month ≈ 1,360 teachers at R$19.90/month-equivalent, or ≈ 2,700 semester packs per month averaged across the year, with peaks concentrated in 4 months. That would take top rankings across hundreds of long-tail queries |

- **Scores (1–5):** WTP 3, low saturation 2, buyer power 2, distribution 3, buildability 5, speed 4, low risk 3 = **22/35**.
- **Cheapest real-world test (R$200, 3 weeks, start before 2026-11-10):** ship a one-age-band MVP (5 anos, 2º semestre) with 20 sample pareceres as an SEO page, plus a paywalled whole-class PDF export at R$19.90 (semester pass). Run R$200 of Google Ads on "relatório descritivo educação infantil 5 anos segundo semestre", "parecer descritivo educação infantil 5 anos de acordo com a bncc" and close variants.
  - **Pass:** CPC ≤ R$0.80 and ≥ 8 paid passes (≥ 3% of ≥ 250 clicks) before 2026-12-15.
  - **Fail:** ≤ 2 sales, or CPC > R$1.50.

### Inferences
- The two candidates mirror each other. A has a payer but no search; B has search but a weak payer. Round 1's laudos generator still has the better combination (engineers pay, and the document carries an ART).
- If B passes its test, school plans (the Tifox model sold to private escolas infantis) are the route to buyer power. If A passes, per-site pricing gives a natural expansion path.
- The FireCert pattern ("certificate software for the contractor") could be reused for adjacent Brazilian contractor trades that issue mandated certificates: brigade trainers (IT 17, "certificado brigada de incêndio" has 8 suggestions incl. "modelo" and "pdf"), SPDA installers and hydrant testers. Each is narrower than extinguishers. Inspefire already sells a brigade module.

### Gaps
- No CPC or volume data; both tests are designed to measure them.
- Inspefire's and Profez's customer counts are unknown, so G2 cannot be quantified.
- Private EI school counts are missing (Sinopse Estatística do Censo Escolar 2025 would answer it).
- Whether outbound cold email to Inmetro-registry firms is acceptable under ANPD guidance was not verified on a primary source.

**Summary of verdicts (2026-10-12)**

| Candidate | Verdict | Score /35 | Failing gate(s) |
|---|---|---|---|
| A. Fire-protection service-firm SaaS (FireCert analog) | CONDITIONAL | 19 | G4 (no commercial search), G2 unclear, G8 doubtful |
| B. Deterministic parecer descritivo generator (Tifox analog) | CONDITIONAL | 22 | G2 weak (AI and free), G3 weak, G8 doubtful |
| 1a. AVCB/alvará license tracker for establishments | KILL | 20 (WTP 2, sat 3, buyer 3, dist 1, build 5, speed 2, risk 4) | G1, G4; same failure as the síndicos calendar |
| Food-handler course or training-record tracker | KILL | 16 (WTP 2, sat 1, buyer 2, dist 2, build 4, speed 3, risk 2) | G1, G2, G4; RDC 216 requires the course only for the responsável |
| .p7s viewer for Brazil | KILL | 21 (WTP 1, sat 2, buyer 2, dist 3, build 5, speed 4, risk 4) | G1, G8; free ITI Validar |
| BasinCheck analog (oil & gas audits) | KILL (not researched in depth) | — | Enterprise, Petrobras-driven B2B sales; requires contacts (inference) |
| Promatic, easyMovingPermits, LegalOne analogs | KILL | — | Services or despachante work, not software |
