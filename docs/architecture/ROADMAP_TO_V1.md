# Lumen Roadmap to v1

Version: v0.5.1-stabilization-hygiene

## Roadmap stance

This roadmap is a restraint document. It separates what v0.5/v0.5.1 can honestly announce from what may come later.

v0.5 is a controlled local fixture demo. v0.5.1 is stabilization and hygiene for that same demo, not capability expansion. v1 should remain method-first, open-source, auditable, and human-centered. No phase below authorizes final truth determination, hidden scoring, paid-only infrastructure, telemetry, or production claims before they are implemented and verified.

## Current baseline: v0.5

Goal: public-readiness for the controlled local demo.

Deliverables:

- simplified four-tab claim-story UI;
- controlled start-date contradiction fixture;
- deterministic local API and fixture substrate;
- visible contested/no-final-verdict language;
- aggregate local verification gate;
- launch docs that match current reality;
- deferred-work list to prevent scope creep.

Gate:

- local verification passes;
- public docs do not describe stale dense dashboard UX as current;
- launch copy avoids capability overclaims.

## Current stabilization step: v0.5.1

Goal: fresh-clone readiness and roadmap hygiene for the existing v0.5 controlled local demo.

Deliverables:

- explicit v0.5.1 scope lock as stabilization/hygiene;
- documented fresh-clone install, verification, and demo flow;
- known environment assumptions for local review;
- roadmap sequencing that keeps later capability work separate;
- deferred-work language that remains honest and non-promissory.

Gate:

- `bash scripts/verify_lumen.sh` remains the aggregate local verifier;
- setup documentation requires no secrets, paid services, telemetry, accounts, live feeds, or LLM calls for the default demo path;
- no v0.5.1 document expands the public claim surface beyond the controlled fixture.

## Phase v0.6 — Documentation and challenge hardening

Goal: make public inspection and contributor review easier without adding analytical surface.

Candidate work:

- tighten README, limitations, contribution, and challenge-path cross-links;
- add public screenshots only after verifier passes;
- add doc checks for stale UI language and overclaim patterns;
- make operator walkthroughs reproducible from a clean clone;
- clarify which detailed components are internal/legacy vs public.

Gate:

- a new contributor can run and challenge the local demo without maintainer context;
- all public docs preserve controlled local fixture boundaries.

## Phase v0.7 — Fixture depth and evaluation coverage

Goal: improve method demonstration quality with more controlled cases, not live coverage.

Candidate work:

- add additional synthetic or historically neutral fixture cases;
- expand golden cases for unsupported, contradicted, contested, and unresolved outputs;
- test source-dependency and missing-evidence behavior across fixtures;
- verify that UI copy stays modest across cases.

Gate:

- fixture expansion improves edge-case coverage without implying global source coverage or live monitoring.

## Phase v0.8 — Local input ergonomics

Goal: make manually supplied local text easier to inspect while preserving default deterministic behavior.

Candidate work:

- improve local text input UX;
- expose placeholder extraction limits close to manual-output results;
- add deterministic parsing/error states;
- document privacy expectations for local-only use.

Gate:

- no URL fetching, live ingestion, external model call, telemetry, account, or hidden network dependency is introduced.

## Phase v0.9 — Packaging and reproducibility

Goal: make the local demo easier to run and verify across machines.

Candidate work:

- harden Docker/local setup documentation;
- add reproducibility notes for fixture outputs;
- improve versioning for fixture, governance rules, and demo contract;
- add release checklist for signed tags or checksums if appropriate.

Gate:

- packaging improves repeatability without changing analytical claims or adding hosted-service dependence.

## Phase v1.0 — Public method baseline

Goal: a stable, inspectable open-source baseline for local claim-inspection methodology.

Possible v1 requirements:

- documented governance/scoring rules are versioned and enforced by tests;
- local demo and fixture suite run from clean setup instructions;
- limitations and challenge process are public and close to outputs;
- audit trail explains transformations without proving underlying claims;
- public UI remains understandable to non-technical users;
- internal/developer inspection path remains available for auditability;
- security and dependency policies are documented and followed.

v1 should not be declared until the implementation, docs, tests, and public wording agree.

## Explicit non-roadmap items

The following are not automatic roadmap commitments:

- production intelligence service;
- broad live web/news ingestion;
- paid-source integrations;
- LLM-backed default analysis;
- user accounts and personalization;
- telemetry/analytics;
- blockchain anchoring;
- authoritative verdicts;
- geopolitical monitoring product.

Any future proposal for those areas requires a new scope document, governance review, security review, user-visible limitations, tests, and explicit human approval.
