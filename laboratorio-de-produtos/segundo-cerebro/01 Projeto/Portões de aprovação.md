---
tags:
  - projeto
  - criterios
atualizado: 2026-10-12
fonte:
  - "[[Validação condicionais e novos focos]]"
  - "[[Rodada 3 - resumo]]"
---

# Portões de aprovação (G1–G8)

Voltar para [[00 Início]] · [[Objetivo e restrições]] · [[Ranking]].

> [!abstract] A regra
> A partir da rodada 2, uma ideia só é **APROVADA** se passar pelas **oito portas ao mesmo tempo**. A pontuação de 1–5 em sete critérios (total sobre 35) continua servindo para ordenar dentro de cada frente, mas **quem decide é a porta reprovada, não o total** ([[Validação condicionais e novos focos]]).

## As oito portas

| Porta | O que exige | Como a pesquisa verifica |
|---|---|---|
| **G1** Disposição a pagar | Pelo menos **dois concorrentes pagos** que provem que alguém paga pelo trabalho | Páginas de preço, receita verificada no TrustMRR, avaliações em marketplaces |
| **G2** Mercado não saturado | Mercado sem multidão **e** prova de que um **recém-chegado ainda consegue faturar** | Censo de concorrentes (lojas de apps, Hotmart, Apify, Play Store), data de fundação e tração dos novatos |
| **G3** Poder de compra | O comprador tem dinheiro e costuma pagar por ferramenta | Honorários, taxas de exame, perfil do comprador |
| **G4** Distribuição sem contatos | Dá para chegar ao comprador por busca, anúncio ou marketplace, sem rede de relacionamento | Autocomplete do Google (sugestões, não volume), intenção comercial × "grátis/modelo" |
| **G5** Construção | MVP em **até quatro semanas**, sem licença ou certificação | Stack, APIs, acesso a SDK, conteúdo necessário |
| **G6** Não vender IA | A IA pode estar na stack, mas não é o que se vende | Proposta de valor do produto ([[IA no centro do produto]]) |
| **G7** Viabilidade legal e de pagamento | Legal, contratual (termos de API e plataforma) e de recebimento **a partir do Brasil** | Termos de uso, política do merchant of record, exigência de CNPJ |
| **G8** Economia unitária | Caminho plausível até **US$ 5 mil/mês** com margem positiva | Preço × universo de compradores × taxas fixas de terceiros |

US$ 5 mil/mês equivalem a cerca de R$ 24.950 pela PTAX de 4,99 de 09/10/2026 ([BCB PTAX](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='10-01-2026'&@dataFinalCotacao='10-12-2026'&$format=json)), ou R$ 27 mil pelo câmbio de referência do projeto (~R$ 5,4/US$; [[Objetivo e restrições]]).

## Portas fáceis e portas que decidem

- **Quase todo mundo passa em G3, G5 e G6.** O dev tem Claude Code, e os compradores escolhidos já pagam taxas ou honorários altos.
- **A rodada inteira se decide em G1, G2, G4 e G8**, mais o G7 de pagamento para quem vende fora do Brasil ([[Validação condicionais e novos focos]]).
- Exemplos de como cada porta matou ideias:
  - **G2:** [[App Forge de Gantt para Jira]], em que novatos sem portfólio ficam com 0–29 instalações.
  - **G4:** buscas brasileiras dominadas por "grátis" e "modelo" ([[Padrão - busca por grátis e modelo]]).
  - **G7:** o Paddle proíbe preparatórios de exame, e marketplaces brasileiros exigem CNPJ ([[Padrão - pagamento e CNPJ bloqueiam rotas]]).
  - **G8:** a taxa fixa dos Correios americanos nas [[Cartas registradas online (EUA e Reino Unido)]] e o universo pequeno do [[Simulado do exame de corretor de seguros (SUSEP)]].

> [!warning] G1 e G2 não se aprovam juntos na pesquisa de mesa
> G1 pede receita observável de concorrentes. G2 pede, ao mesmo tempo, um mercado sem multidão e um novato que fature. Na fonte pública, essas duas provas não convivem: quando a receita aparece, os clones chegam em semanas; onde não há clones, não há receita para observar. **Só dinheiro de desconhecidos pagando por este produto, deste fundador, fecha as duas portas.** Ver [[Padrão - pesquisa de mesa não aprova G1 e G2]].

## Como se relacionam com os 7 critérios da rodada 1

| Critério de pontuação ([[Objetivo e restrições]]) | Porta mais próxima |
|---|---|
| Disposição a pagar (WTP) | G1 |
| Saturação baixa | G2 |
| Poder de compra | G3 |
| Distribuição sem contatos | G4 |
| Construção | G5 |
| Velocidade até a 1ª receita | sem porta própria (entra no prazo dos testes) |
| Risco baixo | G7 |
| — | G6 (restrição do usuário: não vender IA) |
| — | G8 (novo: a conta até US$ 5 mil/mês) |

## Vocabulário dos vereditos

- **APROVADA:** passa nas oito portas. **Nenhuma ideia chegou aqui em três rodadas.**
- **CONDICIONAL:** viva, mas com pelo menos uma porta que só um teste pago resolve. Cada condicional tem um teste e um limiar de abandono em [[Carteira de testes]].
- **KILL / morta:** reprovada por evidência numa porta que nenhum teste barato muda.
- Nas notas de pesquisa, cada porta recebe PASS, PARTIAL, WEAK, CONDITIONAL, UNPROVEN ou FAIL.

## Relacionadas

[[Registro de decisões]] · [[Protocolo de validação]] · [[Armadilhas e ideias mortas]]
