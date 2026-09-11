import json
from pathlib import Path

from pyrax_mcp.tools import pyrax_get_catalog, pyrax_validate_domain_pack


def test_audit_is_disabled_by_default(tmp_path: Path, monkeypatch) -> None:
    audit = tmp_path / "audit.jsonl"
    monkeypatch.delenv("PYRAX_MCP_AUDIT_LOG", raising=False)

    result = pyrax_get_catalog("blocks")

    assert result["found"] is True
    assert audit.exists() is False


def test_audit_records_metadata_without_payloads(tmp_path: Path, monkeypatch) -> None:
    audit = tmp_path / "audit.jsonl"
    monkeypatch.setenv("PYRAX_MCP_AUDIT_LOG", str(audit))
    sensitive_marker = "DO-NOT-LOG-THIS"

    result = pyrax_validate_domain_pack(
        {
            "name": sensitive_marker,
        }
    )

    assert result["valid"] is False
    lines = audit.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1

    record = json.loads(lines[0])
    assert record["tool"] == "pyrax_validate_domain_pack"
    assert record["outcome"] == "success"
    assert record["summary"]["valid"] is False
    assert "framework_version" in record
    assert "api_version" in record
    assert "duration_ms" in record
    assert sensitive_marker not in lines[0]
    assert "domain_pack" not in lines[0]
