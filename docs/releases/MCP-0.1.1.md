# Pyrax MCP 0.1.1 — Validation Instrumentation

Status: **ENGINEERING COMPLETE / BLINDED PRODUCT VALIDATION PENDING**

## Objective

Add deterministic measurement, privacy-safe auditability and contract protection around the technically validated Pyrax MCP v0.1 before expanding the MCP tool surface or deployment model.

V0.1.1 does **not** add new business tools. The public MCP surface remains exactly six read-only tools over local stdio.

## Delivered

- deterministic evaluation harness (`src/pyrax/evaluation.py`);
- synthetic company-neutral Inteligência Operacional D+1 Golden Case;
- adversarial benchmark cases for:
  - uncertified semantic meaning;
  - NULL/unavailable values incorrectly treated as zero;
  - conflicting sources without authoritative reconciliation;
- optional metadata-only JSONL audit through `PYRAX_MCP_AUDIT_LOG`;
- public API v0.1 contract snapshot;
- exact MCP tool-surface snapshot;
- vendor-neutral stdio host examples;
- automated company-neutral public-reference guard;
- blinded baseline-vs-MCP validation protocol;
- experiment aggregation and deterministic GO/NO-GO gate;
- complete eight-run blind execution pack;
- complete eight-run result template;
- engineering closeout record.

## Evaluation contract

Agent observations are normalized into:

```yaml
findings: []
claims: []
unknowns: []
decision: ABSTAIN
calculations: {}
```

Golden Cases define deterministic expectations:

```yaml
expected:
  required_findings: []
  forbidden_claims: []
  expected_unknowns: []
  decision: ABSTAIN
  calculations: {}
```

The canonical benchmark score is produced by deterministic matching, not by another LLM.

## Privacy boundary

Public benchmark/reference material is company-neutral.

- Internal operational references use the neutral name **Inteligência Operacional**.
- Reference values are synthetic or minimized.
- Company/customer names, credentials, proprietary identifiers and private operational values must not enter public fixtures.
- CI scans public docs/examples/Golden Cases and fails if the forbidden company marker reappears.

## Audit boundary

Audit is opt-in and disabled by default.

When configured, the JSONL audit captures:

- UTC timestamp;
- tool name;
- framework version;
- public API version;
- duration;
- outcome;
- small whitelisted result summary or exception type.

It does not capture tool arguments, Domain Packs, Solution Manifests or full results.

## Contract stability

`tests/fixtures/public-api-contract.yaml` pins the API v0.1 response-key surface and MCP tool names.

Backward-incompatible changes require an explicit API-version decision.

## Engineering closeout

The v0.1.1 engineering phase is complete and frozen. The latest finalized blinded-execution-package baseline passed the full GitHub Actions quality workflow before this closeout documentation alignment.

Canonical closeout:

`docs/validation/MCP-0.1.1-ENGINEERING-CLOSEOUT.md`

No additional v0.1.1 MCP tools, transports or infrastructure should be introduced before the external blinded product experiment completes.

## Product experiment gate

The remaining milestone is a controlled comparison of the same synthetic/neutral operational cases under two conditions:

1. agent without Pyrax MCP;
2. the same class of agent with Pyrax MCP available.

Track:

- deterministic harness score;
- forbidden claims;
- missed required findings;
- lost UNKNOWNs;
- decision/abstention correctness;
- deterministic calculation correctness;
- time to correct assessment;
- manual corrections;
- variance across compatible agent hosts/models.

Do not claim internal product validation and do not begin approved v0.2 implementation until the eight blinded runs are frozen, scored and the deterministic gate returns GO.

## Candidate v0.2 scope after GO

- Domain Pack composition through MCP;
- controlled scaffold generation;
- explicit approval/side-effect boundaries;
- internal Streamable HTTP transport.

OAuth, billing, multi-tenancy, public marketplace distribution and operational-system connectivity remain outside this gate.
