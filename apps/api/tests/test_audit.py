from __future__ import annotations

import copy

from app.audit import append_audit_event, create_genesis_event, verify_audit_chain


def _asdict(obj):
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json")
    return obj


def test_genesis_event_has_genesis_previous_hash_and_stable_hash():
    event = create_genesis_event(metadata={"ruleset_version": "lumen-v0.2"})
    data = _asdict(event)

    assert data["operation"] == "genesis"
    assert data["previous_event_hash"] == "0" * 64
    assert data["event_hash"]
    assert len(data["event_hash"]) == 64
    assert data["metadata"]["ruleset_version"] == "lumen-v0.2"


def test_audit_chain_integrity_verifies_for_appended_events():
    ledger = [create_genesis_event(metadata={"ruleset_version": "lumen-v0.2"})]
    append_audit_event(
        ledger,
        operation="score_assigned",
        reason="Assigned visible confidence status and reasons.",
        input_payload={"claim_id": "claim-1"},
        output_payload={"claim_id": "claim-1", "status": "unresolved"},
    )
    append_audit_event(
        ledger,
        operation="briefing_generated",
        reason="Generated deterministic briefing with limitations.",
        input_payload={"claim_id": "claim-1"},
        output_payload={"briefing_id": "briefing-1"},
    )

    result = _asdict(verify_audit_chain(ledger))

    assert result["valid"] is True
    assert result["event_count"] == 3
    assert result["errors"] == []
    assert result["genesis_event_hash"] == ledger[0].event_hash
    assert result["latest_event_hash"] == ledger[-1].event_hash


def test_audit_verification_detects_tampering():
    ledger = [create_genesis_event()]
    append_audit_event(
        ledger,
        operation="claim_extracted",
        reason="Extracted placeholder claim.",
        input_payload={"text": "original"},
        output_payload={"claim_id": "claim-1", "text": "original"},
    )
    tampered = copy.deepcopy(ledger)
    tampered[1].output_hash = "f" * 64

    result = _asdict(verify_audit_chain(tampered))

    assert result["valid"] is False
    assert any("hash" in error.lower() for error in result["errors"])
