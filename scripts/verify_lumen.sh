#!/usr/bin/env bash
# Lumen aggregate verification gate for v0.4 readiness.
#
# Environment expectations:
# - Run from the repository root, or from any directory inside this repo.
# - Use the project Python environment when available: source .venv/bin/activate.
# - python3 must be available and able to import the apps/api test dependencies.
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

note "Lumen v0.4 aggregate verification"
note "Repo root: ${REPO_ROOT}"

if [[ -x ".venv/bin/python" ]]; then
  PYTHON_BIN="${REPO_ROOT}/.venv/bin/python"
  note "Python .venv detected. Using ${PYTHON_BIN}"
else
  PYTHON_BIN="$(command -v python3 || true)"
  note "No .venv Python detected. Using python3 from PATH: ${PYTHON_BIN:-missing}"
fi

if [[ -f "scripts/regen_indexes.py" ]]; then
  run_gate "institutional-memory indexes" "${PYTHON_BIN}" scripts/regen_indexes.py --check --strict
else
  skip_gate "institutional-memory indexes" "scripts/regen_indexes.py not present"
fi

if [[ -d "apps/api/tests" ]]; then
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
    run_gate "web static verification" npm run verify:static --prefix apps/web
    run_gate "web typecheck" npm run typecheck --prefix apps/web
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
