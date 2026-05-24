# Lumen Audit Trail Specification

Version: v0.2-local-deterministic

## Purpose

The audit trail makes Lumen outputs inspectable and tamper-evident. It records meaningful transformations so users can see how claims, evidence, scores, limitations, and briefings were produced.

The audit trail does not prove that a claim is correct. It proves that a declared sequence of transformations produced a declared output.

## MVP Ledger Model

MVP uses a local append-only JSONL-style ledger with a hash chain.

Required properties:

- genesis event exists;
- each later event references the previous event hash;
- event hash is computed from canonical event content;
- verification recomputes the chain;
- tampering changes verification status;
- ledger is local and deterministic.

No blockchain is implemented in v0.2.

## Required Event Fields

Each audit event should include:

- event_id;
- timestamp;
- operation;
- actor_type;
- actor_id;
- rule_version;
- input_hash;
- output_hash;
- previous_event_hash;
- event_hash;
- reason;
- limitations;
- code_version where available;
- model_version where applicable;
- prompt_hash where applicable.

For v0.2 deterministic local operation, model_version and prompt_hash may be null or "not_used" when no model/prompt was used.

## Genesis Event

The genesis event starts a ledger and must declare:

- ledger version;
- rule version;
- fixture/demo status;
- deterministic mode;
- limitations reference;
- previous_event_hash as null.

## Operations That Require Events

Create events for:

- sample loaded;
- input text received;
- claim extracted or placeholder claim generated;
- evidence attached;
- source dependency evaluated;
- contradiction checked;
- confidence scored;
- narrative analysis generated;
- briefing generated;
- audit verification requested;
- governance rule applied;
- human edit or challenge recorded.

## Canonical Hashing

Implementations should hash canonical JSON with stable key order and deterministic separators. Hashes should use SHA-256 for MVP.

The event_hash must exclude the event_hash field itself and include previous_event_hash.

## Verification Output

Audit verification must return:

- valid: boolean;
- checked_event_count;
- genesis_present;
- first_invalid_event_id, if any;
- reason;
- latest_event_hash, if available.

## User-Facing Requirements

Any analysis output must expose an audit reference.
Any briefing must include an audit reference.
Any score must link to the audit event that applied the score.

If audit verification fails, UI must not present the affected analysis as trustworthy. It should display a clear tamper/damage warning.

## Governance Change Events

Governance changes must create audit events or release notes documenting:

- rule changed;
- previous behavior;
- new behavior;
- rationale;
- expected risk;
- tests or evals affected;
- reviewer/challenge notes.

## Limitations

MVP audit trails are local and tamper-evident, not tamper-proof. A local attacker with filesystem access can modify files; verification detects inconsistent chains but cannot prevent deletion or replacement without external anchoring.
