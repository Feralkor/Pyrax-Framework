# Pyrax MCP v0.1.1 — Product Validation Record

Status: MECHANICAL VALIDATION COMPLETE / BLINDED AGENT EXECUTION REQUIRED

## Scope completed

The repository contains the deterministic validation infrastructure required to evaluate Pyrax MCP without using an LLM as judge:

- Golden Case evaluation harness;
- company-neutral Inteligência Operacional D+1 case;
- three adversarial cases;
- optional privacy-safe MCP audit log;
- public API/MCP contract snapshots;
- generic stdio host configuration;
- blinded experiment protocol;
- experiment aggregation and GO/NO-GO gate;
- complete eight-run blinded execution pack;
- complete eight-run result template.

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

The repository CI baseline completed successfully before the blinded run pack was added. The run pack and result-template commits are documentation/data-only experiment preparation and do not alter Pyrax runtime behavior.

## Blinded execution package

Use:

- `examples/validation/mcp-v0.1.1-blind-run-pack.yaml` as the only case input supplied to the isolated agent/host;
- `examples/validation/mcp-v0.1.1-run-template.yaml` to record the eight outputs;
- `docs/validation/MCP-0.1.1-VALIDATION-PROTOCOL.md` as the execution protocol.

The blind run pack intentionally excludes all expected findings, forbidden claims, expected unknowns, expected decisions and expected calculation outputs.

## Empirical product validation

Not yet claimed.

A valid empirical result requires a blinded agent/host that has not inspected the `expected` sections of the frozen cases. The current development conversation has already inspected those expectations and therefore must not be used as product-evidence input.

Running the eight cases inside this same conversation would be a protocol rehearsal, not blinded evidence, and must not be used to promote the release.

## Promotion rule

Do not mark Pyrax MCP v0.1.1 as internally product-validated, and do not open MCP v0.2 as an approved product milestone, until:

1. all four frozen cases are executed under `baseline`;
2. the same four cases are executed under `pyrax_mcp` using the same model/version;
3. observations are normalized and scored by `evaluate_mcp_experiment()`;
4. the deterministic gate passes;
5. the results and qualitative workflow impact are recorded here.

## Current conclusion

All engineering, experiment design, case freezing, privacy safeguards, normalization contracts and GO/NO-GO mechanics are complete. The only remaining release gate is behavioral evidence from an isolated blinded agent/host.
