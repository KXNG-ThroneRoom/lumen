# Lumen Public Release Checklist

Purpose: provide a final release packet gate for v0.5.1 public-facing material. This checklist is narrower than launch planning: it verifies the public claim story, evidence framing, uncertainty language, and auditability before anything is published.

## Release boundary

- [ ] Public material describes v0.5.1 as launch hygiene and stabilization for a controlled local demo.
- [ ] Public material says the demo centers on the fixture-backed question: "When does the regulation start?"
- [ ] Public material names the visible tabs as Story, Evidence, Why uncertain, and Audit.
- [ ] Public material does not describe Lumen as production intelligence, live truth, global coverage, broad web search, or final verification.
- [ ] Public material does not imply live ingestion, LLM calls, paid APIs, auth/accounts, telemetry, database/storage expansion, or hidden hosted services.
- [ ] Public material says confidence and audit outputs are method signals and trace checks, not truth verdicts.

## UI evidence review

- [ ] Screenshots and walkthroughs show the simplified black/white claim story, not internal legacy dashboard language.
- [ ] Conflict is shown in red, supporting evidence in blue, and uncertainty in yellow or equivalent text language.
- [ ] The main public view does not show raw hashes, raw IDs, `.md` references, underscores, provenance jargon, or dense technical dashboards.
- [ ] Technical details, if present, are behind expandable or secondary disclosure surfaces.
- [ ] The Audit tab describes traceability in plain language and does not imply external truth validation.

## Copy review blockers

Block release if public copy says or implies any current capability below:

- [ ] determines truth, proves a claim, settles a dispute, or issues a final verdict;
- [ ] monitors live events, crawls the web, or has production source coverage;
- [ ] detects deception, intent, coordination, propaganda, or neutrality as fact;
- [ ] uses hidden scoring, secret prompts, undisclosed weights, or unavailable audit rules;
- [ ] requires or silently uses credentials, external model calls, paid services, or telemetry;
- [ ] converts the controlled fixture demo into a production-readiness claim.

## Verification packet

Record exact commands and outcomes before release:

- [ ] `python3 scripts/regen_indexes.py --strict`
- [ ] `python3 scripts/regen_indexes.py`
- [ ] `python3 scripts/regen_indexes.py --check --strict`
- [ ] `bash scripts/verify_lumen.sh`
- [ ] Generated/local junk inventory completed; only unambiguous generated junk removed.
- [ ] Secret scan completed with no raw token values printed in logs or reports.
- [ ] Telemetry scan reviewed; hits are either prohibitions/docs or dependency/tooling references, not product telemetry code.
- [ ] Stale public wording scan reviewed; hits are either verifier guard strings, internal schema names, existing checklist prohibitions, or follow-up candidates.

## v0.5.2 validation closeout snapshot

- Date: 2026-05-25
- Repo: `/Users/amirtbz/lumen`
- Branch: `main`
- Commit state: uncommitted local work; no commit created by the validation lane.
- Required institutional-memory commands: pass after v0.5.1 metadata correction and v0.5.2 AAR indexing.
- Aggregate verifier: pass; 7 gates run, 0 failures, 22 API tests passed, static UI verifier passed, web typecheck passed.
- Secret scan coverage: includes release docs plus `apps/api/app`, `apps/api/tests`, and `apps/web/src`; scan output reports only redacted hit locations.
- Generated junk cleanup: validation commands recreated ignored local artifacts at `apps/api/.pytest_cache/`, `apps/api/app/__pycache__/`, `apps/api/tests/__pycache__/`, and `apps/web/tsconfig.tsbuildinfo`; they were reported, not cleaned, in the validation lane.

## Human final check

- [ ] A human reviewer can explain the current public claim in one sentence without using production, live, truth-engine, or final-verdict language.
- [ ] Any reader-facing limitation is close enough to the claim that the demo cannot reasonably be mistaken for live verification.
- [ ] The release packet links `LIMITATIONS.md`, this checklist, and the current swarm after-action report.
