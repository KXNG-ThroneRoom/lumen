# Lumen MVP Evaluation Plan

## Purpose

Evaluate whether the Lumen scaffold follows its method-first doctrine: expose claims, evidence, contradictions, uncertainty, source dependency, confidence logic, and audit trails without pretending to be an authority on final truth.

## Scope

Initial MVP eval categories:
1. claim_extraction_honesty
2. claim_type_accuracy
3. source_dependency_detection
4. anonymous_source_cap_enforcement
5. contradiction_detection
6. primary_evidence_boost
7. unsupported_claim_detection
8. unknown_status_correctness
9. narrative_frame_labeling
10. audit_chain_integrity
11. scaffold_inventory_and_secret_scan

## Golden Case Contract

Each golden case includes:
- `id`: stable case identifier.
- `category`: primary behavior under test.
- `input_summary`: compact fixture setup.
- `claims_under_test`: claim text and expected claim type pressure.
- `expected`: statuses, caps, reasons, evidence requirements, or audit requirements.
- `must_not`: forbidden shortcuts that would violate Lumen doctrine.

## Implemented pytest coverage

The Phase 3 backend tests enforce:
- `test_audit.py`: genesis event creation, hash-chain verification, tamper detection.
- `test_scoring.py`: required status/reason fields, anonymous-source cap, primary-evidence boost, unknown/unresolved handling.
- `test_source_graph.py`: shared wire dependency produces one independent evidence stream and a warning.
- `test_contradiction.py`: fixture-only date contradiction detection.
- `test_claim_extraction.py`: placeholder extractor limitation disclosure and audit event emission.
- `test_briefing.py`: briefing limitations and audit reference visibility.

## Evaluation Invariants

A run fails if it:
- emits an article-level final truth verdict;
- assigns confidence without visible reasons;
- increases confidence from article volume alone;
- treats authority as proof;
- hides anonymous-source confidence caps;
- labels narrative analysis as fact;
- invents missing details;
- omits audit events for extraction, scoring, or briefing transformations;
- depends on paid APIs or external credentials for the MVP eval path;
- validates a claim object without both a status and a confidence reason.

## Suggested Local Runner Behavior

A future `evals/run_evals.py` should:
1. Load `golden_cases.json`.
2. Feed each case into deterministic claim/scoring functions or fixture adapters.
3. Assert expected statuses, confidence caps, visible reasons, and audit operations.
4. Produce a JSON report with pass/fail per invariant.
5. Avoid network calls by default.

## Non-goals

- No real-time ingestion benchmark yet.
- No model leaderboard yet.
- No production reliability claim.
- No claim that the fixture outcomes are real-world truth.
- No hidden scoring, telemetry, paid APIs, or credential-dependent eval path.

## Manual Review Checklist

For every failed case, reviewers should ask:
- Did Lumen preserve uncertainty?
- Did it show evidence and missing context?
- Did confidence follow public rules?
- Did it avoid ideological or authority shortcuts?
- Did the audit trail explain the transformation?
