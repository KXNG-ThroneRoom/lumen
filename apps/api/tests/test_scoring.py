from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.models import Claim, ClaimStatus, ClaimType, Evidence, EvidenceType, Source, SourceGraph
from app.scoring import score_claim


def _dump(obj):
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json")
    return obj


def _claim(**overrides):
    data = {
        "id": "claim-1",
        "raw_claim_text": "A claim under test.",
        "normalized_claim": "a claim under test",
        "claim_type": ClaimType.FACTUAL,
        "confidence_score": 0.0,
        "confidence_reason": ["pending scoring"],
        "status": ClaimStatus.UNKNOWN,
    }
    data.update(overrides)
    return Claim(**data)


def test_claim_requires_status_and_confidence_reason():
    with pytest.raises(ValidationError):
        Claim(
            id="claim-missing-status",
            raw_claim_text="A claim without status must be invalid",
            normalized_claim="a claim without status must be invalid",
            claim_type=ClaimType.FACTUAL,
            confidence_score=0.1,
            confidence_reason=["reason exists"],
        )

    with pytest.raises(ValidationError):
        Claim(
            id="claim-missing-reason",
            raw_claim_text="A claim without confidence reasons must be invalid",
            normalized_claim="a claim without confidence reasons must be invalid",
            claim_type=ClaimType.FACTUAL,
            confidence_score=0.1,
            confidence_reason=[],
            status=ClaimStatus.UNKNOWN,
        )


def test_anonymous_source_cap_is_enforced_and_explained():
    claim = _claim(
        id="claim-anon",
        raw_claim_text="An unnamed official identified the actor responsible.",
        normalized_claim="unnamed official identified actor responsible",
        claim_type=ClaimType.ANONYMOUS_SOURCE,
    )
    evidence = [
        Evidence(
            id="ev-anon",
            evidence_type=EvidenceType.ANONYMOUS_SOURCE,
            summary="Unnamed official claim with no primary document.",
            anonymous=True,
        )
    ]

    scored = _dump(score_claim(claim, evidence=evidence))

    assert scored["status"] in {"unknown", "unresolved", "plausible"}
    assert scored["score"] <= 0.45
    joined = " ".join(scored["reasons"] + scored["caps_applied"]).lower()
    assert "anonymous" in joined
    assert "cap" in joined
    assert "primary" in joined


def test_primary_evidence_boost_is_visible_but_not_absolute_truth():
    claim = _claim(
        id="claim-date",
        raw_claim_text="The regulation starts on July 1.",
        normalized_claim="regulation starts on july 1",
    )
    evidence = [
        Evidence(
            id="ev-primary",
            evidence_type=EvidenceType.PRIMARY_DOCUMENT,
            summary="Official filing states the effective date is July 1.",
            primary=True,
        )
    ]

    scored = _dump(score_claim(claim, evidence=evidence))

    assert scored["score"] > 0.4
    assert scored["score"] < 1.0
    reasons = " ".join(scored["reasons"]).lower()
    assert "primary" in reasons
    assert "does not" in reasons or "not" in reasons


def test_unknown_unresolved_status_is_valid_for_insufficient_evidence():
    claim = _claim(
        id="claim-vague",
        raw_claim_text="A major incident occurred downtown.",
        normalized_claim="major incident occurred downtown",
    )

    scored = _dump(score_claim(claim, evidence=[]))

    assert scored["status"] in {"unknown", "unresolved"}
    assert scored["score"] <= 0.25
    reasons = " ".join(scored["reasons"]).lower()
    assert "insufficient evidence" in reasons or "missing" in reasons
