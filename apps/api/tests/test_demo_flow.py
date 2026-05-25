from __future__ import annotations

from pathlib import Path

from app.demo_fixtures import build_demo_fixture
from app.main import analyze, sample
from app.models import AnalysisRequest


def _dump(response) -> dict:
    return response.model_dump(mode="json")


def test_demo_fixture_is_controlled_and_not_live_analysis() -> None:
    fixture = build_demo_fixture()

    assert fixture.topic == "Fixture: regulation start-date contradiction"
    assert fixture.mode == "fixture_demo"
    assert fixture.limitations_ref == "LIMITATIONS.md"
    assert fixture.claims
    assert fixture.evidence
    assert fixture.sources
    assert all("fixture" in item.provenance.lower() for item in fixture.evidence)


def test_sample_fixture_response_is_identical_across_consecutive_calls() -> None:
    first = _dump(sample())
    second = _dump(sample())

    assert first == second


def test_demo_flow_exposes_claims_evidence_audit_and_uncertainty() -> None:
    payload = _dump(sample())

    assert payload["mode"] == "fixture_demo"
    assert payload["claims"]
    assert payload["evidence"]
    assert payload["audit_trail"]
    assert payload["briefing"]["limitations_ref"] == "LIMITATIONS.md"

    statuses = {claim["status"] for claim in payload["claims"]}
    assert "contested" in statuses or "unresolved" in statuses

    for claim in payload["claims"]:
        joined = " ".join(claim["confidence_reason"] + claim["limitations"]).lower()
        assert "truth verdict" in joined or "uncertainty" in joined or "fixture" in joined or "primary" in joined


def test_analyze_demo_flow_uses_user_input_as_evidence_without_external_calls() -> None:
    payload = _dump(
        analyze(
            AnalysisRequest(
                topic="Controlled local input",
                source_name="analyst-supplied-snippet",
                text="A report claims the pilot reduced costs by 30%. The report gives no denominator.",
            )
        )
    )

    assert payload["mode"] == "local_input"
    assert payload["sources"][0]["source_type"] == "user_supplied_text"
    assert payload["evidence"]
    assert all(evidence["provenance"] == "local_user_input" for evidence in payload["evidence"])
    assert all(claim["evidence_refs"] for claim in payload["claims"])
    assert "No LLM calls" in " ".join(payload["limitations"])


def test_frontend_static_verifier_requires_all_seven_dashboard_panels() -> None:
    verifier = Path("apps/web/scripts/verify-static-ui.mjs").read_text()

    required_panels = [
        "BriefingPanel",
        "ClaimMatrix",
        "EvidenceTrail",
        "AuditTrail",
        "NarrativeMap",
        "SourceSpread",
        "ContradictionBoard",
    ]
    for panel in required_panels:
        assert f"src/components/{panel}.tsx" in verifier
