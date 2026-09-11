# Pyrax MCP v0.1 — Internal Agent Interface

Status: TECHNICALLY VALIDATED / V0.1.1 ENGINEERING COMPLETE / BLINDED PRODUCT VALIDATION PENDING

## Goal

Prove that an AI agent becomes more reliable and efficient at applying Pyrax methodology when framework capabilities are available as native MCP tools instead of being reconstructed from prompts or CLI output.

## Scope

V0.1 is deliberately narrow:

- local stdio transport;
- six read-only tools;
- no direct source-system access;
- no file generation;
- no authentication/billing/multi-tenancy;
- no remote deployment requirement.

## Install

```bash
python -m pip install -e ".[dev]"
```

This installs both:

```bash
pyrax
pyrax-mcp
```

## Run

```bash
pyrax-mcp
```

`pyrax-mcp` communicates over stdin/stdout using MCP. It is intended to be launched by an MCP-capable host rather than used as an interactive terminal program.

A vendor-neutral reference configuration is available under `examples/mcp-hosts/`.

Generic host configuration shape:

```json
{
  "mcpServers": {
    "pyrax": {
      "command": "pyrax-mcp"
    }
  }
}
```

Host-specific configuration locations vary; keep the command contract independent of any one client.

## Tools

### `pyrax_validate_domain_pack`
Validates Domain Pack schema and Pyrax cross-reference integrity.

### `pyrax_assess_readiness`
Returns production-readiness gates after validation.

### `pyrax_assess_maturity`
Returns cumulative Pyrax maturity P0-P5 after validation.

### `pyrax_validate_solution_manifest`
Validates Solution Manifest structure and catalog references.

### `pyrax_get_solution_profile`
Lists available Solution Profile ids when called without a profile id, or returns one profile when supplied.

### `pyrax_get_catalog`
Returns one closed catalog: `blocks`, `adapters`, or `ui`.

## V0.1.1 validation instrumentation

V0.1.1 adds measurement and contract-protection capabilities without expanding the six-tool business surface.

Delivered instrumentation:

- deterministic evaluation harness in `src/pyrax/evaluation.py`;
- synthetic **Inteligência Operacional** D+1 Golden Case;
- initial adversarial cases for uncertified semantics, NULL-as-zero and conflicting sources;
- optional metadata-only local MCP audit log;
- public API/MCP contract snapshots;
- vendor-neutral local stdio host examples;
- experiment aggregation and GO/NO-GO gate;
- complete eight-run blinded execution pack and result template;
- CI enforcement that public reference material remains company-neutral.

### Engineering closeout

The v0.1.1 engineering phase is complete. No additional business tools, transports or deployment infrastructure should be added until the isolated blinded experiment is executed and the promotion gate passes.

Canonical closeout:

`docs/validation/MCP-0.1.1-ENGINEERING-CLOSEOUT.md`

Blinded execution package:

- `examples/validation/mcp-v0.1.1-blind-run-pack.yaml`;
- `examples/validation/mcp-v0.1.1-run-template.yaml`;
- `docs/validation/MCP-0.1.1-VALIDATION-PROTOCOL.md`.

### Optional local audit

Audit is disabled by default. Enable it only by explicitly setting:

```text
PYRAX_MCP_AUDIT_LOG=/local/private/path/pyrax-mcp-audit.jsonl
```

Each JSONL record contains only metadata such as tool name, framework/API version, UTC timestamp, duration, outcome and a small whitelisted result summary. Tool arguments, Domain Packs, Solution Manifests and full results are not logged.

Local audit files are operational artifacts and must not be committed to this repository.

### Contract stability

`tests/fixtures/public-api-contract.yaml` is the current API v0.1 contract snapshot. Tests fail when public response keys or the six-tool MCP surface change without an explicit contract update.

Backward-incompatible changes require an intentional API-version decision rather than an incidental code edit.

## Example agent workflow

A strong internal Golden Case is:

1. provide an Inteligência Operacional Domain Pack or synthetic operational case to the agent;
2. call `pyrax_validate_domain_pack`;
3. call `pyrax_assess_readiness`;
4. call `pyrax_assess_maturity`;
5. ask the agent to explain only what the returned evidence supports;
6. normalize the agent observation;
7. score it with `src/pyrax/evaluation.py`;
8. verify that UNKNOWN/blocked semantics are not invented away.

The comparison baseline is the same task performed without MCP, using only prompting/documentation.

Reference and benchmark cases must not expose company names, credentials, customer identifiers or proprietary operational values. Use neutral product names and synthetic/minimized data.

## Validation metrics

Track at least:

- deterministic harness score;
- time to first correct assessment;
- number of unsupported assumptions introduced by the agent;
- number of Pyrax rule violations;
- number of manual corrections needed;
- usefulness of readiness/maturity output;
- whether the agent chooses to abstain when evidence is insufficient;
- variance between compatible agent hosts/models when the same case is used.

## Security boundary

V0.1 tools only process user-supplied in-memory documents and framework-owned catalogs. They do not connect to Oracle, Senior WMS, PostgreSQL, telemetry providers, REST APIs or external files on behalf of the agent.

## Exit criteria for v0.2

Do not expand the MCP merely because v0.1 works technically. Move forward only after the isolated blinded v0.1.1 product experiment passes the deterministic promotion gate and the empirical result is recorded.

Candidate v0.2 capabilities are:

- Domain Pack composition;
- controlled scaffold generation;
- internal Streamable HTTP deployment.

Each adds a new side-effect or deployment boundary and therefore needs its own tests and guardrails.
