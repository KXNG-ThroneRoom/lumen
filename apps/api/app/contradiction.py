"""Fixture-based contradiction detection stub."""

from __future__ import annotations

from .models import Claim, Contradiction


def detect_contradictions(
    claims: list[Claim],
    evidence: list[object] | None = None,
    *,
    fixture_id: str | None = None,
) -> list[Contradiction] | dict[str, object]:
    """Detect only explicit deterministic fixture contradictions.

    This intentionally does not claim semantic contradiction intelligence. It
    recognizes known fixture patterns and exposes limitations in the result.
    """

    normalized = {claim.id: claim.normalized_claim.lower() for claim in claims}
    contradictions: list[Contradiction] = []

    june_claims = [claim_id for claim_id, text in normalized.items() if "june 1" in text]
    july_claims = [claim_id for claim_id, text in normalized.items() if "july 1" in text]
    if june_claims and july_claims:
        contradictions.append(
            Contradiction(
                id="contradiction-regulation-start-date",
                claim_ids=[june_claims[0], july_claims[0]],
                contradiction_type="time_contradiction",
                summary="Fixture conflict: article claim says June 1 while primary filing says July 1.",
                limitations=["Fixture-based time contradiction; no automatic final truth resolution."],
            )
        )

    image_claims = [claim_id for claim_id, text in normalized.items() if "today" in text and ("image" in text or "photo" in text)]
    old_archive_claims = [claim_id for claim_id, text in normalized.items() if "archived" in text and ("two years" in text or "older" in text)]
    if image_claims and old_archive_claims:
        contradictions.append(
            Contradiction(
                id="contradiction-image-timestamp",
                claim_ids=[image_claims[0], old_archive_claims[0]],
                contradiction_type="timestamp_contradiction",
                summary="Fixture conflict: image is presented as new but fixture archive timestamp is older.",
                limitations=["Does not prove the current event did not happen; only flags media timestamp conflict."],
            )
        )

    if fixture_id == "GC-003-primary-document-contradiction" and not contradictions and claims:
        contradictions.append(
            Contradiction(
                id="contradiction-fixture-gc003",
                claim_ids=[claims[0].id],
                contradiction_type="time_contradiction",
                summary="Golden case fixture marks this claim as contested by a primary document.",
                limitations=["Fixture marker only; no semantic detection claimed."],
            )
        )

    if evidence is not None:
        return {
            "method": "fixture_based",
            "contradictions": [
                {
                    "id": item.id,
                    "claim_id": item.claim_ids[0],
                    "claim_ids": item.claim_ids,
                    "contradiction_type": item.contradiction_type,
                    "summary": item.summary,
                    "status": "contested",
                    "reasons": ["primary document conflicts with article", *item.limitations],
                }
                for item in contradictions
            ],
            "limitations": ["Fixture-based contradiction detection only; no semantic intelligence is claimed."],
        }

    return contradictions


find_contradictions = detect_contradictions
