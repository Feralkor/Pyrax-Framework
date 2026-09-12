# Descoberta e desenho de produto

Leia esta referência antes de propor solução, roadmap ou arquitetura.

## Enquadramento

Defina em linguagem operacional:

- qual decisão hoje é tardia, manual, incerta ou inexistente;
- quem percebe o sinal, quem decide, quem executa e quem responde pelo resultado;
- qual evento inicia o fluxo e qual resultado o encerra;
- custo de atraso, falso positivo, falso negativo e ação incorreta;
- restrições de processo, pessoas, tecnologia, legislação e tempo;
- baseline e resultado mensurável esperado.

Mapeie AS-IS com caminho principal, filas, esperas, handoffs, retrabalho, exceções e controles paralelos. Diferencie sintoma, causa observável e hipótese causal.

## Hipótese de produto

Formule: para **[papel]**, diante de **[estado/evento]**, o sistema detectará **[risco/oportunidade]** com **[evidência e antecedência]**, recomendará **[ação]** e medirá **[resultado]**.

Valide quatro riscos antes de escalar:

1. **Valor:** a antecipação muda uma decisão relevante?
2. **Dados:** o sinal existe com qualidade e antecedência suficientes?
3. **Usabilidade:** o usuário entende, confia e consegue agir?
4. **Viabilidade:** integração, segurança, custo e desempenho cabem na operação?

## Priorização e fatias verticais

Priorize por impacto operacional, urgência, frequência, confiança dos dados, reversibilidade, esforço e dependências. Prefira uma fatia ponta a ponta pequena — fonte, regra, sinal, interface, ação e feedback — a grandes camadas incompletas.

Cada item de backlog deve ligar problema, evidência, regra, comportamento, critério de aceitação e métrica. Use gates explícitos para impedir que funcionalidades dependentes avancem antes da certificação de dados ou regras.

## UX operacional

Projete por papel e contexto: TV/andon para consciência compartilhada, cockpit para decisão do líder e detalhe para investigação. Destaque exceções priorizadas, aging, confiança, causa conhecida ou hipótese, consequência, prazo e próxima ação. Preserve drill-down até a evidência.

Evite índices opacos. Todo índice composto precisa de componentes certificados, fórmula e explicação acessível. Distinga zero, indisponível, atrasado e não aplicável.
