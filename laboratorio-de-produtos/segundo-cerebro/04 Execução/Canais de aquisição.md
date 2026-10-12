---
tags:
  - execucao
  - aquisicao
atualizado: 2026-10-12
---

# Canais de aquisição

Voltar para [[00 Início]].

> [!abstract] Ordem recomendada para quem não tem audiência e tem ~R$ 700
> 1. **Distribuição que já carrega intenção de compra:** um listing em marketplace ou app store.
> 2. **Venda 1:1 feita pelo fundador** nas comunidades onde o comprador já está.
> 3. **Ferramenta ou modelo gratuito** para buscas de cauda longa com intenção de ferramenta. É o canal com efeito composto, e um pequeno teste de Google Ads serve de instrumento de validação.
>
> Fonte: [[gtm_economics_payments]], seção 9.

## Para a aposta principal (laudos): SEO de documento, anúncio pontual e conversa 1:1

- **Modelo gratuito → gerador.** O alvo são buscas de **intenção de ferramenta** ("modelo de laudo de vistoria cautelar", "laudo de inspeção predial modelo"), em que um gerador que funciona é a resposta. A demanda brasileira aparece exatamente assim ("modelo", "pdf", "word"), e não como busca de software ([[Gerador de laudos de vistoria e inspeção]]).
- **Poucas páginas, genuinamente úteis.** A política de abuso de conteúdo em escala do Google pune páginas geradas em massa, *"no matter how it's created"* ([Google Search Central](https://developers.google.com/search/docs/essentials/spam-policies)).
- **Anúncio pago serve para medir intenção e gerar a primeira receita, não para escalar.** Cadastros vindos de busca paga e de Meta convertem pior ([ChartMogul parte 2](https://chartmogul.com/reports/saas-conversion-report-2/)).
- **Conversa 1:1** em grupos de engenharia no Facebook e LinkedIn, oferecendo o modelo gratuito ([[Protocolo de validação]]).
- **YouTube e Instagram** com demonstrações, como canal complementar. A pesquisa não achou benchmark.

## Benchmarks por canal

### SEO e busca orgânica
- É lento: só **1,74–6,11%** das páginas novas chegam ao top 10 em um ano ([Ahrefs](https://ahrefs.com/blog/how-long-does-it-take-to-rank/)). Das que chegam, 40,82% chegam no primeiro mês; 72,9% das páginas do top 10 têm mais de 3 anos.
- Os **AI Overviews** cortaram em cerca de **58%** o CTR da posição 1 em consultas com AI Overview ([Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/)).
- Sinais orgânicos, de indicação, sociais e de LLMs convertem melhor que mídia paga ([ChartMogul parte 2](https://chartmogul.com/reports/saas-conversion-report-2/)).
- Relato da mesma pesquisa: uma biblioteca de modelos gratuitos teve *"40x impact"* no SEO orgânico (anedota).

### Google Ads
- O CPC brasileiro para software **não foi medido**: usar o Keyword Planner antes de gastar.
- Referência global (WordStream/LocaliQ, majoritariamente EUA): **US$ 5,26** por clique, CTR de 6,66% e conversão de 7,52% ([Search Engine Land](https://searchengineland.com/google-ads-costs-rise-again-but-conversions-improve-report-455663)). Nos EUA, US$ 50–100 compram só 10–20 cliques, o que não é teste de conversão.

### Meta Ads
- Mediana de CPC no Brasil de cerca de **US$ 0,37**, dado **não confirmado** (a página só renderizou a visão global) ([Superads](https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/software-and-it-services/brazil)). Global: ~US$ 0,70 em campanhas de tráfego ([WordStream](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025)).
- Cliques baratos, mas os cadastros de pior qualidade. Não recomendado como canal principal.

### Marketplaces e app stores
- **Concentração extrema:** a extensão mediana do Chrome tem **18 usuários**; 70,4% têm até 100 ([Konabayev/Exstats](https://konabayev.com/blog/extension-monetization-statistics-2026/)).
- **Shopify:** 16 mil+ apps, US$ 1 bilhão+ pagos a desenvolvedores em 2024, 0% de comissão no primeiro US$ 1 milhão vitalício e registro único de US$ 19 ([Shopify](https://shopify.dev/docs/apps/launch/distribution/revenue-share)).
- **Atlassian:** 100% da receita Forge até US$ 1 milhão, mas a busca ordena por instalações, o que torna o início frio ([[App Forge de Gantt para Jira]]).
- **Nuvemshop:** depois do trial, não cobra automaticamente a menos que o lojista ative a cobrança ([Nuvemshop](https://atendimento.nuvemshop.com.br/pt_BR/parceiros-tecnologicos/como-eu-recebo-pelo-uso-do-meu-aplicativo-criado-na-nuvemshop)). O risco de plataforma é alto ([[Padrão - plataforma absorve o recurso]]).
- Conversão típica de instalação para pago: ~0,5–2% em extensões e WordPress; 1–2% no Freemius.
- Ranking de marketplaces para um novato ([[marketplace_gaps]], seção 8): 1º Atlassian (Forge), 2º Nuvemshop, 3º Google Workspace, 4º Shopify (só nicho brasileiro), 5º Chrome, …, 8º WordPress.org (evitar), 9º ecossistema do Mercado Livre (evitar).

### Comunidades e conversa 1:1
- Nenhum benchmark quantitativo. Plano: **20–50 conversas qualificadas para 1–5 pilotos pagantes** (inferência da nota).
- Listas com menos de 50 destinatários têm 5,8% de resposta, contra 2,1% acima de 1.000; personalização avançada tem ~17–18% ([Woodpecker](https://woodpecker.co/blog/cold-email-statistics/)).

### Product Hunt, diretórios e e-mail frio
- **Product Hunt:** em geral 100–2.000 visitantes num pico de um dia; público errado para PME brasileira ([MySignature](https://mysignature.io/blog/product-hunt-launch/)).
- **E-mail frio em volume:** o usuário prefere não depender disso; a média de resposta está em ~3,4% e caindo.

## Para as alternativas

- **Cartas:** dezenas de páginas por intenção vertical (contestação, aviso de locador por estado, HMRC/DVLA), que é como os pequenos ranqueiam, mais Google Ads em termos de alta intenção ([[Cartas registradas online (EUA e Reino Unido)]]).
- **Jira:** busca do Marketplace, selo "Runs on Atlassian", páginas de comparação ("BigGantt alternative") e respostas na Atlassian Community ([[App Forge de Gantt para Jira]]).
- **FMCSA:** SEO com lista de amostra grátis; o TruckerDB tem 20 assinantes com 192 visitas/mês ([[Feed de transportadoras recém-registradas (FMCSA)]]).

## Preço que ajuda o canal

- Ficar na faixa em que profissionais brasileiros já pagam por ferramenta de nicho, **R$ 49–149/mês**, com **plano anual pré-pago** (o Howse cobra R$ 672/ano). Uma opção **por laudo de R$ 15–30** atende quem faz poucas vistorias.
- **Assinaturas abaixo de US$ 10 sofrem** com taxa fixa e churn de 6–7% ao mês ([ChartMogul churn](https://chartmogul.com/blog/good-customer-churn-rate/)). Ver [[Expectativas e prazos]].

## Fontes

[[Oportunidade de produto validada 2026]] (seção "Go-to-market") · [[gtm_economics_payments]] (seções 1, 2 e 9) · [[marketplace_gaps]] (seções 7 e 8)
