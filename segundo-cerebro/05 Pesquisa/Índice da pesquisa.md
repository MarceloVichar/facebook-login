---
tags:
  - hub
  - pesquisa
atualizado: 2026-10-12
---

# Índice da pesquisa

Voltar para [[00 Início]].

A pesquisa profunda rodou em **12/10/2026** em 8 frentes: 6 de exploração e 2 de verificação dos finalistas. O relatório final foi escrito em português; as notas de pesquisa estão em inglês e foram mantidas como vieram, só movidas de pasta. A estrutura segue o layout do deep-research:

```
05 Pesquisa/
├── reports/
│   └── Oportunidade de produto validada 2026.md
└── research_notes/
    └── Oportunidade de produto validada 2026/
        ├── brazil_professional_niches.md
        ├── brazil_regulatory_demand.md
        ├── finalists_brazil_verification.md
        ├── finalists_global_verification.md
        ├── gtm_economics_payments.md
        ├── marketplace_gaps.md
        ├── us_eu_regulatory_demand.md
        └── verified_revenue_niches.md
```

> [!info] Hierarquia das fontes
> **A rodada final de verificação prevalece sobre as notas anteriores.** Quando uma nota exploratória e uma de verificação discordam (o número de concorrentes de dedetização, por exemplo), vale a verificação. As pontuações de pesquisadores diferentes servem para ordenar dentro da mesma rodada, não para comparar entre rodadas.

## Relatório final

### [[Oportunidade de produto validada 2026]]
*"Nenhuma oportunidade passa limpa; laudos lideram."* Em português; é a síntese de tudo.
- **Conclusão:** nenhum candidato cumpre os 7 critérios. A aposta mais defensável é o [[Gerador de laudos de vistoria e inspeção]], **condicional a uma pré-venda de 60 dias**. Alternativas: [[Cartas registradas online (EUA e Reino Unido)]] e [[App Forge de Gantt para Jira]] em nicho estreito.
- **Seções:** os critérios e o paradoxo; laudos; cartas e Jira; ideias promissoras não testadas; ideias mortas; validação em 60 dias; go-to-market; pagamento e impostos; prazos; conclusão.
- **Ideia-chave:** escolher a candidata **cuja dúvida restante custa menos para resolver**.
- Vira notas em: [[Ranking]], [[Armadilhas e ideias mortas]], [[Protocolo de validação]], [[Canais de aquisição]], [[Pagamentos e impostos]], [[Expectativas e prazos]].

## Frentes de exploração

### [[brazil_professional_niches]]
*Nichos profissionais e de pequenas empresas brasileiras: fluxos manuais, incumbentes, lacunas de arbitragem.*
- **Método:** ~60 buscas, leitura direta de ~45 páginas de fornecedores e órgãos e varredura do Google Autocomplete (pt-BR) em 80 sementes. A cota de busca acabou no meio.
- **Achado:** a gestão de consultório ou escritório está saturada em todas as profissões. As lacunas são sub-fluxos estreitos, documentais e disparados por conformidade, ainda feitos no Word, no Excel ou no WhatsApp.
- **Candidatos:** [[Gerador de laudos de vistoria e inspeção|Laudos]] (A, 25), [[Gerador de PTAM para corretores|PTAM]] (B, 23), [[Certificados de dedetização e caixa d'água|Dedetização]] (C, 23), [[Calendário de conformidade para síndicos|Síndicos]] (D, 23), [[Gerador de PGR para SST|PGR]] (E, 22), [[Fluxo HoneyBook para arquitetos|HoneyBook]] (G, 22), [[Gestão de perícias judiciais|Perícias]] (F, 21).
- **Armadilhas listadas:** DJEN, gestão de consultório, locador, vistoria de locação, PMOC, NR-1, Airbnb, portais contábeis, entre outras.

### [[brazil_regulatory_demand]]
*Obrigações legais, fiscais e regulatórias do Brasil em 2026–2027 como demanda forçada.*
- **Método:** textos primários (Planalto, STF, Portal do Simples, Receita, CGIBS), notícias contábeis, Google Trends e autocomplete em 12/10/2026.
- **Temas:** Lei 15.270 (IR), Reforma Tributária, Simples híbrido, locação PF, NR-1, NFS-e nacional, Receita Saúde, CNPJ alfanumérico, ECA Digital, Pix Automático, Transparência Salarial, DeCripto.
- **Candidatos:** [[Recibos em lote do Receita Saúde|Receita Saúde]] (C1, 25), [[Gerador do arquivo DeCripto|DeCripto]] (C2, 23) e mais nove que falharam no gate de disposição a pagar ou são armadilhas (C3–C11).

### [[us_eu_regulatory_demand]]
*Prazos regulatórios nos EUA e na UE (2025–2027) que empurram PMEs e vendedores online a comprar software.*
- **Método:** só trechos de mecanismos de busca, porque a ferramenta de leitura de páginas falhou com erro de DNS em todos os domínios. Sem dados de volume de busca.
- **Temas:** GPSR, EPR/PPWR, EUDR, CBAM, e-invoicing, acessibilidade, privacidade e cookies, PCI DSS 4.0.1, DMARC, regras da FTC, sales tax/1099, responsabilidade de ferramentas de conformidade.
- **Candidatos:** [[Botão de desistência da UE fora do Shopify|Desistência UE]] (C1, 26), [[Scanner de green claims (EmpCo)|EmpCo]] (C2, 23), [[Kit EUDR para micro-operadores da UE|EUDR micro-operadores]] (C3, 21) e mais 15 rejeitadas, a maioria armadilhas.

### [[marketplace_gaps]]
*Lacunas em marketplaces e app stores para um dev solo brasileiro.*
- **Método:** crawls próprios das páginas e APIs públicas (Nuvemshop, Atlassian, WordPress.org, Google Workspace, Shopify, Chrome Web Store) e Store Leads.
- **Achado:** ranking de marketplaces por relação demanda/concorrência: 1º Atlassian (Forge), 2º Nuvemshop, 3º Google Workspace.
- **Candidatos:** [[App Forge de Gantt para Jira|Gantt Jira]] (C1, 26), [[Sync Google Sheets e Google Calendar|Sheets ⇄ Calendar]] (C2, 25), [[Macros docs-as-code para Confluence|Confluence]] (C5, 25), [[Lucro real por pedido para Nuvemshop|Lucro real]] (C8, 23), [[Atacado e B2B para Nuvemshop (NubeSDK)|Atacado Nuvemshop]] (C3, 22), [[Extensão Margem ML 2026|Margem ML]] (C7, 22), [[Kit Brasil para Shopify|Kit Brasil Shopify]] (C6, 20), [[Busca e filtros para Nuvemshop|Busca Nuvemshop]] (C4, 19). Mais 13 armadilhas.

### [[verified_revenue_niches]]
*Nichos de software pequenos com receita verificada (US$ 1–30 mil de MRR).*
- **Método:** páginas do TrustMRR, que puxa a receita do processador de pagamento e por isso conta como **verificada**; números do Starter Story são autodeclarados. Sem dados de volume de busca.
- **Achado:** padrões que funcionam sem audiência: prova de nicho profissional, ponte com o mundo físico (cartas), dados públicos virando leads B2B, lacunas de exportação e plugins de e-commerce.
- **Candidatos:** [[Cartas registradas online (EUA e Reino Unido)|Cartas]] (C1, 28), [[Conversor de lacuna de plataforma|Conversor]] (C4, 26), [[Feed de transportadoras recém-registradas (FMCSA)|FMCSA]] (C2, 24), [[Plugin WooCommerce freemium|WooCommerce]] (C5, 24), [[Preparatório de certificação de nicho|Preparatório]] (C3, 23), [[Utilitário inbox-para-operação|Inbox-ops]] (C6, 21), [[App Shopify de nicho|Shopify nicho]] (C7, 21).

### [[gtm_economics_payments]]
*Primeiros clientes, economia de MRR, validação barata e pagamento/impostos para um fundador solo brasileiro.*
- **Método:** páginas de preço lidas ao vivo em 12/10/2026, com etiquetas de confiabilidade: [P] primária, [S] só resumo de busca, [V] fornecedor, [A] anedota.
- **Seções:** benchmarks de funil; canais; tempo até US$ 1 mil/5 mil de MRR e churn; validação e tamanho de amostra; receber no Brasil; vender ao exterior (merchant of record); estrutura legal e impostos; higiene legal; síntese com protocolo de 7–14 dias.
- Vira notas em: [[Protocolo de validação]], [[Canais de aquisição]], [[Pagamentos e impostos]], [[Expectativas e prazos]].

## Rodada final de verificação

### [[finalists_brazil_verification]]
*Teste de estresse de quatro finalistas brasileiros.*
- **Método:** páginas buscadas com curl em 12/10/2026, autocomplete pt-BR e censo de concorrentes.
- **Resultado:** [[Gerador de laudos de vistoria e inspeção|Laudos]] **CONDICIONAL (21)**; [[Certificados de dedetização e caixa d'água|Dedetização]] KILL (19); [[Atacado e B2B para Nuvemshop (NubeSDK)|Atacado Nuvemshop]] KILL (18); [[Recibos em lote do Receita Saúde|Receita Saúde]] KILL (17).
- **Padrão identificado:** nichos regulatórios atraem o governo (modelo grátis), o dono da plataforma (recurso nativo) ou muitos SaaS pequenos. Sobrevive o nicho de saída profissional, presa a norma e fragmentada por municípios.

### [[finalists_global_verification]]
*Teste de estresse de quatro finalistas globais/em dólar.*
- **Método:** páginas primárias e APIs, Tranco como proxy de tráfego e Google Suggest, com etiquetas [V], [S], [3P] e [SS].
- **Resultado:** [[Cartas registradas online (EUA e Reino Unido)|Cartas]] **CONDICIONAL (21)**; [[App Forge de Gantt para Jira|Gantt Jira]] **CONDICIONAL, nicho estreito (22)**; [[Sync Google Sheets e Google Calendar|Sheets ⇄ Calendar]] KILL (17); [[Botão de desistência da UE fora do Shopify|Desistência UE]] KILL (17).
- **Nota:** o ranking contraria as notas brutas de propósito (cartas acima do Jira) por causa da prova de que estreantes sem audiência faturam.

## Lacunas comuns a todas as frentes

- **Volume absoluto de busca e CPC** não foram medidos: sem Keyword Planner, e os conectores Ahrefs e Similarweb falharam. É a primeira coisa a medir ([[Próximos passos]]).
- **Receita de concorrentes brasileiros** nunca foi verificada; só contagens autodeclaradas.
- **Nenhuma entrevista com compradores:** todas as notas são de pesquisa de mesa.
- A cota de buscas compartilhada acabou em várias frentes; cada nota lista o que ficou de fora na seção "Gaps".
