# Lumen Demo Flow

Version: v0.5-launch-hygiene

## Purpose

This document defines the v0.5 controlled local demo flow. The public demo is a simplified claim story: one contested start-date claim, four tabs, plain language, and visible uncertainty.

The demo must show Lumen as method-first infrastructure. It must not imply live coverage, production intelligence reliability, final truth determination, or broad semantic understanding.

Doctrine for every demo surface:

- Methods over conclusions.
- More informed humans, not a new oracle.
- Unknown, unresolved, contested, unsupported, and contradicted are valid outputs.
- Confidence explains a rule path; it is not a command to believe.
- Controlled local fixtures only.

## v0.5 demo boundary

v0.5 is launch hygiene and public-readiness. It does not expand analytical capability.

Demo-ready means:

- the backend and frontend can render the canonical fixture locally;
- the public UI presents the simplified tabbed claim story;
- limitations, uncertainty, and no-final-verdict language stay visible;
- internal audit/contract detail remains available for developers without crowding the public view;
- no path implies live coverage, final truth determination, production intelligence reliability, or hidden scoring.

## Demo scenario boundary

Use the controlled start-date contradiction fixture.

Canonical public story:

- Main claim: "When does the regulation start?"
- News report: June 1.
- Official filing/record: July 1.
- Lumen marks the claim as contested instead of guessing.
- The official record is stronger support, but the conflict remains visible until corrected, explained, or reviewed.

Why this scenario:

- It is low-risk and non-geopolitical.
- It demonstrates claims, evidence, contradiction, source dependency, uncertainty, and auditability without pretending to resolve a live dispute.
- It keeps v0.5 focused on public clarity rather than new epistemic machinery.

## Out of scope for the demo

Do not include:

- live current-events or geopolitical analysis;
- URL fetching or RSS ingestion;
- paid APIs;
- LLM calls;
- production source coverage claims;
- broad semantic contradiction claims;
- final authority language;
- hidden scoring or hidden weighting;
- telemetry, accounts, authentication, or personalization;
- database/storage complexity;
- blockchain anchoring.

## Demo flow sequence

### Step 1 — Verify local boundary

Run from repo root before public capture or announcement:

```text
bash scripts/verify_lumen.sh
```

The verifier should pass API tests, compile checks, static UI verification, web typecheck, and institutional-memory index checks.

### Step 2 — Start local backend

Expected command from repo root:

```text
uvicorn apps.api.app.main:app --reload
```

The local API must expose:

- `GET /health`
- `GET /sample`
- `POST /analyze`
- `GET /audit/verify`

The backend must run without secrets, paid services, telemetry, external network calls, or LLM calls.

### Step 3 — Verify method boundary

Open or call:

```text
GET /health
```

Confirm the health response shows local deterministic mode, rule/schema version, limitation reference, no production-readiness claim, and no final-authority claim.

### Step 4 — Load fixture analysis

Open or call:

```text
GET /sample
```

The response shape is documented in `docs/architecture/API_CONTRACT.md`. It remains an internal/developer inspection surface for claims, evidence, sources, source graph, contradiction fixture, briefing, audit trail, audit verification, and limitations.

### Step 5 — Render current public frontend

Start the web app:

```text
npm run dev --prefix apps/web
```

Open the local Next.js URL printed by the dev server.

The public v0.5 UI must show:

- black/white simplified claim-story frame;
- main claim: "When does the regulation start?";
- summary that the news report says June 1 and the official filing says July 1;
- four tabs: Story, Evidence, Why uncertain, Audit;
- yellow/uncertain, blue/supporting, and red/conflict visual cues;
- controlled-local-demo and no-human-replacement language.

The public v0.5 UI must not show raw hashes, audit IDs, `.md` references, underscores/machine labels, visible provenance strings, or dense technical dashboard wording.

### Step 6 — Demonstrate the Story tab

Show the chronological breakdown:

1. a news report says June 1;
2. the official record says July 1;
3. the two dates do not match;
4. no final verdict yet.

Operator stance:

```text
Lumen keeps the disagreement visible instead of smoothing it over.
```

### Step 7 — Demonstrate the Evidence tab

Show:

- official record as strongest support;
- news report as conflicting source;
- source check explaining that more coverage is not the same as more proof.

Operator stance:

```text
The official record carries more weight, but Lumen does not pretend that the public disagreement disappeared.
```

### Step 8 — Demonstrate the Why uncertain tab

Show:

- what is known: one source says June 1 and one official record says July 1;
- what is not known: whether the report was wrong, outdated, or missing context;
- what would help: correction, newer official record, or human source review.

Operator stance:

```text
The honest answer is contested. Lumen supports review; it does not replace it.
```

### Step 9 — Demonstrate the Audit tab

Show:

- the page uses the same local sample as the backend;
- the method signal is a caution flag, not a truth score;
- checks are recorded;
- raw internal labels stay out of the public view.

Operator stance:

```text
Internal tracking helps inspect the method path. It does not prove that a claim is correct.
```

### Step 10 — Optional manual-text path

After the fixture demo works, `POST /analyze` may be shown with a short local text snippet.

Rules:

- treat submitted text as local input only;
- disclose placeholder extraction limitations;
- return the same response envelope as `/sample`;
- preserve unknown/unresolved/unsupported statuses where evidence is absent;
- do not imply production extraction quality.

Safe example request:

```json
{
  "topic": "Manual local text demo",
  "source_name": "operator_supplied_text",
  "text": "A committee notice says the pilot starts in June. A later memo says the date is still under review."
}
```

## Legacy/internal component note

The repository still contains detailed component files named BriefingPanel, ClaimMatrix, EvidenceTrail, AuditTrail, NarrativeMap, SourceSpread, and ContradictionBoard. In v0.5 they are legacy/internal honesty components and verification targets, not the public demo layout.

Do not use screenshots or copy that present those components as the public v0.5 UI.

## Demo copy rules

Allowed language:

- "Lumen exposes claims, evidence, uncertainty, and audit trails."
- "This is a deterministic local fixture demo."
- "The system shows why a claim is contested or unresolved."
- "Confidence is a transparent method signal, not a command to believe."
- "The audit trail records transformations and method references."

Prohibited language categories:

- guarantee-of-truth phrases;
- claims that the product validates reality itself;
- fully automated intelligence claims;
- production-grade global coverage claims;
- language saying the system settles the dispute;
- propaganda-detection claims;
- deception-proof claims;
- complete source coverage claims;
- live geopolitical analysis claims.

## Screenshot path checklist

A launch-quality screenshot set should capture:

1. full simplified claim-story frame;
2. Story tab with the June 1 vs July 1 sequence;
3. Evidence tab showing official record support and news-report conflict;
4. Why uncertain tab showing what remains unknown;
5. Audit tab showing checks without raw internal identifiers;
6. footer or nearby note that this is a controlled local demo only.

Screenshots must not crop away uncertainty or controlled-demo language.

## Failure states that block demo readiness

Block demo readiness if any of these are true:

- docs describe the old dense seven-component dashboard as the current public UI;
- public UI copy implies the issue is settled;
- public UI hides controlled-local-demo limits;
- fixture data is presented as live analysis;
- repeated source count is presented as independent corroboration;
- copy implies certainty beyond backend data;
- hidden network, paid API, telemetry, account, database, or LLM path is required.

## Handoff notes for sibling lanes

Backend lane:

- Keep fixture response deterministic.
- Keep API contract inspectable, but do not require public UI to expose raw internal fields.

Frontend lane:

- Preserve the simplified four-tab UI unless a later scope doc explicitly changes it.
- Keep legacy/internal components labeled honestly if they remain in the repo.
- Do not reintroduce dense dashboard copy into the public page.

Governance lane:

- Confirm limitations and challenge/adversarial review language remain close to public outputs.
- Confirm confidence language remains methodological.
- Confirm prohibited copy does not appear.

Verifier lane:

- Run the aggregate verifier.
- Scan launch docs for stale dense-dashboard wording and capability overclaims.
