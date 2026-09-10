from pathlib import Path

from pyrax.readiness import assess_domain_pack
from pyrax.validation import load_document, load_schema, validate_domain_pack

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "minimal-domain-pack.yaml"
SCHEMA = ROOT / "schemas" / "domain-pack.schema.json"


def test_minimal_domain_pack_is_valid() -> None:
    pack = load_document(FIXTURE)
    schema = load_schema(SCHEMA)
    assert validate_domain_pack(pack, schema) == []


def test_minimal_domain_pack_is_ready() -> None:
    report = assess_domain_pack(load_document(FIXTURE))
    assert report.production_ready is True


def test_unknown_semantics_prevent_full_readiness() -> None:
    pack = load_document(FIXTURE)
    pack["semantics"]["unknowns"] = ["unvalidated_status"]
    report = assess_domain_pack(pack)
    assert report.production_ready is False
    assert any(item.area == "semantic_certification" and item.status.value == "PARTIAL" for item in report.items)
