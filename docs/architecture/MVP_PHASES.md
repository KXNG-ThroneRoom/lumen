# Lumen MVP Phase Plan

## Status

Lumen is moving into the v0.6 controlled manual/local input lane. v0.2 established the deterministic local baseline, v0.3 stabilized backend/frontend contract and demo flow, v0.4 tightened detailed demo polish, v0.5 aligned public docs with the simplified controlled local demo, and v0.5.1/v0.5.2 tightened stabilization, fresh-clone readiness, and public release framing. v0.6 preserves those boundaries while making manual/local input explicit as an assertion-container layer, not live ingestion.

Current known state:

- Backend local deterministic API and tests exist.
- Static frontend uses the simplified black/white tabbed claim-story UI.
- Main public claim: "When does the regulation start?"
- Public tabs: Story, Evidence, Why uncertain, Audit.
- Legacy/internal detailed component files still exist and may support verification, but they are not the current public UX.
- MVP scope remains locked to local deterministic primitives, fixture-backed analysis, and controlled manual/local input boundaries.
- Manual input is an assertion container, not evidence of truth.
- v0.5 architecture scope is documented in `docs/architecture/V0_5_SCOPE.md`.
- v0.5.1 stabilization scope is documented in `docs/architecture/V0_5_1_SCOPE.md`.
- v0.6 controlled manual/local input scope is documented in `docs/architecture/V0_6_SCOPE.md` and `docs/architecture/CONTROLLED_INPUT_LAYER.md`.
- v0.5 launch gates are documented in `docs/architecture/LAUNCH_READINESS.md`.
- Fresh-clone expectations are documented in `docs/architecture/FRESH_CLONE_READINESS.md`.
- Roadmap and deferred-work boundaries are documented in `docs/architecture/ROADMAP_TO_V1.md` and `docs/architecture/DEFERRED_WORK.md`.


## Phase v0.6 — Controlled Manual/Local Input Layer

Goal: make manually supplied local text and local-file payloads explicit, auditable, and bounded without introducing live ingestion, broad extraction, persistence, auth/accounts, telemetry, LLMs, paid APIs, or production verification.

Owned architecture files:

- `docs/architecture/V0_6_SCOPE.md`
- `docs/architecture/CONTROLLED_INPUT_LAYER.md`
- `docs/architecture/API_CONTRACT.md`
- `docs/architecture/MVP_PHASES.md`
- `docs/architecture/ROADMAP_TO_V1.md`
- `docs/architecture/DEFERRED_WORK.md`

Tasks:

- Define v0.6 as controlled manual/local input only.
- Document RawDocument as the preserved local submission envelope.
- Document SourceDocument as the normalized local analysis container derived from RawDocument.
- Update the API contract for `POST /ingest/manual` as a deterministic local boundary.
- Preserve `/sample` as canonical fixture demo and `/analyze` as the existing local-analysis shortcut.
- Explicitly defer URL fetching, RSS polling, crawling, scraping, live feeds, automated source discovery, LLM extraction/calls, paid APIs, telemetry, auth/accounts, and production storage complexity.
- Preserve the rule that manual input is evidence of what was supplied, not evidence that the supplied article, source label, URL-looking string, or underlying claim is true.

Gate:

- v0.6 docs do not claim live ingestion or production verification.
- `POST /ingest/manual` is described as local document-container creation, not source retrieval.
- RawDocument/SourceDocument lifecycle states carry limitations and audit references.
- Submitted URLs remain inert strings unless a future scope explicitly authorizes retrieval.
- No v0.6 architecture doc introduces network, secret, account, telemetry, database, paid API, or LLM default-path requirements.

## Phase v0.5.1 — Stabilization Hygiene + Fresh-Clone Readiness

Goal: preserve the v0.5 controlled local demo boundary while making the repo easier to verify, explain, and review from a clean checkout.

Owned architecture files:

- `docs/architecture/MVP_PHASES.md`
- `docs/architecture/ROADMAP_TO_V1.md`
- `docs/architecture/DEFERRED_WORK.md`
- `docs/architecture/V0_5_1_SCOPE.md`
- `docs/architecture/FRESH_CLONE_READINESS.md`

Tasks:

- Define v0.5.1 as stabilization/hygiene, not capability expansion.
- Document expected fresh-clone install, verification, demo flow, and environment assumptions.
- Keep v0.5.1 positioned between public-readiness and later roadmap phases.
- Keep deferred-work language explicit that future capabilities are not current promises.
- Remove or reframe stale public-facing references to old dashboard surfaces.
- Prevent scope creep into live ingestion, paid APIs, LLM calls, telemetry, auth/accounts, databases, blockchain, broad verification, or UI redesign.

Gate:

- `V0_5_1_SCOPE.md` says v0.5.1 is hygiene/stabilization only.
- `FRESH_CLONE_READINESS.md` provides install, verification, demo, and environment guidance.
- Roadmap sequencing keeps v0.6 controlled manual/local input separate from future live-ingestion capability.
- No v0.5.1 architecture doc claims new analytical capability.

## Phase v0.5 — Launch Hygiene + Public Readiness

Goal: make the controlled local fixture demo publicly legible, reviewable, and honest without adding live-data or production-intelligence scope.

Owned architecture/demo files:

- `docs/architecture/LAUNCH_READINESS.md`
- `docs/architecture/DEMO_FLOW.md`
- `docs/architecture/MVP_PHASES.md`
- `docs/architecture/V0_5_SCOPE.md`
- `docs/architecture/ROADMAP_TO_V1.md`
- `docs/architecture/DEFERRED_WORK.md`
- `docs/demo/LOCAL_DEMO_WALKTHROUGH.md`

Tasks:

- Define v0.5 as launch hygiene/public-readiness, not analytical expansion.
- Align architecture and demo docs with the simplified four-tab claim-story UI.
- Reframe old detailed component names as legacy/internal if mentioned.
- Create a roadmap to v1 that separates later phases from current capability.
- Create a deferred-work list covering live ingestion, paid APIs, LLM calls, telemetry, accounts/auth, database/storage complexity, blockchain, and broad verification claims.
- Prevent scope creep into live ingestion, paid APIs, LLM calls, telemetry, auth/accounts, databases, blockchain, hidden scoring, or final truth determination.

Gate:

- `V0_5_SCOPE.md` clearly separates public-ready demo commitments from deferred work.
- `LAUNCH_READINESS.md` defines pass/blocker criteria and verification commands.
- `DEMO_FLOW.md` and `LOCAL_DEMO_WALKTHROUGH.md` match the runnable simplified UI.
- `ROADMAP_TO_V1.md` and `DEFERRED_WORK.md` prevent overclaiming future capabilities as current features.
- No v0.5 architecture doc claims live coverage, production reliability, or final authority.

## Phase v0.4 — Demo Polish + Launch Readiness

Goal: make the controlled local fixture demo precise, reviewable, and honest without adding live-data or production intelligence scope.

Historical focus:

- define pass/blocker criteria;
- document API contract and controlled fixture flow;
- ensure detailed internal components preserve uncertainty, limitations, and audit references;
- prevent scope creep into live ingestion, paid APIs, LLM calls, telemetry, accounts, databases, blockchain, hidden scoring, or final truth determination.

Gate:

- detailed demo contract and verification gates exist;
- architecture docs identify fixture-backed vs deferred internals;
- no architecture doc claims production-grade real-world verification.

## Phase v0.3 — Backend/Frontend Contract + Demo Flow

Goal: stabilize the local API response shape and demo sequence around deterministic fixture-backed analysis.

Historical focus:

- document `/health`, `/sample`, `/analyze`, and `/audit/verify`;
- keep fixture response deterministic;
- expose limitations and auditability in the response contract;
- support frontend/static fixture parity.

Gate:

- API contract matches backend/static fixture shapes;
- demo flow has no hidden network, paid API, telemetry, secret, or LLM dependency.

## Phase v0.2 — Deterministic Local Baseline

Goal: build the first local method primitives.

Historical focus:

- Pydantic models for source, evidence, claim, confidence, audit event, and briefing objects;
- tamper-evident local audit ledger primitive;
- deterministic scoring rules;
- fixture-based contradiction handling;
- placeholder claim extraction with explicit limitation metadata;
- FastAPI routes for local inspection.

Gate:

- backend returns structured local analysis from fixtures without paid APIs, telemetry, secrets, or LLM calls;
- route outputs include limitations and audit references where analytical outputs are returned.

## Phase 1 — Governance Hardening

Goal: make the constitution enforceable in product and code.

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

- no confidence or scoring rule exists only in code;
- user-facing docs disclose limitations and no-authority stance.

## Phase 2 — Evals + Tests

Goal: prove the primitives behave correctly and stay aligned with governance.

Tests cover:

- audit chain integrity;
- genesis event creation;
- tamper detection;
- anonymous-source cap enforcement;
- primary-evidence boost;
- unknown/unresolved status handling;
- source dependency warning;
- fixture-based contradiction detection;
- placeholder extractor honesty;
- briefing includes limitations and audit references;
- no claim object is valid without status and confidence reason.

Gate:

- API tests pass from repo root after dependency install;
- audit/reporting docs list verification commands.

## Phase 3 — Fixture and Public Demo Expansion

Goal: improve controlled-fixture coverage only after v0.5 launch hygiene is stable.

Allowed direction:

- add synthetic or historically neutral fixtures;
- add edge cases for contested, unresolved, unsupported, and contradicted claims;
- improve local manual-text ergonomics with explicit placeholder limitations.

Not allowed without a new scope:

- live feeds;
- paid APIs;
- LLM-backed default analysis;
- production source coverage;
- final verdicts.

## Phase 4 — OSS Baseline Prep

Goal: make the repo credible for public inspection.

Tasks:

- polish README and run instructions;
- confirm local setup and optional Compose path;
- maintain license, security policy, limitations, and adversarial review docs;
- clean only clearly generated build junk when explicitly scoped;
- confirm no secrets, telemetry, paid API requirements, hidden scoring, or fake capability claims.

Gate:

- a stranger can inspect, run, challenge, and fork the local MVP.

## Phase 5 — Public Announcement Prep

Positioning:

> Lumen does not tell users what is true. It exposes claims, evidence, contradictions, uncertainty, confidence reasons, and audit trails so humans can reason better.

Launch requirements:

- working local app;
- deterministic sample analysis;
- simplified four-tab public story;
- evidence and uncertainty explanation;
- confidence/method explanation without verdict language;
- audit/check explanation without proof claims;
- README/run path;
- clear limitations and challenge process.

## Phase v1.0 — Public Method Baseline

Goal: a stable, inspectable open-source baseline for local claim-inspection methodology.

v1 should not be declared until implementation, docs, tests, governance, public wording, and limitations agree.
