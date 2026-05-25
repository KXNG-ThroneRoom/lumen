# Lumen Demo Flow

Version: v0.4-demo-polish

## Purpose

This document defines the local demo flow for Lumen v0.3 and the v0.4 controlled-demo polish layer.

The demo must show Lumen as method-first infrastructure: claims, evidence, uncertainty, provenance, source dependency, limitations, and audit trails are visible together. The demo must not imply live coverage, production intelligence reliability, final truth determination, or broad semantic understanding.

Doctrine for every demo surface:

- Methods over conclusions.
- More informed humans, not a new oracle.
- Unknown, unresolved, contested, unsupported, and contradicted are valid outputs.
- Confidence explains a rule path; it is not a command to believe.
- Controlled fixtures only.

## v0.4 demo boundary

v0.4 is demo polish, not expanded analytical capability. The operator should present it as a controlled fixture demonstration of method visibility.

Demo-ready means:

- the backend and frontend can render the canonical fixture locally;
- limitations, confidence reasons, audit references, and unresolved states stay visible;
- fixture-backed panels are labeled as such;
- deferred or stubbed panels say exactly what is missing;
- no path implies live coverage, final truth determination, production intelligence reliability, or hidden scoring.

## Demo scenario boundary

Use a controlled synthetic or historically neutral fixture that demonstrates a start-date or event-detail contradiction.

Recommended canonical scenario:

- Topic: `Fixture: regulation start-date contradiction`
- Claim A: a source states that a rule starts on 1 June.
- Claim B: another fixture source states that the same rule starts on 1 July.
- Evidence includes one primary/near-primary fixture item, one repeated wire/dependent item, and one missing/unclear evidence item.
- Source dependency shows that repeated article count is not independent corroboration.
- Contradiction board shows the date conflict as unresolved.
- Briefing preserves uncertainty and points to limitations.

Why this scenario:

- It is low-risk and non-geopolitical.
- It demonstrates claims, evidence, contradictions, source dependency, and audit refs without pretending to resolve a real-world live dispute.
- It keeps the sprint integration-focused and avoids deep epistemic algorithm design.

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
- telemetry, accounts, or personalization.

## Demo flow sequence

### Step 1 — Start local backend

Expected command from repo root:

```text
uvicorn apps.api.app.main:app --reload
```

Acceptable if the repo uses a wrapper script, but the local API must expose:

- `GET /health`
- `GET /sample`
- `POST /analyze`
- `GET /audit/verify`

The backend must run without secrets, paid services, telemetry, external network calls, or LLM calls.

### Step 2 — Verify method boundary

Open or call:

```text
GET /health
```

The demo operator should confirm the health response shows:

- local deterministic mode;
- rule/schema version;
- limitation reference;
- no production-readiness claim;
- no final-authority claim.

If health output does not disclose limitations, stop the demo and fix the contract.

### Step 3 — Load fixture analysis

Open or call:

```text
GET /sample
```

Expected response shape is defined in `docs/architecture/API_CONTRACT.md`.

The response must include:

- claims;
- evidence;
- sources;
- source dependency metadata;
- contradiction fixture;
- narrative frame or explicitly deferred/fixture-backed narrative object;
- briefing;
- audit events;
- audit verification;
- top-level limitations and `limitations_ref`.

### Step 4 — Render frontend dashboard

The frontend may consume either:

- backend-compatible static fixture: `apps/web/src/data/demo-response.json`; or
- local backend `/sample` response.

Required panels:

- `BriefingPanel`
- `ClaimMatrix`
- `EvidenceTrail`
- `AuditTrail`
- `NarrativeMap`
- `SourceSpread`
- `ContradictionBoard`

Panel requirements:

| Panel | Must show | Must not imply |
| --- | --- | --- |
| BriefingPanel | bottom line, confidence summary, limitations ref, audit ref, unresolved questions | that the system settled the dispute |
| ClaimMatrix | each claim status, confidence reason, evidence refs, audit ref | article-level truth labels |
| EvidenceTrail | relationship, source/provenance, locator, limitations, audit ref | that evidence is complete |
| AuditTrail | verification state, event refs/hashes, method trace | that audit proves the claim true |
| NarrativeMap | fixture-backed/deferred label, analysis-not-fact label | proof of intent or deception |
| SourceSpread | source dependency and independence notes | that repeated source count means corroboration |
| ContradictionBoard | conflict description/status and unresolved state | automatic resolution |

v0.4 panel status requirements:

- NarrativeMap is demo-ready only as a labeled fixture/deferred analysis panel unless richer fixture narrative data exists. It must say narrative labels are analysis, not fact, and must not infer intent, deception, or coordination.
- SourceSpread is demo-ready as fixture-backed source metadata plus dependency warnings. It must not infer ownership, funding, geography, affiliation, or independence that is absent from the fixture.
- ContradictionBoard is demo-ready as a fixture-backed conflict display. It must show unresolved/fixture status and must not claim broad semantic contradiction detection.

### Step 5 — Demonstrate claim inspection

In the claim matrix, select or inspect a contested claim.

The visible claim row/card must include:

- claim text;
- normalized claim;
- status such as `contested` or `unresolved`;
- confidence reason;
- linked evidence references;
- linked contradiction references if present;
- audit reference;
- limitations.

Invalid demo state:

- claim shown without status;
- claim shown without confidence reason;
- claim shown without evidence reference or explicit missing-evidence object;
- claim shown without audit reference;
- claim shown as a full-article verdict.

### Step 6 — Demonstrate evidence trail

Open evidence linked to the selected claim.

The evidence trail must show:

- evidence relationship: supports, contradicts, contextualizes, missing, or unclear;
- source or document reference;
- quote/excerpt or fixture summary;
- provenance/locator field;
- source dependency notes when applicable;
- limitations;
- audit reference.

The operator should say, in effect:

```text
This panel shows what the system inspected and where uncertainty remains. It does not claim complete source coverage.
```

### Step 7 — Demonstrate source dependency

Open SourceSpread or source dependency panel.

The panel must show that repeated wire/dependent sources are not counted as independent evidence streams.

Required visible language:

```text
Source quantity is not source independence. Repeated origin streams are counted separately from independent corroboration.
```

If dependency metadata is absent for a dependency scenario, the demo is incomplete.

### Step 8 — Demonstrate contradiction handling

Open ContradictionBoard.

The board must show:

- contradiction type, e.g. `time`;
- conflicting claim/evidence IDs;
- unresolved or open status;
- limitations;
- audit reference.

Required stance:

```text
Lumen exposes this conflict. It does not force resolution from incomplete fixture evidence.
```

### Step 9 — Demonstrate briefing with limitations

Open BriefingPanel.

The briefing must include:

- bottom line that preserves contested/unresolved status;
- confidence summary with reasons;
- missing information;
- unresolved questions;
- limitations reference;
- audit reference.

The briefing must not hide limitations behind polished prose.

### Step 10 — Demonstrate audit verification

Open AuditTrail or call:

```text
GET /audit/verify
```

The audit output must show:

- verification valid/invalid state;
- checked event count;
- genesis presence;
- latest event hash;
- reason.

Required explanation:

```text
The audit trail records the method path and detects inconsistent transformation history. It does not prove that a real-world claim is correct.
```

## Optional manual-text path

After the fixture demo works, `POST /analyze` may be shown with a short local text snippet.

Rules:

- treat submitted text as local input only;
- disclose placeholder extraction limitations;
- return same response envelope as `/sample`;
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

Expected behavior:

- extracted claims are labeled deterministic placeholder or fixture/manual;
- missing evidence is explicit;
- confidence remains low/unknown/unresolved unless local evidence supports more;
- briefing states limitations.

## Demo copy rules

Allowed language:

- "Lumen exposes claims, evidence, uncertainty, provenance, and audit trails."
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

1. Full dashboard with all seven panels visible or clearly navigable.
2. Briefing panel showing limitations reference and audit reference.
3. Claim matrix row showing status, confidence reason, evidence refs, and audit ref.
4. Evidence trail showing relationship/provenance/limitations.
5. Source spread showing dependency note and independent stream count.
6. Contradiction board showing unresolved fixture conflict.
7. Audit trail showing verification status and latest event hash.
8. Limitations text visible near analytical outputs.

Screenshots must not crop away uncertainty, limitations, or audit references.

## Integration gates

Before declaring demo-ready, run the implementation verification commands from the swarm task, including:

```text
python3 -m pytest apps/api/tests -q
python3 -m compileall apps/api/app
npm run verify:static --prefix apps/web
npm run typecheck --prefix apps/web
```

Repo-wide forbidden-reference and certainty-overclaim scans from the swarm task should also pass. Keep those exact grep commands in the task/audit runner rather than in this document so the architecture docs themselves do not contain forbidden strings.

For this architecture lane, the minimum doc gate is:

- `/sample` and `/analyze` schemas are documented in `API_CONTRACT.md`;
- the demo sequence documents visible limitations and audit references;
- `MVP_SCOPE.md` allows v0.3 contract/demo integration without expanding beyond local deterministic fixtures;
- no architecture doc introduces prohibited capability claims.

## Failure states that block demo readiness

Block demo readiness if any of these are true:

- frontend renders a claim without status;
- frontend renders confidence without reason;
- frontend renders a claim without evidence reference or explicit missing-evidence object;
- frontend renders a claim without audit reference;
- briefing lacks limitations reference;
- audit verification is absent from the demo;
- narrative/source/contradiction panels are unlabeled stubs;
- fixture data is presented as live analysis;
- repeated source count is presented as independent corroboration;
- copy implies certainty beyond backend data;
- hidden network, paid API, telemetry, or LLM path is required.

## Handoff notes for sibling lanes

Backend lane:

- Use `API_CONTRACT.md` as the target contract for `/sample` and `/analyze`.
- If implementation must use transitional names, tests should still enforce the display invariants: claim status, confidence reason, evidence ref, audit ref, briefing limitations ref.
- Keep fixture response deterministic.

Frontend lane:

- Static `demo-response.json` must match backend-compatible schema.
- All seven dashboard panels must be present.
- Stubbed/deferred panels must be clearly labeled.
- Do not over-polish away uncertainty.

Governance lane:

- Confirm limitations and challenge/adversarial review language remain close to outputs.
- Confirm confidence language remains methodological.
- Confirm prohibited copy does not appear.

Eval/auditor lane:

- Test both `/sample` and `/analyze` against the schema and display invariants.
- Verify no prohibited references or certainty-overclaim language appears.
- Record final verification status in the v0.3 audit report.
