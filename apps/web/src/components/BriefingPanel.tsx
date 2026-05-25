import type { Briefing } from '../lib/api-contract';
import { briefingCanRender } from '../lib/api-contract';

export function BriefingPanel({
  briefing,
  limitationsReference,
}: {
  briefing: Briefing;
  limitationsReference: string;
}) {
  if (!briefingCanRender(briefing, limitationsReference)) {
    return (
      <section className="panel briefing-panel" aria-labelledby="briefing-heading">
        <div className="panel-kicker">Briefing panel</div>
        <h2 id="briefing-heading">Briefing withheld by uncertainty guard</h2>
        <p>Limitations reference, briefing limitations, confidence reasons, and audit reference are required before a briefing can render.</p>
      </section>
    );
  }

  return (
    <section className="panel briefing-panel" aria-labelledby="briefing-heading">
      <div className="panel-kicker">Briefing panel</div>
      <h2 id="briefing-heading">{briefing.topic}</h2>
      <p className="bottom-line">{briefing.bottom_line}</p>
      <div className="confidence-strip">
        <span>Confidence method signal</span>
        <strong>{Math.round(briefing.confidence.score * 100)}% / {briefing.confidence.status.replaceAll('_', ' ')}</strong>
      </div>
      <div className="reason-list" aria-label="Briefing confidence reasons">
        {briefing.confidence.reasons.map((reason) => (
          <span key={reason}>{reason}</span>
        ))}
      </div>
      <div className="two-col-list">
        <div>
          <h3>Missing information</h3>
          <ul>
            {briefing.missing_information.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
        <div>
          <h3>Unresolved questions</h3>
          <ul>
            {briefing.unresolved_questions.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      </div>
      <div className="two-col-list">
        <div>
          <h3>Watch indicators</h3>
          <ul>
            {briefing.watch_indicators.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
        <div>
          <h3>Limitations displayed with briefing</h3>
          <ul>
            {briefing.limitations.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      </div>
      <p>Limitations reference: {limitationsReference}. Audit reference: {briefing.audit_reference}.</p>
    </section>
  );
}
