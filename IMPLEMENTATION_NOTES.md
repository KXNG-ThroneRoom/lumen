# Implementation Notes

## 2026-05-24 — Lumen v0.3 verifier remediation and swarm closeout

### Authorization

- User authorized repository writes and Kanban completion flow with `god bless`.

### Decisions

- Treated verifier blocker as documentation/schema drift, not backend/frontend runtime failure.
- Aligned `docs/architecture/API_CONTRACT.md` to the implemented Pydantic schema in `apps/api/app/models.py` rather than changing backend models late in the verification cycle.
- Preserved v0.3 scope boundaries: local deterministic fixture/local-text paths only; no live ingestion, LLM, paid API, telemetry, or final-truth claims.

### Changes

- Rewrote `docs/architecture/API_CONTRACT.md` to match implemented v0.3 Pydantic models:
  - `AnalysisResponse`
  - `AnalysisRequest`
  - `Claim`
  - `Evidence`
  - `Briefing`
  - `ConfidenceBreakdown`
  - `Source`
  - `SourceGraph`
  - `Contradiction`
  - `AuditEvent`
  - `AuditVerification`
- Removed stale contract references to top-level fields that are not implemented:
  - `analysis_id`
  - `rule_version`
  - `input_document_ids`
  - `source_dependency_edges`
  - `narrative_frames`
  - `confidence_assessments`
- Corrected documented modes to implemented values:
  - `fixture_demo`
  - `local_input`

### Verification plan

Run the full verifier suite after this edit:

- `git status --short`
- `python3 -m pytest apps/api/tests -q`
- `python3 -m compileall apps/api/app`
- `npm run verify:static --prefix apps/web`
- `npm run typecheck --prefix apps/web`
- forbidden legacy-project-name scan
- certainty-overclaim language scan

### Edge cases / risks

- `docs/architecture/API_CONTRACT.md` is a documentation artifact and is not currently enforced by automated schema-doc parity tests.
- Existing backend `FastAPI` app version/health route still report `0.2.0`; contract documents current implementation rather than forcing a runtime version bump during closeout.
- `audit_events` and `audit_trail` both expose the current ledger for compatibility; future cleanup may consolidate naming once UI/eval consumers stabilize.
- The auto-generated final synthesizer card had known bad skill `avoid-ai-writing`; it was reclaimed/blocked after crash-looping and replaced with `t_18502f05`, a no-bad-skill synthesizer card.
- Created `docs/audits/V0_3_SWARM_AGENT_SUMMARY.md` to summarize each v0.3 swarm agent's contribution.
- Replacement synthesizer `t_18502f05` completed successfully; final v0.3 swarm synthesis is done and verifier gate `t_dbf5c47a` is pass.

## 2026-05-24 — Institutional-memory AAR backfill for prior swarms

### Authorization

- User authorized repository writes for AAR generation with `god bless`.

### Decisions

- Treated the last three completed swarms as the `lumen-build-server` board lineage rooted at `t_40a9e4d1`, `t_b6cc656e`, and `t_d86ecfe5`.
- Created missing canonical AARs for the read-only readiness swarm and v0.2 deterministic-core swarm.
- Preserved the existing v0.3 canonical AAR and added a related-swarm link back to the v0.2 report rather than duplicating it.
- Created concise forensic logs for the two newly backfilled reports to preserve task graph and crash-loop recovery evidence without bloating canonical cards.

### Changes

- Added `docs/swarms/2026-05-24_lumen-v1-readiness.md`.
- Added `docs/swarms/2026-05-24_lumen-v0-2-deterministic-core.md`.
- Added `docs/forensics/swarms/2026-05-24_lumen-v1-readiness.log.md`.
- Added `docs/forensics/swarms/2026-05-24_lumen-v0-2-deterministic-core.log.md`.
- Updated `docs/swarms/2026-05-24_lumen-v0-3-contract-demo.md` with a related-swarm link to the v0.2 report.
- Regenerated `docs/swarms/index.jsonl`.

### Verification

- `python3 scripts/regen_indexes.py --strict` passed with 3 swarm records and 0 postmortem records.
- `python3 scripts/regen_indexes.py` regenerated indexes.
- `python3 scripts/regen_indexes.py --check --strict` passed with both indexes current.

### Risks / follow-up

- This task generated AARs only. Several incidents in these swarms are postmortem candidates under the universal SOP: missing `avoid-ai-writing` crash loops, v0.2 audit-chain remediation, v0.2 forbidden-reference remediation, and v0.3 schema/API contract drift.

## 2026-05-25 — v0.6 governance/docs manual input boundaries

### Authorization

- Root Kanban card `t_61343179` carried write authorization phrase `god bless` for v0.6 work.

### Decisions

- Treated v0.6 as controlled manual/local input only, not live ingestion or capability expansion into production verification.
- Framed submitted articles, excerpts, files, source labels, and URL-looking strings as assertion containers rather than facts or verified source access.
- Preserved the simplified public UI contract: Story, Evidence, Why uncertain, and Audit tabs, with visible limitations close to outputs.
- Left live ingestion, crawling, scraping, RSS, URL fetching, broad extraction, persistence, auth/accounts, telemetry, LLM calls, paid APIs, and production verification deferred.

### Commands run

- `git fetch origin && git status --short --branch && git grep -nE '<<<<<<<|=======|>>>>>>>' -- . || true`
- `git diff -- README.md LIMITATIONS.md CONSTITUTION.md docs/architecture/ROADMAP_TO_V1.md docs/architecture/DEFERRED_WORK.md docs/architecture/MVP_PHASES.md docs/demo/LOCAL_DEMO_WALKTHROUGH.md IMPLEMENTATION_NOTES.md docs/architecture/V0_6_SCOPE.md`
- `git grep -nE 'truth machine|oracle|proves|settles|production intelligence|global coverage|propaganda detection|deception proof|final verdict|final-verdict|reality determination|live intelligence|production oracle|production verification|broad source coverage' -- README.md LIMITATIONS.md CONSTITUTION.md docs/architecture/ROADMAP_TO_V1.md docs/architecture/DEFERRED_WORK.md docs/architecture/MVP_PHASES.md docs/demo/LOCAL_DEMO_WALKTHROUGH.md IMPLEMENTATION_NOTES.md || true` — matches reviewed as prohibitions, limitation disclosures, or deferred-scope language.
- `git grep -nE 'seven-component|seven component|dense dashboard|multi-panel|old dashboard|raw fingerprints|internal audit keys|source file names|machine labels' -- README.md LIMITATIONS.md docs/architecture/ROADMAP_TO_V1.md docs/architecture/DEFERRED_WORK.md docs/architecture/MVP_PHASES.md docs/demo/LOCAL_DEMO_WALKTHROUGH.md IMPLEMENTATION_NOTES.md || true` — matches reviewed as stale-UI prohibitions or “do not show” guidance.
- Final scoped `git diff -- README.md LIMITATIONS.md CONSTITUTION.md docs/architecture/ROADMAP_TO_V1.md docs/architecture/DEFERRED_WORK.md docs/architecture/MVP_PHASES.md docs/demo/LOCAL_DEMO_WALKTHROUGH.md IMPLEMENTATION_NOTES.md` reviewed for scope.

### Risks / edge cases

- `docs/demo/LOCAL_DEMO_WALKTHROUGH.md` had pre-existing v0.6 UI-alignment edits before this lane; this pass preserved and extended them instead of reverting.
- `docs/architecture/V0_6_SCOPE.md` already existed as an untracked scope file before this lane and was used as context, not modified here.

## 2026-05-25 — v0.6 frontend controlled manual input affordance

### Authorization

- Root Kanban card `t_61343179` carried write authorization phrase `god bless` for v0.6 work.

### Decisions

- Added a controlled local textarea affordance inside the simplified public page instead of adding live ingestion or a backend submit path.
- Labeled pasted text as a local assertion container and not a verified fact; staged text does not change the fixture answer or the four-tab claim story.
- Kept the public UI in the Story, Evidence, Why uncertain, and Audit model with black/white base and yellow uncertainty styling for manual/local input.

### Changes

- Updated `apps/web/src/app/page.tsx` with local-only manual assertion state, preview copy, character-limited input, hidden pasted-text summary, and no network/submission behavior.
- Added manual input styling in `apps/web/src/app/globals.css` using the existing uncertainty color tokens.
- Extended `apps/web/scripts/verify-static-ui.mjs` to require manual-input boundary copy in the public page.
- Updated `apps/web/README.md` so the frontend contract names the manual affordance and no-submit boundary.

### Commands run

- `git fetch origin && git status --short --branch && git grep -nE '<<<<<<<|=======|>>>>>>>' -- . ':!node_modules'`
- `npm run verify:static --prefix apps/web` (expected RED before implementation: missing `Manual input area`)
- `npm run verify:static --prefix apps/web && npm run typecheck --prefix apps/web` (passed)
- Independent review found the first preview echoed pasted text; remediated by hiding the pasted text in the preview and adding `maxLength={1200}`.
- `npm run verify:static --prefix apps/web && npm run typecheck --prefix apps/web` (rerun after remediation, passed)

### Risks / edge cases

- `docs/demo/LOCAL_DEMO_WALKTHROUGH.md` still says the public UI should not add a manual-input workflow to the demo page; this lane avoided editing broad docs outside the owned area, but the root v0.6 task objective now supersedes that older walkthrough sentence and should be reconciled by the docs/release lane.
