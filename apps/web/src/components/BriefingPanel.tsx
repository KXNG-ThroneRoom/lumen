type Briefing = {
  topic: string;
  bottomLine: string;
  confidence: string;
  watchIndicators: string[];
  unresolvedQuestions: string[];
};

export function BriefingPanel({
  briefing,
  limitationsReference,
  auditReference,
}: {
  briefing: Briefing;
  limitationsReference: string;
  auditReference: string;
}) {
  if (!limitationsReference || !auditReference) {
    return (
      <section className="panel briefing-panel" aria-labelledby="briefing-heading">
        <div className="panel-kicker">Briefing panel</div>
        <h2 id="briefing-heading">Briefing withheld by uncertainty guard</h2>
        <p>Limitations reference and audit reference are required before a briefing can be rendered.</p>
      </section>
    );
  }

  return (
    <section className="panel briefing-panel" aria-labelledby="briefing-heading">
      <div className="panel-kicker">Briefing panel</div>
      <h2 id="briefing-heading">{briefing.topic}</h2>
      <p className="bottom-line">{briefing.bottomLine}</p>
      <div className="confidence-strip">
        <span>Confidence</span>
        <strong>{briefing.confidence}</strong>
      </div>
      <div className="two-col-list">
        <div>
          <h3>Watch indicators</h3>
          <ul>
            {briefing.watchIndicators.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
        <div>
          <h3>Unresolved questions</h3>
          <ul>
            {briefing.unresolvedQuestions.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      </div>
      <p>
        Limitations reference: {limitationsReference}. Audit reference: {auditReference}.
      </p>
    </section>
  );
}
