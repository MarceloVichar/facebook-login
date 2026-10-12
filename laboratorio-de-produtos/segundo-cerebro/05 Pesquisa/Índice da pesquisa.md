---
tags:
  - hub
  - pesquisa
atualizado: 2026-10-12
---

# Índice da pesquisa

Voltar para [[00 Início]].

A pesquisa rodou em **três rodadas, todas em 12/10/2026**. Os relatórios estão em português; as notas de pesquisa estão em inglês e foram mantidas como vieram. A rodada 3 não teve relatório próprio: o [[Rodada 3 - resumo]] foi escrito depois, a partir das três notas, mantendo as citações. A estrutura segue o layout do deep-research:

```
05 Pesquisa/
├── reports/
│   ├── Oportunidade de produto validada 2026.md   (rodada 1)
│   ├── Validação condicionais e novos focos.md    (rodada 2)
│   └── Rodada 3 - resumo.md                       (rodada 3, escrito a partir das notas)
└── research_notes/
    ├── Oportunidade de produto validada 2026/      (rodada 1)
    │   ├── brazil_professional_niches.md
    │   ├── brazil_regulatory_demand.md
    │   ├── finalists_brazil_verification.md
    │   ├── finalists_global_verification.md
    │   ├── gtm_economics_payments.md
    │   ├── marketplace_gaps.md
    │   ├── us_eu_regulatory_demand.md
    │   └── verified_revenue_niches.md
    ├── Validação condicionais e novos focos/      (rodada 2)
    │   ├── brazil_emerging_platforms.md
    │   ├── certified_mail_validation.md
    │   ├── laudos_validation.md
    │   ├── niche_exam_prep.md
    │   ├── portuguese_spanish_arbitrage.md
    │   ├── public_records_data.md
    │   ├── trustmrr_newcomers.md
    │   ├── trustmrr_newcomers.csv
    │   └── unmet_feature_requests.md
    └── Análogos brasileiros e provas de nicho/    (rodada 3)
        ├── brazil_regulated_documents.md
        ├── exam_prep_deep.md
        └── trustmrr_br_pt_mapping.md
```

> [!info] Hierarquia das fontes
> **A rodada mais recente prevalece sobre as anteriores**, e dentro da rodada 1, a verificação final prevalece sobre as notas exploratórias. Quando uma nota exploratória e uma de verificação discordam (o número de concorrentes de dedetização, por exemplo), vale a verificação. As pontuações de pesquisadores diferentes servem para ordenar dentro da mesma rodada, não para comparar entre rodadas.

## Rodada 1

### Relatório final

#### [[Oportunidade de produto validada 2026]]
*"Nenhuma oportunidade passa limpa; laudos lideram."* Em português; é a síntese de tudo.
- **Conclusão:** nenhum candidato cumpre os 7 critérios. A aposta mais defensável é o [[Gerador de laudos de vistoria e inspeção]], **condicional a uma pré-venda de 60 dias**. Alternativas: [[Cartas registradas online (EUA e Reino Unido)]] e [[App Forge de Gantt para Jira]] em nicho estreito.
- **Seções:** os critérios e o paradoxo; laudos; cartas e Jira; ideias promissoras não testadas; ideias mortas; validação em 60 dias; go-to-market; pagamento e impostos; prazos; conclusão.
- **Ideia-chave:** escolher a candidata **cuja dúvida restante custa menos para resolver**.
- Vira notas em: [[Ranking]], [[Armadilhas e ideias mortas]], [[Protocolo de validação]], [[Canais de aquisição]], [[Pagamentos e impostos]], [[Expectativas e prazos]].

### Frentes de exploração

#### [[brazil_professional_niches]]
*Nichos profissionais e de pequenas empresas brasileiras: fluxos manuais, incumbentes, lacunas de arbitragem.*
- **Método:** ~60 buscas, leitura direta de ~45 páginas de fornecedores e órgãos e varredura do Google Autocomplete (pt-BR) em 80 sementes. A cota de busca acabou no meio.
- **Achado:** a gestão de consultório ou escritório está saturada em todas as profissões. As lacunas são sub-fluxos estreitos, documentais e disparados por conformidade, ainda feitos no Word, no Excel ou no WhatsApp.
- **Candidatos:** [[Gerador de laudos de vistoria e inspeção|Laudos]] (A, 25), [[Gerador de PTAM para corretores|PTAM]] (B, 23), [[Certificados de dedetização e caixa d'água|Dedetização]] (C, 23), [[Calendário de conformidade para síndicos|Síndicos]] (D, 23), [[Gerador de PGR para SST|PGR]] (E, 22), [[Fluxo HoneyBook para arquitetos|HoneyBook]] (G, 22), [[Gestão de perícias judiciais|Perícias]] (F, 21).
- **Armadilhas listadas:** DJEN, gestão de consultório, locador, vistoria de locação, PMOC, NR-1, Airbnb, portais contábeis, entre outras.

#### [[brazil_regulatory_demand]]
*Obrigações legais, fiscais e regulatórias do Brasil em 2026–2027 como demanda forçada.*
- **Método:** textos primários (Planalto, STF, Portal do Simples, Receita, CGIBS), notícias contábeis, Google Trends e autocomplete em 12/10/2026.
- **Temas:** Lei 15.270 (IR), Reforma Tributária, Simples híbrido, locação PF, NR-1, NFS-e nacional, Receita Saúde, CNPJ alfanumérico, ECA Digital, Pix Automático, Transparência Salarial, DeCripto.
- **Candidatos:** [[Recibos em lote do Receita Saúde|Receita Saúde]] (C1, 25), [[Gerador do arquivo DeCripto|DeCripto]] (C2, 23) e mais nove que falharam no gate de disposição a pagar ou são armadilhas (C3–C11).

#### [[us_eu_regulatory_demand]]
*Prazos regulatórios nos EUA e na UE (2025–2027) que empurram PMEs e vendedores online a comprar software.*
- **Método:** só trechos de mecanismos de busca, porque a ferramenta de leitura de páginas falhou com erro de DNS em todos os domínios. Sem dados de volume de busca.
- **Temas:** GPSR, EPR/PPWR, EUDR, CBAM, e-invoicing, acessibilidade, privacidade e cookies, PCI DSS 4.0.1, DMARC, regras da FTC, sales tax/1099, responsabilidade de ferramentas de conformidade.
- **Candidatos:** [[Botão de desistência da UE fora do Shopify|Desistência UE]] (C1, 26), [[Scanner de green claims (EmpCo)|EmpCo]] (C2, 23), [[Kit EUDR para micro-operadores da UE|EUDR micro-operadores]] (C3, 21) e mais 15 rejeitadas, a maioria armadilhas.

#### [[marketplace_gaps]]
*Lacunas em marketplaces e app stores para um dev solo brasileiro.*
- **Método:** crawls próprios das páginas e APIs públicas (Nuvemshop, Atlassian, WordPress.org, Google Workspace, Shopify, Chrome Web Store) e Store Leads.
- **Achado:** ranking de marketplaces por relação demanda/concorrência: 1º Atlassian (Forge), 2º Nuvemshop, 3º Google Workspace.
- **Candidatos:** [[App Forge de Gantt para Jira|Gantt Jira]] (C1, 26), [[Sync Google Sheets e Google Calendar|Sheets ⇄ Calendar]] (C2, 25), [[Macros docs-as-code para Confluence|Confluence]] (C5, 25), [[Lucro real por pedido para Nuvemshop|Lucro real]] (C8, 23), [[Atacado e B2B para Nuvemshop (NubeSDK)|Atacado Nuvemshop]] (C3, 22), [[Extensão Margem ML 2026|Margem ML]] (C7, 22), [[Kit Brasil para Shopify|Kit Brasil Shopify]] (C6, 20), [[Busca e filtros para Nuvemshop|Busca Nuvemshop]] (C4, 19). Mais 13 armadilhas.

#### [[verified_revenue_niches]]
*Nichos de software pequenos com receita verificada (US$ 1–30 mil de MRR).*
- **Método:** páginas do TrustMRR, que puxa a receita do processador de pagamento e por isso conta como **verificada**; números do Starter Story são autodeclarados. Sem dados de volume de busca.
- **Achado:** padrões que funcionam sem audiência: prova de nicho profissional, ponte com o mundo físico (cartas), dados públicos virando leads B2B, lacunas de exportação e plugins de e-commerce.
- **Candidatos:** [[Cartas registradas online (EUA e Reino Unido)|Cartas]] (C1, 28), [[Conversor de lacuna de plataforma|Conversor]] (C4, 26), [[Feed de transportadoras recém-registradas (FMCSA)|FMCSA]] (C2, 24), [[Plugin WooCommerce freemium|WooCommerce]] (C5, 24), [[Preparatório de certificação de nicho|Preparatório]] (C3, 23), [[Utilitário inbox-para-operação|Inbox-ops]] (C6, 21), [[App Shopify de nicho|Shopify nicho]] (C7, 21).

#### [[gtm_economics_payments]]
*Primeiros clientes, economia de MRR, validação barata e pagamento/impostos para um fundador solo brasileiro.*
- **Método:** páginas de preço lidas ao vivo em 12/10/2026, com etiquetas de confiabilidade: [P] primária, [S] só resumo de busca, [V] fornecedor, [A] anedota.
- **Seções:** benchmarks de funil; canais; tempo até US$ 1 mil/5 mil de MRR e churn; validação e tamanho de amostra; receber no Brasil; vender ao exterior (merchant of record); estrutura legal e impostos; higiene legal; síntese com protocolo de 7–14 dias.
- Vira notas em: [[Protocolo de validação]], [[Canais de aquisição]], [[Pagamentos e impostos]], [[Expectativas e prazos]].

### Rodada final de verificação

#### [[finalists_brazil_verification]]
*Teste de estresse de quatro finalistas brasileiros.*
- **Método:** páginas buscadas com curl em 12/10/2026, autocomplete pt-BR e censo de concorrentes.
- **Resultado:** [[Gerador de laudos de vistoria e inspeção|Laudos]] **CONDICIONAL (21)**; [[Certificados de dedetização e caixa d'água|Dedetização]] KILL (19); [[Atacado e B2B para Nuvemshop (NubeSDK)|Atacado Nuvemshop]] KILL (18); [[Recibos em lote do Receita Saúde|Receita Saúde]] KILL (17).
- **Padrão identificado:** nichos regulatórios atraem o governo (modelo grátis), o dono da plataforma (recurso nativo) ou muitos SaaS pequenos. Sobrevive o nicho de saída profissional, presa a norma e fragmentada por municípios.

#### [[finalists_global_verification]]
*Teste de estresse de quatro finalistas globais/em dólar.*
- **Método:** páginas primárias e APIs, Tranco como proxy de tráfego e Google Suggest, com etiquetas [V], [S], [3P] e [SS].
- **Resultado:** [[Cartas registradas online (EUA e Reino Unido)|Cartas]] **CONDICIONAL (21)**; [[App Forge de Gantt para Jira|Gantt Jira]] **CONDICIONAL, nicho estreito (22)**; [[Sync Google Sheets e Google Calendar|Sheets ⇄ Calendar]] KILL (17); [[Botão de desistência da UE fora do Shopify|Desistência UE]] KILL (17).
- **Nota:** o ranking contraria as notas brutas de propósito (cartas acima do Jira) por causa da prova de que estreantes sem audiência faturam.

## Rodada 2: validação das condicionais e novos focos

Instrução do usuário: resolver as condicionais e continuar pesquisando até haver ideias aprovadas ([[Registro de decisões]]). A rodada introduziu as oito portas G1–G8 ([[Portões de aprovação]]).

### Relatório

#### [[Validação condicionais e novos focos]]
*"Segunda rodada não aprova nenhuma ideia."*
- **Conclusão:** nenhum dos mais de 60 candidatos passa nas oito portas. Laudos seguem condicionais com a cunha nova; cartas, Jira e FMCSA morrem; doze condicionais novas.
- **Ideia-chave:** a pesquisa de mesa não consegue aprovar G1 e G2 juntos ([[Padrão - pesquisa de mesa não aprova G1 e G2]]).
- **Recomendação:** carteira de três testes pagos (corretor, laudos por laudo, .p7m), ~R$ 650, com limiares fixados antes.
- Vira notas em: [[Portões de aprovação]], [[Carteira de testes]], [[Ranking]], [[Armadilhas e ideias mortas]], [[Padrão - enxurrada de micro-SaaS feito com IA]], [[Padrão - pagamento e CNPJ bloqueiam rotas]].

### Notas

#### [[laudos_validation]]
*Gerador determinístico de laudos de inspeção, cautelar, recebimento e reforma NBR 16280.*
- **Método:** 302 consultas de autocomplete, censo na Play Store, raspagem do Hotmart, tabela de honorários do IBAPE-SP.
- **Resultado:** [[Gerador de laudos de vistoria e inspeção|Laudos]] **CONDICIONAL (21)**; G2 e G4 reprovados na pesquisa de mesa; cunha nova (reforma NBR 16280 + recebimento); plano de 21 dias e variante de R$ 19 por laudo.

#### [[certified_mail_validation]]
*Cartas registradas online nos EUA e no Reino Unido: CONDICIONAL vira APROVADA ou KILL?*
- **Resultado:** [[Cartas registradas online (EUA e Reino Unido)|Cartas]] **KILL (23)** em G8. A LetterStream (Monetization Mode) e o Stripe Brasil resolvem G7; a taxa do USPS não fecha a conta. Inclui a carta pronta para a LetterStream.

#### [[unmet_feature_requests]]
*Pedidos não atendidos em rastreadores públicos e o veredito final do Jira.*
- **Resultado:** [[App Forge de Gantt para Jira|Jira]] **KILL (19)**; [[Merge de tickets para Jira Service Management]] (23) e [[Compartilhamento externo de dashboards do Jira]] (21) condicionais fracos; repasse da Atlassian a pessoa física brasileira parece viável, com risco de retenção de 30%.

#### [[public_records_data]]
*Produtos de dados pagos sobre registros públicos nos EUA e no Brasil.*
- **Resultado:** [[Feed de transportadoras recém-registradas (FMCSA)|FMCSA]] **KILL (23)**; INPI, PNCP e mais 14 KILLs; condicionais [[Feed semanal de novas práticas de saúde (NPPES)|NPPES]] (23), [[Feed de licenças de bebida e restaurantes (EUA)|licenças de bebida]] (20) e [[Vencedores do PNCP para corretores de seguro-garantia|PNCP para seguro-garantia]] (19).

#### [[niche_exam_prep]]
*Preparatórios de exames de licenciamento com material oficial ou público, EUA e Brasil.*
- **Resultado:** [[Simulado do exame de corretor de seguros (SUSEP)|Corretor de seguros]] (23), [[Simulado do exame de despachante aduaneiro dos EUA (CBLE)|CBLE]] (24) e [[Simulado do Exame de Suficiência do CFC|CFC]] (20) condicionais; [[Matemática para exames de operadores de água e esgoto (EUA)|operadores de água]] condicional baixa (21); 15 exames KILL.

#### [[portuguese_spanish_arbitrage]]
*Arbitragem de idioma local em Portugal, Espanha e América Latina.*
- **Resultado:** [[Preparatório do teste de nacionalidade portuguesa|Nacionalidade portuguesa]] (22) e [[Software de condomínio autogerido em Portugal|condomínio autogerido]] (22) condicionais; alojamento local, recibos verdes, Verifactu, compliance na América Latina e outros KILL.

#### [[brazil_emerging_platforms]]
*Lacunas de ferramentas para vendedores nas plataformas brasileiras emergentes (TikTok Shop, Shopee, Temu, Shein, Kwai, WhatsApp, Hotmart).*
- **Resultado:** só o [[Lucro por live e comissão de host no TikTok Shop]] fica condicional (17); nove KILLs. A loja do TikTok BR tem 297 apps, cerca de 57% de 2026, e marketplaces exigem CNPJ.

#### [[trustmrr_newcomers]]
*Recém-chegados não-IA, com pouca audiência e receita verificada no TrustMRR.*
- **Método:** rastreamento de 11.403 páginas; 681 startups fundadas desde abril de 2025 com ≥ US$ 1 mil em 30 dias; 267 passam em todos os filtros. Dados em [trustmrr_newcomers.csv](research_notes/Validação%20condicionais%20e%20novos%20focos/trustmrr_newcomers.csv).
- **Resultado:** [[Visualizador de p7m para a Itália|.p7m]] (24), nacionalidade portuguesa (22) e relatórios de campo por ofício (22, reforço dos laudos), todos condicionais. Não vender IA não custa receita (mediana de US$ 3.311 contra US$ 3.106).

## Rodada 3: análogos brasileiros e provas de nicho

### Resumo

#### [[Rodada 3 - resumo]]
*Escrito a partir das três notas, porque a rodada não teve relatório.*
- **Conclusão:** nenhuma aprovada. CBLE vira o nº 1 (27); SUSEP morre como aposta; Portugal segue à espera da regra; três condicionais novas (parecer descritivo, extintores, SketchUp).

### Notas

#### [[exam_prep_deep]]
*Fechar as portas da SUSEP, de Portugal e do CBLE, e triar novos exames.*
- **Método:** painel Power BI da SUSEP, páginas da CBP, do IRN, do Gumroad e do Hotmart renderizadas, API do iTunes.
- **Resultado:** [[Simulado do exame de despachante aduaneiro dos EUA (CBLE)|CBLE]] **CONDICIONAL nº 1 (27)**; [[Preparatório do teste de nacionalidade portuguesa|Portugal]] **CONDICIONAL nº 2 (20)**; [[Simulado do exame de corretor de seguros (SUSEP)|SUSEP]] **KILL como aposta (24)**; despachante aduaneiro BR, CFC EQT, NMLS, FAA A&P, CWI e outros KILL.

#### [[brazil_regulated_documents]]
*Análogos brasileiros das vitórias europeias do tipo "a norma obriga um documento".*
- **Resultado:** [[Gerador de parecer descritivo da educação infantil|Parecer descritivo]] **CONDICIONAL (22)**; [[Software para empresas de manutenção de extintores|software para extintores]] **CONDICIONAL (19)**; controle de AVCB, curso de manipulador, .p7s no Brasil e outros KILL.

#### [[trustmrr_br_pt_mapping]]
*Os 267 recém-chegados do TrustMRR mapeados para Brasil e Portugal.*
- **Resultado:** só 3 passaram na triagem; [[Conversor de versões do SketchUp (PT e ES)|conversor do SketchUp]] **CONDICIONAL (22)**; carimbo CNPJ e leilões de Portugal KILL. A vantagem do idioma local quase não chega ao Brasil.

## Lacunas comuns a todas as rodadas

- **Volume absoluto de busca e CPC** não foram medidos em nenhuma das três rodadas: sem Keyword Planner, e os conectores Ahrefs e Similarweb falharam. É a primeira checagem de custo zero da [[Carteira de testes]].
- **Receita de concorrentes brasileiros** nunca foi verificada; só contagens autodeclaradas. O Hotmart não mostra vendas e a loja do TikTok BR não mostra instalações.
- **Nenhuma entrevista com compradores:** todas as notas são de pesquisa de mesa.
- A cota de buscas compartilhada acabou em várias frentes; cada nota lista o que ficou de fora na seção "Gaps".
