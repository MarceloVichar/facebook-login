---
tags:
  - oportunidade
  - mercado/br
  - status/condicional
  - rodada/3
status: condicional
veredito: CONDICIONAL
score: 22
mercado: BR
rodada: "3"
teste: "[[Carteira de testes]]"
fonte:
  - "[[brazil_regulated_documents]]"
  - "[[Rodada 3 - resumo]]"
---

# Gerador de parecer descritivo da educação infantil

Voltar para [[Ranking]].

> [!tip] Condicional (22/35, rodada 3): o teste mais urgente da carteira
> É o análogo brasileiro do **Tifox** (França). Tem a melhor demanda de busca de todas as ideias brasileiras da rodada 3, mas comprador fraco e concorrência de IA e de modelos grátis. O teste custa **R$ 200** e precisa **começar antes de 10/11/2026**, para pegar o pico de fim do 2º semestre ([[Carteira de testes]]).

## O que é

Um app web **determinístico, sem LLM**. A professora cria a turma e marca, por criança, os comportamentos observáveis em cada um dos **5 campos de experiência da BNCC** e por faixa etária (bebês, crianças bem pequenas, crianças pequenas). Acrescenta fotos e notas curtas e recebe um parecer por criança, montado a partir de **bancos de frases curados e editáveis**, com os códigos da BNCC. Exporta PDF ou Word da turma inteira. O plano escolar deixa a coordenação padronizar frases e revisar. Como não há LLM, os dados das crianças não saem da ferramenta ([[brazil_regulated_documents]], Q6-B).

- **Preço proposto pela nota:** R$ 19,90 por semestre por professora, ou ~R$ 9 por turma por ano para escolas (modelo Tifox).

## Comprador

- **Base:** cerca de **687 mil docentes** na educação infantil (Censo Escolar, declaração do MEC de 23/09/2025) ([Diario de Pernambuco](https://www.diariodepernambuco.com.br/brasil/2025/09/11696464-governo-do-brasil-lanca-ciclo-2025-2026-do-programa-de-formacao-continuada-leitura-e-escrita-na-educacao-infantil.html)).
- **Poder de compra fraco:** a maioria trabalha em redes municipais com salário baixo. O comprador realista é a professora a R$ 15–25/mês (faixa da Profez) ou a escola particular por turma (modelo Tifox). A rede privada encolhe: −2,47% nas matrículas de creche de 2024 para 2025 ([Jornal de Brasília](https://jornaldebrasilia.com.br/noticias/brasil/matriculas-na-creche-e-pre-escola-voltam-a-cair-no-brasil-em-2025/)).
- **Âncora regulatória:** na educação infantil, o parecer descritivo é o instrumento oficial de avaliação (LDB e BNCC; sem nota nem retenção). Pelotas exige um formato próprio, o PDEI ([Profez](https://profez.com.br/modelos/parecer-descritivo/de-acordo-com-a-bncc)).
- **Dor:** 20–25 pareceres por professora a cada semestre, e o copia-e-cola é notado pela coordenação e pelas famílias (alegação de um concorrente).

## Evidências

- **Demanda (autocomplete, 12/10/2026): 10 sugestões em quase todo termo principal.** "parecer descritivo" → "educação infantil", "pronto", "de acordo com a bncc", "5 anos"; "relatório descritivo educação infantil" → "bncc", "3/4/5 anos", "segundo semestre", "1/4 bimestre" ([autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=parecer%20descritivo%20educa%C3%A7%C3%A3o%20infantil)).
- **Intenção comercial quase nula:** "gerador de parecer descritivo" 0, "app parecer descritivo" 0, "parecer descritivo ia" 1 ([[Padrão - busca por grátis e modelo]]).
- **Sazonalidade:** as sugestões citam semestre, bimestre e trimestre; os picos são junho–julho e novembro–dezembro (inferência). Outubro fica logo antes do pico.
- **Prova estrangeira verificada:** Tifox, €12–25 por turma por ano, **US$ 1.586 em 30 dias**, 57 assinaturas ([TrustMRR Tifox](https://trustmrr.com/startup/tifox)).

## Concorrentes

| Ferramenta | O que faz | Preço |
|---|---|---|
| [Profez](https://profez.com.br/parecer-descritivo) | Suíte com IA: "Parecer descritivo pronto em 30 segundos", modo turma, Word/PDF, páginas de SEO por idade | Grátis (5 materiais/mês); R$ 17,91/mês (Pro); R$ 31,58/mês (Pro+) |
| Kits no Hotmart | 15 pareceres por campo de experiência; e-books de frases | ~US$ 4 ([Hotmart](https://hotmart.com/pt-br/marketplace/produtos/modelos-de-parecer-descritivo-educacao-infantil-3o-trimestre-15-alunos/G96187555I)) |
| Modelos grátis em blogs, ChatGPT | Texto livre | Grátis |
| Google Play | Nenhum app dedicado nos primeiros resultados ([Play](https://play.google.com/store/search?q=parecer+descritivo&c=apps&hl=pt_BR&gl=BR)) | — |

> [!note] "Sem IA" é defesa para a coordenação, não para a professora
> Um gerador determinístico evita alucinação e a exposição LGPD de mandar dados de crianças a um LLM. Mas a Profez já ranqueia com texto individualizado por IA, e o ChatGPT é grátis. A consistência e a auditabilidade interessam à coordenadora; a professora quer rapidez (inferência da nota).

## Portas ([[Portões de aprovação]])

| Porta | Veredito | Evidência |
|---|---|---|
| G1 | PASS | Planos pagos da Profez; kits no Hotmart; Tifox verificado |
| G2 | **FRACA** | A Profez mostra que um novato ranqueia, mas ocupa a vaga com IA; modelos grátis em excesso |
| G3 | FRACA–MÉDIA | Professoras a ~R$ 18/mês; rede privada encolhendo |
| G4 | PASS informacional / FAIL comercial | Cauda longa rica; intenção de ferramenta quase zero |
| G5 | PASS | Motor de bancos de frases + PDF |
| G6 | PASS por desenho, e é a desvantagem competitiva | — |
| G7 | PASS | Sem certificação; LGPD para dados de crianças; Hotmart, Asaas ou Stripe BR |
| G8 | DUVIDOSO | R$ 27 mil/mês ≈ 1.360 professoras a R$ 19,90/mês equivalente, ou ~2.700 passes semestrais por mês na média do ano, com picos em 4 meses |

## Pontuação

| WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|
| 3 | 2 | 2 | 3 | 5 | 4 | 3 | **22/35** |

- **Construção:** 2–3 semanas; o trabalho principal é o banco de frases, e o usuário é falante nativo.
- **Primeira receita:** 2–6 semanas se lançar antes do pico de nov–dez; senão, espera junho de 2027.

## Teste (resumo; detalhes em [[Carteira de testes]])

- MVP de **uma faixa etária (5 anos, 2º semestre)** com 20 pareceres de exemplo numa página de SEO e exportação da turma em PDF atrás de um paywall de **R$ 19,90** (passe semestral).
- **R$ 200** de Google Ads em "relatório descritivo educação infantil 5 anos segundo semestre", "parecer descritivo educação infantil 5 anos de acordo com a bncc" e variações.
- **Passa:** CPC ≤ R$ 0,80 **e** ≥ 8 passes pagos (≥ 3% de ≥ 250 cliques) até **15/12/2026**.
- **Falha:** ≤ 2 vendas, ou CPC > R$ 1,50.

## Riscos

- Sazonalidade forte; baixa disposição a pagar das professoras; intenção "pronto/grátis".
- Incumbentes de IA; tempo para ranquear no SEO.
- O conteúdo precisa ser original: nada copiado de kits do Hotmart ou de blogs.

## Veredito

**CONDICIONAL.** Se passar, o caminho para o poder de compra são os planos escolares (modelo Tifox para escolas infantis particulares). A nota conclui que ele não desloca o [[Gerador de laudos de vistoria e inspeção]], que tem a combinação melhor (o engenheiro paga e o documento leva ART).

## Notas de pesquisa

- [[brazil_regulated_documents]], Q3 e Q6 (candidato B)
- [[Rodada 3 - resumo]], seção 2
- Relacionadas: [[Padrão - busca por grátis e modelo]], [[IA no centro do produto]]
