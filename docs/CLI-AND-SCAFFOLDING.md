# Pyrax CLI and Scaffolding

The CLI turns the framework from a documentation set into an executable starting point for new solutions.

## Install for development

```bash
python -m pip install -e ".[dev]"
```

## Validate

Validate a Domain Pack against the canonical schema:

```bash
pyrax validate domain-packs/my-domain/domain-pack.yaml
```

Exit code `0` means structurally valid. Exit code `1` means schema errors were found.

## Assess

Assess solution maturity:

```bash
pyrax assess domain-packs/my-domain/domain-pack.yaml
```

The command returns a machine-readable JSON report. Exit code `0` is reserved for full production readiness; exit code `2` means the Domain Pack is valid/useful but one or more readiness gates are not complete.

## Scaffold

Generate a new solution skeleton:

```bash
pyrax scaffold my-solution \
  --domain-pack domain-packs/my-domain/domain-pack.yaml \
  --destination ../
```

The scaffolder validates the Domain Pack first and then generates:

- `README.md`;
- `domain-pack.yaml` and `domain-pack.json`;
- Product Charter;
- Source Map;
- Signal Catalog;
- Decision Catalog;
- QA Plan;
- Golden Cases directory;
- Python package skeleton;
- tests/config placeholders.

Use `--allow-invalid` only during deliberate discovery work. Use `--force` only when intentionally replacing generated files.

## Recommended workflow

```text
Discovery Worksheet
→ Domain Pack
→ pyrax validate
→ pyrax assess
→ pyrax scaffold
→ implement vertical slice
→ add Golden Cases
→ add contract/reconciliation/integration tests
→ reassess
```

Scaffolding is not certification. Generated documents are starting artifacts and must be filled with domain evidence.
