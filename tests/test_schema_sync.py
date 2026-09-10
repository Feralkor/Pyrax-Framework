import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_packaged_domain_pack_schema_matches_root_schema() -> None:
    root_schema = json.loads((ROOT / "schemas" / "domain-pack.schema.json").read_text(encoding="utf-8"))
    packaged_schema = json.loads(
        (ROOT / "src" / "pyrax" / "resources" / "domain-pack.schema.json").read_text(encoding="utf-8")
    )
    assert packaged_schema == root_schema
