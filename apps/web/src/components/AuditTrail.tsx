import type { AuditEvent, AuditVerification } from '../lib/api-contract';

export function AuditTrail({ events, verification }: { events: AuditEvent[]; verification: AuditVerification }) {
  return (
    <section className="panel" aria-labelledby="audit-heading">
      <div className="panel-kicker">Audit trail</div>
      <h2 id="audit-heading">Append-only hash-chain design preview</h2>
      <p>
        Verification: {verification.valid ? 'valid fixture chain' : 'invalid fixture chain'}; events checked: {verification.event_count}; latest hash:{' '}
        {verification.latest_event_hash ?? 'missing'}. The audit trail records method path and detects inconsistent transformation history; it does not
        prove the underlying claim.
      </p>
      <ol className="audit-list">
        {events.map((event) => (
          <li className="audit-event" key={event.event_id}>
            <div className="audit-head">
              <span>{event.event_id}</span>
              <strong>{event.operation}</strong>
            </div>
            <p>{event.reason}</p>
            <code>input {event.input_hash}</code>
            <code>output {event.output_hash}</code>
            <code>previous {event.previous_event_hash}</code>
            <code>event {event.event_hash}</code>
            <span className="rule-version">{event.rule_version} / {event.actor_type}:{event.actor_id}</span>
          </li>
        ))}
      </ol>
    </section>
  );
}
