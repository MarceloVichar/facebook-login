---
tags:
  - armadilha
  - padrao
atualizado: 2026-10-12
---

# Padrão: a plataforma absorve o recurso

Voltar para [[Armadilhas e ideias mortas]].

> [!warning] A regra
> Uma categoria "vazia" num marketplace pode estar vazia **porque a plataforma já a absorveu**, e não porque a demanda está sem atendimento. Quem constrói sobre a plataforma de outro vive do roteiro dela.

## Casos na pesquisa

| Ideia | O que a plataforma fez |
|---|---|
| [[Atacado e B2B para Nuvemshop (NubeSDK)]] | Lançou atacado nativo a partir do plano Impulso, além de NF-e e assinaturas nativas e gratuitas (FAQs de 17/08 e 02/10/2026) |
| [[Botão de desistência da UE fora do Shopify]] | O Shopware pôs o recurso no core (6.7.9.0), o Jimdo lançou botão nativo e o Shopify tem fluxo nativo parcial |
| [[Gerador de GPSR]] | Etsy e outros marketplaces têm campos nativos |
| [[App Forge de Gantt para Jira]] | O Timeline nativo (todos os planos) e o Plans (Premium/Enterprise) cobrem o básico |
| [[Conversor de lacuna de plataforma]] | O Embed Notion Pages perdeu 24% quando o Notion lançou embeds nativos ([TrustMRR](https://trustmrr.com/startup/embed-notion-pages)) |
| Repricers do Mercado Livre | A API bloqueou edição de preço em itens com automação nativa desde 18/03/2026 |
| Apps de NF-e | O ML tem Faturador nativo com IBS/CBS |
| [[Busca e filtros para Nuvemshop]] | Filtros nativos podem existir, e o NubeSDK pode não permitir trocar a busca (não verificado) |

## Sinais de alerta

- Mudança forçada de plataforma (NubeSDK, fim do Connect, MV2 do Chrome, Scripts do Shopify) parece uma oportunidade, mas na pesquisa os incumbentes **migraram antes** ou a plataforma **entregou o recurso**.
- O autocomplete já pergunta se a plataforma tem o recurso: "nuvemshop tem b2b", "nuvemshop tem emissor de nota fiscal".
- O FAQ ou o changelog da plataforma foi atualizado há poucas semanas sobre o tema.

## Como testar antes de construir

- Ler o FAQ, o changelog e a página de recursos da plataforma, com data.
- Perguntar direto ao suporte de parceiros (a Nuvemshop promete resposta em até 1 hora).
- Preferir apps **só de API** quando possível: na Nuvemshop, ficam fora da obrigação do NubeSDK.

## Rodada 2

- **Hotmart:** integrações gratuitas, recuperação de vendas e agente de vendas nativos absorveram os add-ons para criadores ([Hotmart](https://hotmart.com/pt-br/integracoes); [[brazil_emerging_platforms]], C10).
- **ClickUp:** está construindo a sincronização de calendário que seria um add-on ([[unmet_feature_requests]]).
- **TikTok Shop:** o próprio TikTok e a ByteDance (BytePlus Live) se sobrepõem às ferramentas de live ([[Lucro por live e comissão de host no TikTok Shop]]).

## Relacionadas

[[Padrão - governo entrega de graça]] · [[Padrão - saturação]] · [[Padrão - pagamento e CNPJ bloqueiam rotas]]
