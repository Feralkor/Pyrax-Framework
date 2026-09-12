# Arquitetura, dados e inteligência

Leia esta referência ao desenhar integrações, modelo canônico, regras, sinais, IA ou evolução preditiva.

## Arquitetura de referência

Separe responsabilidades:

`Fontes → Adapters → Ingestão → Normalização → Modelo canônico → Estado operacional → Regras/Métricas → Sinais → Recomendação → API/UX → Ação/Feedback`

- **Adapters** absorvem diferenças de ERP, WMS, TMS, sensores, arquivos e APIs.
- **Modelo canônico** preserva identidade, tempo, estado, evento e linhagem.
- **Motor de verdade** reconcilia fatos e expõe qualidade/cobertura.
- **Motor de antecipação** detecta risco, tendência, anomalia ou oportunidade.
- **Motor de decisão** prioriza opções, restrições e impacto; não oculta evidência.
- **Histórico operacional** guarda sinais, versões de regra/modelo, decisões, ações e resultados.

## Contrato de dados

Para cada entidade, evento ou KPI, registre: nome, definição, fonte, dono, grão, chave, timestamp e timezone, dimensões, unidade, fórmula, janela, frequência, cobertura, tolerância, exceções, linhagem e classificação de evidência.

Valide cardinalidade e duplicidade antes de agregar. Reconcilie totais e amostras com a fonte. Use sanity checks de faixa, nulidade, sequência temporal e invariantes do domínio. Ausência de dado nunca equivale automaticamente a zero.

## Contrato de sinal

Todo sinal deve declarar:

- tipo: fato, regra preventiva, anomalia, projeção, padrão ou oportunidade;
- entidade e janela temporal afetadas;
- evidência e versão da lógica;
- severidade, confiança e horizonte;
- explicação legível e fatores relevantes;
- ação sugerida, responsável, prazo e condição de escalonamento;
- validade, deduplicação e condição de encerramento.

## Escolha da inteligência

Use a técnica mínima capaz de melhorar a decisão:

- regras para restrições, thresholds, elegibilidade e prevenção conhecida;
- estatística para baseline, variabilidade, tendência e anomalias;
- simulação/digital twin para cenários e consequências;
- ML quando há histórico representativo, alvo válido, ganho mensurável e plano de monitoramento;
- LLM para explicar, resumir, priorizar, consultar contexto e apoiar investigação, nunca para inventar fatos ou substituir cálculos certificados.

Meça precisão operacional, antecedência útil, cobertura, falsos positivos/negativos, adoção da recomendação e impacto realizado. Monitore drift de dados, regra, processo e comportamento humano.

## Modularidade

Mantenha o núcleo independente do domínio. Configure vocabulário, entidades, regras, métricas, thresholds, integrações e componentes de UX em um pacote de domínio versionado. Evite condicionais de cliente espalhadas pelo código. Versione contratos e ofereça migração compatível quando possível.
