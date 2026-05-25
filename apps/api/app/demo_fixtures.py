"""Controlled fixture payloads for the local demo API flow.

These fixtures are deterministic and illustrative. They are not live analysis,
real-time ingestion, or production verification output.
"""

from __future__ import annotations

from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict

from .claim_extraction import sample_claims, sample_evidence, sample_sources
from .models import Claim, Evidence, Source


class DemoFixture(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str = "lumen.analysis.v0.3"
    mode: str = "fixture_demo"
    topic: str
    claims: list[Claim]
    evidence: list[Evidence]
    sources: list[Source]
    limitations: list[str]
    fixture_timestamp: datetime
    limitations_ref: str = "LIMITATIONS.md"


FIXTURE_TIMESTAMP = datetime(2026, 1, 1, 0, 0, 0, tzinfo=timezone.utc)


def _with_fixture_timestamp(claims: list[Claim]) -> list[Claim]:
    return [claim.model_copy(update={"created_at": FIXTURE_TIMESTAMP}) for claim in claims]


def build_demo_fixture() -> DemoFixture:
    """Return the controlled v0.3 demo fixture used by /sample."""

    return DemoFixture(
        topic="Fixture: regulation start-date contradiction",
        claims=_with_fixture_timestamp(sample_claims()),
        evidence=sample_evidence(),
        sources=sample_sources(),
        fixture_timestamp=FIXTURE_TIMESTAMP,
        limitations=[
            "Fixture data is illustrative and local; it is not live geopolitical or production analysis.",
            "Contradiction detection is fixture-backed and exposes conflict without resolving final truth.",
            "Confidence is a visible method signal, not an instruction to believe.",
        ],
    )
