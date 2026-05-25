from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.main import analyze, app, audit_verify, health, ingest_manual, sample
from app.models import AnalysisRequest, ManualIngestRequest

REQUIRED_TOP_LEVEL_KEYS = {
    "schema_version",
    "mode",
    "topic",
    "claims",
    "evidence",
    "sources",
    "source_graph",
    "contradictions",
    "briefing",
    "audit_trail",
    "audit_verification",
    "limitations",
    "limitations_ref",
}


def _dump(response) -> dict:
    return response.model_dump(mode="json")


def assert_contract_response(payload: dict) -> None:
    assert REQUIRED_TOP_LEVEL_KEYS <= payload.keys()
    assert payload["schema_version"] == "lumen.analysis.v0.3"
    assert payload["mode"] in {"fixture_demo", "local_input"}
    assert payload["limitations"]
    assert payload["limitations_ref"] == "LIMITATIONS.md"
    assert payload["audit_trail"]
    assert payload["audit_verification"]["valid"] is True

    audit_hashes = {event["event_hash"] for event in payload["audit_trail"]}
    evidence_ids = {item["id"] for item in payload["evidence"]}

    for claim in payload["claims"]:
        assert claim["status"]
        assert claim["confidence_reason"]
        assert claim["evidence_refs"]
        assert set(claim["evidence_refs"]) <= evidence_ids
        assert claim["audit_reference"] in audit_hashes
        assert claim["limitations_ref"] == "LIMITATIONS.md"

    briefing = payload["briefing"]
    assert briefing["limitations"]
    assert briefing["limitations_ref"] == "LIMITATIONS.md"
    assert briefing["audit_reference"] in audit_hashes


def test_health_route_reports_v04_local_demo_boundaries() -> None:
    payload = health()

    assert payload["status"] == "ok"
    assert payload["service"] == "lumen-api"
    assert payload["version"] == "0.4.0"
    assert payload["deterministic"] is True
    assert "not a new oracle" in payload["doctrine"]
    assert any("No LLM calls" in limitation for limitation in payload["limitations"])


def test_sample_returns_stable_v03_contract() -> None:
    payload = _dump(sample())

    assert payload["mode"] == "fixture_demo"
    assert_contract_response(payload)


def test_sample_route_returns_stable_documented_fixture_response() -> None:
    route_paths = {route.path for route in app.routes}
    assert "/sample" in route_paths

    payload = _dump(sample())
    assert payload["mode"] == "fixture_demo"
    assert payload["topic"] == "Fixture: regulation start-date contradiction"
    assert_contract_response(payload)


def test_analyze_returns_stable_v03_contract_with_local_input_evidence() -> None:
    payload = _dump(
        analyze(
            AnalysisRequest(
                topic="Fixture user supplied text",
                source_name="local-test-input",
                text="An agency said the program doubled results. An unnamed official said the change caused delays.",
            )
        )
    )

    assert payload["mode"] == "local_input"
    assert_contract_response(payload)
    assert all(item["provenance"] == "local_user_input" for item in payload["evidence"])


def test_analyze_route_returns_local_input_contract_without_external_capability_claims() -> None:
    route_paths = {route.path for route in app.routes}
    assert "/analyze" in route_paths

    payload = _dump(
        analyze(
            AnalysisRequest(
                topic="Route local input",
                source_name="operator-paste",
                text="The agency said the review remains unresolved. A report claims the pilot reduced costs by 30%.",
            )
        )
    )

    assert payload["mode"] == "local_input"
    assert_contract_response(payload)
    assert all(item["provenance"] == "local_user_input" for item in payload["evidence"])
    assert "No LLM calls" in " ".join(payload["limitations"])


def test_manual_ingest_creates_assertion_container_without_url_fetching() -> None:
    route_paths = {route.path for route in app.routes}
    assert "/ingest/manual" in route_paths

    payload = ingest_manual(
        ManualIngestRequest(
            input_method="manual_text",
            raw_text="The local article claims the program begins on June 1.",
            title="Manual article assertion",
            source_name="Operator pasted article",
            source_url="https://example.invalid/not-fetched",
        )
    ).model_dump(mode="json")

    assert payload["schema_version"] == "lumen.ingest.manual.v0.6"
    assert payload["mode"] == "manual_input"
    assert payload["limitations_ref"] == "LIMITATIONS.md"
    assert any("No URL fetching" in limitation for limitation in payload["limitations"])

    raw_document = payload["raw_document"]
    assert raw_document["state"] == "normalized"
    assert raw_document["input_method"] == "manual_text"
    assert raw_document["source_url"] == "https://example.invalid/not-fetched"
    assert raw_document["source_url_fetched"] is False
    assert raw_document["content_hash"].startswith("sha256:")
    assert raw_document["audit_reference"] in {event["event_hash"] for event in payload["audit_trail"]}
    assert "assertion container" in " ".join(raw_document["limitations"]).lower()

    source_document = payload["source_document"]
    assert source_document["raw_document_id"] == raw_document["raw_document_id"]
    assert source_document["state"] == "ready_for_local_analysis"
    assert source_document["source_assertion_type"] == "user_supplied"
    assert source_document["analysis_allowed"] is True
    assert source_document["audit_reference"] in {event["event_hash"] for event in payload["audit_trail"]}
    assert "must not be treated as verified" in " ".join(source_document["limitations"]).lower()
    assert payload["audit_verification"]["valid"] is True


def test_manual_ingest_rejects_live_ingestion_modes() -> None:
    with pytest.raises(ValidationError) as exc:
        ManualIngestRequest(source_name="operator", raw_text="https://example.invalid/live", input_method="url")  # type: ignore[arg-type]

    assert "manual_text" in str(exc.value)


def test_audit_verify_route_returns_valid_sample_chain() -> None:
    route_paths = {route.path for route in app.routes}
    assert "/audit/verify" in route_paths

    payload = audit_verify()
    assert payload["valid"] is True
    assert payload["event_count"] >= 5
    assert isinstance(payload["genesis_event_hash"], str)
    assert isinstance(payload["latest_event_hash"], str)
    assert len(payload["genesis_event_hash"]) == 64
    assert len(payload["latest_event_hash"]) == 64
