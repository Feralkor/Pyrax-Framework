# Reusable agent skills

A skill is a saved set of instructions that helps an AI assistant handle similar tasks consistently.

## sistemas-preditivos-operacionais

The complete Portuguese skill captures the recurring fernandocorrea.dev method for operational predictive systems, combining product, software engineering, QA, design, data, integration, operational reliability and iterative evolution.

- [Skill instructions](sistemas-preditivos-operacionais/SKILL.md)
- [Discovery and product](sistemas-preditivos-operacionais/references/discovery-product.md)
- [Architecture and intelligence](sistemas-preditivos-operacionais/references/architecture-intelligence.md)
- [Reliability and delivery](sistemas-preditivos-operacionais/references/reliability-delivery.md)
- [Agent metadata](sistemas-preditivos-operacionais/agents/openai.yaml)

The five source files are an unchanged copy of the approved skill. They contain no customer-specific datasets or runtime dependencies. Installation or discovery by an assistant is separate from storing this copy in GitHub.

## Use

Copy the complete `sistemas-preditivos-operacionais` directory into the skill directory supported by your assistant, preserving its references and metadata. Where supported, invoke `$sistemas-preditivos-operacionais` or allow implicit selection through the supplied metadata.

Examples:

- `$sistemas-preditivos-operacionais conceba um sistema para antecipar paradas em uma fábrica.`
- `$sistemas-preditivos-operacionais transforme este processo manual em um produto operacional confiável.`
- `$sistemas-preditivos-operacionais avalie esta arquitetura e proponha o próximo incremento.`

## Relationship to canonical Pyrax contracts

This portable methodology complements Pyrax; repository changes still follow [AGENTS.md](../AGENTS.md) and canonical framework contracts.

- The skill's descriptive-to-adaptive progression is conceptual guidance, not a replacement for [Pyrax maturity P0–P5](../docs/MATURITY-MODEL.md). Do not assume a one-to-one mapping.
- Production readiness is assessed separately through the [Readiness Model](../docs/READINESS-MODEL.md). A mature concept or structurally valid artifact is not production certification.
- Domain meaning belongs in Domain Packs; selected reusable components belong in Solution Manifests, as defined in [Productization and Composition](../docs/PRODUCTIZATION-AND-COMPOSITION.md).
- Evidence and component-level confidence follow [Evidence Standard](../docs/EVIDENCE-STANDARD.md) and [Confidence Model](../docs/CONFIDENCE-MODEL.md). Preserve UNKNOWN and abstain when required evidence is insufficient.
- The skill grants no additional execution permissions and does not expand the [MCP tool surface](../docs/MCP-SPECIFICATION.md).

## Maintenance

Keep the skill source as the versioned artifact rather than committing duplicate ZIP binaries. To package from the repository root:

```bash
python -m zipfile -c sistemas-preditivos-operacionais.zip skills/sistemas-preditivos-operacionais
```

Review future revisions against canonical Pyrax contracts. Validate skill metadata, relative links and package contents; use behavioral evaluation when the method itself changes.
