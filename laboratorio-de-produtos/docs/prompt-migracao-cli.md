# Prompt para colar no Claude Code CLI (local)

Abra o terminal na pasta onde você guarda seus projetos (por exemplo `~/projetos`), rode `claude` e cole o texto abaixo.

---

Vamos migrar e continuar um projeto que comecei numa sessão do Claude Code na nuvem. Siga as etapas na ordem e confirme cada uma antes de passar para a próxima.

## 1. Trazer o projeto
- Clone https://github.com/MarceloVichar/facebook-login.git numa pasta temporária e faça checkout do branch `ccr-f72cc16f-9urhz1`.
- Copie a pasta `laboratorio-de-produtos/` desse branch para `./laboratorio-de-produtos`, no diretório atual. Ela contém o vault do Obsidian (`segundo-cerebro/`), `CLAUDE.md`, `README.md`, `docs/` e `apps/`.
- Apague a pasta temporária do clone.

## 2. Criar o repositório novo
- Dentro de `./laboratorio-de-produtos`, rode `git init -b main` e faça o commit inicial com tudo.
- Crie o repositório **privado** `laboratorio-de-produtos` na minha conta com o `gh`: `gh repo create laboratorio-de-produtos --private --source . --push`. Antes, confira com `gh auth status` que estou logado.
- Confirme que o push funcionou e me mostre a URL.

## 3. Carregar todo o contexto
Leia nesta ordem, por inteiro:
1. `CLAUDE.md`
2. `segundo-cerebro/00 Início.md`
3. todas as notas de `segundo-cerebro/01 Projeto/` (objetivo e restrições, portões de aprovação G1–G8, registro de decisões, próximos passos)
4. `segundo-cerebro/02 Oportunidades/Ranking.md`
5. `segundo-cerebro/03 Armadilhas/Armadilhas e ideias mortas.md`
6. `segundo-cerebro/04 Execução/Carteira de testes.md`
7. os três relatórios em `segundo-cerebro/05 Pesquisa/reports/`
8. as notas `segundo-cerebro/02 Oportunidades/` do **gerador de parecer descritivo** e do **simulador do CBLE**, e as notas de pesquisa ligadas a elas (`brazil_regulated_documents.md` e `exam_prep_deep.md`)

Depois de ler, me dê um resumo de no máximo 15 linhas: objetivo, restrições, o que foi descartado e por quê, e os dois testes ativos com seus limites de passa/abandona. Assim eu confirmo que você pegou o contexto.

## 4. Decisões já tomadas por mim (não reabrir)
- **Custo zero nos testes:** nada de anúncio pago. Divulgação orgânica (grupos de Facebook, Pinterest, Reddit, LinkedIn, fóruns), hospedagem grátis (Vercel ou Cloudflare Pages) e pagamento sem mensalidade (Asaas para Pix no Brasil, Gumroad para o exterior). Começo no meu CPF; só abro CNPJ se um teste passar.
- **A IA pode estar na stack, mas o produto não pode ser "vender IA".**
- **Teste 1, gerador de parecer descritivo para a educação infantil (BR).** É determinístico: checklist de observações → banco de frases alinhado à BNCC → relatório da turma em PDF. Os dados das crianças não passam por IA. Precisa estar no ar antes de **10/11/2026**.
- **Teste 2, simulador do CBLE** (exame de licença de despachante aduaneiro dos EUA, da CBP). Simulador cronometrado grátis com a prova pública de abril de 2026 (80 questões, 4h30, aprovação com 75%) e pré-venda do pacote completo no Gumroad (US$ 149). Precisa estar pronto antes de **10/11/2026**, para pegar quem reprovar na prova de 28/10/2026.
- Os limites de passa/abandona são os da `Carteira de testes.md`, adaptados para tráfego orgânico. Na versão sem anúncio, o critério passa a ser vendas por N visitantes, e não só número de vendas.

## 5. Próximo trabalho
- Monte um plano curto (uma lista) para construir o Teste 1 e o Teste 2 em `apps/parecer-descritivo/` e `apps/simulador-cble/`: stack, telas, dados, deploy grátis, pagamento e textos de divulgação.
- Me mostre o plano antes de codar.
- Toda decisão nova entra em `segundo-cerebro/01 Projeto/Registro de decisões.md`, com data. Todo resultado de teste entra no log da `Carteira de testes.md`.
- Faça commit e push no repositório novo a cada etapa concluída.

Pode usar todas as ferramentas e MCPs disponíveis nesta máquina (gh, navegador, Obsidian etc.).
