from __future__ import annotations

from pyrax.catalogs import SOLUTION_PROFILES, get_solution_profile
from pyrax.composition import compose_domain_pack, materialize_solution_manifest, validate_solution_manifest
from pyrax.scaffold import scaffold_project


def test_profiles_cover_reference_product_shapes() -> None:
    expected = {
        "fleet-intelligence",
        "asset-radar",
        "predictive-maintenance",
        "industrial-performance",
        "decision-intelligence",
    }
    assert expected.issubset(SOLUTION_PROFILES)
    assert "dead-reckoning" in get_solution_profile("fleet-intelligence")["blocks"]


def test_domain_pack_overlay_replaces_lists_and_merges_mappings() -> None:
    base = {
        "name": "Base",
        "semantics": {"certified": ["a"], "unknowns": ["b"]},
        "states": ["OPEN"],
    }
    overlay = {
        "name": "Customer",
        "semantics": {"unknowns": []},
        "states": ["OPEN", "CLOSED"],
    }
    result = compose_domain_pack(base, overlay)
    assert result["name"] == "Customer"
    assert result["semantics"]["certified"] == ["a"]
    assert result["semantics"]["unknowns"] == []
    assert result["states"] == ["OPEN", "CLOSED"]


def test_solution_manifest_inherits_profile_defaults() -> None:
    manifest = {"profile": "asset-radar"}
    assert validate_solution_manifest(manifest) == []
    resolved = materialize_solution_manifest(manifest)
    assert resolved["profile"] == "asset-radar"
    assert "telemetry" in resolved["adapters"]
    assert "object-360" in resolved["ui_components"]


def test_solution_manifest_rejects_unknown_parts() -> None:
    errors = validate_solution_manifest(
        {
            "profile": "decision-intelligence",
            "blocks": ["does-not-exist"],
            "adapters": ["sql"],
            "ui_components": ["decision-card"],
        }
    )
    assert errors == ["unknown building block: does-not-exist"]


def test_profile_scaffold_materializes_composition(tmp_path) -> None:
    pack = {
        "name": "Fleet Demo",
        "problem": {
            "decision_to_improve": "Reduce route risk",
            "decision_owner": "Dispatcher",
            "allowed_actions": ["review"],
        },
        "sources": [],
        "signals": [],
        "decisions": [],
        "implementation": {"technology_profile": "hybrid"},
    }
    root = scaffold_project(
        "fleet-demo",
        tmp_path,
        domain_pack=pack,
        solution_profile="fleet-intelligence",
    )
    text = (root / "solution-manifest.yaml").read_text(encoding="utf-8")
    composition = (root / "docs" / "COMPOSITION.md").read_text(encoding="utf-8")
    assert "fleet-intelligence" in text
    assert "dead-reckoning" in text
    assert "scenario-panel" in composition
