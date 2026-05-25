---
schema_version: 1
doc_type: swarm_after_action_report
project: Lumen
phase: v0.3
sprint: contract-demo-integration
date: 2026-05-24
repo_path: /Users/amirtbz/lumen
repo_commit_before: uncommitted-local-before-v0.3-swarm
repo_commit_after: uncommitted-local-after-v0.3-swarm
branch: main
board: lumen-build-server
tenant: local
root_task: t_d86ecfe5
verifier_task: t_dbf5c47a
synthesizer_task: t_18502f05
status: pass
gate_status: pass
duration_hours: 0
files_changed_count: 28
tests_passed: 17
tests_failed: 0
blockers_resolved: 3
blockers_unresolved: 0
modules_touched:
  - api_contract
  - demo_flow
  - backend_api
  - frontend_dashboard
  - governance_docs
  - evals
  - audit_docs
constitution_articles_engaged:
  - V
  - XX
  - XXI
  - XXIV
  - XXV
workers:
  - profile: default
    task_id: t_d86ecfe5
    lane: root_planning
    status: done
    files_owned: []
    key_deliverable: Planned the v0.3 contract and demo integration swarm.
  - profile: tr-lumen-architect
    task_id: t_cc74277b
    lane: architecture
    status: done
    files_owned:
      - docs/architecture/API_CONTRACT.md
      - docs/architecture/DEMO_FLOW.md
      - docs/architecture/MVP_SCOPE.md
    key_deliverable: Defined the local v0.3 API contract and demo scope.
  - profile: tr-lumen-governance
    task_id: t_f060f3b7
    lane: governance
    status: done
    files_owned:
      - LIMITATIONS.md
      - ADVERSARIAL_REVIEW.md
      - docs/governance/CONFIDENCE_SCORING.md
      - docs/governance/GOVERNANCE_RULES.md
    key_deliverable: Preserved limitations, uncertainty, and anti-oracle language.
  - profile: tr-lumen-backend
    task_id: t_1817363a
    lane: backend
    status: done
    files_owned:
      - apps/api/app/main.py
      - apps/api/app/models.py
      - apps/api/app/demo_fixtures.py
      - apps/api/tests/test_api_contract.py
      - apps/api/tests/test_demo_flow.py
    key_deliverable: Implemented deterministic fixture-backed v0.3 API responses.
  - profile: tr-lumen-frontend
    task_id: t_dc48671a
    lane: frontend
    status: done
    files_owned:
      - apps/web/src/app/page.tsx
      - apps/web/src/data/demo-response.json
      - apps/web/src/lib/api-contract.ts
      - apps/web/src/components/BriefingPanel.tsx
      - apps/web/src/components/ClaimMatrix.tsx
      - apps/web/src/components/EvidenceTrail.tsx
      - apps/web/src/components/AuditTrail.tsx
      - apps/web/src/components/NarrativeMap.tsx
      - apps/web/src/components/SourceSpread.tsx
      - apps/web/src/components/ContradictionBoard.tsx
    key_deliverable: Rendered all seven dashboard panels from the v0.3 demo contract.
  - profile: tr-lumen-eval-auditor
    task_id: t_dab060a2
    lane: eval_audit
    status: done
    files_owned:
      - apps/api/tests/test_api_contract.py
      - apps/api/tests/test_demo_flow.py
      - evals/golden_cases.json
      - docs/audits/V0_3_AUDIT.md
      - docs/audits/scaffold_inventory.json
    key_deliverable: Added contract/demo tests, golden cases, and audit report.
  - profile: tr-tester-reviewer
    task_id: t_dbf5c47a
    lane: verifier
    status: done
    files_owned: []
    key_deliverable: Blocked twice, then passed the final verification gate.
  - profile: tr-orchestrator
    task_id: t_b77301d6
    lane: synthesizer
    status: blocked
    files_owned: []
    key_deliverable: Blocked by unavailable task-level skill avoid-ai-writing.
  - profile: tr-orchestrator
    task_id: t_18502f05
    lane: synthesizer_replacement
    status: done
    files_owned:
      - docs/audits/V0_3_SWARM_AGENT_SUMMARY.md
    key_deliverable: Produced the operational swarm summary used as forensic evidence.
supersedes: ""
related_postmortems: []
related_swarms: []
tags:
  - v0.3
  - contract_demo
  - fixture_backed
  - verifier_gate
retrieval_keywords:
  - API_CONTRACT
  - demo-response
  - fixture_demo
  - local_input
  - schema_parity
  - verifier_gate
  - anti_oracle
related_docs:
  - docs/audits/V0_3_AUDIT.md
  - docs/audits/V0_3_SWARM_AGENT_SUMMARY.md
  - docs/architecture/API_CONTRACT.md
  - docs/architecture/DEMO_FLOW.md
  - docs/architecture/MVP_SCOPE.md
  - evals/golden_cases.json
forensic_log: docs/forensics/swarms/2026-05-24_lumen-v0-3-contract-demo.log.md
index_record: docs/swarms/index.jsonl
---

## Sprint goal
Stabilize a local deterministic v0.3 demo flow with aligned backend, frontend, audit, eval, and governance artifacts.

## Outcome
The swarm passed the verifier gate after two operator remediations: frontend static demo/types were aligned to the backend `AnalysisResponse` schema, and `docs/architecture/API_CONTRACT.md` was rewritten to match the implemented v0.3 Pydantic models. The result is a fixture-backed local demo contract with seven frontend panels, backend contract/demo tests, golden cases, and explicit limitations; no commit was made during the swarm.

## Decisions
### D1: Keep v0.3 local and fixture-backed
- Decision: Bound the sprint to deterministic fixtures and local input responses instead of live ingestion, paid APIs, LLM calls, or real-time geopolitical analysis.
- Reason: The demo needed to show methods, provenance, uncertainty, and audit surfaces without implying production intelligence capability.
- Tradeoff: The system remained a controlled demo rather than a live analysis product.
- Reversibility: moderate
- Article reference: XXIV, XXV
- Evidence: `docs/architecture/DEMO_FLOW.md`, `LIMITATIONS.md`, `docs/audits/V0_3_AUDIT.md`

### D2: Treat backend schema as the source of truth for frontend parity
- Decision: Regenerate/update frontend demo data and TypeScript contract fields from the implemented backend v0.3 response shape.
- Reason: The verifier found missing top-level and nested fields in `apps/web/src/data/demo-response.json` and `apps/web/src/lib/api-contract.ts`.
- Tradeoff: Frontend static data became tightly coupled to the backend fixture contract.
- Reversibility: easy
- Article reference: XX, XXI
- Evidence: `apps/api/app/models.py`, `apps/web/src/data/demo-response.json`, `apps/web/src/lib/api-contract.ts`

### D3: Rewrite API contract docs to match implementation
- Decision: Replace stale `docs/architecture/API_CONTRACT.md` content with the actual v0.3 Pydantic model fields and modes.
- Reason: The verifier found architecture documentation drift from implemented schema.
- Tradeoff: Earlier aspirational fields were removed from the v0.3 contract surface.
- Reversibility: easy
- Article reference: V, XX, XXI
- Evidence: `docs/architecture/API_CONTRACT.md`, verifier task `t_dbf5c47a`

### D4: Replace the crash-looping synthesizer
- Decision: Block obsolete synthesizer task `t_b77301d6` and create replacement task `t_18502f05` without the unavailable task-level skill.
- Reason: The original card repeatedly failed on missing skill `avoid-ai-writing`.
- Tradeoff: Final synthesis depended on a replacement task instead of the original synthesizer card.
- Reversibility: easy
- Article reference: XX
- Evidence: `docs/forensics/swarms/2026-05-24_lumen-v0-3-contract-demo.log.md`

## Deferred intentionally
- Live ingestion, paid APIs, LLM calls, and real-time geopolitical analysis were deferred to preserve the controlled local v0.3 scope; revisit only after governance and audit surfaces are stronger.
- HTTP-level contract tests were deferred to avoid adding a new dependency during this scaffold gate; revisit when dependency policy allows.
- Dedicated secret/dependency/security scanning was deferred beyond grep-based checks; revisit before public release.
- Local runtime API fetch from the frontend was deferred in favor of static fixture fallback; revisit in the next demo-flow sprint.

## Blockers & resolutions
- Blocker: Frontend static demo/types did not match backend v0.3 `AnalysisResponse`.
- Root cause: Schema changes landed in backend models without the static frontend contract being regenerated from the same source.
- Resolution: Operator regenerated/updated `apps/web/src/data/demo-response.json`, updated `apps/web/src/lib/api-contract.ts`, and strengthened `apps/web/scripts/verify-static-ui.mjs`.
- Prevention: Add automated schema-doc/static-contract parity checks in a later sprint.

- Blocker: `docs/architecture/API_CONTRACT.md` drifted from implemented Pydantic models.
- Root cause: Architecture documentation described stale and aspirational fields after implementation converged elsewhere.
- Resolution: Operator rewrote `docs/architecture/API_CONTRACT.md` to match the v0.3 schema.
- Prevention: Add schema-doc parity verification.

- Blocker: Original synthesizer task crash-looped on unavailable skill `avoid-ai-writing`.
- Root cause: Task-level runtime profile referenced a missing skill.
- Resolution: Obsolete card was reclaimed and blocked; replacement synthesizer `t_18502f05` was created without the bad skill.
- Prevention: Validate task-level skill availability before dispatch.

## Constitutional pressure points
- Article XXV was engaged because a polished local demo could be mistaken for live or authoritative analysis; limitations and fixture-backed labels were preserved.
- Articles XX and XXI were engaged by schema drift between backend, frontend, tests, and architecture docs; verifier remediation restored traceable contract alignment.
- Article V was engaged by the need to document what passed, what remained local-only, and what was deferred.

## Verification evidence
- `python3 -m pytest apps/api/tests -q` -> 17 passed
- `python3 -m compileall apps/api/app` -> pass
- `npm run verify:static --prefix apps/web` -> pass
- `npm run typecheck --prefix apps/web` -> pass
- `forbidden legacy-project-name scan` -> clean
- `certainty-overclaim scan` -> clean
- `Pydantic demo parity spot check` -> pass
- `API contract model-field spot check` -> pass
- `git diff --check` -> pass

## Risks carried forward
- `docs/audits/scaffold_inventory.json` is a point-in-time inventory and should be regenerated after later edits.
- Secret/dependency checking was grep-based, not a dedicated scanner.
- Contract tests call route functions directly rather than HTTP TestClient to avoid adding dependency footprint.
- The frontend still uses static fixture data rather than a runtime API fetch path.

## Next sprint recommendation
Add automated contract parity checks so backend models, frontend static demo data, TypeScript contract types, and `docs/architecture/API_CONTRACT.md` cannot drift silently. Keep the same doctrine: deterministic/local-first by default, no oracle language, no hidden network calls, no paid API use, and no LLM default path.
