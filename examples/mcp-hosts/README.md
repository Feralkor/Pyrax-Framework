# Pyrax MCP — Host Examples

These examples show the minimum local `stdio` contract needed to launch Pyrax MCP from an MCP-capable host.

They are intentionally vendor-neutral. Host-specific configuration locations and wrappers may change independently of Pyrax.

## Prerequisite

Install the repository environment so the `pyrax-mcp` console entry point is available:

```bash
python -m pip install -e ".[dev]"
```

Confirm the command is resolvable in the same environment used by the host:

```bash
pyrax-mcp
```

The command is a protocol server, not an interactive shell. An MCP host starts it and communicates through stdin/stdout.

## Generic configuration

See `stdio.generic.json`:

```json
{
  "mcpServers": {
    "pyrax": {
      "command": "pyrax-mcp"
    }
  }
}
```

If the host cannot resolve the console script, use the absolute executable path for the Python environment that installed Pyrax rather than embedding secrets or environment-specific paths in the public repository.

## Optional local audit

To record metadata-only tool-call audit events, set `PYRAX_MCP_AUDIT_LOG` in the host process environment:

```text
PYRAX_MCP_AUDIT_LOG=/local/private/path/pyrax-mcp-audit.jsonl
```

Audit logging is disabled by default. Records do not contain Domain Pack payloads, Solution Manifest payloads or full tool results.

Do not commit local audit logs to this repository.

## Validation workflow

For the first internal experiment:

1. launch Pyrax MCP through the host;
2. confirm the six v0.1 tools are visible;
3. run the synthetic Inteligência Operacional Golden Case;
4. capture the agent's normalized observation;
5. score it with the deterministic evaluation harness;
6. compare against the same task without Pyrax MCP.

See `docs/MCP-EVALUATION.md`.
