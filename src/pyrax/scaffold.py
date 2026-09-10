from __future__ import annotations

from pathlib import Path


FILES = {
    "README.md": "# {name}\n\nGenerated from Pyrax Framework.\n",
    "docs/PRODUCT-CHARTER.md": "# Product Charter — {name}\n\n## Problema\n\n## Decisão a melhorar\n\n## Usuário/decision owner\n\n## Ações permitidas\n",
    "docs/SOURCE-MAP.md": "# Source Map — {name}\n\n| Fonte | Autoridade | Acesso | Grão | Freshness |\n|---|---|---|---|---|\n",
    "docs/SIGNAL-CATALOG.md": "# Signal Catalog — {name}\n\n| Signal | Evidência | Regra | Severidade | Confiança |\n|---|---|---|---|---|\n",
    "docs/DECISION-CATALOG.md": "# Decision Catalog — {name}\n\n| Decision | Trigger | Recommendation | Constraints | Human approval |\n|---|---|---|---|---|\n",
    "docs/QA-PLAN.md": "# QA Plan — {name}\n\n## Golden Cases\n\n## Contract tests\n\n## Reconciliation\n\n## Failure modes\n",
    "golden-cases/README.md": "# Golden Cases\n\nDeterministic reference scenarios for regression.\n",
    "src/.gitkeep": "",
    "tests/.gitkeep": "",
    "config/.gitkeep": "",
}


def scaffold_project(name: str, destination: str | Path, *, force: bool = False) -> Path:
    root = Path(destination) / name
    if root.exists() and any(root.iterdir()) and not force:
        raise FileExistsError(f"Destination is not empty: {root}")
    root.mkdir(parents=True, exist_ok=True)
    for relative, content in FILES.items():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not force:
            continue
        target.write_text(content.format(name=name), encoding="utf-8")
    return root
