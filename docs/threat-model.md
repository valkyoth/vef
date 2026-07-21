# VEF Threat Model

Status: foundation threat model

## Assets

- One correct message-boundary and routing interpretation.
- Correct connection, stream, transition, and flow-control state.
- Availability under adversarial fragmentation and control-frame traffic.
- Confidential fields protected from compression-policy misuse and logging.
- Release, standards, test, and supply-chain evidence integrity.

## Adversaries

- Remote clients, servers, and peers supplying arbitrary bytes and timing.
- Confused or inconsistent proxy chains attempting different interpretations.
- Attackers using oversized values, deep fragmentation, floods, compression
  bombs, stream churn, or response amplification.
- Compromised dependency, tool, source, CI, or release infrastructure.
- Incorrect adapters supplying stale time, TLS, identity, or transport state.

## Trust boundaries

- Bytes to syntactically validated protocol structures.
- Syntax to role-aware semantic and framing decisions.
- HPACK bytes to bounded decoded fields and synchronized compression state.
- Frames to connection/stream state and application-visible events.
- Protocol transition requests to confirmed tunnel/upgrade ownership.
- Protocol commands/events to runtime, TLS, and application adapters.
- Immutable standards text to extracted requirement decisions.

## Baseline controls

- Dependency-free `no_std` protocol crates with unsafe Rust forbidden.
- Checked arithmetic and bounds-checked access on untrusted values.
- Immutable limits and explicit work/output budgets.
- Deterministic structured errors and progress contracts.
- Complete field validation before application visibility.
- Explicit role and transition state.
- RFC checksum locks, requirement traceability, adversarial tests, fuzzing,
  model checking where useful, exact-commit pentests, and independent final
  audit.

## Residual risks

`no_std`, safe Rust, fuzzing, and formal checks do not prove protocol
correctness. Caller-provided storage can still be undersized or mismanaged;
adapters can violate contracts; deployment limits can be inappropriate; and
interoperability peers can contain distinct bugs. These are contained through
typed contracts, deterministic failure, documentation, and integration tests,
not claimed away.
