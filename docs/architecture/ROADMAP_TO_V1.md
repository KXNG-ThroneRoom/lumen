# Lumen Roadmap to v1

Version: v0.6-controlled-manual-input

## Roadmap stance

This roadmap is a restraint document. It separates what v0.6 can honestly announce from what remains deferred, while preserving the v0.5/v0.5.1/v0.5.2 stabilization history.

v0.5 is a controlled local fixture demo. v0.5.1/v0.5.2 are stabilization, release-packet, and public-framing hygiene for that same demo. v0.6 is controlled manual/local input only: submitted text, local files, source labels, and URL-looking strings are assertion containers, not verified facts or live source retrieval. v1 should remain method-first, open-source, auditable, and human-centered. No phase below authorizes final truth determination, hidden scoring, paid-only infrastructure, telemetry, live URL/RSS ingestion, broad extraction, persistence, auth/accounts, LLM-backed default analysis, or production claims before they are implemented and verified under explicit scope.

## Current baseline: v0.5/v0.5.2

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

## Phase v0.6 — Controlled manual/local input

Goal: accept manually supplied local text or explicitly local-file payloads as assertion containers, preserving uncertainty, visible limitations, and auditability without adding live ingestion or production verification.

Candidate work:

- define RawDocument and SourceDocument lifecycle states;
- add or document `POST /ingest/manual` as the controlled local boundary;
- keep submitted URLs inert unless future scope authorizes retrieval;
- carry limitations that articles, pasted excerpts, local files, source labels, and URL-looking strings are containers of claims or user assertions, not facts;
- map existing `POST /analyze` local-text behavior to the document lifecycle;
- add local deterministic validation/error states for empty or unsupported input.

Gate:

- no URL fetching, crawling, scraping, RSS polling, live feeds, paid APIs, LLM calls, telemetry, auth/accounts, persistence expansion, or production storage complexity;
- manual input is represented as supplied material, not verified truth;
- audit events explain local transformations without proving real-world correctness.

## Phase v0.7 — Documentation, challenge hardening, and fixture depth

Goal: make public inspection easier and improve method demonstration quality with more controlled cases, not live coverage.

Candidate work:

- tighten README, limitations, contribution, and challenge-path cross-links;
- add doc checks for stale UI language and overclaim patterns;
- add additional synthetic or historically neutral fixture cases;
- expand golden cases for unsupported, contradicted, contested, and unresolved outputs;
- test source-dependency and missing-evidence behavior across fixtures;
- verify that UI copy stays modest across cases.

Gate:

- fixture expansion improves edge-case coverage without implying global source coverage or live monitoring.

## Phase v0.8 — Local input ergonomics hardening

Goal: make manually supplied local text easier to inspect after the v0.6 boundary is stable while preserving default deterministic behavior.

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
- broad live web/news ingestion, crawling, scraping, RSS polling, or URL fetching;
- paid-source integrations;
- LLM-backed default analysis;
- user accounts and personalization;
- telemetry/analytics;
- blockchain anchoring;
- authoritative verdicts;
- geopolitical monitoring product.

Any future proposal for those areas requires a new scope document, governance review, security review, user-visible limitations, tests, and explicit human approval.
