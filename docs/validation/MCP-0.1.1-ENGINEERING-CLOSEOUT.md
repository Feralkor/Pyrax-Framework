# Pyrax MCP v0.1.1 — Engineering Closeout

Status: **ENGINEERING COMPLETE / EXTERNAL BLINDED VALIDATION PENDING**

Closeout date: 2026-09-11

## Scope frozen

The engineering scope for Pyrax MCP v0.1.1 is complete.

Current product boundaries are intentionally frozen until the blinded product-validation gate is executed:

- Pyrax Framework package: `0.5.0`;
- public Pyrax API contract: v0.1;
- MCP validation track: v0.1.1;
- transport: local stdio;
- public MCP surface: exactly six read-only tools;
- no direct operational-system access;
- no file-writing/scaffold side effects through MCP;
- no Streamable HTTP deployment;
- no OAuth, billing, multi-tenancy or marketplace distribution.

## Double-check completed

The final engineering review confirmed:

- framework/package version alignment at `0.5.0`;
- `pyrax-mcp` entry point is registered;
- MCP server exposes exactly the six frozen read-only tools;
- MCP tools delegate to `pyrax.api` instead of invoking/parsing CLI output;
- public API and MCP contract snapshots are present;
- deterministic evaluation and experiment aggregation are covered by tests;
- audit logging is opt-in and excludes input payloads/full results;
- public reference material remains company-neutral and uses **Inteligência Operacional** for the internal-origin reference case;
- the eight-run blind execution pack contains no `expected`, forbidden-claim, expected-UNKNOWN, expected-decision or expected-calculation answer metadata;
- the latest full GitHub Actions baseline for the finalized blinded execution package completed successfully.

## Frozen MCP v0.1 tool surface

1. `pyrax_validate_domain_pack`
2. `pyrax_assess_readiness`
3. `pyrax_assess_maturity`
4. `pyrax_validate_solution_manifest`
5. `pyrax_get_solution_profile`
6. `pyrax_get_catalog`

All six tools remain read-only and closed-world.

## External blinded validation handoff

The remaining gate is behavioral evidence, not engineering work.

Use these files in an isolated agent/host that has not read the Golden Case expectations:

- `examples/validation/mcp-v0.1.1-blind-run-pack.yaml` — eight blinded inputs;
- `examples/validation/mcp-v0.1.1-run-template.yaml` — result capture contract;
- `docs/validation/MCP-0.1.1-VALIDATION-PROTOCOL.md` — execution protocol;
- `docs/validation/MCP-0.1.1-PRODUCT-VALIDATION.md` — canonical validation record.

The isolated run must execute four cases under `baseline` and the same four under `pyrax_mcp`, using the same model/version for paired runs when possible.

## Promotion gate

Do not mark v0.1.1 as internally product-validated and do not begin approved MCP v0.2 implementation until:

1. all eight blinded runs are complete;
2. observations are frozen before evaluation;
3. `evaluate_mcp_experiment()` is executed;
4. the deterministic gate returns GO;
5. the empirical results are recorded in the canonical product-validation document.

A HOLD or NO-GO result must be treated as evidence to revise the MCP/tooling hypothesis rather than bypass the gate.

## Candidate v0.2 scope after GO

Only after promotion may the next engineering phase consider:

- Domain Pack composition through MCP;
- controlled scaffold generation with explicit side-effect boundaries;
- approval semantics for write-capable operations;
- internal Streamable HTTP transport.

OAuth, billing, multi-tenancy, public marketplace distribution and direct operational-system connectivity remain separate future gates.

## Closeout conclusion

No additional v0.1.1 engineering work is required in the current development track. The repository is frozen at an externally testable state, and the next valid activity is the isolated blinded product experiment.
