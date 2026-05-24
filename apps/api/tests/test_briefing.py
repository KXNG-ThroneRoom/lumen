from __future__ import annotations

from app.audit import append_audit_event, create_genesis_event
from app.briefing import generate_briefing
from app.models import Claim, ClaimStatus, ClaimType


def _dump(obj):
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json")
    return obj


def test_briefing_includes_limitations_and_audit_reference():
    claim = Claim(
        id="claim-1",
        raw_claim_text="A major incident occurred downtown.",
        normalized_claim="major incident occurred downtown",
        claim_type=ClaimType.FACTUAL,
        status=ClaimStatus.UNKNOWN,
        confidence_score=0.2,
        confidence_reason=["insufficient evidence", "missing timestamp", "single vague source"],
    )
    ledger = [create_genesis_event()]
    scored = append_audit_event(
        ledger,
        operation="score_assigned",
        reason="Assigned visible confidence status and reasons.",
        input_payload={"claim_id": "claim-1"},
        output_payload={"claim_id": "claim-1", "status": "unknown"},
    )

    briefing = _dump(
        generate_briefing(
            topic="Fixture uncertainty briefing",
            claims=[claim],
            evidence=[],
            contradictions=[],
            audit_reference=scored.event_hash,
        )
    )

    assert briefing["limitations"]
    assert briefing["audit_reference"] == scored.event_hash
    text = briefing["bottom_line"] + " " + " ".join(briefing["limitations"])
    lowered = text.lower()
    assert "not" in lowered and ("truth" in lowered or "final" in lowered)
    assert briefing["unresolved_questions"]
