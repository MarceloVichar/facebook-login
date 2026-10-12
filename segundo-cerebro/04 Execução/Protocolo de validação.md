---
tags:
  - execucao
  - validacao
atualizado: 2026-10-12
---

# Protocolo de validação

Voltar para [[00 Início]] · checklist em [[Próximos passos]].

> [!important] Princípio
> **Só dinheiro de desconhecidos é sinal forte.** E-mail em lista de espera é sinal fraco. Pré-venda, depósito reembolsável ou trial com cartão obrigatório são sinais fortes ([[gtm_economics_payments]], seção 4).

O protocolo junta a regra de decisão de 7–14 dias de [[gtm_economics_payments]] com o gatilho de 60 dias da [[finalists_brazil_verification|verificação brasileira]]. Ele foi desenhado para o [[Gerador de laudos de vistoria e inspeção]], mas o mesmo roteiro vale para as alternativas.

## Por que ~100 visitantes por página

- Benchmarks de quem já tem tração: mediana de **8%** de grátis para pago em seis meses, e **25–35%** em trials com cartão obrigatório ([ChartMogul](https://chartmogul.com/reports/saas-conversion-report/)). Um produto novo deve planejar no **quartil inferior, até 2,5%**.
- **Regra de três:** zero conversões em *n* tentativas limitam a taxa real a menos de 3/*n* com 95% de confiança ([Regra de três](https://en.wikipedia.org/wiki/Rule_of_three_(statistics))). Zero em 100 visitas significa menos de 3%; zero em 200, menos de 1,5%.
- **Com menos de ~100 visitantes qualificados, não dá para distinguir uma oferta de 3% de uma de 10%.**

| Conversão real | n = 100 | n = 200 | n = 400 |
|---|---|---|---|
| 5% | ±4,3 pp | ±3,0 pp | ±2,1 pp |
| 10% | ±5,9 pp | ±4,2 pp | ±2,9 pp |
| 20% | ±7,8 pp | ±5,5 pp | ±3,9 pp |

Intervalos de Wilson para contagens pequenas: 3/30 → 3,5–25,6%; 5/50 → 4,3–21,4%; 10/100 → 5,5–17,4% (cálculo da nota de GTM).

## Roteiro de 60 dias (laudos)

### Semanas 1–2: páginas de modelo, sem escrever o app
Publicar **três páginas de modelo gratuito**:
1. Laudo de inspeção predial/autovistoria (NBR 16747)
2. Vistoria cautelar com estrutura IBAPE
3. Vistoria de recebimento de imóvel novo

Cada página leva:
- um **protótipo clicável** do gerador;
- **preço visível**, por exemplo R$ 99/mês ou R$ 790/ano;
- dois botões: **"Garantir vaga de fundador"**, com link real de Pix/cartão no Asaas e reembolso de 7 dias, e **"Entrar na lista"**;
- analytics com UTMs.

### Semanas 2–4: tráfego e conversas
- **R$ 300–400 em Google Ads**, correspondência exata e de frase, nas buscas de modelo, buscando **≥100 cliques por página**. Antes de gastar, medir CPC no Keyword Planner, porque o CPC brasileiro para software não foi medido ([[Canais de aquisição]]).
- **20–40 conversas individuais** em grupos de engenharia no Facebook e LinkedIn, oferecendo o modelo gratuito. Mensagens pequenas e personalizadas têm resposta de 5,8–18%, contra 3,4% da média de disparo frio ([Woodpecker](https://woodpecker.co/blog/cold-email-statistics/)).
- Oferecer um **preço de fundador** a quem interagiu (por exemplo, 3 meses pelo preço de 1, ou 50% vitalício).

### Semanas 4–8: MVP só para quem pagou
- PWA offline, fotos comprimidas, três modelos e exportação DOCX/PDF: **2–4 semanas com Claude Code**.
- Pedir aos clientes que **revisem os modelos contra as normas** (NBR são pagas).

## Regras de decisão

| Decisão | Condição |
|---|---|
| **Seguir** | ≥3 pagamentos de desconhecidos (ou ≥R$ 300 recebidos) **e** ≥10% dos visitantes qualificados na lista, **ou** ≥1–2% dos cliques de anúncio pagando |
| **Iterar** (mais um ciclo de 7 dias em copy, segmento ou preço) | 3–10% de conversão para a lista e 0–2 pagamentos |
| **Abandonar** | <3% de conversão para a lista após 100–150 visitantes qualificados **e** 0 pagamentos após 20+ conversas, **ou** menos de 5 pré-vendas anuais em ~60 dias |

Limiares auxiliares da nota de GTM (síntese dos pesquisadores, não padrão do mercado):
- CTR ≥5% no anúncio indica que a busca combina com a oferta.
- Clique em "comprar" ≥2–3% num fake door justifica passar à pré-venda real, mostrando depois do clique uma mensagem honesta de "lançando em breve, reserve sua vaga".
- ≥5% de clique para cadastro, ou ≥1% de clique para pagamento, indica oferta real.

> [!tip] Cartão obrigatório como filtro
> Na pesquisa MicroConf, **71% dos SaaS independentes exigem cartão**, e a recomendação para fundadores de primeira viagem é mantê-lo até ter 10–50 clientes pagantes ([SFTROU ep. 721](https://www.startupsfortherestofus.com/episodes/episode-721-7-key-takeaways-from-the-2024-state-of-independent-saas-report)).

## Orçamento (cabe nos R$ 700, com folga para um 2º ciclo)

| Item | Custo estimado |
|---|---|
| Domínio .com.br | R$ 50–100 |
| Hospedagem e banco (camadas gratuitas) | R$ 0 |
| Google Ads (teste) | R$ 300–400 |
| Asaas (sem mensalidade; taxa só por cobrança) | R$ 0 fixo |
| Reserva para um segundo ciclo de teste | R$ 200–350 |

Os valores de domínio e hospedagem são estimativas, não cotações verificadas.

## Se os laudos forem abandonados

O mesmo roteiro se aplica às [[Cartas registradas online (EUA e Reino Unido)|cartas]], **desde que a Lob tenha respondido o ticket por escrito**. Senão, a próxima candidata a verificar é o [[Feed de transportadoras recém-registradas (FMCSA)]].

## Fontes

[[Oportunidade de produto validada 2026]] (seção "Validação em 60 dias") · [[gtm_economics_payments]] (seções 4 e 9) · [[finalists_brazil_verification]] ("Scores and ranked verdicts")
