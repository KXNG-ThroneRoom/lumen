---
schema_version: 1
doc_type: swarm_after_action_report
project: Lumen
phase: v0.4
sprint: demo-polish-launch-readiness
date: 2026-05-25
repo_path: /Users/amirtbz/lumen
repo_commit_before: ab467fe
repo_commit_after: ab467fe
branch: main
board: lumen-build-server
tenant: lumen-001
root_task: t_1004c661
verifier_task: t_1004c661
synthesizer_task: t_aef177db
status: pass
gate_status: pass
duration_hours: 0
files_changed_count: 39
tests_passed: 22
tests_failed: 0
blockers_resolved: 1
blockers_unresolved: 0
modules_touched:
  - verification
  - launch_checklists
  - frontend_dashboard
  - backend_api
  - institutional_memory
constitution_articles_engaged:
  - V
  - XI
  - XII
  - XIV
  - XVII
workers:
  - profile: tr-tester-reviewer
    task_id: t_1004c661
    lane: verifier
    status: done
    files_owned: []
    key_deliverable: Passed the v0.4 aggregate gate and recorded the host Python dependency caveat.
  - profile: tr-lumen-eval-auditor
    task_id: t_aef177db
    lane: verification_memory
    status: done
    files_owned:
      - scripts/verify_lumen.sh
      - docs/checklists/V0_4_VERIFICATION_CHECKLIST.md
      - docs/checklists/LAUNCH_PREP_CHECKLIST.md
      - docs/swarms/2026-05-25_lumen-v0-4-demo-polish-launch-readiness.md
      - docs/postmortems/2026-05-25_verification-environment-python-mismatch.md
      - docs/swarms/index.jsonl
      - docs/postmortems/index.jsonl
    key_deliverable: Added/verified aggregate verification scaffolding, launch checklists, and institutional memory artifacts.
supersedes: ""
related_postmortems:
  - docs/postmortems/2026-05-25_verification-environment-python-mismatch.md
related_swarms:
  - docs/swarms/2026-05-24_lumen-v0-3-contract-demo.md
tags:
  - v0.4
  - launch_readiness
  - verification
  - institutional_memory
retrieval_keywords:
  - verify_lumen
  - launch prep
  - v0.4 checklist
  - aggregate gate
  - controlled fixture demo
related_docs:
  - docs/checklists/V0_4_VERIFICATION_CHECKLIST.md
  - docs/checklists/LAUNCH_PREP_CHECKLIST.md
  - docs/architecture/V0_4_SCOPE.md
  - docs/architecture/LAUNCH_READINESS.md
  - docs/architecture/DEMO_FLOW.md
  - docs/architecture/API_CONTRACT.md
  - LIMITATIONS.md
  - evals/golden_cases.json
forensic_log: ""
index_record: docs/swarms/index.jsonl
---

## Sprint goal
Make the v0.4 controlled local demo more launch-ready by tightening verification scripts, checklists, panel honesty, and institutional memory without expanding analytical claims.

## Outcome
The v0.4 gate passed through the aggregate verifier after the repo converged on deterministic backend output, backend/frontend fixture parity, seven-panel static UI verification, TypeScript typecheck, and strict institutional-memory indexes. The new verification lane preserved the local fixture boundary, documented launch blockers, and recorded the Python environment caveat as a postmortem rather than hiding it.

## Decisions
### D1: Use an aggregate verifier as the release gate
- Decision: Treat `scripts/verify_lumen.sh` as the canonical v0.4 local gate for strict memory indexes, API pytest, API compileall, static UI verification, and web typecheck.
- Reason: A single auditable script reduces handoff ambiguity and prevents selective pass claims.
- Tradeoff: The gate depends on installed local dependencies, especially `.venv` and `apps/web/node_modules`.
- Reversibility: easy
- Article reference: XI, XII
- Evidence: `scripts/verify_lumen.sh`, `docs/checklists/V0_4_VERIFICATION_CHECKLIST.md`

### D2: Keep v0.4 as demo polish, not new intelligence capability
- Decision: Verification and launch checklists enforce controlled fixtures, visible limitations, no LLM/default network calls, no hidden scoring, and no final-truth claims.
- Reason: Launch polish increases false-authority risk unless every output keeps uncertainty and provenance visible.
- Tradeoff: The public demo remains narrower than a production analysis product.
- Reversibility: moderate
- Article reference: V, XIV, XVII
- Evidence: `LIMITATIONS.md`, `docs/architecture/DEMO_FLOW.md`, `docs/checklists/LAUNCH_PREP_CHECKLIST.md`

### D3: Record environment caveats as institutional memory
- Decision: The host Python pytest miss was documented as a low-severity postmortem instead of being lost in verifier prose.
- Reason: Future runs need to distinguish a dependency setup issue from a product regression.
- Tradeoff: Adds a small institutional-memory artifact for a non-code issue.
- Reversibility: easy
- Article reference: XI, XII
- Evidence: `docs/postmortems/2026-05-25_verification-environment-python-mismatch.md`

## Deferred intentionally
- Live ingestion, paid APIs, LLM-assisted extraction, telemetry, accounts, databases, blockchain anchoring, and production-scale source coverage remain deferred indefinitely for the controlled MVP demo.
- Runtime frontend fetching from a live backend remains optional; static fixture verification remains acceptable while the demo contract is local and deterministic.
- Dedicated secret scanning and broader dependency auditing remain future launch-hardening work; this sprint verified the local aggregate gates and overclaim boundaries.

## Blockers & resolutions
- Blocker: Bare `python3 -m pytest apps/api/tests -q` failed on the host interpreter because pytest was not installed there.
- Root cause: Dependency ownership was tied to the project `.venv`, while the direct command used a different interpreter.
- Resolution: `.venv/bin/python -m pytest apps/api/tests -q` and `bash scripts/verify_lumen.sh` passed; the environment caveat is documented in the verification checklist and postmortem.
- Prevention: Use the aggregate verifier and record the interpreter in future handoffs.

## Constitutional pressure points
- Article V was engaged because verification artifacts had to separate real pass evidence from environment caveats.
- Article XI was engaged because release readiness depends on auditable commands, indexes, and method traces.
- Article XII was engaged because deterministic local reproduction depends on the correct interpreter and fixture parity.
- Article XIV and Article XVII were engaged because launch polish can overstate capability unless limitations and MVP restraint stay close to outputs.

## Verification evidence
- `python3 scripts/regen_indexes.py --check --strict` before new artifacts -> pass, existing indexes current with 3 swarm records and 0 postmortem records.
- `.venv/bin/python -m pytest apps/api/tests -q` -> 22 passed in verifier handoff.
- `python3 -m compileall apps/api/app` -> pass in verifier handoff.
- `npm run verify:static --prefix apps/web` -> pass in verifier handoff.
- `npm run typecheck --prefix apps/web` -> pass in verifier handoff.
- `bash scripts/verify_lumen.sh` -> `RESULT PASS` in verifier handoff.
- `python3 scripts/regen_indexes.py --check --strict` after adding this AAR/postmortem -> stale indexes expected because new reports were not yet indexed.
- `python3 scripts/regen_indexes.py && python3 scripts/regen_indexes.py --check --strict` -> wrote 1 postmortem record and 4 swarm records; strict check passed.
- `bash scripts/verify_lumen.sh` after indexing -> `RESULT PASS`, 5 gates run, 0 failures, 22 API tests passed.

## Risks carried forward
- The shared working tree still contains substantial pre-existing modified and untracked work; no automatic commit, reset, clean, or discard occurred.
- The bare host `python3` lacks pytest; contributors should use `.venv` or install test dependencies into the interpreter they invoke.
- The verifier gate is local and deterministic; it does not prove production readiness, live coverage, or real-world correctness.

## Next sprint recommendation
Before public release, add a focused no-secrets/no-telemetry scan and review all README/UI launch copy against the launch checklist. Keep the next sprint bounded to local deterministic fixture demo hardening unless a separate architecture/governance decision expands scope.
