---
tags:
  - hub
  - armadilha
atualizado: 2026-10-12
---

# Armadilhas e ideias mortas

Voltar para [[00 Início]] · [[Ranking]].

> [!abstract] O mapa da morte
> As ideias morrem por motivos que se repetem nas três rodadas:
> - **o governo entrega a ferramenta de graça** ([[Padrão - governo entrega de graça]]);
> - **a plataforma absorve o recurso** ([[Padrão - plataforma absorve o recurso]]);
> - **dezenas de pequenos SaaS chegam antes** ([[Padrão - saturação]]), e em 2026 isso acontece em semanas, com apps feitos com IA ([[Padrão - enxurrada de micro-SaaS feito com IA]]);
> - **não há como receber**: o Paddle proíbe a categoria ou a plataforma exige CNPJ ([[Padrão - pagamento e CNPJ bloqueiam rotas]]);
> - **a busca brasileira quer o modelo grátis**, não a ferramenta ([[Padrão - busca por grátis e modelo]]);
> - **a aritmética de G8 não fecha**: uma taxa fixa de terceiros (os US$ 8,46 do USPS nas cartas) ou um universo pequeno (~2,2 mil examinandos do CBLE por ano, ~4,8 mil novos corretores da SUSEP) mata o que a demanda salvaria ([[Validação condicionais e novos focos]]).
>
> E uma lição de método: **a pesquisa de mesa não aprova G1 e G2 juntos** ([[Padrão - pesquisa de mesa não aprova G1 e G2]]). As portas estão em [[Portões de aprovação]].
>
> Duas armadilhas transversais têm nota própria: [[IA no centro do produto]] e [[Ideias inviáveis do thread]].

## 1. Mortas nas rodadas 2 e 3 (com nota própria)

| Ideia | Motivo em uma linha | Evidência decisiva |
|---|---|---|
| [[Cartas registradas online (EUA e Reino Unido)]] | G8: margem estrutural. A LetterStream resolveu o bloqueio contratual, mas a taxa do USPS é piso para todos | US$ 5,55 + US$ 2,91 por carta ([USPS Notice 123](https://pe.usps.com/text/dmm300/Notice123.htm)); white-label da LetterStream ([API](https://www.letterstream.com/api)); seriam 470–800 cartas/mês, 1,8–3,4× o melhor novato ([TrustMRR PostalForm](https://trustmrr.com/startup/postal-form)) |
| [[App Forge de Gantt para Jira]] | G2 e G8: o nicho estreito foi tentado por outros e não funcionou | Novatos com 0–29 instalações ([API baseline](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=baseline&limit=10&withVersion=true)); Katabarwa com 10+ apps em 0–2 ([API Katabarwa](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=Katabarwa&limit=10&withVersion=true)) |
| [[Feed de transportadoras recém-registradas (FMCSA)]] | G2: saturado em 2026 | 8+ SaaS e 67 atores no Apify sobre o mesmo censo; o TruckerDB tem 20 assinantes ([Apify](https://api.apify.com/v2/store?search=fmcsa&limit=40); [TrustMRR](https://trustmrr.com/startup/truckerdb)) |
| [[Simulado do exame de corretor de seguros (SUSEP)]] | G8: universo pequeno (morta como aposta; teste opcional de caixa) | ~4,6–4,9 mil novos corretores PF por ano, todas as rotas ([painel SUSEP](https://app.powerbi.com/view?r=eyJrIjoiNWM3OWIyNmQtNWRlNi00Njc3LTllYTctYTkwNjdlNTllNTdkIiwidCI6ImFlZmVkMDQ0LTg4ODctNDI1NS1hNWU5LThkNzgzOTc3MmI4OSJ9)) |

## 2. Mortas nas rodadas 2 e 3 (sem nota própria)

### Rodada 2: plataformas brasileiras emergentes, de [[brazil_emerging_platforms]]
Barreira comum: TikTok, Shopee e Temu exigem CNPJ para desenvolvedor ([[Padrão - pagamento e CNPJ bloqueiam rotas]]).

| Ideia | Motivo | Evidência |
|---|---|---|
| NFS-e em lote para a Comissão Extra da Shopee (C1, 18) | G2: a janela abriu e fechou no mesmo trimestre | Conta Azul em 24/07 e ≥ 6 ofertas em ~10 semanas ([Conta Azul](https://contaazul.com/blog/como-emitir-nota-fiscal-afiliado-shopee-na-conta-azul/)); reforça [[Emissor de NFS-e Nacional]] |
| Lucro real e conciliação de repasses no TikTok Shop (C2, 20) | G2: ~20 apps, planos grátis e ERPs | [Loja TikTok BR](https://seller-br.tiktok.com/appstore/br/search?category_id=1&page=1) |
| CRM de criadores e amostras do TikTok Shop (C3, 18) | G2: 20 apps, muitos com IA | Euka US$ 199–599 ([Euka](https://www.euka.ai/pricing)); TF Collab, Cruva, Crevideo |
| NF-e de amostra grátis no TikTok Shop (C4, 15) | G2 contra incumbentes grátis; risco fiscal | Bling, UpSeller (grátis), Tray e Olist já têm o selo ([loja BR](https://seller-br.tiktok.com/appstore/br/)) |
| Auditor de faixas de taxa Shopee/TikTok/ML (C6, 20) | G1 e G4: calculadoras grátis; recurso de apps existentes | [Ecommerce na Prática](https://ecommercenapratica.com/blog/taxa-shopee/) |
| RPA em lote para afiliados PF da Shopee (C7, 13) | G5 e G7: território de folha e eSocial, com responsabilidade de INSS e IRRF | [Fórum Contábeis](https://www.contabeis.com.br/forum/Tributos%20Federais/415123/rpa-em-lote-para-afiliado-pf-comissao-extra-shopee-periodicidade-certa-no-esocial-s-1200-s-2500/) |
| Monitor de custo da API do WhatsApp (C8, 16) | G1 e G2: nenhum produto pago avulso; painéis dos BSPs e do WhatsApp Manager | [Meta pricing](https://developers.facebook.com/docs/whatsapp/pricing/) |
| Conectores para Temu, Shein e Kwai Shop (C9, 13) | G4 e G5: Temu só aceita desenvolvedores de ERP/OMS; hubs já dentro | [Temu partner](https://partner.temu.com/documentation?menu_code=52ef88bdef1d4527b15f6d303b173e48) |
| Add-ons para Hotmart, Kiwify e Eduzz (C10, 18) | A plataforma absorve: integrações grátis, recuperação e agente nativos | [Hotmart integrações](https://hotmart.com/pt-br/integracoes) |

### Rodada 2: cartas, de [[certified_mail_validation]]
- **Cartas de contestação de relatório de crédito:** KILL por CROA e pelas restrições do Stripe e do PayPal a reparo de crédito ([Stripe restricted](https://stripe.com/legal/restricted-businesses)).

### Rodada 2: preparatórios de exame, de [[niche_exam_prep]]
| Exame | Motivo |
|---|---|
| Aplicador de pesticidas (EUA) | 50+ planos estaduais; melhor app com 1 mil+ instalações; comprador de salário baixo |
| NHIE, inspetor residencial (EUA) | Conteúdo proprietário (exige especialista); teste grátis da InterNACHI |
| EPA 608 (EUA) | "Free" domina; 30+ apps |
| Testador de backflow e Certified Pool Operator (EUA) | A credencial é vendida como curso ou prova prática |
| Notário estadual (EUA) | 28 apps no Play; provas de baixo risco |
| Ajustador de seguros (EUA) | A marca ExamFX aparece no autocomplete; incumbentes de pré-licenciamento |
| ASE e NATE (EUA) | Saturação de apps; ASE a US$ 62 por prova |
| Patent Bar (USPTO) | Wysebridge entrincheirada, com plano grátis e 6.000+ alunos ([Wysebridge](https://www.wysebridge.com/patent-bar-exam-annual-reports)) |
| Revalida | Medway, MedCof, Estratégia MED e Descomplica |
| ANBIMA (CPA / C-Pro) e Ancord | Reforma não abriu lacuna: produtos C-Pro R no Hotmart e TopInvest atualizada em meses |
| Exame de Ordem (OAB) | G2 |
| Títulos de especialista médico | Exige especialista; a Medway vende "Prova de Título" |

### Rodada 2: Portugal, Espanha e América Latina, de [[portuguese_spanish_arbitrage]]
| Ideia | Motivo | Evidência |
|---|---|---|
| Registro de hóspedes do alojamento local (SIBA) e taxa turística | G2 e G8: incumbente local a ~€ 4,50 e player financiado a € 3,95 | [Hostkit](https://hostkit.pt/planos/); [Chekin](https://chekin.com/en/pricing/) |
| Companheiro de recibos verdes | G1 fraco, G4: Artur faz US$ 30 de MRR a € 6,99; simuladores oficiais | [[portuguese_spanish_arbitrage]], 2.2 |
| Livro de Reclamações eletrônico | O Estado entrega (livroreclamacoes.pt) | [[Padrão - governo entrega de graça]] |
| RGPD para PMEs portuguesas | Sem evidência nova; cookies já saturados | [[Consentimento de cookies e GPC]] |
| Registros HACCP digitais (PT/ES) | G1: nenhuma receita de software; apps com 0 avaliações; demanda por PDF | [[portuguese_spanish_arbitrage]], 2.6 |
| Ferramenta para pequeno senhorio (PT) | Modelos e portal grátis da AT; Gesar a € 40/mês para profissionais | [[portuguese_spanish_arbitrage]], 2.8 |
| Lacunas do IRS automático | A AT pré-preenche e tem simulador | [[portuguese_spanish_arbitrage]], 2.9 |
| Plugins WooCommerce para Portugal | Um incumbente (Naked Cat); o maior plugin só português tem 7 mil instalações | [[portuguese_spanish_arbitrage]], 2.10 |
| Verifactu, CCSE e SES.Hospedajes (Espanha) | Faturação excluída; saturado | [[Conversor de e-invoicing]] |
| Compliance na América Latina (Ley Karin, NOM-035, SG-SST) | Oferta grátis de órgãos quase oficiais; intenção grátis | [[portuguese_spanish_arbitrage]], seção 4 |
| Coletor de avaliações do Google para PMEs portuguesas | G7: o Paddle proíbe ferramentas automáticas de avaliação | [Paddle AUP](https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle) |

### Rodada 2: dados públicos, de [[public_records_data]]
| Ideia | Motivo | Evidência |
|---|---|---|
| Vigilância de marcas no INPI | G2 e G8: incumbente igual, mais barato e feito com SEO | MonitoraMarca R$ 19,90–149 ([MonitoraMarca](https://monitoramarca.com.br/)) |
| Alertas de licitação do PNCP por segmento | G2 e G8; o governo avisa MEIs de graça | Alerta Licitação R$ 44,90 com 6.441 portais ([Alerta Licitação](https://alertalicitacao.com.br/)); Contrata+Brasil ([Jornal Contábil](https://jornalcontabil.com.br/noticia/contratabrasil-amplia-participacao-do-mei-com-34-novas-ocupacoes/)) |
| Listas de CNPJs novos | G2, G4 e G7 (LGPD) | Speedio R$ 719+, 194 atores no Apify, "grátis" no topo do autocomplete |
| Agregador de leilões e imóveis da Caixa | G2 e G5 (CAPTCHA da Caixa) | Mapa do Leilão com 44.180 usuários a R$ 74,90 |
| Monitoramento do Querido Diário | G5: cobertura de 510 dos 5.570 municípios | [[public_records_data]] |
| Alertas de Anatel, ANVISA e CVM | G1 e G4: consultas oficiais grátis | [[public_records_data]] |
| Leads de inventário (probate), despejo e divórcio (EUA) | G5 (acesso condado a condado), G7 (FCRA no despejo), G4 | 15 U.S.C. §1681a; b2bsaas levou 16 anos |
| Pré-execução, ônus fiscais, UCC e alvarás de obra (EUA) | G2: PropStream US$ 99/mês; 199 atores (pré-execução) e 578 (alvarás) no Apify | [Apify alvarás](https://api.apify.com/v2/store?search=building%20permit&limit=40) |
| Novas LLCs, SAM.gov e registros da FAA (EUA) | G2 e G5: 276 e 204 atores no Apify; contatos do SAM restritos; FAA sem intenção de lead | [[public_records_data]] |

### Rodada 2: pedidos não atendidos da Atlassian e de outros, de [[unmet_feature_requests]]
| Ideia | Motivo |
|---|---|
| Backlinks de entrada no Confluence | Universo e teto pequenos; um novato já entrou (Linking for Confluence com 1.218 instalações) |
| Campos somente leitura, SLA e responsável no portal do JSM | Novatos falhando no mesmo nicho (Deviniti com 5.301 instalações) |
| Arquivar componentes do Jira | Nenhuma prova de que alguém pague só por isso |
| Valores padrão para campos do sistema | Incumbente grátis (Big Fig Tree, 2.445 instalações) |
| Funções JQL de sprint | Lotado; novatos com 15–186 instalações |
| Notificações personalizadas no Jira/JSM | Exige serviço de e-mail fora do Forge; Email This Issue com 5.548 instalações |
| Sync de calendário do Asana/ClickUp, auto-refresh do Zendesk | Plataforma absorvendo (o ClickUp está construindo) ou sem cobrança no marketplace |

### Rodada 3: exames, de [[exam_prep_deep]]
| Exame | Motivo |
|---|---|
| Despachante aduaneiro brasileiro (RFB/COANA 2026) | Taxa de R$ 80, só para ajudantes com 2+ anos, inscrições encerradas ([RFB](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/setembro/publicado-edital-do-exame-de-qualificacao-tecnica-para-despachante-aduaneiro-2026/1-edital-de-abertura-e-inscricoes-coana-rfb-2026-legalle-concursos.pdf)) |
| CFC EQT (auditor CNAI, perito contábil) | 730 aprovados no QTG e 75 em perícia em 2025.2 ([CFC](https://cfc.org.br/wp-content/uploads/2026/01/cfc-eqt-2025.2-resultado-final-de-aprovados_09.01.2026.pdf)) |
| Certificação do Banco Central | Só o módulo EQT-BCB, com 7 aprovados em 2025.2 |
| ABNT e INMETRO | Nenhum exame individual de massa identificado (não verificado) |
| NMLS SAFE MLO (EUA) | Saturado; o curso obrigatório de 20 h embute o preparatório |
| FAA A&P (EUA) | Intenção "prep free" |
| AWS CWI e NCCCO (EUA) | Conteúdo depende de normas com direito autoral ou prova prática |
| Enrolled Agent (EUA) | Saturado (não reverificado) |

### Rodada 3: documentos forçados por norma, de [[brazil_regulated_documents]]
| Ideia | Motivo | Evidência |
|---|---|---|
| Controle de vencimento de AVCB e alvarás | G1 e G4: o mesmo modo de falha do [[Calendário de conformidade para síndicos]] | Contadores recusam ou já têm alerta ([Fórum Contábeis](https://www.contabeis.com.br/forum/Legaliza%C3%A7%C3%A3o%20de%20Empresas/415115/como-voces-controlam-vencimento-de-alvara-avcb-de-varios-clientes-ao-mesmo-tempo/)) |
| Curso de manipulador de alimentos ou registro de treinamentos | G1, G2 e G4: a RDC 216 exige curso só do responsável; intenção "gratuito" | [RDC 216](https://bvsms.saude.gov.br/bvs/saudelegis/anvisa/2004/res0216_15_09_2004.html); [Unieducar grátis](https://unieducar.org.br/catalogo/curso-gratis/boas-praticas-em-servicos-de-alimentacao-descomplicando-a-manipulacao-de) |
| Visualizador de .p7s para o Brasil | G1 e G8: o Validar do ITI é gratuito | [ITI cartilha](https://h-validar.iti.gov.br/Docs/cartilha-de-uso.pdf) |
| Análogo do BasinCheck (auditorias de óleo e gás) | Venda enterprise puxada pela Petrobras; exige contatos (inferência) | [[brazil_regulated_documents]], Q6 |
| Análogos de Promatic, easyMovingPermits e LegalOne | Serviço ou despachante, não software | [[brazil_regulated_documents]], Q5 |

### Rodada 3: recém-chegados do TrustMRR mapeados para Brasil e Portugal, de [[trustmrr_br_pt_mapping]]
Dos 267 produtos, 64 eram anônimos e 191 morreram por outros motivos. Os principais:

| Ideia | Motivo | Evidência |
|---|---|---|
| Gerador de carimbo CNPJ e profissional | G2 e G8: geradores grátis em português; risco de atestado falso | [Hanko Maker](https://hankomaker.com/pt-br/carimbo-digital/); [Sealgenerator](https://www.sealgenerator.com/pt) |
| Agregador de leilões judiciais e fiscais em Portugal | G2: 4–5 agregadores em 2026, um grátis com alertas | [Martelo](https://martelo.pt/); [Licito](https://licito.pt/) |
| Multicálculo para corretores de plano de saúde (análogo do QuoteDeck) | Saturado | Agger R$ 79/licença ([Agger](https://agger.com.br/produtos/painel-do-corretor/)); Simulador Online a partir de R$ 30 |
| Lista de empresas abertas no Brasil (análogo do TruckerDB) | "Grátis" no topo da busca | [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=lista%20de%20empresas%20abertas) |
| QR code de avaliação no Google (análogo do MyFrank) | Intenção "gerar grátis" | [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=qr%20code%20avalia%C3%A7%C3%A3o%20google) |
| Foto 3x4 online (análogo do Passport Photo Ready) | "Grátis"; remoção de fundo por IA no centro | [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=foto%203x4%20online) |
| Reserva de voo para visto (análogo do Safeonward) | Só 2 sugestões; precisa de backend de reservas | [[trustmrr_br_pt_mapping]] |
| Passo o ponto / trespasse (análogo do Attivita24) | Território de OLX e idealista, grátis | [autocomplete PT](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-PT&gl=pt&q=trespasse) |
| Autorização de mudança (análogo do easyMovingPermits) | Municipal e com placas físicas | [[trustmrr_br_pt_mapping]] |
| Regras de drone (análogo do DrohnenAtlas) | Sistemas oficiais gratuitos da ANAC e do DECEA | [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=drone%20anac) |
| Leilões de imóveis no Brasil (análogo do LandBankSearch) | Dominado pela Caixa e pelos bancos | [autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=leil%C3%A3o%20de%20im%C3%B3veis) |

## 3. Mortas na rodada final da rodada 1

| Ideia | Motivo em uma linha | Evidência decisiva |
|---|---|---|
| [[Recibos em lote do Receita Saúde]] | O governo entrega o modelo de graça e as suítes já exportam | Modelo CSV oficial com validador no e-CAC ([ZIP Receita](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/documentos-tecnicos/escrituracao-do-carne-leao/escrituracao-carne-leao.zip)); PsicoPront inclui a exportação a R$ 79/mês ([PsicoPront](https://psicopront.com.br/recursos)); Corpora lê o retorno desde abril de 2026 |
| [[Atacado e B2B para Nuvemshop (NubeSDK)]] | A plataforma lançou o recurso | Atacado nativo a partir do plano Impulso, além de NF-e e assinaturas nativas ([Nuvemshop FAQ](https://atendimento.nuvemshop.com.br/pt_BR/varejo-e-atacado/perguntas-frequentes-sobre-vendas-no-atacado-e-varejo-na-nuvemshop)) |
| [[Certificados de dedetização e caixa d'água]] | Saturado | Seis ou mais sistemas de R$ 69–497/mês; Pragfy "desde 2011"; PestFácil "mais de 1000 empresas" ([Pragfy](https://pragfy.com.br/); [PestFácil](https://www.pestfacil.com/)) |
| [[Botão de desistência da UE fora do Shopify]] | Lacuna fechada; o prazo passou em 19/06/2026 | 68 plugins WooCommerce de 2026 ([WP API](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[search]=withdrawal%20button&request[per_page]=50)); Shopware no core desde a 6.7.9.0 ([Xictron](https://www.xictron.com/de/blog/widerrufsbutton-umsetzung-shopware-juni-2026/)); a disposição a pagar ficou no Shopify, com 2.317 avaliações no app líder ([Shopify](https://apps.shopify.com/eu-widerrufsbutton)) |
| [[Sync Google Sheets e Google Calendar]] | Saturado e pagamento baixo | 15+ add-ons, alternativas de 4,5–4,8★ presas em 25 mil instalações e scripts grátis; €5/mês sem receita verificada ([Workspace](https://workspace.google.com/marketplace/search/sheets%20to%20calendar); [Sheets2GCal](https://www.sheets2gcal.com/)) |

## 4. Candidatas descartadas nas rodadas exploratórias da rodada 1 (com nota própria)

**Brasil**
- [[Emissor de NFS-e Nacional]]: concorre com o Emissor Nacional gratuito e com Focus NFe (R$ 62,90–657,90), NFE.io e Brasil NFe ([Focus NFe](https://focusnfe.com.br/precos/)).
- [[Plataforma NR-1 psicossocial (COPSOQ)]]: saturada, e as sanções estão suspensas pelo STF ([Migalhas](https://www.migalhas.com.br/quentes/465248/andre-mendonca-prorroga-por-mais-90-dias-suspensao-de-sancoes-da-nr-1)).
- [[Gerador de PGR para SST]]: mais de 10 fornecedores em 2026, vários feitos com IA.
- [[Triagem do Simples híbrido para contadores]]: concorre com o simulador oficial gratuito desde 18/09/2026 ([Movimento Econômico](https://movimentoeconomico.com.br/receita-federal/2026/09/18/simulador-da-receita-indica-impacto-de-cbs-e-ibs-nas-empresas-do-simples/)).
- [[Planejador de IRPFM e dividendos]]: calculadoras gratuitas, e a Receita pode pré-calcular o redutor ([Calculabr](https://calculabr.net.br/calculadora-imposto-dividendos/)).
- [[Camada de cobrança Pix Automático]]: exige PSP, e o Asaas não cobra extra pelo recurso ([Asaas](https://central.ajuda.asaas.com/hc/pt-br/articles/41912520942235-Quais-s%C3%A3o-as-taxas-do-Pix-Autom%C3%A1tico-no-Asaas)).
- [[Kit CNPJ alfanumérico]]: os CNPJs existentes não mudam e há bibliotecas grátis ([Agência Gov](https://agenciagov.ebc.com.br/noticias/202607/implantacao-do-cnpj-alfanumerico-ocorrera-a-partir-de-31-de-julho)).
- [[Verificação de idade ECA Digital]]: a obrigação é de lojas de apps, sistemas operacionais e apps, não de PMEs.
- [[Assistente de Transparência Salarial]]: o MTE gera o relatório, e o comprador é enterprise.
- [[Simulador IBS-CBS para locador pessoa física]]: população pequena e calculadoras gratuitas.
- [[Gestão de perícias judiciais]]: 5+ entrantes desde 2025, muitos com IA, e demanda fraca.
- [[EUDR para pequenos produtores brasileiros]]: plataformas gratuitas da Cecafé–Serasa, da Conab e do MAPA ([Campo Vivo](https://campovivo.com.br/apresentado-por-prime-cafe/2026/09/08/rastreabilidade-passa-a-definir-o-acesso-do-cafe-brasileiro-ao-mercado-europeu/)).
- [[Calculadora de landed cost]]: território de transportadoras e marketplaces.

**Exterior**
- [[Mais um app de desistência no Shopify]]: líderes com ~2.160, 465 e 275 avaliações.
- [[Gerador de GPSR]]: ~15 apps com quase nenhuma avaliação, e os marketplaces têm campos nativos.
- [[Rastreador de EPR de embalagens]]: quem domina são os serviços; no máximo, afiliado.
- [[Conversor de e-invoicing]]: 149 plataformas aprovadas na França e geradores grátis ([Presse-citron](https://www.presse-citron.net/facturation-electronique-entre-vigueur-aujourdhui-voici-149-plateformes-agreees-france/)).
- [[Auditoria de acessibilidade para PMEs]]: saturada. A FTC multou a accessiBe em US$ 1 milhão ([TestParty](https://testparty.ai/blog/are-accessibility-overlays-legal)).
- [[Consentimento de cookies e GPC]]: Pandectes ~2.690 e Consentmo ~1.751 avaliações.
- [[Monitor de scripts PCI]]: alívio do SAQ A e plano grátis do cside.
- [[Monitor de DMARC]]: planos grátis de Cloudflare, Valimail, dmarcian, EasyDMARC e Postmark.
- [[Ferramenta de CBAM]]: ~90% dos importadores isentos; enterprise.
- [[Verificador de junk fees (FTC)]] e [[Kit click-to-cancel]]: fiscalização voltada a grandes plataformas e nenhuma regra federal de click-to-cancel.
- [[Ferramenta de sales tax e 1099]]: incumbentes financiados e limites subindo.
- [[ADA Title II para governos locais]]: venda para governo.
- [[Preparatório de certificação de nicho]]: exige especialista, ou seja, um contato.

## 5. Armadilhas da rodada 1 sem nota própria

### Brasil (nichos profissionais), de [[brazil_professional_niches]]
- **Monitores de DJEN e prazos para advogados:** incumbentes grandes (Astrea, R$ 379 para 5 usuários e 120 mil+ usuários; ADVBOX, 5 mil+ escritórios) e calculadoras grátis por tribunal. As regras ainda estão em aberto (STJ Tema 1.180), e a API estava geobloqueada fora do Brasil ([Astrea](https://www.aurum.com.br/astrea/); [ADVBOX](https://advbox.com.br/precos)).
- **Gestão de consultório** (médicos, dentistas, psicólogos, fisioterapeutas, nutricionistas, veterinários, estética): iClinic (50 mil+ médicos, R$ 99–299) e SimplesVet (R$ 359–440) entrincheirados; buscas por "gratuito" dominam; prontuário eletrônico traz exposição à certificação SBIS/CFM ([iClinic](https://iclinic.com.br/precos/); [SimplesVet](https://simples.vet/precos)).
- **Autogestão para locadores (clone do TurboTenant):** pelo menos seis apps brasileiros a R$ 29,90–59,90, mais o QuintoAndar ([Aluga Fácil](https://www.alugafacil.app/); [ProprietárioZen](https://proprietariozen.com.br/)).
- **Apps de vistoria de locação:** Devolus está há mais de 10 anos no mercado, além de Vistortec, Pleno, Widesys, VistoHouse e Hauseful, alguns com plano grátis ([Devolus](https://www.aplicativodevistoria.com.br/)). É por isso que o [[Gerador de laudos de vistoria e inspeção|gerador de laudos]] mira só a engenharia.
- **Software de PMOC:** Meu Pmoc tem plano grátis e pagos de R$ 159,99–299,99; pmoc.online a partir de R$ 59,90; Matum, Produttivo, Auvo e Tecniko também ([Meu Pmoc](https://meupmoc.com.br/blog/quanto-custa-um-software-de-pmoc)).
- **Channel manager de Airbnb/temporada:** o Stays domina com R$ 79–249 mais percentual e status Preferred+ do Airbnb; o acesso à API de parceiro provavelmente é exigido (não verificado) ([Stays](https://stays.net/precos/)).
- **Portais contábeis de coleta de documentos:** Gestta e Acessórias entrincheirados no ecossistema Domínio, mais entrantes com IA.
- **Fatura ou câmbio para PJ que exporta serviço:** a economia fica com as casas de câmbio licenciadas (a Husky cobra até 1%), e os modelos de invoice são grátis ([Husky](https://husky.io/)).
- **Gestão de rebanho, CAR e ITR:** venda feita por gerente de contas (Aegro); "gestão de rebanho app" retornou 0 sugestões ([Aegro](https://aegro.com.br/suporte/conta-e-assinatura/planos-de-assinatura-aegro/)).
- **Orçamento SINAPI:** o OrçaFascio se apresenta como "a maior plataforma de orçamento de obras do país", e as pessoas buscam planilhas SINAPI grátis ([Projeto Draft](https://www.projetodraft.com/como-os-amapaenses-da-orcafascio-criaram-a-maior-plataforma-de-orcamento-de-obras-do-pais/)).
- **Field service genérico (clone do Jobber):** Auvo, Field Control (R$ 295 por usuário), Produttivo e Tecniko; "sistema ordem de serviço gratuito" é busca comum ([Capterra Field Control](https://www.capterra.com/p/207608/Field-Control/)).

### Brasil (regulatório), de [[brazil_regulatory_demand]]
- **Ferramentas de split payment:** é opcional, só B2B e vem no 2º semestre de 2027 ([Radar da Reforma Tributária](https://radardareformatributaria.com/split-payment-testes-2026-implantacao-gradual-2027/)).
- **Calculadoras genéricas de preço com IBS/CBS:** existe calculadora oficial gratuita.
- **Automatizar portais do governo com o certificado do usuário** (como faz a Rebots): risco de segurança e de termos de uso ([Rebots](https://rebots.com.br/api-receita-saude)).

### Marketplaces, de [[marketplace_gaps]]
- **Apps de migração Scripts→Functions do Shopify:** o prazo passou em 30/06/2026, e os incumbentes estão entrincheirados (ETP 571, HidePay 392, Melon MOQ 385 avaliações) ([Shopify](https://shopify.dev/changelog/shopify-scripts-will-be-deprecated-on-june-30-2026)).
- **Clones de extensões famosas para substituir o MV2 do Chrome:** os sucessores já dominam (uBO Lite com 21 milhões de usuários) ([Chrome](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline)).
- **Repricers do Mercado Livre:** edição de preço via API bloqueada em itens com automação nativa desde 18/03/2026, e o programa de parceiros está fechado, com exigência de US$ 2,5 milhões de GMV ([ML](https://developers.mercadolivre.com.br/pt_br/automatizacoes-de-precos)).
- **Apps de emissão de NF-e:** o ML tem Faturador nativo com IBS/CBS, e o Bling domina na Nuvemshop (469 avaliações). Ver [[Emissor de NFS-e Nacional]].
- **Mala direta no Gmail:** YAMM (16M+), Mail Merge (12M+), Mailmeteor (7M+), e escopos restritos do Gmail exigem reavaliação anual ([Workspace](https://workspace.google.com/marketplace/search/mail%20merge)).
- **Apps de avaliações:** Judge.me roda em 4.998 lojas Shopify brasileiras; a Nuvemshop tem 36 apps de avaliação, liderados pela Lily Reviews (411).
- **Apps de WhatsApp na Nuvemshop:** 68 apps com 3.953 avaliações; só o WhatsApp Marketing tem 1.003 ([Comunicação](https://www.nuvemshop.com.br/loja-aplicativos-nuvem/categorias/comunicacao)).
- **Substituir plugins "abandonados" do WordPress:** o Limit Login Attempts já foi deslocado pelo Reloaded (1 milhão de instalações), Wordfence e Loginizer.
- **Planning poker e time tracking na Atlassian:** 1.076 e 2.782 resultados; Tempo Timesheets com 26.369 instalações.
- **Macro de Confluence só de Mermaid:** visualizador grátis da Atlassian Labs (7.600) e Just Add+ (8.072). Ver [[Macros docs-as-code para Confluence]].
- **Extensão "espiã" do ML:** Avantpro lidera com 100 mil usuários a R$ 59,90/mês. Ver [[Extensão Margem ML 2026]].
- **Lojas de apps de Tray, Loja Integrada e VTEX:** a Tray não mostra avaliações e 552 de 738 apps são ERP; a Loja Integrada caiu 29% em um ano; a VTEX é enterprise.
- **Extensões de Chrome como negócio principal:** os desenvolvedores do ExtensionPay faturaram só US$ 800 mil somados desde 2021 ([ExtensionPay](https://extensionpay.com/)).
- **Excluídas pela restrição:** serviços de migração (cartões do CRM clássico do HubSpot, consultoria DC→Cloud da Atlassian) exigem contatos; apps VTEX são venda enterprise; ferramentas espiãs com scraping têm risco de termos de uso.

### Exterior (regulatório), de [[us_eu_regulatory_demand]]
- **Responsible Person do GPSR ou representante autorizado de EPR "como serviço":** exige entidade legal na UE e assumir responsabilidade ([EUverify](https://euverify.com/resource/eu-responsible-person-under-gpsr/)).

### Receita verificada, de [[verified_revenue_niches]] (números do TrustMRR)
- **SaaS vertical para trades americanos feito por dev remoto:** HoodCleaningReport US$ 308 no total (o vendedor diz que precisa de um operador de vendas em tempo integral), InstantTradeQuote US$ 0, Volt Quotes US$ 52 de MRR, RoofEx US$ 0, AfterInspect US$ 0, Perfect HOA US$ 322 de MRR ([TrustMRR](https://trustmrr.com/startup/hoodcleaningreport)).
- **Job boards de nicho:** PlumbingJobs.org US$ 415 no total; PlumbingJobsHQ e PharmacyJobsHQ US$ 0; H1BVisaJobs US$ 740.
- **Preparatórios genéricos com IA:** ExamForge US$ 0, NomoExam US$ 35, IELTSprep US$ 30, WinePrep US$ 33, OrbitPrep US$ 0 ([TrustMRR](https://trustmrr.com/startup/exam-forge)). Ver [[IA no centro do produto]].
- **Geradores de comentário de boletim com IA por estado (SEO programático):** NSW US$ 167, VIC US$ 79, QLD US$ 13, NZ US$ 17 no total.
- **Geradores de assinatura de e-mail:** o SyncSignature faz US$ 2.536 de MRR depois de ~3 anos de SEO; os novos fazem US$ 36 e US$ 4.
- **Conversores de extrato bancário:** comprovado, mas lotado e virando commodity. SimpleBankExcel caiu a US$ 0, ScanToExcel tem US$ 25 de MRR, o DocuClipper é bem avaliado e LLMs genéricos já fazem o trabalho ([DocuClipper](https://www.docuclipper.com/pricing/)).
- **Compartilhamento de fotos de evento por QR:** um player grande tem US$ 548.870 no total; o novato me-mo.ro tem US$ 143.
- **Memoriais online** (QuickMemorial, US$ 52), **geradores de recibo** (ReceiptWorks US$ 319, BuildReceipts US$ 36, com risco de uso para recibo falso) e **clones de timer de palco** (ShareMyTimer, US$ 443 no total, contra US$ 21,8 mil/mês autodeclarados do stagetimer.io).
- **Dependência de plataforma:** o Embed Notion Pages perdeu 24% quando o Notion lançou embeds nativos; o pico do AutoPrintEmail passou de US$ 10.354 em 30 dias para US$ 1.640.
- **Termos de uso:** FriendFilter (US$ 1,8 milhão no total, mas dependente do Facebook), SoldComps (contorna limites da API do eBay), Maps2Sheets (extração do Google Maps).
- **Excluídas:** concierge de licença de mudança (exige operação física), comps do eBay, automação de Facebook/LinkedIn/Maps e apps mobile por ASO. Os US$ 99/ano da Apple sozinhos são ~76% do orçamento de ~US$ 130.

### Do thread de origem, de [[Thread X napoleaomp4]]
- Revenda de contas ou acesso ao Claude, servidor de GTA, "API pela metade do preço" e o "WebApp de direct response para Tier 1". Detalhes em [[Ideias inviáveis do thread]].
