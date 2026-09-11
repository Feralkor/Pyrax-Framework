# Pyrax MCP v0.1.1 — Product Validation Record

Status: MECHANICAL VALIDATION COMPLETE / BLINDED AGENT RUN PENDING

## Scope completed

The repository now contains the full deterministic validation infrastructure required to evaluate Pyrax MCP without using an LLM as judge:

- Golden Case evaluation harness;
- company-neutral Inteligência Operacional D+1 case;
- three adversarial cases;
- optional privacy-safe MCP audit log;
- public API/MCP contract snapshots;
- generic stdio host configuration;
- blinded experiment protocol;
- experiment aggregation and GO/NO-GO gate.

## Mechanical validation

The deterministic evaluator is covered by tests for:

- accepted conservative behavior;
- rejected semantic guessing;
- forbidden-claim detection;
- UNKNOWN preservation;
- decision matching;
- calculation matching;
- experiment aggregation across baseline and Pyrax MCP conditions;
- GO when MCP is safer/more accurate;
- NO-GO when MCP introduces a forbidden claim;
- required presence of both experiment conditions.

## Empirical product validation

Not yet claimed.

A valid empirical result requires a blinded agent/host that has not inspected the `expected` sections of the frozen cases. The current development conversation has already inspected those expectations and therefore must not be used as product-evidence input.

## Promotion rule

Do not mark Pyrax MCP v0.1.1 as internally product-validated, and do not open MCP v0.2 as an approved product milestone, until:

1. all four frozen cases are executed under `baseline`;
2. the same four cases are executed under `pyrax_mcp` using the same model/version;
3. observations are normalized and scored by `evaluate_mcp_experiment()`;
4. the deterministic gate passes;
5. the results and qualitative workflow impact are recorded here.

## Current conclusion

The validation system itself is ready and testable. The remaining evidence is behavioral, not architectural: a genuinely blinded agent run is required to determine whether MCP access materially improves the agent workflow.
