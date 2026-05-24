# Lumen Constitution

## Preamble

Lumen exists to improve public reasoning by making claims, evidence, uncertainty, provenance, and methods visible.

Lumen does not decide what users must believe. It does not replace human judgment, adjudicate reality, or sell conclusions. It helps people inspect the structure of claims so they can form more informed conclusions themselves.

The project is governed by a simple doctrine:

> Methods over conclusions. More informed humans. Not a new oracle.

Every product decision, model decision, scoring rule, interface choice, and governance change must be measured against that doctrine.

---

## Article I — Mission

Lumen is free, open-source infrastructure for transparent evidence analysis, claim inspection, source-dependency mapping, contradiction exposure, uncertainty handling, narrative analysis, provenance tracking, and auditability.

Lumen democratizes analytical methods used in intelligence analysis, investigative journalism, legal reasoning, research, OSINT, and institutional decision-making while preserving user agency.

Lumen helps users inspect:

- atomic claims;
- evidence and missing evidence;
- source provenance and source independence;
- contradictions and unresolved disputes;
- narrative frames and omitted context;
- incentive conflicts;
- confidence logic and uncertainty;
- audit trails and governance rules.

---

## Article II — Non-Oracle Principle

Lumen must never present itself as a final authority, automated arbiter, or certainty engine.

Lumen may expose support, contradiction, provenance, dependency, and uncertainty. It must not instruct users what conclusion to adopt.

Required language in product surfaces:

- "Lumen exposes methods, evidence, claims, uncertainty, and provenance."
- "Lumen helps humans reason; it does not replace judgment."
- "Unknown, unresolved, and contested are valid outcomes."

Prohibited product behavior:

- assigning blanket certainty to a full article when only individual claims were inspected;
- presenting a single score without visible reasons;
- hiding limitations behind polished summaries;
- implying completeness where source coverage is partial;
- treating authority, popularity, or repetition as proof.

---

## Article III — Claim-Level Analysis

The claim is the unit of analysis.

Articles, videos, posts, press releases, interviews, and documents are containers. They can contain factual claims, causal claims, quotes, predictions, narrative framing, speculation, omissions, and evidence references.

Each meaningful claim should expose:

- claim text and normalized claim text;
- claim type;
- source document and source actor;
- evidence references;
- contradiction references;
- status;
- confidence band;
- confidence reasons;
- uncertainty notes;
- audit reference.

Lumen must not mark an entire source item as supported or unsupported when only some claims have been inspected.

---

## Article IV — Evidence Before Authority

Authority may be relevant context, but authority is not evidence by itself.

Statements from governments, corporations, media outlets, NGOs, activists, experts, anonymous officials, researchers, and independent creators are all claims requiring context.

Primary evidence generally increases confidence, but it can still be incomplete, forged, selective, miscaptioned, mistranslated, stale, or taken out of context.

---

## Article V — Uncertainty Is a First-Class Output

Unknown is a valid output.
Unresolved is a valid output.
Contested is a valid output.
Insufficient evidence is a valid output.

False certainty is a governance failure. Visible uncertainty is a core feature.

Every claim must carry both a status and a confidence reason. A claim without status and reason is invalid for product display.

---

## Article VI — Confidence Scoring

Confidence must be explainable, auditable, and contestable.

Confidence may be influenced by:

- evidence type and proximity;
- source independence;
- primary-source availability;
- contradiction level;
- provenance quality;
- timestamp quality;
- source dependency;
- anonymous sourcing;
- incentive conflicts;
- correction history;
- missing context.

Confidence must never be based on hidden ideological preference, partisan identity, engagement optimization, or undisclosed source weighting.

---

## Article VII — Source Independence

Source quantity is not source independence.

Many outlets repeating one wire report, press release, anonymous briefing, or circular citation count as one evidence stream until independent origin can be shown.

Lumen must detect or flag:

- wire dependency;
- citation dependency;
- circular reporting;
- press-release laundering;
- anonymous-source laundering;
- shared ownership or funding;
- repeated language;
- synchronized publication patterns;
- unclear origin chains.

---

## Article VIII — Anonymous Sources

Anonymous-source claims are confidence-capped unless supported by stronger evidence.

Anonymous claims can be relevant but cannot be self-validating. Product surfaces must disclose when anonymity affects confidence.

Lumen distinguishes at minimum:

- anonymous official;
- anonymous eyewitness;
- anonymous expert;
- unnamed institutional source;
- leaked document;
- unsupported anonymous assertion.

---

## Article IX — Narrative Analysis

Narrative analysis must be labeled as analysis, not fact.

Lumen may identify framing patterns such as hero, villain, victim, threat, solution, emotional language, omitted context, implied causality, beneficiary, and repeated phrasing.

The presence of framing does not prove deception. Lumen's role is to make framing visible, not to pathologize communication.

---

## Article X — Bias Resistance

Lumen cannot guarantee perfect neutrality. Bias resistance comes from process, not self-declaration.

The process must include:

- public methodology;
- transparent scoring rules;
- visible uncertainty;
- adversarial review;
- diverse source comparison;
- primary-source preference;
- challenge mechanisms;
- reproducible outputs where possible;
- forkability.

Lumen must apply the same methodological scrutiny to governments, media organizations, corporations, NGOs, activists, influencers, opposition movements, and independent creators.

---

## Article XI — Auditability

Every meaningful transformation must be auditable.

This includes ingestion, parsing, extraction, normalization, scoring, evidence matching, contradiction detection, narrative analysis, briefing generation, human intervention, and governance-rule changes.

Audit trails must be:

- append-only in normal operation;
- tamper-evident;
- inspectable by users;
- linked to rule versions;
- sufficient to explain how an output was produced.

---

## Article XII — Reproducibility

Where technically possible, the same inputs, code version, rule version, model version, prompt version, and fixture set should produce the same output.

Non-deterministic components must be labeled. MVP v0.2 is local and deterministic: no paid APIs, no live ingestion, no hidden services, no telemetry, and no LLM calls.

---

## Article XIII — Governance Changes

Governance changes must be public, documented, justified, versioned, reviewable, and reversible where possible.

Changes to scoring rules, confidence caps, source weighting, narrative analysis, limitation disclosures, or audit behavior must not be silent.

---

## Article XIV — Limitations

Lumen must disclose limitations plainly and close to outputs.

Known limitation categories include incomplete source coverage, extraction errors, translation errors, missing primary evidence, source metadata gaps, ambiguous claims, evolving events, adversarial manipulation, false equivalence risk, overconfidence risk, and interface-induced false legitimacy.

Limitations must not be hidden for marketing purposes.

---

## Article XV — Public Service and Open Source

Lumen must remain free and open source.

The project may accept donations, grants, sponsorship, infrastructure support, hosting support, consulting, education, or implementation services only when those relationships do not compromise public access, governance independence, scoring transparency, auditability, or methodological neutrality.

Lumen must not sell privileged conclusions or hidden intelligence outputs unavailable to the public version.

---

## Article XVI — Contribution Standards

Contributions should be rejected when they introduce hidden scoring, ideological weighting, fake capability claims, opaque manipulation, undisclosed dependencies, unverifiable claims, or product copy that overstates confidence.

Every feature should answer:

- Does this improve evidence visibility?
- Does this improve claim clarity?
- Does this improve uncertainty handling?
- Does this improve auditability?
- Does this improve human reasoning?

If not, it is probably not core.

---

## Article XVII — MVP Restraint

The MVP may demonstrate claim extraction placeholders, sample evidence trails, simple confidence logic, narrative mapping, a hash-chained audit ledger, static briefings, source-dependency flags, and contradiction fixtures.

The MVP must not claim real-world verification completeness, propaganda immunity, perfect neutrality, objective conclusion generation, production intelligence reliability, or live event coverage.

---

## Final Principle

More informed humans. Not a new oracle.

This principle overrides product hype, political pressure, contributor ideology, user demand, institutional influence, and interface polish.
