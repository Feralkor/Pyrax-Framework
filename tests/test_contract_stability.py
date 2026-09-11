import asyncio
from pathlib import Path

import yaml
from mcp import Client

from pyrax.api import (
    API_VERSION,
    assess_maturity,
    assess_readiness,
    get_catalog,
    get_solution_profile,
    validate_domain_pack,
    validate_solution_manifest,
)
from pyrax.validation import load_document
from pyrax_mcp.server import mcp

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "tests" / "fixtures" / "public-api-contract.yaml"
DOMAIN_PACK = ROOT / "tests" / "fixtures" / "minimal-domain-pack.yaml"


def _contract() -> dict:
    with CONTRACT.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _assert_keys(operation: str, payload: dict) -> None:
    expected = set(_contract()["operations"][operation]["keys"])
    assert set(payload) == expected


def test_public_api_contract_snapshot() -> None:
    contract = _contract()
    pack = load_document(DOMAIN_PACK)

    assert API_VERSION == contract["api_version"]
    _assert_keys("validate_domain_pack", validate_domain_pack(pack))
    _assert_keys("assess_readiness", assess_readiness(pack))
    _assert_keys("assess_maturity", assess_maturity(pack))
    _assert_keys(
        "validate_solution_manifest",
        validate_solution_manifest({"profile": "fleet-intelligence"}),
    )
    _assert_keys("get_solution_profile_list", get_solution_profile())
    _assert_keys("get_solution_profile_item", get_solution_profile("fleet-intelligence"))
    _assert_keys("get_catalog", get_catalog("blocks"))


def test_mcp_tool_surface_matches_contract_snapshot() -> None:
    expected = set(_contract()["mcp"]["tools"])

    async def scenario() -> None:
        async with Client(mcp) as client:
            result = await client.list_tools()
            assert {tool.name for tool in result.tools} == expected

    asyncio.run(scenario())
