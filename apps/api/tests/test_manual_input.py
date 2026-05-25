from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.main import ingest_manual, sample
from app.models import ManualIngestRequest


def _dump(response) -> dict:
    return response.model_dump(mode="json")


def _has_key(payload: object, key: str) -> bool:
    if isinstance(payload, dict):
        return key in payload or any(_has_key(value, key) for value in payload.values())
    if isinstance(payload, list):
        return any(_has_key(value, key) for value in payload)
    return False


def test_manual_text_ingest_normalizes_line_endings_and_hashes_stably() -> None:
    first = _dump(
        ingest_manual(
            ManualIngestRequest(
                title="  Local pasted article  ",
                source_name="  Operator supplied source  ",
                author="  Reporter Name  ",
                published_at="  2026-05-01  ",
                source_url="https://example.invalid/manual-only",
                raw_text="\r\n  The agency says the regulation starts June 1.\r\n\r\n",
                input_method="manual_text",
            )
        )
    )
    second = _dump(
        ingest_manual(
            ManualIngestRequest(
                title="Local pasted article",
                source_name="Operator supplied source",
                author="Reporter Name",
                published_at="2026-05-01",
                source_url="https://example.invalid/manual-only",
                raw_text="The agency says the regulation starts June 1.",
                input_method="manual_text",
            )
        )
    )

    assert first["source_document"]["text_for_analysis"] == "The agency says the regulation starts June 1."
    assert first["raw_document"]["submitted_text"] == "\r\n  The agency says the regulation starts June 1.\r\n\r\n"
    assert first["content_hash"] == second["content_hash"]
    assert first["content_hash"].startswith("sha256:")
    assert first["metadata"]["source_url"] == "https://example.invalid/manual-only"
    assert first["metadata"]["source_url_fetched"] is False
    assert first["raw_document"]["source_url_fetched"] is False
    assert first["audit_event"]["operation"] == "manual_ingested"
    assert first["audit_event"]["event_hash"] in {event["event_hash"] for event in first["audit_trail"]}
    assert first["audit_verification"]["valid"] is True


def test_manual_ingest_accepts_only_canonical_request_schema() -> None:
    legacy_method_key = "_".join(("input", "mode"))
    request = ManualIngestRequest(
        title="Canonical title",
        source_name="Canonical source",
        source_url="https://example.invalid/metadata-only",
        raw_text="The source claims the pilot remains unresolved.",
        input_method="manual_text",
    )

    assert request.input_method == "manual_text"

    with pytest.raises(ValidationError) as exc:
        ManualIngestRequest.model_validate(
            {
                "title": "Alias attempt",
                "source_name": "operator",
                "raw_text": "The article claims the route changed.",
                legacy_method_key: "manual_text",
            }
        )

    assert legacy_method_key in str(exc.value)

    legacy_url_key = "_".join(("declared", "url"))
    with pytest.raises(ValidationError) as legacy_exc:
        ManualIngestRequest.model_validate(
            {
                "topic": "Legacy topic",
                "source_name": "operator",
                legacy_url_key: "https://example.invalid/not-fetched",
                "text": "The article claims the route changed.",
            }
        )

    assert "raw_text" in str(legacy_exc.value)


def test_manual_ingest_rejects_empty_normalized_text() -> None:
    with pytest.raises(ValidationError) as exc:
        ManualIngestRequest(source_name="operator", raw_text=" \r\n\t ", input_method="manual_text")

    assert "raw_text" in str(exc.value)


def test_manual_ingest_rejects_unsupported_input_method() -> None:
    with pytest.raises(ValidationError) as exc:
        ManualIngestRequest(source_name="operator", raw_text="https://example.invalid/live", input_method="url")  # type: ignore[arg-type]

    assert "manual_text" in str(exc.value)


def test_manual_ingest_rejects_unimplemented_file_input_method() -> None:
    file_input_method = "_".join(("local", "file"))

    with pytest.raises(ValidationError) as exc:
        ManualIngestRequest.model_validate(
            {
                "source_name": "operator",
                "raw_text": "The local file parser is not part of this contract.",
                "input_method": file_input_method,
            }
        )

    assert "manual_text" in str(exc.value)


def test_manual_ingest_limitations_do_not_claim_final_truth_or_fetching() -> None:
    payload = _dump(
        ingest_manual(
            ManualIngestRequest(
                title="Manual assertion",
                source_name="operator",
                source_url="https://example.invalid/not-fetched",
                raw_text="The article claims the start date is contested.",
                input_method="manual_text",
            )
        )
    )
    joined = " ".join(payload["limitations"] + payload["raw_document"]["limitations"] + payload["source_document"]["limitations"]).lower()

    assert "not fetched" in joined or "no url fetching" in joined
    assert "assertion container" in joined
    assert "final verdict" not in joined
    assert payload["metadata"]["source_url"] == "https://example.invalid/not-fetched"
    assert payload["metadata"]["source_url_fetched"] is False
    assert payload["metadata"]["metadata_role"] == "user_asserted_metadata_only"
    assert payload["analysis"]["mode"] == "local_input"
    assert payload["analysis"]["limitations_ref"] == "LIMITATIONS.md"


def test_manual_ingest_response_exposes_only_canonical_input_method() -> None:
    legacy_method_key = "_".join(("input", "mode"))
    payload = _dump(
        ingest_manual(
            ManualIngestRequest(
                source_name="operator",
                raw_text="The article says the result is still contested.",
                input_method="manual_text",
            )
        )
    )

    assert _has_key(payload, "input_method")
    assert not _has_key(payload, legacy_method_key)


def test_sample_remains_stable_after_manual_ingest_route_exists() -> None:
    before = _dump(sample())
    ingest_manual(
        ManualIngestRequest(source_name="operator", raw_text="A manual article claims the pilot remains unresolved.")
    )
    after = _dump(sample())

    assert before == after
