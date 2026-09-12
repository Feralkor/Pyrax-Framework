# Confiabilidade, QA e entrega iterativa

Leia esta referência ao implementar, automatizar, testar, integrar, empacotar ou colocar um incremento em operação.

## Estratégia de integração

Prefira, conforme disponibilidade e estabilidade: API suportada, acesso read-only a dados, arquivo estruturado e, por último, automação de interface. Use menor privilégio, queries parametrizadas, limites, timeouts e orçamento operacional. Isole credenciais e dados sensíveis.

Para rotinas repetíveis, assegure idempotência, deduplicação, checkpoints, retry limitado com backoff, fila de falhas, reprocessamento seletivo e confirmação do resultado. Falhe de modo visível e seguro; não continue silenciosamente com dado parcial.

## Pirâmide de validação

Escolha testes pelo risco:

- unitários para fórmulas, regras e transições de estado;
- contrato para schemas, adapters e compatibilidade;
- integração para fontes, persistência, APIs e destinos;
- golden cases e snapshots reais para reconciliação;
- regressão para invariantes e incidentes já observados;
- performance para tempo, volume e concorrência reais;
- smoke para instalação, inicialização e fluxo crítico;
- UAT para linguagem, confiança, ação e resultado operacional.

Não teste apenas o caminho feliz. Cubra nulos, duplicidade, atraso, eventos fora de ordem, fonte indisponível, dado obsoleto, reprocessamento, mudança de schema, permissão negada e ação parcialmente concluída.

## Gates de evolução

Um gate deve ter critério observável, evidência, responsável e decisão: avançar, corrigir ou limitar escopo. Gates típicos:

1. problema e métrica aprovados;
2. fonte, grão e semântica certificados;
3. regra reconciliada com casos reais;
4. fluxo ponta a ponta observável em ambiente controlado;
5. shadow mode comparando previsto/recomendado e realizado;
6. ativação assistida com rollback;
7. expansão após estabilidade e impacto comprovados.

## Operação e observabilidade

Registre correlação, versão, origem, latência, qualidade, sinal, recomendação, decisão humana, ação e resultado. Monitore disponibilidade, frescor, erros, backlog, tempo de processamento, qualidade do sinal e impacto. Defina alertas acionáveis, runbooks, ownership e SLOs compatíveis com criticidade.

## Definition of Done operacional

Além de código e testes aprovados, exija reconciliação, proteção contra regressão, mensagens e estados de erro claros, auditoria, segurança, desempenho, documentação mínima, critérios de suporte, rollback e validação com usuários e dados representativos. Limitações e riscos residuais devem permanecer explícitos.
