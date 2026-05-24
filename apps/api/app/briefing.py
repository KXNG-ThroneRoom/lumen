"""Deterministic briefing generator."""

from __future__ import annotations

from .models import Briefing, Claim, ClaimStatus, ConfidenceBreakdown, Contradiction, Evidence

BRIEFING_LIMITATIONS = [
    "This briefing is deterministic and fixture/local-input based.",
    "It exposes claims, evidence, contradictions, and uncertainty; it does not declare final truth.",
    "Placeholder extraction and fixture contradiction detection are not production intelligence capabilities.",
]


def aggregate_confidence(claims: list[Claim], contradictions: list[Contradiction]) -> ConfidenceBreakdown:
    if not claims:
        return ConfidenceBreakdown(
            score=0.0,
            status=ClaimStatus.UNKNOWN,
            reasons=["no claims available for briefing"],
            rule_references=["briefing.aggregate.v0.2"],
        )

    avg = round(sum(claim.confidence_score for claim in claims) / len(claims), 2)
    reasons = ["briefing confidence is an aggregate method signal, not a truth verdict"]
    reasons.extend({reason for claim in claims for reason in claim.confidence_reason[:2]})
    if contradictions:
        status = ClaimStatus.CONTESTED
        reasons.append("contradictions remain visible in the briefing")
        avg = min(avg, 0.55)
    elif any(claim.status in {ClaimStatus.UNKNOWN, ClaimStatus.UNRESOLVED} for claim in claims):
        status = ClaimStatus.UNRESOLVED
    else:
        status = ClaimStatus.PLAUSIBLE

    return ConfidenceBreakdown(
        score=avg,
        status=status,
        reasons=sorted(set(reasons)),
        rule_references=["briefing.aggregate.v0.2"],
        warnings=["Do not interpret aggregate confidence as article-level truth."],
    )


def generate_briefing(
    claims: list[Claim] | None = None,
    *,
    topic: str = "Local deterministic analysis",
    evidence: list[Evidence] | None = None,
    contradictions: list[Contradiction] | None = None,
    audit_reference: str | None = None,
    audit_events: list[object] | None = None,
) -> Briefing | dict[str, object]:
    claims = claims or []
    evidence = evidence or []
    contradictions = contradictions or []

    if audit_events is not None:
        refs = [getattr(event, "event_hash", None) for event in audit_events]
        refs = [ref for ref in refs if ref]
        summary = (
            f"{len(claims)} claim(s) remain "
            f"{claims[0].status.value if claims else 'unknown'}; this briefing is not a truth verdict."
        )
        return {
            "id": "briefing-local-deterministic",
            "summary": summary,
            "limitations": BRIEFING_LIMITATIONS,
            "audit_event_refs": refs,
            "claims": [claim.model_dump(mode="json") for claim in claims],
            "method": "deterministic_briefing",
        }

    contradiction_phrase = "contradictions are present" if contradictions else "no fixture contradictions detected"
    bottom_line = (
        f"{topic}: {len(claims)} claim(s) represented; {contradiction_phrase}. "
        "Use the evidence and audit trail to inspect the method, not as a final truth verdict."
    )
    missing = [
        "independent source confirmation" if len(evidence) < 2 else "human review of source independence",
        "primary evidence for any claim lacking a primary evidence reference",
        "durable audit storage beyond local MVP memory",
    ]
    unresolved = [
        "Which evidence streams are truly independent?",
        "What primary material would change confidence?",
        "Are any interested-party incentives missing from the source metadata?",
    ]
    narrative_frames = ["Narrative analysis deferred; any future frame labels must be marked as analysis, not fact."]
    watch = ["new primary documents", "named on-record sources", "corrections or retractions", "source dependency changes"]

    return Briefing(
        id="briefing-local-deterministic",
        topic=topic,
        bottom_line=bottom_line,
        confidence=aggregate_confidence(claims, contradictions),
        key_claims=claims,
        evidence=evidence,
        contradictions=contradictions,
        missing_information=missing,
        narrative_frames=narrative_frames,
        watch_indicators=watch,
        unresolved_questions=unresolved,
        limitations=BRIEFING_LIMITATIONS,
        audit_reference=audit_reference or "audit-reference-unavailable",
    )
