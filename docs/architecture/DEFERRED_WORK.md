# Lumen Deferred Work

Version: v0.6-controlled-manual-input

## Purpose

This document lists work intentionally deferred from v0.5/v0.5.1/v0.5.2 and from v0.6. Deferred does not mean forgotten, promised, or silently implemented. It means the item is outside the current controlled local demo and controlled manual/local input boundary.

v0.5 should announce only what exists: a local deterministic fixture demo with a simplified claim-story UI. v0.5.1/v0.5.2 should only stabilize that boundary through fresh-clone readiness, verification clarity, roadmap discipline, release-packet hygiene, and public framing. v0.6 is controlled manual/local input only: submitted text, local files, source labels, and URL-looking strings are assertion containers, not facts, live sources, or production ingestion feeds.

## Deferred capability categories

### Live ingestion and monitoring

Deferred:

- crawling;
- RSS polling;
- URL fetching;
- live current-event feeds;
- geopolitical monitoring;
- automated source discovery.

Reason: v0.5 demonstrates method visibility with controlled fixtures, and v0.6 only permits user-supplied local/manual containers. Live data would expand the claim surface and create false completeness pressure.

Revisit when: governance, security, source-coverage limits, caching, evidence preservation, and user-facing disclaimers are designed and tested.

### Paid APIs, hosted dependencies, and LLM calls

Deferred:

- paid search/news APIs;
- proprietary hosted extraction or scoring;
- default-path LLM calls;
- hidden model services;
- secrets required for local demo.

Reason: the current demo must remain free, inspectable, deterministic, and runnable without credentials.

Revisit when: optional paths can be isolated from the default demo and labeled clearly.

### Production claim extraction

Deferred:

- broad automatic claim extraction;
- semantic claim clustering;
- multilingual extraction;
- image/video claim extraction;
- robust quote attribution.

Reason: placeholder/local extraction is enough for the controlled v0.6 manual/local demo. Production extraction would need evaluation data, failure-mode disclosures, and stronger review.

Revisit when: fixture/eval coverage can measure extraction failures and user-facing copy makes uncertainty explicit.

### Broad contradiction detection

Deferred:

- semantic contradiction detection across arbitrary documents;
- temporal and causal contradiction inference;
- conflict resolution logic;
- automatic claim settlement.

Reason: v0.6 shows a controlled date conflict and can inspect only supplied local assertions under limitations. It does not infer contradictions broadly or resolve disputes.

Revisit when: contradiction types, test fixtures, and limitation wording are mature.

### Source-independence inference

Deferred:

- ownership/funding inference;
- affiliation inference;
- geographic/source reputation modeling;
- coordinated campaign detection;
- anonymous-source laundering detection beyond controlled examples.

Reason: v0.6 can explain that source quantity is not independence, but it must not infer metadata that is absent from fixtures or user-supplied local input.

Revisit when: data provenance, governance rules, and error disclosures are explicit.

### Production infrastructure and storage complexity

Deferred:

- durable databases;
- graph databases;
- vector stores;
- object storage;
- background jobs;
- queues;
- production document stores for RawDocument/SourceDocument;
- multi-tenant hosting;
- account/auth systems;
- personalization;
- telemetry/analytics.

Reason: v0.6 is local, deterministic, and manually bounded. Production infrastructure would add operational and privacy risks without improving launch honesty.

Revisit when: a scoped deployment plan exists and is approved separately.

### Audit hardening beyond local tamper evidence

Deferred:

- external timestamping;
- signed releases;
- remote anchoring;
- blockchain anchoring;
- tamper-proof claims.

Reason: current audit trail is a method trace and tamper-evident local primitive. It does not prove a claim or prevent filesystem-level replacement.

Revisit when: release and reproducibility needs justify added complexity.

### Public UI expansion

Deferred:

- restoring the old dense seven-component dashboard as public UX;
- adding advanced analyst panels to the launch page;
- exposing raw fingerprints, audit IDs, `.md` file references, machine labels, or provenance strings in the main public view;
- redesigning beyond current simplified tabbed story.

Reason: v0.5 public-readiness depends on clarity for normal readers. Detailed internals can remain available for developers and reviewers without overwhelming the public story.

Revisit when: there is a separate design scope for advanced/developer modes.

## Deferred-work acceptance rule

A deferred item may move into scope only with:

- an explicit scope document;
- governance review;
- security/privacy review when data or network behavior changes;
- tests/evals appropriate to the claim surface;
- public limitations close to outputs;
- verification commands;
- human approval for the scope change.

Documentation cleanup, fresh-clone instructions, roadmap edits, or manual/local input wording do not move deferred capabilities into scope. Capability changes require the acceptance rule above before implementation or public announcement.


### Live-ingestion migration from controlled input

Deferred:

- treating `POST /ingest/manual` as a URL ingestion endpoint;
- dereferencing `declared_url` fields;
- converting RawDocument into fetched web captures;
- source reachability checks;
- background refresh of submitted material;
- source-monitoring subscriptions.

Reason: v0.6 document vocabulary is for manual/local input only. Reusing the same words for live retrieval without a new scope would blur the truth boundary and make users think Lumen inspected sources it never fetched.

Revisit when: a separate live-ingestion scope defines governance, security/privacy review, evidence preservation, cache/retention rules, failure states, limitation wording, and tests.
