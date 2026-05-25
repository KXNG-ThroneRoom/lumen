# Lumen Adversarial Review Process

Version: v0.5-public-framing

## Purpose

Adversarial review protects Lumen from hidden bias, false certainty, source laundering, overclaiming, and interface-induced authority.

The goal is not to win arguments. The goal is to make methods inspectable and improve user reasoning.

This process is the public challenge path for Lumen governance, confidence scoring, limitation disclosure, audit completeness, and user-interface wording. Governance and demo documentation should link here when describing how users can contest an output, rule, or public framing choice.

Adversarial review does not turn Lumen into an arbiter of truth. It is a documented way to challenge whether Lumen exposed methods, evidence, uncertainty, provenance, limitations, and audit references honestly.

## What Can Be Challenged

Reviewers may challenge:

- claim extraction boundaries;
- status assignment;
- confidence band or reason;
- anonymous-source cap application;
- source-independence assessment;
- contradiction handling;
- limitation disclosure;
- audit completeness;
- UI wording that implies excessive certainty;
- governance rule changes.

## Challenge Packet

A useful challenge should include:

- challenged output or rule;
- exact claim or UI text;
- alleged failure mode;
- evidence or reasoning for the challenge;
- affected governance rule;
- proposed correction;
- severity: low, medium, high, blocking;
- reproducibility notes;
- audit reference where available.

## Review Questions

Reviewers should ask:

- Is the claim atomic enough?
- Is the source original or dependent?
- Is article volume being mistaken for independence?
- Is anonymous sourcing capped correctly?
- Is primary evidence relevant and adequately sourced?
- Are contradictions exposed rather than hidden?
- Are unknown, unresolved, and contested states preserved?
- Does the interface overstate certainty?
- Can the audit trail explain the output?

## Red-Team Cases

MVP adversarial cases should include:

- many articles from one wire origin;
- anonymous claim repeated by dependent outlets;
- official statement with incentive conflict;
- primary document contradicting a headline;
- old image presented as current;
- missing denominator in a statistic;
- ambiguous quote attribution;
- hostile sources agreeing on one narrow fact;
- unresolved claim with insufficient evidence;
- emotionally strong wording with weak evidence.
- current-demo copy that implies live coverage, production authority, or final verdicts.

## Resolution States

Challenges may resolve as:

- accepted: output/rule should change;
- partially accepted: narrower change required;
- rejected with reason: current rule stands;
- deferred: requires data or capability outside MVP;
- needs human decision: governance tradeoff unresolved.

## Documentation

Accepted and partially accepted challenges should update the relevant governance docs, tests/evals, and audit notes. If a challenge concerns public-demo wording, the correction should preserve the v0.5 boundary: controlled local fixture, simplified UI, no live claim-verification promise, and no final authority language.

Governance changes must be public and versioned. Silent scoring or disclosure changes are prohibited.

Contributor onboarding should direct reviewers here before changing public wording, confidence rules, limitation placement, audit requirements, or demo capability claims.
