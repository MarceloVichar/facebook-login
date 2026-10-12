# Laboratório de Produtos

Projeto de um desenvolvedor solo brasileiro para encontrar, testar e lançar um produto de software que gere receita. O Claude é parceiro de pesquisa e de construção.

## Restrições do projeto (não violar)
- Sem clientes, contatos ou audiência. A venda vem de busca, comunidades e marketplaces.
- Custo zero nos testes: sem anúncios pagos. Use hospedagem gratuita (Vercel/Cloudflare Pages) e plataformas de pagamento sem mensalidade (Asaas para Pix no Brasil, Gumroad para o exterior).
- A IA pode estar na stack, mas o produto não pode ser "vender IA" (nada de chatbot ou wrapper como proposta de valor).
- Ninguém abre empresa (CNPJ) antes de um teste passar. Começa no CPF.
- Os limites de passa/abandona de cada teste ficam fixados antes de começar. Só conta dinheiro de desconhecidos.

## Onde está cada coisa
- `segundo-cerebro/` é o vault do Obsidian e a fonte da verdade do projeto.
  - `00 Início.md` é o mapa geral e mostra o status atual.
  - `01 Projeto/` traz objetivo, restrições, portões de aprovação G1–G8, registro de decisões e próximos passos.
  - `02 Oportunidades/` tem uma nota por ideia, com frontmatter (status/score/mercado), e o `Ranking.md`.
  - `03 Armadilhas/` reúne as ideias mortas e os padrões de por que morrem.
  - `04 Execução/Carteira de testes.md` traz os testes, os prazos e os limites.
  - `05 Pesquisa/` guarda os relatórios e as notas brutas das 3 rodadas de pesquisa.
- `apps/` tem um subdiretório por MVP em teste, por exemplo `apps/parecer-descritivo/` e `apps/simulador-cble/`.
- `docs/` guarda as instruções para um Claude Project e outros documentos de apoio.

## Como trabalhar neste repo
- Antes de propor uma ideia nova, leia `02 Oportunidades/Ranking.md` e `03 Armadilhas/Armadilhas e ideias mortas.md` para não repetir ideias descartadas.
- Toda decisão relevante entra em `01 Projeto/Registro de decisões.md`, com data.
- Todo resultado de teste entra no log de resultados da `Carteira de testes.md`.
- As notas são escritas em português do Brasil, com links `[[wikilink]]`, frontmatter YAML e fontes com URL. Não invente números.
- Os MVPs são simples: site estático ou app web leve, sem backend, a menos que seja necessário. Deploy gratuito.

## Testes ativos (out/2026)
1. **Gerador de parecer descritivo para a educação infantil (BR).** Precisa estar no ar antes de 10/11/2026. Divulgação em grupos de professoras e no Pinterest. Venda via Pix (Asaas).
2. **Simulador do CBLE**, o exame de licença de despachante aduaneiro dos EUA. Simulador grátis da prova de abril de 2026 com pré-venda no Gumroad. Divulgação no Reddit, no LinkedIn e em grupos de estudo, depois da prova de 28/10/2026.
