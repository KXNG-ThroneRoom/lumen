"""Tamper-evident local audit ledger primitives."""

from __future__ import annotations

from datetime import datetime
from hashlib import sha256
from typing import Any

from .models import AuditEvent, AuditVerification, utc_now

GENESIS_PREVIOUS_HASH = "0" * 64
RULE_VERSION = "lumen.rules.v0.2"


def _dump(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if hasattr(value, "dict"):
        return value.dict()
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, list):
        return [_dump(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _dump(val) for key, val in value.items()}
    return value


def canonical_json(value: Any) -> str:
    """Serialize a value in a stable form for deterministic hashing."""

    import json

    return json.dumps(_dump(value), sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def hash_payload(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def calculate_event_hash(event_data: dict[str, Any]) -> str:
    """Hash an audit event excluding its own event_hash field."""

    payload = {key: value for key, value in event_data.items() if key not in {"event_hash", "timestamp"}}
    return hash_payload(payload)


def create_audit_event(
    *,
    event_id: str,
    operation: str,
    reason: str,
    input_payload: Any,
    output_payload: Any,
    previous_event_hash: str,
    metadata: dict[str, Any] | None = None,
    actor_type: str = "system",
    actor_id: str = "lumen.local.deterministic",
) -> AuditEvent:
    event_data = {
        "event_id": event_id,
        "timestamp": utc_now(),
        "actor_type": actor_type,
        "actor_id": actor_id,
        "operation": operation,
        "reason": reason,
        "input_hash": hash_payload(input_payload),
        "output_hash": hash_payload(output_payload),
        "previous_event_hash": previous_event_hash,
        "event_hash": "",
        "rule_version": RULE_VERSION,
        "model_version": "none",
        "prompt_hash": "none",
        "code_version": "local",
        "metadata": metadata or {},
    }
    event_data["event_hash"] = calculate_event_hash(event_data)
    return AuditEvent(**event_data)


def create_genesis_event(metadata: dict[str, Any] | None = None, **legacy_kwargs: Any) -> AuditEvent:
    if legacy_kwargs:
        metadata = {**(metadata or {}), **legacy_kwargs}
    actor = metadata.pop("actor", None) if metadata and "actor" in metadata else None
    return create_audit_event(
        event_id="audit-000-genesis",
        operation="genesis",
        reason="Initialize local deterministic Lumen audit ledger.",
        input_payload={"genesis": True},
        output_payload={"ledger": "initialized"},
        previous_event_hash=GENESIS_PREVIOUS_HASH,
        metadata=metadata or {"rule_version": RULE_VERSION},
        actor_id=actor or "lumen.local.deterministic",
    )


def append_audit_event(
    ledger: list[AuditEvent],
    *,
    operation: str,
    reason: str | None = None,
    input_payload: Any | None = None,
    output_payload: Any | None = None,
    metadata: dict[str, Any] | None = None,
    actor: str | None = None,
    payload: Any | None = None,
) -> AuditEvent:
    if payload is not None:
        input_payload = input_payload if input_payload is not None else payload
        output_payload = output_payload if output_payload is not None else payload
    if not ledger:
        ledger.append(create_genesis_event())
    event = create_audit_event(
        event_id=f"audit-{len(ledger):03d}-{operation}",
        operation=operation,
        reason=reason or f"{operation} recorded in deterministic audit ledger.",
        input_payload={} if input_payload is None else input_payload,
        output_payload={} if output_payload is None else output_payload,
        previous_event_hash=ledger[-1].event_hash,
        metadata=metadata,
        actor_id=actor or "lumen.local.deterministic",
    )
    ledger.append(event)
    return event


def build_audit_ledger(steps: list[tuple[str, str, Any, Any]]) -> list[AuditEvent]:
    ledger = [create_genesis_event()]
    for operation, reason, input_payload, output_payload in steps:
        append_audit_event(
            ledger,
            operation=operation,
            reason=reason,
            input_payload=input_payload,
            output_payload=output_payload,
        )
    return ledger


def verify_audit_chain(events: list[AuditEvent]) -> AuditVerification:
    errors: list[str] = []
    if not events:
        return AuditVerification(valid=False, event_count=0, errors=["audit ledger is empty"])

    first = events[0]
    if first.operation != "genesis":
        errors.append("first event is not genesis")
    if first.previous_event_hash != GENESIS_PREVIOUS_HASH:
        errors.append("genesis previous hash is invalid")

    previous_hash: str | None = None
    for index, event in enumerate(events):
        event_data = event.model_dump(mode="json")
        recalculated = calculate_event_hash(event_data)
        if recalculated != event.event_hash:
            errors.append(f"event {index} hash mismatch")
        if index > 0 and event.previous_event_hash != previous_hash:
            errors.append(f"event {index} previous hash mismatch")
        previous_hash = event.event_hash

    return AuditVerification(
        valid=not errors,
        event_count=len(events),
        errors=errors,
        genesis_event_hash=events[0].event_hash,
        latest_event_hash=events[-1].event_hash,
    )


# Compatibility aliases for likely tests.
append_event = append_audit_event
verify_ledger = verify_audit_chain
