# Lumen Ingestors

Boundary for collecting inputs while preserving originals. MVP starts with sample JSON/manual inputs; production crawling and paid data feeds are out of scope.

## Contract

- Inputs and outputs must be schema-described.
- Derived outputs must reference source object IDs and audit event IDs where applicable.
- Limitations and placeholders must be visible.
- No hidden scoring, secret prompts, telemetry, credentials, or paid API requirement in the MVP scaffold.

## MVP status

This directory is a package boundary placeholder. Implementation should stay narrow and deterministic until a specific sprint expands it.
