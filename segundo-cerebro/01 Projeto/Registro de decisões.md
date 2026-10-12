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

### Pendente: discutir os achados com o usuário
- **Próximo passo:** apresentar o resultado, confirmar ou rejeitar a estratégia de duas pernas e só então iniciar a semana 1 do [[Protocolo de validação]]. Ver [[Próximos passos]].
