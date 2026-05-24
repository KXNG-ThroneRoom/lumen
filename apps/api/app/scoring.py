"""Deterministic confidence scoring rules for Lumen MVP.

Scores are method signals, not final truth claims. Each output includes visible
reasons and rule references.
"""

from __future__ import annotations

from .models import Claim, ClaimStatus, ClaimType, ConfidenceBreakdown, Evidence, EvidenceType, SourceGraph

ANONYMOUS_SOURCE_CAP = 0.45
INTERESTED_PARTY_CAP = 0.50
INSUFFICIENT_EVIDENCE_CAP = 0.25
STATISTICAL_WITHOUT_CONTEXT_CAP = 0.40

PRIMARY_TYPES = {
    EvidenceType.PRIMARY_DOCUMENT,
    EvidenceType.OFFICIAL_DATASET,
    EvidenceType.COURT_FILING,
    EvidenceType.FULL_TRANSCRIPT,
    EvidenceType.RAW_VIDEO,
    EvidenceType.RAW_IMAGE,
    EvidenceType.GEOLOCATION,
}


def _status_from_score(score: float, *, contested: bool = False, contradicted: bool = False) -> ClaimStatus:
    if contradicted:
        return ClaimStatus.CONTRADICTED
    if contested:
        return ClaimStatus.CONTESTED
    if score >= 0.80:
        return ClaimStatus.STRONGLY_CORROBORATED
    if score >= 0.65:
        return ClaimStatus.PROBABLE
    if score >= 0.45:
        return ClaimStatus.PLAUSIBLE
    if score >= 0.26:
        return ClaimStatus.UNRESOLVED
    return ClaimStatus.UNKNOWN


def score_claim(
    claim: Claim,
    evidence: list[Evidence] | None = None,
    source_graph: SourceGraph | None = None,
    contradiction_count: int = 0,
) -> ConfidenceBreakdown:
    """Apply transparent deterministic confidence rules to a claim."""

    evidence = evidence or []
    score = 0.20
    reasons: list[str] = []
    caps: list[str] = []
    warnings: list[str] = []
    rule_refs = ["constitution.article_xii", "governance.confidence.v0.2"]

    if not evidence:
        reasons.extend(["insufficient evidence", "single vague source"])
        caps.append("insufficient evidence cap 0.25")
        score = min(score, INSUFFICIENT_EVIDENCE_CAP)
        return ConfidenceBreakdown(
            score=score,
            status=ClaimStatus.UNKNOWN,
            reasons=reasons,
            rule_references=rule_refs,
            caps_applied=caps,
            warnings=warnings,
        )

    primary_count = sum(1 for item in evidence if item.primary or item.evidence_type in PRIMARY_TYPES)
    anonymous_count = sum(1 for item in evidence if item.anonymous or item.evidence_type == EvidenceType.ANONYMOUS_SOURCE)
    named_count = sum(1 for item in evidence if item.evidence_type in {EvidenceType.NAMED_SOURCE, EvidenceType.LOCAL_REPORTING})

    score += min(primary_count * 0.25, 0.35)
    score += min(named_count * 0.15, 0.25)
    if primary_count:
        reasons.append("primary evidence attached; raises confidence but does not resolve all uncertainty")
    if named_count:
        reasons.append("named/on-record or local direct reporting attached")

    independent_streams = source_graph.independent_evidence_streams if source_graph else 1
    if independent_streams > 1:
        score += min((independent_streams - 1) * 0.12, 0.24)
        reasons.append(f"{independent_streams} independent evidence streams")
    else:
        reasons.append("single evidence stream")

    if source_graph and source_graph.warnings:
        warnings.extend(source_graph.warnings)
        for warning in source_graph.warnings:
            if "wire dependency" in warning or "citation dependency" in warning:
                reasons.append("source dependency warning: article volume is not proof")
                score -= 0.10
                break

    if anonymous_count:
        reasons.append("anonymous source; confidence capped unless stronger evidence is attached")
        if not primary_count:
            score = min(score, ANONYMOUS_SOURCE_CAP)
            caps.append("anonymous source cap 0.45")

    if claim.claim_type == ClaimType.ANONYMOUS_SOURCE and not primary_count:
        reasons.append("no primary evidence")
        score = min(score, ANONYMOUS_SOURCE_CAP)
        caps.append("anonymous-source claim cap 0.45")

    if claim.claim_type == ClaimType.INTERESTED_PARTY and not primary_count:
        reasons.extend(["interested party", "authority is not proof"])
        score = min(score, INTERESTED_PARTY_CAP)
        caps.append("interested party cap 0.50")

    if claim.claim_type == ClaimType.STATISTICAL:
        text = claim.raw_claim_text.lower()
        if "doubled" in text and not any("denominator" in item.summary.lower() for item in evidence):
            reasons.extend(["missing denominator", "missing baseline", "missing time window", "missing data source"])
            score = min(score, STATISTICAL_WITHOUT_CONTEXT_CAP)
            caps.append("missing statistical context cap 0.40")

    if contradiction_count:
        reasons.append("contradictory fixture evidence attached")
        score = min(score, 0.55) - min(contradiction_count * 0.10, 0.20)

    score = max(0.0, min(round(score, 2), 1.0))
    status = _status_from_score(score, contested=contradiction_count > 0)

    if claim.claim_type == ClaimType.MORAL_FRAMING:
        status = ClaimStatus.NARRATIVE_ONLY
        reasons.append("narrative analysis label required; not a factual verdict")

    return ConfidenceBreakdown(
        score=score,
        status=status,
        reasons=reasons or ["deterministic scoring completed with visible method rules"],
        rule_references=rule_refs,
        caps_applied=sorted(set(caps)),
        warnings=sorted(set(warnings)),
    )


def apply_scoring(claim: Claim, evidence: list[Evidence], source_graph: SourceGraph | None = None, contradiction_count: int = 0) -> Claim:
    """Return a new claim with score/status/reasons updated."""

    breakdown = score_claim(claim, evidence, source_graph, contradiction_count)
    return claim.model_copy(
        update={
            "confidence_score": breakdown.score,
            "status": breakdown.status,
            "confidence_reason": breakdown.reasons,
        }
    )


calculate_confidence = score_claim
