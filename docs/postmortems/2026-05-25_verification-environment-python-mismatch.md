---
schema_version: 1
doc_type: implementation_postmortem
project: Lumen
phase: v0.4
sprint: demo-polish-launch-readiness
date: 2026-05-25
detected_at: 2026-05-25
introduced_at: unknown
resolved_at: 2026-05-25
detection_method: verifier
repo_path: /Users/amirtbz/lumen
repo_commit_before: ab467fe
repo_commit_after: ab467fe
branch: main
status: resolved
severity: low
prevention_status: verified
failure_classes:
  - dependency_issue
  - documentation_gap
affected_modules:
  - verification
affected_files:
  - scripts/verify_lumen.sh
  - docs/checklists/V0_4_VERIFICATION_CHECKLIST.md
related_tasks:
  - t_1004c661
  - t_aef177db
related_swarms:
  - docs/swarms/2026-05-25_lumen-v0-4-demo-polish-launch-readiness.md
related_postmortems: []
constitution_articles_at_risk:
  - XI
  - XII
supersedes: ""
tags:
  - v0.4
  - verification
  - dependency_environment
retrieval_keywords:
  - verify_lumen
  - python3 pytest
  - .venv
  - aggregate gate
related_docs:
  - docs/checklists/V0_4_VERIFICATION_CHECKLIST.md
  - docs/checklists/LAUNCH_PREP_CHECKLIST.md
  - scripts/verify_lumen.sh
forensic_log: ""
index_record: docs/postmortems/index.jsonl
---

## Summary
The final v0.4 verifier observed that bare `python3 -m pytest apps/api/tests -q` failed on this host because the Homebrew Python lacked pytest, while the project `.venv` path and aggregate verifier passed. The incident did not invalidate the demo gate, but it exposed an environment ambiguity that could make future verification look falsely broken.

## Symptom
`python3 -m pytest apps/api/tests -q` returned `No module named pytest` under the host Python, while `.venv/bin/python -m pytest apps/api/tests -q` returned 22 passing tests and `bash scripts/verify_lumen.sh` returned `RESULT PASS`.

## Root cause
The repository verification docs included the bare `python3` pytest command as a target, but the shared workstation did not have the test dependencies installed in that interpreter. The aggregate verifier correctly prefers `.venv/bin/python` when present, but the checklist needed to state that expectation clearly.

## Causal chain
Bare host Python lacked pytest -> direct pytest command failed before test collection -> verifier had to use `.venv/bin/python` and the aggregate script to establish the actual project gate.

## Fix
No runtime source code changed in this postmortem. The v0.4 verification artifacts document `.venv` as the preferred path, and `scripts/verify_lumen.sh` selects `.venv/bin/python` when available before falling back to `python3`.

## Prevention
Prevention status: verified. Future verifier handoffs should run `scripts/verify_lumen.sh` from the repo root and record whether `.venv` was used; the checklist now treats missing dependencies as an environment setup issue rather than a silent product failure.

## What we learned
Verification commands must identify the interpreter that owns the installed dependencies. A passing aggregate gate is more reproducible than a bare interpreter command whose dependency state varies by host.
