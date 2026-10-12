---
tags:
  - oportunidade
  - mercado/br
  - status/recomendada
  - finalista
status: recomendada
veredito: CONDICIONAL
score: 21
score_inicial: 25
mercado: BR
rodada: final
fonte:
  - "[[brazil_professional_niches]]"
  - "[[finalists_brazil_verification]]"
  - "[[Oportunidade de produto validada 2026]]"
---

# Gerador de laudos de vistoria e inspeção

Voltar para [[Ranking]].

> [!tip] Aposta principal (CONDICIONAL, 21/35)
> Foi a única finalista brasileira que sobreviveu ao teste de estresse. O critério que ela não cumpre é a **prova de pagamento**, que é também o mais barato de testar: **R$ 300–400 e 60 dias de pré-venda**, sem câmbio, sem risco contratual e no idioma do comprador. Roteiro em [[Protocolo de validação]].

## O que é

Um **PWA offline** para celular. O engenheiro ou arquiteto fotografa por imóvel, ambiente, elemento construtivo e anomalia, classifica a gravidade e exporta um **laudo DOCX/PDF padronizado e com a sua marca**: grade de fotos numeradas, campo de ART/RRT, bloco de assinatura e link de compartilhamento para o cliente.

Três modelos de laudo:
- **Vistoria cautelar de vizinhança**, em lote: uma obra gera N laudos de vizinhos.
- **Vistoria de recebimento de imóvel novo.**
- **Inspeção predial / autovistoria** (ABNT NBR 16747).

O diferencial tem de ser a **saída estruturada pela norma**: seções da NBR 16747, classificação de anomalias com priorização GUT/urgência, campos de ART/RRT e laudos em lote para a cautelar. **Nada disso é IA**, o que respeita a restrição do projeto ([[Objetivo e restrições]]). Também diferencia do Howse, que se vende por conclusões geradas por IA.

## Comprador

- **Quem:** engenheiros civis, arquitetos e pequenas firmas de engenharia que vendem vistorias e laudos.
- **Tamanho da base:** cerca de 1,2 milhão de registrados no sistema Confea (engenharia, agronomia e geociências; censo de maio de 2025) e mais de 200 mil arquitetos ([Confea](https://www.confea.org.br/node/232061); [ArchDaily](https://www.archdaily.com/pt/tag/cau-br)). A fatia que vende laudos é desconhecida; 1% seriam ~14 mil profissionais (inferência da nota).
- **Poder de compra:** 68% das famílias de profissionais do sistema Confea ganham mais de cinco salários mínimos, contra 48% entre advogados ([Confea](https://www.confea.org.br/node/232061)).
- **Valor do tempo:** a tabela do IBAPE-SP fixa a hora técnica em **R$ 625** ([MK Avaliações](https://mkavaliacoesimobiliarias.com.br/o-que-e-vistoria-cautelar-de-vizinhanca/)). Um blog comercial sem data cita **R$ 2,5–15 mil por inspeção predial** ([blog](https://vestibularifsp.com.br/valor-de-laudo-de-inspecao-predial-e-a-importancia-da-abnt-nbr-16747/)). Uma ferramenta de R$ 79–149/mês se paga no primeiro laudo.
- **Dor:** laudos com dezenas a centenas de fotos são diagramados à mão no Word ou no Excel. Isso aparece em buscas como "relatório fotográfico word download" e "laudo de inspeção predial word".

## Evidências

**1. Lacuna de mercado**
- Na Play Store, as buscas "vistoria predial", "vistoria cautelar" e "laudo de vistoria" mostram apps de locação, Detran e veículos. Nenhum app específico de engenharia com instalações relevantes apareceu ([Play Store](https://play.google.com/store/search?q=vistoria%20cautelar&c=apps&hl=pt_BR&gl=BR)).
- O segmento lotado é o de vistoria de **locação** e **veicular**, com apps de 1 mil a 100 mil instalações. O de engenharia está vazio.

**2. Análogo americano**
- O **Spectora** (relatórios de inspeção residencial) teria cerca de **US$ 5,9 milhões** de receita estimada e mais de **9 mil inspetores** ([Latka](https://getlatka.com/companies/spectora.com); [Datanyze](https://www.datanyze.com/companies/spectora/448152301)).

**3. Demanda por documento** (Google Autocomplete, 12/10/2026; entre colchetes, o número de sugestões)
- Sementes de modelo e norma são ricas: "nbr 16747" [10], "vistoria de recebimento de imóvel" [10], "vistoria entrega de chaves" [10], "autovistoria rio de janeiro" [9], "laudo de vistoria de recebimento" [7]. Os modificadores são "modelo", "pdf", "word" e "checklist".
- Sementes de software quase não existem: "app inspeção predial", "software inspeção predial" e "software laudo técnico engenharia" dão 0 sugestões; "app vistoria cautelar" dá [1].
- Fonte: [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=vistoria%20de%20recebimento%20de%20im%C3%B3vel)

**4. Motor legal, que é fraco**
- O IBAPE conta **41 leis municipais e 5 estaduais** de inspeção predial, mas só **9 municipais e 1 estadual** são regulamentadas. O PL federal 6.014/2013 ainda é projeto ([IBAPE 2026](https://biblioteca.ibape-nacional.com.br/wp-content/uploads/2026/01/adrian1.pdf)).
- No Rio, a autovistoria é exigida a cada no máximo 5 anos, feita por engenheiro, arquiteto ou firma com ART/RRT. No prazo de 1/7/2014, cerca de 270 mil prédios eram obrigados e só **5%** haviam cumprido ([JB](https://www.jb.com.br/rio/noticias/2014/06/24/amp/prazo-para-autovistoria-em-predios-do-rio-termina-dia-1o-julho.html)). Um ano depois, eram **11,7%** (31.785), segundo resumo de busca ([Sindiconet](https://www.sindiconet.com.br/informese/autovistorias-noticias-manutencao-1)).

## Concorrentes

| Ferramenta | Foco | Preço | Tração |
|---|---|---|---|
| [Howse](https://howseapp.com/) | Laudos de engenharia, "Feito por Engenheiros", conclusões por IA | "De R$ 70/mês"; R$ 672/ano | Não publica; nenhum listing no Play encontrado |
| [Inspect App](https://inspectapp.com.br/) | Formulários genéricos com modelos de laudo | Só demo | "10 mil usuários ativos" (autodeclarado); Play 1.000+ |
| [Inspeção Pro](https://inspecao.pro/) | FSM e inspeção, "laudos automáticos" | Sem preço público | Play 100+ |
| [Onlaine](https://www.onlaine.com.br/) | Inspeções e laudos técnicos | Sem preço público | n/d |
| Produttivo | FSM genérico | Sem preço (trial de 15 dias) | n/d |
| [Afirma Vistoria Fácil](https://afirma.cc/vistoria-facil/) | Construtoras | R$ 1.500 de setup | n/d |
| Apps de locação (Devolus, Vistortec, Pleno, BeSoft, Hauseful…) | Locação | R$ 59,90–299/mês | 1 mil–100 mil instalações |

> [!note] O substituto real
> O concorrente de verdade são os **construtores genéricos de formulário**, como o Inspect App, em que o engenheiro monta o próprio modelo. Por isso a defesa é o **formato normativo**, não o "app de fotos".

## Riscos

> [!warning] O que pode matar a ideia
> - **Pagamento não verificado.** Nenhum concorrente brasileiro tem receita verificada, e a demanda aparece como busca por **modelo grátis**.
> - **Base pequena.** Pela conta da nota de verificação, 270 mil prédios no Rio num ciclo de 5 anos dariam ~54 mil laudos/ano com conformidade total, mas só ~6 mil/ano na conformidade observada de 11,7%. Isso significa algumas centenas de compradores ativos no Rio e, no país, provavelmente poucos milhares. Basta para R$ 27 mil/mês (~180–275 usuários a R$ 99–149), mas exige uma fatia alta do nicho.
> - **Normas pagas.** NBR 16747 e NBR 12722 são pagas, então a estrutura dos modelos precisa ser conferida por engenheiros praticantes. Os primeiros clientes da pré-venda podem cumprir esse papel. A nota não conseguiu verificar se a NBR 12722 exige a vistoria cautelar.
> - **Clones.** Uma onda de micro-SaaS montados com IA chegou aos nichos óbvios brasileiros em 2025–2026, e o código se copia em meses. A defesa está no formato normativo, na profundidade do SEO de modelos e no preço transparente.
> - O Howse ou os apps de locação podem copiar os recursos. Também há o custo de armazenar fotos.

## Pontuação

| Rodada | WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|---|
| Final ([[finalists_brazil_verification]]) | 3 | 3 | 4 | 3 | 3 | 2 | 3 | **21/35** |
| Exploratória ([[brazil_professional_niches]]) | 3 | 4 | 4 | 4 | 4 | 3 | 3 | 25/35 |

## Preço, canal e construção (hipóteses das notas)

- **Preço:** R$ 79–149/mês ou R$ 15–30 por laudo, com plano anual pré-pago, que é padrão no setor (Howse R$ 672/ano). Na pré-venda, por exemplo, R$ 99/mês ou R$ 790/ano.
- **Canal:** páginas de modelo gratuito que levam ao gerador ("gere este laudo automaticamente"), um teste de R$ 300–400 em Google Ads nas buscas de modelo, grupos de engenharia no Facebook e LinkedIn e vídeos no YouTube e Instagram ([[Canais de aquisição]]).
- **Construção:** MVP em 2–4 semanas com Claude Code: armazenamento offline de fotos, compressão, motor de layout DOCX/PDF, três modelos e cobrança por Pix e cartão.
- **Tempo até a primeira receita:** ~4–8 semanas; a pré-venda pode antecipar.

## Veredito

**CONDICIONAL.** Vira GO se a pré-venda passar. As condições, da nota de verificação:
1. Publicar 3 modelos gratuitos estruturados pela norma (NBR 16747/autovistoria RJ, cautelar com estrutura IBAPE, recebimento de imóvel novo) e medir tráfego e conversão de modelo para cadastro **antes** do app completo.
2. Pré-vender **5–10 planos anuais** (~R$ 600–1.200/ano).
3. Diferenciar por saída **determinística e normativa**, não por IA.
4. **Gatilho de abandono:** menos de 5 pré-vendas em ~60 dias, ou visitantes dos modelos que recusam o upgrade pago.

## Notas de pesquisa

- [[Oportunidade de produto validada 2026]], seção "Laudos de engenharia: lacuna real, pagamento ainda por provar"
- [[finalists_brazil_verification]], "Finalist 2" e "Scores and ranked verdicts"
- [[brazil_professional_niches]], candidato A (seções 1.8, 2 e 4)
- Relacionadas: [[Gerador de PTAM para corretores]] (mesma mecânica de SEO de modelo), [[Calendário de conformidade para síndicos]] (a inspeção predial está na lista de obrigações do síndico), [[Padrão - saturação]]
