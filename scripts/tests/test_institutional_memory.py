from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import new_report  # noqa: E402
import regen_indexes  # noqa: E402


def setup_memory_tree(root: Path) -> None:
    for folder in (
        "docs/swarms",
        "docs/postmortems",
        "docs/forensics/swarms",
        "docs/forensics/postmortems",
    ):
        (root / folder).mkdir(parents=True, exist_ok=True)
    (root / "docs/swarms/index.jsonl").write_text("", encoding="utf-8")
    (root / "docs/postmortems/index.jsonl").write_text("", encoding="utf-8")


def valid_swarm_card(
    *,
    status: str = "pass",
    gate_status: str = "pass",
    forensic_log: str = "docs/forensics/swarms/valid.log.md",
    body: str | None = None,
) -> str:
    body = body or """
## Sprint goal
Exercise the institutional memory enforcement path.

## Outcome
The card contains enough evidence to be indexed.

## Decisions
### D1: Keep the validator strict
- Decision: Reject invalid canonical cards before indexing.
- Reason: Invalid memory records create false legitimacy.
- Tradeoff: Draft cards cannot be indexed until complete.
- Reversibility: easy
- Evidence: `scripts/regen_indexes.py`

## Deferred intentionally
- Nothing was deferred; revisit indefinite.

## Verification evidence
- `python3 scripts/regen_indexes.py --check --strict` -> pass

## Risks carried forward
- No carried risk from this fixture.

## Next sprint recommendation
Keep validator tests close to the scripts they protect.
"""
    return f"""---
schema_version: 1
doc_type: swarm_after_action_report
project: Lumen
phase: v-test
sprint: memory-enforcement
date: 2026-05-24
repo_path: /tmp/lumen
repo_commit_before: fixture-before
repo_commit_after: fixture-after
branch: test
board: memory-board
tenant: local
root_task: t_root
verifier_task: t_verify
synthesizer_task: t_synth
status: {status}
gate_status: {gate_status}
duration_hours: 1
files_changed_count: 1
tests_passed: 1
tests_failed: 0
blockers_resolved: 0
blockers_unresolved: 0
modules_touched:
  - institutional_memory
constitution_articles_engaged:
  - XXV
workers:
  - profile: tester
    task_id: t_worker
    lane: validation
    status: done
    files_owned: []
    key_deliverable: Validated the memory card.
supersedes: ""
related_postmortems: []
related_swarms: []
tags:
  - fixture
retrieval_keywords:
  - memory
related_docs:
  - scripts/regen_indexes.py
forensic_log: {forensic_log}
index_record: docs/swarms/index.jsonl
---
{body}"""


def valid_postmortem_card(
    *,
    status: str = "resolved",
    prevention_status: str = "implemented",
    body: str | None = None,
) -> str:
    body = body or """
## Summary
The indexer previously allowed invalid records to be emitted.

## Symptom
An invalid canonical card could appear in the queryable index.

## Root cause
Validation errors were collected after records were already prepared for emission.

## Causal chain
- Invalid card entered canonical folder.
- Validator collected errors.
- Old writer could still update indexes outside strict mode.

## Fix
Changed `scripts/regen_indexes.py` to validate before writing.

## Prevention
Added `scripts/tests/test_institutional_memory.py` coverage for invalid writes.

## What we learned
Institutional memory needs enforcement at the index boundary.
"""
    return f"""---
schema_version: 1
doc_type: implementation_postmortem
project: Lumen
phase: v-test
sprint: memory-enforcement
date: 2026-05-24
detected_at: 2026-05-24
introduced_at: unknown
resolved_at: 2026-05-24
detection_method: test
repo_path: /tmp/lumen
repo_commit_before: fixture-before
repo_commit_after: fixture-after
branch: test
status: {status}
severity: high
prevention_status: {prevention_status}
failure_classes:
  - documentation_gap
affected_modules:
  - institutional_memory
affected_files:
  - scripts/regen_indexes.py
related_tasks: []
related_swarms: []
related_postmortems: []
constitution_articles_at_risk:
  - XXV
supersedes: ""
tags:
  - fixture
retrieval_keywords:
  - memory
related_docs:
  - scripts/regen_indexes.py
forensic_log: ""
index_record: docs/postmortems/index.jsonl
---
{body}"""


def write_valid_swarm(root: Path, **kwargs: object) -> Path:
    setup_memory_tree(root)
    (root / "docs/forensics/swarms/valid.log.md").write_text(
        "raw verifier fixture\n", encoding="utf-8"
    )
    path = root / "docs/swarms/2026-05-24_valid.md"
    path.write_text(valid_swarm_card(**kwargs), encoding="utf-8")
    return path


def write_valid_postmortem(root: Path, **kwargs: object) -> Path:
    setup_memory_tree(root)
    path = root / "docs/postmortems/2026-05-24_valid.md"
    path.write_text(valid_postmortem_card(**kwargs), encoding="utf-8")
    return path


def test_valid_swarm_card_indexes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    write_valid_swarm(tmp_path)
    monkeypatch.setattr(regen_indexes, "REPO_ROOT", tmp_path)

    records, errors = regen_indexes.collect(
        tmp_path / "docs/swarms", "swarm_after_action_report"
    )

    assert errors == []
    assert len(records) == 1
    assert records[0]["status"] == "pass"


def test_placeholder_pass_card_rejected(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    body = """
## Sprint goal
<one sentence>

## Outcome
TODO

## Decisions
### D1: Placeholder
- Decision: TBD
- Reason: TBD
- Tradeoff: TBD
- Reversibility: easy
- Evidence: TBD

## Deferred intentionally
TBD

## Verification evidence
- `<command>` -> pass

## Risks carried forward
TBD

## Next sprint recommendation
TBD
"""
    write_valid_swarm(tmp_path, body=body)
    monkeypatch.setattr(regen_indexes, "REPO_ROOT", tmp_path)

    records, errors = regen_indexes.collect(
        tmp_path / "docs/swarms", "swarm_after_action_report"
    )

    assert records == []
    assert any("placeholder" in err for err in errors)


def test_invalid_enum_rejected(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    write_valid_swarm(tmp_path, status="green")
    monkeypatch.setattr(regen_indexes, "REPO_ROOT", tmp_path)

    records, errors = regen_indexes.collect(
        tmp_path / "docs/swarms", "swarm_after_action_report"
    )

    assert records == []
    assert any("status `green`" in err for err in errors)


def test_stale_index_detected_by_check(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    write_valid_swarm(tmp_path)
    monkeypatch.setattr(regen_indexes, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(sys, "argv", ["regen_indexes.py", "--check"])

    assert regen_indexes.main() == 2


def test_strict_does_not_mutate_indexes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    write_valid_swarm(tmp_path)
    stale_index = tmp_path / "docs/swarms/index.jsonl"
    stale_index.write_text("stale\n", encoding="utf-8")
    monkeypatch.setattr(regen_indexes, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(sys, "argv", ["regen_indexes.py", "--strict"])

    assert regen_indexes.main() == 0
    assert stale_index.read_text(encoding="utf-8") == "stale\n"


def test_scaffold_output_does_not_default_to_pass(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(new_report, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "new_report.py",
            "--type",
            "swarm",
            "--swarm-id",
            "fixture-swarm",
            "--board",
            "memory-board",
            "--root-task",
            "t_root",
        ],
    )

    assert new_report.main() == 0
    [created] = (tmp_path / "docs/swarms").glob("*_fixture-swarm.md")
    text = created.read_text(encoding="utf-8")
    assert "status: partial" in text
    assert "status: pass" not in text


def test_missing_evidence_rejects_pass(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    body = """
## Sprint goal
Exercise the evidence gate.

## Outcome
The card claims pass without command evidence.

## Decisions
### D1: Evidence
- Decision: Require evidence.
- Reason: False legitimacy risk.
- Tradeoff: More writing.
- Reversibility: easy
- Evidence: `scripts/regen_indexes.py`

## Deferred intentionally
- Nothing was deferred.

## Verification evidence
- The verifier looked acceptable.

## Risks carried forward
- None.

## Next sprint recommendation
Keep testing evidence rules.
"""
    write_valid_swarm(tmp_path, body=body)
    monkeypatch.setattr(regen_indexes, "REPO_ROOT", tmp_path)

    records, errors = regen_indexes.collect(
        tmp_path / "docs/swarms", "swarm_after_action_report"
    )

    assert records == []
    assert any("pass status requires verification evidence" in err for err in errors)


def test_line_ceiling_failure(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    long_tail = "\n".join(f"- extra evidence line {i}" for i in range(220))
    body = (
        valid_postmortem_card(status="unresolved", prevention_status="proposed")
        + "\n"
        + long_tail
    )
    setup_memory_tree(tmp_path)
    path = tmp_path / "docs/postmortems/2026-05-24_long.md"
    path.write_text(body, encoding="utf-8")
    monkeypatch.setattr(regen_indexes, "REPO_ROOT", tmp_path)

    records, errors = regen_indexes.collect(
        tmp_path / "docs/postmortems", "implementation_postmortem"
    )

    assert records == []
    assert any("exceeds 200-line ceiling" in err for err in errors)


def test_forensic_log_path_validation(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    write_valid_swarm(tmp_path, forensic_log="docs/forensics/swarms/missing.log.md")
    monkeypatch.setattr(regen_indexes, "REPO_ROOT", tmp_path)

    records, errors = regen_indexes.collect(
        tmp_path / "docs/swarms", "swarm_after_action_report"
    )

    assert records == []
    assert any("does not exist" in err for err in errors)


def test_resolved_postmortem_without_prevention_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    body = """
## Summary
The issue was closed too quickly.

## Symptom
The report claims resolution.

## Root cause
The prevention mechanism was never recorded.

## Causal chain
- Report claimed resolution.
- Prevention evidence was absent.

## Fix
Closed the issue verbally.

## Prevention
None.

## What we learned
Resolved status needs prevention evidence.

## Open questions
No prevention mechanism has been filed.
"""
    write_valid_postmortem(tmp_path, prevention_status="none", body=body)
    monkeypatch.setattr(regen_indexes, "REPO_ROOT", tmp_path)

    records, errors = regen_indexes.collect(
        tmp_path / "docs/postmortems", "implementation_postmortem"
    )

    assert records == []
    assert any("prevention_status other than none" in err for err in errors)
