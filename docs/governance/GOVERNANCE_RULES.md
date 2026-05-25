# Lumen Governance Rules

Version: v0.6-controlled-manual-input
Scope: MVP governance, scoring, audit, and public-facing disclosure rules.

## 1. Governing Doctrine

Lumen exposes methods, evidence, claims, uncertainty, and provenance. It does not decide what users must believe.

All outputs must preserve the distinction between:

- what was claimed;
- who or what made the claim;
- what evidence was linked;
- what evidence is missing;
- what contradictions were found;
- what rules were applied;
- what remains unknown, unresolved, or contested.

## 2. Mandatory Output Rules

Every displayed claim must include:

- status;
- confidence band;
- confidence reason;
- evidence references or explicit missing-evidence notes;
- source/provenance reference;
- audit reference.

Every demo flow must include a visible limitations reference and must preserve the no-authority stance: outputs expose method-state, evidence, provenance, uncertainty, and audit lineage for human inspection.

For v0.6, controlled manual input is an assertion boundary. Submitted text, source labels, and URL-looking strings may be inspected as supplied material, but they must not be presented as fetched, authenticated, current, complete, or true unless a later scoped capability explicitly provides that evidence and limitation disclosure.

Public README, contributing, demo, and release notes must link `LIMITATIONS.md` and `ADVERSARIAL_REVIEW.md` when they describe analytical outputs, confidence, or audit trails.

## 3. Valid Claim Statuses

Lumen may use these MVP statuses:

- supported: evidence currently attached supports the claim under documented rules.
- strongly_corroborated: multiple independent evidence streams support the claim, with strong provenance.
- plausible: evidence is partial, indirect, or not independently confirmed.
- unresolved: evidence is insufficient to support or reject the claim.
- contested: credible attached evidence or claims conflict.
- contradicted: attached evidence directly conflicts with the claim.
- unsupported: no adequate supporting evidence is attached.
- unknown: the system cannot classify the claim honestly with available inputs.

Status labels describe method-state, not final reality.

## 4. Confidence Bands

MVP confidence bands:

- high: strong provenance, primary or near-primary evidence, and independent support with no material unresolved contradiction.
- medium: meaningful support exists, but some dependency, missing context, or indirect evidence remains.
- low: weak, indirect, dependent, anonymous, or incomplete evidence dominates.
- capped: a rule cap prevents a higher band, usually due to anonymity, dependency, missing provenance, or unresolved contradiction.
- unknown: confidence cannot be assigned honestly.

A confidence band without a visible reason is invalid.

## 5. Anonymous-Source Caps

Anonymous-source claims are capped unless stronger evidence is attached.

Default caps:

- unsupported anonymous assertion: capped at low;
- anonymous official or unnamed institutional source: capped at low unless independently supported;
- anonymous eyewitness: capped at low unless corroborated by primary or independent evidence;
- anonymous expert interpretation: capped at low unless tied to inspectable evidence;
- leaked document: score the document provenance separately; anonymity of leaker does not make the document self-validating.

No number of dependent anonymous repeats should raise confidence by itself.

## 6. Source-Independence Rules

Article volume is not evidence volume.

Sources are not independent when they share:

- the same wire-service origin;
- circular citation;
- a common press release;
- the same anonymous briefing;
- replicated wording without separate reporting;
- same ownership/funding where relevant to the claim;
- synchronized publication without disclosed independent evidence.

Dependent sources may show spread or amplification. They must not be counted as independent corroboration.

## 7. Primary-Evidence Rule

Primary evidence can raise confidence when provenance and relevance are adequate.

Primary evidence includes original documents, full transcripts, official datasets, court filings, direct video, direct images, geolocation material, timestamped records, raw source material, and archived originals.

Primary evidence does not remove uncertainty. It must still be assessed for authenticity, completeness, context, chain of custody, timestamp quality, and relevance.

## 8. Contradiction Handling

Contradictions must be exposed, not forced into premature resolution.

When material contradictions exist, the claim should usually be contested or capped unless governance rules document why the contradiction is not material.

Contradiction outputs must identify:

- conflicting claim or evidence;
- contradiction type;
- source references;
- uncertainty note;
- audit reference.

## 9. Limitation Disclosure Policy

Limitations must appear close to the output they qualify.

Required disclosures include:

- fixture/demo data;
- placeholder extraction;
- incomplete source coverage;
- missing primary evidence;
- source dependency;
- anonymous-source caps;
- unresolved contradiction;
- stale or uncertain timestamps;
- current-demo scope limits.
- manual/local input limits, including that `source_url` is metadata only and no URL is fetched in v0.6.

Limitations must be written plainly and must not be buried in footnotes alone.

For v0.6 demo and launch-facing surfaces, limitation links are required in `README.md`, `LIMITATIONS.md`, `docs/architecture/DEMO_FLOW.md`, and any UI/API path that displays analysis. A missing limitation reference is a release blocker, not a copy edit.

## 10. Audit Requirements

Every meaningful transformation must create or reference an audit event.

MVP audit events should cover:

- sample loaded;
- claim extracted or placeholder-generated;
- evidence attached;
- score assigned;
- source dependency evaluated;
- contradiction checked;
- governance rule applied.

Audit events must include rule version, operation, reason, input hash, output hash, previous hash, and event hash where available.

## 11. User Interface Governance

The interface must not create certainty theater.

UI must avoid:

- single unexplained aggregate scores;
- green/red verdict framing without method context;
- hidden uncertainty;
- unsupported badges of authority;
- overconfident summaries;
- suppressing unresolved questions;
- stale multi-panel interface language on the current public demo.

The v0.6 public UI must match the simplified controlled demo unless a later scoped change updates this rule:

- main claim: "When does the regulation start?";
- explanation: two sources disagree, with June 1 from a news report and July 1 from an official filing;
- tabs: Story, Evidence, Why uncertain, Audit;
- visual language: uncertain/contested, support, and conflict;
- no raw hashes, audit IDs, machine labels, or `.md` references in the public UI;
- no wording that says Lumen decides the final truth.
- no wording that implies manual/local input performs live ingestion, source authentication, URL retrieval, or production verification.

## 12. Governance Change Process

Any change to these rules must be documented with:

- changed rule;
- reason;
- expected effect;
- risk of misuse;
- test/eval impact;
- reviewer or challenge notes when available.

Silent governance changes are prohibited.

## 13. Adversarial Review Linkage

The public challenge process is defined in `../../ADVERSARIAL_REVIEW.md`.

Governance docs, demo documentation, and launch-facing flows should link or name the adversarial review process wherever Lumen asks users to trust its methods. At minimum, the challenge path must be visible from:

- limitation disclosures;
- confidence/scoring documentation;
- audit or verification documentation;
- public demo notes or release audit notes.

Challenges may target status assignment, confidence reasons, source-independence handling, limitation disclosure, audit completeness, and UI wording that implies excessive certainty.

Contributor onboarding must point new contributors to this challenge path before they change public wording, scoring rules, or demo claims.
