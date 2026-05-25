'use client';

import { useState } from 'react';
import demoResponseJson from '../data/demo-response.json';
import type { AnalysisResponse } from '../lib/api-contract';

const demoResponse = demoResponseJson as AnalysisResponse;

type ViewId = 'story' | 'evidence' | 'uncertain' | 'audit';
type Tone = 'good' | 'bad' | 'middle';

const views: Array<{ id: ViewId; label: string }> = [
  { id: 'story', label: 'Story' },
  { id: 'evidence', label: 'Evidence' },
  { id: 'uncertain', label: 'Why uncertain' },
  { id: 'audit', label: 'Audit' },
];

const confidencePercent = Math.round(demoResponse.briefing.confidence.score * 100);
const officialRecord = demoResponse.evidence.find((item) => item.primary);
const newsReport = demoResponse.evidence.find((item) => !item.primary);
const sourceCount = demoResponse.source_graph.independent_evidence_streams;
const checkCount = demoResponse.audit_verification.event_count;

const storySteps: Array<{
  tone: Tone;
  title: string;
  note: string;
  detail: string;
}> = [
  {
    tone: 'bad',
    title: 'A news report says June 1.',
    note: 'This is the claim people might repeat first.',
    detail: newsReport?.summary ?? 'A secondary report gives the June 1 date.',
  },
  {
    tone: 'good',
    title: 'The official record says July 1.',
    note: 'This is stronger evidence, but it does not erase the conflict by itself.',
    detail: officialRecord?.summary ?? 'An official record gives the July 1 date.',
  },
  {
    tone: 'middle',
    title: 'The two dates do not match.',
    note: 'Lumen keeps the disagreement visible instead of smoothing it over.',
    detail: demoResponse.contradictions[0]?.summary ?? 'The available sources disagree about the start date.',
  },
  {
    tone: 'middle',
    title: 'No final verdict yet.',
    note: 'The honest answer is contested, not yes or no.',
    detail: 'A stronger follow-up record, correction, or human review could change the answer later.',
  },
];

const evidenceCards: Array<{
  tone: Tone;
  label: string;
  title: string;
  body: string;
  detail: string;
}> = [
  {
    tone: 'good',
    label: 'Strongest source',
    title: 'Official record',
    body: 'Supports July 1.',
    detail: 'This carries more weight because it comes from the record itself, not from commentary about it.',
  },
  {
    tone: 'bad',
    label: 'Conflicting source',
    title: 'News report',
    body: 'Says June 1.',
    detail: 'This is still useful, but it conflicts with the official record and needs follow-up.',
  },
  {
    tone: 'middle',
    label: 'Source check',
    title: `${sourceCount} separate evidence streams`,
    body: 'More coverage is not the same thing as more proof.',
    detail: 'Repeated articles can come from the same original report. Lumen separates quantity from actual independence.',
  },
];

function toneLabel(tone: Tone) {
  if (tone === 'good') return 'supporting';
  if (tone === 'bad') return 'conflict';
  return 'uncertain';
}

export default function Home() {
  const [activeView, setActiveView] = useState<ViewId>('story');
  const [manualAssertion, setManualAssertion] = useState('');
  const trimmedManualAssertion = manualAssertion.trim();

  return (
    <main className="app-shell">
      <div className="demo-frame">
        <header className="claim-hero">
          <div className="top-line">
            <span>Lumen local demo</span>
            <span>v0.6 local/manual only</span>
            <span>Methods over conclusions</span>
          </div>

          <p className="section-label">Main claim</p>
          <h1>When does the regulation start?</h1>
          <p className="claim-summary">
            Two sources disagree. A news report says June 1. An official filing says July 1. Lumen marks this as contested
            instead of guessing.
          </p>

          <div className="signal-row" aria-label="Claim status summary">
            <div className="signal signal-middle">
              <span>Current answer</span>
              <strong>Contested</strong>
            </div>
            <div className="signal signal-good">
              <span>Best support</span>
              <strong>Official record</strong>
            </div>
            <div className="signal signal-bad">
              <span>Main problem</span>
              <strong>Dates conflict</strong>
            </div>
          </div>

          <section className="manual-input-card" aria-labelledby="manual-input-heading">
            <div>
              <p className="section-label">Manual input area</p>
              <h2 id="manual-input-heading">Local assertion container</h2>
              <p>
                Paste a sentence here to stage it locally as something to inspect later. It is an assertion container, not a verified fact,
                it does not submit anywhere, and it does not change the demo answer.
              </p>
            </div>
            <label className="manual-input-label" htmlFor="manual-assertion">
              Local text to inspect
            </label>
            <textarea
              id="manual-assertion"
              value={manualAssertion}
              onChange={(event) => setManualAssertion(event.target.value)}
              placeholder="Example: A report says the regulation starts June 1."
              rows={4}
              maxLength={1200}
            />
            <div className="manual-preview" aria-live="polite">
              <strong>{trimmedManualAssertion ? 'Staged locally' : 'Waiting for local text'}</strong>
              <p>
                {trimmedManualAssertion
                  ? `A manual assertion is staged locally (${manualAssertion.length}/1200 characters). The text stays hidden in this summary until a reviewer chooses evidence to inspect.`
                  : 'Nothing has been staged. Keep it local until a reviewer chooses what evidence to inspect.'}
              </p>
            </div>
          </section>
        </header>

        <nav className="view-tabs" aria-label="Lumen demo sections">
          {views.map((view) => (
            <button
              key={view.id}
              type="button"
              className={activeView === view.id ? 'tab-button active' : 'tab-button'}
              aria-pressed={activeView === view.id}
              onClick={() => setActiveView(view.id)}
            >
              {view.label}
            </button>
          ))}
        </nav>

        <section className="view-panel" aria-live="polite">
          {activeView === 'story' && (
            <div className="story-view">
              <div className="view-heading">
                <p className="section-label">Chronological breakdown</p>
                <h2>What happened, in order</h2>
              </div>

              <ol className="timeline">
                {storySteps.map((step, index) => (
                  <li key={step.title} className={`timeline-step tone-${step.tone}`}>
                    <span className="step-number">{index + 1}</span>
                    <div>
                      <h3>{step.title}</h3>
                      <p>{step.note}</p>
                      <details>
                        <summary>More context</summary>
                        <p>{step.detail}</p>
                      </details>
                    </div>
                  </li>
                ))}
              </ol>
            </div>
          )}

          {activeView === 'evidence' && (
            <div className="evidence-view">
              <div className="view-heading">
                <p className="section-label">What Lumen looked at</p>
                <h2>Two sources, one disagreement</h2>
              </div>

              <div className="evidence-list">
                {evidenceCards.map((card) => (
                  <article key={card.title} className={`simple-card tone-${card.tone}`}>
                    <div className="card-topline">
                      <span>{card.label}</span>
                      <small>{toneLabel(card.tone)}</small>
                    </div>
                    <h3>{card.title}</h3>
                    <p>{card.body}</p>
                    <details>
                      <summary>Why this matters</summary>
                      <p>{card.detail}</p>
                    </details>
                  </article>
                ))}
              </div>
            </div>
          )}

          {activeView === 'uncertain' && (
            <div className="uncertain-view">
              <div className="view-heading">
                <p className="section-label">Why Lumen will not decide yet</p>
                <h2>No final verdict</h2>
              </div>

              <div className="plain-stack">
                <p>
                  The official record is stronger, but the public claim still conflicts with it. Lumen shows that tension
                  instead of pretending the issue is settled.
                </p>
                <ul className="plain-list">
                  <li>What we know: one source says June 1, one official record says July 1.</li>
                  <li>What we do not know: whether the report was wrong, outdated, or missing context.</li>
                  <li>What would help: a correction, a newer official record, or a human source review.</li>
                </ul>
              </div>
            </div>
          )}

          {activeView === 'audit' && (
            <div className="audit-view">
              <div className="view-heading">
                <p className="section-label">Behind the scenes</p>
                <h2>Checked, but not overclaimed</h2>
              </div>

              <div className="audit-grid">
                <article className="simple-card tone-good">
                  <h3>Data loaded</h3>
                  <p>The page is using the same local sample as the backend.</p>
                </article>
                <article className="simple-card tone-middle">
                  <h3>{confidencePercent}% method signal</h3>
                  <p>This is a caution flag, not a truth score.</p>
                </article>
                <article className="simple-card tone-middle">
                  <h3>{checkCount} checks recorded</h3>
                  <p>Technical tracking exists, but raw internal labels are hidden from this view.</p>
                </article>
              </div>

              <details className="wide-detail">
                <summary>What is intentionally hidden?</summary>
                <p>
                  Internal fingerprints, file references, and machine labels stay out of the main UI. They are useful for
                  developers, but they make the claim harder for normal readers to understand.
                </p>
              </details>
            </div>
          )}
        </section>

        <footer className="demo-note">
          Controlled local demo only. It accepts local/manual inputs as assertions, not facts. It does not read live
          news, declare truth, or replace human judgment.
        </footer>
      </div>
    </main>
  );
}
