# Lumen Security and Threat Model

Version: v0.2-local-deterministic

## Scope

This document covers MVP v0.2 local deterministic operation.

The MVP is not a hosted production service. It has no user accounts, no telemetry, no paid API dependency, no live ingestion, and no blockchain anchoring.

## Assets

Primary assets:

- source/evidence files;
- fixture data;
- audit ledgers;
- governance rules;
- scoring code and docs;
- generated analysis outputs;
- user-supplied local text for analysis.

## Threats

MVP threats include:

- tampering with audit logs;
- modifying fixtures to alter outputs;
- deleting or replacing evidence files;
- introducing hidden scoring rules;
- adding undisclosed network calls;
- leaking local user-supplied text;
- prompt or text injection affecting future model-backed components;
- dependency compromise;
- interface wording that creates false legitimacy;
- malicious contributions that weaken limitation disclosures.

## MVP Controls

Required controls:

- deterministic local processing;
- no paid APIs;
- no LLM calls in v0.2 core;
- no telemetry;
- no secrets in repo;
- hash-chained audit ledger;
- public governance docs;
- visible limitation disclosures;
- source/evidence immutability by convention;
- tests for audit-chain tamper detection;
- review of network dependencies before adding them.

## Audit Security

The MVP audit chain is tamper-evident, not tamper-proof.

It can detect inconsistent changes to event content or ordering. It cannot prevent an attacker with filesystem access from deleting, replacing, or regenerating the entire ledger.

Future hardening may include signed releases, external timestamping, reproducible builds, and optional remote anchoring. These are deferred and must not be implied as implemented.

## Data Handling

MVP should avoid storing unnecessary user data. If user text is analyzed locally, outputs should disclose that analysis is local and deterministic.

No secrets, API keys, tokens, credentials, or private user data should be committed.

## Dependency Policy

Dependencies should be minimal and inspectable.

Before adding dependencies, reviewers should ask:

- Is this needed for the MVP?
- Does it introduce network behavior?
- Does it collect telemetry?
- Does it require credentials?
- Is the license compatible?
- Can the feature work deterministically without it?

## Reporting Security Issues

For MVP development, report security issues through the project issue tracker or maintainer channel once established. Include:

- affected file/component;
- reproduction steps;
- expected impact;
- whether secrets or user data are involved;
- suggested mitigation if known.

Do not publish active exploit details against deployed instances until maintainers have had a reasonable chance to respond.
