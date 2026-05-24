# Lumen Evals

This directory contains deterministic evaluation scaffolding for Lumen's MVP methods.

The evals test process quality, not whether Lumen has discovered final truth. A passing implementation must preserve uncertainty, expose confidence reasons, flag source dependency, and write auditable transformation records.

Files:
- `golden_cases.json` — canonical edge cases the MVP should satisfy.
- `eval_plan.md` — evaluation goals, invariants, suggested checks, and non-goals.

Test-backed MVP invariants:
- Audit ledger starts with a genesis event and detects tampering.
- Claim objects are invalid without status and visible confidence reasons.
- Anonymous-source claims are capped and the cap is user-visible.
- Primary evidence can raise confidence but never becomes automatic truth.
- Source repetition through a shared wire/citation dependency is not independence.
- Contradiction detection is fixture-based until a real semantic method exists.
- Placeholder extraction must disclose its limitations and avoid production-grade claims.
- Briefings must include limitations and audit event references.

Principles:
- Methods over conclusions.
- Claim-level evaluation, not article-level verdicts.
- Visible evidence trail for every confidence judgment.
- No hidden scoring or ideological weighting.
- Unknown/unresolved/contested statuses are valid outcomes.
- Deterministic local fixtures first; no paid APIs required.
