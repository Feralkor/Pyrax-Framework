---
name: sistemas-preditivos-operacionais
description: Conceber, avaliar ou evoluir sistemas operacionais que antecipam riscos, gargalos e oportunidades com dados, regras, software e decisão assistida. Use para produtos preditivos, control towers, digital twins, automações operacionais e plataformas modulares; não use para previsões isoladas sem fluxo operacional ou para dashboards meramente descritivos.
---

# Sistemas Preditivos Operacionais

Transforme uma dor operacional em um sistema confiável, explicável e acionável. Atue de forma integrada como produto, engenharia de software, arquitetura, dados/IA, QA, UX e liderança técnica, sem confundir responsabilidades nem inventar evidência.

## Princípios invariantes

- Comece pela decisão e pelo resultado operacional, não pela tecnologia ou pelo dashboard.
- Trate a fonte da verdade, o grão, a semântica, o tempo e a qualidade dos dados como pré-condições da inteligência.
- Separe explicitamente: fato observado, regra determinística, hipótese, projeção estatística, recomendação e ação executada.
- Prefira prevenção determinística e explicável antes de ML. Adicione IA somente quando ela produzir ganho verificável.
- Mantenha intervenção humana proporcional ao impacto e à confiança. Uma previsão orienta; não autoriza ação crítica por si só.
- Projete integração, observabilidade, recuperação, segurança e auditoria como partes do produto.
- Use núcleo reutilizável mais pacote de domínio variável; evite acoplar o método a um cliente, setor, banco ou stack.

## Ciclo de concepção

Use esta sequência como mapa de decisão, adaptando profundidade e artefatos ao risco:

1. **Problema** — defina ator, processo AS-IS, dor, decisão, impacto, restrições e métrica de resultado.
2. **Evidência** — identifique fonte da verdade, fatos disponíveis, lacunas, hipóteses e nível de confiança.
3. **Modelo de domínio** — modele entidades, estados, eventos, regras, exceções e linguagem operacional.
4. **Dados** — certifique grão, chaves, timestamps, cardinalidade, cobertura, linhagem, qualidade e reconciliação.
5. **Regras** — formalize cálculos, elegibilidade, thresholds, prioridades, SLAs e condições de exceção.
6. **Inteligência** — produza sinais de risco/oportunidade com evidência, confiança, horizonte e explicação.
7. **Interface** — entregue a informação certa, no momento certo, ao papel certo, com ação e consequência claras.
8. **Ação** — defina recomendação, responsável, autorização, execução, confirmação, reversão e escalonamento.
9. **Feedback** — registre resultado, falsos positivos, desvios, decisões humanas e aprendizado para a próxima versão.

Antes de propor arquitetura ou backlog, leia [references/discovery-product.md](references/discovery-product.md). Para decisões de arquitetura, dados, regras ou IA, leia [references/architecture-intelligence.md](references/architecture-intelligence.md). Para implementação, automação, validação ou entrada em operação, leia [references/reliability-delivery.md](references/reliability-delivery.md).

## Progressão de maturidade

Classifique o estágio atual e proponha apenas o próximo avanço sustentável:

`Descritivo → Diagnóstico → Monitoramento → Preditivo → Prescritivo → Adaptativo`

Não chame de preditivo o que apenas exibe o passado. Não avance se o nível anterior não tiver dados e comportamento certificados. Quando a evidência for insuficiente, entregue diagnóstico da lacuna e plano de instrumentação.

## Forma da solução

Estruture a proposta como:

`Núcleo operacional + Pacote de domínio + Integrações + Regras específicas + UX específica`

O núcleo deve concentrar contratos, eventos, evidências, sinais, auditoria, observabilidade e ciclo de feedback. O pacote de domínio contém vocabulário, entidades, regras, métricas, riscos, ações e configurações próprias da operação. Adapters isolam fontes e destinos.

## Saída mínima

Produza somente os artefatos úteis à decisão atual, mas cubra:

- objetivo, usuários, decisão operacional e métrica de sucesso;
- mapa AS-IS e fluxo futuro, incluindo exceções e fronteiras do sistema;
- inventário e contrato das fontes de dados, com riscos de qualidade;
- modelo de domínio, estados, eventos, regras e sinais explicáveis;
- arquitetura modular, integrações, autorização e observabilidade;
- UX operacional orientada a exceções e ações, não apenas indicadores;
- backlog incremental com critérios de aceitação, dependências e gates;
- estratégia de testes, validação com dados reais e rollout seguro;
- riscos, suposições, limites, pendências e próxima decisão recomendada.

Declare o que é fato, inferência e proposta. Ao detectar lacunas críticas, não fabrique precisão: descreva a evidência necessária e o experimento mínimo para obtê-la.

## Definição de pronto

Considere um incremento pronto apenas quando o comportamento esperado estiver comprovado: objetivo e critérios atendidos; dados reconciliados; testes relevantes aprovados; erros e estados vazios tratados; logs, métricas e rastreabilidade disponíveis; segurança e performance compatíveis com a operação; documentação atualizada; limitações explícitas; validação do usuário operacional; e plano seguro de ativação, rollback ou intervenção.

Feche cada ciclo com `Previsto/Recomendado → Ação → Resultado → Aprendizado`, usando o resultado observado para recalibrar regras, UX e prioridades.
