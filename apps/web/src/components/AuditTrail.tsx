import type { AuditEvent } from '../data/lumenSample';

export function AuditTrail({ events }: { events: AuditEvent[] }) {
  return (
    <section className="panel" aria-labelledby="audit-heading">
      <div className="panel-kicker">Audit trail</div>
      <h2 id="audit-heading">Append-only hash-chain design preview</h2>
      <ol className="audit-list">
        {events.map((event) => (
          <li className="audit-event" key={event.id}>
            <div className="audit-head">
              <span>{event.id}</span>
              <strong>{event.operation}</strong>
            </div>
            <p>{event.note}</p>
            <code>input {event.inputHash}</code>
            <code>output {event.outputHash}</code>
            <code>previous {event.previousHash}</code>
            <span className="rule-version">{event.ruleVersion} / {event.actor}</span>
          </li>
        ))}
      </ol>
    </section>
  );
}
