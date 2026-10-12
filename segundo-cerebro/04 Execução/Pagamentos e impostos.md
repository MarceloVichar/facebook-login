---
tags:
  - execucao
  - pagamentos
  - impostos
atualizado: 2026-10-12
---

# Pagamentos e impostos

Voltar para [[00 Início]].

> [!abstract] Resumo
> **Comece no CPF e migre para ME no Simples.** Valide recebendo no CPF pelo Asaas. Com receita recorrente, por volta do 2º ou 3º mês ou antes de passar de R$ 3–5 mil/mês, abra uma ME no Simples Nacional, com Fator R para cair no Anexo III. Para vender ao exterior, use o Paddle. **Confirme tudo com um contador**: as notas não substituem orientação contábil.

> [!warning] Itens marcados para confirmar com o contador
> - Se o **INSS de contribuinte individual (20%)** é obrigatório na fase em CPF ([INSS](https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-contribuicao-mensal)).
> - A **data da NFS-e nacional obrigatória** para ME/EPP do Simples. As notas divergem: **1/9/2026** pela Res. CGSN 189/2026 ([COAD](https://www.coad.com.br/home/noticias-detalhe/137522/nfs-e-de-padrao-nacional-sera-obrigatoria-para-empresas-do-simples-nacional)) ou **1/11/2026** pela Res. CGSN 191/2026, que a teria substituído ([Conta Azul](https://contaazul.com/blog/nfse-padrao-nacional/)).
> - Se vendas a brasileiros **via Paddle** contam como exportação para a imunidade de IBS/CBS a partir de 2027 (LC 214, art. 80, §1º-A).

> [!warning] Atualização das rodadas 2 e 3: o Paddle não serve para tudo
> A política do Paddle (13/04/2026) proíbe **preparatórios de exame**, **serviços de governo**, **entrega física** e **ferramentas automáticas de avaliação**, e restringe **televendas**. Para preparatórios vendidos fora do Brasil, a rota é o **Gumroad** (10% + US$ 0,50), que repassa ao Brasil só via PayPal, a confirmar com um teste de US$ 1. TikTok Shop, Shopee e Temu exigem CNPJ, e o MEI não cobre programação. Detalhes em [[Padrão - pagamento e CNPJ bloqueiam rotas]]; uso em cada teste em [[Carteira de testes]].

## Fase A: validação (semanas 0–6), no CPF

| Provedor | CPF? | Pix | Cartão | Observação |
|---|---|---|---|---|
| **Asaas** (padrão) | Sim | R$ 1,99 por Pix (R$ 0,99 promocional nos 3 primeiros meses) | 2,99% + R$ 0,49 à vista ou assinatura | Sem mensalidade; assinaturas nativas; NFS-e a R$ 0,49 ([Asaas](https://www.asaas.com/precos-e-taxas)) |
| **Efí Pro** | "Conta para negócios sem CNPJ" | 1,19% | 3,49% à vista | Pix Automático a R$ 3,50 por cobrança ([Efí](https://sejaefi.com.br/tarifas)) |
| **Mercado Pago** | Sim | 0,99% | 3,99–4,98% conforme o prazo de liberação | Pix mais barato e familiar ao comprador ([Mercado Pago](https://www.mercadopago.com.br/ferramentas-para-vender/link-de-pagamento)) |
| Pagar.me | **Exige CNPJ ou MEI** | 0,99% | 4,19% | ([Pagar.me](https://pagar.me/precos/)) |
| Stripe Brasil | Não verificado | 1,19%, só por convite | 3,99% + R$ 0,39 (+2% internacional) | Contestação a R$ 55; Billing +0,7% ([Stripe BR](https://stripe.com/br/pricing)) |
| Hotmart / Kiwify / Eduzz | Sim | — | ~9–15% por venda | Só valem pela rede de afiliados |

Taxa sobre uma assinatura de R$ 49 (cálculo da nota de GTM): Asaas cartão R$ 1,96 (4,0%); Asaas Pix R$ 1,99 (4,1%); Mercado Pago Pix R$ 0,49 (1,0%); Efí Pix R$ 0,58 (1,2%); Stripe BR cartão + Billing R$ 2,69 (5,5%); Hotmart R$ 7,34 (15,0%). O **Pix de taxa fixa sai caro em tíquete baixo**; o Pix percentual é melhor abaixo de ~R$ 170–200.

**Imposto na fase A:**
- Recolher via **Carnê-Leão** até o último dia útil do mês seguinte ([Receita](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao)).
- Desde janeiro de 2026, rendimento tributável de **até R$ 5 mil/mês tem IR zero**, com redução decrescente até R$ 7.350 ([Lei 15.270/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm)).
- Para algum comprador estrangeiro logo no início, a nota de GTM sugere o **Gumroad** (merchant of record, 10% + 50¢) em vez de montar conformidade fiscal.

**Higiene legal mínima:**
- Termos de uso.
- Aviso de privacidade conforme a LGPD (art. 9), com **canal de contato**. Agentes de pequeno porte não precisam de encarregado ([ANPD Res. 2/2022](https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-2-de-27-de-janeiro-de-2022-376562019)).
- **Reembolso de 7 dias**, exigido pelo art. 49 do CDC ([CDC](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm)), que também protege contra contestações.
- O Decreto 7.962/2013 exige mostrar no site nome, **CPF/CNPJ** e endereço, mais um motivo para abrir CNPJ cedo e não expor CPF e endereço residencial.

## Fase B: receita recorrente, ME no Simples Nacional

- **MEI não serve:** programação não é atividade permitida. O PLP 25/2026, que a incluiria, só passou por uma comissão da Câmara, em 30/06/2026 ([Fenacon](https://fenacon.org.br/noticias/comissao-aprova-inclusao-de-programadores-e-desenvolvedores-de-software-no-mei/)). Não usar uma ocupação de MEI sem relação como atalho: é risco de conformidade.
- **Fator R:** licenciamento de software cai no **Anexo III (6% na primeira faixa)** quando a folha, incluindo o pró-labore, chega a **28% da receita** dos últimos 12 meses. Abaixo disso, cai no **Anexo V (15,5%)** ([LC 123](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm), art. 18 §§5º-D, 5º-K e 5º-M).
- Um **pró-labore de um salário mínimo (R$ 1.621)** cumpre o Fator R até cerca de **R$ 5,8 mil** de receita mensal (1.621 ÷ 0,28 ≈ R$ 5.789). Acima disso, o pró-labore precisa subir, ou a empresa cai no Anexo V.
- CNAE provável: **6203-1/00** (licenciamento de software não customizável); 6311-9/00 é alternativa para SaaS/hospedagem, se o contador preferir.
- **NFS-e** pelo Emissor Nacional, que o Asaas pode automatizar a R$ 0,49 por nota.
- Mover o Asaas para o CNPJ. O Pix Automático no Mercado Pago exige CNPJ com mais de 6 meses.

**Carga estimada** (cálculo da nota de GTM, sem honorários do contador):

| Cenário | CPF (Carnê-Leão + INSS) | ME, Anexo III com Fator R | ME, Anexo V, pró-labore mínimo |
|---|---|---|---|
| US$ 1 mil de MRR (R$ 5.400/mês) | IR ≈ R$ 150 (2,8%); com INSS de 20%, ≈ R$ 1.117 (20,7%) | Doméstico ≈ R$ 502 (9,3%); exportação ≈ R$ 343 (6,4%) | Doméstico ≈ R$ 1.015 (18,8%); exportação ≈ R$ 755 (14,0%) |
| US$ 5 mil de MRR (R$ 27.000/mês), tudo exportação | ≈ R$ 7.745 (28,7%) | ≈ R$ 2.915 (10,8%) | ≈ R$ 3.132 (11,6%) |

## Fase C: vendas ao exterior

Vale para as alternativas, não para os laudos.

| Opção | Situação para quem mora no Brasil |
|---|---|
| **Paddle** (merchant of record) | **Brasil suportado**; 5% + 50¢; repasse mensal por wire (SWIFT de US$ 15 quando a moeda difere) ou Payoneer; não paga em BRL ([Paddle](https://www.paddle.com/pricing)). **Não serve para cartas físicas**: proíbe produtos "that require physical delivery" |
| Polar | **Evitar**: não paga no Brasil ([Polar](https://polar.sh/docs/merchant-of-record/supported-countries)) |
| Stripe Managed Payments | Indisponível para empresas no Brasil ([Stripe](https://docs.stripe.com/payments/managed-payments/eligibility)) |
| Lemon Squeezy | Arriscado: só repassa via PayPal para o Brasil e está migrando para o Stripe Managed Payments |
| Gumroad | Funciona, mas custa 10% + 50¢ (30% via Discover) |
| Stripe Brasil direto | O fundador vira o vendedor, responsável por VAT e sales tax; +2% internacional e câmbio a partir de 2% |

- Pedir que o câmbio seja registrado como **exportação de serviço**, com **IOF zero** ([Decreto 6.306](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6306.htm), art. 15-B I), em vez dos 0,38% genéricos.
- Receita de exportação no Simples tira ISS, PIS e Cofins da guia, deixando ~3,05% efetivos na primeira faixa do Anexo III.
- Definir limite de repasse de **≥US$ 500** para diluir a taxa SWIFT de US$ 15.

## Fontes

[[Oportunidade de produto validada 2026]] (seção "Pagamento e impostos") · [[gtm_economics_payments]] (seções 5–9)
