from __future__ import annotations

from .models import ReadinessItem, ReadinessReport, ReadinessStatus

DESIGN_AREAS = {
    "problem": ("decision_to_improve", "decision_owner", "allowed_actions"),
    "sources": (),
    "entities": (),
    "signals": (),
    "decisions": (),
    "evidence": (),
    "outcomes": (),
    "guardrails": (),
}


def _presence(area: str, value: object, nested_required: tuple[str, ...] = ()) -> ReadinessItem:
    if value in (None, "", [], {}):
        return ReadinessItem(area, ReadinessStatus.NOT_STARTED, "Área ausente ou vazia")
    if nested_required and isinstance(value, dict):
        missing = [key for key in nested_required if value.get(key) in (None, "", [], {})]
        if missing:
            return ReadinessItem(
                area,
                ReadinessStatus.PARTIAL,
                f"Campos pendentes: {', '.join(missing)}",
            )
    return ReadinessItem(area, ReadinessStatus.PASS, "Cobertura mínima presente")


def _boolean_gate(area: str, value: object, reason: str) -> ReadinessItem:
    if value is True:
        return ReadinessItem(area, ReadinessStatus.PASS, reason)
    if value is False:
        return ReadinessItem(area, ReadinessStatus.BLOCKED, reason.replace("presente", "não concluído"))
    return ReadinessItem(area, ReadinessStatus.NOT_STARTED, "Evidência de conclusão não declarada")


def assess_domain_pack(pack: dict) -> ReadinessReport:
    items: list[ReadinessItem] = [
        _presence(area, pack.get(area), nested_required)
        for area, nested_required in DESIGN_AREAS.items()
    ]

    semantics = pack.get("semantics", {})
    unknowns = semantics.get("unknowns", []) if isinstance(semantics, dict) else []
    candidates = semantics.get("candidates", []) if isinstance(semantics, dict) else []
    if unknowns:
        items.append(
            ReadinessItem(
                "semantic_certification",
                ReadinessStatus.BLOCKED,
                f"{len(unknowns)} semântica(s) ainda UNKNOWN",
            )
        )
    elif candidates:
        items.append(
            ReadinessItem(
                "semantic_certification",
                ReadinessStatus.PARTIAL,
                f"{len(candidates)} semântica(s) ainda candidata(s)",
            )
        )
    else:
        items.append(
            ReadinessItem(
                "semantic_certification",
                ReadinessStatus.PASS,
                "Semânticas necessárias declaradas como certificadas",
            )
        )

    qa = pack.get("qa", {}) if isinstance(pack.get("qa", {}), dict) else {}
    golden_cases = qa.get("golden_cases")
    if isinstance(golden_cases, int) and golden_cases > 0:
        items.append(ReadinessItem("golden_cases", ReadinessStatus.PASS, f"{golden_cases} Golden Case(s) declarado(s)"))
    elif golden_cases == 0:
        items.append(ReadinessItem("golden_cases", ReadinessStatus.BLOCKED, "Nenhum Golden Case declarado"))
    else:
        items.append(ReadinessItem("golden_cases", ReadinessStatus.NOT_STARTED, "Golden Cases não declarados"))

    items.append(_boolean_gate("contract_tests", qa.get("contract_tests"), "Contract tests presentes"))
    items.append(_boolean_gate("reconciliation_tests", qa.get("reconciliation_tests"), "Reconciliation tests presentes"))

    implementation = pack.get("implementation", {}) if isinstance(pack.get("implementation", {}), dict) else {}
    items.append(_boolean_gate("runtime", implementation.get("runtime"), "Runtime presente"))
    items.append(_boolean_gate("integration_tests", implementation.get("integration_tests"), "Integration tests presentes"))
    items.append(_boolean_gate("deployment", implementation.get("deployment"), "Deployment/packaging presente"))

    return ReadinessReport(tuple(items))
