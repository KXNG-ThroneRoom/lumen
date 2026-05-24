from __future__ import annotations

from app.claim_extraction import extract_claims


def _dump(obj):
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json")
    return obj


def test_placeholder_extractor_is_honest_about_limitations():
    text = "Headline: Study proves policy caused the change. Body: Researchers observed correlation and warned about confounders."

    result = _dump(extract_claims(text, source_document_id="GC-004-headline-stronger-than-body"))

    assert result["claims"]
    assert result["method"] in {"placeholder", "deterministic_placeholder", "fixture_placeholder"}
    limitations = " ".join(result["limitations"] + [result.get("capability_claim", "")]).lower()
    assert "placeholder" in limitations
    assert "not production" in limitations or "not comprehensive" in limitations or "not production-grade" in limitations
    assert "deterministic" in limitations or result["method"].startswith("deterministic")
    for claim in result["claims"]:
        assert claim["status"]
        assert claim["confidence_reason"]
        assert claim["confidence_score"] <= 0.25
