---
tags:
  - armadilha
  - padrao
atualizado: 2026-10-12
---

# Padrão: o governo entrega de graça

Voltar para [[Armadilhas e ideias mortas]].

> [!warning] A regra
> **Obrigações nacionais e uniformes atraem a ferramenta gratuita do governo.** Quando todo mundo no país tem de cumprir a mesma obrigação, do mesmo jeito, a Receita, o ministério ou o órgão regulador acaba publicando um modelo, um simulador ou um emissor de graça. A janela para um SaaS pago fecha antes de ele ganhar tração.

## Casos na pesquisa

| Ideia | O que o governo entregou |
|---|---|
| [[Recibos em lote do Receita Saúde]] | Modelo CSV oficial (20/10/2025) com validador e relatório de erros no e-CAC |
| [[Emissor de NFS-e Nacional]] | Emissor Nacional gratuito |
| [[Triagem do Simples híbrido para contadores]] | Simulador oficial de IBS/CBS no Simples, desde 18/09/2026 |
| [[Simulador IBS-CBS para locador pessoa física]] | Calculadora oficial gratuita |
| [[Planejador de IRPFM e dividendos]] | A Receita pode calcular o redutor ela mesma (art. 16-B §7º da Lei 15.270) |
| [[Assistente de Transparência Salarial]] | O MTE gera o relatório |
| [[EUDR para pequenos produtores brasileiros]] | Plataformas gratuitas da Conab e do MAPA, além da da indústria (Cecafé–Serasa) |
| Exterior: [[Conversor de e-invoicing]] | Registro Peppol gratuito na Bélgica e geradores gratuitos |

## O contraponto: onde o padrão não pega

A ideia que sobreviveu, o [[Gerador de laudos de vistoria e inspeção]], tem o perfil oposto. A obrigação é **fragmentada** (41 leis municipais e 5 estaduais de inspeção predial, só 10 regulamentadas), **técnica** (NBR 16747, estrutura IBAPE, ART/RRT) e o documento é assinado por um profissional. Nenhum governo vai publicar "o gerador de laudo" de todos os municípios. *"Obrigações fragmentadas, técnicas e presas a normas ficam para os pequenos"* ([[Oportunidade de produto validada 2026]]).

## Como testar antes de construir

- Procurar "modelo oficial", "simulador", "emissor gratuito" e "baixe o modelo" nos portais gov.br e no e-CAC.
- Ver se o autocomplete traz "gratuito", "oficial" ou "receita" junto da obrigação.
- Desconfiar quando a obrigação é **federal, uniforme e baseada em arquivo**: é exatamente o que o governo consegue padronizar.

## Relacionadas

[[Padrão - plataforma absorve o recurso]] · [[Padrão - saturação]]

## Rodadas 2 e 3: a regra ganha uma nuance

> [!note] A ferramenta grátis só mata quando ocupa a busca comercial
> O **P7M.io** fatura US$ 4.627 em 30 dias apesar dos visualizadores gratuitos dos certificadores italianos, porque eles não dominam a busca comercial ([[Visualizador de p7m para a Itália]]). A regra "o governo dá de graça" é um **teto de preço**, não sempre uma sentença ([[trustmrr_newcomers]]).

Novos casos em que o Estado entregou de graça e matou a ideia:

| Ideia | O que o Estado entregou |
|---|---|
| Visualizador de .p7s para o Brasil (rodada 3) | O Validar do ITI, gratuito ([ITI](https://h-validar.iti.gov.br/Docs/cartilha-de-uso.pdf)) |
| Livro de Reclamações e recibos de renda em Portugal (rodada 2) | Portais oficiais (livroreclamacoes.pt, Portal das Finanças) |
| Alertas de licitação para MEIs (rodada 2) | O Contrata+Brasil avisa por WhatsApp ([Jornal Contábil](https://jornalcontabil.com.br/noticia/contratabrasil-amplia-participacao-do-mei-com-34-novas-ocupacoes/)) |
| Compliance da Lei Karin no Chile (rodada 2) | Protocolos oferecidos pelas mútuas |
| Regras de drone no Brasil (rodada 3) | SISANT e SARPAS, da ANAC e do DECEA |

Risco ainda aberto: o [[Preparatório do teste de nacionalidade portuguesa]] morre se o Estado publicar um banco de questões oficial grátis, como fez o Instituto Cervantes na Espanha.
