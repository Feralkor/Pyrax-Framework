# Pyrax CLI and Scaffolding

The CLI turns the framework from a documentation set into an executable discovery, validation and product-composition workflow.

## Install for development

```bash
python -m pip install -e ".[dev]"
```

## Discovery

```bash
pyrax bootstrap "Organization Name"
```

This creates an intentionally incomplete discovery workspace. Generated drafts are not certified facts.

## Domain Pack validation and readiness

```bash
pyrax validate domain-pack.yaml
pyrax assess domain-pack.yaml
pyrax maturity domain-pack.yaml
```

- `validate` checks Domain Pack structure/cross-references.
- `assess` evaluates production-readiness gates.
- `maturity` reports intelligence maturity P0-P5 independently of release readiness.

## V0.5 catalogs

Inspect reusable starting points and mechanics:

```bash
pyrax profiles
pyrax profiles fleet-intelligence
pyrax catalog blocks
pyrax catalog adapters
pyrax catalog ui
```

Profiles and catalogs are reusable hypotheses. They never certify business semantics.

## Solution Manifest

Validate and materialize a composition:

```bash
pyrax manifest solution-manifest.yaml
```

The manifest selects a Solution Profile and may override blocks, adapters, UI components, maturity target and technology profile.

The manifest does not replace the Domain Pack:

- Domain Pack = domain meaning and truth contracts.
- Solution Manifest = selected reusable Pyrax composition.

## Domain Pack composition

A reusable base can be combined with explicit local overlays:

```bash
pyrax compose base-domain-pack.yaml \
  --overlay organization-overlay.yaml \
  --output domain-pack.yaml
```

Multiple `--overlay` arguments are applied in order.

Mappings merge recursively. Lists and scalar values are replaced by the later overlay. Composition reduces duplication; it is not semantic certification.

## Scaffold from a Domain Pack

```bash
pyrax scaffold my-solution \
  --domain-pack domain-pack.yaml \
  --destination ../
```

## Scaffold from a Solution Profile

```bash
pyrax scaffold fleet-ops \
  --profile fleet-intelligence \
  --domain-pack domain-pack.yaml \
  --destination ../
```

## Scaffold from a Solution Manifest

```bash
pyrax scaffold fleet-ops \
  --manifest solution-manifest.yaml \
  --domain-pack domain-pack.yaml \
  --destination ../
```

The generated project includes:

- `README.md`;
- `solution-manifest.yaml`;
- Domain Pack YAML/JSON when supplied;
- Product Charter;
- Source Map;
- Signal Catalog;
- Decision Catalog;
- Composition document;
- Evidence Contract;
- QA Plan;
- Golden Cases directory;
- domain/adapters/composition Python skeleton;
- tests/config placeholders.

Use `--allow-invalid` only during deliberate discovery work. Use `--force` only when intentionally replacing generated files.

## Recommended V0.5 workflow

```text
Organization discovery
→ Domain Pack
→ validate
→ choose Solution Profile
→ Solution Manifest
→ compose organization overlays if useful
→ assess + maturity
→ scaffold
→ bind blocks to certified domain semantics
→ implement vertical slice
→ Golden Cases
→ contract/reconciliation/integration tests
→ reassess
```

Scaffolding and composition are not certification. Generated documents and reused mechanics must be bound to evidence from the target organization.
