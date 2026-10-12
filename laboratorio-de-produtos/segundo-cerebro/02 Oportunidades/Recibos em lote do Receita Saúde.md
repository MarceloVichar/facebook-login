---
tags:
  - oportunidade
  - mercado/br
  - status/morta
  - finalista
status: morta
veredito: KILL
score: 17
score_inicial: 25
mercado: BR
rodada: final
fonte:
  - "[[brazil_regulatory_demand]]"
  - "[[finalists_brazil_verification]]"
  - "[[Oportunidade de produto validada 2026]]"
---

# Recibos em lote do Receita Saúde

Voltar para [[Ranking]] · [[Armadilhas e ideias mortas]].

> [!failure] Morta na rodada final (17/35)
> A **própria Receita distribui um modelo CSV oficial e gratuito** com validador no e-CAC, e as suítes de consultório já incluem a exportação. Buscas por ferramenta dão 0–1 sugestão. Exemplo clássico do [[Padrão - governo entrega de graça]].

## O que era

Um web app que transforma a lista de pacientes e os pagamentos do mês no **CSV de lote oficial do Receita Saúde** para importar no Carnê-Leão. Também acompanharia os recibos emitidos (lendo o arquivo de retorno) e enviaria lembretes no fechamento do mês e antes do prazo de fevereiro.

## Comprador

Psicólogos, fisioterapeutas, fonoaudiólogos, terapeutas ocupacionais, dentistas e médicos que atendem como pessoa física. A nota regulatória estimou 45–90 mil emissores ativos ou mais.
- Janeiro de 2025, o primeiro mês obrigatório: **1.368.312 recibos** ([Jornal Contábil](https://jornalcontabil.com.br/noticia/receita-saude-mais-de-13-milhao-de-recibos-foram-emitidos-em-janeiro/)).
- Psicólogos emitiram **mais de 400 mil** recibos naquele mês ([CFP](https://site.cfp.org.br/profissionais-da-psicologia-emitem-mais-de-400-mil-recibos-virtuais-em-janeiro/)).
- Multa de **R$ 100 por mês** para quem não emite ou emite com erro (IN RFB 2.240/2024, [Manual 2.1](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/manuais/orientacao-tributaria/receita-saude-2.1.pdf)).

## Evidência decisiva

- **Modelo oficial gratuito:** o manual do Carnê-Leão traz "Baixe o modelo". O ZIP contém "Modelo de arquivo para recibos do Receita Saúde.csv", datado de 20/10/2025 ([ZIP Receita](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/documentos-tecnicos/escrituracao-do-carne-leao/escrituracao-carne-leao.zip)). O e-CAC importa o arquivo e devolve um relatório de erros por linha e campo, com até 1.000 linhas por arquivo e 16 campos.
- **Suítes que já fazem:**
  - [PsicoPront](https://psicopront.com.br/recursos): R$ 79/mês ou R$ 790/ano; exporta o CSV no formato oficial.
  - [Psicontrole](https://psicontrole.com.br/): R$ 97 por 90 dias.
  - **Corpora**: desde 14/4/2026, gera o arquivo **e lê o de retorno**, ou seja, a melhor versão da ideia já foi lançada ([Leia Notícias](https://leianoticias.com.br/329672-corpora-lanca-integracao-com-receita-saude-para-psicologos/)).
  - Clínica Idée, Clinicorp, uma planilha paga (ePlanilhas, R$ 149,90), um modelo grátis no YouTube e um projeto open source (salutti).
- **Ninguém procura ferramenta:** "receita saude em lote" [1]. "planilha", "csv", "excel", "gerador" e "automatizar" dão **0 sugestões**. As buscas ricas são de dúvida ("retroativo", "erro 02", "passo a passo").
- Num fórum contábil, um contador diz que *"é bem simples elaborar essa planilha"* ([Contábeis](https://www.contabeis.com.br/forum/tributos-federais/411363/emissao-em-lote-de-recibos-do-receita-saude/)).

## Riscos que sobravam

- **LGPD:** o arquivo tem CPFs de pacientes ligados a um serviço de saúde, o que plausivelmente é dado sensível (art. 11). É inferência, não conferida com advogado.
- **Baixa receita por usuário:** seriam ~1.100 assinantes a R$ 24,90 para chegar a R$ 27 mil/mês.

## Pontuação

| Rodada | WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|---|
| Final ([[finalists_brazil_verification]]) | 2 | 2 | 3 | 1 | 5 | 2 | 2 | **17/35** |
| Exploratória ([[brazil_regulatory_demand]], C1) | 3 | 3 | 3 | 4 | 5 | 4 | 3 | 25/35 |

## Veredito

**KILL** como produto pago. No máximo, serviria como gerador gratuito no navegador, usado de isca de SEO para outro produto.

## Notas de pesquisa

- [[finalists_brazil_verification]], "Finalist 1"
- [[brazil_regulatory_demand]], seções 7, 15 e 16
- [[brazil_professional_niches]], lista de armadilhas da seção 4
