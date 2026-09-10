from __future__ import annotations

from .models import ReadinessItem, ReadinessReport, ReadinessStatus


REQUIRED_AREAS = {
    "problem": ("decision_to_improve", "decision_owner", "allowed_actions"),
    "sources": (),
    "entities": (),
    "signals": (),
    "decisions": (),
    "evidence": (),
    "outcomes": (),
    "guardrails": (),
}


def assess_domain_pack(pack: dict) -> ReadinessReport:
    items: list[ReadinessItem] = []
    for area, nested_required in REQUIRED_AREAS.items():
        value = pack.get(area)
        if value in (None, "", [], {}):
            items.append(ReadinessItem(area, ReadinessStatus.NOT_STARTED, "Área ausente ou vazia"))
            continue
        if nested_required and isinstance(value, dict):
            missing = [key for key in nested_required if value.get(key) in (None, "", [], {})]
            if missing:
                items.append(
                    ReadinessItem(
                        area,
                        ReadinessStatus.PARTIAL,
                        f"Campos pendentes: {', '.join(missing)}",
                    )
                )
                continue
        items.append(ReadinessItem(area, ReadinessStatus.PASS, "Cobertura mínima presente"))

    semantics = pack.get("semantics", {})
    unknowns = semantics.get("unknowns", []) if isinstance(semantics, dict) else []
    if unknowns:
        items.append(
            ReadinessItem(
                "semantic_certification",
                ReadinessStatus.PARTIAL,
                f"{len(unknowns)} semântica(s) ainda UNKNOWN",
            )
        )
    else:
        items.append(
            ReadinessItem(
                "semantic_certification",
                ReadinessStatus.PASS,
                "Nenhum UNKNOWN declarado",
            )
        )

    return ReadinessReport(tuple(items))
