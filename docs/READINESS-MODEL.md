# Pyrax Readiness Model

The Readiness Model prevents a well-written Domain Pack from being mistaken for a production-ready product.

## Principle

Validation answers: **is the Domain Pack structurally valid?**

Assessment answers: **is the solution mature enough for the intended release?**

These are different questions.

## Assessed areas

### Design readiness

- problem;
- sources;
- entities;
- signals;
- decisions;
- evidence;
- outcomes;
- guardrails.

### Semantic readiness

- `semantics.unknowns` blocks production readiness;
- `semantics.candidates` keeps semantic certification `PARTIAL`;
- only the absence of unresolved required semantics allows semantic `PASS`.

### QA readiness

- at least one Golden Case;
- contract tests;
- reconciliation tests.

### Implementation readiness

- runtime implemented;
- integration tests implemented;
- deployment/packaging implemented.

## Status vocabulary

- `PASS` — evidence for this gate is present.
- `PARTIAL` — usable progress exists, but closure is incomplete.
- `BLOCKED` — a declared condition prevents production readiness.
- `NOT_STARTED` — evidence of completion was not declared.

## Production readiness

`production_ready=true` only when every assessed gate is `PASS`.

A project can still be useful in discovery, shadow mode or assisted mode while production readiness is false. Products should expose their real maturity instead of weakening gates.

## CLI

```bash
pyrax assess path/to/domain-pack.yaml
```

The command emits JSON so CI, agents or project tooling can consume the result.
