# Lumen v0.5 Launch Readiness

Version: v0.5-launch-hygiene

## Readiness stance

v0.5 is public-readiness and launch-hygiene work for the controlled local demo. It is not a production-readiness certification and it does not add analytical capability.

Lumen is launch-ready for v0.5 only if a reviewer can run the local fixture demo, understand the simplified claim story, see uncertainty preserved, and verify that public docs do not imply live coverage, final authority, hidden scoring, or real-world verification completeness.

Allowed readiness labels:

- `ready-controlled-local-demo`: local verifier passes and public copy matches the simplified fixture demo.
- `ready-with-documented-limitations`: core demo works, but non-blocking gaps are documented close to the output.
- `not-ready`: any blocker in this document remains unresolved.

Do not use labels that imply production fitness, automated intelligence readiness, final judgment, or live-event coverage.

## v0.5 scope

v0.5 is launch hygiene:

- align public documentation with the current simplified black/white tabbed claim-story UI;
- preserve the controlled local fixture boundary;
- keep the existing backend/API contract available for internal inspection;
- make old detailed component names clearly legacy/internal when mentioned;
- document v1 roadmap and deferred work without pulling it into the launch;
- keep verification language auditable and modest.

v0.5 does not add live ingestion, paid APIs, LLM calls, telemetry, accounts, authentication, database/storage complexity, blockchain anchoring, or a new analytical claim surface.

## Required local verification

Run from repo root:

```text
bash scripts/verify_lumen.sh
```

Expected result for launch-ready status:

- institutional-memory index check passes;
- API tests pass;
- API modules compile;
- static UI verification passes;
- web typecheck passes;
- any failure is recorded as a blocker, not ignored.

## Current public UI gates

The public demo UI is the simplified claim-story interface, not the old dense dashboard.

Required visible story:

- Main claim: "When does the regulation start?"
- Explanation: "Two sources disagree. A news report says June 1. An official filing says July 1. Lumen marks this as contested instead of guessing."
- Tabs: Story, Evidence, Why uncertain, Audit.
- Visual language: yellow/uncertain for contested, blue/supporting for stronger support, red/conflict for disagreement.
- Footer or nearby note: controlled local demo only; no live news; no replacement for human judgment.

Required public-copy behavior:

- explain the disagreement in human-readable language;
- show the official record as stronger support without claiming the dispute is settled;
- explain why uncertainty remains;
- keep technical internals out of the main public view;
- say that internal tracking exists without exposing raw fingerprints, machine labels, or source-file references in the public UI.

Public UI must not show raw hashes, audit IDs, `.md` references, underscores/machine labels, visible provenance strings, or dense technical dashboard wording.

## Legacy/internal component policy

The old detailed component files may remain in the repository as legacy/internal honesty components and static verification targets. If mentioned in architecture docs, label them as internal/legacy surfaces, not the current public UX.

Legacy/internal component names include:

- BriefingPanel
- ClaimMatrix
- EvidenceTrail
- AuditTrail
- NarrativeMap
- SourceSpread
- ContradictionBoard

These names must not be described as the public v0.5 layout. The public layout is the four-tab claim story.

## API readiness gates

The local API remains part of the inspectable demo substrate. It must stay deterministic and local.

`GET /health` must show:

- service status;
- local deterministic method boundary;
- limitations or limitations reference;
- no production-readiness claim;
- no final-authority claim.

`GET /sample` must return the canonical controlled fixture response with claims, evidence, sources, source graph, contradictions, briefing, audit trail/verification, limitations, and limitation reference.

`POST /analyze` must:

- accept manually supplied local text only;
- not fetch URLs;
- not call paid APIs;
- not call LLMs in the default path;
- disclose placeholder extraction limits;
- return the same analysis envelope shape as `/sample`.

`GET /audit/verify` must explain audit-chain consistency only. It must not say the audit trail proves an underlying claim.

## Content and copy readiness gates

Pass requires public and launch-adjacent copy to preserve these messages:

- Lumen exposes methods, evidence, uncertainty, contradictions, and auditability so humans can reason better.
- Lumen helps humans reason; it does not replace judgment.
- The demo uses controlled local fixtures unless explicitly labeled otherwise.
- Confidence is a visible method signal, not a verdict.
- Contradictions expose unresolved disputes; they do not settle them.
- Audit trails record transformation history and can detect inconsistent history; they do not prove a claim.

Block readiness if copy implies:

- final truth determination;
- article-level truth labels;
- live geopolitical analysis;
- complete source coverage;
- production intelligence reliability;
- propaganda or deception certainty;
- hidden model/scoring authority.

## Documentation readiness gates

Before v0.5 public-readiness is claimed, these docs must agree:

- `docs/architecture/V0_5_SCOPE.md` defines launch hygiene and deferrals;
- `docs/architecture/DEMO_FLOW.md` matches the simplified four-tab public demo;
- `docs/demo/LOCAL_DEMO_WALKTHROUGH.md` gives an operator path for the current UI;
- `docs/architecture/MVP_PHASES.md` places v0.5 after v0.4 as public-readiness hygiene, not new capability;
- `docs/architecture/ROADMAP_TO_V1.md` separates future phases from v0.5;
- `docs/architecture/DEFERRED_WORK.md` lists deferred items explicitly;
- `LIMITATIONS.md` remains linked or visible near outputs by public docs and launch materials;
- governance docs preserve no-authority, confidence-reason, and auditability rules.

## Blocker taxonomy

Use these labels in handoff or verification reports:

- `ui-reality-blocker`: docs describe the old dense dashboard as the public UI.
- `copy-overclaim-blocker`: copy implies final authority, live coverage, broad verification, or hidden judgment.
- `demo-boundary-blocker`: default demo requires network calls, paid services, telemetry, secrets, accounts, or LLM calls.
- `api-contract-blocker`: route or schema drift prevents local fixture inspection.
- `audit-overclaim-blocker`: audit wording implies proof of the underlying claim.
- `docs-blocker`: launch docs disagree with the runnable implementation.

## Final readiness decision

A v0.5 readiness claim is valid only when the local verifier passes, stale public-UX references are removed or reframed, deferred work is explicit, and no public surface expands beyond the controlled local demo.
