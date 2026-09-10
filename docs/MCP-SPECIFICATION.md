# Pyrax Framework — MCP Specification

Status: **ACTIVE — INTERNAL AGENT INTERFACE v0.1**

MCP work was explicitly activated after the Pyrax Framework v0.5 productization baseline. The first implementation is intentionally internal, local and read-only. Commercial hosting, authentication, billing, multi-tenancy and direct source-system access remain out of scope until internal value and external willingness-to-pay are validated.

## Purpose

Pyrax MCP exposes canonical framework capabilities to AI agents without duplicating Pyrax business logic.

The architectural rule is:

`Pyrax Core -> pyrax.api -> CLI / MCP / future adapters`

The MCP server is an adapter. It must never become an alternative source of validation, readiness, maturity or composition truth.

## v0.1 scope

Transport: **stdio**.

Public tool surface:

- `pyrax_validate_domain_pack`
- `pyrax_assess_readiness`
- `pyrax_assess_maturity`
- `pyrax_validate_solution_manifest`
- `pyrax_get_solution_profile`
- `pyrax_get_catalog`

All v0.1 tools are read-only and operate on in-memory payloads or closed Pyrax catalogs. They do not access customer databases, credentials, external APIs or production systems.

## Public Python API

`src/pyrax/api.py` is the public programmatic boundary reused by MCP and future adapters. Every response includes:

- `framework_version`;
- `api_version`;
- operation-specific structured fields.

Invalid Domain Packs and Solution Manifests are normal validation results, not protocol failures. Unexpected implementation errors must remain visible during development and testing.

## MCP server

`src/pyrax_mcp/server.py` uses the official MCP Python SDK v2 `MCPServer`. The default run mode is stdio.

Install and run:

```bash
python -m pip install -e ".[dev]"
pyrax-mcp
```

Equivalent module execution:

```bash
python -m pyrax_mcp.server
```

## Guardrails

The MCP must never:

- fabricate missing source semantics;
- certify a field because its name appears obvious;
- convert UNKNOWN, unavailable or null into zero/false;
- mutate canonical operational state through a read-only tool;
- access production systems in v0.1;
- copy one organization's business semantics into another without explicit validation;
- allow an LLM response to overwrite canonical facts;
- weaken Pyrax validation/readiness/maturity rules merely to complete an agent task.

## Error semantics

Expected domain-validation failures are returned as structured data, for example `valid: false` plus `errors` or `validation_errors`.

MCP protocol/tool failures are reserved for malformed tool calls or unexpected implementation errors. This distinction lets an agent reason about an invalid artifact without confusing it with a server outage.

## Testing

The v0.1 release gate requires:

1. public API unit tests;
2. exact six-tool MCP surface validation;
3. read-only tool annotations;
4. in-memory MCP client calls through the official SDK;
5. structured validation failures without protocol errors;
6. existing Pyrax regression suite passing;
7. Ruff passing;
8. package build succeeding.

## Deferred work

The following remain intentionally deferred:

- `compose` and `scaffold` as MCP write/generation tools;
- Streamable HTTP deployment;
- OAuth/authentication;
- multi-tenant isolation;
- billing and quotas;
- remote telemetry/usage metering;
- customer source-system adapters exposed through MCP;
- marketplace/registry distribution.

Those capabilities require a separate validation gate and must not be pulled into v0.1 by convenience.

## Commercial progression

The intended sequence is:

`Internal stdio v0.1 -> internal composition/HTTP experiment -> paid design partner -> repeatable external use -> commercial infrastructure`

Do not build SaaS infrastructure before internal usefulness and external willingness-to-pay are demonstrated.
