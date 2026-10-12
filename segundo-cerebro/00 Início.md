---
tags:
  - hub
  - moc
atualizado: 2026-10-12
---

# Início: segundo cérebro do projeto

> [!abstract] Objetivo
> Achar, validar e vender um **produto de software** que resolva uma dor real de um comprador com poder de compra, rumo a **US$ 5 mil/mês** (cerca de R$ 27 mil, na taxa de ~R$ 5,4/US$ usada na pesquisa). O ponto de partida é **cerca de R$ 700 (~US$ 130)**, **nenhum cliente, nenhum contato** e Claude Code para construir. A IA entra na stack, **não é o produto**. Detalhes em [[Objetivo e restrições]].

## Status atual (12/10/2026)

> [!warning] Nenhuma candidata cumpre todos os critérios
> A pesquisa profunda (8 frentes, 12/10/2026) terminou sem uma vencedora limpa. Onde há prova forte de pagamento, há concorrência. Onde não há concorrência, falta prova de pagamento.

| Papel | Ideia | Veredito | Por que |
|---|---|---|---|
| **Aposta principal** | [[Gerador de laudos de vistoria e inspeção]] | CONDICIONAL (21/35) | Lacuna real em laudos de engenharia; o que falta (prova de pagamento) se testa com R$ 300–400 em 60 dias |
| Alternativa 1 | [[Cartas registradas online (EUA e Reino Unido)]] | CONDICIONAL (21/35) | Melhor prova de receita de estreantes, mas margem fina e bloqueios contratuais |
| Alternativa 2 | [[App Forge de Gantt para Jira]] | CONDICIONAL, só nicho estreito (22/35) | Comprador em dólar, mas mercado lotado e início frio |
| Próxima a verificar | [[Feed de transportadoras recém-registradas (FMCSA)]] | Não testada na rodada final | Concorrente com receita verificada sobre dados públicos |

A estratégia recomendada tem **duas pernas**:
1. **Pré-venda dos laudos** com prazo e gatilho de abandono explícito ([[Protocolo de validação]]).
2. **Ticket na Lob hoje**, que não custa nada, para destravar as cartas se os laudos falharem.

## Próximo passo

> [!tip] Agora
> **Discutir os achados com o usuário** e decidir se ele aceita a estratégia de duas pernas. Depois, seguir a checklist em [[Próximos passos]].

## Mapa do vault

- **01 Projeto**
  - [[Objetivo e restrições]]: meta, restrições e os 7 critérios
  - [[Registro de decisões]]: o que foi decidido, quando e por quê
  - [[Próximos passos]]: checklist
- **02 Oportunidades**
  - [[Ranking]]: tabela com todas as 51 ideias avaliadas, com link para cada nota
- **03 Armadilhas**
  - [[Armadilhas e ideias mortas]]: tudo o que morreu, com motivo e evidência
  - Padrões de morte: [[Padrão - governo entrega de graça]], [[Padrão - plataforma absorve o recurso]], [[Padrão - saturação]]
  - [[IA no centro do produto]] e [[Ideias inviáveis do thread]]
- **04 Execução**
  - [[Protocolo de validação]]: pré-venda de 60 dias e regras de decisão
  - [[Canais de aquisição]]: SEO de documento, anúncio pontual, conversa 1:1, marketplaces
  - [[Pagamentos e impostos]]: CPF → ME no Simples, Asaas, Paddle, Fator R
  - [[Expectativas e prazos]]: quanto tempo leva de verdade
- **05 Pesquisa**
  - [[Índice da pesquisa]]: o relatório final e as 8 notas de pesquisa
  - Relatório: [[Oportunidade de produto validada 2026]]
- **06 Fontes**
  - [[Thread X napoleaomp4]]: o post que originou o projeto, com a árvore completa de respostas
- [[07 Glossário]]: MRR, CAC, Merchant of Record, Fator R, PTAM, NBR 16747, NubeSDK, Forge e outros

## Como usar este vault

> [!info] Abrir no Obsidian
> O vault mora na pasta `segundo-cerebro/` do repositório **github.com/MarceloVichar/facebook-login**, branch **`ccr-f72cc16f-9urhz1`**.
>
> 1. Clone o repositório já na branch certa:
>    ```bash
>    git clone -b ccr-f72cc16f-9urhz1 https://github.com/MarceloVichar/facebook-login.git
>    ```
>    Se você já tem o clone, atualize:
>    ```bash
>    git fetch origin
>    git checkout ccr-f72cc16f-9urhz1
>    git pull
>    ```
> 2. No Obsidian, escolha **"Open folder as vault"** ("Abrir pasta como cofre") e selecione `facebook-login/segundo-cerebro`.
> 3. Comece por esta nota. As notas usam wikilinks `[[...]]`, tags (`#status/recomendada`, `#mercado/br`…) e propriedades YAML (`status`, `score`, `mercado`, `fonte`) que aparecem no painel de propriedades.

Convenções:
- **Pontuação** em escala 1–5 por critério, total sobre 35. As notas de rodadas diferentes foram feitas por pesquisadores diferentes, então compare totais **dentro da mesma rodada**. A rodada final prevalece sobre as anteriores.
- **Status:** `recomendada`, `alternativa`, `condicional` (viva, mas sem validação), `morta` (eliminada por evidência) e `armadilha` (soa boa, mas está lotada ou é inviável).
- Os números vêm das fontes citadas, com as URLs originais. Onde a pesquisa fez inferência ou estimativa, a nota diz.
- O arquivo `.obsidian/workspace.json` está no `.gitignore`, para o estado local da interface não gerar conflito no `git pull`.
