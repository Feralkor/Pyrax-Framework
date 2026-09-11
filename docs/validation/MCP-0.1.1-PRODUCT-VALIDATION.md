# Pyrax MCP v0.1.1 — Product Validation Record

Status: ENGINEERING COMPLETE / BLINDED AGENT EXECUTION REQUIRED

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
- complete eight-run result template;
- formal engineering closeout.

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

The finalized blinded execution package baseline at commit `5a2774997a5244e35a4bac61440019a02be70fb0` completed the full `Pyrax Framework Quality` GitHub Actions workflow successfully. The subsequent closeout changes only align documentation/status and do not expand the frozen MCP business surface.

## Blinded execution package

Use:

- `examples/validation/mcp-v0.1.1-blind-run-pack.yaml` as the only case input supplied to the isolated agent/host;
- `examples/validation/mcp-v0.1.1-run-template.yaml` to record the eight outputs;
- `docs/validation/MCP-0.1.1-VALIDATION-PROTOCOL.md` as the execution protocol;
- `docs/validation/MCP-0.1.1-ENGINEERING-CLOSEOUT.md` as the engineering handoff record.

The blind run pack intentionally excludes all expected findings, forbidden claims, expected unknowns, expected decisions and expected calculation outputs.

## Empirical product validation

Not yet claimed.

A valid empirical result requires a blinded agent/host that has not inspected the `expected` sections of the frozen cases. The current development conversation has already inspected those expectations and therefore must not be used as product-evidence input.

Running the eight cases inside this same conversation would be a protocol rehearsal, not blinded evidence, and must not be used to promote the release.

## Promotion rule

Do not mark Pyrax MCP v0.1.1 as internally product-validated, and do not open MCP v0.2 as an approved product milestone, until:

1. all four frozen cases are executed under `baseline`;
2. the same four cases are executed under `pyrax_mcp` using the same model/version;
3. observations are frozen before evaluation;
4. observations are normalized and scored by `evaluate_mcp_experiment()`;
5. the deterministic gate passes with GO;
6. the results and qualitative workflow impact are recorded here.

## Current conclusion

All v0.1.1 engineering, experiment design, case freezing, privacy safeguards, normalization contracts and GO/NO-GO mechanics are complete. No additional development is required in this track before the external blinded experiment. The only remaining release gate is behavioral evidence from an isolated agent/host.
