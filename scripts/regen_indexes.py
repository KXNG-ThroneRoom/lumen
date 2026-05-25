#!/usr/bin/env python3
"""
regen_indexes.py — Rebuild institutional-memory indexes from canonical cards.

Walks docs/postmortems/ and docs/swarms/, parses YAML frontmatter from each
.md file, validates against closed enums, and writes one JSON line per card
into the corresponding index.jsonl.

Usage:
    python3 scripts/regen_indexes.py
    python3 scripts/regen_indexes.py --check   # exit non-zero if indexes are stale
    python3 scripts/regen_indexes.py --strict  # validate only; never writes indexes

Governed by: docs/sops/SOP_INSTITUTIONAL_MEMORY.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Closed enums — must match docs/sops/CHANGELOG.md
# ---------------------------------------------------------------------------

ENUMS: dict[str, set[str]] = {
    "failure_classes": {
        "schema_drift",
        "test_failure",
        "orchestration_failure",
        "integration_failure",
        "architecture_drift",
        "governance_risk",
        "documentation_gap",
        "dependency_issue",
    },
    "postmortem_status": {"resolved", "partially_resolved", "unresolved"},
    "swarm_status": {"pass", "partial", "fail"},
    "severity": {"low", "medium", "high", "critical"},
    "prevention_status": {"none", "proposed", "filed", "implemented", "verified"},
    "detection_method": {
        "human_review",
        "verifier",
        "test",
        "user_report",
        "grep",
        "runtime",
        "other",
    },
    "worker_status": {"done", "blocked", "abandoned", "replaced"},
    "decision_reversibility": {"easy", "moderate", "hard"},
}

# ---------------------------------------------------------------------------
# Minimal YAML frontmatter parser
# Supports: scalars, lists (- item), nested maps, quoted strings, blanks.
# Does NOT support: anchors, multi-line scalars, flow style.
# Sufficient for our template schema; refuses anything weirder.
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, Any] | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    return parse_yaml_block(m.group(1))


def parse_yaml_block(block: str) -> dict[str, Any]:
    lines = block.splitlines()
    result, _ = _parse_mapping(lines, 0, indent=0)
    return result


def _strip_comment(value: str) -> str:
    # Strip trailing `# comment` if not inside quotes.
    in_single = False
    in_double = False
    for i, ch in enumerate(value):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double:
            return value[:i].rstrip()
    return value.rstrip()


def _coerce_scalar(raw: str) -> Any:
    s = _strip_comment(raw).strip()
    if s == "":
        return ""
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    low = s.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if low in ("null", "~"):
        return None
    # number?
    try:
        if "." in s:
            return float(s)
        return int(s)
    except ValueError:
        pass
    return s


def _indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _parse_mapping(lines: list[str], start: int, indent: int) -> tuple[dict[str, Any], int]:
    out: dict[str, Any] = {}
    i = start
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped == "" or stripped.startswith("#"):
            i += 1
            continue
        cur_indent = _indent_of(line)
        if cur_indent < indent:
            return out, i
        if cur_indent > indent:
            # malformed at this level; skip
            i += 1
            continue
        if ":" not in stripped:
            i += 1
            continue
        key, _, rest = stripped.partition(":")
        key = key.strip()
        rest = rest.rstrip()
        # Empty value → nested map or list on following lines
        if rest.strip() == "":
            # Peek next non-blank line
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j >= len(lines):
                out[key] = None
                i = j
                continue
            peek = lines[j]
            peek_indent = _indent_of(peek)
            peek_stripped = peek.strip()
            if peek_indent <= indent:
                out[key] = None
                i = j
                continue
            if peek_stripped.startswith("- "):
                value, i = _parse_list(lines, j, peek_indent)
                out[key] = value
                continue
            value, i = _parse_mapping(lines, j, peek_indent)
            out[key] = value
            continue
        # Inline value
        rest_stripped = rest.strip()
        if rest_stripped.startswith("[") and rest_stripped.endswith("]"):
            # Flow-style empty or simple list
            inner = rest_stripped[1:-1].strip()
            if inner == "":
                out[key] = []
            else:
                items = [_coerce_scalar(x) for x in _split_top_commas(inner)]
                out[key] = items
        else:
            out[key] = _coerce_scalar(rest)
        i += 1
    return out, i


def _split_top_commas(s: str) -> list[str]:
    parts, depth, cur, in_s, in_d = [], 0, [], False, False
    for ch in s:
        if ch == "'" and not in_d:
            in_s = not in_s
        elif ch == '"' and not in_s:
            in_d = not in_d
        if ch in "[{" and not in_s and not in_d:
            depth += 1
        elif ch in "]}" and not in_s and not in_d:
            depth -= 1
        if ch == "," and depth == 0 and not in_s and not in_d:
            parts.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    if cur:
        parts.append("".join(cur).strip())
    return [p for p in parts if p]


def _parse_list(lines: list[str], start: int, indent: int) -> tuple[list[Any], int]:
    out: list[Any] = []
    i = start
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped == "" or stripped.startswith("#"):
            i += 1
            continue
        cur_indent = _indent_of(line)
        if cur_indent < indent:
            return out, i
        if cur_indent > indent:
            i += 1
            continue
        if not stripped.startswith("- "):
            return out, i
        item_text = stripped[2:].rstrip()
        if item_text == "":
            # Nested item
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and _indent_of(lines[j]) > cur_indent:
                value, i = _parse_mapping(lines, j, _indent_of(lines[j]))
                out.append(value)
                continue
            out.append(None)
            i += 1
            continue
        # Inline item — could be `- key: value` (mapping) or a scalar
        if ":" in item_text and not (item_text.startswith('"') or item_text.startswith("'")):
            key, _, rest = item_text.partition(":")
            key = key.strip()
            rest = rest.strip()
            item_map: dict[str, Any] = {}
            if rest == "":
                item_map[key] = None
            else:
                item_map[key] = _coerce_scalar(rest)
            # Continuation lines deeper than item_indent are part of this map
            item_inner_indent = cur_indent + 2
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                nxt_stripped = nxt.strip()
                if nxt_stripped == "" or nxt_stripped.startswith("#"):
                    j += 1
                    continue
                if _indent_of(nxt) < item_inner_indent:
                    break
                if nxt_stripped.startswith("- "):
                    break
                # parse single key: value
                if ":" in nxt_stripped:
                    k2, _, r2 = nxt_stripped.partition(":")
                    k2 = k2.strip()
                    r2_stripped = r2.strip()
                    if r2_stripped == "":
                        # nested list/map
                        k = j + 1
                        while k < len(lines) and lines[k].strip() == "":
                            k += 1
                        if k < len(lines) and _indent_of(lines[k]) > _indent_of(nxt):
                            peek = lines[k].strip()
                            if peek.startswith("- "):
                                v, j = _parse_list(lines, k, _indent_of(lines[k]))
                            else:
                                v, j = _parse_mapping(lines, k, _indent_of(lines[k]))
                            item_map[k2] = v
                            continue
                        item_map[k2] = None
                        j += 1
                        continue
                    if r2_stripped.startswith("[") and r2_stripped.endswith("]"):
                        inner = r2_stripped[1:-1].strip()
                        item_map[k2] = (
                            [_coerce_scalar(x) for x in _split_top_commas(inner)] if inner else []
                        )
                    else:
                        item_map[k2] = _coerce_scalar(r2)
                j += 1
            out.append(item_map)
            i = j
            continue
        out.append(_coerce_scalar(item_text))
        i += 1
    return out, i


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

EXPECTED_INDEX_RECORDS = {
    "implementation_postmortem": "docs/postmortems/index.jsonl",
    "swarm_after_action_report": "docs/swarms/index.jsonl",
}

EXPECTED_FORENSIC_PREFIXES = {
    "implementation_postmortem": "docs/forensics/postmortems/",
    "swarm_after_action_report": "docs/forensics/swarms/",
}

LINE_CEILINGS = {
    "implementation_postmortem": 200,
    "swarm_after_action_report": 250,
}

COMMON_REQUIRED = [
    "schema_version",
    "doc_type",
    "project",
    "phase",
    "sprint",
    "date",
    "repo_path",
    "repo_commit_before",
    "repo_commit_after",
    "branch",
    "status",
    "index_record",
]

POSTMORTEM_REQUIRED = [
    "detected_at",
    "introduced_at",
    "detection_method",
    "severity",
    "prevention_status",
    "failure_classes",
]

SWARM_REQUIRED = [
    "board",
    "root_task",
    "gate_status",
    "duration_hours",
    "files_changed_count",
    "tests_passed",
    "tests_failed",
    "blockers_resolved",
    "blockers_unresolved",
    "modules_touched",
    "workers",
]

POSTMORTEM_REQUIRED_SECTIONS = [
    "Summary",
    "Symptom",
    "Root cause",
    "Causal chain",
    "Fix",
    "Prevention",
    "What we learned",
]

SWARM_REQUIRED_SECTIONS = [
    "Sprint goal",
    "Outcome",
    "Decisions",
    "Deferred intentionally",
    "Verification evidence",
    "Risks carried forward",
    "Next sprint recommendation",
]

PLACEHOLDER_RE = re.compile(
    r"(\bTBD\b|\bTODO\b|Fill in|<!--\s*SCAFFOLD:|<[^>\n]+>|\[\s*\.\.\.\s*\])",
    re.IGNORECASE,
)
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _is_empty(value: Any) -> bool:
    return value in ("", None)


def _require_nonempty(fm: dict[str, Any], keys: list[str], path: Path) -> list[str]:
    errs: list[str] = []
    for key in keys:
        if key not in fm:
            errs.append(f"{path}: missing required field `{key}`")
        elif _is_empty(fm[key]):
            errs.append(f"{path}: required field `{key}` must not be empty")
    return errs


def body_from_text(text: str) -> str:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return text
    return text[m.end():]


def markdown_sections(body: str) -> dict[str, str]:
    matches = list(SECTION_RE.finditer(body))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        sections[title.lower()] = body[start:end].strip()
    return sections


def has_placeholder(text: str) -> bool:
    return bool(PLACEHOLDER_RE.search(text))


def strip_html_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def has_substantive_content(text: str) -> bool:
    cleaned = strip_html_comments(text)
    if has_placeholder(cleaned):
        return False
    for line in cleaned.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if re.search(r"[A-Za-z0-9]", stripped):
            return True
    return False


def validate_required_sections(
    body: str, required: list[str], path: Path, doc_label: str
) -> tuple[dict[str, str], list[str]]:
    errs: list[str] = []
    sections = markdown_sections(body)
    if has_placeholder(body):
        errs.append(f"{path}: {doc_label} body contains scaffold placeholder text")
    for title in required:
        content = sections.get(title.lower())
        if content is None:
            errs.append(f"{path}: missing required section `## {title}`")
        elif not has_substantive_content(content):
            errs.append(f"{path}: required section `## {title}` is empty or placeholder-only")
    return sections, errs


def validate_line_ceiling(text: str, fm: dict[str, Any], path: Path, doc_type: str) -> list[str]:
    errs: list[str] = []
    ceiling = LINE_CEILINGS[doc_type]
    line_count = len(text.splitlines())
    has_exception = fm.get("line_ceiling_exception") is True
    reason = fm.get("line_ceiling_exception_reason")
    if line_count > ceiling and not has_exception:
        errs.append(
            f"{path}: {line_count} lines exceeds {ceiling}-line ceiling; "
            "move detail to forensic_log or set line_ceiling_exception with reason"
        )
    if has_exception and not has_substantive_content(str(reason or "")):
        errs.append(f"{path}: line_ceiling_exception requires line_ceiling_exception_reason")
    return errs


def validate_common(fm: dict[str, Any], text: str, path: Path, doc_type: str) -> list[str]:
    errs = _require_nonempty(fm, COMMON_REQUIRED, path)
    if fm.get("schema_version") != 1:
        errs.append(f"{path}: schema_version must be 1")
    if fm.get("doc_type") != doc_type:
        errs.append(f"{path}: doc_type must be `{doc_type}`")
    if fm.get("project") != "Lumen":
        errs.append(f"{path}: project must be `Lumen`")
    if fm.get("index_record") != EXPECTED_INDEX_RECORDS[doc_type]:
        errs.append(
            f"{path}: index_record must be `{EXPECTED_INDEX_RECORDS[doc_type]}`"
        )
    date_value = fm.get("date")
    if isinstance(date_value, str) and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_value):
        errs.append(f"{path}: date must use YYYY-MM-DD")
    elif not isinstance(date_value, str):
        errs.append(f"{path}: date must be a YYYY-MM-DD string")
    errs.extend(validate_forensic_log(fm, path, doc_type))
    errs.extend(validate_line_ceiling(text, fm, path, doc_type))
    return errs


def validate_forensic_log(fm: dict[str, Any], path: Path, doc_type: str) -> list[str]:
    errs: list[str] = []
    forensic_log = fm.get("forensic_log", "")
    if _is_empty(forensic_log):
        return errs
    if not isinstance(forensic_log, str):
        return [f"{path}: forensic_log must be a relative path string"]
    expected_prefix = EXPECTED_FORENSIC_PREFIXES[doc_type]
    if forensic_log.startswith("/") or ".." in Path(forensic_log).parts:
        errs.append(f"{path}: forensic_log must be a safe relative path under {expected_prefix}")
        return errs
    if not forensic_log.startswith(expected_prefix) or not forensic_log.endswith(".log.md"):
        errs.append(f"{path}: forensic_log must live under {expected_prefix} and end in .log.md")
        return errs
    target = REPO_ROOT / forensic_log
    if not target.exists():
        errs.append(f"{path}: forensic_log `{forensic_log}` does not exist")
    return errs


def validate_list_enum(
    fm: dict[str, Any], field: str, enum_name: str, path: Path
) -> list[str]:
    errs: list[str] = []
    values = fm.get(field) or []
    if not isinstance(values, list):
        return [f"{path}: {field} must be a list"]
    for value in values:
        if value and value not in ENUMS[enum_name]:
            errs.append(f"{path}: {field} value `{value}` not in {sorted(ENUMS[enum_name])}")
    return errs


def validate_worker_statuses(fm: dict[str, Any], path: Path) -> list[str]:
    errs: list[str] = []
    workers = fm.get("workers")
    if workers is None:
        return errs
    if not isinstance(workers, list):
        return [f"{path}: workers must be a list"]
    for w in workers:
        if not isinstance(w, dict):
            errs.append(f"{path}: each worker entry must be a map")
            continue
        status = w.get("status")
        if status and status not in ENUMS["worker_status"]:
            errs.append(
                f"{path}: worker.status `{status}` not in {sorted(ENUMS['worker_status'])}"
            )
    return errs


def validate_decision_reversibility(sections: dict[str, str], path: Path) -> list[str]:
    errs: list[str] = []
    decisions = sections.get("decisions", "")
    for match in re.finditer(r"(?im)^\s*-\s*Reversibility:\s*(.+?)\s*$", decisions):
        value = match.group(1).strip()
        if value not in ENUMS["decision_reversibility"]:
            errs.append(
                f"{path}: decision.reversibility `{value}` not in "
                f"{sorted(ENUMS['decision_reversibility'])}"
            )
    return errs


def has_command_result(content: str) -> bool:
    for line in content.splitlines():
        stripped = line.strip()
        lowered = stripped.lower()
        if not stripped.startswith("-"):
            continue
        has_check = (
            "`" in stripped
            or "check" in lowered
            or "scan" in lowered
            or "test" in lowered
            or "verify" in lowered
        )
        has_result = any(
            token in lowered
            for token in ("->", "→", " passed", " pass", " clean", " ok", " failed", " fail")
        )
        if has_check and has_result:
            return True
    return False


def has_evidence_marker(content: str) -> bool:
    for line in content.splitlines():
        lowered = line.lower()
        if "`" in line:
            return True
        if re.search(r"\b(apps|docs|scripts|tests|evals)/", line):
            return True
        if any(token in lowered for token in ("commit", "pr ", "issue", "test", "verified")):
            return True
    return False


def validate_postmortem(fm: dict[str, Any], text: str, path: Path) -> list[str]:
    doc_type = "implementation_postmortem"
    errs = validate_common(fm, text, path, doc_type)
    errs.extend(_require_nonempty(fm, POSTMORTEM_REQUIRED, path))
    if fm.get("status") and fm["status"] not in ENUMS["postmortem_status"]:
        errs.append(f"{path}: status `{fm['status']}` not in {sorted(ENUMS['postmortem_status'])}")
    if fm.get("severity") and fm["severity"] not in ENUMS["severity"]:
        errs.append(f"{path}: severity `{fm['severity']}` not in {sorted(ENUMS['severity'])}")
    if fm.get("prevention_status") and fm["prevention_status"] not in ENUMS["prevention_status"]:
        errs.append(
            f"{path}: prevention_status `{fm['prevention_status']}` not in "
            f"{sorted(ENUMS['prevention_status'])}"
        )
    if fm.get("detection_method") and fm["detection_method"] not in ENUMS["detection_method"]:
        errs.append(
            f"{path}: detection_method `{fm['detection_method']}` not in "
            f"{sorted(ENUMS['detection_method'])}"
        )
    errs.extend(validate_list_enum(fm, "failure_classes", "failure_classes", path))

    body = body_from_text(text)
    sections, section_errors = validate_required_sections(
        body, POSTMORTEM_REQUIRED_SECTIONS, path, "postmortem"
    )
    errs.extend(section_errors)

    status = fm.get("status")
    prevention_status = fm.get("prevention_status")
    if status == "resolved":
        if _is_empty(fm.get("resolved_at")):
            errs.append(f"{path}: resolved postmortems require resolved_at")
        if prevention_status == "none":
            errs.append(f"{path}: resolved postmortems require prevention_status other than none")
        fix = sections.get("fix", "")
        prevention = sections.get("prevention", "")
        if not has_evidence_marker(fix):
            errs.append(f"{path}: resolved postmortems require fix evidence")
        if not has_evidence_marker(prevention):
            errs.append(f"{path}: resolved postmortems require prevention evidence or rationale")
    if prevention_status == "none":
        open_questions = sections.get("open questions")
        if open_questions is None or not has_substantive_content(open_questions):
            errs.append(f"{path}: prevention_status none requires `## Open questions` rationale")
    root_cause = sections.get("root cause", "")
    if re.search(r"\bunknown\b", root_cause, re.IGNORECASE):
        open_questions = sections.get("open questions")
        if open_questions is None or not has_substantive_content(open_questions):
            errs.append(f"{path}: unknown root cause requires `## Open questions`")
    return errs


def validate_swarm(fm: dict[str, Any], text: str, path: Path) -> list[str]:
    doc_type = "swarm_after_action_report"
    errs = validate_common(fm, text, path, doc_type)
    errs.extend(_require_nonempty(fm, SWARM_REQUIRED, path))
    for key in ("status", "gate_status"):
        value = fm.get(key)
        if value and value not in ENUMS["swarm_status"]:
            errs.append(f"{path}: {key} `{value}` not in {sorted(ENUMS['swarm_status'])}")
    errs.extend(validate_worker_statuses(fm, path))

    body = body_from_text(text)
    sections, section_errors = validate_required_sections(
        body, SWARM_REQUIRED_SECTIONS, path, "swarm"
    )
    errs.extend(section_errors)
    errs.extend(validate_decision_reversibility(sections, path))

    if fm.get("status") == "pass" or fm.get("gate_status") == "pass":
        verification = sections.get("verification evidence", "")
        if not has_command_result(verification):
            errs.append(
                f"{path}: pass status requires verification evidence with at least "
                "one command/check and result"
            )
    return errs


# ---------------------------------------------------------------------------
# Index emission
# ---------------------------------------------------------------------------

def is_template_or_readme(path: Path) -> bool:
    name = path.name.lower()
    return name in ("readme.md",) or "template" in name


def collect(folder: Path, doc_type: str) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    if not folder.exists():
        return records, errors
    for path in sorted(folder.glob("*.md")):
        if is_template_or_readme(path):
            continue
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{path}: missing or malformed YAML frontmatter")
            continue
        if fm.get("doc_type") != doc_type:
            errors.append(
                f"{path}: doc_type `{fm.get('doc_type')}` does not match folder type `{doc_type}`"
            )
            continue
        path_errors: list[str]
        if doc_type == "implementation_postmortem":
            path_errors = validate_postmortem(fm, text, path)
        else:
            path_errors = validate_swarm(fm, text, path)
        if path_errors:
            errors.extend(path_errors)
            continue
        # Attach source path for traceability
        fm["_source"] = _rel(path)
        records.append(fm)
    return records, errors


def write_index(records: list[dict[str, Any]], index_path: Path) -> None:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with index_path.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, sort_keys=True, ensure_ascii=False) + "\n")


def render_proposed(records: list[dict[str, Any]]) -> str:
    return "".join(
        json.dumps(rec, sort_keys=True, ensure_ascii=False) + "\n" for rec in records
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if existing indexes differ from regenerated output. "
        "Does not write files.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Validate only and exit non-zero on any validation error. Does not write files.",
    )
    args = parser.parse_args()

    targets = [
        (
            REPO_ROOT / "docs" / "postmortems",
            REPO_ROOT / "docs" / "postmortems" / "index.jsonl",
            "implementation_postmortem",
        ),
        (
            REPO_ROOT / "docs" / "swarms",
            REPO_ROOT / "docs" / "swarms" / "index.jsonl",
            "swarm_after_action_report",
        ),
    ]

    all_errors: list[str] = []
    target_results: list[tuple[Path, list[dict[str, Any]]]] = []
    stale = False

    for folder, index_path, doc_type in targets:
        records, errors = collect(folder, doc_type)
        all_errors.extend(errors)
        target_results.append((index_path, records))

    if all_errors:
        print("\nValidation errors:", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    if args.strict and not args.check:
        for index_path, records in target_results:
            print(f"VALID: {index_path.relative_to(REPO_ROOT)} ({len(records)} records)")
        return 0

    for index_path, records in target_results:
        proposed = render_proposed(records)
        if args.check:
            existing = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
            if existing != proposed:
                stale = True
                print(f"STALE: {index_path.relative_to(REPO_ROOT)}")
            else:
                print(f"OK:    {index_path.relative_to(REPO_ROOT)} ({len(records)} records)")
        else:
            write_index(records, index_path)
            print(
                f"wrote {index_path.relative_to(REPO_ROOT)}  "
                f"({len(records)} records)"
            )

    if args.check and stale:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
