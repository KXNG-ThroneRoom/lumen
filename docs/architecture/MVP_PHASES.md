# Lumen MVP Phase Plan

## Status

Lumen is in the v0.4 demo-polish and launch-readiness swarm. v0.2 established the deterministic local baseline and v0.3 stabilized backend/frontend contract and demo flow around that baseline. v0.4 must not expand the analytical claim surface; it tightens demo scope, panel labeling, launch gates, and deferrals.

Current known state:

- Static UI scaffold exists.
- JSON fixtures parse.
- Repo contains untracked scaffold/docs/frontend/backend artifacts pending baseline review.
- Backend deterministic core is the main implementation blocker.
- Governance docs require hardening into enforceable product/code rules.
- MVP scope is locked to local deterministic primitives and fixture-backed analysis.
- v0.4 architecture scope is documented in `docs/architecture/V0_4_SCOPE.md`.
- v0.4 launch gates are documented in `docs/architecture/LAUNCH_READINESS.md`.
- NarrativeMap, SourceSpread, and ContradictionBoard must be fixture-backed, clearly stubbed, or explicitly deferred.

## Phase v0.4 — Demo Polish + Launch Readiness

Goal: make the controlled local fixture demo precise, reviewable, and honest without adding live-data or production intelligence scope.

Owned architecture files:

- `docs/architecture/MVP_PHASES.md`
- `docs/architecture/DEMO_FLOW.md`
- `docs/architecture/API_CONTRACT.md`
- `docs/architecture/LAUNCH_READINESS.md`
- `docs/architecture/V0_4_SCOPE.md`

Tasks:

- Define v0.4 scope and deferrals separately from v0.2/v0.3 baseline work.
- Keep `/sample` and `/analyze` contract clarity aligned with implementation.
- Make the operator demo path precise enough for backend, frontend, eval, and governance lanes to verify independently.
- Mark NarrativeMap, SourceSpread, and ContradictionBoard as fixture-backed, stubbed, or deferred instead of allowing ambiguous polish.
- Define launch-readiness states and blocker taxonomy.
- Prevent scope creep into live ingestion, paid APIs, LLM calls, telemetry, auth/accounts, databases, blockchain, hidden scoring, or final truth determination.

Gate:

- `V0_4_SCOPE.md` clearly separates demo-ready from deferred work.
- `LAUNCH_READINESS.md` defines pass/blocker criteria and verification commands.
- `DEMO_FLOW.md` gives an exact controlled-fixture operator path.
- `API_CONTRACT.md` documents v0.4 panel status without forcing an unnecessary schema break.
- No v0.4 architecture doc claims live coverage, production reliability, or final authority.

## Phase 0 — Scope Lock + Architecture Hardening

Goal: freeze the MVP boundary before implementation expands.

Owned architecture files:

- `docs/architecture/MVP_SCOPE.md`
- `docs/architecture/MVP_PHASES.md`
- `docs/architecture/SYSTEM_OVERVIEW.md`
- `docs/architecture/DATA_MODEL.md`

Tasks:

- Define the v0.2 scope boundary.
- Separate implemented primitives, deferred modules, and explicit non-goals.
- Harden module boundaries around deterministic local backend primitives.
- Align data model with backend/eval/frontend lanes.
- Make source independence, confidence reasons, limitations, and audit references first-class architecture requirements.
- Avoid new product claims beyond deterministic local fixture-backed analysis.

Gate:

- `MVP_SCOPE.md` clearly separates v0.2 commitments from deferred intelligence modules.
- Architecture docs identify exact model and API contracts needed by backend, eval, and frontend lanes.
- No architecture doc claims production-grade real-world verification.

## Phase 1 — Governance Hardening

Goal: make the constitution enforceable in product and code.

Owned governance files:

- `CONSTITUTION.md`
- `docs/governance/GOVERNANCE_RULES.md`
- `docs/governance/CONFIDENCE_SCORING.md`
- `docs/governance/AUDIT_TRAIL_SPEC.md`
- `docs/governance/BIAS_RESISTANCE.md`
- `LIMITATIONS.md`
- `ADVERSARIAL_REVIEW.md`
- `SECURITY.md`

Tasks:

- Harden anti-authority language without weakening evidence discipline.
- Define confidence statuses and required reason fields.
- Define anonymous-source caps and cap exceptions only when stronger evidence exists.
- Define source-independence rules: wire dependency, citation dependency, shared origin, source laundering, and repeated-origin evidence streams.
- Define limitation disclosure policy for API, briefing, and UI outputs.
- Define adversarial review/challenge process.
- Define MVP security/threat model for local deterministic use.

Required governance rules:

- Methods over conclusions.
- No automated final authority claims.
- Claim is the unit of analysis.
- Unknown, unresolved, and contested are valid outputs.
- Confidence must include visible reasons.
- Anonymous-source claims are capped.
- Source independence matters more than article volume.
- Narrative analysis must be labeled as analysis.
- Every meaningful transformation must be auditable.

Gate:

- No confidence or scoring rule exists only in code. Every rule is documented.
- User-facing docs disclose limitations and no-authority stance.

## Phase 2 — Backend Deterministic Core

Goal: build the first local epistemic primitives.

Owned backend files:

- `apps/api/README.md`
- `apps/api/pyproject.toml`
- `apps/api/app/__init__.py`
- `apps/api/app/main.py`
- `apps/api/app/models.py`
- `apps/api/app/audit.py`
- `apps/api/app/scoring.py`
- `apps/api/app/claim_extraction.py`
- `apps/api/app/source_graph.py`
- `apps/api/app/contradiction.py`
- `apps/api/app/briefing.py`

Tasks:

- Implement Pydantic models matching `DATA_MODEL.md` for source, evidence, claim, confidence, audit event, and briefing objects.
- Implement audit ledger with genesis event, append-only events, previous hash, event hash, and verification function.
- Implement deterministic scoring rules for primary evidence, source independence, anonymous caps, contradictions, unsupported evidence, and unknown/unresolved outputs.
- Implement source graph primitive with `wire_dependency`, `citation_dependency`, and `independence_notes`.
- Implement fixture-based contradiction detection only; do not imply broad semantic detection.
- Implement deterministic briefing generation from claims, evidence, scoring, limitations, and audit refs.
- Implement placeholder claim extraction with explicit limitation metadata.
- Implement FastAPI routes:
  - `GET /health`
  - `GET /sample`
  - `POST /analyze`
  - `GET /audit/verify`

Gate:

- Backend returns structured local analysis from fixtures without paid APIs, telemetry, secrets, or LLM calls.
- Backend app imports cleanly.
- Route outputs include limitations and audit references where analytical outputs are returned.

## Phase 3 — Evals + Tests

Goal: prove the primitives behave correctly and stay aligned with governance.

Owned eval/audit files:

- `apps/api/tests/test_audit.py`
- `apps/api/tests/test_scoring.py`
- `apps/api/tests/test_source_graph.py`
- `apps/api/tests/test_contradiction.py`
- `apps/api/tests/test_briefing.py`
- `apps/api/tests/test_claim_extraction.py`
- `evals/README.md`
- `evals/eval_plan.md`
- `evals/golden_cases.json`
- `docs/audits/SCAFFOLD_AUDIT.md`
- `docs/audits/scaffold_inventory.json`

Tests:

- Audit chain integrity.
- Genesis event creation.
- Tamper detection.
- Anonymous-source cap enforcement.
- Primary-evidence boost.
- Unknown/unresolved status handling.
- Source dependency warning.
- Fixture-based contradiction detection.
- Placeholder extractor honesty.
- Briefing includes limitations and audit references.
- No claim object is valid without status and confidence reason.

Gate:

- `python3 -m pytest apps/api/tests -q` passes from repo root after dependency install.
- Audit report lists created/changed files and verification commands.

## Phase 4 — Frontend/API Readiness

Goal: connect or preserve the UI without overstating backend maturity.

Owned frontend files:

- `apps/web/README.md`
- `apps/web/src/app/page.tsx`
- `apps/web/src/components/ClaimMatrix.tsx`
- `apps/web/src/components/EvidenceTrail.tsx`
- `apps/web/src/components/BriefingPanel.tsx`
- `apps/web/src/components/AuditTrail.tsx`
- `apps/web/src/components/NarrativeMap.tsx`
- `apps/web/src/components/SourceSpread.tsx`
- `apps/web/src/components/ContradictionBoard.tsx`

Tasks:

- Keep existing static dashboard aesthetic unless API contract is stable.
- Render claim matrix, evidence trail, audit trail, and briefing panel from fixture/API-shaped data where safe.
- Preserve explicit stubs/deferred labels for narrative map, source spread, and contradiction board if backend data is not ready.
- Enforce uncertainty rendering:
  - no claim displayed without status
  - no confidence displayed without reason
  - no briefing displayed without limitations
  - no analysis displayed without audit reference

Gate:

- UI cannot imply certainty beyond backend output.
- Stubbed/deferred panels are labeled honestly.

## Phase 5 — Demo Scenario

Goal: create one honest demo flow after deterministic primitives pass tests.

Tasks:

- Use controlled fixtures, not a live event feed.
- Prefer a historically resolved or synthetic/fixture scenario where claims, evidence, contradictions, and unknowns can be shown safely.
- Demonstrate:
  - placeholder claim extraction limitations
  - claim matrix
  - scoring reasons
  - source dependency notes
  - contradiction fixture
  - unknown/unresolved output
  - audit verification
  - limitations visibility

Gate:

- Demo is impressive as a method demonstration without claiming live-world completeness.

## Phase 6 — OSS Baseline Prep

Goal: make the repo credible for public inspection after the v0.2 primitives pass.

Tasks:

- Polish README and run instructions.
- Confirm Docker Compose path or document any gap.
- Add/confirm license, security policy, limitations, and adversarial review docs.
- Clean only clearly generated build junk such as `.next`, `tsbuildinfo`, and caches.
- Confirm no secrets, telemetry, paid API requirements, hidden scoring, or fake capability claims.

Gate:

- A stranger can inspect, run, challenge, and fork the local MVP.
- Baseline commit is ready only after code/tests/docs verification passes and human review accepts the untracked scaffold.

## Phase 7 — Public Announcement Prep

Positioning:

> Lumen does not tell users what is true. It exposes claims, evidence, contradictions, uncertainty, provenance, confidence reasons, and audit trails so humans can reason better.

Launch requirements:

- Working local app.
- Deterministic sample analysis.
- Claim matrix.
- Evidence trail.
- Source dependency notes.
- Confidence explanations.
- Audit verification.
- Briefing panel with limitations.
- README/run path.
- Clear limitations and challenge process.
