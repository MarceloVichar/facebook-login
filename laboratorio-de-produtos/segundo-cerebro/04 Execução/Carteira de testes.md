---
tags:
  - execucao
  - validacao
  - carteira
atualizado: 2026-10-12
fonte:
  - "[[Validação condicionais e novos focos]]"
  - "[[Rodada 3 - resumo]]"
  - "[[laudos_validation]]"
  - "[[exam_prep_deep]]"
  - "[[brazil_regulated_documents]]"
  - "[[trustmrr_br_pt_mapping]]"
  - "[[trustmrr_newcomers]]"
---

# Carteira de testes

Voltar para [[00 Início]] · [[Próximos passos]] · [[Ranking]].

> [!important] Por que existe esta nota
> Três rodadas de pesquisa e **nenhuma ideia aprovada**. A pesquisa de mesa não consegue fechar G1 e G2 juntos: só **dinheiro de desconhecidos** fecha ([[Padrão - pesquisa de mesa não aprova G1 e G2]], [[Portões de aprovação]]). Esta é a carteira de testes reais e baratos que transforma as condicionais em dado, **em ordem de urgência de prazo**. Ela junta a carteira recomendada da [[Validação condicionais e novos focos|rodada 2]] com os testes da [[Rodada 3 - resumo|rodada 3]]. Os limiares de passa/falha vêm das notas de pesquisa; onde as notas não definem algo, esta nota diz "não definido" e propõe uma regra para o usuário aprovar.

## As regras (valem para todos os testes)

> [!warning] Regras fixas
> 1. **Os limiares são fixados antes de começar** e não mudam no meio do teste. Só conta dinheiro de desconhecidos: amigos, família e "vou comprar quando sair" não contam.
> 2. **O primeiro teste que passar ganha foco total.** Os outros param (anúncios pausados), e o dinheiro que sobrar vai para construir o MVP para quem pagou, com reembolso automático se a entrega atrasar e o direito de arrependimento de 7 dias do art. 49 do CDC ([CDC](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm)).
> 3. **Nenhuma empresa é aberta antes de um teste passar**, e nenhuma conta em dólar é paga antes disso. Todos os testes da carteira funcionam no CPF (Asaas, Hotmart, Kiwify, Gumroad) ou com um merchant of record que aceita software (Paddle, só no .p7m). Ver [[Padrão - pagamento e CNPJ bloqueiam rotas]].
> 4. **Se todos falharem,** a próxima rodada não busca ideias novas no papel: repete o mesmo protocolo nas condicionais restantes, em ordem de custo do teste. Zero pagantes em todas as frentes também é resultado: indica que a restrição real é a distribuição, e a decisão passa a ser construir audiência ou SEO por 6–12 meses ([[Validação condicionais e novos focos]], conclusão).
>
> **Como ler zero vendas:** pela regra de três, zero vendas em *n* cliques limitam a conversão real a menos de 3/*n*. Zero em 250 cliques significa menos de 1,2% ([Rule of three](https://en.wikipedia.org/wiki/Rule_of_three_(statistics))).

> [!question] Exceção proposta (o usuário confirma)
> O teste da **SUSEP** é só de caixa: mesmo que passe, o teto de G8 continua em US$ 0,6–1,5 mil/mês ([[exam_prep_deep]]). Proposta: **um "passa" na SUSEP não dispara a regra 2**; o dinheiro entra como reforço de orçamento para os outros testes.

## Visão geral, por urgência de prazo

| Ordem | Teste | Custo | Janela ou prazo | Decisão em | Porta que resolve |
|---|---|---|---|---|---|
| 0 | [[#0. Checagens de custo zero]] | R$ 0 (+ US$ 1) | semana de 12/10/2026 | antes de gastar | G4, G7, G8 |
| 1 | [[#1. Parecer descritivo da educação infantil]] | R$ 200 | **anúncios no ar antes de 10/11/2026** | até 15/12/2026 | G1, G2, G4, G8 |
| 2 | [[#2. Simulado do CBLE]] | US$ 80 + US$ 1 | **simulado publicado até 10/11/2026**; anúncios 11/11–20/12 | 31/12/2026 (ou 15/04/2027) | G1, G2, G8 |
| 3 | [[#3. Pré-venda SUSEP (opcional)]] | R$ 150 | 20/10 a **23/11/2026** | 23/11/2026 | caixa (G8 já falhou) |
| 4 | [[#4. Laudos: gerador por laudo]] | ~R$ 100–150 | 14 dias, assim que o formulário ficar pronto | dia 14 | G1, G2, G4 |
| 5 | [[#5. Visualizador de p7m para a Itália]] | € 40 | novembro, ~14 dias | dia 14 | G4, G8 |
| 6 | [[#6. Teste de nacionalidade portuguesa]] | € 40 | **gatilho:** publicação da regulamentação | 21 dias depois do lançamento | G1, G4 |
| 7 | [[#7. Conversor de versões do SketchUp]] | ≈ R$ 200 | **gatilho:** aprovação do SDK da Trimble (até 14 dias) | 21 dias depois do lançamento | G5, G7, G1 |

## Orçamento

| Item | Custo | Observação |
|---|---|---|
| Parecer descritivo | R$ 200 | Google Ads |
| CBLE | US$ 80 + US$ 1 | ≈ R$ 437 pelo câmbio de referência do projeto (R$ 5,4/US$), sem IOF nem taxa de cartão internacional |
| SUSEP (opcional) | R$ 150 | Google Ads |
| Laudos por laudo | ~R$ 100–150 | Google Ads; o teste completo de 21 dias (≤ R$ 500) só se este passar |
| p7m | € 40 | Conversão para reais não cotada nas notas |
| Portugal | € 40 | Só depois do gatilho |
| SketchUp | ≈ R$ 200 (R$ 150 de anúncios) | Só depois da aprovação do SDK; custo da VM Windows não cotado |
| Domínio | estimativa de R$ 40–100/ano, não recotada | Um único domínio com subdomínios para os testes brasileiros reduz o gasto |

> [!warning] A soma passa de R$ 700
> Só parecer + CBLE + laudos já somam ~R$ 737–787, antes do domínio. A carteira não estoura porque **os testes são sequenciais e condicionais**: pela regra 2, um "passa" encerra os demais, e os testes 5–7 só gastam se os anteriores falharem ou se houver receita. O relatório da rodada 2 já previa que o CBLE seria **"pago com receita dos testes"**. Opções para o usuário decidir antes de 10/11:
> - reduzir os laudos ao piso de R$ 100 e usar um único domínio;
> - pular a SUSEP (é opcional);
> - financiar os anúncios do CBLE com a receita da SUSEP ou dos laudos, se houver.

---

## 0. Checagens de custo zero

Fazer **antes de qualquer gasto**, na semana de 12/10/2026. Cada uma pode cancelar um teste sem gastar nada.

| # | Checagem | Quem faz | Corta o quê |
|---|---|---|---|
| Z1 | **Keyword Planner:** volume e CPC de todas as palavras-chave dos testes 1–7 | **Você:** criar a conta no Google Ads (exige cartão). **Claude:** monta as listas de palavras-chave e lê os resultados com você | Laudos: descartar palavra com lance de topo > R$ 5; CPC mediano > R$ 4 corta o cluster C; > R$ 5 mata o teste. Parecer: CPC > R$ 1,50 é o limiar de falha. p7m: CPC > €0,80 cancela (trocar pelo [[Feed semanal de novas práticas de saúde (NPPES)|NPPES]], US$ 50). SketchUp: CPC > R$ 2,00 é falha. SUSEP: o critério da rodada 2 era ≥ 2 mil buscas/mês somando "simulado / prova / curso corretor de seguros" |
| Z2 | **Pedidos via LAI no Fala.BR** à SUSEP e à FGV: inscritos e aprovados por edição do exame de corretor, e a divisão entre rota de exame e rota de curso, 2023–2026 | **Você:** protocolar com login gov.br. **Claude:** redige os pedidos | Refina o universo da SUSEP (o painel já mostra ~4,8 mil novos corretores PF por ano). O prazo legal de resposta é de 20 dias, prorrogáveis por 10 (Lei 12.527/2011, art. 11) |
| Z3 | **Alerta no Diário da República** e na página do IRN para a alteração do Regulamento da Nacionalidade, conferido toda semana | **Você:** cadastrar o alerta. **Claude:** confere a página do IRN a cada sessão, se pedido | É o gatilho do teste 6 |
| Z4 | **Pedido de acesso ao C SDK da Trimble** e leitura dos termos | **Você:** pedir com a sua conta Trimble. **Claude:** redige a justificativa do pedido e lê os termos com você | É o gatilho do teste 7. Para se não houver aprovação em 14 dias ou se os termos proibirem serviço hospedado |
| Z5 | **Teste de repasse de US$ 1 no Gumroad:** criar um produto de US$ 1, comprar com o próprio cartão e confirmar a chegada via PayPal ao Brasil | **Você:** contas Gumroad e PayPal no seu nome. **Claude:** acompanha e registra taxas e prazo | Se o dinheiro não chegar, CBLE e Portugal ficam sem rota de pagamento (G7) |

---

## 1. Parecer descritivo da educação infantil

Nota: [[Gerador de parecer descritivo da educação infantil]] · fonte: [[brazil_regulated_documents]], Q6-B.

- **Hipótese:** professoras de educação infantil (ou escolas) pagam **R$ 19,90 por um passe semestral** que monta, sem IA, os pareceres da turma inteira a partir de um checklist dos campos de experiência da BNCC.
- **Custo:** R$ 200 de Google Ads (mais o domínio).
- **Prazo:** **anúncios no ar antes de 10/11/2026**, para pegar o pico de fim do 2º semestre. Decisão até **15/12/2026**. Se perder a janela, o próximo pico é junho de 2027.

**Passos**
1. **Até 19/10:** Keyword Planner (Z1) para "relatório descritivo educação infantil 5 anos segundo semestre", "parecer descritivo educação infantil 5 anos de acordo com a bncc" e variações. Se o CPC estimado já passar de R$ 1,50, não lançar: é o limiar de falha.
2. **13/10 a ~02/11:** Claude constrói o MVP de **uma faixa etária (5 anos, 2º semestre)**:
   - banco de frases original por campo de experiência, com códigos da BNCC;
   - checklist por criança, parecer por criança e exportação da turma em PDF/Word atrás do paywall;
   - página de SEO com **20 pareceres de exemplo**;
   - aviso LGPD (dados mínimos; consentimento da escola);
   - checkout no Asaas a R$ 19,90 (Pix e cartão) com webhook que libera a exportação.
3. **Até 10/11:** anúncios no ar, em correspondência exata, ~R$ 10/dia.
4. **Revisão no meio:** pausar grupos de anúncio sem nenhum checkout iniciado.
5. **Até 15/12:** decisão (ou antes, ao atingir 250 cliques).

| Você faz | Claude constrói |
|---|---|
| Conta no Asaas (CPF); conta e cartão no Google Ads; domínio; revisar o banco de frases como falante nativo | Banco de frases, app web, PDF/Word, página de SEO, checkout e webhook, anúncios e palavras negativas, painel de resultados |

- **Passa:** CPC ≤ R$ 0,80 **e** ≥ 8 passes pagos (≥ 3% de ≥ 250 cliques) antes de 15/12/2026.
- **Falha:** ≤ 2 vendas, ou CPC > R$ 1,50.
- **Entre os dois** (3–7 vendas, ou CPC entre R$ 0,80 e R$ 1,50): não definido na nota. Proposta: um ciclo extra de 7 dias, como na regra "iterar" do [[Protocolo de validação]].
- **Gatilhos de morte:** CPC > R$ 1,50 (no Keyword Planner ou no teste); ≤ 2 vendas até 15/12.
- **Se passar:** planos escolares (modelo Tifox) e as outras faixas etárias antes do pico de junho de 2027.

## 2. Simulado do CBLE

Nota: [[Simulado do exame de despachante aduaneiro dos EUA (CBLE)]] · fonte: [[exam_prep_deep]], Q5-A.

- **Hipótese:** quem reprovou ou vai fazer o CBLE paga **US$ 149 de pré-venda** por um simulador interativo e cronometrado, construído sobre as provas públicas da CBP.
- **Custo:** US$ 80 de Google Ads mais US$ 1 do teste de repasse.
- **Prazo:** simulado grátis publicado **até 10/11/2026** (os resultados da prova de 28/10 saem em 2–3 semanas, por volta de 11–18/11). Anúncios de 11/11 a 20/12/2026. Decisão em **31/12/2026**, com uma segunda leitura em **15/04/2027**.

**Passos**
1. **Antes de construir:** Z5, o teste de repasse de US$ 1 no Gumroad. Se falhar, parar.
2. **Até 10/11:** Claude constrói o simulado grátis da **prova de abril de 2026** com o gabarito da CBP: 80 questões, 4,5 horas, linha de 75% e aviso de "a até 3 questões: pode recorrer". Sem cadastro.
3. **Até 10/11:** pré-venda no Gumroad, "April 2027 Simulator – US$ 149 founder price", com data de entrega e reembolso se atrasar.
4. **11/11 a 20/12:** US$ 80 de Google Ads nos EUA ("cble past exams", "customs broker exam practice test"). Posts orgânicos no Reddit e em grupos de despachantes no LinkedIn.
5. **31/12:** primeira decisão. **15/04/2027:** segunda leitura.

| Você faz | Claude constrói |
|---|---|
| Contas Gumroad e PayPal; teste de US$ 1; Google Ads com segmentação EUA; posts no Reddit e no LinkedIn com suas contas | Extração das questões e do gabarito do PDF da CBP, simulado cronometrado, página em inglês, produto no Gumroad, anúncios, painel de conclusões |

- **Passa:** ≥ 150 simulados grátis concluídos **e** ≥ 8 pré-encomendas pagas até 31/12/2026, **ou** ≥ 25 pagas até 15/04/2027.
- **Falha:** < 3 pagas até 31/12/2026 → KILL.
- **Gatilhos de morte:** o teste de repasse falha; < 3 pagas até 31/12.
- **Se passar:** produto completo até a prova de abril de 2027 (as cinco provas, ~400 questões, treinos de consulta ao 19 CFR e ao HTSUS, repetição espaçada). O teto continua sendo o universo de ~2,2 mil examinandos por ano.

## 3. Pré-venda SUSEP (opcional)

Nota: [[Simulado do exame de corretor de seguros (SUSEP)]] · fontes: [[exam_prep_deep]], Q5-C; [[niche_exam_prep]], Q7.

- **Hipótese:** candidatos ao exame FGV de dezembro pagam **R$ 197** por um pacote de simulados no formato da prova.
- **Custo:** R$ 150 de Google Ads.
- **Prazo:** de **20/10 a 23/11/2026**, quando fecham as inscrições. A prova é em 5–6/12/2026.

**Passos**
1. **Até 19/10:** Z1 (Keyword Planner) e Z2 (LAI). Se as buscas somarem menos de 2 mil/mês, pular o teste.
2. **Até 20/10:** Claude constrói a página com um **diagnóstico grátis de 20 questões** (Danos), cada uma citando o artigo de lei ou a circular, e o produto "Pacote Dezembro 2026" a R$ 197 no Hotmart.
3. **20/10 a 23/11:** R$ 150 de Google Ads em "simulado susep" e "prova susep fgv 2026".
4. **Se vender:** Claude entrega os simulados antes da prova de 5–6/12 (o motor sai em menos de 4 semanas; o gargalo são 600–900 questões citadas). Se não der para entregar a tempo, reembolso integral.

| Você faz | Claude constrói |
|---|---|
| Conta no Hotmart (CPF); Google Ads; pedido LAI | Diagnóstico, banco de questões com citação conferida contra o texto oficial, simulados no formato FGV (70% no conjunto, sem zerar disciplina), página e anúncios |

- **Passa:** ≥ 10 vendas. (A rodada 2 pedia também ≥ 5% dos visitantes deixando e-mail.)
- **Falha:** < 3 vendas.
- **Gatilho de morte:** < 2 mil buscas/mês no Keyword Planner, ou < 3 vendas até 23/11.
- **Mesmo que passe, o teto de G8 não muda:** é dinheiro rápido, não o negócio de US$ 5 mil/mês.

## 4. Laudos: gerador por laudo

Nota: [[Gerador de laudos de vistoria e inspeção]] · fonte: [[laudos_validation]], seções 6 e 7.

- **Hipótese:** engenheiros e arquitetos pagam **R$ 19 por Pix** por um laudo/plano de reforma **NBR 16280** gerado em DOCX + PDF a partir de um formulário com fotos. O teste prova disposição a pagar pelo **uso**, não por um arquivo de Word.
- **Custo:** ~R$ 100–150 (cerca de R$ 10/dia × 10 dias de anúncios no cluster de reforma).
- **Prazo:** 14 dias a partir do lançamento. O formulário fica pronto em 5–7 dias. Não depende de calendário externo, então pode rodar logo depois de o parecer entrar no ar.

**Passos**
1. **Keyword Planner** (Z1) para as palavras do cluster A: "modelo de laudo de reforma de apartamento", "laudo de reforma modelo", "plano de reforma nbr 16280 modelo", "laudo nbr 16280", "art de reforma modelo", "como fazer um laudo de reforma" e as demais da tabela de [[laudos_validation]]. Descartar palavra com lance de topo acima de R$ 5. Se o CPC mediano passar de R$ 5, o teste morre antes de começar.
2. **Dias 0–7:** Claude constrói o formulário web:
   - sem app e sem modo offline;
   - campos do plano de reforma e upload de até 30 fotos, com compressão;
   - DOCX + PDF gerados no servidor;
   - checkout de R$ 19 no Asaas com webhook;
   - bloco "você assina e emite sua ART; a ferramenta só monta o documento";
   - aviso LGPD;
   - nenhum texto copiado de NBR.
3. **Dias 7–21:** anúncios em correspondência exata, com as negativas da nota (veicular, locação, aluguel, "grátis", "download", "abnt pdf" e outras).
4. **Dia 21:** decisão.

| Você faz | Claude constrói |
|---|---|
| Conta no Asaas (CPF); Google Ads; domínio; responder dúvidas de quem comprar | Formulário, gerador DOCX/PDF, checkout e webhook, página com exemplo em PDF com marca d'água, anúncios e negativas, painel de eventos (visita → clique em comprar → checkout → pago) |

- **Passa:** ≥ 5 laudos pagos em 14 dias, **ou** ≥ 2 clientes que voltam para um segundo laudo.
- **Falha:** 0–1 laudo pago.
- **Entre os dois** (2–4 laudos): não definido na nota. Proposta: tratar como "iterar" ([[Protocolo de validação]]).
- **Gatilhos de morte:** CPC mediano > R$ 5; 0–1 laudo pago em 14 dias.
- **Se passar:** teste completo de 21 dias (≤ R$ 500), com kits de R$ 47–97 e pré-venda de fundador a R$ 390/ano. **GO:** ≥ 10 kits **e** ≥ 3 pré-vendas (ou ≥ 5 pacotes de créditos), ou conversão paga ≥ 3% dos cliques com ≥ 1 pré-venda. **KILL:** ≤ 2 kits e 0 pré-vendas depois de ≥ 250 cliques qualificados e ≥ 20 conversas, ou CPC mediano > R$ 5.

## 5. Visualizador de p7m para a Itália

Nota: [[Visualizador de p7m para a Itália]] · fonte: [[trustmrr_newcomers]], candidato A.

- **Hipótese:** usuários italianos pagam **€3,99 por arquivo ou €12,99 por ano** a um novato por um visualizador de .p7m no navegador, sem upload, apesar das ferramentas grátis.
- **Custo:** € 40 de Google Ads na Itália.
- **Prazo:** novembro de 2026, ~14 dias.

**Passos**
1. **Z1:** se o CPC na Itália passar de €0,80, cancelar e rodar o teste do [[Feed semanal de novas práticas de saúde (NPPES)|NPPES]] (US$ 50) no lugar, como indica o relatório da rodada 2.
2. **Até 7 dias:** Claude constrói o visualizador:
   - leitura do envelope CAdES no navegador, extração do PDF e dados do signatário;
   - aviso explícito de que **não é verificação jurídica da assinatura**;
   - cinco páginas em italiano ("aprire file p7m", "p7m in pdf", "fattura elettronica p7m" e outras).
3. **Venda por merchant of record** (VAT europeu): o Paddle aceita software.
4. **~14 dias:** €40 de anúncios e decisão.

| Você faz | Claude constrói |
|---|---|
| Conta no Paddle (aprovação é condição); Google Ads com segmentação Itália | Visualizador, páginas em italiano, integração com o Paddle, anúncios |

- **Passa:** CPC ≤ €0,40 **e** ≥ 1 conversão paga a cada 80 cliques.
- **Falha:** zero vendas com os €40, ou CPC > €0,80.
- **Gatilhos de morte:** CPC > €0,80 no Keyword Planner; o Paddle recusar a conta; zero vendas.

## 6. Teste de nacionalidade portuguesa

Nota: [[Preparatório do teste de nacionalidade portuguesa]] · fontes: [[exam_prep_deep]], Q5-B; [[portuguese_spanish_arbitrage]].

- **Hipótese:** brasileiros que vão pedir a nacionalidade portuguesa pagam **€9,90 de pré-venda** por um preparatório da nova prova de cultura, história, símbolos e organização do Estado.
- **Custo:** € 40 (€ 25 de Google Ads, mais grupos do Facebook).
- **Gatilho:** a publicação da regulamentação (Z3). A rodada 2 pôs este teste como "gatilho"; a rodada 3 diz que a lista de espera poderia começar já. **Padrão desta carteira: esperar o gatilho**, porque antes dele o universo de compradores é quase zero e advogados orientam não protocolar.

**Passos (depois do gatilho)**
1. Claude lê a portaria e ajusta o formato dos simulados ao oficial.
2. Claude publica uma página em pt-BR com lista de espera, diagnóstico grátis de 20 questões e pré-venda de €9,90 (Hotmart ou Gumroad).
3. Você posta em 3–5 grupos de brasileiros em Portugal no Facebook; €25 de Google Ads.
4. Decisão em 21 dias.

| Você faz | Claude constrói |
|---|---|
| Alerta no DRE (Z3); conta Gumroad ou Hotmart; posts nos grupos | Banco de questões citadas (~400), diagnóstico, simulados, página, anúncios |

- **Passa (21 dias):** ≥ 300 inscritos na lista **e** ≥ 15 pré-vendas.
- **Falha:** < 100 inscritos ou < 5 pré-vendas.
- **Gatilhos de morte:**
  - a regulamentação isentar nacionais da CPLP da prova cívica;
  - o Estado publicar banco de questões ou app oficial grátis;
  - o testenacionalidade.com passar de 10 mil instalações no Play antes do lançamento.

## 7. Conversor de versões do SketchUp

Nota: [[Conversor de versões do SketchUp (PT e ES)]] · fonte: [[trustmrr_br_pt_mapping]], candidato A.

- **Hipótese:** usuários brasileiros de SketchUp pagam **R$ 19,90 por arquivo** para abrir um .skp novo numa versão antiga.
- **Custo:** ≈ R$ 200 (R$ 150 de Google Ads em 5 buscas exatas). O custo da VM Windows não foi cotado.
- **Gatilho:** aprovação do C SDK da Trimble (Z4) em até 14 dias, com termos que permitam serviço hospedado. A nota diz que a página pode rodar em paralelo com entrega manual. **Padrão desta carteira: só gastar depois do SDK**, para não validar algo que não se pode construir.

**Passos (depois do gatilho)**
1. Claude publica a página em pt-BR para "converter sketchup versão anterior online", com checkout de R$ 19,90 por arquivo (Pix e cartão).
2. Durante o teste, a entrega é **manual**, com prazo de até 2 horas avisado na página: você converte com uma cópia licenciada do SketchUp ou pelo 3D Warehouse.
3. R$ 150 de anúncios nas 5 buscas exatas; decisão em 21 dias.

| Você faz | Claude constrói |
|---|---|
| Pedido do SDK; licença do SketchUp ou rota do 3D Warehouse para a entrega manual; Asaas; Google Ads | Página, checkout, anúncios; depois de um "passa", o CLI em C++ e o worker Windows |

- **Passa:** CPC ≤ R$ 1,00 **e** ≥ 5 pedidos pagos em ≤ 250 cliques.
- **Falha:** ≤ 1 pedido, ou CPC > R$ 2,00.
- **Gatilhos de morte:** SDK negado ou sem resposta em 14 dias; termos que proíbem serviço hospedado; CPC > R$ 2,00.

---

## Fora da carteira, e por quê

| Ideia | Motivo |
|---|---|
| [[Software para empresas de manutenção de extintores]] | O único teste é prospecção ativa a 150 empresas do cadastro do Inmetro, **em conflito com a restrição de não ter contatos**. Entra só se o usuário aceitar esse canal |
| [[Feed semanal de novas práticas de saúde (NPPES)]] | Substituto do p7m se o CPC na Itália for proibitivo |
| [[Software de condomínio autogerido em Portugal]] | G4 fraco: "grátis" domina; o canal que funcionou para o concorrente foi telefone |
| [[Lucro por live e comissão de host no TikTok Shop]] | Exige CNPJ antes de vender; nenhum pagante visível |
| [[Feed de licenças de bebida e restaurantes (EUA)]], [[Vencedores do PNCP para corretores de seguro-garantia]] | Dependem de e-mail frio; G1 não provado |
| [[Merge de tickets para Jira Service Management]], [[Compartilhamento externo de dashboards do Jira]] | 3–5 meses até o primeiro pagamento; G2 e G8 fracos |
| [[Simulado do Exame de Suficiência do CFC]] | Data da edição 2027.1 não publicada; categoria lotada; ticket de R$ 130 |
| [[Matemática para exames de operadores de água e esgoto (EUA)]] | Nenhum pagante visível |
| [[Cartas registradas online (EUA e Reino Unido)]] | Morta em G8; o teste opcional de US$ 100 para carta ao IRS não é recomendado |

## Registro de resultados

Preencher à medida que cada teste roda. Só desconhecidos contam.

| Teste | Início | Fim | Gasto | Cliques | CPC médio | Vendas | Passa/Falha | Decisão |
|---|---|---|---|---|---|---|---|---|
| Z1–Z5 |  |  | R$ 0 / US$ 1 | — | — | — |  |  |
| 1. Parecer |  |  |  |  |  |  |  |  |
| 2. CBLE |  |  |  |  |  |  |  |  |
| 3. SUSEP |  |  |  |  |  |  |  |  |
| 4. Laudos |  |  |  |  |  |  |  |  |
| 5. p7m |  |  |  |  |  |  |  |  |
| 6. Portugal |  |  |  |  |  |  |  |  |
| 7. SketchUp |  |  |  |  |  |  |  |  |

## Relacionadas

[[Protocolo de validação]] · [[Canais de aquisição]] · [[Pagamentos e impostos]] · [[Registro de decisões]]
