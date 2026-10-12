---
tags:
  - oportunidade
  - mercado/global
  - status/condicional
  - rodada/3
status: condicional
veredito: "CONDICIONAL, à espera do SDK da Trimble"
score: 22
mercado: "BR, PT e América Latina"
rodada: "3"
teste: "[[Carteira de testes]]"
fonte:
  - "[[trustmrr_br_pt_mapping]]"
  - "[[Rodada 3 - resumo]]"
---

# Conversor de versões do SketchUp (PT e ES)

Voltar para [[Ranking]].

> [!info] Condicional (22/35, rodada 3): o único mapeamento do TrustMRR que manteve as três forças do original
> Um arquivo .skp novo não abre numa versão antiga do SketchUp. O **DownConvert** cobra para converter e não tem página em português. Dois bloqueios: o **C SDK da Trimble** exige pedido de acesso desde maio de 2026 (e os termos para serviço hospedado não foram lidos), e a biblioteca **roda em Windows**. O primeiro passo é pedir o SDK, de graça ([[Carteira de testes]]).

## O que é

Envia um .skp, escolhe a versão de destino (2017–2025) e recebe o arquivo convertido em menos de 60 segundos; os arquivos são apagados em 7 dias. Interface e checkout em pt-BR (Pix e cartão), espanhol em seguida. Primeiro arquivo grátis, depois preço por arquivo ou licença ilimitada de pagamento único ([[trustmrr_br_pt_mapping]], candidato A).

## Comprador

- Arquitetos, designers de interiores, freelancers de 3D e marceneiros (persona do TrustMRR).
- O CAU teria "mais de 200 mil" profissionais (fonte secundária; o portal do CAU retornou 403) ([ArchDaily](https://www.archdaily.com/pt/tag/cau-br)). Não há contagem oficial de usuários de SketchUp no Brasil.
- Sinal de base em versões antigas: "sketchup 2017 make", "sketchup 2017 gratis", "sketchup 2017 download mega" ([autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=sketchup%202017)).

## Evidências

- **DownConvert:** US$ 5.395 em 30 dias e US$ 36.089 no total desde 05/12/2025, DR 28, à venda por US$ 17.900 ([TrustMRR](https://trustmrr.com/startup/digital-natives-services-fz-llc)). US$ 3,90 por arquivo ou US$ 24,90 ilimitado ([preços](https://downconvert-sketchup-files.com/pricing)).
- **A prova é contestada pelo próprio vendedor:** "DISCLAIMER TRUSTMRR TOOK RANDOM NUMBERS FROM MY STRIPE… 464 $/M AVERAGE REVENUE… 12K visitors/m" (autodeclarado). O rodapé liga sites irmãos (conversor de Rhino, GLB→glTF, how-to-sketchup.com), então o número verificado pode cobrir uma rede de sites.
- **Demanda em pt-BR, pt-PT e espanhol:** "converter sketchup versão anterior online", "salvar sketchup 2026 em versao anterior", "plugin salvar sketchup versao anterior"; em espanhol, "convertir sketchup a versión anterior online" ([autocomplete pt](https://suggestqueries.google.com/complete/search?client=firefox&hl=pt-BR&gl=br&q=salvar%20sketchup); [autocomplete es](https://suggestqueries.google.com/complete/search?client=firefox&hl=es&gl=es&q=convertir%20sketchup)). Não há modificador de preço ou "comprar".
- **Sem página /pt** no DownConvert (404); o how-to-sketchup.com tem artigo em espanhol de 16/07/2026, mas nada em português.

## Concorrentes e substitutos

- **Grátis:** "Salvar como" no desktop (exige licença); subir no 3D Warehouse e baixar versão antiga (nem sempre funciona); extensão Eneroth "Open Newer Version" (só Windows) ([fórum](https://forums.sketchup.com/t/conversion-to-older-sketchup-version/213816)).
- **Pagos:** gigs no Fiverr a ~US$ 10 por arquivo ([Fiverr](https://www.fiverr.com/sketchup3d/convert-your-sketchup-file-to-older-version)); extensão OldSave no Patreon.
- Conversores de formato (AnyConv, InnerScene) não rebaixam versão.

## Construção e bloqueios

- A C API do SketchUp lê e grava modelos; a biblioteca de Windows é 64 bits, feita no Visual Studio 2022 ([C API](https://extensions.sketchup.com/developers/sketchup_c_api/sketchup/index.html)). Daí a necessidade de um **worker Windows** (inferência).
- O SDK de macOS "não estava disponível para download público" em maio de 2026, e a Trimble criou um formulário de pedido de acesso; um usuário relatou pedido sem confirmação em 27/05/2026 ([fórum](https://forums.sketchup.com/t/sketchup-c-sdk-2026-macos-unavailable/346672)).
- MVP em ≤ 4 semanas **se** o SDK for liberado: front em Next.js, fila e uma VM Windows com um CLI em C++ (inferência). O custo da VM não foi cotado.

## Portas ([[Portões de aprovação]])

| Porta | Veredito |
|---|---|
| G1 | PASS fraco (DownConvert verificado mas contestado; Fiverr e Patreon como substitutos pagos) |
| G2 | PASS na saturação (nenhum conversor em pt-BR); prova de novato com ressalva |
| G3 | PASS (médio): profissionais que cobram clientes; ticket baixo |
| G4 | PASS nas sugestões; volume não medido |
| G5 | **CONDICIONAL**: depende do SDK e de um worker Windows |
| G6 | PASS (conversão determinística) |
| G7 | **NÃO VERIFICADO**: termos do SDK não recuperados; pagamentos não reverificados |
| G8 | DUVIDOSO: teto só em português de ~US$ 500–1.500/mês (especulativo); só chega a US$ 5 mil com espanhol, inglês e conversores vizinhos (Rhino, Revit, Promob) |

## Pontuação

| WTP | Saturação | Poder | Distribuição | Construção | Velocidade | Risco | Total |
|---|---|---|---|---|---|---|---|
| 3 | 4 | 3 | 4 | 3 | 3 | 2 | **22/35** |

## Teste (resumo; detalhes em [[Carteira de testes]])

1. **Dia 0:** pedir acesso ao C SDK da Trimble e ler os termos. **Para** se não houver aprovação em 14 dias ou se os termos proibirem serviço hospedado.
2. **Em paralelo (≈R$ 200, 21 dias):** página em pt-BR para "converter sketchup versão anterior online", checkout a **R$ 19,90 por arquivo** (Pix e cartão), entrega manual durante o teste com uma cópia licenciada do SketchUp ou pelo 3D Warehouse, avisando prazo de até 2 horas. **R$ 150** de Google Ads em 5 buscas exatas.
3. **Passa:** CPC ≤ R$ 1,00 **e** ≥ 5 pedidos pagos em ≤ 250 cliques. **Falha:** ≤ 1 pedido, ou CPC > R$ 2,00.

## Veredito

**CONDICIONAL.** O que sobrevive não é "a versão brasileira de uma regra local", e sim **a versão em português de um utilitário global forçado por versão de arquivo**. O fosso é SEO num idioma não atendido, não conhecimento regulatório. No melhor caso, um ativo lateral de US$ 500–1.500/mês, a menos que vire um portfólio de conversores.

## Notas de pesquisa

- [[trustmrr_br_pt_mapping]], "Deep validation of the top 3", candidato A
- [[Rodada 3 - resumo]], seção 3
- Relacionada: [[Conversor de lacuna de plataforma]] (o mesmo padrão de utilitário de conversão, rodada 1)
