---
tags:
  - oportunidade
  - mercado/br
  - status/condicional
  - rodada/3
status: condicional
veredito: "CONDICIONAL; exige prospecção ativa"
score: 19
mercado: BR
rodada: "3"
teste: "[[Carteira de testes]]"
fonte:
  - "[[brazil_regulated_documents]]"
  - "[[Rodada 3 - resumo]]"
---

# Software para empresas de manutenção de extintores

Voltar para [[Ranking]].

> [!warning] Condicional (19/35, rodada 3), em conflito com a restrição de não ter contatos
> É o análogo brasileiro do **FireCert** (Reino Unido, US$ 5.003 em 30 dias). O comprador é bom: uma empresa B2B que atende muitos clientes e paga todo mês. Mas a busca comercial é de 0–3 sugestões, então **a venda teria de ser por prospecção ativa** (e-mail ou WhatsApp a empresas do cadastro público do Inmetro). Isso **conflita com a restrição de "sem contatos" e "sem prospecção"** do projeto ([[Objetivo e restrições]]). Por isso fica fora da carteira até o usuário decidir se aceita esse canal ([[Carteira de testes]]).

## O que é

Um app web mobile-first para empresas que fazem manutenção de extintores, hidrantes, alarmes e iluminação de emergência ([[brazil_regulated_documents]], Q6-A):
- etiqueta QR por equipamento e níveis de inspeção da NBR 12962;
- checklist do técnico com fotos;
- certificado ou relatório em PDF e ordem de serviço gerados automaticamente;
- portal do cliente com os vencimentos de cada local: recarga a cada 12 meses e teste hidrostático a cada 5 anos, mais AVCB, brigada e SPDA como gancho de retenção.

Cobrança por local de cliente atendido, no estilo da Inspefire, ou preço fixo por empresa.

## Comprador

- **1.776 registros ativos** de empresas de inspeção e manutenção de extintores no Inmetro (16/07/2025), concentradas no Sul e Sudeste, com São Paulo à frente. O Inmetro diz que os registros novos caem, "possivelmente por saturação do mercado" ([Inmetro ARR](https://www.gov.br/inmetro/pt-br/assuntos/regulamentacao/avaliacao-de-resultado-regulatorio/2026/inspecao-tecnica-e-manutencao-de-extintores-de-incendio/sei_inmetro-2373600-relatorio-final.pdf)).
- O universo informal é maior: em BH, em 2020, "das mais de 110 empresas… pouco mais de 10 possuem cadastro" ([CMBH](https://cmbh.mg.gov.br/print/comunica%C3%A7%C3%A3o/not%C3%ADcias/2020/11/comiss%C3%A3o-ir%C3%A1-propor-pl-para-regulamentar-empresas-do-setor)).
- Licitações públicas chegam a exigir sistema de rastreio por extintor ([TRE-MS](https://www.tre-ms.jus.br/transparencia-e-prestacao-de-contas/licitacoes/pregao/pregao-2023/arquivos-2023/tre-ms-disp-eletr-05-2023-recarga-extintores-etp)).

## Concorrentes

| Ferramenta | Preço | Tração |
|---|---|---|
| [Inspefire](https://www.inspefire.com.br) | R$ 49 (START) a R$ 24 (MASTER, ≤ 30 contas) **por conta/CNPJ por mês**; 30 dias grátis; módulos de brigada, LGE, cozinha industrial, WhatsApp e "Inspe IA" | 55 avaliações no Play, atualizado em 10/10/2026; já tem busca pela marca |
| [Produttivo](https://www.produttivo.com.br/modelo/checklist-extintores/) | Modelo de checklist de extintores com QR | Genérico |
| [Inspeção Pro](https://inspecaopro.com.br), Extinguisher 360, Auvo, Field Control, Tecniko | — | Genéricos |

**Brecha possível (inferência):** a Inspefire cobra por CNPJ, então uma empresa com 30 clientes paga ~R$ 720/mês (30 × R$ 24). Um preço fixo por empresa poderia sair mais barato para carteiras grandes.

## Portas ([[Portões de aprovação]])

| Porta | Veredito | Evidência |
|---|---|---|
| G1 | PASS (fraco) | Planos pagos da Inspefire; FireCert e BasinCheck no exterior |
| G2 | INCERTO | Um incumbente focado mais ferramentas genéricas; nenhum novato brasileiro vencendo |
| G3 | PASS | Empresas registradas vendendo serviço recorrente |
| G4 | **FAIL na busca**; prospecção possível | 0–3 sugestões comerciais; cadastro público de 1.776 empresas |
| G5 | PASS | CRUD, QR, PWA offline, PDF em 3–4 semanas |
| G6 | PASS | — |
| G7 | PASS | Sem licença; e-mail frio por legítimo interesse B2B na LGPD **não verificado** com a ANPD |
| G8 | DUVIDOSO | R$ 27 mil/mês ≈ 135 empresas a R$ 199 (~7,6% de todas as registradas), ou ~900 locais a R$ 30 |

## Pontuação

| WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|
| 3 | 2 | 3 | 2 | 4 | 2 | 3 | **19/35** |

- **Primeira receita:** 6–10 semanas (B2B por prospecção; trial de 30 dias é o padrão da Inspefire).

## Teste proposto pela nota (fora da carteira por exigir prospecção)

- **≈ R$ 150 e 14–21 dias.** Escolher à mão 150 empresas registradas de SP e do Sul no cadastro público do Inmetro (sem raspagem) e mandar e-mail ou WhatsApp pessoal oferecendo piloto grátis de 30 dias de um protótipo clicável (QR → certificado em PDF → página de vencimentos do cliente), com preço de fundador de **R$ 149/mês fixo**.
- **Passa:** ≥ 10 respostas, ≥ 5 demonstrações e ≥ 2 empresas pagando R$ 149 (ou o 1º mês antecipado) em 21 dias.
- **Falha:** < 3 demonstrações, ou todas respondendo "já uso o Inspefire/planilha".

> [!question] Decisão do usuário
> Este é o único teste da rodada 3 que depende de abordar desconhecidos um a um. A rodada 1 rejeitou serviços porque dependem de prospecção ([[Registro de decisões]]). Se o usuário aceitar prospecção ativa para software B2B, o teste entra na carteira; se não, a ideia fica parada.

## Veredito

**CONDICIONAL.** Tem o teto por cliente mais alto da rodada 3, mas falha em G4 por busca e enfrenta um incumbente focado com preços brasileiros (o FireCert cobra £79–129/mês fixos, 3–5 vezes o que a Inspefire cobra de uma empresa pequena). O mesmo padrão poderia valer para instrutores de brigada, instaladores de SPDA e testadores de hidrante, cada um mais estreito.

## Notas de pesquisa

- [[brazil_regulated_documents]], Q1 (1b) e Q6 (candidato A)
- Relacionadas: [[Certificados de dedetização e caixa d'água]] (morta por saturação, mesmo formato de certificado de prestador), [[Calendário de conformidade para síndicos]]
