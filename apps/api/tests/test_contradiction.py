from __future__ import annotations

from app.contradiction import detect_contradictions
from app.models import Claim, ClaimStatus, ClaimType


def _claim(id: str, text: str):
    return Claim(
        id=id,
        raw_claim_text=text,
        normalized_claim=text.rstrip("."),
        claim_type=ClaimType.FACTUAL,
        status=ClaimStatus.UNRESOLVED,
        confidence_score=0.0,
        confidence_reason=["pending contradiction check"],
    )


def _dump(obj):
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json")
    return obj


def test_fixture_contradiction_detects_primary_document_date_conflict():
    claims = [
        _claim("claim-june", "The regulation starts on June 1."),
        _claim("claim-july", "The official filing states the regulation starts on July 1."),
    ]

    result = [_dump(item) for item in detect_contradictions(claims, fixture_id="GC-003-primary-document-contradiction")]

    assert result
    first = result[0]
    assert first["contradiction_type"] == "time_contradiction"
    assert set(first["claim_ids"]) == {"claim-june", "claim-july"}
    assert "june" in first["summary"].lower()
    assert "july" in first["summary"].lower()
    assert "final truth" in " ".join(first["limitations"]).lower() or "semantic" in " ".join(first["limitations"]).lower()
