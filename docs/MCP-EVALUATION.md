# Pyrax MCP Evaluation Protocol

Status: **ACTIVE — v0.1.1 VALIDATION INSTRUMENTATION**

## Purpose

Measure whether access to native Pyrax MCP tools makes an AI agent more reliable, reproducible and conservative when reasoning about operational-intelligence artifacts.

Technical correctness of the MCP server is already covered by unit/protocol tests. This protocol evaluates product value: whether the agent behaves better because Pyrax is available.

## Evaluation principle

Do not use an LLM as the canonical judge of another LLM. Golden Cases define normalized identifiers and expected deterministic outcomes. `src/pyrax/evaluation.py` scores structured observations against those expectations.

An agent observation uses this shape:

```yaml
findings: []
claims: []
unknowns: []
decision: ABSTAIN
calculations: {}
```

Golden Cases may define:

```yaml
expected:
  required_findings: []
  forbidden_claims: []
  expected_unknowns: []
  decision: ABSTAIN
  calculations: {}
```

The harness checks exact normalized identifiers. Natural-language quality may be reviewed separately, but it must not override deterministic benchmark results.

## Primary comparison

Run the same case in two conditions:

1. **Baseline** — agent receives the case and instructions but no Pyrax MCP tools.
2. **Pyrax MCP** — agent receives the same case and may call the v0.1 read-only tools.

Do not change the business facts between conditions.

## Metrics

Track at least:

- deterministic harness score;
- required findings missed;
- forbidden claims introduced;
- expected UNKNOWNs lost;
- decision/abstention correctness;
- deterministic calculations;
- time to correct assessment;
- manual corrections required;
- Pyrax invariant violations.

## First Golden Case

`golden-cases/inteligencia-operacional-d1.yaml`

The case is synthetic and company-neutral. It represents a D+1 replenishment-risk situation where demand and picking availability support a deterministic deficit calculation, but replenishment origin, lot eligibility and source-ordering policy remain UNKNOWN.

The expected behavior is:

- detect the deficit;
- calculate 35 units;
- preserve the three UNKNOWNs;
- identify the action as blocked;
- abstain from an executable replenishment recommendation;
- never invent FIFO, FEFO, origin or lot selection.

## Privacy and naming

Public Pyrax benchmark/reference cases must not contain company names, credentials, customer names, proprietary IDs or real operational values unless the information is explicitly public and intentionally included.

Internal-origin cases should be anonymized into neutral product/context names such as **Inteligência Operacional** and use synthetic or minimized values before they are committed.

## Exit gate

Do not expand to MCP v0.2 solely because the server works. Evidence for progression should show that MCP-assisted runs materially improve at least one of these dimensions without degrading the others:

- fewer unsupported assumptions;
- fewer invariant violations;
- better UNKNOWN preservation;
- fewer manual corrections;
- faster correct assessment;
- lower variance between compatible agent hosts/models.
