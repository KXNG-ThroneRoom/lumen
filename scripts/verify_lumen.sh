#!/usr/bin/env bash
# Lumen aggregate verification gate for v0.6 controlled manual/local input readiness.
#
# Environment expectations:
# - Run from the repository root, or from any directory inside this repo.
# - Use the project Python environment when available: source .venv/bin/activate.
# - .venv/bin/python, or python3 from PATH, must be able to import the
#   apps/api test dependencies.
# - apps/web/node_modules must be installed before npm static/typecheck gates run.
# - This script does not install dependencies, mutate source files, call networks, or
#   require secrets. It only runs local deterministic verification commands.

set -u
set -o pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

failures=0
ran=0
PYTHON_BIN=""

note() {
  printf '\n[%s] %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$*"
}

run_gate() {
  local name="$1"
  shift
  ran=$((ran + 1))
  note "START ${name}: $*"
  if "$@"; then
    note "PASS  ${name}"
  else
    local status=$?
    note "FAIL  ${name} (exit ${status})"
    failures=$((failures + 1))
  fi
}

skip_gate() {
  local name="$1"
  local reason="$2"
  note "SKIP  ${name}: ${reason}"
}

fail_gate_without_run() {
  local name="$1"
  local reason="$2"
  note "FAIL  ${name}: ${reason}"
  failures=$((failures + 1))
}

run_no_hit_scan() {
  local name="$1"
  local pattern="$2"
  shift 2
  ran=$((ran + 1))
  note "START ${name}: local repository scan"
  if "${PYTHON_BIN}" - "$pattern" "$@" <<'PY'
import re
import sys
from pathlib import Path

pattern = re.compile(sys.argv[1], re.IGNORECASE)
roots = sys.argv[2:] or ['.']
repo = Path.cwd()
skip_dirs = {'.git', '.next', '.pytest_cache', '.venv', '__pycache__', 'node_modules'}
skip_names = {'package-lock.json'}
allowed_suffixes = {'.css', '.json', '.jsonl', '.md', '.mjs', '.py', '.sh', '.tsx', '.ts', '.txt', '.yml', '.yaml'}
hits = []

for root_arg in roots:
    root = (repo / root_arg).resolve()
    if not root.exists():
        continue
    candidates = [root] if root.is_file() else root.rglob('*')
    for path in candidates:
        if not path.is_file():
            continue
        rel = path.relative_to(repo)
        if any(part in skip_dirs for part in rel.parts):
            continue
        if path.name in skip_names or path.suffix not in allowed_suffixes:
            continue
        try:
            text = path.read_text(encoding='utf-8', errors='ignore')
        except OSError:
            hits.append(f'{rel}:0: unable to read during scan')
            continue
        for match in pattern.finditer(text):
            line = text[:match.start()].count('\n') + 1
            hits.append(f'{rel}:{line}: redacted scan hit')

if hits:
    print('\n'.join(hits))
    sys.exit(1)
PY
  then
    note "PASS  ${name}"
  else
    local status=$?
    note "FAIL  ${name} (exit ${status})"
    failures=$((failures + 1))
  fi
}

note "Lumen v0.6 aggregate verification: controlled manual/local input only"
note "Repo root: ${REPO_ROOT}"

if [[ -x ".venv/bin/python" ]]; then
  PYTHON_BIN="${REPO_ROOT}/.venv/bin/python"
  note "Python .venv detected. Using ${PYTHON_BIN}"
else
  PYTHON_BIN="$(command -v python3 || true)"
  note "No .venv Python detected. Using python3 from PATH: ${PYTHON_BIN:-missing}"
fi

if [[ -z "${PYTHON_BIN}" ]]; then
  note "FAIL  python interpreter discovery (exit 127)"
  exit 127
fi

if ! "${PYTHON_BIN}" --version >/dev/null 2>&1; then
  note "FAIL  python interpreter check (exit 127)"
  exit 127
fi

if [[ -f "scripts/regen_indexes.py" ]]; then
  run_gate "institutional-memory indexes" "${PYTHON_BIN}" scripts/regen_indexes.py --check --strict
else
  skip_gate "institutional-memory indexes" "scripts/regen_indexes.py not present"
fi

run_no_hit_scan \
  "project contamination scan" \
  'D[o]cD[o]ctor|Open[ ]Epistemic[ ]Engine' \
  README.md CONTRIBUTING.md LIMITATIONS.md SECURITY.md ADVERSARIAL_REVIEW.md CONSTITUTION.md docs apps scripts packages evals examples

run_no_hit_scan \
  "secret literal scan" \
  'AKIA[0-9A-Z]{16}|BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY|OPENAI[_]API[_]KEY|ANTHROPIC[_]API[_]KEY|FAL[_]KEY|LLMAPI[_]API[_]KEY|password\s*=|token\s*=|secret\s*=' \
  README.md CONTRIBUTING.md LIMITATIONS.md SECURITY.md ADVERSARIAL_REVIEW.md docs/checklists docs/demo docs/architecture docs/governance scripts apps/api/README.md apps/api/app apps/api/tests apps/web/README.md apps/web/scripts apps/web/src

if [[ -d "apps/api/tests" ]]; then
  run_gate "api manual/local input contract pytest" \
    "${PYTHON_BIN}" -m pytest \
    apps/api/tests/test_manual_input.py \
    apps/api/tests/test_api_contract.py::test_analyze_returns_stable_v03_contract_with_local_input_evidence \
    apps/api/tests/test_api_contract.py::test_analyze_route_returns_local_input_contract_without_external_capability_claims \
    apps/api/tests/test_api_contract.py::test_manual_ingest_creates_assertion_container_without_url_fetching \
    apps/api/tests/test_api_contract.py::test_manual_ingest_rejects_live_ingestion_modes \
    -q
  run_gate "api pytest" "${PYTHON_BIN}" -m pytest apps/api/tests -q
else
  skip_gate "api pytest" "apps/api/tests not present"
fi

if [[ -d "apps/api/app" ]]; then
  run_gate "api compileall" "${PYTHON_BIN}" -m compileall apps/api/app
else
  skip_gate "api compileall" "apps/api/app not present"
fi

if [[ -f "apps/web/package.json" ]]; then
  if [[ -d "apps/web/node_modules" ]]; then
    if command -v npm >/dev/null 2>&1; then
      run_gate "web static verification" npm run verify:static --prefix apps/web
      run_gate "web typecheck" npm run typecheck --prefix apps/web
    else
      fail_gate_without_run "web npm discovery" "npm not found in PATH"
    fi
  else
    skip_gate "web static verification" "apps/web/node_modules not present; run npm install in apps/web first"
    skip_gate "web typecheck" "apps/web/node_modules not present; run npm install in apps/web first"
    failures=$((failures + 1))
  fi
else
  skip_gate "web verification" "apps/web/package.json not present"
fi

note "Aggregate gates run: ${ran}; failures: ${failures}"

if [[ "${failures}" -ne 0 ]]; then
  note "RESULT FAIL"
  exit 1
fi

note "RESULT PASS"
exit 0
