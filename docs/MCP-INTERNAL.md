# Pyrax MCP v0.1 — Internal Agent Interface

Status: INTERNAL VALIDATION

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

## Example agent workflow

A strong internal Golden Case is:

1. provide an Inteligência Operacional Domain Pack or synthetic operational case to the agent;
2. call `pyrax_validate_domain_pack`;
3. call `pyrax_assess_readiness`;
4. call `pyrax_assess_maturity`;
5. ask the agent to explain only what the returned evidence supports;
6. verify that UNKNOWN/blocked semantics are not invented away.

The comparison baseline is the same task performed without MCP, using only prompting/documentation.

Reference and benchmark cases must not expose company names, credentials, customer identifiers or proprietary operational values. Use neutral product names and synthetic/minimized data.

## Validation metrics

Track at least:

- time to first correct assessment;
- number of unsupported assumptions introduced by the agent;
- number of Pyrax rule violations;
- number of manual corrections needed;
- usefulness of readiness/maturity output;
- whether the agent chooses to abstain when evidence is insufficient.

## Security boundary

V0.1 tools only process user-supplied in-memory documents and framework-owned catalogs. They do not connect to Oracle, Senior WMS, PostgreSQL, telemetry providers, REST APIs or external files on behalf of the agent.

## Exit criteria for v0.2

Do not expand the MCP merely because v0.1 works technically. Move forward when internal use shows that native Pyrax tools materially improve an agent workflow.

Candidate v0.2 capabilities are:

- Domain Pack composition;
- controlled scaffold generation;
- internal Streamable HTTP deployment.

Each adds a new side-effect or deployment boundary and therefore needs its own tests and guardrails.
