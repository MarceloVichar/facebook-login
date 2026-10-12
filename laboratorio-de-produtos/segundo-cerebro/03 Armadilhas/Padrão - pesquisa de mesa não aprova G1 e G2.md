---
tags:
  - armadilha
  - padrao
  - metodo
atualizado: 2026-10-12
fonte:
  - "[[Validação condicionais e novos focos]]"
  - "[[Rodada 3 - resumo]]"
---

# Padrão: a pesquisa de mesa não aprova G1 e G2 juntos

Voltar para [[Armadilhas e ideias mortas]] · [[Portões de aprovação]].

> [!important] A conclusão central da rodada 2, confirmada na rodada 3
> **Três rodadas e mais de 100 ideias depois, nenhuma foi aprovada.** Isso não quer dizer que as ideias são ruins. Quer dizer que a evidência que falta **só existe depois que um desconhecido paga** ([[Validação condicionais e novos focos]]).

## Por que as duas portas não convivem na fonte pública

G1 pede receita observável de concorrentes. G2 pede um mercado sem multidão **e** um recém-chegado que fature. Três mecanismos impedem que as duas provas apareçam juntas:

1. **Visibilidade gera imitação.**
   - A receita do TruckerDB ficou pública em 2026 e, no mesmo ano, surgiram TruckingLists, Carrier Signal e Truckr sobre o mesmo dado ([newauthorityleads.com](https://newauthorityleads.com/)).
   - Os votos públicos da Atlassian geraram a enxurrada da Katabarwa ([[Padrão - enxurrada de micro-SaaS feito com IA]]).
   - Os termos da API do TrustMRR proíbem "cloning businesses" ([TrustMRR API](https://trustmrr.com/docs/api)).
   - **Quando a prova de G1 aparece, G2 já está fechando.**
2. **Onde não há concorrentes, não há receita para observar.** Corretor de seguros, NPPES, licenças de bebida e lucro por live passam em G2 justamente porque ninguém visível vende aquilo, e por isso falham ou ficam fracos em G1.
3. **As fontes brasileiras escondem a venda.** O Hotmart não mostra quantas vendas um produto teve, a loja do TikTok BR não mostra instalações nem avaliações, e incumbentes como Onlaine e Inspect só publicam números autodeclarados ([Inspect App](https://inspectapp.com.br/)).

## O que a pesquisa de mesa ainda resolve, e o que não resolve

| Resolve sem dinheiro (melhora G4 e G8) | Só um teste pago resolve (G1 + G2) |
|---|---|
| Volume e CPC no Keyword Planner | Um desconhecido pagando **por este produto, deste fundador** |
| Pedido via LAI à SUSEP e à FGV | Conversão real de clique em venda |
| Data da regulamentação portuguesa (alerta no Diário da República) | Se quem baixa o modelo paga pelo gerador |
| Aprovação do SDK da Trimble | — |
| Repasse Gumroad → PayPal → Brasil (US$ 1) | — |

**Regra de três:** zero vendas em 250 cliques põem a conversão real abaixo de 1,2% ([Rule of three](https://en.wikipedia.org/wiki/Rule_of_three_(statistics))). É esse tipo de número que decide, e ele só existe depois de um teste pago.

## Consequência prática

- A pergunta deixa de ser "qual ideia passa nas oito portas?" e passa a ser **"qual dúvida restante custa menos para virar dado?"**
- Por isso o próximo passo é a [[Carteira de testes]], com limiares fixados antes de começar, e não mais uma rodada de pesquisa no papel.
- Se a carteira devolver zero pagantes, o relatório da rodada 2 diz que isso também é resultado: indica que, com R$ 700 e sem audiência, **a restrição real é a distribuição**, e a próxima decisão seria construir audiência ou SEO por 6–12 meses.

## Relacionadas

[[Padrão - saturação]] · [[Protocolo de validação]] · [[Registro de decisões]]
