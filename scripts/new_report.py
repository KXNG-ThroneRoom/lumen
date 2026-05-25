#!/usr/bin/env python3
"""
new_report.py — Scaffold a new institutional-memory card.

Creates a new canonical card under docs/postmortems/ or docs/swarms/ with
pre-populated YAML frontmatter and the required narrative section headers.

Usage:
    # Swarm AAR
    python3 scripts/new_report.py --type swarm \
      --swarm-id lumen-v0-4-ingestion --board lumen-build-server \
      --root-task t_xxxxxx --status partial

    # Postmortem
    python3 scripts/new_report.py --type postmortem \
      --slug api-contract-schema-drift --severity high

Governed by: docs/sops/SOP_INSTITUTIONAL_MEMORY.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

POSTMORTEM_BODY = """
## Summary
<!-- SCAFFOLD: replace with one paragraph before running regen_indexes.py. -->

## Symptom
<!-- SCAFFOLD: replace with observed surface failure only. -->

## Root cause
<!-- SCAFFOLD: replace with root cause, or "unknown" plus investigation stop reason. -->

## Causal chain
<!-- SCAFFOLD: replace with one causal step per line. -->

## Fix
<!-- SCAFFOLD: replace with changed files/commits, or state "no code changed". -->

## Prevention
<!-- SCAFFOLD: replace with prevention mechanism and evidence/rationale. -->

## What we learned
<!-- SCAFFOLD: replace with one or two transferable sentences. -->

## Open questions
<!-- SCAFFOLD: required while prevention_status is none or root cause is unknown. -->
"""

SWARM_BODY = """
## Sprint goal
<!-- SCAFFOLD: replace with one sentence before running regen_indexes.py. -->

## Outcome
<!-- SCAFFOLD: replace with one paragraph about shipped vs. attempted work. -->

## Decisions

<!-- SCAFFOLD: replace with D1/D2 entries using the governing template. -->

## Deferred intentionally
<!-- SCAFFOLD: replace with intentional deferrals or state none. -->

## Verification evidence
<!-- SCAFFOLD: replace with command/check bullets and results. -->

## Risks carried forward
<!-- SCAFFOLD: replace with carried risks or state none. -->

## Next sprint recommendation
<!-- SCAFFOLD: replace with one paragraph. -->
"""


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    return s.strip("-")


def today() -> str:
    return dt.date.today().isoformat()


def build_postmortem(slug: str, severity: str) -> tuple[str, str]:
    date = today()
    filename = f"{date}_{slugify(slug)}.md"
    frontmatter = f"""---
schema_version: 1
doc_type: implementation_postmortem
project: Lumen
phase: ""
sprint: ""
date: {date}
detected_at: ""
introduced_at: ""
resolved_at: ""
detection_method: human_review
repo_path: ""
repo_commit_before: ""
repo_commit_after: ""
branch: ""
status: unresolved
severity: {severity}
prevention_status: none
failure_classes: []
affected_modules: []
affected_files: []
related_tasks: []
related_swarms: []
related_postmortems: []
constitution_articles_at_risk: []
supersedes: ""
tags: []
retrieval_keywords: []
related_docs: []
forensic_log: ""
index_record: "docs/postmortems/index.jsonl"
---
"""
    return filename, frontmatter + POSTMORTEM_BODY


def build_swarm(
    swarm_id: str,
    board: str,
    root_task: str,
    status: str,
    verifier_task: str,
    synthesizer_task: str,
) -> tuple[str, str]:
    date = today()
    filename = f"{date}_{slugify(swarm_id)}.md"
    frontmatter = f"""---
schema_version: 1
doc_type: swarm_after_action_report
project: Lumen
phase: ""
sprint: ""
date: {date}
repo_path: ""
repo_commit_before: ""
repo_commit_after: ""
branch: ""
board: "{board}"
tenant: ""
root_task: "{root_task}"
verifier_task: "{verifier_task}"
synthesizer_task: "{synthesizer_task}"
status: {status}
gate_status: {status}
duration_hours: 0
files_changed_count: 0
tests_passed: 0
tests_failed: 0
blockers_resolved: 0
blockers_unresolved: 0
modules_touched: []
constitution_articles_engaged: []
workers: []
supersedes: ""
related_postmortems: []
related_swarms: []
tags: []
retrieval_keywords: []
related_docs: []
forensic_log: ""
index_record: "docs/swarms/index.jsonl"
---
"""
    return filename, frontmatter + SWARM_BODY


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--type", choices=["postmortem", "swarm"], required=True)
    p.add_argument("--slug", help="postmortem only — short slug for filename")
    p.add_argument("--severity", choices=["low", "medium", "high", "critical"], default="medium")
    p.add_argument("--swarm-id", help="swarm only")
    p.add_argument("--board", default="", help="swarm only")
    p.add_argument("--root-task", default="", help="swarm only")
    p.add_argument("--verifier-task", default="", help="swarm only")
    p.add_argument("--synthesizer-task", default="", help="swarm only")
    p.add_argument(
        "--status", choices=["pass", "partial", "fail"], default="partial",
        help="swarm only",
    )
    p.add_argument("--force", action="store_true", help="overwrite if file exists")
    args = p.parse_args()

    if args.type == "postmortem":
        if not args.slug:
            print("error: --slug required for postmortem", file=sys.stderr)
            return 1
        filename, body = build_postmortem(args.slug, args.severity)
        target_dir = REPO_ROOT / "docs" / "postmortems"
    else:
        if not args.swarm_id:
            print("error: --swarm-id required for swarm", file=sys.stderr)
            return 1
        filename, body = build_swarm(
            args.swarm_id,
            args.board,
            args.root_task,
            args.status,
            args.verifier_task,
            args.synthesizer_task,
        )
        target_dir = REPO_ROOT / "docs" / "swarms"

    target_dir.mkdir(parents=True, exist_ok=True)
    out = target_dir / filename
    if out.exists() and not args.force:
        print(f"error: {out.relative_to(REPO_ROOT)} already exists (use --force)", file=sys.stderr)
        return 1
    out.write_text(body, encoding="utf-8")
    print(str(out.relative_to(REPO_ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
