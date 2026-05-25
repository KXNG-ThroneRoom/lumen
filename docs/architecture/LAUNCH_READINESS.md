# Lumen v0.4 Launch Readiness

Version: v0.4-demo-polish

## Readiness stance

This checklist is for a controlled local demo. It is not a production-readiness certification.

Lumen is launch-ready for v0.4 only if the demo makes methods visible without overstating capability. Passing this checklist means the local fixture demo is inspectable, deterministic, and honest about limits. It does not mean Lumen verifies live reality, provides global coverage, or replaces human judgment.

## Required local verification

Run from repo root unless noted.

```text
bash scripts/verify_lumen.sh
```

The aggregate verifier prefers `.venv/bin/python` when present, then falls back
to `python3`. This avoids treating a host interpreter without pytest as a
product failure.

Expected result for demo-ready status:

- the aggregate command completes successfully;
- failures are recorded as blockers, not ignored;
- any skipped test must be justified as intentionally outside v0.4 scope.

## API readiness gates

`GET /health` must show:

- service status;
- deterministic/local method boundary;
- limitations or limitations reference;
- no production-readiness claim;
- no final-authority claim.

`GET /sample` must return the canonical controlled fixture response with:

- `schema_version`;
- `mode: "fixture_demo"`;
- claims;
- evidence;
- sources;
- source graph;
- contradictions;
- briefing;
- audit events or audit trail;
- audit verification;
- limitations and `limitations_ref`.

`POST /analyze` must:

- accept manually supplied local text only;
- not fetch URLs;
- not call paid APIs;
- not call LLMs in the default path;
- disclose placeholder extraction limits;
- return the same analysis envelope shape as `/sample`.

`GET /audit/verify` must:

- return valid/invalid state;
- include event count;
- include genesis/latest event hashes when available;
- explain audit-chain consistency only, not claim truth.

## Frontend readiness gates

The dashboard is demo-ready only if these panels are present and honest:

| Panel | Required for pass |
| --- | --- |
| BriefingPanel | bottom line preserves uncertainty; confidence reasons, limitations, limitations ref, audit ref are visible |
| ClaimMatrix | every rendered claim has status, confidence reason, evidence ref, limitations ref, audit ref |
| EvidenceTrail | evidence shows provenance/proximity/limitations/audit ref and does not imply completeness |
| AuditTrail | verification state and method trace are visible; copy does not say audit proves the claim |
| NarrativeMap | labeled analysis-not-fact and fixture-backed/deferred; no intent/deception inference |
| SourceSpread | wire/citation/dependency notes visible; repeated count is not treated as corroboration |
| ContradictionBoard | fixture conflict is shown as unresolved/exposed, not settled |

## Content and copy readiness gates

Pass requires all user-facing demo copy to preserve these messages:

- Lumen exposes claims, evidence, contradictions, uncertainty, provenance, confidence reasons, and audit trails.
- Lumen helps humans reason; it does not replace judgment.
- Controlled fixtures are used unless explicitly labeled otherwise.
- Confidence is a visible method signal, not a truth verdict.
- Contradictions expose unresolved disputes; they do not settle them.
- Narrative analysis is analysis, not fact.
- Source quantity is not source independence.
- Audit trails record transformation history and can detect inconsistent history; they do not prove the underlying claim.

Block readiness if copy implies:

- final truth determination;
- article-level truth labels;
- live geopolitical analysis;
- complete source coverage;
- production intelligence reliability;
- propaganda/deception certainty;
- hidden model/scoring authority.

## Fixture readiness gates

The canonical v0.4 fixture must demonstrate:

- at least one contested or unresolved claim;
- at least one primary or near-primary evidence object;
- at least one dependent/repeated source stream;
- at least one fixture contradiction;
- visible missing information or unresolved questions;
- visible limitations at top-level and briefing level;
- audit references on displayed claims, evidence, and briefing.

The fixture must not include live current-event claims unless they are clearly synthetic or historically neutral controlled examples with no claim of live coverage.

## Security and operations gates

Pass requires:

- no secrets required for the default demo path;
- no telemetry or analytics in the default demo path;
- no hidden external network dependency for fixture demo;
- no automatic commit/push/deploy expectation;
- no mutation, deletion, or replacement of raw evidence as part of demo flow;
- local-only run instructions remain accurate.

## Documentation readiness gates

Before v0.4 launch-readiness is claimed, these docs must agree:

- `docs/architecture/V0_4_SCOPE.md` defines the scope and deferrals;
- `docs/architecture/API_CONTRACT.md` matches backend/static response shape;
- `docs/architecture/DEMO_FLOW.md` matches the runnable operator path;
- `docs/architecture/MVP_PHASES.md` places v0.4 after v0.3 contract/demo integration as demo polish, not a new intelligence layer;
- `LIMITATIONS.md` remains linked or visible near outputs;
- governance docs preserve no-authority, confidence-reason, and auditability rules.

## Blocker taxonomy

Use these labels in handoff or verification reports:

- `api-contract-blocker`: route or schema drift prevents contract trust.
- `frontend-honesty-blocker`: UI hides or overstates uncertainty, limitations, status, reasons, or audit references.
- `fixture-blocker`: canonical fixture lacks claims/evidence/source dependency/contradiction/limitations needed for demo.
- `audit-blocker`: audit trail or verification is absent, invalid, or overclaimed.
- `scope-blocker`: implementation introduces live ingestion, paid APIs, LLM calls, telemetry, accounts, or production claims.
- `docs-blocker`: docs disagree with the runnable implementation.

## Final readiness decision

Allowed final states:

- `ready-controlled-demo`: all required gates pass; remaining deferrals are intentional and visible.
- `ready-with-documented-limitations`: core demo works, but non-blocking gaps are explicitly documented near outputs.
- `not-ready`: any blocker taxonomy item remains unresolved.

Do not use broader labels that imply production fitness, truth determination, or automated intelligence readiness for v0.4.
