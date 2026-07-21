# VEF Testing Strategy

Status: release requirement

Every observable behavior must be testable without a socket or wall clock.
Protocol engines accept bytes, commands, capacities, and injected time, making
tests deterministic and portable.

Each feature requires, as applicable:

- constructor and domain-boundary unit tests;
- positive and negative syntax tests;
- truncation at every byte boundary;
- delivery split at every byte boundary and selected multi-split sequences;
- serializer round-trip and canonical-output properties;
- arbitrary-input no-panic and bounded-work properties;
- role and state-transition tables, including invalid transitions;
- capacity exhaustion before mutation and recovery after backpressure;
- regression cases for every fixed defect;
- adversarial smuggling, cross-protocol, decompression, flow-control, stream
  churn, control-flood, and response-amplification corpora;
- differential and interoperability evidence against independent peers;
- fuzz targets from the first hostile-input implementation milestone;
- formal checks for small arithmetic/state domains where they add assurance.

Test count is not a quality ceiling. A release stops whenever a behavior lacks
an observable deterministic oracle.
