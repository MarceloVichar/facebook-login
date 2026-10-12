---
tags:
  - oportunidade
  - mercado/br
  - status/condicional
  - finalista
status: condicional
veredito: "CONDICIONAL (cunha nova: reforma NBR 16280 + vistoria de recebimento)"
score: 21
score_inicial: 25
mercado: BR
rodada: "2"
teste: "[[Carteira de testes]]"
fonte:
  - "[[brazil_professional_niches]]"
  - "[[finalists_brazil_verification]]"
  - "[[Oportunidade de produto validada 2026]]"
  - "[[laudos_validation]]"
  - "[[Validação condicionais e novos focos]]"
---

# Gerador de laudos de vistoria e inspeção

Voltar para [[Ranking]].

> [!warning] Condicional (21/35), com a cunha trocada na rodada 2
> A rodada 2 fez a verificação mais profunda de todas (302 consultas de autocomplete, censo na Play Store, raspagem do Hotmart e tabela de honorários do IBAPE-SP). O lado bom se confirmou, mas **G2 e G4 ficaram vermelhos na pesquisa de mesa** ([[Portões de aprovação]]). Duas mudanças:
> 1. **A cunha deixa de ser inspeção predial e cautelar e passa a ser laudo/plano de reforma NBR 16280 + vistoria de recebimento**, os documentos de maior frequência. O **PL 159/2026** (Lite) é um bônus regulatório possível.
> 2. **O teste começa pela mecânica real do produto:** um formulário web que gera o laudo de reforma e cobra **R$ 19 por Pix** ([[Carteira de testes]]).
>
> O texto abaixo, até "Rodada 2", é da rodada 1 e foi mantido como histórico.

> [!tip] Rodada 1: aposta principal (CONDICIONAL, 21/35)
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
| Rodada 2 ([[laudos_validation]]) | 3 | 2 | 4 | 2 | 4 | 3 | 3 | **21/35** |

## Preço, canal e construção (hipóteses das notas)

- **Preço:** R$ 79–149/mês ou R$ 15–30 por laudo, com plano anual pré-pago, que é padrão no setor (Howse R$ 672/ano). Na pré-venda, por exemplo, R$ 99/mês ou R$ 790/ano.
- **Canal:** páginas de modelo gratuito que levam ao gerador ("gere este laudo automaticamente"), um teste de R$ 300–400 em Google Ads nas buscas de modelo, grupos de engenharia no Facebook e LinkedIn e vídeos no YouTube e Instagram ([[Canais de aquisição]]).
- **Construção:** MVP em 2–4 semanas com Claude Code: armazenamento offline de fotos, compressão, motor de layout DOCX/PDF, três modelos e cobrança por Pix e cartão.
- **Tempo até a primeira receita:** ~4–8 semanas; a pré-venda pode antecipar.

## Rodada 2: o que mudou

**O lado bom se confirmou** ([[laudos_validation]]):
- A hora técnica do IBAPE-SP é **R$ 625**, com mínimo de **R$ 6.875 por contrato**; o mercado cobra **R$ 500–3.500 por vistoria de recebimento** de apartamento em 2026 ([IBAPE-SP](https://www.ibape-sp.org.br/wp-content/uploads/2025/11/1744630330-regulamento-de-honorarios-2025-aprovado.pdf); [Monitor do Mercado](https://monitordomercado.com.br/noticias/409181-quanto-custa-contratar-uma-vistoria-profissional-antes-de-receber-as-chaves-do-apartamento/)). Uma ferramenta de R$ 79–149/mês custa menos de 10% de um único serviço.
- **PL 159/2026** criaria o Laudo de Inspeção Técnica de Edificação (**Lite**), com 13 itens obrigatórios, entre eles foto de cada anomalia e classificação de prioridade, exatamente o que um gerador determinístico produz. Está "pronto para deliberação do plenário" do Senado desde 09/04/2026 ([Senado](https://legis.senado.leg.br/dadosabertos/processo?codigoMateria=172470); [texto do PL](https://legis.senado.gov.br/sdleg-getter/dadosabertos/documento/24d183db-0325-41b0-8993-83cb907dd560)). O profissional, não a ferramenta, assina e emite a ART (art. 7 do projeto).
- Provas estrangeiras de SaaS não-IA de relatório de campo: Valideo (França, US$ 5.287 em 30 dias), FireCert (Reino Unido, US$ 5.003) e BasinCheck (US$ 2.235) ([TrustMRR Valideo](https://trustmrr.com/startup/valideo); [FireCert](https://trustmrr.com/startup/firecert); [BasinCheck](https://trustmrr.com/startup/basincheck)). Nenhuma é brasileira.

**O lado ruim pesou mais:**
- **G2:** a rodada 1 subestimou o **Onlaine**, incumbente de 15 anos com planos de R$ 89, R$ 139 e R$ 219 por usuário e "+3000 laudos/mês" autodeclarados ([Onlaine](https://www.onlaine.com.br/onlaine-inspecao.html)). O Howse, o novato mais parecido, tem **100+ downloads e 8 avaliações** ([Play](https://play.google.com/store/apps/details?id=com.leonelgregioauler.vistorias)). No Hotmart, dos **66 modelos datados desde 2025, só 1 tem avaliação**, e já há "geradores" a US$ 2–7 ([Hotmart](https://hotmart.com/pt-br/marketplace/produtos?q=nbr%2016280)).
- **G4:** das **96 sondagens** "laudo + app/software/programa/gerador", só 11 trouxeram alguma sugestão; a única intenção de ferramenta relevante foi "relatório fotográfico", território do FotoGeo (100 mil+ downloads, módulos a R$ 9,90 por semestre) ([Play FotoGeo](https://play.google.com/store/apps/details?id=fotogeo.com.br.app)). Ver [[Padrão - busca por grátis e modelo]].
- **Universo online pequeno:** o IBAPE tem ~2 mil associados, os maiores canais do YouTube têm 3–4 mil inscritos e o melhor curso da Udemy tem 400 alunos ([Udemy](https://www.udemy.com/course/inspecao-predial-e-plano-de-manutencao-para-condominios/)). A nota estima um público ativo online de ~3–15 mil. R$ 24.950/mês exigem 168–362 assinantes, ou 1–12% desse universo.

**A cunha nova:** vídeos de laudo de reforma têm 8–12 mil views, e o lançamento de 453 mil unidades em 2025 alimenta as vistorias de entrega de chaves ([YouTube](https://youtu.be/KyUl6lKqW_4); [InfoMoney](https://www.infomoney.com.br/?p=3217679)). Modelos da fase 1: laudo/plano de reforma NBR 16280 e vistoria de recebimento. Fase 2: inspeção predial/Lite e cautelar em lote.

**Cuidados de G7:** não reproduzir texto de norma da ABNT (o direito autoral é disputado: há decisões excluindo normas técnicas, mas a ABNT afirmou em set/2025 que as NBRs são protegidas ([Migalhas](https://www.migalhas.com.br/depeso/198566/justica-federal-confirma-que-normas-tecnicas-da-abnt-nao-sao-objeto-de-direitos-de-autor); [CFF](https://site.cff.org.br/noticia/Noticias-gerais/10/09/2025/abnt-alerta-para-distribuicao-nao-autorizada-de-norma-tecnica-sobre-exame-de-urina))); estruturar pelos itens públicos do PL 159; cláusula de LGPD para as fotos (a ferramenta é operadora, o engenheiro é controlador).

**Teste da rodada 2** (detalhes em [[Carteira de testes]]):
- **Variante barata, preferida:** formulário web do plano de reforma NBR 16280, até 30 fotos, **R$ 19 por Pix (Asaas)**, DOCX + PDF gerados no servidor; ~R$ 100 de anúncios exatos no cluster de reforma. **Passa:** ≥ 5 laudos pagos em 14 dias, ou ≥ 2 clientes que voltam. **Falha:** 0–1 laudo pago.
- **Se passar, teste completo de 21 dias (≤ R$ 500):** kits a R$ 47–97 e pré-venda de fundador a R$ 390/ano. **GO:** ≥ 10 kits e ≥ 3 pré-vendas. **KILL:** ≤ 2 kits e 0 pré-vendas depois de ≥ 250 cliques qualificados e ≥ 20 conversas, ou CPC mediano > R$ 5.

## Veredito

**Rodada 2: CONDICIONAL**, com a cunha nova e o teste por laudo. Não passa em todas as portas pela pesquisa de mesa e não deve ser morta pela pesquisa de mesa: só estranhos pagando fecham G1, G2, G4 e G8 ([[laudos_validation]], seção 6).

**Rodada 1:** CONDICIONAL. Vira GO se a pré-venda passar. As condições, da nota de verificação:
1. Publicar 3 modelos gratuitos estruturados pela norma (NBR 16747/autovistoria RJ, cautelar com estrutura IBAPE, recebimento de imóvel novo) e medir tráfego e conversão de modelo para cadastro **antes** do app completo.
2. Pré-vender **5–10 planos anuais** (~R$ 600–1.200/ano).
3. Diferenciar por saída **determinística e normativa**, não por IA.
4. **Gatilho de abandono:** menos de 5 pré-vendas em ~60 dias, ou visitantes dos modelos que recusam o upgrade pago.

## Notas de pesquisa

- [[laudos_validation]], seções 6 e 7 (rodada 2)
- [[Validação condicionais e novos focos]], seção "Laudos sobrevivem, mas a cunha muda"
- [[Oportunidade de produto validada 2026]], seção "Laudos de engenharia: lacuna real, pagamento ainda por provar"
- [[finalists_brazil_verification]], "Finalist 2" e "Scores and ranked verdicts"
- [[brazil_professional_niches]], candidato A (seções 1.8, 2 e 4)
- Relacionadas: [[Gerador de PTAM para corretores]] (mesma mecânica de SEO de modelo), [[Calendário de conformidade para síndicos]] (a inspeção predial está na lista de obrigações do síndico), [[Padrão - saturação]]
