---
tags:
  - projeto
  - decisoes
atualizado: 2026-10-12
---

# Registro de decisões

Voltar para [[00 Início]]. Mais recente no fim. Cada entrada traz o contexto, a decisão e o motivo.

> [!info] Sobre as datas
> O post de origem é de 10/10/2026. A análise do thread, a discussão das ideias de serviço e a pesquisa profunda aconteceram em 12/10/2026. A árvore de respostas foi salva às 16h46, as notas de pesquisa entre 16h54 e 18h01 e o relatório às 18h06, segundo os horários dos arquivos.
>
> As rodadas 2 e 3 também rodaram em 12/10/2026: as notas da rodada 2 foram salvas entre 18h59 e 19h49 e o relatório às 19h56; as notas da rodada 3, entre 20h00 e 20h14, segundo os horários dos arquivos.

---

### 10/10/2026: origem do projeto
- **Contexto:** o post de [[Thread X napoleaomp4|@napoleaomp4]], *"Se vc tivesse 700 reais e o Claude ilimitado, o que vc faria pra bater 5K dol?"*, com 153 mil visualizações.
- **Decisão:** usar o post como ponto de partida e levar a pergunta a sério, com o orçamento de ~R$ 700 e a meta de US$ 5 mil/mês.

### 12/10/2026: análise do thread
- **Contexto:** leitura de toda a árvore de respostas ([[Thread X napoleaomp4]]).
- **Conclusões:**
  - A resposta do "WebApp de direct response para Tier 1", elogiada pelo autor, **nunca foi explicada** e vive em nichos que a Meta restringe.
  - A **melhor ideia do thread** era um serviço para brasileiros empresários nos EUA.
  - **Responder leads rápido** é validado pela HBR: contato em até 1 hora deixa a empresa cerca de 7 vezes mais propensa a qualificar o lead.
  - **Revender contas do Claude** viola os termos da Anthropic.
  - **Servidor de GTA** e **"API pela metade do preço"** são inviáveis ([[Ideias inviáveis do thread]]).
- **Nota de ambiente:** a rede do ambiente de nuvem teve de ser trocada para **"Full"** antes de o x.com ficar acessível.

### 12/10/2026: ideias de serviço rejeitadas
- **Contexto:** as primeiras sugestões foram de serviço (agência para brasileiros empresários nos EUA, com landing page, Google Meu Negócio, tráfego pago e social media).
- **Decisão:** **rejeitar serviços.** O usuário não tem contatos, e serviço depende de prospecção e relacionamento.
- **Consequência:** o foco passa a ser **produto de software** vendido por tráfego pago e orgânico ([[Objetivo e restrições]]).

### 12/10/2026: premissas do produto fixadas
- **Decisão:** a IA faz parte da stack, mas **não é o produto** (*"não quero entregar IA pro cliente"*). Exigir disposição a pagar comprovada, mercado não saturado e algo que o Claude consiga construir.
- **Motivo:** produtos com IA no centro já estão lotados e quase não faturam ([[IA no centro do produto]]).

### 12/10/2026: pesquisa profunda em 8 frentes
- **Decisão:** rodar uma pesquisa com 6 frentes de exploração e 2 rodadas de verificação de finalistas ([[Índice da pesquisa]]):
  1. [[brazil_professional_niches]]: nichos profissionais brasileiros
  2. [[brazil_regulatory_demand]]: obrigações legais e fiscais no Brasil 2026–2027
  3. [[us_eu_regulatory_demand]]: prazos regulatórios nos EUA e na UE
  4. [[marketplace_gaps]]: lacunas em marketplaces e app stores
  5. [[verified_revenue_niches]]: nichos com receita verificada
  6. [[gtm_economics_payments]]: go-to-market, economia, pagamentos e impostos
  7. [[finalists_brazil_verification]]: teste de estresse de 4 finalistas brasileiros
  8. [[finalists_global_verification]]: teste de estresse de 4 finalistas globais

### 12/10/2026: resultado da pesquisa
- **Resultado:** **nenhuma candidata cumpre todos os critérios.** Na rodada final, 5 dos 8 finalistas morreram e 3 sobreviveram só sob condição ([[Ranking]]).
- **Recomendação principal:** [[Gerador de laudos de vistoria e inspeção]] (vistoria cautelar, recebimento de imóvel, inspeção predial NBR 16747), **condicionada a uma pré-venda de 60 dias** com gatilho de abandono.
- **Alternativas:** [[Cartas registradas online (EUA e Reino Unido)]] e um [[App Forge de Gantt para Jira]] em nicho estreito.
- **Critério de escolha adotado:** escolher a candidata **cuja dúvida restante custa menos para resolver**, e não a que tem mais evidência de receita. Nos laudos, a dúvida (engenheiros pagam por software?) se responde com ~R$ 400 e 60 dias, sem risco contratual nem câmbio. Nas cartas, a dúvida depende dos termos da Lob, da política do Paddle e de uma margem que não admite erros.
- **Estratégia de duas pernas:** pré-venda dos laudos (principal) e ticket com a Lob aberto hoje (secundária, custo zero).

### 12/10/2026: vault criado
- **Decisão:** organizar o projeto neste vault do Obsidian. O relatório e as notas foram movidos para `05 Pesquisa/` com `git mv`.

### 12/10/2026: instrução do usuário depois da rodada 1
- **Contexto:** a rodada 1 terminou sem vencedora limpa, com laudos, cartas e Jira como condicionais.
- **Instrução do usuário:** **resolver as ideias condicionais e continuar pesquisando até haver ideias aprovadas.**
- **Consequência:** abrir a rodada 2, com oito frentes que reverificaram as condicionais e abriram novos focos, e endurecer o filtro com as oito portas G1–G8 ([[Portões de aprovação]]).

### 12/10/2026: rodada 2, validação das condicionais e novos focos
- **Frentes:** [[laudos_validation]], [[certified_mail_validation]], [[unmet_feature_requests]], [[niche_exam_prep]], [[public_records_data]], [[portuguese_spanish_arbitrage]], [[brazil_emerging_platforms]] e [[trustmrr_newcomers]] (com o `trustmrr_newcomers.csv`). Relatório: [[Validação condicionais e novos focos]].
- **Resultado:** **nenhum dos mais de 60 candidatos passa nas oito portas.**
- **Condicionais da rodada 1:**
  - [[Gerador de laudos de vistoria e inspeção|Laudos]] seguem **CONDICIONAIS**, agora reprovados em G2 e G4 na pesquisa de mesa. A cunha muda para **laudo/plano de reforma NBR 16280 + vistoria de recebimento**, com o PL 159/2026 como bônus.
  - [[Cartas registradas online (EUA e Reino Unido)|Cartas]] → **MORTA** em G8. A LetterStream resolveu o bloqueio contratual com white-label por escrito, mas a taxa do USPS deixa US$ 6–11 por carta.
  - [[App Forge de Gantt para Jira|Jira Forge]] → **MORTO** em G2 e G8. Novatos com 0–29 instalações; a Katabarwa com 10+ apps em 0–2.
  - [[Feed de transportadoras recém-registradas (FMCSA)|FMCSA]] → **MORTA**: 8+ SaaS e 67 atores no Apify em 2026.
- **Doze condicionais novas**, a mais urgente sendo o [[Simulado do exame de corretor de seguros (SUSEP)|simulado de corretor de seguros]] (inscrições até 23/11/2026).
- **Conclusão de método:** a pesquisa de mesa não aprova G1 e G2 juntos; só dinheiro de desconhecidos fecha ([[Padrão - pesquisa de mesa não aprova G1 e G2]]).
- **Recomendação do relatório:** uma carteira de três testes pagos (corretor, laudos por laudo e .p7m para a Itália), com cerca de R$ 650 e limiares fixados antes.

### 12/10/2026: rodada 3, análogos brasileiros e provas de nicho
- **Frentes:** [[exam_prep_deep]], [[brazil_regulated_documents]] e [[trustmrr_br_pt_mapping]]. A rodada não teve relatório próprio; o resumo foi escrito em [[Rodada 3 - resumo]].
- **Resultado:** **nenhuma ideia aprovada.**
- **Mudanças:**
  - **SUSEP → MORTA como aposta de US$ 5 mil/mês:** o painel da SUSEP mostra ~4,8 mil novos corretores PF por ano, e o teto realista é de US$ 0,6–1,5 mil/mês. Fica como teste opcional de caixa.
  - [[Simulado do exame de despachante aduaneiro dos EUA (CBLE)|CBLE]] → **CONDICIONAL nº 1, 27/35**, a melhor nota das três rodadas. Teste: simulado grátis até 10/11/2026 e pré-venda de US$ 149.
  - [[Preparatório do teste de nacionalidade portuguesa|Nacionalidade portuguesa]] → **CONDICIONAL nº 2**: regulamentação não publicada, concorrente lançado em agosto, Paddle proíbe preparatórios.
  - Novas condicionais: [[Gerador de parecer descritivo da educação infantil|parecer descritivo]] (teste de R$ 200 antes de 10/11/2026), [[Software para empresas de manutenção de extintores|software para extintores]] (exige prospecção ativa, em conflito com a restrição de não ter contatos) e [[Conversor de versões do SketchUp (PT e ES)|conversor do SketchUp]] (depende do SDK da Trimble).
  - KILLs em [[Armadilhas e ideias mortas]], seção 2.

### 12/10/2026: carteira de testes adotada como próximo passo
- **Decisão:** parar de buscar ideias no papel e executar a [[Carteira de testes]], em ordem de urgência de prazo: parecer descritivo, CBLE, SUSEP (opcional), laudos por laudo, .p7m, Portugal (no gatilho da regulamentação) e SketchUp (no gatilho do SDK). Antes, as checagens de custo zero.
- **Regras:** limiares fixados antes; o primeiro teste que passar ganha foco total; nenhuma empresa aberta antes de um teste passar.
- **Motivo:** depois de três rodadas, a evidência que falta só existe depois de um pagamento. A pergunta passou a ser "qual dúvida restante custa menos para virar dado?".
- **Status aposentados:** `recomendada` e `alternativa` deixam de ser usados até um teste pago passar ([[Ranking]]).

### Pendente: aprovação do usuário para executar a carteira
- **Próximo passo:** o usuário confirma a carteira e as decisões abertas: o orçamento acima de R$ 700, a exceção da SUSEP e se aceita prospecção ativa para extintores. Depois, abre as contas e roda as checagens de custo zero. Ver [[Próximos passos]].
