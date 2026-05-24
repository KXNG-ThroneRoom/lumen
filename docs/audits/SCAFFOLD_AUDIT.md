# Lumen Scaffold Audit Notes

This file records scaffold-worker decisions, verification, limitations, and handoffs for the first local Lumen scaffold. It is not a production certification.

## Architecture / root scaffold handoff

Changed domain:
- `README.md`
- `LICENSE`
- `.gitignore`
- `docker-compose.yml`
- `docs/architecture/SYSTEM_OVERVIEW.md`
- `docs/architecture/MVP_SCOPE.md`
- `docs/architecture/DATA_MODEL.md`
- `packages/governance/README.md`
- `packages/scoring/README.md`
- `packages/audit_ledger/README.md`
- `packages/claim_extractor/README.md`
- `packages/ingestors/README.md`
- `packages/source_graph/README.md`
- `packages/briefing/README.md`

Decisions:
- MVP is deterministic and local-first over sample JSON.
- Claims are the unit of analysis.
- Raw evidence is immutable; changed source material becomes a new version.
- Confidence is explainable with visible reasons, caps, boosts, penalties, and uncertainty notes.
- Audit ledger is a local append-only hash-chain design primitive, not a blockchain implementation.
- Narrative analysis is labeled as analysis, not fact.
- Future model-assisted stages must expose model version, prompt hash, rule version, and limitations.

Verification notes:
- Owned architecture/package files were reported present by the architecture worker.
- Common key/secret pattern scan reported no matches in authored/repo scan.
- Docker CLI was unavailable on this host, so compose runtime validation was limited to file shape.

Limitations:
- Backend, frontend, governance, examples, evals, and inventory remain separate worker domains.
- Compose dev services require backend and frontend scaffolds before end-to-end local run.

## Examples / evals handoff

Changed domain:
- `examples/sample_article.json`
- `examples/sample_claim_matrix.json`
- `examples/sample_audit_trail.json`
- `examples/sample_briefing.json`
- `evals/README.md`
- `evals/eval_plan.md`
- `evals/golden_cases.json`

Decisions:
- Example fixture is a synthetic city water advisory and makes no real-world factual claim.
- Golden cases cover source dependency, anonymous-source caps, contradictions, stale media, missing context, and visible uncertainty.
- Static sample audit hashes are explicit placeholders until the backend audit primitive computes canonical SHA-256 hashes.

Verification notes:
- Example/eval JSON parsed with Python stdlib.
- Owned examples/evals were scanned for project rename/reference drift and credential-like material; no owned-file issues were reported.

Limitations:
- No eval runner implemented in this scaffold task; `evals/eval_plan.md` defines the future deterministic runner contract.

## Backend handoff

Status:
- Backend worker blocked before writes due profile-level implementation authorization policy.

Observed next step:
- Create the FastAPI scaffold, deterministic audit ledger primitive, scoring primitive, claim extraction placeholder, and pytest tests when unblocked.

Impact:
- `apps/api/**` should be treated as missing until a backend worker completes it.

## Frontend worker handoff — t_5ab4e3c2

Changed domain:
- `apps/web/README.md`
- `apps/web/package.json`
- `apps/web/package-lock.json`
- `apps/web/next.config.mjs`
- `apps/web/next-env.d.ts`
- `apps/web/tsconfig.json`
- `apps/web/scripts/verify-static-ui.mjs`
- `apps/web/src/app/layout.tsx`
- `apps/web/src/app/page.tsx`
- `apps/web/src/app/globals.css`
- `apps/web/src/components/BriefingPanel.tsx`
- `apps/web/src/components/ClaimMatrix.tsx`
- `apps/web/src/components/EvidenceTrail.tsx`
- `apps/web/src/components/NarrativeMap.tsx`
- `apps/web/src/components/ContradictionBoard.tsx`
- `apps/web/src/components/AuditTrail.tsx`
- `apps/web/src/data/lumenSample.ts` (adapter over canonical `examples/*.json` fixtures)

Decisions:
- Implemented the Lumen web scaffold as a static Next.js App Router dashboard driven by canonical local `examples/*.json` fixtures through a TypeScript adapter.
- Added six visible panels: BriefingPanel, ClaimMatrix, EvidenceTrail, NarrativeMap, ContradictionBoard, and AuditTrail.
- Used a dark, raw intelligence-dashboard aesthetic with monospace method labels and visible uncertainty language rather than glossy SaaS styling.
- Kept the UI honest: no live ingestion, no final truth claims, no hidden scoring, no paid API dependency, and telemetry disabled in npm scripts.
- Added a `postcss` override to keep `npm audit --audit-level=moderate` clean with the current Next dependency chain.
- Added `*.tsbuildinfo` to `.gitignore` because `tsc --noEmit` creates an incremental build artifact.

Verification:
- `cd apps/web && npm run verify:static` passed.
- `cd apps/web && npm run typecheck` passed.
- `cd apps/web && npm run build` passed.
- `cd apps/web && npm audit --audit-level=moderate` passed with 0 vulnerabilities.
- Frontend-owned file scan found no API-key/secret/token/private-key/password pattern matches.

Risks / TODOs:
- No browser-level visual regression test is present yet.
- Next.js root is pinned in `next.config.mjs` to the repository root so the frontend can import canonical local `examples/*.json` fixtures without parent-lockfile inference warnings.

## Open scaffold risks

- Backend remains blocked/missing until the backend task is unblocked and completed.
- Governance files beyond the architecture worker's scope may still need independent verification.
- `docs/audits/scaffold_inventory.json` still needs final inventory generation by the auditor/synthesizer lane.

## Phase 3 eval/auditor lane handoff — t_a35b2e6f

Changed domain:
- `apps/api/tests/test_audit.py`
- `apps/api/tests/test_scoring.py`
- `apps/api/tests/test_source_graph.py`
- `apps/api/tests/test_contradiction.py`
- `apps/api/tests/test_briefing.py`
- `apps/api/tests/test_claim_extraction.py`
- `evals/README.md`
- `evals/eval_plan.md`
- `evals/golden_cases.json`
- `docs/audits/scaffold_inventory.json`
- `docs/audits/SCAFFOLD_AUDIT.md`

Decisions:
- Added pytest coverage for the Phase 3 eval requirements: genesis event, audit chain integrity, tamper detection, anonymous-source cap, primary-evidence boost, unknown/unresolved handling, source dependency warning, fixture contradiction behavior, placeholder extractor honesty, briefing limitations/audit reference, and mandatory claim status/confidence reasons.
- Updated golden cases to schema `lumen.evals.golden_cases.v2`, adding explicit briefing/audit visibility coverage and placeholder-extractor limitation requirements.
- Generated `docs/audits/scaffold_inventory.json` with a non-generated file inventory, SHA-256 hashes, git status snapshot, owned-file list, excluded generated/dependency directories, and local secret-pattern scan results.
- After backend handoff recovery, reran the full backend/eval verification and confirmed the prior audit-chain blocker is fixed.

Verification:
- `git fetch origin` attempted first in the initial run; repository has no usable `origin` remote.
- `git status --short` shows the repository contents are still untracked rather than baseline-committed.
- `git grep -nE '<<<<<<<|=======|>>>>>>>'` reported no conflict markers.
- `python3 -m pip install --user 'pydantic>=2.7,<3.0' 'fastapi>=0.111,<1.0' 'uvicorn[standard]>=0.30,<1.0' 'pytest>=8.0,<9.0'` installed local test/runtime dependencies for this profile environment during the initial run.
- `python3 -m pytest apps/api/tests -q` now reports `11 passed`.
- `python3 -m compileall apps/api/app` passed.
- `find . -maxdepth 4 -type f | sort` was rerun for inventory visibility; generated/dependency artifacts are present and excluded from the JSON inventory.
- Required forbidden-reference scan was rerun after rewording the legacy architecture acceptance criterion and now reports no hits.
- Required certainty-claim scan reports no hits.
- Local generated/dependency-aware secret scan in `scaffold_inventory.json` reports `0` hits.

Resolved blocker:
- `apps/api/tests/test_audit.py::test_audit_chain_integrity_verifies_for_appended_events` now passes after the backend audit hash canonicalization fix.
- Audit chain verification passes for genesis, appended events, and tamper detection in the eval test suite.

Additional scan findings:
- The banned-project-name/reference scan is clean after rewording the legacy architecture acceptance criterion.
- The certainty-claim scan is clean on the required pattern set.
- The prior forbidden-reference finding is resolved and no longer blocks verifier/synthesizer handoff.

Risks / TODOs:
- Generated pytest/cache/build artifacts appeared during local verification; they are excluded from inventory and should be cleaned before a baseline commit if the owning/synthesizer lane chooses to do repo hygiene.
- Repo is not ready for baseline commit until the untracked scaffold is reviewed and intentionally added.


## Verifier remediation — forbidden-reference cleanup

Changed domain:
- `docs/architecture/PROJECT_BLUEPRINT.md`
- `docs/audits/SCAFFOLD_AUDIT.md`
- `docs/audits/scaffold_inventory.json`

Decision:
- Reworded the legacy named-project acceptance criterion to `no legacy project references` so the required forbidden-reference scan can enforce repository hygiene without embedding banned terms in source documents.

Verification:
- Required forbidden-reference scan now reports no hits for the banned legacy-name patterns in non-generated source files.
- The scaffold inventory was updated to mark the forbidden-reference scan as passing and to move the prior reference-scan blocker into resolved blockers.

Risk / TODO:
- The project remains untracked/no baseline commit; review generated and source files before first commit.
