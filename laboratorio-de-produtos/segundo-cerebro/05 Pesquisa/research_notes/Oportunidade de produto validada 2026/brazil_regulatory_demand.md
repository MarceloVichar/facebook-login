# Brazil 2026–2027 legal, tax and regulatory obligations as forced demand for simple paid software (status checked as of 12 Oct 2026)

Method note: facts come from primary texts where they could be reached (Planalto, STF, Portal do Simples Nacional, Agência Gov/Receita, CGIBS, the Receita open-data PDF). Otherwise they come from accounting and legal news and from vendor pages. "(search summary)" marks items seen only through a search-engine summary, not a fetched page. I queried Google Trends (Brazil, last 12 months) and Google autocomplete (pt-BR) directly on 2026-10-12. The shared web-search budget ran out before every item could be checked; the holes are listed under each "Gaps" heading.

## 1. Lei 15.270/2025 (IR reform): R$5k exemption, 10% dividend withholding, IRPFM, 2025-profits transition, and what owners and accountants need

### Takeaway
All three pillars have applied since 1 Jan 2026. The transition window for 2025 profits closed on 31 Jan 2026, after an STF extension. Two forced moments remain: monthly dividend planning (no more than R$50k per paying company per person per month) and the first IRPFM calculation in the 2027 return (Mar–May 2027), including the complex art. 16-B "redutor". Free calculators already cover the simple-calculator layer, and I found no paid planning tool with verified traction.

### Cited Findings
- The law is dated 26 Nov 2025. It "entra em vigor na data de sua publicação e produzirá efeitos a partir de 1º de janeiro de 2026" (art. 8º) — [Planalto, Lei 15.270/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm)
- Exemption (art. 3º-A of Lei 9.250, from January 2026): monthly taxable income up to R$5,000.00 gets a reduction of up to R$312.89 "de modo que o imposto devido seja zero". Income of R$5,000.01–R$7,350.00 gets a reduction of R$978.62 − (0.133145 × income). Above R$7,350.00 there is no reduction — [Planalto](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm)
- Dividends (art. 6º-A): from January 2026, profits and dividends paid "por uma mesma pessoa jurídica a uma mesma pessoa física residente no Brasil em montante superior a R$ 50.000,00 … em um mesmo mês" suffer 10% IRRF "sobre o total do valor pago". No deductions are allowed, and the tax is recalculated when there are several payments in the month — [Planalto](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm)
- IRPFM (art. 16-A): from exercício 2027 (ano-calendário 2026), an individual whose total income exceeds R$600,000 owes a minimum tax. The rate is 10% at R$1.2M or more. Between the two thresholds, "Alíquota % = (REND/60.000) − 10" — [Planalto](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm)
- Transition (art. 16-A §1º XII): profits from results up to 2025 are excluded from the IRPFM base if distribution was "aprovada até 31 de dezembro de 2025", payment occurs "nos anos-calendário de 2026, 2027 e 2028", and the terms of the approval act are respected — [Planalto](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm)
- Redutor (art. 16-B): a reducer applies when the company's effective rate plus the IRPFM effective rate exceeds the nominal sum: 34% in general and 40% for insurers/capitalização. §4º makes the reducer conditional on "demonstrações financeiras … na forma de regulamento". Under §6º, companies outside Lucro Real may use a simplified lucro contábil: revenue minus payroll, cost of goods, raw materials, rent, financing interest and depreciation. Under §7º, Receita "poderá … calcular o valor do redutor na declaração pré-preenchida" using information from the paying companies — [Planalto](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm). The 45% figure for banks comes from a secondary source — [Migalhas (depeso)](https://www.migalhas.com.br/depeso/443112/o-novo-imposto-de-renda-sobre-altas-rendas-a-logica-do-irpf-minimo) (search summary)
- On 26 Dec 2025 STF minister Nunes Marques extended the 31/12/2025 approval deadline to 31 Jan 2026 (ADIs 7912 by CNC and 7914 by CNI). The referendum was set for the virtual session of 13–24 Feb 2026. In the same decision he denied OAB's request (ADI 7917) to exclude Simples Nacional companies — [STF](https://noticias.stf.jus.br/postsnoticias/stf-prorroga-prazo-para-aprovacao-de-lucros-e-dividendos-ate-janeiro-de-2026/)
- On 02/12/2025 the Senate CAE approved PL 5.473/2025, which would allow approval of 2025 profits until 30/04/2026. I found no confirmation that it became law — [MRS Advogados](https://mrsadvogados.com/cae-aprova-pl-5-473-2025-para-ampliar-prazo-de-deliberacao-de-dividendos-isentos/) (search summary)
- Receita said it is "bastante simples" to secure non-withholding on 2025 profits — [Migalhas](https://www.migalhas.com.br/quentes/447142/para-receita-e-simples-evitar-retencao-de-ir-sobre-lucros-de-2025) (search summary)
- Simples Nacional dispute: Receita holds that the withholding applies to Simples companies. Taxpayers argue that only a complementary law could change the LC 123 art. 14 exemption — [Barbieri Advogados](https://www.barbieriadvogados.com/simples-nacional-tributacao-dividendos/); [Conjur](https://conjur.com.br/2025-dez-04/lei-15-270-2025-dividendos-e-simples-nacional/)
- EFD-Reinf NT 02/2026 created isenção type "12" in R-4010 (nature 12001, "Lucro e dividendo"), valid from 1 Jan 2026, with XSD schemas published on 14/05/2026. Analysts describe it as a layout change, not a new filing — [TecnoSpeed](https://blog.tecnospeed.com.br/efd-reinf-nota-tecnica-02-2026-lucros-dividendos/); [Contábeis](https://www.contabeis.com.br/noticias/76660/efd-reinf-ganha-novo-codigo-para-lucros-dividendos/) (search summary)
- Free tools already online:
  - dividend calculators: [Calculabr](https://calculabr.net.br/calculadora-imposto-dividendos/), [Calculadora Brasil](https://calculadorabrasil.com.br/imposto-dividendos/), [Irmãos Meira](https://irmaosmeira.com.br/calculadoras/distribuicao-lucros), [Valor Final](https://valorfinal.com.br/guia/distribuicao-de-lucros-como-funciona)
  - IRPFM simulators: [Somas](https://somas.io/investimentos/simulador-irpfm), [Fatorial](https://fatorialinvest.com.br/simulador-irpf-2026/), [OSP Contabilidade](https://ospcontabilidade.com.br/materiais/calcular/simulador-ir-alta-renda/)
  - bank explainer: [Safra](https://oespecialista.safra.com.br/irpfm-imposto-minimo-alta-renda/)
- Search demand on Google Trends BR, 12-month average: "lei 15.270" scores 4, with a peak of 17 in 23–29 Nov 2025, against 36 for "nfs-e nacional" — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=riscos%20psicossociais,receita%20sa%C3%BAde,nfs-e%20nacional,carn%C3%AA%20le%C3%A3o,lei%2015.270). "irpfm" scores about 1 — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=receita%20sa%C3%BAde,nfs-e%20nacional,nr%201,simples%20nacional%20h%C3%ADbrido,irpfm)
- Autocomplete (pt-BR) returns:
  - "distribuição de lucros 2026 acima de 50 mil", "… reinf", "… dominio", "… simples nacional", "… lucro presumido" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=distribui%C3%A7%C3%A3o%20de%20lucros%202026)
  - "imposto mínimo para alta renda", "imposto mínimo irpfm" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=imposto%20m%C3%ADnimo)

### Inferences
- The "accumulated profits up to 2025" spike is over: the approval window closed on 31 Jan 2026. What remains is tracking the 2026–2028 payment schedules of approved 2025 profits, which is small and handled in spreadsheets and ERPs.
- The real remaining complexity is the art. 16-B redutor: the company's effective rate, the §6º simplified calculation for Presumido/Simples companies, and consolidated statements. It matters to partners with more than R$600k of income and to their accountants. Demand peaks would be year-end planning (Nov–Dec 2026) and the first IRPFM return (Mar–May 2027). Receita pre-filling under §7º may shrink the need.
- The autocomplete "distribuição de lucros 2026 dominio" suggests accountants look for this workflow inside their ERP (Domínio), so incumbent ERPs are the default channel.
- Liability: a planner that outputs "how much to distribute, and when" is close to tax advice. A disclaimer is enough only if the tool is framed as a simulation of user-entered assumptions for professional users (accountants). It is not enough if the tool is sold to business owners as a recommendation.

### Gaps
- How many taxpayers will owe IRPFM. A government estimate of about 141k circulates, but I could not verify it before the search budget ran out.
- Whether PL 5.473/2025 became law, and the merits rulings in ADIs 7912, 7914 and 7917.
- Whether Receita has issued the regulation for art. 16-B §§4º–6º, and whether companies must give partners a demonstrativo.
- Prices or traction of any paid IRPFM or dividend-planning tool. None found.

## 2. Reforma Tributária do consumo (EC 132/2023, LC 214/2025): 2026 test year, IBS/CBS fields in NF-e/NFC-e/NFS-e, CBS from 2027, split payment

### Takeaway
2026 is an informational test year with penalties waived. IBS/CBS fields have been required in NF-e since 3 Aug 2026 and in NFS-e since 1 Oct 2026, though NFS-e without them is not rejected until 31 Dec 2026. Simples Nacional follows from 1 Jan 2027. CBS replaces PIS/Cofins in 2027. Split payment is only in testing (from 15 Oct 2026) and becomes optional, B2B only, in H2 2027. All of this is ERP and emitter work, not a standalone product.

### Cited Findings
- Ato Conjunto RFB/CGIBS nº 1 (Dec 2025):
  - IBS/CBS calculation in 2026 has "caráter meramente informativo", with no payment.
  - Penalties for the new ancillary obligations are waived "até o primeiro dia do quarto mês subsequente à publicação da parte comum dos regulamentos", which depends on the sanction of PLP 108/2024.
  - NF-e, NFC-e, CT-e and NFS-e get IBS/CBS fields, and missing fields bring no sanction during the adaptation period.
  - Source: [CGIBS](https://www.cgibs.gov.br/comite-gestor-e-receita-federal-garantem-prazo-de-adaptacao-e-transicao-segura-para-contribuintes-do-ibs-e-da-cbs-em-2026)
- Ato Conjunto RFB/CGIBS nº 4 (30 Jul 2026) sets the NFS-e schedule — [Contábeis](https://www.contabeis.com.br/noticias/79768/nfs-e-informacoes-de-ibs-e-cbs-passam-a-ser-exigidas-em-outubro/):
  - 1 Oct 2026: IBS/CBS information required for most LC 116 services.
  - 1 Dec 2026: digital platforms, ISS subitems 1.03, 1.05, 1.09 and 16.01, certain rentals and condominium revenues.
  - 1 Jan 2027: Simples Nacional.
  - An NFS-e missing IBS/CBS will not be rejected until 31 Dec 2026, but the document is still non-compliant.
- NF-e, CT-e and MDF-e waves started on 3 Aug 2026 — [Contmatic](https://simplifique.contmatic.com.br/blogs/obrigatoriedade-ibs-cbs-documentos-fiscais-4-ondas-2026) (search summary)
- Ajuste SINIEF 49/2025 covers NF-e debit/credit notes for four scenarios: future-delivery sales, inventory losses, value reductions and refused deliveries. Its mandatory start was postponed to 1 Jan 2027 (published 14 Aug 2026). This is the second postponement: the start was originally May 2026, then August 2026 under Ajuste SINIEF 15/2026 — [Debate Jurídico](https://debatejuridico.com.br/confaz-adia-obrigatoriedade-do-ajuste-sinief-49-2025-para-janeiro-de-2027/)
- From 2027 CBS is fully in force, PIS/Cofins are extinct and IPI goes to zero except in the Zona Franca de Manaus — [Movimento Econômico, 18/09/2026](https://movimentoeconomico.com.br/receita-federal/2026/09/18/simulador-da-receita-indica-impacto-de-cbs-e-ibs-nas-empresas-do-simples/)
- Split payment:
  - integration tests from 15 Oct 2026 — [Comsefaz](https://comsefaz.org.br/novo/split-payment-entra-em-fase-de-testes-a-partir-de-15-de-outubro-saiba-o-que-muda/) (search summary)
  - available in H2 2027, gradual, optional and B2B only; the first stage covers boleto, Pix, TED and TEF; no mandatory date has been set — [Radar da Reforma Tributária](https://radardareformatributaria.com/split-payment-testes-2026-implantacao-gradual-2027/); [Urbano Vitalino](https://www.urbanovitalino.com.br/split-payment-manuais-tecnicos-aprovados-e-inicio-facultativo-so-entre-empresas-em-2027/) (search summaries)
- An official free "Calculadora de Tributos sobre o Consumo" (piloto-cbs.tributos.gov.br) simulates operations in both the regular regime and Simples — [Movimento Econômico](https://movimentoeconomico.com.br/receita-federal/2026/09/18/simulador-da-receita-indica-impacto-de-cbs-e-ibs-nas-empresas-do-simples/)

### Inferences
- NF-e and NFS-e emitters and ERPs absorb the new document fields. A solo developer cannot sell "IBS/CBS fields" on their own.
- Split payment is infrastructure for payment providers and banks and requires being a payment participant, so it is excluded under constraint (c).
- Generic IBS/CBS price-impact calculators compete with a free official calculator. Trap.

### Gaps
- I did not verify the 2027 CBS/IBS reference rates or the status of PLP 108/2024, which decides when penalties can start.
- Sources give conflicting act numbers for split payment (Ato Técnico nº 4 or nº 5/2026).

## 3. Simples Nacional "hybrid" option (IBS/CBS paid outside the DAS): dates, who decides, and whether a decision simulator is needed

### Takeaway
The first window ran from 1 to 30 Sep 2026, with effects for Jan–Jun 2027. The choice can be cancelled until 30 Nov 2026. The next window is March 2027 (for H2 2027), and after that every March and September. The decision is real and recurring for 11.6M ME/EPP. But Receita launched a free official simulator on 18 Sep 2026, and at least seven free calculators exist, so willingness to pay for a simulator is unproven.

### Cited Findings
- Resolução CGSN nº 186/2026 (published 17/04/2026) — [Portal do Simples Nacional](https://www8.receita.fazenda.gov.br/simplesnacional/noticias/NoticiaCompleta.aspx?id=c739e03c-8482-473f-8e82-f38ec3b13637):
  - The option to join Simples for 2027 moves to 1–30 Sep 2026.
  - In the same window a company chooses whether IBS/CBS stay inside the DAS or go to the regular regime, valid for Jan–Jun 2027. With no choice, both stay in the DAS in H1 2027.
  - A new window opens in March 2027 for H2 2027.
  - A September option can be cancelled "até o último dia de novembro de 2026".
  - CNPJs opened between 1 Oct and 31 Dec 2026 follow special rules.
  - The MEI/SIMEI option stays in January.
- Resolução CGSN nº 190/2026 complements 186/2026; cancellation "em caráter irretratável, até o último dia de novembro de 2026" — [Prefeitura de Montes Claros, 17/08/2026](https://financas.montesclaros.mg.gov.br/comunicado/simples-nacional-2027-atencao-aos-novos-prazos-de-opcao)
- From then on, regular-regime options can be made "em março e setembro de cada ano, com efeitos sobre o semestre seguinte". A company that chose the regular regime stays in it until it renounces in a window — [Contábeis, 01/09/2026](https://www.contabeis.com.br/noticias/79143/simples-nacional-abre-opcao-pelo-regime-regular-de-ibs-e-cbs/)
- Contábeis on the decision:
  - "a escolha não deve ser feita apenas com base na alíquota nominal. Será necessário simular os dois cenários".
  - B2B sellers may gain because their buyers get full credits.
  - Accountants should "simular os dois modelos e documentar a decisão adotada por cada empresa".
  - Source: [Contábeis](https://www.contabeis.com.br/noticias/79143/simples-nacional-abre-opcao-pelo-regime-regular-de-ibs-e-cbs/)
- Who decides, and the official simulator — [Movimento Econômico, 18/09/2026](https://movimentoeconomico.com.br/receita-federal/2026/09/18/simulador-da-receita-indica-impacto-de-cbs-e-ibs-nas-empresas-do-simples/):
  - About 11.6M ME/EPP had to decide.
  - Simples has 24.8M companies: 13.2M MEI, 9.8M ME and 1.8M EPP, according to a May 2026 sector manifesto.
  - MEIs cannot take the regular regime; companies above R$3.6M of 12-month revenue must pay IBS in the regular regime.
  - On 18 Sep 2026 Receita launched a CBS/IBS simulator for Simples inside the Calculadora de Tributos sobre o Consumo.
- Free simulators:
  - [e-Auditoria](https://www.e-auditoria.com.br/blog/simulador-de-carga-tributaria-no-simples-nacional/)
  - [Alterdata (inside its ERP)](https://ajuda.alterdata.com.br/wfiscal/simulador-cbs-ibs-para-simples-nacional-fiscal)
  - [Calculadora Contábil](https://www.calculadoracontabil.com.br/calculadoras/comparativo-simples-hibrido-rt)
  - [Business Consultoria](https://www.consultoriabusiness.com.br/ferramentas/calculadora-simples-hibrido/)
  - [OSP Contabilidade](https://ospcontabilidade.com.br/materiais/calcular/simulador-simples-hibrido/)
  - [Escola Superior (free spreadsheet)](https://escolasuperioresn.com.br/material-gratuito-calculadora-simples-atual-vs-sistema-hibrido/)
  - [independent Netlify app](https://simples-nacional-buratigt.netlify.app/)
- On Google Trends BR, "simples nacional híbrido" has a 12-month average of about 1 (weekly values 4–5 in late Aug–Sep 2026), against 19 for "nfs-e nacional" in the same comparison — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=receita%20sa%C3%BAde,nfs-e%20nacional,nr%201,simples%20nacional%20h%C3%ADbrido,irpfm)
- Autocomplete returns:
  - "simples nacional híbrido ou convencional", "… híbrido x tradicional", "… híbrido 2027" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=simples%20nacional%20h%C3%ADbrido)
  - "simulador simples nacional hibrido", "simulador simples nacional reforma tributaria" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=simulador%20simples%20nacional)

### Inferences
- The problem is real and recurs twice a year, but:
  - the buyer is the accountant;
  - the free official simulator anchors the price at zero;
  - demand windows are short: the Nov 2026 cancellation deadline, Feb–Mar 2027 and Aug–Sep 2027.
- The only defensible paid angle is an accountant workflow. The tool would import a client list (revenue, annex, B2B share, creditable purchases), flag which clients should consider the hybrid regime, and produce a client-facing PDF documenting the decision. I found no evidence of willingness to pay for this.
- Liability: output that "recommends" a regime exposes the seller. Showing scenario comparisons to professionals, with explicit assumptions and a disclaimer, is acceptable. Selling recommendations to business owners is not.

### Gaps
- How many companies actually took the regular regime in Sep 2026.
- Whether CGSN will move the cancellation deadline. One mention links this to the publication date of the CBS reference rate; I could not verify it.
- How many accounting firms exist in Brazil, which would size the market for an accountant tool.

## 4. Individuals renting out property (more than 3 properties and over R$240k) becoming IBS/CBS taxpayers; price-impact calculators for service providers

### Takeaway
LC 214 makes these landlords IBS/CBS taxpayers, with a 70% rate reduction for rentals. CNPJ registration for such individuals has reportedly been pushed to 2027. The affected population is small and the questions are legal planning (individual vs holding company), so tools drift into advice. A free official calculator commoditises price-impact calculators.

### Cited Findings
- An individual landlord becomes a taxpayer when, in the prior year, rental revenue exceeds R$240k and the contracts involve more than three distinct properties. Both conditions are required, and the threshold is IPCA-updated. One source cites an in-year trigger of about R$288k (20% above the limit) — [Radar da Reforma Tributária](https://radardareformatributaria.com/locacao-imoveis-ibs-cbs-2027-pessoa-fisica-holding-transicao/); [Valor Final](https://valorfinal.com.br/guia/reforma-tributaria-aluguel) (search summaries)
- IBS/CBS rates on rentals are reduced by 70% (art. 261) — [Radar da Reforma Tributária](https://radardareformatributaria.com/locacao-imoveis-ibs-cbs-2027-pessoa-fisica-holding-transicao/) (search summary)
- CNPJ registration for individual taxpayers was postponed to 1 Jan 2027 by "Decreto nº 13.075/2026", per a single source — [Andere Advogados](https://andere.adv.br/aluguel-pessoa-fisica-ibs-cbs-cnpj-2027-reforma-tributaria/) (search summary). Receita postponed to 2027 the CNPJ requirement for individuals issuing IBS/CBS documents — [RS Data](https://www.rsdata.com.br/cnpj-pessoa-fisica-documentos-fiscais-2027/) (search summary; the page returned 403 when fetched)
- Existing free content and tools: [Valor Final](https://valorfinal.com.br/guia/reforma-tributaria-aluguel), [Pilota Imóveis (rental-management SaaS)](https://pilotaimoveis.com.br/reforma-tributaria-aluguel-ibs-cbs), [Portas](https://portas.com.br/reforma-tributaria/reforma-tributaria-imoveis/)
- Autocomplete returns:
  - "aluguel pessoa fisica ibs cbs", "ibs cbs aluguel temporada" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=aluguel%20ibs%20cbs)
  - "carnê leão aluguel 2026" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=carn%C3%AA%20le%C3%A3o%20aluguel)
- The official Calculadora de Tributos sobre o Consumo is free — [Movimento Econômico](https://movimentoeconomico.com.br/receita-federal/2026/09/18/simulador-da-receita-indica-impacto-de-cbs-e-ibs-nas-empresas-do-simples/)

### Inferences
- The buyers have high purchasing power, but the niche is thin and advice-heavy, and content from lawyers and holding-company planners dominates it. Low priority.

### Gaps
- How many individuals meet both criteria, and the primary text of the CNPJ-postponement decree.

## 5. NR-1 psychosocial risk management (GRO/PGR): real enforcement date, fines, tools, room for a cheap self-serve tool

### Takeaway
The obligation is in force. But as of Oct 2026 the STF has suspended all sanctions based on the psychosocial items. The first suspension of 25 Jun 2026 ran 90 days and was extended by another 90 days around 24–25 Sep 2026, to about late Dec 2026, while a conciliation works out objective criteria. The tooling market is already crowded and search interest fell sharply after the suspension. This is a trap for now.

### Cited Findings
- Portaria MTE 1.419/2024 added psychosocial factors to GRO/PGR. It formally took effect in May 2025 with one educational year. Fines were to be possible from 26 May 2026, and Minister Marinho said there would be no new postponement — [Contábeis, 27/04/2026](https://www.contabeis.com.br/noticias/76376/nr-1-fiscalizacao-de-riscos-psicossociais-comeca-em-maio-de-2026/)
- STF suspension (ADPF 1316, filed by Confenen) — [STF](https://noticias.stf.jus.br/postsnoticias/stf-suspende-sancoes-da-nr-1-e-abre-conciliacao-sobre-regras-de-riscos-psicossociais-no-trabalho/):
  - Minister André Mendonça suspended for 90 days fines and other sanctions tied to the items on including psychosocial risks in GRO, considering them in working conditions, choosing assessment tools, documenting criteria and analysing the efficacy of measures.
  - The norm's general guidelines "continuam válidas".
  - Sanctions already applied are also suspended.
  - The case goes to conciliation at Nusol.
  - Plenary referendum in the virtual session of 7–18 Aug 2026.
- The decision was dated 25 June, and the unanimous referendum ended on 18 Aug — [Metrópoles, 25/09/2026](https://www.metropoles.com/saude/stf-prorroga-por-90-dias-suspensao-de-multas-da-nr-1-sobre-saude-mental)
- Extension — [Migalhas, 25/09/2026](https://www.migalhas.com.br/quentes/465248/andre-mendonca-prorroga-por-mais-90-dias-suspensao-de-sancoes-da-nr-1):
  - Another 90 days, at the request of CNSaúde and CNC; the first period ended on Wednesday 23 Sep.
  - The first conciliation meeting was on 14 Sep 2026.
  - AGU asked to move the dispute to the Sejan chamber.
  - ADPFs 1333 (CNSaúde) and 1340 (CNC) are now heard together with it.
- Migalhas also reported a separate injunction suspending NR-1 sanctions for Fiesp-linked companies (headline only) — [Migalhas (related headlines)](https://www.migalhas.com.br/quentes/448486/nr-1-a-partir-de-maio-empresas-devem-monitorar-riscos-a-saude-mental)
- A law firm cites fines of R$1,610.12–R$6,708.08 per exposed worker (unverified) — [Vieites Advogados](https://vieitesadvogados.com.br/riscos-psicossociais-na-nr-1-o-que-muda-para-as-empresas-a-partir-de-26-de-maio-de-2026/) (search summary)
- Competitors and prices:
  - Taochi charges R$30 per employee per month or R$300 per year. It estimates consultancies at R$80–250 per employee per cycle, i.e. R$8k–25k for 100 staff — [Taochi](https://taochi.com.br/blog/quanto-custa-adequacao-nr1-riscos-psicossociais/)
  - QWork charges per report: R$1,500 (1–49 staff), R$2,663 (50–100) and R$4,970 (101–200). The tiers appear on its page; the prices come from a search summary — [QWork](https://www.qwork.app.br/)
  - NRGuard has a free start, a "Plano Consultor" (5/10/25 companies) and a "relatório técnico gerado por IA". It claims "Mais de 100 empresas já se cadastraram" and "847 PGRs assinados" (self-reported and inconsistent) — [NRGuard](https://nrguard.com.br/)
  - Focando uses COPSOQ II/III with quote-based pricing — [Focando](https://focando.com.br/)
  - The COPSOQ questionnaire is free (the cost is in application and reporting), and a free COPSOQ Brasil platform exists — [Weex](https://weex.digital/copsoq-brasil/)
  - An automated COPSOQ spreadsheet is sold — [Amigo da Prevenção](https://amigodaprevencao.com/planilha-copsoq-automatizada-avaliacao-psicossocial-nr17-oferta/)
  - Large HR suites are also active — [Sólides](https://solides.com.br/blog/copsoq-br/)
- On Google Trends BR, "riscos psicossociais" reached 71 in 24–30 May 2026 (the highest of the weeks sampled), then 31–35 in June and 14–23 from July to early October — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=riscos%20psicossociais,receita%20sa%C3%BAde,nfs-e%20nacional,carn%C3%AA%20le%C3%A3o,lei%2015.270)
- Autocomplete returns "nr 1 psicossocial foi prorrogada", "… prorrogação", "… adiamento", "… foi adiado" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=nr%201%20psicossocial)

### Inferences
- Sanctions are unlikely before about late Dec 2026, and the conciliation may change what an "adequate" assessment looks like. Building to today's criteria risks rework.
- The market is saturated at both ends: cheap self-serve SaaS at R$30 per employee, and consultancies that already hold the SST client relationships. A cheaper self-serve tool would also face free COPSOQ platforms and spreadsheets.
- AI-generated PGR reports (as NRGuard markets) are an AI-wrapper value proposition and are excluded by constraint (e).
- Liability: selling "laudos" or "conformidade NR-1" while the criteria are suspended or undefined is risky. A disclaimer is not enough if the report is presented as satisfying the PGR.

### Gaps
- Whether the NR-1 PGR exemption for ME/EPP in risk grades 1–2 also covers psychosocial risks.
- Any MTE guidance issued after the STF decision.
- Current QWork and Focando prices from their own pages.

## 6. NFS-e Padrão Nacional (mandatory under LC 214 from 2026): who is affected, pain points, emitters and API providers

### Takeaway
Municipalities had to adhere by 1 Jan 2026. MEIs billing companies have used the national standard since Sep 2023. Simples ME/EPP must use the Emissor Nacional from 1 Nov 2026 (Res. CGSN 191/2026), with IBS/CBS fields for them from Jan 2027. This has the strongest search demand of any item checked. But a free official emitter and a crowded API, ERP and billing market make a new emitter a trap.

### Cited Findings
- LC 214/2025 requires all municipalities to adhere by 1 Jan 2026, on pain of losing voluntary federal transfers. Integration is not the same as emission: an integrated municipality may still require its own system — [Conta Azul, 14/08/2026](https://contaazul.com/blog/nfse-padrao-nacional/); [AMM](https://portalamm.com/municipios-devem-fazer-adesao-obrigatoria-a-nfs-e-nacional-ou-perderao-recursos-em-2026/)
- MEIs providing services to companies have been required to use the national standard since 1 Sep 2023 (Res. CGSN 169/2022); it is optional for services to individuals — [Conta Azul](https://contaazul.com/blog/nfse-padrao-nacional/)
- Simples ME/EPP must use it from 1 Nov 2026 under "Resolução CGSN nº 191, de 4 de agosto de 2026", which replaced Res. CGSN 189/2026 (that had set September) — [Conta Azul](https://contaazul.com/blog/nfse-padrao-nacional/). Receita clarified that the Emissor Nacional becomes mandatory for Simples companies on 1 Nov 2026 and that IBS/CBS rules apply to them from 1 Jan 2027 — [Contábeis](https://www.contabeis.com.br/noticias/79768/nfs-e-informacoes-de-ibs-e-cbs-passam-a-ser-exigidas-em-outubro/)
- Lucro Presumido and Lucro Real companies have no single federal date; it depends on each municipality — [Conta Azul](https://contaazul.com/blog/nfse-padrao-nacional/)
- On 5 Jan 2026 several municipalities reported instability. Receita attributed most problems to municipal configuration — [Soluti](https://conteudo.soluti.com.br/instabilidade-marca-inicio-da-obrigatoriedade-da-nfs-e-nacional-em-2026-confira-orientacoes-da-receita-federal/) (search summary)
- Prices:
  - Focus NFe's pricing page lists plans at R$62.90, R$94.90, R$119.90, R$572.00 and R$657.90 per month, and "cada documento emitido ou recebido conta como uma unidade" — [Focus NFe](https://focusnfe.com.br/precos/) (fetched 12 Oct 2026). An older snapshot of the same page showed Solo at R$89.90 (1 CNPJ, 100 notes), Growth at R$548 (4,000 notes) and R$199 per new municipality (search summary).
  - NFE.io NFS-e plans: R$190 (250 notes), R$265 (500) and R$375 (1,000) — [NFE.io](https://nfe.io/precos/emissao-nfse/) (search summary; page about 1.5 years old)
  - Brasil NFe: R$99.90 per month flat — [Brasil NFe](https://www.brasilnfe.com.br/products/nfs-e/) (search summary)
  - Nuvem Fiscal and PlugNotas publish no prices — [x-apps comparison](https://x-apps.com.br/captura-fiscal-comparativo-fornecedores/) (search summary)
  - eNotas sells automatic NFS-e integrated with Hotmart — [eNotas](https://enotas.com.br/precos/)
- On Google Trends BR, "nfs-e nacional" has the highest 12-month average of all terms tested (36). It peaked at 100 in 4–10 Jan 2026 and reached 71 in 30 Aug–5 Sep 2026 and 54 in 27 Sep–3 Oct 2026 — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=riscos%20psicossociais,receita%20sa%C3%BAde,nfs-e%20nacional,carn%C3%AA%20le%C3%A3o,lei%2015.270)
- Autocomplete returns:
  - "nfs-e nacional api", "nfs-e nacional mei", "nfs-e nacional para empresas do simples é adiada para novembro" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=nfs-e%20nacional)
  - "emissor nacional nfs e fora do ar" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=emissor%20nacional%20nfs-e)

### Inferences
- 1 Nov 2026 forces a mass migration. But an ME/EPP's default answer is the free official Emissor Nacional, its accountant's portal, or an ERP or billing tool that is already integrated. API buyers already have Focus, NFE.io, Nuvem Fiscal and PlugNotas.
- A new emitter would have to hold A1 certificates, handle each municipality's settings and support users on fiscal documents. That is heavy support and liability for a solo developer. Useful at most as SEO content.

### Gaps
- How many Simples service providers move on 1 Nov 2026.
- Current Nuvem Fiscal and PlugNotas prices.

## 7. Receita Saúde (mandatory electronic receipts for self-employed health professionals since 2025): pain, API or automation, tools

### Takeaway
Receita Saúde has been mandatory since 1 Jan 2025 for health professionals working as individuals (PF). Since Nov 2025 Receita accepts a batch CSV (up to 1,000 lines) imported through Carnê-Leão Web, but building that file is still manual. Practice-management suites bundle the export into paid plans. A cheap single-purpose batch and receipt tool is an open, low-liability niche, with willingness to pay proven only through bundled features.

### Cited Findings
- Since 1 Jan 2025, receipts from health professionals working as PF must be issued through Receita Saúde — [Agência Gov, Dec 2024](https://agenciagov.ebc.com.br/noticias/202412/emissao-de-recibo-digital-por-profissionais-da-saude-passa-a-ser-obrigatorio-a-partir-de-1o-de-janeiro). This includes psychologists working as PF; clinics and hospitals keep using DMED — [CFP](https://site.cfp.org.br/psicologas-e-psicologos-que-atendam-como-pessoa-fisica-terao-que-emitir-recibo-digital-pelo-receita-saude-a-partir-de-1o-de-janeiro/)
- Professions covered: doctors, psychologists, dentists, physiotherapists, speech therapists and occupational therapists — [Leia Notícias (Corpora)](https://leianoticias.com.br/329672-corpora-lanca-integracao-com-receita-saude-para-psicologos/)
- Receipts for 2025 could be issued until 28 Feb 2026 — [Portal da Reforma Tributária](https://www.reformatributaria.com/brasil/prazo-para-emissao-do-receita-saude-2025-termina-em-28-de-fevereiro-de-2026/); [CRC-MA](https://crcma.org.br/noticias/profissionais-de-saude-devem-regularizar-recibos-eletronicos-de-2025-ate-fevereiro-de-2026)
- In January 2025, 1,368,312 receipts were issued, and three professions accounted for more than 90% — [Receita Federal, Feb 2025](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2025/fevereiro/receita-saude-simplifica-a-vida-de-milhares-de-brasileiros-e-reduz-riscos-fiscais) (search summary)
- In Nov 2025 Receita released an official batch-issuance feature using an integration file, "para … evitar que o profissional tenha de preencher as mesmas informações em dois sistemas". Receita publishes the file layout (date, amount, payer type, CPF of the payer) — [Leia Notícias (Corpora)](https://leianoticias.com.br/329672-corpora-lanca-integracao-com-receita-saude-para-psicologos/)
- File rules — [Receita Saúde manual v2.1](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/manuais/orientacao-tributaria/receita-saude-2.1.pdf) (search summary); [Formato do arquivo de Escrituração](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/manual/formato-arquivo):
  - The manual is version 2.1 (Oct 2025).
  - The file is a CSV with semicolon-separated fields and up to 1,000 lines.
  - Each line uses the actual payment date, and all payments in one file must be from the same year.
  - Each line carries an occupation code (255 = psychologist).
  - The file is imported in Carnê-Leão on e-CAC.
- A whole imported batch can be undone within 10 days ("Desfazer escrituração") — [Hotina](https://hotina.app/blog/receita-saude-para-psicologas-autonomas-2026/)
- A free tutorial with a free template exists on YouTube — [YouTube](https://www.youtube.com/watch?v=UWvzUaK6Xfg&vl=pt-BR). Accountants discuss the batch import on a forum — [Contábeis fórum](https://www.contabeis.com.br/forum/tributos-federais/411363/emissao-em-lote-de-recibos-do-receita-saude/)
- Paid tools that bundle the feature (no customer counts found):
  - Psicontrole lets users "gere o lote de recibos do Receita Saúde". Its offer is R$97 for 90 days of access, and its pitch describes "domingo à noite, celular na mão, emitindo recibo por recibo" — [Psicontrole](https://psicontrole.com.br/)
  - PsicoPront offers a CSV export for Receita Saúde and Carnê-Leão inside a single paid plan, and claims it "Evita multa de R$ 100,00 por mês calendário" (vendor claim) — [PsicoPront](https://psicopront.com.br/recursos)
  - Corpora puts its Receita Saúde integration in the Pro plan — [Leia Notícias](https://leianoticias.com.br/329672-corpora-lanca-integracao-com-receita-saude-para-psicologos/)
  - Rebots sells a REST API: JWT authentication, a one-time PFX certificate upload, and the official PDF returned by callback. It claims "Profissionais perdem até 20% do dia preenchendo recibos" (vendor claim) — [Rebots](https://rebots.com.br/api-receita-saude)
- On Google Trends BR, "receita saúde" has a 12-month average of 27 against 12 for "carnê leão". It peaked at 59 in 24–30 May 2026 (IRPF deadline week) and ran at 18–23 in Aug–Oct 2026 — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=riscos%20psicossociais,receita%20sa%C3%BAde,nfs-e%20nacional,carn%C3%AA%20le%C3%A3o,lei%2015.270)
- Autocomplete returns:
  - "receita saúde emitir recibo", "receita saúde carnê leão" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=receita%20sa%C3%BAde)
  - "receita saude em lote" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=receita%20saude%20lote)
  - "recibo receita saude pode ser emitido retroativo", "… serve como nota fiscal", "… ecac", "… fisioterapia" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=recibo%20receita%20saude)

### Inferences
- Active issuers: 1.37M receipts in Jan 2025, at roughly 15–30 receipts per professional per month, suggests about 45k–90k issuers that month. This is a rough estimate; January is a low season, so the real base is probably larger.
- The batch CSV removed the "one receipt at a time in the app" pain only for people who can build a correct CSV. Everyone else pays for a full suite (about R$32 a month or more) or uses a free template. That leaves room for a R$15–29 per month single-purpose tool.
- Seasonality: a retroactive rush in Jan–Feb (the prior year's deadline is the end of February) and the IRPF season in Apr–May. Launching in Nov–Dec 2026 would catch the Feb 2027 deadline for 2026 receipts.
- Liability is low. The tool only formats data that the professional reviews and imports into the official system, so a disclaimer is enough. Avoid the Rebots model of holding users' certificates and automating the government portal, which raises security and ToS issues.

### Gaps
- How many PF health professionals are registered and how many used Receita Saúde in 2025–2026.
- The official penalty for not using Receita Saúde (only a vendor claim found).
- Prices of PsicoPront, Corpora and other suites.
- Whether Receita plans native recurring receipts.

## 8. CNPJ alfanumérico (July 2026): who must adapt; product or dev task?

### Takeaway
Alphanumeric CNPJs started on 31 Jul 2026 for new registrations. Existing CNPJs do not change, both formats coexist, and numeric CNPJs can still be issued. This is a pure dev task, not a product.

### Cited Findings
- From 31 Jul 2026 CNPJs can combine letters and numbers in 14 characters. Existing entities keep their numbers "e não precisarão realizar qualquer procedimento". Both formats coexist, and purely numeric CNPJs can still be issued because only about 69 million of 99,999,999 combinations have been used. Systems are advised to adapt — [Agência Gov via Receita, Jul 2026](https://agenciagov.ebc.com.br/noticias/202607/implantacao-do-cnpj-alfanumerico-ocorrera-a-partir-de-31-de-julho)
- Earlier reports conflict:
  - a start focused on large companies — [Contábeis](https://www.contabeis.com.br/noticias/75609/cnpj-alfanumerico-deve-comecar-em-julho-de-2026-focado-apenas-em-grandes-empresas/) (search summary)
  - "obrigatório para todas as empresas em 2027" (headline) — [SEFIN-RO](https://reformatributaria.sefin.ro.gov.br/2026/03/16/cnpj-alfanumerico-inicia-em-julho-26-e-sera-obrigatorio-para-todas-as-empresas-em-2027/)
- Autocomplete queries are developer-oriented: "cnpj alfanumérico gerador", "… válido", "… exemplo valido" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=cnpj%20alfanum%C3%A9rico)

### Inferences
- Validators and generators are trivial and free; at most a free SEO traffic magnet. Excluded.

### Gaps
- None material.

## 9. ECA Digital (Lei 15.211/2025): age verification and parental control; any SMB website opportunity?

### Takeaway
The law has been in force since 17 Mar 2026, and ANPD enforcement actions start in Jan 2027, focused on age assurance. The duties fall on app stores and operating systems, on apps, and on sites with pornographic or otherwise prohibited content. Ordinary SMB websites are not the target, and age-verification products carry identity-data liability. Excluded.

### Cited Findings
- In force since 17 Mar 2026: art. 41-A, added by Lei 15.352/2026, after MP 1.319/2025 had set a six-month vacatio — [Correio Braziliense](https://www.correiobraziliense.com.br/cbradar/lei-15-211-o-eca-digital-preve-multa-de-ate-10-do-faturamento-no-brasil-limitada-a-r-50-milhoes-por-infracao-e-a-anpd-marca-janeiro-de-2027-para-comecar-as-acoes-de-fiscalizacao-com-foco-na-veri/); [Lefosse](https://lefosse.com/noticias/alerta/eca-digital-entra-em-vigor-em-17-de-marco-como-se-preparar/)
- Duties by article — [Correio Braziliense](https://www.correiobraziliense.com.br/cbradar/lei-15-211-o-eca-digital-preve-multa-de-ate-10-do-faturamento-no-brasil-limitada-a-r-50-milhoes-por-infracao-e-a-anpd-marca-janeiro-de-2027-para-comecar-as-acoes-de-fiscalizacao-com-foco-na-veri/):
  - Art. 12: app stores and operating systems must take "medidas proporcionais, auditáveis e tecnicamente seguras" to check age, offer parental supervision tools, and send apps an age signal through an API.
  - Art. 9: pornographic or prohibited content requires reliable age verification at every access, and self-declaration is banned.
  - Art. 14: apps must receive the age signal and keep their own mechanisms.
- ANPD schedule — [Correio Braziliense](https://www.correiobraziliense.com.br/cbradar/lei-15-211-o-eca-digital-preve-multa-de-ate-10-do-faturamento-no-brasil-limitada-a-r-50-milhoes-por-infracao-e-a-anpd-marca-janeiro-de-2027-para-comecar-as-acoes-de-fiscalizacao-com-foco-na-veri/):
  - Monitoring of app stores and operating systems since Mar 2026.
  - Age-assurance guidance from Aug 2026, with adaptation from Aug to Nov 2026.
  - Updated sanction regulations from Nov 2026.
  - Stage III enforcement from Jan 2027, with no specific day set.
  - The ANPD page was last updated on 10 Jun 2026 and shows no postponement.
- Sanctions (art. 35): a warning with up to 30 days to fix, then a fine of up to 10% of the group's Brazilian revenue. Without revenue the fine is R$10–1,000 per user, capped at R$50M per infraction. Suspension and bans are also possible — [Correio Braziliense](https://www.correiobraziliense.com.br/cbradar/lei-15-211-o-eca-digital-preve-multa-de-ate-10-do-faturamento-no-brasil-limitada-a-r-50-milhoes-por-infracao-e-a-anpd-marca-janeiro-de-2027-para-comecar-as-acoes-de-fiscalizacao-com-foco-na-veri/)
- Lei 15.352 (Feb 2026) made ANPD a regulatory agency, and Decreto 12.880 (Mar 2026) regulated the statute — [Correio Braziliense](https://www.correiobraziliense.com.br/cbradar/lei-15-211-o-eca-digital-preve-multa-de-ate-10-do-faturamento-no-brasil-limitada-a-r-50-milhoes-por-infracao-e-a-anpd-marca-janeiro-de-2027-para-comecar-as-acoes-de-fiscalizacao-com-foco-na-veri/)

### Inferences
- An SMB "age-gate" plugin cannot rely on self-declaration for restricted content. It would need identity-verification vendors and ANPD-compliant methods that are not yet specified. That is both a legal problem and an enterprise sale. Excluded.

### Gaps
- ANPD's final age-assurance guidance (due from Aug 2026) was not retrieved.

## 10. Pix Automático (June 2025) and recurring billing for small service businesses: players and fees

### Takeaway
Pix Automático has been live since 16 Jun 2025. Payers cannot be charged, and providers price freely; Asaas charges nothing beyond its standard Pix fees. Any product must sit on top of a payment provider and competes with those providers' own dashboards and with vertical systems. Trap.

### Cited Findings
- Launched on 16 Jun 2025 — [Agência Gov](https://agenciagov.ebc.com.br/noticias/202506/pix-automatico-chega-em-16-de-junho)
- Charging the payer is prohibited; the receiver's provider may charge the receiver at its own discretion — [BCB FAQ](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/pix-automatico-FAQ-participantes.pdf) (search summary)
- Fees:
  - Asaas: "não há nenhum custo adicional por utilizar a funcionalidade"; standard Pix receipt fees apply — [Asaas help center](https://central.ajuda.asaas.com/hc/pt-br/articles/41912520942235-Quais-s%C3%A3o-as-taxas-do-Pix-Autom%C3%A1tico-no-Asaas) (search summary)
  - Efí: R$3.50 per Pix Automático settled, against 1.19% for an ordinary Pix charge — [Efí blog](https://sejaefi.com.br/blog/qual-custo-do-pix) (search summary, vendor)
  - OpenPix: 0.8% per paid transaction — [OpenPix](https://openpix.com.br/articles/pix-para-recorrencia/) (search summary)
  - Cora: R$0.20–0.50 per transaction on average — [Cora](https://www.cora.com.br/blog/pix-automatico/) (search summary)
- The gym and course verticals are already being pitched — [Sistema Pacto](https://blog.sistemapacto.com.br/debito-recorrente-academia-quanto-custa-como-implementar-2026/); [Mercado Pago](https://www.mercadopago.com.br/blog/pix-automatico-academias-cursos-reduzir-inadimplencia)

### Inferences
- Holding funds requires a payment-institution licence, which constraint (c) excludes. A thin layer over Asaas or Efí competes with their free dashboards and with gym and school ERPs. Trap.

### Gaps
- Mercado Pago and Inter Pix Automático fees were not found.

## 11. Relatório de Transparência Salarial (Lei 14.611/2023): semiannual report for 100+ employees

### Takeaway
The report is semiannual. For the 6th cycle, the data update ran from 4 to 31 Aug 2026 and proof of publication was due by 30 Sep 2026. MTE generates the report itself; companies only fill in a form and publish it. Little room for a product.

### Cited Findings
- Between 4 and 31 Aug 2026, employers with 100 or more employees had to update their remuneration criteria, diversity actions and family/parenting initiatives in Portal Emprega Brasil for the 6th report, a semiannual mandatory document — [Agência Gov, Aug 2026](https://agenciagov.ebc.com.br/noticias/202608/empresas-com-100-ou-mais-empregados-devem-atualizar-informacoes-para-o-6o-relatorio-de-transparencia-salarial)
- Companies publish the report on their own channels and prove publication by 30 Sep. The fine is up to 3% of payroll, capped at 100 minimum wages — [Agência Brasil, Aug 2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-08/transparencia-salarial-empregadores-devem-atualizar-dados-ate-segunda) (search summary)
- The 5th report's deadline moved from 31 Mar to 6 Apr 2026 because of technical problems — [Agência Brasil, Mar 2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-03/relatorio-de-transparencia-salarial-pode-ser-publicado-ate-6-de-abril) (search summary)

### Inferences
- The buyers are companies with 100+ employees (HR and legal), and the government does the heavy lifting. Excluded: enterprise sale, low pain.

### Gaps
- The number of companies covered.

## 12. DCTFWeb/MIT, EFD-Reinf, eSocial changes in 2026, new NR updates, LGPD/ANPD enforcement

### Takeaway
I verified only the EFD-Reinf dividend code (NT 02/2026) and ANPD's new status as a regulatory agency; the search budget ran out before the rest. All of these belong to ERP and payroll vendors, not solo-developer products.

### Cited Findings
- EFD-Reinf NT 02/2026 (dividends in R-4010) — [TecnoSpeed](https://blog.tecnospeed.com.br/efd-reinf-nota-tecnica-02-2026-lucros-dividendos/)
- ANPD became a regulatory agency under Lei 15.352 (Feb 2026) — [Correio Braziliense](https://www.correiobraziliense.com.br/cbradar/lei-15-211-o-eca-digital-preve-multa-de-ate-10-do-faturamento-no-brasil-limitada-a-r-50-milhoes-por-infracao-e-a-anpd-marca-janeiro-de-2027-para-comecar-as-acoes-de-fiscalizacao-com-foco-na-veri/)

### Inferences
- Accounting ERPs absorb layout changes in federal ancillary obligations; autocomplete such as "distribuição de lucros 2026 reinf/dominio" points that way. Excluded.
- LGPD compliance kits for SMEs were not researched. Treat them as unproven, not as an opportunity.

### Gaps
- MIT/DCTFWeb changes in 2026, eSocial layout updates, other NR revisions, and ANPD sanctions against SMEs were not researched because the search budget was exhausted.

## 13. Other obligations starting in 2026–2027 found in searches (DeCripto and others)

### Takeaway
The standout is DeCripto (IN RFB 2.291/2025). Since 1 Jul 2026 it requires a monthly crypto report from anyone moving more than R$35k a month outside Brazilian exchanges. It has an official file layout, real fines and high-income users, and only a few Brazil-specific tools. The market appears small. The other items are ERP tasks or unconfirmed: NF-e debit/credit notes in 2027, CNPJ for individual IBS/CBS taxpayers in 2027, and MEI invoicing to individuals in 2027.

### Cited Findings
- IN RFB 2.291 was published on 14 Nov 2025. From 1 Jul 2026, individuals and companies must declare operations made through foreign providers, decentralized platforms (DEX) or without an intermediary when the monthly total exceeds R$35k (R$30k under IN 1.888) — [Exame, 18/11/2025](https://exame.com/invest/minhas-financas/nova-declaracao-de-cripto-nao-muda-tributacao-mas-aumenta-risco-de-multas/)
- How it is filed — [Blue Consult](https://blueconsult.com.br/coleta-nacional-decripto-tela-a-tela/):
  - Monthly, by the last business day of the following month; the first return (July operations) was due on 31 Aug 2026.
  - Filed in Coleta Nacional on e-CAC, either typed record by record or uploaded as a file in the official layout.
  - Three layouts (Manual approved by ADE Copes nº 2/2025): Exchange (national providers), Exchange Estrangeira and Sem Exchange.
  - Example records: 0210 (crypto-to-crypto swap), 0650 (transfer to a non-custodial wallet) and 0980 (atomic smart-contract operation reported by hash).
  - Values use fair value (art. 10) and the PTAX selling rate of the day (art. 11).
  - Blue Consult: "ninguém monta a DeCripto dentro do Coleta Nacional. Monta-se fora, numa planilha ou num software".
- The layout file is pipe-delimited with CR+LF line endings and DDMMAAAA dates. Exchange Estrangeira has 8 record types and Sem Exchange has 9 — [Manual de Orientação do Leiaute da DeCripto](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/manuais/manual-orientacao-leiaute-criptoativos/manual-de-orientacao-do-leiaute-da-decripto-v1.pdf) (search summary)
- Penalties (art. 13), per [Blue Consult](https://blueconsult.com.br/decripto-nova-declaracao-criptoativos/):
  - Late filing: R$100 a month for individuals; R$500 or R$1,500 a month for companies.
  - Incorrect or omitted information: 1.5% of the operation value for individuals; 3% for companies (minimum R$100).
  - Possible referral to the Federal Public Prosecutor (MPF) if there are signs of money laundering (art. 14).
  - Spontaneous correction before any notice avoids the fine (art. 15).
- Foreign providers serving Brazilian residents are also obligated reporters (art. 5º, I), and DeCripto implements the OECD's CARF — [Blue Consult](https://blueconsult.com.br/decripto-nova-declaracao-criptoativos/); [Mattos Filho](https://www.mattosfilho.com.br/unico/decripto-receita-federal-ocde/). ABToken argued that obligating foreign providers and setting penalties goes beyond the law — [Exame](https://exame.com/invest/minhas-financas/nova-declaracao-de-cripto-nao-muda-tributacao-mas-aumenta-risco-de-multas/)
- Receita open data under the IN 1.888 regime, monthly declared values in 2025 — [Receita Federal, Criptoativos – Relatório de Dados Abertos (Nov 2025)](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/criptoativos/arquivos/criptoativos_dados_abertos_20251112.pdf):

  | Channel (2025) | Monthly declared value |
  |---|---|
  | Individuals via foreign exchanges | R$502.4M (Jan), R$326.9M (Feb), R$271.7M (Mar), R$365.6M (Apr), R$355.8M (May), R$309.7M (Jun), R$584.1M (Jul), R$183.5M (Aug), R$93.6M (Sep) |
  | Individuals without an exchange | R$5.6M–R$367.2M |
  | Brazilian exchanges | R$17.6B–R$35.4B |

  Unique CPFs across all channels combined were 4.76M–6.03M per month in Jan–Apr 2025.
- Competitors, per Blue Consult's comparison (data consulted 08/09/2026; Blue sells a competing product) — [Blue Consult](https://blueconsult.com.br/melhor-programa-imposto-criptomoedas/):
  - Blue Cripto: a free tier without reports, and a "Completo" plan at R$697 per fiscal year (GCAP, IRPF, the monthly IN 1.888/DeCripto return and carnê-leão, up to 25k operations). Blue claims more than 10,000 declarations processed since 2018 (self-reported).
  - Fiscal Cripto: R$2,499 per 1,000 operations a month and R$4,799.90 per 10,000.
  - Declare Cripto: price only by quote, 45-day trial, Lite and Advanced plans.
  - Koinly (US$49–199 a year) and CoinTracking (US$49–899 a year) do not produce the DeCripto return.
- Autocomplete returns:
  - "decripto receita federal" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=decripto)
  - "declarar binance 2026", "como declarar binance no imposto de renda 2026" — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=declarar%20binance)
- Ajuste SINIEF 49/2025 moves to 1 Jan 2027 — [Debate Jurídico](https://debatejuridico.com.br/confaz-adia-obrigatoriedade-do-ajuste-sinief-49-2025-para-janeiro-de-2027/)
- The CNPJ requirement for individuals issuing IBS/CBS documents was postponed to 2027 — [RS Data](https://www.rsdata.com.br/cnpj-pessoa-fisica-documentos-fiscais-2027/) (search summary)
- Sebrae material says MEIs will have to invoice individuals too from 2027 (unconfirmed) — [Winsite](https://winsitegestao.com.br/blogs/central-do-mei-microempreendedor-individual/mei-sera-obrigado-a-emitir-nota-fiscal-em-2027-entenda-o-que-muda-e-como-se-preparar) (search summary)

### Inferences
- DeCripto market size is small. Dividing the 2025 monthly volume declared by individuals via foreign exchanges (R$94M–R$584M) by an assumed R$50k–200k per filer gives roughly 500–12,000 compliant individual filers a month. Non-compliance is probably large. CARF data exchange and the new 0650 self-custody record may push more people to file.
- Structural risk: if foreign exchanges report as obligated providers (or obtain Brazilian authorisation), users' own obligation shrinks to DEX, P2P and self-custody activity.
- Good fit otherwise: high-income buyers, a monthly deadline, a precise public file specification, few Brazil-specific tools, and published prices of R$697–2,499 a year, which proves willingness to pay.

### Gaps
- How many people have filed DeCripto since July 2026.
- Whether Binance, OKX and Bybit file as obligated providers.
- Google Trends for "decripto" (the request was rate-limited).
- Declare Cripto prices.
- Confirmation of the 2027 MEI invoicing rule.

## 14. Do affected people search for solutions themselves? (Google Trends BR and autocomplete, queried 12 Oct 2026)

### Takeaway
Yes for NFS-e Nacional and Receita Saúde, and for NR-1 until June; barely for the Simples hybrid option, IRPFM and Lei 15.270. Autocomplete shows mostly "how to" and "has it been postponed" intent. "nfs-e nacional api" and "receita saude em lote" are the only tool-seeking queries.

### Cited Findings
- 12-month Brazil averages in one comparison: "nfs-e nacional" 36, "receita saúde" 27, "riscos psicossociais" 22, "carnê leão" 12, "lei 15.270" 4 — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=riscos%20psicossociais,receita%20sa%C3%BAde,nfs-e%20nacional,carn%C3%AA%20le%C3%A3o,lei%2015.270)
- In a second comparison: "nr 1" 30 (an ambiguous term), "nfs-e nacional" 19, "receita saúde" 14, "simples nacional híbrido" 1, "irpfm" 1 — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=receita%20sa%C3%BAde,nfs-e%20nacional,nr%201,simples%20nacional%20h%C3%ADbrido,irpfm)
- Peaks: "nfs-e nacional" 100 in 4–10 Jan 2026; "riscos psicossociais" 71 and "receita saúde" 59 in 24–30 May 2026; "lei 15.270" 17 in 23–29 Nov 2025 — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=riscos%20psicossociais,receita%20sa%C3%BAde,nfs-e%20nacional,carn%C3%AA%20le%C3%A3o,lei%2015.270)
- The autocomplete lists are in sections 1, 3–8 and 13 — [Google autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=receita%20sa%C3%BAde)

### Inferences
- These are relative values only. Against "carnê leão" as a benchmark, "receita saúde" is a mainstream tax term among professionals. The final week (11–17 Oct) was incomplete when queried.

### Gaps
- Absolute monthly search volumes and CPCs; Google Ads Keyword Planner was not available.
- Trends for "decripto" (HTTP 429).

## 15. Candidate products: definitions, evidence and scores

### Takeaway
Only two candidates pass both gating criteria (willingness-to-pay evidence of 3 or more and low saturation of 3 or more):
- a Receita Saúde batch and receipt manager for self-employed health professionals;
- a DeCripto monthly file generator for crypto users.

Everything else fails on free official tools, saturation, suspended enforcement, licensing, or legal exposure.

### Cited Findings
- Price anchors (details and dates in sections 1–13):
  - Psicontrole R$97 for 90 days — [Psicontrole](https://psicontrole.com.br/)
  - Blue Cripto R$697 a year, Fiscal Cripto R$2,499 — [Blue Consult](https://blueconsult.com.br/melhor-programa-imposto-criptomoedas/)
  - Taochi R$30 per employee per month — [Taochi](https://taochi.com.br/blog/quanto-custa-adequacao-nr1-riscos-psicossociais/)
  - Focus NFe R$62.90–657.90 a month — [Focus NFe](https://focusnfe.com.br/precos/)
  - Official free Simples and IBS/CBS simulators — [Movimento Econômico](https://movimentoeconomico.com.br/receita-federal/2026/09/18/simulador-da-receita-indica-impacto-de-cbs-e-ibs-nas-empresas-do-simples/)
- Customer-count evidence found: only self-reported claims (Blue Consult ">10,000 declarações"; NRGuard "Mais de 100 empresas"/"847 PGRs") — [Blue Consult](https://blueconsult.com.br/coleta-nacional-decripto-tela-a-tela/); [NRGuard](https://nrguard.com.br/)

### Inferences
Scores run 1–5, where higher is better; "Low risk 5" means low risk. The revenue goal assumes US$5k ≈ R$27k a month, using the ≈R$5.4/US$ rate implied by the brief.

#### C1 — "Receita Saúde em lote": batch receipt manager for self-employed health professionals
- **Definition:** a web app that turns a patient list and monthly payments into the official Receita Saúde batch CSV for Carnê-Leão import. Payments can be typed or imported from a spreadsheet, a calendar or a bank Pix statement. It tracks which receipts have been issued (by reading the return file) and sends reminders at monthly close and before the end-of-February deadline.
- **Buyer and count:** psychologists, physiotherapists, speech and occupational therapists, dentists and doctors working as individuals. About 45k–90k or more active issuers, estimated from 1.37M receipts in Jan 2025 (section 7).
- **Pain and evidence:** receipts per patient every month. The official batch exists but needs a correct CSV. Vendors pitch the "Sunday night receipts" pain, and people search "receita saude em lote" (section 7).
- **Competitors:**
  - Psicontrole: R$97 per 90 days, price checked on its site.
  - PsicoPront: bundled, price not retrieved.
  - Corpora: in its Pro plan.
  - Rebots: an API for businesses.
  - A free YouTube template.
  - No revenue or customer counts were found.
- **Competitor weaknesses:**
  - The suites are full practice-management systems (agenda, patient records), which is overkill for someone who only wants receipts.
  - The free template is error-prone.
  - Rebots requires handing a digital certificate to a third party.
- **Demand signals:** Trends average 27, above "carnê leão" at 12; peaks in May and at the February deadline; autocomplete "em lote" and "retroativo".
- **Acquisition without contacts:**
  - SEO on long-tail how-to queries.
  - YouTube walkthroughs.
  - Public Instagram and Facebook communities of psychologists and physiotherapists.
  - A R$300–500 Google Ads test on "receita saúde em lote" and "planilha receita saúde".
  - Freemium, for example a free monthly receipt quota.
- **Build complexity:** low. CRUD, a CSV writer per manual v2.1, a return-file parser and subscription billing; a 1–2 week MVP.
- **Time to first revenue:** 2–6 weeks, timed for the Jan–Feb 2027 retroactive rush.
- **Main risks:**
  - Receita improves its own app or batch flow.
  - Suites bundle the feature.
  - Low revenue per user: about 1,100 subscribers at R$24.90 are needed for R$27k a month.
  - LGPD: patients' CPFs in a health context, so minimise and encrypt data.
  - The layout may change between versions.
- **Liability:** a disclaimer is enough, because this is a formatting tool and the user reviews and imports the file.
- **Scores:** WTP 3 · low saturation 3 · purchasing power 3 · distribution 4 · buildability 5 · speed 4 · low risk 3 = **25/35**. No exclusion flags.

#### C2 — "DeCripto mensal": DeCripto file generator
- **Definition:** a web app that imports history from foreign exchanges (CSV, or read-only API keys) and wallets, converts values at the PTAX rate, and classifies each operation into the official record types. It flags months above R$35k and exports the pipe-delimited Exchange Estrangeira and Sem Exchange files with an audit trail.
- **Buyer and count:** individuals operating above R$35k a month outside national providers. Roughly 500–12,000 compliant filers a month is my estimate (section 13), with a larger non-compliant pool.
- **Pain and evidence:**
  - Record-by-record entry, or an exact file format.
  - Rules on fair value and PTAX.
  - Common classification errors.
  - Fines of R$100 a month for late filing and 1.5% of the operation value for incorrect information (section 13).
- **Competitors:**
  - Blue Cripto: R$697 a year, published price; Blue Consult claims more than 10k declarations (self-reported).
  - Fiscal Cripto: R$2,499 per 1,000 operations, published price.
  - Declare Cripto: quote only.
  - Koinly and CoinTracking: no DeCripto return, according to Blue (a competitor).
- **Competitor weaknesses:** Blue is a consultancy that upsells services; Declare Cripto's pricing is opaque; Fiscal Cripto is expensive; the global tools lack Brazilian outputs.
- **Demand signals:** autocomplete "decripto receita federal" and "declarar binance 2026". Trends for "decripto" not obtained.
- **Acquisition without contacts:**
  - SEO for queries per exchange and wallet ("decripto binance", "decripto bybit", "decripto okx", "decripto metamask").
  - YouTube.
  - Public crypto Telegram, Discord and Reddit groups.
  - Small Google Ads bursts in the last ten days of each month.
- **Build complexity:** medium. Parsers for each exchange, PTAX data, record mapping and DeFi edge cases; a 2–4 week MVP covering 3 exchanges plus generic CSV and manual entry. I assume BCB PTAX rates can be pulled programmatically; not verified here.
- **Time to first revenue:** 3–6 weeks, with monthly deadlines creating repeated urgency.
- **Main risks:**
  - A small, possibly shrinking market if foreign exchanges report directly.
  - DeFi complexity.
  - Competition from Blue Consult's content.
  - Exchange CSV formats change.
  - Security of stored API keys (keep them read-only).
  - About 470 annual subscribers at R$697, or about 550 monthly subscribers at R$49, are needed for R$27k a month, which is a large share of the estimated base.
- **Liability:** a disclaimer alone is not enough. A wrong value costs the user 1.5% of the operation value. Mitigate by:
  - making the user review and transmit the file;
  - publishing the methodology;
  - offering no compliance guarantee;
  - never filing on the user's behalf;
  - suggesting accountant review for heavy DeFi use.
- **Scores:** WTP 4 · low saturation 3 · purchasing power 5 · distribution 3 · buildability 3 · speed 3 · low risk 2 = **23/35**. No exclusion flags, but the liability caution applies.

#### C3 — Simples hybrid-regime triage and client report for accountants
- **Definition:** upload a client list; the tool flags which clients should consider IBS/CBS outside the DAS and produces a white-label PDF documenting each decision.
- **Buyer:** accounting firms serving 11.6M ME/EPP (firm count unknown).
- **Pain:** "simular os dois cenários … documentar a decisão".
- **Competitors:** the free official simulator and at least seven free calculators; no paid tool found.
- **Demand:** Trends average about 1.
- **Channel:** SEO and accountants' public forums.
- **Build:** low to medium.
- **Time to first revenue:** slow; the next window is March 2027.
- **Risks:** free tools; volatile rules; liability if presented as a recommendation.
- **Scores:** 1 · 2 · 4 · 3 · 4 · 2 · 3 = **19/35**. Fails the WTP gate.

#### C4 — IRPFM and dividend planner (art. 16-B redutor with the §6º simplified calculation)
- **Definition:** schedules monthly distributions at or below R$50k per company per person, projects IRPFM, computes the redutor, and produces a PDF for the accountant.
- **Buyer:** partners earning more than R$600k (count unverified) and their accountants.
- **Pain:** redutor complexity (Planalto).
- **Competitors:** at least seven free calculators, ERPs (Domínio), and Receita's possible pre-filling.
- **Demand:** "lei 15.270" Trends average 4.
- **Channel:** SEO and LinkedIn content.
- **Build:** medium.
- **Time to first revenue:** 4–8 weeks, with the main window in Mar–May 2027.
- **Risks:** regulation still pending (§§4º–5º); advice liability.
- **Scores:** 2 · 2 · 5 · 3 · 4 · 3 · 2 = **21/35**. Fails the WTP gate.

#### C5 — NFS-e Nacional emitter or API for Simples service providers
- **Scores:** 4 · 1 · 3 · 2 · 2 · 2 · 2 = **16/35**.
- **Why it fails:** proven WTP but saturated: a free official emitter; Focus, NFE.io, Brasil NFe, eNotas, Nuvem Fiscal and PlugNotas; ERPs and billing tools; plus certificate custody and support load. **Trap.**

#### C6 — NR-1 psychosocial self-serve COPSOQ platform
- **Scores:** 4 · 1 · 3 · 2 · 4 · 3 · 1 = **18/35**.
- **Why it fails:** saturated; sanctions suspended until about late Dec 2026; criteria under conciliation; the AI-generated-PGR variant is excluded as an AI wrapper. **Trap.**

#### C7 — ECA Digital age-gate or parental-control kit for SMB sites
- **Scores:** 1 · 3 · 3 · 2 · 2 · 2 · 1 = **14/35**.
- **Why it fails:** the obligations sit with app stores, operating systems, apps and adult sites; self-declaration is banned; identity-data liability; ANPD rules pending. **Excluded: legal problem / enterprise sale.**

#### C8 — Pix Automático recurring-billing layer for gyms, schools and clinics
- **Scores:** 4 · 1 · 3 · 2 · 3 · 3 · 2 = **18/35**.
- **Why it fails:** needs a payment provider (a licence if it holds funds); Asaas adds no fee; vertical systems already integrate. **Trap.**

#### C9 — CNPJ alfanumérico validator or migration kit
- **Scores:** 1 · 1 · 2 · 3 · 5 · 4 · 5 = **21/35**.
- **Why it fails:** existing CNPJs are unchanged and free libraries exist. **Excluded: no WTP (a dev task).**

#### C10 — Transparência Salarial helper
- **Scores:** 1 · 3 · 4 · 1 · 4 · 2 · 4 = **19/35**.
- **Why it fails:** MTE generates the report and the buyers are 100+ employee companies. **Excluded: enterprise sale / needs contacts.**

#### C11 — Individual landlord IBS/CBS checker and individual-vs-holding simulator
- **Scores:** 1 · 3 · 5 · 3 · 4 · 2 · 2 = **20/35**.
- **Why it fails:** small affected population, free calculators, advice liability. Fails the WTP gate.

#### Scoring summary

| # | Candidate | WTP | Low sat. | Buyer power | Distribution | Build | Speed | Low risk | Total | Gate / flag |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Receita Saúde batch manager | 3 | 3 | 3 | 4 | 5 | 4 | 3 | 25 | Passes |
| C2 | DeCripto file generator | 4 | 3 | 5 | 3 | 3 | 3 | 2 | 23 | Passes (liability caution) |
| C4 | IRPFM/dividend planner | 2 | 2 | 5 | 3 | 4 | 3 | 2 | 21 | Fails WTP |
| C9 | CNPJ alfanumérico kit | 1 | 1 | 2 | 3 | 5 | 4 | 5 | 21 | Excluded (no WTP) |
| C11 | Landlord IBS/CBS checker | 1 | 3 | 5 | 3 | 4 | 2 | 2 | 20 | Fails WTP |
| C3 | Simples hybrid report | 1 | 2 | 4 | 3 | 4 | 2 | 3 | 19 | Fails WTP |
| C10 | Transparência Salarial helper | 1 | 3 | 4 | 1 | 4 | 2 | 4 | 19 | Excluded (enterprise sale) |
| C6 | NR-1 COPSOQ self-serve | 4 | 1 | 3 | 2 | 4 | 3 | 1 | 18 | Trap; AI variant excluded |
| C8 | Pix Automático billing layer | 4 | 1 | 3 | 2 | 3 | 3 | 2 | 18 | Trap (licence/PSP) |
| C5 | NFS-e Nacional emitter | 4 | 1 | 3 | 2 | 2 | 2 | 2 | 16 | Trap (saturated) |
| C7 | ECA Digital age-gate | 1 | 3 | 3 | 2 | 2 | 2 | 1 | 14 | Excluded (legal/enterprise) |

- Any "Reforma Tributária AI assistant" or "chatbot for accountants" idea is excluded by constraint (e). I did not research it.

### Gaps
- Revenue and customer counts for all competitors (none verified).
- Absolute search volumes and CPCs.
- The number of PF health professionals and of DeCripto filers.
- Prices of the psychologist practice-management suites other than Psicontrole.

## 16. Top 2 candidates and traps

### Takeaway
1. **C1, the Receita Saúde batch and receipt manager.** It has the best mix of a forced recurring obligation, a large base, an official file route (no ToS issues), low liability and the fastest build.
2. **C2, the DeCripto monthly file generator.** It has the strongest willingness-to-pay evidence and the richest buyers, but the market is small and may shrink, and liability is higher.

Popular-sounding traps: NFS-e emitters, NR-1 psychosocial platforms, Simples hybrid simulators, dividend and IRPFM calculators, Pix Automático billing, CNPJ alfanumérico tools, ECA Digital age-gates, Transparência Salarial helpers, split-payment tools and generic IBS/CBS price calculators.

### Cited Findings
- Trap evidence:
  - **NFS-e emitter:** a free Emissor Nacional, plus Focus NFe at R$62.90–657.90 a month, NFE.io at R$190–375 and Brasil NFe at R$99.90 — [Focus NFe](https://focusnfe.com.br/precos/); [NFE.io](https://nfe.io/precos/emissao-nfse/); [Brasil NFe](https://www.brasilnfe.com.br/products/nfs-e/)
  - **NR-1:** sanctions suspended and the suspension extended on 25/09/2026 — [Migalhas](https://www.migalhas.com.br/quentes/465248/andre-mendonca-prorroga-por-mais-90-dias-suspensao-de-sancoes-da-nr-1). Existing SaaS at R$30 per employee per month — [Taochi](https://taochi.com.br/blog/quanto-custa-adequacao-nr1-riscos-psicossociais/). Search interest fell from 71 to about 15 — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=riscos%20psicossociais,receita%20sa%C3%BAde,nfs-e%20nacional,carn%C3%AA%20le%C3%A3o,lei%2015.270)
  - **Simples hybrid simulator:** an official free simulator since 18/09/2026 — [Movimento Econômico](https://movimentoeconomico.com.br/receita-federal/2026/09/18/simulador-da-receita-indica-impacto-de-cbs-e-ibs-nas-empresas-do-simples/); free calculators — [Calculadora Contábil](https://www.calculadoracontabil.com.br/calculadoras/comparativo-simples-hibrido-rt)
  - **Dividend and IRPFM calculators:** free tools — [Calculabr](https://calculabr.net.br/calculadora-imposto-dividendos/), [Somas](https://somas.io/investimentos/simulador-irpfm); Receita may compute the redutor itself (art. 16-B §7º) — [Planalto](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm)
  - **Pix Automático:** Asaas adds no fee — [Asaas](https://central.ajuda.asaas.com/hc/pt-br/articles/41912520942235-Quais-s%C3%A3o-as-taxas-do-Pix-Autom%C3%A1tico-no-Asaas)
  - **CNPJ alfanumérico:** existing CNPJs unchanged and formats coexist — [Agência Gov](https://agenciagov.ebc.com.br/noticias/202607/implantacao-do-cnpj-alfanumerico-ocorrera-a-partir-de-31-de-julho)
  - **ECA Digital:** obligations sit with app stores, operating systems, apps and adult sites; self-declaration is banned — [Correio Braziliense](https://www.correiobraziliense.com.br/cbradar/lei-15-211-o-eca-digital-preve-multa-de-ate-10-do-faturamento-no-brasil-limitada-a-r-50-milhoes-por-infracao-e-a-anpd-marca-janeiro-de-2027-para-comecar-as-acoes-de-fiscalizacao-com-foco-na-veri/)
  - **Transparência Salarial:** MTE generates the report — [Agência Gov](https://agenciagov.ebc.com.br/noticias/202608/empresas-com-100-ou-mais-empregados-devem-atualizar-informacoes-para-o-6o-relatorio-de-transparencia-salarial)
  - **Split payment:** optional, B2B only, H2 2027 — [Radar da Reforma Tributária](https://radardareformatributaria.com/split-payment-testes-2026-implantacao-gradual-2027/)
  - **IBS/CBS price calculators:** an official free calculator exists — [Movimento Econômico](https://movimentoeconomico.com.br/receita-federal/2026/09/18/simulador-da-receita-indica-impacto-de-cbs-e-ibs-nas-empresas-do-simples/)
  - **Automating government portals with users' certificates**, as Rebots does, carries security and ToS risk — [Rebots](https://rebots.com.br/api-receita-saude)

### Inferences
- **Why C1 first:**
  - The obligation has been mandatory and monthly since 2025.
  - Since Nov 2025 there is an official, documented file route, so the product never touches government credentials.
  - Willingness to pay is shown by paid suites bundling the feature (Psicontrole R$97 per 90 days).
  - Searchers show clear intent ("receita saude em lote").
  - It is the simplest build, and the Jan–Feb 2027 deadline arrives right after a Nov–Dec 2026 launch.
  - The path to US$5k a month needs about 1,100 subscribers at about R$25, or growth through:
    - clinic multi-professional plans;
    - Carnê-Leão and livro-caixa add-ons;
    - an annual plan sold around the February deadline.
- **Why C2 second:**
  - High-income buyers face a new monthly obligation with fines and a precise public specification.
  - Competitors charge R$697–2,499 a year, but only one Brazil-specific tool shows a published DeCripto price.
  - The constraints are a possibly very small, shrinking base and real data-accuracy liability.
  - Treat it as a higher-revenue-per-user bet that needs validation: for example, a landing page with a waitlist before the end of October and November 2026 deadlines, plus a converter for one exchange first.
- **Runner-up:** C4 (the IRPFM planner for accountants) could be reconsidered for Feb–May 2027 if Receita does not pre-compute the redutor. I found no current willingness-to-pay evidence.
- **Where a disclaimer is enough and where it is not:**
  - **Enough:** C1 (a formatting tool; the user imports into the official system) and C9.
  - **Partly enough:** C3 and C4, only if sold to professionals as scenario simulations with explicit assumptions and no "recommendation" wording.
  - **Not enough:** C2, because wrong data causes fines of 1.5% of value; it needs a review-and-submit-yourself design, a published methodology, terms limiting liability, and no filing on the user's behalf. Also C6 ("laudo"/compliance claims while criteria are suspended) and C7 (age-assurance compliance claims).
- **Budget fit (approximate costs, not verified here):** a .com.br domain, free-tier hosting and a R$300–500 Google Ads test fit within R$700 for C1 and C2. Neither needs a licence, certification, hardware or an enterprise sale.

### Gaps
- No verified competitor revenue for either top candidate.
- Absolute search volumes and CPCs for "receita saúde em lote" and "decripto".
- LGPD specifics for storing patients' CPFs (C1) and exchange API keys (C2) were not researched.
- Whether Receita will add native batch or recurring receipts to the app (C1 platform risk), or will list foreign exchanges as obligated reporters (C2 market risk).
