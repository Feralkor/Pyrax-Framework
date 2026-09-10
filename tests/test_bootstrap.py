from pathlib import Path

from pyrax.bootstrap import bootstrap_discovery


def test_bootstrap_creates_discovery_workspace(tmp_path: Path) -> None:
    root = bootstrap_discovery(
        "Example Company",
        tmp_path,
        archetype="predictive-operations",
    )

    assert root.name == "example-company-discovery"
    assert (root / "organization-profile.yaml").exists()
    assert (root / "DISCOVERY-WORKSHEET.md").exists()
    assert (root / "DATA-INVENTORY.md").exists()
    assert (root / "SOLUTION-ARCHETYPE.md").exists()
    assert (root / "domain-pack.draft.yaml").exists()
    assert (root / "NEXT-STEPS.md").exists()

    archetype = (root / "SOLUTION-ARCHETYPE.md").read_text(encoding="utf-8")
    assert "predictive-operations" in archetype

    draft = (root / "domain-pack.draft.yaml").read_text(encoding="utf-8")
    assert "discovery-incomplete" in draft
    assert "HUMAN_ASSISTED" in draft
