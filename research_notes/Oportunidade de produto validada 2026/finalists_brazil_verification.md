# Stress test of four Brazilian software finalists (verification round, data gathered 2026-10-12)

Method note: all pages were fetched with curl on 2026-10-12 unless a finding says "search summary" (WebSearch result text, page not opened). DuckDuckGo returned a captcha and Bing returned irrelevant results, so discovery used WebSearch plus direct URLs. Google Autocomplete was queried with `client=firefox&hl=pt-BR&gl=br`; "[n]" is the number of suggestions returned. Any seed can be reproduced by swapping `q=` in [this URL](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=receita%20saude%20em%20lote). "Self-reported" marks vendor claims.

## Finalist 1: Is a Receita Saúde batch-receipt tool still a gap?

### Takeaway
KILL as a standalone paid product. The contradiction resolves against the opportunity. The Receita itself publishes a free official CSV model (file dated 2025-10-20). At least four practice-management suites already export the batch file, and one also reads the return file to track issued receipts. Free templates are on YouTube, a paid spreadsheet exists, and an accountant on a forum calls the file "bem simples" to build. Tool-seeking searches are almost nonexistent: "planilha", "csv", "excel", "gerador" and "automatizar" seeds all return 0 suggestions.

### Cited Findings
**Official layout and process (primary sources, verified 2026-10-12)**
- Manual Receita Saúde v2.1 (Oct 2025), Q24 covers batch issue. The steps are:
  1. Build the file.
  2. In e-CAC, open Carnê-Leão and choose "Escrituração" → "Importar Escrituração".
  3. Click "Analisar Arquivo". The error report gives line, field and description.
  4. Click "Importar".
  5. Download the list of generated receipts with their numbers.
  - File rules: "formato CSV (campos separados por ponto e vírgula)" with "até 1000 linhas".
  - Q25: a wrong batch can be cancelled in bulk via "Desfazer escrituração".
  - Source: [Manual Receita Saúde 2.1](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/manuais/orientacao-tributaria/receita-saude-2.1.pdf)
- Penalty: a professional who does not issue the receipt, or issues it with errors, "estará sujeito à multa de R$ 100 (cem reais) por mês calendário ou fração", under art. 4 of IN RFB 2.240/2024 — [Manual Receita Saúde 2.1, Q6](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/manuais/orientacao-tributaria/receita-saude-2.1.pdf)
- The official "Recibos do Receita Saúde" layout has 16 fields:
  - Data do pagamento (DD/MM/AAAA, all lines in the same year)
  - Código do rendimento, fixed "R01.001.001"
  - Código da ocupação: 225 médico, 226 odontólogo, 230 fonoaudiólogo, 231 fisioterapeuta, 232 terapeuta ocupacional, 255 psicólogo
  - Valor, with comma decimals and no thousands separator
  - Dedução, empty
  - Descrição, up to 255 characters
  - "PF", fixed
  - CPF do pagador
  - CPF do beneficiário
  - Four fields that are always empty
  - Indicador de recibo "S"
  - CPF do profissional
  - Registro profissional, up to 15 characters
  - Source: [Receita Federal – Formato do arquivo de Escrituração](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/manual/formato-arquivo)
- **The Receita gives away the template.**
  - The Carnê-Leão manual page links "Baixe o modelo" — [Manual do Carnê-Leão](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/manual). I downloaded the ZIP. It contains "Modelo de arquivo para recibos do Receita Saúde.csv" (dated 2025-10-20 in the archive), a sample line `99/99/9999;R01.001.001;999;999999999,99;;Recibo do Receita Saúde;PF;99999999999;99999999999;;;;;S;99999999999;REGISTRO_PROFISSIONAL`, and an instruction PDF.
  - The PDF says "São três modelos para importação de rendimentos, dois para pagamentos e um para recibos do Receita Saúde… utilize-os como base para construção de seus próprios arquivos" — [escrituracao-carne-leao.zip](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/documentos-tecnicos/escrituracao-do-carne-leao/escrituracao-carne-leao.zip)
- Fenacon (4 Nov 2025): the feature "busca atender às necessidades de profissionais que utilizam sistemas de gestão de consultório ao permitir que esses sistemas gerem arquivos de integração" — [Fenacon](https://fenacon.org.br/noticias/disponibilizada-nova-funcionalidade-para-emissao-em-lote-de-recibos-do-receita-saude/)

**Competitor census: tools that generate the batch file (accessed 2026-10-12)**

| Tool | Type | Price | What it does with Receita Saúde | Source |
|---|---|---|---|---|
| Receita Federal official model | Free CSV template | R$0 | Template + error-checking importer in e-CAC | [ZIP](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/documentos-tecnicos/escrituracao-do-carne-leao/escrituracao-carne-leao.zip) |
| Psicontrole | Psychologist suite | R$97 for 90 days ("Black Friday" promo; no list price shown) | "gere o lote de recibos do Receita Saúde quando precisar fechar o período" | [Psicontrole](https://psicontrole.com.br/) |
| PsicoPront | Psychologist suite (also uses GPT-4o-mini summaries) | R$79/month or R$790/year, single plan | Exports a CSV in the official format, code 255 preset, "Até 1000 recibos por arquivo"; claims it "Evita multa de R$ 100,00" (self-reported) | [PsicoPront recursos/preços](https://psicopront.com.br/recursos) |
| Corpora | Psychologist suite, Pro plan | Price not found | Launched 14 Apr 2026. Generates the import file, then **reads the return file** so the system knows which receipts were issued; Corpora Pay payments feed the flow | [Leia Notícias (DINO press release)](https://leianoticias.com.br/329672-corpora-lanca-integracao-com-receita-saude-para-psicologos/) |
| Clínica Idée | Practice suite | Not found | "Gerar escrituração para carnê-leão" CSV export (help article "há 2 anos", so possibly income-only, pre-Receita-Saúde layout) | [Clínica Idée help](https://clinicaidee.tawk.help/article/aprenda-a-usar-o-arquivo-de-escritura%C3%A7%C3%A3o-para-carn%C3%AA-le%C3%A3o) |
| Clinicorp | Dental suite | Not checked | Blog lists "Integração Clinicorp x Receita Saúde"; content not readable (JS) | [Clinicorp search](https://www.clinicorp.com/?s=receita+saude) |
| ePlanilhas | Paid spreadsheet | R$149.90 (list R$299.80) | "Planilha de importação de carne leão em csv"; Receita Saúde compatibility not verified | [ePlanilhas](https://www.eplanilhas.com.br/planilha-de-importacao-de-carne-leao-em-csv/) |
| Contabiliza Mais (YouTube) | Free template | R$0 | "Receita Saúde em LOTE: Gere vários recibos com 1 arquivo (tutorial com modelo grátis)" | [YouTube oEmbed-verified title](https://www.youtube.com/watch?v=UWvzUaK6Xfg) |
| salutti (GitHub) | Open-source practice tool | Free | PR titled "Fiscal: carnê-leão, Receita Saúde, recibo e informe anual" (search summary; not opened) | [GitHub](https://github.com/vittorccf/salutti/pull/48) |
| PSICLO | Platform | Unknown | Terms of use mention fortnightly receipt issuing as a paid service (search summary) | [PSICLO terms PDF](https://yamrgxjnvdhpxbeejmuo.supabase.co/storage/v1/object/public/legal-docs/TERMOS_DE_USO_PSICLO_PF.pdf) |

- Contábeis forum thread (23 Nov 2025; 1 reply, 427 views): an accountant asked for the file. The reply: "é bem simples elaborar essa planilha. Crie as colunas com cada campo e respeite os formatos… salve com a extensão CSV" — [Contábeis fórum](https://www.contabeis.com.br/forum/tributos-federais/411363/emissao-em-lote-de-recibos-do-receita-saude/)
- Simples Dental's Receita Saúde guide covers the app and procurations but does not advertise a batch export — [Simples Dental blog](https://simplesdental.com/blog/?p=4700)
- Agilize (an accounting firm, 9 May 2026) promotes batch issue and accounting automation as part of its service — [Agilize](https://agilize.com.br/artigos/?p=2534)

**Size of the base**
- January 2025, the first mandatory month: 1,368,312 receipts were issued. "Os três primeiros profissionais foram responsáveis por mais de 90% dos recibos". In 2024 (optional phase) 498 thousand receipts were issued — [Jornal Contábil, 06/02/2025](https://jornalcontabil.com.br/noticia/receita-saude-mais-de-13-milhao-de-recibos-foram-emitidos-em-janeiro/)
- Psychologists issued "mais de 400 mil" receipts in January 2025 and were the second-largest category — [CFP, 11/02/2025](https://site.cfp.org.br/profissionais-da-psicologia-emitem-mais-de-400-mil-recibos-virtuais-em-janeiro/)
- Number of psychologists: "cerca de 437 mil psicólogos ativos" (press figure, undated; search summary) — [Correio 24 Horas](https://www.correio24horas.com.br/economia/6-dicas-essenciais-para-quem-deseja-empreender-em-psicologia-1025)
- I found no official count of how many distinct professionals issue receipts in 2025–2026 (searched twice).

**PT-BR demand signals (Google Autocomplete, 2026-10-12)**
- Tool-seeking seeds:
  - "receita saude em lote" [1]: only itself
  - "receita saude lote" [1] and "receita saúde lote" [1]: both → "receita saude em lote"
  - "receita saude importar" [1] → "importar receita saude"
  - "importar escrituração carne leão" [1]
  - "receita saude sistema" [2]: includes "sistema receita saude fora do ar"
- Zero suggestions for:
  - "receita saude planilha", "planilha receita saude", "modelo planilha receita saude"
  - "receita saude csv", "receita saude excel"
  - "receita saude automatizar", "receita saude varios recibos"
  - "emitir recibos em lote", "gerador recibo receita saude"
  - "receita saude extensão", "carne leao importar arquivo"
- How-to seeds are rich:
  - "recibo receita saude" [10]: "serve como nota fiscal", "pode ser emitido retroativo", "ecac", "nutricionista"
  - "receita saude carne leao" [10]
  - "receita saude psicologo" [10]: "passo a passo", "app", "retroativo", "crp"
  - "receita saude retroativo" [10]
  - "receita saude erro" [6]: "erro 02", "erro 01", "erro inesperado"
  - "receita saude multa" [3]
  - "carne leão planilha" [4]: "planilha carne leao 2026/2025/aluguel"
  - "recibo psicologo" [10]
- Source for all: [Google Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=receita%20saude%20lote)
- The earlier researcher's Trends data puts "receita saúde" at a 12-month average of 27 against 12 for "carnê leão", with a May 2026 peak of 59 (from brazil_regulatory_demand.md; not re-checked) — [Google Trends](https://trends.google.com/trends/explore?date=today%2012-m&geo=BR&q=riscos%20psicossociais,receita%20sa%C3%BAde,nfs-e%20nacional,carn%C3%AA%20le%C3%A3o,lei%2015.270)

### Inferences
- **The contradiction resolves this way.** Researcher A was right that the batch file is sold only inside suites; no standalone paid SaaS was found. Researcher B was right that it is no longer a gap: the Receita itself ships a free template and error-checking importer, and the cheapest suite that includes it costs R$79/month for a whole practice system. A standalone tool would compete with free, below a R$79 all-in-one.
- **The best version of the idea has already shipped.** The "track what has been issued" feature (reading the Carnê-Leão return file) exists in Corpora since April 2026.
- **The realistic target does not search for it.** Professionals without a practice system ask "how do I issue / is it retroactive / what is erro 02". They do not ask "spreadsheet / generator / batch tool". With ~0 tool-seeking query volume, a R$700 search-ads test would mostly buy how-to traffic.
- **Professionals without a system have revealed low software WTP.** Those with many patients (the batch use case) are the ones most likely to already have a suite.
- **LGPD risk (inference, not checked with counsel).** The file holds patient and payer CPFs tied to a health service, which plausibly counts as sensitive health data under LGPD art. 11. A server-side tool would carry security and liability burdens. A browser-only generator avoids this but is trivially copyable and hard to charge for.
- A free, client-side "gerador de CSV Receita Saúde" could still work as an SEO lead magnet for some other product. As a business, it fails.

### Gaps
- The prices of Corpora Pro, Clinicorp and Clínica Idée, and whether iClinic, Ninsaúde, Feegow, Amplimed and Doctoralia support the batch file. Their sites were search pages or JS-rendered.
- The share of PF health professionals without any practice-management system. No survey found.
- An official 2025 annual total of receipts and distinct issuers. Not found in two searches.
- Absolute search volumes and CPCs (no Keyword Planner access).

## Finalist 2: Field-inspection report generator for engineers and architects (vistoria cautelar, inspeção predial/autovistoria, vistoria de recebimento)

### Takeaway
CONDITIONAL, and the strongest of the four. Brazilian vistoria apps are crowded, but almost all target rental and vehicle inspections. Engineering-grade tools are few and small: Howse at R$70/month, plus generic form builders and FSM tools such as Inspect App, Inspeção Pro, Onlaine and Produttivo. The legal driver is real but weakly enforced: IBAPE counts 41 municipal and 5 state inspection laws, yet only 9 municipal and 1 state law are regulated. Rio, the flagship, had only 11.7% compliance a year after its 2014 deadline. Demand surfaces as template searches ("modelo", "pdf", "word") rather than software searches. That makes template SEO the realistic channel, but those searchers lean toward free.

### Cited Findings
**Competitor census (accessed 2026-10-12)**

| Tool | Focus | Price | Traction proxy | Source |
|---|---|---|---|---|
| Howse | Engineering vistorias and laudos prediais, "Feito por Engenheiros", AI conclusions | "De R$ 70/mês", 20% off annual (earlier notes: R$672/yr, 20 vistorias/month) | No Play listing found under the obvious IDs; testimonials only | [Howse](https://howseapp.com/) |
| Inspect App (InMediam) | Generic inspection forms with HTML laudo templates, photo markup | Demo only | "10 mil usuários ativos", "2.500+ formulários enviados… todos os meses" (self-reported); Play "Inspect - Smart Vistoria" 1,000+ installs, 11 reviews | [Inspect App](https://inspectapp.com.br/), [Play](https://play.google.com/store/apps/details?id=br.com.inmediam.inspect) |
| Inspeção Pro | FSM/inspection app, "Laudos automáticos com a marca de sua empresa" | "assinatura mensal", no price | Play subscriber app 100+ installs | [Inspeção Pro](https://inspecao.pro/), [Play](https://play.google.com/store/apps/details?id=com.inspecaomobile) |
| Onlaine Inspeção | "inspeções e laudos técnicos" for engineering firms | Plans page has no prices | n/a | [Onlaine](https://www.onlaine.com.br/) |
| Produttivo | Generic FSM; publishes a laudo de inspeção predial guide | No public price (15-day trial) | n/a | [Produttivo blog](https://www.produttivo.com.br/blog/o-que-e-laudo-de-inspecao-predial) |
| GoAudits | Global audit app | US$10/user/month Starter, US$30 Enterprise (annual) | n/a | [GoAudits pricing](https://goaudits.com/pricing/) |
| Checklist Fácil | Generic checklists | Pricing page JS-only, not read | n/a | [Checklist Fácil](https://www.checklistfacil.com/precos/) |
| Rede Vistorias (nKey) | Rental vistorias | Not read (JS) | Play 5,000+ installs, 73 reviews | [Play](https://play.google.com/store/apps/details?id=br.com.redevistorias.vistorias) |
| Vistoria de Imóveis (BeSoft) | Rental | n/a | Play 100,000+ installs, 668 reviews | [Play](https://play.google.com/store/apps/details?id=br.com.besoft.bevistoria) |
| Pleno Vistoria | Rental | No public price | Play 10,000+, 431 reviews | [Play](https://play.google.com/store/apps/details?id=br.com.plenosoftware.vistoria) |
| Vistoriador Online | Rental/general | n/a | Play 10,000+, 10 reviews, last update Jun 2025 | [Play](https://play.google.com/store/apps/details?id=com.vistoriadoronline.natively) |
| Hauseful | Rental, service + app | Service R$545–833/month (earlier notes) | Play 1,000+, 128 reviews | [Play](https://play.google.com/store/apps/details?id=com.hauseful.fhost.app) |
| VistoHouse | Rental | n/a | Play 1,000+, 89 reviews | [Play](https://play.google.com/store/apps/details?id=br.com.vistohouse) |
| Vistortec | Rental | R$59.90–299/month (earlier notes) | Play 500+, 11 reviews | [Play](https://play.google.com/store/apps/details?id=br.com.vistortec) |
| Coonecta Vistoria | General | n/a | Play 1,000+, 8 reviews | [Play](https://play.google.com/store/apps/details?id=com.coonecta_vistoria) |
| VistorIA (Aesgaard) | Rental, AI | n/a | Play 100+ | [Play](https://play.google.com/store/apps/details?id=app.aesgaard.vistoria) |
| Plinto | Unknown | n/a | plinto.app returns only the title "Plinto" (JS shell) | [Plinto](https://plinto.app/) |
| Vistoria Online | Unknown | n/a | vistoriaonline.com.br failed TLS verification; not read | — |

- Play search results for "vistoria predial", "vistoria cautelar" and "laudo de vistoria" are dominated by rental, Detran and vehicle vistoria apps (checkpro, carfacts, detran.vistoria2). No engineering-specific app with meaningful installs appeared — [Play search](https://play.google.com/store/search?q=vistoria%20cautelar&c=apps&hl=pt_BR&gl=BR)
- Earlier notes list Devolus (free for 2 vistorias/month, then R$79.90–139.90) and Afirma Vistoria Fácil (R$1,500 setup, for construtoras) — [Devolus](https://www.aplicativodevistoria.com.br/), [Afirma](https://afirma.cc/vistoria-facil/)

**Standards and mandates**
- ABNT NBR 16747 (Inspeção predial), "1ª Edição 21/05/2020" — [IBAPE mesa-redonda 2026 (Roxo, Falcão, Rabelo, Santana)](https://biblioteca.ibape-nacional.com.br/wp-content/uploads/2026/01/adrian1.pdf)
- IBAPE's survey of inspection laws (2026):
  - "5 legisl. estaduais" and "41 legisl. municipais"
  - By decade: 1991–2000 5 municipal/0 state; 2001–2010 9/1; 2011–2020 20/3; 2021–2025 7/1
  - 33 municipal laws predate NBR 16747 and 8 are later
  - 22 municipal laws mention technical norms; 16 of those "mencionam, mas não definem" which
  - Regulation exists for only 9 municipal and 1 state law; 32 municipal and 4 state laws are unregulated
  - Cities include Rio de Janeiro, Niterói, Duque de Caxias, Nova Iguaçu, Campos, Cabo Frio, Santos, Guarujá, São Vicente, Guarulhos, Jundiaí, Mogi das Cruzes, Ribeirão Preto, Bauru, Caraguatatuba, Arujá, Maringá, Balneário Camboriú, Porto Alegre, Canoas, Bagé, Torres, Capão da Canoa, Cidreira, Xangri-lá and Salvador (Lei 5.907/2001, Decreto 13.251/2001)
  - Federal PL 6.014/2013 is still a bill
  - Source: [IBAPE 2026](https://biblioteca.ibape-nacional.com.br/wp-content/uploads/2026/01/adrian1.pdf)
- Rio de Janeiro:
  - State Lei 6.400/2013 and municipal LC 126/2013 were regulated by Decreto 37.426 (11 Jul 2013)
  - Autovistoria is required "com intervalo máximo de 05 (cinco) anos", by an engineer, architect or firm with ART/RRT
  - Exemptions include buildings of up to two floors and 1,000 m² and AEIS areas
  - Source: search summary of [Sindiconet](https://www.sindiconet.com.br/informese/autovistoria-noticias-administracao)
  - The city's service page "Comunicação de Autovistoria" exists (last updated March 2024 per the search summary) — [Carioca Digital](https://carioca.rio/servicos/comunicacao-de-autovistoria/)
- Rio compliance (old data): about 270k buildings were obliged at the 1 Jul 2014 deadline and only 5% had filed — [JB, 24/06/2014](https://www.jb.com.br/rio/noticias/2014/06/24/amp/prazo-para-autovistoria-em-predios-do-rio-termina-dia-1o-julho.html). One year later only 11.7% (31,785) had complied (search summary) — [Sindiconet](https://www.sindiconet.com.br/informese/autovistorias-noticias-manutencao-1)
- Balneário Camboriú Lei 2.805/2008 is described as the only SC law with mandatory periodic inspection — [CREA-SC](https://portal.crea-sc.org.br/inspecao-predial-crea-sc-participa-de-audiencia-na-alesc-para-tratar-de-minuta-de-projeto-de-lei-no-estado/) (search summary)
- Fortaleza (Lei 9.913/2012) is reported as lacking effective enforcement — [Diário do Nordeste](https://diariodonordeste.verdesmares.com.br/politica/legislacao-sobre-inspecao-predial-e-desafio-em-outras-capitais-1.2164869) (search summary)
- Porto Alegre: sources conflict on the law number (LC 284/1992 with Decreto 18.574/2014 vs. "Lei 806/2017") — [IBAPE 2020](https://ibape-nacional.com.br/biblioteca/wp-content/uploads/2020/03/III-Sem-Nac-de-Eng-de-Av-e-Per-Patricia-Bitencourt.pdf), [Câmara POA](https://www.camarapoa.rs.gov.br/draco/sessoes_plenarias/83178/1571340056.pdf) (search summaries)
- Vistoria cautelar: the main references are IBAPE norms (IBAPE-SP 2013, IBAPE-MG 2014) and municipal tender specifications, which require "registros fotográficos" and anomaly records — [UTFPR thesis](https://riut.utfpr.edu.br/jspui/bitstream/1/33649/1/laudovistoriacautelarobra.pdf), [Xanxerê ETP](https://xanxere.sc.gov.br/uploads/sites/92/2025/03/ETP988383_000040_2025.pdf) (search summaries). **I could not verify that NBR 12722 itself mandates vistoria cautelar** (the norm is paywalled).
- Practitioners describe NBR 16747 as leaving methodological gaps that hinder standardisation — [IFSC](https://repositorio.ifsc.edu.br/bitstreams/1e95c85c-3eff-4980-89b2-941828fdd7ed/download) (search summary)

**Buyer pool**
- The Confea system has about 1.2 million registered professionals (engineering, agronomy, geoscience; May 2025 census) — [Confea](https://www.confea.org.br/node/232051) (search summary)
- A 2019 CREA-SC note calls civil engineering the largest Confea profession, with "mais de 300 mil" registered (search summary; exact page not opened) — [CREA-SC](https://portal.crea-sc.org.br/abenc-promove-25o-congresso-brasileiro-de-engenheiros-civis-em-florianopolis/?print=pdf)
- US analog Spectora: "over 9,000 home inspectors" (company claim via Datanyze) and about US$5.9M revenue (Latka estimate), from earlier notes — [Datanyze](https://www.datanyze.com/companies/spectora/448152301), [Latka](https://getlatka.com/companies/spectora.com)

**PT-BR demand signals (Autocomplete 2026-10-12)**
- Software seeds are thin:
  - "app vistoria cautelar" [1], "software vistoria cautelar" [1], "sistema vistoria cautelar" [1]
  - "aplicativo inspeção predial" [1], "aplicativo laudo de vistoria" [1]
  - "relatório fotográfico app" [2], including "app relatório fotográfico grátis"
  - Zero suggestions: "app inspeção predial", "software inspeção predial", "app laudo técnico", "software laudo técnico engenharia", "app para engenheiro vistoria", "app vistoria entrega de chaves", "app laudo de vistoria engenharia"
  - "howse app" [3], of which 2 are unrelated
- Template and norm seeds are rich:
  - "vistoria de recebimento de imóvel" [10]: "valor", "checklist", "modelo", "pdf", "precisa de art"
  - "laudo de vistoria de recebimento" [7]: "…de imovel pdf", "modelo de laudo…"
  - "nbr 16747" [10]: "pdf", "download", "comentada", "atualizada"
  - "autovistoria rio de janeiro" [9]: "lei", "decreto", "prefeitura"
  - "laudo autovistoria" [4]: "…predial pdf", "…rj"
  - "laudo técnico de engenharia modelo" [5]
  - "modelo laudo vistoria cautelar" [3]
  - "laudo de inspeção predial modelo" [3]: "…técnico…", "modelo proposta…"
  - "inspeção predial obrigatória" [3]: "…será obrigatória", "…é obrigatória em são paulo"
  - "vistoria entrega de chaves" [10]: consumer and local intent ("joinville", "curitiba", "valor", "curso")
  - Source: [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=vistoria%20de%20recebimento%20de%20im%C3%B3vel)

### Inferences
- **The niche is not saturated in its engineering-grade form.** The saturated part is rental and vehicle vistorias; their Play apps have 1k–100k installs. No engineering-specific laudo generator showed real traction on Play. Howse, the nearest match, is AI-positioned, has no visible Play listing and publishes no traction numbers.
- **Generic form builders are the true substitute.** Inspect App claims 10k active users and has HTML laudo templates. An engineer can build a custom laudo template in such tools, so the moat must be the norm-structured output: NBR 16747 sections, anomaly classification with GUT/urgency prioritisation, ART fields, and batch neighbour reports for cautelar.
- **Demand per professional recurs only for specialists.** Autovistoria repeats per building (≤5 years in Rio), and cautelar is per construction job. Back-of-envelope (inference): 270k Rio buildings on a 5-year cycle is about 54k laudos/year at full compliance. At the observed 11.7% compliance it is only about 6k/year, which at 20–50 laudos per professional per year means only a few hundred active Rio buyers. Nationally the pool is plausibly low thousands. That is small but enough for a solo developer at R$70–150/month.
- **Distribution without contacts is feasible but leans to free.** The rich queries are template seekers. A free "modelo de laudo NBR 16747 / vistoria cautelar / recebimento de imóvel" plus a generator upsell is the obvious play. The risk is that template seekers want free Word files.
- **This is not an AI wrapper.** A deterministic, norm-structured PDF generator with photos and anomaly tables satisfies the constraint and differentiates from Howse's AI conclusions.

### Gaps
- Howse's real traction, plus the prices of Inspeção Pro, Onlaine, Checklist Fácil and Rede Vistorias (no public prices or JS-only pages); Vistoria Online (TLS failure) and Plinto (empty shell).
- The text of NBR 12722 and NBR 16747 (paywalled), so required laudo sections are known only from secondary sources.
- Current (2024–2026) autovistoria compliance numbers for Rio. Only 2014–2015 figures were found.
- The number of engineers and architects who actually sell inspections. No registry data found.

## Finalist 3: NubeSDK-native B2B/wholesale app for Nuvemshop, and other thin Nuvemshop categories

### Takeaway
KILL. The NubeSDK deadlines are verified, but the opportunity is gone because **Nuvemshop now ships wholesale natively**. Its help pages (updated 17/08/2026) describe price tables per customer type, minimum order by value or quantity, reseller self-registration with approval and a single stock, all from the Impulso plan up. Two other "thin" categories are also native: NF-e (MEI/Simples, page updated 17/08/2026) and subscriptions (FAQ updated 02/10/2026). These categories are thin because the platform absorbed them, not because demand is unmet. I could not identify which apps were delisted on 30 Sep 2026 because the Wayback Machine was offline.

### Cited Findings
**NubeSDK enforcement (primary, verified 2026-10-12)**
- "O prazo de adoção foi adiado de 30 de agosto para 30 de setembro de 2026. 30 de setembro: apps sujeitos à obrigação que não migraram são retirados da Loja de Aplicativos. 30 de outubro: começa a desinstalação progressiva desses apps das lojas."
- "Apps que usam apenas a API ou rodam apenas dentro do Admin estão fora dessa obrigação."
- Since 5 Jun 2026, new homologation requests for script-injecting apps require NubeSDK validation.
- "O checkout já exige NubeSDK para scripts de apps."
- Private script-injecting apps are blocked systemically in the front-end.
- Source: [nuvemshop.dev – Visão geral / Prazo de adoção do NubeSDK](https://nuvemshop.dev/apps/admin/overview)
- Homologation adds only the SDK check. Already-published apps go through "re-homologação para o NubeSDK", and the docs mention a 10-business-day response window after artefacts are submitted — [nuvemshop.dev – Homologação](https://nuvemshop.dev/apps/publish/homologation/overview)

**Native wholesale already exists (primary, verified)**
- FAQ "Perguntas frequentes sobre vendas no atacado e varejo", "Última atualização: 17/08/2026":
  - "a Nuvemshop oferece um recurso nativo para criar listas de preços exclusivas para atacadistas", with "regras de pedido mínimo e descontos segmentados"
  - Tables per plan: "Impulso: 1 tabela… Escala: até 3… Next: tabelas ilimitadas. Começo e Essencial: Essa funcionalidade de atacado não está disponível"
  - "Promoções nativas, cupons e frete grátis são exclusivos do varejo"
  - "Sem login, os preços exibidos serão sempre os de varejo"
  - "Essa solução está sendo liberada progressivamente para as lojas a partir do plano Impulso"
  - Source: [Nuvemshop FAQ](https://atendimento.nuvemshop.com.br/pt_BR/varejo-e-atacado/perguntas-frequentes-sobre-vendas-no-atacado-e-varejo-na-nuvemshop)
- The marketing page lists "Tabela de preço por tipo de cliente", "Estoque único pra atacado e varejo", "Compra mínima automática… valor ou… quantidade mínima" and "Auto-cadastro de clientes atacado… você aprova". Discounts can be set "por categoria ou produto específico" — [nuvemshop.com.br/vender/atacado](https://www.nuvemshop.com.br/vender/atacado)
- The earlier "Blended" beta (updated 05/06/2025) allowed only one table and "Todos os produtos". The 2026 pages show it has since expanded — [Loja Blended](https://atendimento.nuvemshop.com.br/pt_BR/b2b/como-configurar-minha-loja-blended-na-nuvemshop)

**Other "thin" categories are native too**
- NF-e ("Última atualização: 17/08/2026"):
  - Native emission for MEI and Simples Nacional; requires a digital certificate
  - Not available for other regimes, Multi-CD, exports, mixed digital/physical orders or return notes
  - First 5 notes free; then per note R$1.49 Começo, R$0.99 Essencial, R$0.49 Impulso, R$0.25 Escala, R$0.10 Next
  - Source: [Nuvemshop – emissão de nota fiscal](https://atendimento.nuvemshop.com.br/pt_BR/minhas-vendas/como-funciona-a-emissao-de-nota-fiscal-pelo-painel-da-nuvemshop)
- Tiny Faturador is free up to 30 notes/month, then from R$29/month (search summary) — [App page](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/tiny-faturador)
- Subscriptions ("Última atualização: 02/10/2026"):
  - "A funcionalidade é gratuita"
  - Credit card via Nuvem Pago only; one product and one frequency per subscription; lower plans get a 7-day trial
  - Source: [Nuvemshop – assinaturas FAQ](https://atendimento.nuvemshop.com.br/pt_BR/venda-por-assinatura/perguntas-frequentes-sobre-vendas-por-assinatura)

**App Store census (my crawl of all 10 categories with pagination, 2026-10-12)**
- 643 unique apps; median 3 reviews; 187 with 0 reviews; 53 with ≥100 reviews. The earlier researcher counted 647 the same day. Source: category pages such as [Recursos extras](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/recursos-extras)
- Wholesale/B2B-related apps:
  - Compre por Grade Pro – Huapps: 4.9 (10), "Compras no app"; R$59.90/month per earlier notes. Grid ordering of all variations plus back-in-stock alerts; reviews dated Jan–Mar 2026 — [App page](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/compra-por-grade-pro)
  - Solicitar Orçamento (Abejita): 5.0 (2), free, a B2B quote form
  - Backchannel: 5.0 (3), sourcing of wholesale stock (not B2B pricing)
  - "Tabela de Preços" (Abejita): 5.0 (5), a plan-comparison widget (not wholesale)
  - "Preços Parcelas e Promoções": 4.9 (170), price and instalment display (not wholesale)
- Search and filters: SmartHint 4.9 (26), HintUP 4.5 (18), Busca Inteligente 5.0 (4), My Brands 5.0 (1)
- Gift cards: Gifty 4.8 (40) is the only dedicated app found
- NF-e/ERP: Bling 4.6 (469), Olist 3.7 (163), ERP Laserchip 5.0 (23), Notazz 4.8 (19), Omie 3.8 (12), plus about 15 ERPs with ≤8 reviews
- Subscriptions: no dedicated subscription-billing app in the BR store. Smartbis (334) is cashback and Cliqenvio is WhatsApp.

**Demand and complaints**
- Autocomplete:
  - "nuvemshop atacado" [3]: "…e varejo", "vender atacado nuvemshop"
  - "nuvemshop b2b" [2]: includes "nuvemshop tem b2b"
  - "nuvemshop pedido minimo" [1]
  - "nuvemshop tabela de preço" [1]
  - Zero suggestions: "nuvemshop app atacado", "nuvemshop preço atacado", "nuvemshop compra por grade", "nuvemshop catalogo atacado", "nuvemshop esconder preço"
  - "nuvemshop nota fiscal" [7]: includes "…tem emissor de nota fiscal"
  - "nuvemshop gift card" [2], "nuvemshop vale presente" [1]
  - Source: [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=nuvemshop%20atacado)
- Reclame Aqui: the search found no complaints about missing wholesale features. The complaints that surfaced concern a wholesale store's delivery and Nuvem Pago account blocks (search summary) — [Reclame Aqui – Nuvemshop](https://www.reclameaqui.com.br/empresa/nuvem-shop/lista-reclamacoes/)

### Inferences
- **The platform risk has already materialised.** Nuvemshop shipped wholesale, NF-e and subscriptions natively in 2025–2026, so an app in these categories competes with a free first-party feature and with continued roadmap encroachment.
- **Residual wholesale gaps are narrow and could be closed by Nuvemshop at any time.** They are:
  - wholesale for Começo/Essencial-plan stores
  - promotions and coupons in wholesale
  - quantity-tiered price breaks (not mentioned in the native docs)
  - grid/variation-matrix ordering, already served by Huapps
  - hiding prices or catalogue mode for anonymous visitors
- **NubeSDK replacement demand is unproven.** Without a pre-delisting list I cannot name a single popular delisted app. API-only and Admin-only apps (ERPs, analytics) are exempt, which shrinks the forced-replacement pool to storefront widgets.
- Gift cards (Gifty, 40 reviews) and search (24–48 reviews across 3–4 apps) show some payment, but their volumes are tiny and both are storefront-script categories where NubeSDK coverage matters.

### Gaps
- Which apps were delisted on 30 Sep 2026. The Wayback Machine returned "Temporarily Offline", then DNS failure for web.archive.org. A pre-October snapshot of the category pages would settle this.
- Install counts. The Nuvemshop store shows reviews only.
- Whether native wholesale supports quantity tiers or per-product minimums, which needs a merchant account to check.

## Finalist 4: Pest-control and water-tank-cleaning certificate tool with expiry reminders

### Takeaway
KILL. The premise of "one R$350/month competitor" is false. I found at least six dedicated Brazilian pest-control systems with public prices from R$69 to R$497/month, plus generic tools. Several already do exactly the proposed product: certificates for dedetização and limpeza de reservatórios, QR validation and expiry/warranty reminders. They include a vendor claiming 1,000+ companies and one in market since 2011. Regulation is real (RDC 622/2022 art. 19, 11 mandatory fields), and the buyer pool is about 34k mostly micro firms. The niche is saturated.

### Cited Findings
**Competitor census (accessed 2026-10-12 unless noted)**

| Tool | Price | Relevant features | Traction (self-reported) | Source |
|---|---|---|---|---|
| Gestor de Dedetização | Price not in today's static HTML (#precos anchor); R$350/month per earlier notes | Certificates/laudos for dedetização and **limpeza de reservatórios** with before/during/after photos; "alertas de vencimento"; QR-code validator; client area; contracts; stock; fleet | none | [Gestor de Dedetização](https://www.gestordedetizacao.com.br/) |
| Pragfy | R$90/month (≤2 users), R$150 (≤5), higher tiers; first month free | Built for pest control; guarantee and certificate expiry tracking; online forms with client signature | "Desde 2011", "Mais de 15 anos no mercado" | [Pragfy](https://pragfy.com.br/) |
| PestFácil (BENU ERP partner) | "a partir de R$ 69" (search summary) | OSs and certificates; RJ/ES/PR state rules; expired-guarantee alerts with automatic e-mails; caixa d'água services; offline Android app | "usado por mais de 1000 empresas", "mais de 20 milhões de OSs" | [PestFácil](https://www.pestfacil.com/), [BENU](https://benuerp.com/pestfacil-sistema-pequenas-dedetizadoras/) |
| VEL Sistema | No price | "100% voltado para Controladoras": mobile app with QR code, CIP monitoring reports, contracts, boleto/NF | none | [VEL](https://velsistema.com.br/) |
| DedetizaGestor | R$117 / R$247 / R$497 per month, or R$197 "Profissional" (conflicting, search summary) | CRM with AI for pest control; 30-day trial | none | [DedetizaGestor](https://dedetizagestor.com.br/) |
| Sistema iPragas | Not read (empty response) | Management system for dedetizadoras (search summary) | none | [iPragas](https://sistemaipragas.com.br/) |
| CPT Softwares Dedetizadora | Licence (search summary) | Claims compliance with RDC 52/2009 and 59/2010 | none | [CPT](https://dedetizadora.cptsoftwares.com.br/) |
| Simples Agenda | From R$39.90/month | Generic scheduling with WhatsApp and a dedetizadora landing page | "Mais de 3.900 negócios" (all segments) | [Simples Agenda](https://www.simplesagenda.com.br/site/sistema-para-dedetizadora) |
| Produttivo | No public price | Generic FSM with a "checklist de dedetização" template | none | [Produttivo](https://www.produttivo.com.br/modelo/checklist-dedetizacao/) |

**Regulation (primary text)**
- RDC nº 622 of 9 Mar 2022 (DOU nº 51, 16 Mar 2022) is in force since 1 Apr 2022. It revoked RDC 52/2009 and RDC 20/2010.
- Art. 19 requires a "comprovante de execução de serviço" with at least these fields:
  1. client name
  2. property address
  3. target pest(s)
  4. date of service
  5. "prazo de assistência técnica, escrito por extenso… por praga(s) alvo"
  6. chemical group(s) of the products
  7. product name and concentration
  8. guidance
  9. technical manager with council registration
  10. CIT phone number
  11. company identification with "números das licenças sanitária e ambiental com seus respectivos prazos de validade"
- Art. 20 requires posters in collective, commercial or service buildings. Art. 21 makes only private-company invoices valid. Art. 23 sets penalties under Lei 6.437/1977.
- Source: [RDC 622/2022 (VISA Jundiaí copy)](https://visa.jundiai.sp.gov.br/wp-content/uploads/2023/03/RDC_622_2022-controle-de-pragas-produtos.pdf)
- The RDC text contains no mention of "reservatório" or "caixa" (grep of the full text). Water-tank cleaning is driven by municipal and health rules:
  - Florianópolis requires cleaning and disinfection every six months — [CondomínioSC](https://condominiosc.com.br/jornal-dos-condominios/manutencao/1632-limpeza-da-caixa-d-agua-e-manutencao-obrigatoria) (search summary)
  - A São Paulo city technical annex says reservoirs should be cleaned "no mínimo, semestralmente" — [Prefeitura SP](https://www.prefeitura.sp.gov.br/cidade/secretarias/upload/Anexo%20I%20-%20Especifica%C3%A7%C3%B5es%20t%C3%A9cnicas.pdf) (search summary)
  - I did not verify that Portaria GM/MS 888/2021 sets a cleaning periodicity.

**Number of companies**
- Sebrae PR "Sebrae em dados" (10 Jan 2023):
  - 33,782 companies with CNAE 8122-2/00 as main activity, plus 1,218 branches, present in 3,276 municipalities
  - São Paulo 2,958, Rio de Janeiro 1,400, Brasília 843
  - ME 73.7%, MEI 11.02%, EPP 10.01%
  - 1,154 opened in 2022 and 942 closed; "taxa de mortalidade" 28.03%
  - The sector moved "mais de R$ 1 bilhão" in 2016 (citing the industry association)
  - Source: [Sebrae PR](https://sebraepr.com.br/comunidade/artigo/sebrae-em-dados-servicos-de-dedetizacao-2)
- Contradiction on MEIs: a contabilidade.com article says this CNAE is not allowed for MEI — [contabilidade.com](https://contabilidade.com/blog/cnae-8122200-imunizacao-e-controle-de-pragas-urbanas-simples-nacional-tributacao-e-abertura-de-empresa/) (search summary). An older Belo Horizonte city-council text estimates about 6,000 specialised firms — [CMBH](https://www.cmbh.mg.gov.br/printpdf/24086) (search summary)

**Demand signals (Autocomplete 2026-10-12)**
- "certificado de dedetização" [10]: "pdf", "modelo", "word", "em pdf grátis", "anvisa", "validade", "online", "veicular"
- "certificado de limpeza de caixa d'água" [6]: "pdf", "modelo", "como emitir", "quem pode emitir"
- "sistema para dedetizadora" [4]: "grátis", "sistema de gestão para dedetizadora"
- "software para dedetizadora" [2]: "gratuito"
- "rdc 622" [10]; "dedetização validade" [3]; "ordem de serviço dedetização" [2]; "sistema para limpeza de caixa d água" [1]
- "como abrir uma dedetizadora" [4]
- Zero suggestions: "app para dedetizadora", "comprovante de execução de serviço dedetização"
- Source: [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=certificado%20de%20dedetiza%C3%A7%C3%A3o)
- Google Play searches for "dedetização", "dedetizadora" and "controle de pragas" return games and cleaner apps, with no B2B pest-control app in the top 20 — [Play search](https://play.google.com/store/search?q=dedetizadora&c=apps&hl=pt_BR&gl=BR)

### Inferences
- **Willingness to pay is proven, and that is exactly why the niche is crowded.** Six or more paid vendors span R$69–497/month, including a 15-year-old vendor and one claiming 1,000+ customers.
- **A new entrant cannot win on price.** R$69–90 tiers already exist, and Simples Agenda covers basic scheduling at R$39.90.
- **The proposed differentiators are already table stakes.** Certificates with RDC 622 fields, water-tank certificates, QR validation and expiry reminders all ship in Gestor de Dedetização, PestFácil and Pragfy.
- **Buyer purchasing power is low.** 84% are micro/small firms and the closure rate is 28%. Autocomplete repeatedly surfaces "grátis/gratuito".
- **The previous research undercounted.** Its "one competitor" finding probably came from a single search result; a wider search surfaces many.

### Gaps
- Verified current prices for Gestor de Dedetização (JS-rendered #precos), iPragas, CPT and DedetizaGestor (conflicting figures).
- A current 2025–2026 company count. The Sebrae figure is from January 2023; Receita CNPJ open data was not processed.
- Municipal water-tank cleaning mandates beyond Florianópolis and São Paulo.

## Scores and ranked verdicts

### Takeaway
Only the field-inspection report generator survives, and only conditionally. Receita Saúde is killed by a free official template and suites that bundle the export. Nuvemshop wholesale is killed by native platform features. Pest-control certificates are killed by saturation.

### Cited Findings
Scores (1 = worst, 5 = best) from the evidence above. Columns: WTP = willingness-to-pay evidence; Sat. = low saturation; Power = buyer purchasing power; Dist. = distribution without contacts; Build = buildability; Speed = speed to first revenue; Risk = low risk.

| Finalist | WTP | Sat. | Power | Dist. | Build | Speed | Risk | Total /35 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 2. Field-inspection report generator | 3 (Howse R$70/mo; rental apps R$60–300; inspection fees high per earlier notes) | 3 (engineering-grade tools few and small; rental crowded; generic form builders substitute) | 4 (engineers and firms selling laudos) | 3 (template SEO: "modelo/pdf" queries [3–10]; software queries ~0) | 3 (offline photo capture, PDF layout, batch neighbour reports) | 2 (needs SEO time; template seekers lean to free) | 3 (weak law enforcement: 32/41 municipal laws unregulated; Rio 11.7% compliance in 2015) | **21** | **CONDITIONAL** |
| 4. Pest-control / caixa d'água certificates | 4 (6+ paid vendors, R$69–497) | 1 (Gestor de Dedetização, Pragfy, PestFácil, VEL, iPragas, CPT, DedetizaGestor, Simples Agenda, Produttivo) | 2 (84% micro/small; "grátis" queries) | 3 ("sistema para dedetizadora" [4]) | 4 | 2 | 3 | **19** | **KILL** (saturated) |
| 3. Nuvemshop NubeSDK wholesale (and NF-e, subscriptions) | 2 (Grade Pro 10 reviews; Gifty 40) | 2 (thin apps but **native platform features**) | 3 | 4 (App Store is a built-in channel) | 3 (NubeSDK + re-homologation) | 3 | 1 (Nuvemshop shipped wholesale, NF-e and subscriptions natively in 2025–2026) | **18** | **KILL** |
| 1. Receita Saúde batch tool | 2 (only bundled: PsicoPront R$79/mo, Psicontrole R$97/90d, Corpora Pro) | 2 (free official template, free YouTube template, 4+ suites, paid spreadsheet) | 3 | 1 (tool-seeking queries return 0–1 suggestions) | 5 (16-field CSV) | 2 | 2 (LGPD health data; free official route) | **17** | **KILL** |

Ranking:
1. **Field-inspection report generator: CONDITIONAL.** Conditions to turn it into GO:
   - Publish 3 free norm-structured templates (NBR 16747 inspeção predial / autovistoria RJ, vistoria cautelar with IBAPE structure, vistoria de recebimento de imóvel novo). Measure organic and R$200–300 ads traffic and template-to-signup conversion before building the full app.
   - Pre-sell 5–10 annual plans (around R$600–1,200/yr) to engineers reached via the template funnel or cold LinkedIn/Instagram outreach.
   - Differentiate on deterministic, norm-structured output (anomaly classification, urgency prioritisation, ART fields, batch neighbour reports), not on AI.
   - Kill trigger: if fewer than 5 pre-sales come in after about 60 days, or template visitors refuse paid upgrades.
2. **Pest-control certificates: KILL.** WTP is real but the space is saturated. Revisit only with a sharply different wedge, for example a free compliance-certificate validator for síndicos that sells leads to dedetizadoras. That is a different product and was not researched here.
3. **Nuvemshop wholesale/NF-e/subscriptions: KILL.** Native features ship from the Impulso plan up. A residual angle (wholesale on the Começo/Essencial plans, tiered quantity pricing, catalogue mode) is narrow and exposed to the same platform risk.
4. **Receita Saúde batch tool: KILL** as a paid product. It is at most a free client-side generator used as an SEO lead magnet.

### Inferences
- Across all four finalists, regulation-driven niches in Brazil attract either the government itself (free official template), the platform owner (Nuvemshop native features) or many small vertical SaaS vendors (pest control). The niche that survives is the one where output quality is professional and norm-bound, and where the obligation is fragmented across municipalities, which large players ignore.
- The client's R$700 budget fits a template-SEO-first validation for finalist 2 (domain, hosting, R$200–300 of ads). It does not fit a marketplace bet that depends on Nuvemshop's roadmap.

### Gaps
- None of the scores are based on interviews; all come from desk evidence. Absolute search volumes and CPCs were unavailable.
- The list of apps Nuvemshop delisted on 30 Sep 2026 (Wayback offline) could still reveal a specific storefront widget worth rebuilding. That would be a different idea from wholesale.
