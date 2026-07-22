# VEF Release Plan to 1.0

Status: planning document

This is the authoritative implementation sequence. VEF processes
attacker-controlled traffic, so every milestone has one primary capability and
an acceptance boundary that can be implemented, reviewed, tested, pentested,
and stopped independently. Split work into patch releases whenever a security
argument no longer fits one review pass.

## Release principles

Every release requires applicable RFC and errata evidence, explicit
non-applicability decisions, bounded-resource behavior, positive and negative
tests, relevant fragmentation coverage, adversarial and regression evidence,
documentation, release notes, portability evidence, dependency-policy proof, a
clean SBOM, full-SHA CI pins, CodeQL default-setup review, and an exact-commit
pentest. Tests cover the new outcome and prior behavior, never future features.

Protocol and I/O-contract crates remain `no_std`, safe Rust, and free of
third-party Rust crates. Tool-only fuzzers, model checkers, and interoperability
peers do not enter the production dependency graph.

## Rules binding every milestone

- A profile is compliant only when every applicable MUST/MUST NOT is verified,
  every SHOULD decision is recorded, verified/held errata are dispositioned,
  and deviations or non-applicability decisions are explicit.
- Incremental calls consume input, produce output, emit an event, commit a
  transition, or return a typed blocked condition. Success never reports zero
  progress.
- Peer-controlled sizes and work use checked reserve/commit/refund accounting.
- Parsing and semantic validation withhold application publication until the
  relevant barrier passes. State changes use typed deltas where rollback is
  legal.
- HPACK is special: valid compression-state updates remain committed even when
  later HTTP semantic validation rejects a stream. Unsafe incomplete decoding
  is connection-fatal.
- Reusable slots carry generations. Borrowed events are acknowledged before
  backing storage is recycled.
- Every source file stays below 500 lines.
- Fuzz and model harnesses begin with each hostile surface; final campaigns
  replay and expand them rather than creating them for the first time.

## Pentest flow

At each implementation stop, do not tag. Pentest the exact commit, remediate
findings with regression tests, repeat all gates, then add the permanent passing
report as the only file in the direct child of the reviewed commit. Critical or
high findings block release. Phase exits add full-repository manual review,
stateful fuzzing, corpus minimization, multi-peer interoperability,
resource-exhaustion assessment, and conformance-decision review.

## Phase 1 — Foundation and shared semantics

Phase contract: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.

### v0.1.0 — Workspace, crate boundaries, licenses, security policy, and release evidence

Status: foundation implementation in progress

#### Goal

Deliver **Workspace, crate boundaries, licenses, security policy, and release evidence** as the sole primary capability in this stop. It builds
on the repository foundation and must be independently trustworthy before v0.2.0 (Core module skeleton and authority boundaries) begins.

#### Deliverables

- Acceptance contract: Expose Workspace, crate boundaries, licenses, security policy, and release evidence with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Workspace, crate boundaries, licenses, security policy, and release evidence and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Workspace, crate boundaries, licenses, security policy, and release evidence contract and all previously implemented relevant behavior have
reproducible evidence; the repository foundation still passes; no behavior assigned to v0.2.0 (Core module skeleton and authority boundaries) is
claimed; and no critical or high finding remains open.

`0.1.0 implementation stop reached. Run pentest for this exact commit.`

### v0.2.0 — Core module skeleton and authority boundaries

Status: planned

#### Goal

Deliver **Core module skeleton and authority boundaries** as the sole primary capability in this stop. It builds
on v0.1.0 (Workspace, crate boundaries, licenses, security policy, and release evidence) and must be independently trustworthy before v0.3.0 (Checked byte cursor with no unchecked indexing) begins.

#### Deliverables

- Acceptance contract: Expose Core module skeleton and authority boundaries with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Core module skeleton and authority boundaries and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Core module skeleton and authority boundaries contract and all previously implemented relevant behavior have
reproducible evidence; v0.1.0 (Workspace, crate boundaries, licenses, security policy, and release evidence) still passes; no behavior assigned to v0.3.0 (Checked byte cursor with no unchecked indexing) is
claimed; and no critical or high finding remains open.

`0.2.0 implementation stop reached. Run pentest for this exact commit.`

### v0.3.0 — Checked byte cursor with no unchecked indexing

Status: planned

#### Goal

Deliver **Checked byte cursor with no unchecked indexing** as the sole primary capability in this stop. It builds
on v0.2.0 (Core module skeleton and authority boundaries) and must be independently trustworthy before v0.4.0 (Non-zero parser progress and explicit blocked states) begins.

#### Deliverables

- Acceptance contract: Expose Checked byte cursor with no unchecked indexing with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Checked byte cursor with no unchecked indexing and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked byte cursor with no unchecked indexing contract and all previously implemented relevant behavior have
reproducible evidence; v0.2.0 (Core module skeleton and authority boundaries) still passes; no behavior assigned to v0.4.0 (Non-zero parser progress and explicit blocked states) is
claimed; and no critical or high finding remains open.

`0.3.0 implementation stop reached. Run pentest for this exact commit.`

### v0.4.0 — Non-zero parser progress and explicit blocked states

Status: planned

#### Goal

Deliver **Non-zero parser progress and explicit blocked states** as the sole primary capability in this stop. It builds
on v0.3.0 (Checked byte cursor with no unchecked indexing) and must be independently trustworthy before v0.5.0 (Checked protocol-size domains) begins.

#### Deliverables

- Acceptance contract: Represent successful byte advancement with a non-zero type or checked constructor and distinguish input, output, event, transition, NeedInput, NeedOutput, and CapacityExceeded outcomes.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Non-zero parser progress and explicit blocked states and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Non-zero parser progress and explicit blocked states contract and all previously implemented relevant behavior have
reproducible evidence; v0.3.0 (Checked byte cursor with no unchecked indexing) still passes; no behavior assigned to v0.5.0 (Checked protocol-size domains) is
claimed; and no critical or high finding remains open.

`0.4.0 implementation stop reached. Run pentest for this exact commit.`

### v0.5.0 — Checked protocol-size domains

Status: planned

#### Goal

Deliver **Checked protocol-size domains** as the sole primary capability in this stop. It builds
on v0.4.0 (Non-zero parser progress and explicit blocked states) and must be independently trustworthy before v0.6.0 (Decode, work, transition, and response budgets) begins.

#### Deliverables

- Acceptance contract: Expose Checked protocol-size domains with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Checked protocol-size domains and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked protocol-size domains contract and all previously implemented relevant behavior have
reproducible evidence; v0.4.0 (Non-zero parser progress and explicit blocked states) still passes; no behavior assigned to v0.6.0 (Decode, work, transition, and response budgets) is
claimed; and no critical or high finding remains open.

`0.5.0 implementation stop reached. Run pentest for this exact commit.`

### v0.6.0 — Decode, work, transition, and response budgets

Status: planned

#### Goal

Deliver **Decode, work, transition, and response budgets** as the sole primary capability in this stop. It builds
on v0.5.0 (Checked protocol-size domains) and must be independently trustworthy before v0.7.0 (Caller-owned arenas and fixed-capacity stores) begins.

#### Deliverables

- Acceptance contract: Expose Decode, work, transition, and response budgets with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Decode, work, transition, and response budgets and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Decode, work, transition, and response budgets contract and all previously implemented relevant behavior have
reproducible evidence; v0.5.0 (Checked protocol-size domains) still passes; no behavior assigned to v0.7.0 (Caller-owned arenas and fixed-capacity stores) is
claimed; and no critical or high finding remains open.

`0.6.0 implementation stop reached. Run pentest for this exact commit.`

### v0.7.0 — Caller-owned arenas and fixed-capacity stores

Status: planned

#### Goal

Deliver **Caller-owned arenas and fixed-capacity stores** as the sole primary capability in this stop. It builds
on v0.6.0 (Decode, work, transition, and response budgets) and must be independently trustworthy before v0.8.0 (Structured errors and error-scope taxonomy) begins.

#### Deliverables

- Acceptance contract: Define fixed stores, borrowed views, generation-safe recycling, explicit capacity failures, and no hidden growth before any complete protocol parser.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Caller-owned arenas and fixed-capacity stores and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Caller-owned arenas and fixed-capacity stores contract and all previously implemented relevant behavior have
reproducible evidence; v0.6.0 (Decode, work, transition, and response budgets) still passes; no behavior assigned to v0.8.0 (Structured errors and error-scope taxonomy) is
claimed; and no critical or high finding remains open.

`0.7.0 implementation stop reached. Run pentest for this exact commit.`

### v0.8.0 — Structured errors and error-scope taxonomy

Status: planned

#### Goal

Deliver **Structured errors and error-scope taxonomy** as the sole primary capability in this stop. It builds
on v0.7.0 (Caller-owned arenas and fixed-capacity stores) and must be independently trustworthy before v0.9.0 (Case-sensitive extension-capable Method) begins.

#### Deliverables

- Acceptance contract: Separate syntax, policy, capacity, transport, connection, stream, and application errors so adapters cannot mistake a fatal condition for a recoverable one.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Structured errors and error-scope taxonomy and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured errors and error-scope taxonomy contract and all previously implemented relevant behavior have
reproducible evidence; v0.7.0 (Caller-owned arenas and fixed-capacity stores) still passes; no behavior assigned to v0.9.0 (Case-sensitive extension-capable Method) is
claimed; and no critical or high finding remains open.

`0.8.0 implementation stop reached. Run pentest for this exact commit.`

### v0.9.0 — Case-sensitive extension-capable Method

Status: planned

#### Goal

Deliver **Case-sensitive extension-capable Method** as the sole primary capability in this stop. It builds
on v0.8.0 (Structured errors and error-scope taxonomy) and must be independently trustworthy before v0.10.0 (Validated StatusCode with unknown-code preservation) begins.

#### Deliverables

- Acceptance contract: Expose Case-sensitive extension-capable Method with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Case-sensitive extension-capable Method and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Case-sensitive extension-capable Method contract and all previously implemented relevant behavior have
reproducible evidence; v0.8.0 (Structured errors and error-scope taxonomy) still passes; no behavior assigned to v0.10.0 (Validated StatusCode with unknown-code preservation) is
claimed; and no critical or high finding remains open.

`0.9.0 implementation stop reached. Run pentest for this exact commit.`

### v0.10.0 — Validated StatusCode with unknown-code preservation

Status: planned

#### Goal

Deliver **Validated StatusCode with unknown-code preservation** as the sole primary capability in this stop. It builds
on v0.9.0 (Case-sensitive extension-capable Method) and must be independently trustworthy before v0.11.0 (HTTP version and wire-version representation) begins.

#### Deliverables

- Acceptance contract: Expose Validated StatusCode with unknown-code preservation with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Validated StatusCode with unknown-code preservation and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Validated StatusCode with unknown-code preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.9.0 (Case-sensitive extension-capable Method) still passes; no behavior assigned to v0.11.0 (HTTP version and wire-version representation) is
claimed; and no critical or high finding remains open.

`0.10.0 implementation stop reached. Run pentest for this exact commit.`

### v0.11.0 — HTTP version and wire-version representation

Status: planned

#### Goal

Deliver **HTTP version and wire-version representation** as the sole primary capability in this stop. It builds
on v0.10.0 (Validated StatusCode with unknown-code preservation) and must be independently trustworthy before v0.12.0 (Case-insensitive validated FieldName) begins.

#### Deliverables

- Acceptance contract: Expose HTTP version and wire-version representation with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP version and wire-version representation and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP version and wire-version representation contract and all previously implemented relevant behavior have
reproducible evidence; v0.10.0 (Validated StatusCode with unknown-code preservation) still passes; no behavior assigned to v0.12.0 (Case-insensitive validated FieldName) is
claimed; and no critical or high finding remains open.

`0.11.0 implementation stop reached. Run pentest for this exact commit.`

### v0.12.0 — Case-insensitive validated FieldName

Status: planned

#### Goal

Deliver **Case-insensitive validated FieldName** as the sole primary capability in this stop. It builds
on v0.11.0 (HTTP version and wire-version representation) and must be independently trustworthy before v0.13.0 (Byte-oriented FieldValue with raw and semantic views) begins.

#### Deliverables

- Acceptance contract: Expose Case-insensitive validated FieldName with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Case-insensitive validated FieldName and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Case-insensitive validated FieldName contract and all previously implemented relevant behavior have
reproducible evidence; v0.11.0 (HTTP version and wire-version representation) still passes; no behavior assigned to v0.13.0 (Byte-oriented FieldValue with raw and semantic views) is
claimed; and no critical or high finding remains open.

`0.12.0 implementation stop reached. Run pentest for this exact commit.`

### v0.13.0 — Byte-oriented FieldValue with raw and semantic views

Status: planned

#### Goal

Deliver **Byte-oriented FieldValue with raw and semantic views** as the sole primary capability in this stop. It builds
on v0.12.0 (Case-insensitive validated FieldName) and must be independently trustworthy before v0.14.0 (Ordered FieldLine and FieldSection storage) begins.

#### Deliverables

- Acceptance contract: Expose Byte-oriented FieldValue with raw and semantic views with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Byte-oriented FieldValue with raw and semantic views and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Byte-oriented FieldValue with raw and semantic views contract and all previously implemented relevant behavior have
reproducible evidence; v0.12.0 (Case-insensitive validated FieldName) still passes; no behavior assigned to v0.14.0 (Ordered FieldLine and FieldSection storage) is
claimed; and no critical or high finding remains open.

`0.13.0 implementation stop reached. Run pentest for this exact commit.`

### v0.14.0 — Ordered FieldLine and FieldSection storage

Status: planned

#### Goal

Deliver **Ordered FieldLine and FieldSection storage** as the sole primary capability in this stop. It builds
on v0.13.0 (Byte-oriented FieldValue with raw and semantic views) and must be independently trustworthy before v0.15.0 (Request-target, URI, and authority types) begins.

#### Deliverables

- Acceptance contract: Expose Ordered FieldLine and FieldSection storage with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Ordered FieldLine and FieldSection storage and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Ordered FieldLine and FieldSection storage contract and all previously implemented relevant behavior have
reproducible evidence; v0.13.0 (Byte-oriented FieldValue with raw and semantic views) still passes; no behavior assigned to v0.15.0 (Request-target, URI, and authority types) is
claimed; and no critical or high finding remains open.

`0.14.0 implementation stop reached. Run pentest for this exact commit.`

### v0.15.0 — Request-target, URI, and authority types

Status: planned

#### Goal

Deliver **Request-target, URI, and authority types** as the sole primary capability in this stop. It builds
on v0.14.0 (Ordered FieldLine and FieldSection storage) and must be independently trustworthy before v0.16.0 (Request and response control-data types) begins.

#### Deliverables

- Acceptance contract: Expose Request-target, URI, and authority types with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Request-target, URI, and authority types and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Request-target, URI, and authority types contract and all previously implemented relevant behavior have
reproducible evidence; v0.14.0 (Ordered FieldLine and FieldSection storage) still passes; no behavior assigned to v0.16.0 (Request and response control-data types) is
claimed; and no critical or high finding remains open.

`0.15.0 implementation stop reached. Run pentest for this exact commit.`

### v0.16.0 — Request and response control-data types

Status: planned

#### Goal

Deliver **Request and response control-data types** as the sole primary capability in this stop. It builds
on v0.15.0 (Request-target, URI, and authority types) and must be independently trustworthy before v0.17.0 (Role, profile, and policy types) begins.

#### Deliverables

- Acceptance contract: Expose Request and response control-data types with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Request and response control-data types and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Request and response control-data types contract and all previously implemented relevant behavior have
reproducible evidence; v0.15.0 (Request-target, URI, and authority types) still passes; no behavior assigned to v0.17.0 (Role, profile, and policy types) is
claimed; and no critical or high finding remains open.

`0.16.0 implementation stop reached. Run pentest for this exact commit.`

### v0.17.0 — Role, profile, and policy types

Status: planned

#### Goal

Deliver **Role, profile, and policy types** as the sole primary capability in this stop. It builds
on v0.16.0 (Request and response control-data types) and must be independently trustworthy before v0.18.0 (Minimal synchronous I/O contracts) begins.

#### Deliverables

- Acceptance contract: Expose Role, profile, and policy types with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Role, profile, and policy types and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Role, profile, and policy types contract and all previously implemented relevant behavior have
reproducible evidence; v0.16.0 (Request and response control-data types) still passes; no behavior assigned to v0.18.0 (Minimal synchronous I/O contracts) is
claimed; and no critical or high finding remains open.

`0.17.0 implementation stop reached. Run pentest for this exact commit.`

### v0.18.0 — Minimal synchronous I/O contracts

Status: planned

#### Goal

Deliver **Minimal synchronous I/O contracts** as the sole primary capability in this stop. It builds
on v0.17.0 (Role, profile, and policy types) and must be independently trustworthy before v0.19.0 (Runtime-neutral readiness and poll contracts) begins.

#### Deliverables

- Acceptance contract: Expose Minimal synchronous I/O contracts with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Minimal synchronous I/O contracts and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Minimal synchronous I/O contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.17.0 (Role, profile, and policy types) still passes; no behavior assigned to v0.19.0 (Runtime-neutral readiness and poll contracts) is
claimed; and no critical or high finding remains open.

`0.18.0 implementation stop reached. Run pentest for this exact commit.`

### v0.19.0 — Runtime-neutral readiness and poll contracts

Status: planned

#### Goal

Deliver **Runtime-neutral readiness and poll contracts** as the sole primary capability in this stop. It builds
on v0.18.0 (Minimal synchronous I/O contracts) and must be independently trustworthy before v0.20.0 (Injected monotonic clock and deadline contracts) begins.

#### Deliverables

- Acceptance contract: Expose Runtime-neutral readiness and poll contracts with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Runtime-neutral readiness and poll contracts and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Runtime-neutral readiness and poll contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.18.0 (Minimal synchronous I/O contracts) still passes; no behavior assigned to v0.20.0 (Injected monotonic clock and deadline contracts) is
claimed; and no critical or high finding remains open.

`0.19.0 implementation stop reached. Run pentest for this exact commit.`

### v0.20.0 — Injected monotonic clock and deadline contracts

Status: planned

#### Goal

Deliver **Injected monotonic clock and deadline contracts** as the sole primary capability in this stop. It builds
on v0.19.0 (Runtime-neutral readiness and poll contracts) and must be independently trustworthy before v0.21.0 (Cancellation, close, and bounded-backpressure contracts) begins.

#### Deliverables

- Acceptance contract: Expose Injected monotonic clock and deadline contracts with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Injected monotonic clock and deadline contracts and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Injected monotonic clock and deadline contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.19.0 (Runtime-neutral readiness and poll contracts) still passes; no behavior assigned to v0.21.0 (Cancellation, close, and bounded-backpressure contracts) is
claimed; and no critical or high finding remains open.

`0.20.0 implementation stop reached. Run pentest for this exact commit.`

### v0.21.0 — Cancellation, close, and bounded-backpressure contracts

Status: planned

#### Goal

Deliver **Cancellation, close, and bounded-backpressure contracts** as the sole primary capability in this stop. It builds
on v0.20.0 (Injected monotonic clock and deadline contracts) and must be independently trustworthy before v0.22.0 (Deterministic fake transport and driver harness) begins.

#### Deliverables

- Acceptance contract: Expose Cancellation, close, and bounded-backpressure contracts with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Cancellation, close, and bounded-backpressure contracts and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Cancellation, close, and bounded-backpressure contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.20.0 (Injected monotonic clock and deadline contracts) still passes; no behavior assigned to v0.22.0 (Deterministic fake transport and driver harness) is
claimed; and no critical or high finding remains open.

`0.21.0 implementation stop reached. Run pentest for this exact commit.`

### v0.22.0 — Deterministic fake transport and driver harness

Status: planned

#### Goal

Deliver **Deterministic fake transport and driver harness** as the sole primary capability in this stop. It builds
on v0.21.0 (Cancellation, close, and bounded-backpressure contracts) and must be independently trustworthy before v0.23.0 (Engine event, command, acknowledgement, and publication contract) begins.

#### Deliverables

- Acceptance contract: Expose Deterministic fake transport and driver harness with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Deterministic fake transport and driver harness and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Deterministic fake transport and driver harness contract and all previously implemented relevant behavior have
reproducible evidence; v0.21.0 (Cancellation, close, and bounded-backpressure contracts) still passes; no behavior assigned to v0.23.0 (Engine event, command, acknowledgement, and publication contract) is
claimed; and no critical or high finding remains open.

`0.22.0 implementation stop reached. Run pentest for this exact commit.`

### v0.23.0 — Engine event, command, acknowledgement, and publication contract

Status: planned

#### Goal

Deliver **Engine event, command, acknowledgement, and publication contract** as the sole primary capability in this stop. It builds
on v0.22.0 (Deterministic fake transport and driver harness) and must be independently trustworthy before v0.24.0 (Requirement, applicability, and errata evidence system) begins.

#### Deliverables

- Acceptance contract: Choose the outstanding-event model; define acknowledgements, command acceptance, reentrancy prohibition, input/output ownership, cancellation aftermath, publication barriers, and capacity reserved for mandatory responses.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Engine event, command, acknowledgement, and publication contract and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Engine event, command, acknowledgement, and publication contract contract and all previously implemented relevant behavior have
reproducible evidence; v0.22.0 (Deterministic fake transport and driver harness) still passes; no behavior assigned to v0.24.0 (Requirement, applicability, and errata evidence system) is
claimed; and no critical or high finding remains open.

`0.23.0 implementation stop reached. Run pentest for this exact commit.`

### v0.24.0 — Requirement, applicability, and errata evidence system

Status: planned

#### Goal

Deliver **Requirement, applicability, and errata evidence system** as the sole primary capability in this stop. It builds
on v0.23.0 (Engine event, command, acknowledgement, and publication contract) and must be independently trustworthy before v0.25.0 (Foundation Kani campaign, audit, and pentest) begins.

#### Deliverables

- Acceptance contract: Expose Requirement, applicability, and errata evidence system with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Requirement, applicability, and errata evidence system and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Requirement, applicability, and errata evidence system contract and all previously implemented relevant behavior have
reproducible evidence; v0.23.0 (Engine event, command, acknowledgement, and publication contract) still passes; no behavior assigned to v0.25.0 (Foundation Kani campaign, audit, and pentest) is
claimed; and no critical or high finding remains open.

`0.24.0 implementation stop reached. Run pentest for this exact commit.`

### v0.25.0 — Foundation Kani campaign, audit, and pentest

Status: planned

#### Goal

Deliver **Foundation Kani campaign, audit, and pentest** as the sole primary capability in this stop. It builds
on v0.24.0 (Requirement, applicability, and errata evidence system) and must be independently trustworthy before v0.26.0 (HTTP/1 role and parser profiles) begins.

#### Deliverables

- Acceptance contract: Expose Foundation Kani campaign, audit, and pentest with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event/command ownership, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Foundation Kani campaign, audit, and pentest and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Foundation Kani campaign, audit, and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.24.0 (Requirement, applicability, and errata evidence system) still passes; no behavior assigned to v0.26.0 (HTTP/1 role and parser profiles) is
claimed; and no critical or high finding remains open.

`0.25.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 2 — HTTP/1 and isolated HTTP/0.9

Phase contract: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.

### v0.26.0 — HTTP/1 role and parser profiles

Status: planned

#### Goal

Deliver **HTTP/1 role and parser profiles** as the sole primary capability in this stop. It builds
on v0.25.0 (Foundation Kani campaign, audit, and pentest) and must be independently trustworthy before v0.27.0 (Incremental HTTP/1 request-line parser) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/1 role and parser profiles with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/1 role and parser profiles and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 role and parser profiles contract and all previously implemented relevant behavior have
reproducible evidence; v0.25.0 (Foundation Kani campaign, audit, and pentest) still passes; no behavior assigned to v0.27.0 (Incremental HTTP/1 request-line parser) is
claimed; and no critical or high finding remains open.

`0.26.0 implementation stop reached. Run pentest for this exact commit.`

### v0.27.0 — Incremental HTTP/1 request-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 request-line parser** as the sole primary capability in this stop. It builds
on v0.26.0 (HTTP/1 role and parser profiles) and must be independently trustworthy before v0.28.0 (Incremental HTTP/1 status-line parser) begins.

#### Deliverables

- Acceptance contract: Expose Incremental HTTP/1 request-line parser with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental HTTP/1 request-line parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.26.0 (HTTP/1 role and parser profiles) still passes; no behavior assigned to v0.28.0 (Incremental HTTP/1 status-line parser) is
claimed; and no critical or high finding remains open.

`0.27.0 implementation stop reached. Run pentest for this exact commit.`

### v0.28.0 — Incremental HTTP/1 status-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 status-line parser** as the sole primary capability in this stop. It builds
on v0.27.0 (Incremental HTTP/1 request-line parser) and must be independently trustworthy before v0.29.0 (Every-byte fragmentation support) begins.

#### Deliverables

- Acceptance contract: Expose Incremental HTTP/1 status-line parser with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental HTTP/1 status-line parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.27.0 (Incremental HTTP/1 request-line parser) still passes; no behavior assigned to v0.29.0 (Every-byte fragmentation support) is
claimed; and no critical or high finding remains open.

`0.28.0 implementation stop reached. Run pentest for this exact commit.`

### v0.29.0 — Every-byte fragmentation support

Status: planned

#### Goal

Deliver **Every-byte fragmentation support** as the sole primary capability in this stop. It builds
on v0.28.0 (Incremental HTTP/1 status-line parser) and must be independently trustworthy before v0.30.0 (Strict CRLF and separately named LF compatibility) begins.

#### Deliverables

- Acceptance contract: Expose Every-byte fragmentation support with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Every-byte fragmentation support and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Every-byte fragmentation support contract and all previously implemented relevant behavior have
reproducible evidence; v0.28.0 (Incremental HTTP/1 status-line parser) still passes; no behavior assigned to v0.30.0 (Strict CRLF and separately named LF compatibility) is
claimed; and no critical or high finding remains open.

`0.29.0 implementation stop reached. Run pentest for this exact commit.`

### v0.30.0 — Strict CRLF and separately named LF compatibility

Status: planned

#### Goal

Deliver **Strict CRLF and separately named LF compatibility** as the sole primary capability in this stop. It builds
on v0.29.0 (Every-byte fragmentation support) and must be independently trustworthy before v0.31.0 (Incremental HTTP/1 field-line parser) begins.

#### Deliverables

- Acceptance contract: Expose Strict CRLF and separately named LF compatibility with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Strict CRLF and separately named LF compatibility and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Strict CRLF and separately named LF compatibility contract and all previously implemented relevant behavior have
reproducible evidence; v0.29.0 (Every-byte fragmentation support) still passes; no behavior assigned to v0.31.0 (Incremental HTTP/1 field-line parser) is
claimed; and no critical or high finding remains open.

`0.30.0 implementation stop reached. Run pentest for this exact commit.`

### v0.31.0 — Incremental HTTP/1 field-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 field-line parser** as the sole primary capability in this stop. It builds
on v0.30.0 (Strict CRLF and separately named LF compatibility) and must be independently trustworthy before v0.32.0 (Explicit OWS handling with raw-value preservation) begins.

#### Deliverables

- Acceptance contract: Expose Incremental HTTP/1 field-line parser with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental HTTP/1 field-line parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.30.0 (Strict CRLF and separately named LF compatibility) still passes; no behavior assigned to v0.32.0 (Explicit OWS handling with raw-value preservation) is
claimed; and no critical or high finding remains open.

`0.31.0 implementation stop reached. Run pentest for this exact commit.`

### v0.32.0 — Explicit OWS handling with raw-value preservation

Status: planned

#### Goal

Deliver **Explicit OWS handling with raw-value preservation** as the sole primary capability in this stop. It builds
on v0.31.0 (Incremental HTTP/1 field-line parser) and must be independently trustworthy before v0.33.0 (Injection-proof HTTP/1 head serialization) begins.

#### Deliverables

- Acceptance contract: Expose Explicit OWS handling with raw-value preservation with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit OWS handling with raw-value preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.31.0 (Incremental HTTP/1 field-line parser) still passes; no behavior assigned to v0.33.0 (Injection-proof HTTP/1 head serialization) is
claimed; and no critical or high finding remains open.

`0.32.0 implementation stop reached. Run pentest for this exact commit.`

### v0.33.0 — Injection-proof HTTP/1 head serialization

Status: planned

#### Goal

Deliver **Injection-proof HTTP/1 head serialization** as the sole primary capability in this stop. It builds
on v0.32.0 (Explicit OWS handling with raw-value preservation) and must be independently trustworthy before v0.34.0 (Role-specific obs-fold and invalid-field disposition) begins.

#### Deliverables

- Acceptance contract: Expose Injection-proof HTTP/1 head serialization with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Injection-proof HTTP/1 head serialization and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Injection-proof HTTP/1 head serialization contract and all previously implemented relevant behavior have
reproducible evidence; v0.32.0 (Explicit OWS handling with raw-value preservation) still passes; no behavior assigned to v0.34.0 (Role-specific obs-fold and invalid-field disposition) is
claimed; and no critical or high finding remains open.

`0.33.0 implementation stop reached. Run pentest for this exact commit.`

### v0.34.0 — Role-specific obs-fold and invalid-field disposition

Status: planned

#### Goal

Deliver **Role-specific obs-fold and invalid-field disposition** as the sole primary capability in this stop. It builds
on v0.33.0 (Injection-proof HTTP/1 head serialization) and must be independently trustworthy before v0.35.0 (Field count, line, and section caps) begins.

#### Deliverables

- Acceptance contract: Implement the RFC 9112 role matrix for server requests, proxy/gateway responses, and user-agent responses rather than one blanket rejection rule.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Role-specific obs-fold and invalid-field disposition contract and all previously implemented relevant behavior have
reproducible evidence; v0.33.0 (Injection-proof HTTP/1 head serialization) still passes; no behavior assigned to v0.35.0 (Field count, line, and section caps) is
claimed; and no critical or high finding remains open.

`0.34.0 implementation stop reached. Run pentest for this exact commit.`

### v0.35.0 — Field count, line, and section caps

Status: planned

#### Goal

Deliver **Field count, line, and section caps** as the sole primary capability in this stop. It builds
on v0.34.0 (Role-specific obs-fold and invalid-field disposition) and must be independently trustworthy before v0.36.0 (Typed HTTP/1 protocol-error response and close actions) begins.

#### Deliverables

- Acceptance contract: Expose Field count, line, and section caps with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Field count, line, and section caps and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Field count, line, and section caps contract and all previously implemented relevant behavior have
reproducible evidence; v0.34.0 (Role-specific obs-fold and invalid-field disposition) still passes; no behavior assigned to v0.36.0 (Typed HTTP/1 protocol-error response and close actions) is
claimed; and no critical or high finding remains open.

`0.35.0 implementation stop reached. Run pentest for this exact commit.`

### v0.36.0 — Typed HTTP/1 protocol-error response and close actions

Status: planned

#### Goal

Deliver **Typed HTTP/1 protocol-error response and close actions** as the sole primary capability in this stop. It builds
on v0.35.0 (Field count, line, and section caps) and must be independently trustworthy before v0.37.0 (HTTP/1.1 Host validation and duplicate rejection) begins.

#### Deliverables

- Acceptance contract: Map failures to mandatory typed actions such as RejectAndClose(400/414/431), BadGatewayAndCloseUpstream, DiscardResponseAndClose, ConnectionError, or StreamError without unsafe continuation.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Typed HTTP/1 protocol-error response and close actions and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Typed HTTP/1 protocol-error response and close actions contract and all previously implemented relevant behavior have
reproducible evidence; v0.35.0 (Field count, line, and section caps) still passes; no behavior assigned to v0.37.0 (HTTP/1.1 Host validation and duplicate rejection) is
claimed; and no critical or high finding remains open.

`0.36.0 implementation stop reached. Run pentest for this exact commit.`

### v0.37.0 — HTTP/1.1 Host validation and duplicate rejection

Status: planned

#### Goal

Deliver **HTTP/1.1 Host validation and duplicate rejection** as the sole primary capability in this stop. It builds
on v0.36.0 (Typed HTTP/1 protocol-error response and close actions) and must be independently trustworthy before v0.38.0 (Method and request-target-form coherence) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/1.1 Host validation and duplicate rejection with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1.1 Host validation and duplicate rejection contract and all previously implemented relevant behavior have
reproducible evidence; v0.36.0 (Typed HTTP/1 protocol-error response and close actions) still passes; no behavior assigned to v0.38.0 (Method and request-target-form coherence) is
claimed; and no critical or high finding remains open.

`0.37.0 implementation stop reached. Run pentest for this exact commit.`

### v0.38.0 — Method and request-target-form coherence

Status: planned

#### Goal

Deliver **Method and request-target-form coherence** as the sole primary capability in this stop. It builds
on v0.37.0 (HTTP/1.1 Host validation and duplicate rejection) and must be independently trustworthy before v0.39.0 (Checked Content-Length grammar) begins.

#### Deliverables

- Acceptance contract: Expose Method and request-target-form coherence with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Method and request-target-form coherence and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Method and request-target-form coherence contract and all previously implemented relevant behavior have
reproducible evidence; v0.37.0 (HTTP/1.1 Host validation and duplicate rejection) still passes; no behavior assigned to v0.39.0 (Checked Content-Length grammar) is
claimed; and no critical or high finding remains open.

`0.38.0 implementation stop reached. Run pentest for this exact commit.`

### v0.39.0 — Checked Content-Length grammar

Status: planned

#### Goal

Deliver **Checked Content-Length grammar** as the sole primary capability in this stop. It builds
on v0.38.0 (Method and request-target-form coherence) and must be independently trustworthy before v0.40.0 (Repeated and comma-list Content-Length resolution) begins.

#### Deliverables

- Acceptance contract: Expose Checked Content-Length grammar with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked Content-Length grammar contract and all previously implemented relevant behavior have
reproducible evidence; v0.38.0 (Method and request-target-form coherence) still passes; no behavior assigned to v0.40.0 (Repeated and comma-list Content-Length resolution) is
claimed; and no critical or high finding remains open.

`0.39.0 implementation stop reached. Run pentest for this exact commit.`

### v0.40.0 — Repeated and comma-list Content-Length resolution

Status: planned

#### Goal

Deliver **Repeated and comma-list Content-Length resolution** as the sole primary capability in this stop. It builds
on v0.39.0 (Checked Content-Length grammar) and must be independently trustworthy before v0.41.0 (Transfer-Encoding grammar and ordering) begins.

#### Deliverables

- Acceptance contract: Expose Repeated and comma-list Content-Length resolution with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Repeated and comma-list Content-Length resolution contract and all previously implemented relevant behavior have
reproducible evidence; v0.39.0 (Checked Content-Length grammar) still passes; no behavior assigned to v0.41.0 (Transfer-Encoding grammar and ordering) is
claimed; and no critical or high finding remains open.

`0.40.0 implementation stop reached. Run pentest for this exact commit.`

### v0.41.0 — Transfer-Encoding grammar and ordering

Status: planned

#### Goal

Deliver **Transfer-Encoding grammar and ordering** as the sole primary capability in this stop. It builds
on v0.40.0 (Repeated and comma-list Content-Length resolution) and must be independently trustworthy before v0.42.0 (TE/CL conflict resolution and mandatory close action) begins.

#### Deliverables

- Acceptance contract: Expose Transfer-Encoding grammar and ordering with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Transfer-Encoding grammar and ordering contract and all previously implemented relevant behavior have
reproducible evidence; v0.40.0 (Repeated and comma-list Content-Length resolution) still passes; no behavior assigned to v0.42.0 (TE/CL conflict resolution and mandatory close action) is
claimed; and no critical or high finding remains open.

`0.41.0 implementation stop reached. Run pentest for this exact commit.`

### v0.42.0 — TE/CL conflict resolution and mandatory close action

Status: planned

#### Goal

Deliver **TE/CL conflict resolution and mandatory close action** as the sole primary capability in this stop. It builds
on v0.41.0 (Transfer-Encoding grammar and ordering) and must be independently trustworthy before v0.43.0 (Central HTTP/1 message-body-length algorithm) begins.

#### Deliverables

- Acceptance contract: Expose TE/CL conflict resolution and mandatory close action with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test TE/CL conflict resolution and mandatory close action and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The TE/CL conflict resolution and mandatory close action contract and all previously implemented relevant behavior have
reproducible evidence; v0.41.0 (Transfer-Encoding grammar and ordering) still passes; no behavior assigned to v0.43.0 (Central HTTP/1 message-body-length algorithm) is
claimed; and no critical or high finding remains open.

`0.42.0 implementation stop reached. Run pentest for this exact commit.`

### v0.43.0 — Central HTTP/1 message-body-length algorithm

Status: planned

#### Goal

Deliver **Central HTTP/1 message-body-length algorithm** as the sole primary capability in this stop. It builds
on v0.42.0 (TE/CL conflict resolution and mandatory close action) and must be independently trustworthy before v0.44.0 (Fixed-length body decoder) begins.

#### Deliverables

- Acceptance contract: Produce exactly one framing decision with checked arithmetic across method/status context, TE/CL ambiguity, body-forbidden responses, and mandatory-close behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- Add Kani proofs for framing arithmetic and exhaustive method/status/field decisions now.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Central HTTP/1 message-body-length algorithm contract and all previously implemented relevant behavior have
reproducible evidence; v0.42.0 (TE/CL conflict resolution and mandatory close action) still passes; no behavior assigned to v0.44.0 (Fixed-length body decoder) is
claimed; and no critical or high finding remains open.

`0.43.0 implementation stop reached. Run pentest for this exact commit.`

### v0.44.0 — Fixed-length body decoder

Status: planned

#### Goal

Deliver **Fixed-length body decoder** as the sole primary capability in this stop. It builds
on v0.43.0 (Central HTTP/1 message-body-length algorithm) and must be independently trustworthy before v0.45.0 (Close-delimited response decoder) begins.

#### Deliverables

- Acceptance contract: Expose Fixed-length body decoder with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Fixed-length body decoder and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Fixed-length body decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.43.0 (Central HTTP/1 message-body-length algorithm) still passes; no behavior assigned to v0.45.0 (Close-delimited response decoder) is
claimed; and no critical or high finding remains open.

`0.44.0 implementation stop reached. Run pentest for this exact commit.`

### v0.45.0 — Close-delimited response decoder

Status: planned

#### Goal

Deliver **Close-delimited response decoder** as the sole primary capability in this stop. It builds
on v0.44.0 (Fixed-length body decoder) and must be independently trustworthy before v0.46.0 (Checked chunk-size parser) begins.

#### Deliverables

- Acceptance contract: Expose Close-delimited response decoder with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Close-delimited response decoder and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Close-delimited response decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.44.0 (Fixed-length body decoder) still passes; no behavior assigned to v0.46.0 (Checked chunk-size parser) is
claimed; and no critical or high finding remains open.

`0.45.0 implementation stop reached. Run pentest for this exact commit.`

### v0.46.0 — Checked chunk-size parser

Status: planned

#### Goal

Deliver **Checked chunk-size parser** as the sole primary capability in this stop. It builds
on v0.45.0 (Close-delimited response decoder) and must be independently trustworthy before v0.47.0 (Incremental chunk-data state) begins.

#### Deliverables

- Acceptance contract: Expose Checked chunk-size parser with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked chunk-size parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.45.0 (Close-delimited response decoder) still passes; no behavior assigned to v0.47.0 (Incremental chunk-data state) is
claimed; and no critical or high finding remains open.

`0.46.0 implementation stop reached. Run pentest for this exact commit.`

### v0.47.0 — Incremental chunk-data state

Status: planned

#### Goal

Deliver **Incremental chunk-data state** as the sole primary capability in this stop. It builds
on v0.46.0 (Checked chunk-size parser) and must be independently trustworthy before v0.48.0 (Bounded chunk-extension parser) begins.

#### Deliverables

- Acceptance contract: Expose Incremental chunk-data state with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental chunk-data state contract and all previously implemented relevant behavior have
reproducible evidence; v0.46.0 (Checked chunk-size parser) still passes; no behavior assigned to v0.48.0 (Bounded chunk-extension parser) is
claimed; and no critical or high finding remains open.

`0.47.0 implementation stop reached. Run pentest for this exact commit.`

### v0.48.0 — Bounded chunk-extension parser

Status: planned

#### Goal

Deliver **Bounded chunk-extension parser** as the sole primary capability in this stop. It builds
on v0.47.0 (Incremental chunk-data state) and must be independently trustworthy before v0.49.0 (Last-chunk and trailer transition) begins.

#### Deliverables

- Acceptance contract: Expose Bounded chunk-extension parser with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Bounded chunk-extension parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.47.0 (Incremental chunk-data state) still passes; no behavior assigned to v0.49.0 (Last-chunk and trailer transition) is
claimed; and no critical or high finding remains open.

`0.48.0 implementation stop reached. Run pentest for this exact commit.`

### v0.49.0 — Last-chunk and trailer transition

Status: planned

#### Goal

Deliver **Last-chunk and trailer transition** as the sole primary capability in this stop. It builds
on v0.48.0 (Bounded chunk-extension parser) and must be independently trustworthy before v0.50.0 (Trailer declarations and prohibited-trailer policy) begins.

#### Deliverables

- Acceptance contract: Expose Last-chunk and trailer transition with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Last-chunk and trailer transition contract and all previously implemented relevant behavior have
reproducible evidence; v0.48.0 (Bounded chunk-extension parser) still passes; no behavior assigned to v0.50.0 (Trailer declarations and prohibited-trailer policy) is
claimed; and no critical or high finding remains open.

`0.49.0 implementation stop reached. Run pentest for this exact commit.`

### v0.50.0 — Trailer declarations and prohibited-trailer policy

Status: planned

#### Goal

Deliver **Trailer declarations and prohibited-trailer policy** as the sole primary capability in this stop. It builds
on v0.49.0 (Last-chunk and trailer transition) and must be independently trustworthy before v0.51.0 (Chunked encoder with partial-output state) begins.

#### Deliverables

- Acceptance contract: Expose Trailer declarations and prohibited-trailer policy with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Trailer declarations and prohibited-trailer policy and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Trailer declarations and prohibited-trailer policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.49.0 (Last-chunk and trailer transition) still passes; no behavior assigned to v0.51.0 (Chunked encoder with partial-output state) is
claimed; and no critical or high finding remains open.

`0.50.0 implementation stop reached. Run pentest for this exact commit.`

### v0.51.0 — Chunked encoder with partial-output state

Status: planned

#### Goal

Deliver **Chunked encoder with partial-output state** as the sole primary capability in this stop. It builds
on v0.50.0 (Trailer declarations and prohibited-trailer policy) and must be independently trustworthy before v0.52.0 (Unified HTTP/1 outbound message state machine) begins.

#### Deliverables

- Acceptance contract: Expose Chunked encoder with partial-output state with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Chunked encoder with partial-output state and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Chunked encoder with partial-output state contract and all previously implemented relevant behavior have
reproducible evidence; v0.50.0 (Trailer declarations and prohibited-trailer policy) still passes; no behavior assigned to v0.52.0 (Unified HTTP/1 outbound message state machine) is
claimed; and no critical or high finding remains open.

`0.51.0 implementation stop reached. Run pentest for this exact commit.`

### v0.52.0 — Unified HTTP/1 outbound message state machine

Status: planned

#### Goal

Deliver **Unified HTTP/1 outbound message state machine** as the sole primary capability in this stop. It builds
on v0.51.0 (Chunked encoder with partial-output state) and must be independently trustworthy before v0.53.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) begins.

#### Deliverables

- Acceptance contract: Serialize a head followed by exactly no body, fixed-length bytes, or chunked bytes; reject length disagreement, illegal trailers, post-completion commands, and sender-side HEAD/CONNECT/1xx/204/304 violations under one-byte output fragmentation.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Unified HTTP/1 outbound message state machine and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Unified HTTP/1 outbound message state machine contract and all previously implemented relevant behavior have
reproducible evidence; v0.51.0 (Chunked encoder with partial-output state) still passes; no behavior assigned to v0.53.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) is
claimed; and no critical or high finding remains open.

`0.52.0 implementation stop reached. Run pentest for this exact commit.`

### v0.53.0 — Inbound body acknowledgement, drain, discard, cancellation, and reuse

Status: planned

#### Goal

Deliver **Inbound body acknowledgement, drain, discard, cancellation, and reuse** as the sole primary capability in this stop. It builds
on v0.52.0 (Unified HTTP/1 outbound message state machine) and must be independently trustworthy before v0.54.0 (HTTP/1.1 persistence and Connection semantics) begins.

#### Deliverables

- Acceptance contract: Expose borrowed BodyChunk events plus Consume, Drain, DiscardAndClose, and Cancel; retain exact over-read bytes, apply backpressure before consumption, handle rejection around 100 Continue, and reuse only after body/trailer completion.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Inbound body acknowledgement, drain, discard, cancellation, and reuse and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Inbound body acknowledgement, drain, discard, cancellation, and reuse contract and all previously implemented relevant behavior have
reproducible evidence; v0.52.0 (Unified HTTP/1 outbound message state machine) still passes; no behavior assigned to v0.54.0 (HTTP/1.1 persistence and Connection semantics) is
claimed; and no critical or high finding remains open.

`0.53.0 implementation stop reached. Run pentest for this exact commit.`

### v0.54.0 — HTTP/1.1 persistence and Connection semantics

Status: planned

#### Goal

Deliver **HTTP/1.1 persistence and Connection semantics** as the sole primary capability in this stop. It builds
on v0.53.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) and must be independently trustworthy before v0.55.0 (Sequential request/response connection state) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/1.1 persistence and Connection semantics with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/1.1 persistence and Connection semantics and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1.1 persistence and Connection semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.53.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) still passes; no behavior assigned to v0.55.0 (Sequential request/response connection state) is
claimed; and no critical or high finding remains open.

`0.54.0 implementation stop reached. Run pentest for this exact commit.`

### v0.55.0 — Sequential request/response connection state

Status: planned

#### Goal

Deliver **Sequential request/response connection state** as the sole primary capability in this stop. It builds
on v0.54.0 (HTTP/1.1 persistence and Connection semantics) and must be independently trustworthy before v0.56.0 (Optional bounded pipelining queue) begins.

#### Deliverables

- Acceptance contract: Expose Sequential request/response connection state with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Sequential request/response connection state and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Sequential request/response connection state contract and all previously implemented relevant behavior have
reproducible evidence; v0.54.0 (HTTP/1.1 persistence and Connection semantics) still passes; no behavior assigned to v0.56.0 (Optional bounded pipelining queue) is
claimed; and no critical or high finding remains open.

`0.55.0 implementation stop reached. Run pentest for this exact commit.`

### v0.56.0 — Optional bounded pipelining queue

Status: planned

#### Goal

Deliver **Optional bounded pipelining queue** as the sole primary capability in this stop. It builds
on v0.55.0 (Sequential request/response connection state) and must be independently trustworthy before v0.57.0 (Informational response lifecycle) begins.

#### Deliverables

- Acceptance contract: Expose Optional bounded pipelining queue with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Optional bounded pipelining queue and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Optional bounded pipelining queue contract and all previously implemented relevant behavior have
reproducible evidence; v0.55.0 (Sequential request/response connection state) still passes; no behavior assigned to v0.57.0 (Informational response lifecycle) is
claimed; and no critical or high finding remains open.

`0.56.0 implementation stop reached. Run pentest for this exact commit.`

### v0.57.0 — Informational response lifecycle

Status: planned

#### Goal

Deliver **Informational response lifecycle** as the sole primary capability in this stop. It builds
on v0.56.0 (Optional bounded pipelining queue) and must be independently trustworthy before v0.58.0 (Expect: 100-continue state) begins.

#### Deliverables

- Acceptance contract: Expose Informational response lifecycle with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Informational response lifecycle and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Informational response lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.56.0 (Optional bounded pipelining queue) still passes; no behavior assigned to v0.58.0 (Expect: 100-continue state) is
claimed; and no critical or high finding remains open.

`0.57.0 implementation stop reached. Run pentest for this exact commit.`

### v0.58.0 — Expect: 100-continue state

Status: planned

#### Goal

Deliver **Expect: 100-continue state** as the sole primary capability in this stop. It builds
on v0.57.0 (Informational response lifecycle) and must be independently trustworthy before v0.59.0 (EOF, truncation, and incomplete-message rules) begins.

#### Deliverables

- Acceptance contract: Expose Expect: 100-continue state with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Expect: 100-continue state and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Expect: 100-continue state contract and all previously implemented relevant behavior have
reproducible evidence; v0.57.0 (Informational response lifecycle) still passes; no behavior assigned to v0.59.0 (EOF, truncation, and incomplete-message rules) is
claimed; and no critical or high finding remains open.

`0.58.0 implementation stop reached. Run pentest for this exact commit.`

### v0.59.0 — EOF, truncation, and incomplete-message rules

Status: planned

#### Goal

Deliver **EOF, truncation, and incomplete-message rules** as the sole primary capability in this stop. It builds
on v0.58.0 (Expect: 100-continue state) and must be independently trustworthy before v0.60.0 (HEAD response-framing context) begins.

#### Deliverables

- Acceptance contract: Expose EOF, truncation, and incomplete-message rules with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test EOF, truncation, and incomplete-message rules and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The EOF, truncation, and incomplete-message rules contract and all previously implemented relevant behavior have
reproducible evidence; v0.58.0 (Expect: 100-continue state) still passes; no behavior assigned to v0.60.0 (HEAD response-framing context) is
claimed; and no critical or high finding remains open.

`0.59.0 implementation stop reached. Run pentest for this exact commit.`

### v0.60.0 — HEAD response-framing context

Status: planned

#### Goal

Deliver **HEAD response-framing context** as the sole primary capability in this stop. It builds
on v0.59.0 (EOF, truncation, and incomplete-message rules) and must be independently trustworthy before v0.61.0 (1xx, 204, 304, and body-forbidden response handling) begins.

#### Deliverables

- Acceptance contract: Expose HEAD response-framing context with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HEAD response-framing context and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HEAD response-framing context contract and all previously implemented relevant behavior have
reproducible evidence; v0.59.0 (EOF, truncation, and incomplete-message rules) still passes; no behavior assigned to v0.61.0 (1xx, 204, 304, and body-forbidden response handling) is
claimed; and no critical or high finding remains open.

`0.60.0 implementation stop reached. Run pentest for this exact commit.`

### v0.61.0 — 1xx, 204, 304, and body-forbidden response handling

Status: planned

#### Goal

Deliver **1xx, 204, 304, and body-forbidden response handling** as the sole primary capability in this stop. It builds
on v0.60.0 (HEAD response-framing context) and must be independently trustworthy before v0.62.0 (CONNECT request and successful tunnel transition) begins.

#### Deliverables

- Acceptance contract: Expose 1xx, 204, 304, and body-forbidden response handling with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test 1xx, 204, 304, and body-forbidden response handling and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The 1xx, 204, 304, and body-forbidden response handling contract and all previously implemented relevant behavior have
reproducible evidence; v0.60.0 (HEAD response-framing context) still passes; no behavior assigned to v0.62.0 (CONNECT request and successful tunnel transition) is
claimed; and no critical or high finding remains open.

`0.61.0 implementation stop reached. Run pentest for this exact commit.`

### v0.62.0 — CONNECT request and successful tunnel transition

Status: planned

#### Goal

Deliver **CONNECT request and successful tunnel transition** as the sole primary capability in this stop. It builds
on v0.61.0 (1xx, 204, 304, and body-forbidden response handling) and must be independently trustworthy before v0.63.0 (RFC 9931 optimistic-data protections) begins.

#### Deliverables

- Acceptance contract: Expose CONNECT request and successful tunnel transition with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test CONNECT request and successful tunnel transition and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONNECT request and successful tunnel transition contract and all previously implemented relevant behavior have
reproducible evidence; v0.61.0 (1xx, 204, 304, and body-forbidden response handling) still passes; no behavior assigned to v0.63.0 (RFC 9931 optimistic-data protections) is
claimed; and no critical or high finding remains open.

`0.62.0 implementation stop reached. Run pentest for this exact commit.`

### v0.63.0 — RFC 9931 optimistic-data protections

Status: planned

#### Goal

Deliver **RFC 9931 optimistic-data protections** as the sole primary capability in this stop. It builds
on v0.62.0 (CONNECT request and successful tunnel transition) and must be independently trustworthy before v0.64.0 (Connection-option, Upgrade, and hop-by-hop field grammar) begins.

#### Deliverables

- Acceptance contract: Expose RFC 9931 optimistic-data protections with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test RFC 9931 optimistic-data protections and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RFC 9931 optimistic-data protections contract and all previously implemented relevant behavior have
reproducible evidence; v0.62.0 (CONNECT request and successful tunnel transition) still passes; no behavior assigned to v0.64.0 (Connection-option, Upgrade, and hop-by-hop field grammar) is
claimed; and no critical or high finding remains open.

`0.63.0 implementation stop reached. Run pentest for this exact commit.`

### v0.64.0 — Connection-option, Upgrade, and hop-by-hop field grammar

Status: planned

#### Goal

Deliver **Connection-option, Upgrade, and hop-by-hop field grammar** as the sole primary capability in this stop. It builds
on v0.63.0 (RFC 9931 optimistic-data protections) and must be independently trustworthy before v0.65.0 (101 Switching Protocols transition and publication barrier) begins.

#### Deliverables

- Acceptance contract: Parse Connection option tokens and Upgrade grammar before any 101 or WebSocket validation and derive explicit hop-by-hop handling without implicit normalization.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Connection-option, Upgrade, and hop-by-hop field grammar and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection-option, Upgrade, and hop-by-hop field grammar contract and all previously implemented relevant behavior have
reproducible evidence; v0.63.0 (RFC 9931 optimistic-data protections) still passes; no behavior assigned to v0.65.0 (101 Switching Protocols transition and publication barrier) is
claimed; and no critical or high finding remains open.

`0.64.0 implementation stop reached. Run pentest for this exact commit.`

### v0.65.0 — 101 Switching Protocols transition and publication barrier

Status: planned

#### Goal

Deliver **101 Switching Protocols transition and publication barrier** as the sole primary capability in this stop. It builds
on v0.64.0 (Connection-option, Upgrade, and hop-by-hop field grammar) and must be independently trustworthy before v0.66.0 (Separate WebSocket handshake crate, key, version, and token validation) begins.

#### Deliverables

- Acceptance contract: Commit a valid 101 transition before exposing buffered post-handshake bytes and reject success paths whose Connection/Upgrade prerequisites are invalid.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test 101 Switching Protocols transition and publication barrier and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The 101 Switching Protocols transition and publication barrier contract and all previously implemented relevant behavior have
reproducible evidence; v0.64.0 (Connection-option, Upgrade, and hop-by-hop field grammar) still passes; no behavior assigned to v0.66.0 (Separate WebSocket handshake crate, key, version, and token validation) is
claimed; and no critical or high finding remains open.

`0.65.0 implementation stop reached. Run pentest for this exact commit.`

### v0.66.0 — Separate WebSocket handshake crate, key, version, and token validation

Status: planned

#### Goal

Deliver **Separate WebSocket handshake crate, key, version, and token validation** as the sole primary capability in this stop. It builds
on v0.65.0 (101 Switching Protocols transition and publication barrier) and must be independently trustworthy before v0.67.0 (WebSocket accept generation and client/server validation) begins.

#### Deliverables

- Acceptance contract: Create an optional no_std handshake boundary that validates Sec-WebSocket-Key base64 shape, version 13, Upgrade/Connection tokens, and distinct client/server rules without implementing frames.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Separate WebSocket handshake crate, key, version, and token validation and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Separate WebSocket handshake crate, key, version, and token validation contract and all previously implemented relevant behavior have
reproducible evidence; v0.65.0 (101 Switching Protocols transition and publication barrier) still passes; no behavior assigned to v0.67.0 (WebSocket accept generation and client/server validation) is
claimed; and no critical or high finding remains open.

`0.66.0 implementation stop reached. Run pentest for this exact commit.`

### v0.67.0 — WebSocket accept generation and client/server validation

Status: planned

#### Goal

Deliver **WebSocket accept generation and client/server validation** as the sole primary capability in this stop. It builds
on v0.66.0 (Separate WebSocket handshake crate, key, version, and token validation) and must be independently trustworthy before v0.68.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) begins.

#### Deliverables

- Acceptance contract: Implement and vector-test the RFC 6455 SHA-1 plus base64 accept calculation, server generation, client validation, invalid padding/length rejection, and bounded dependency-free operation.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test WebSocket accept generation and client/server validation and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WebSocket accept generation and client/server validation contract and all previously implemented relevant behavior have
reproducible evidence; v0.66.0 (Separate WebSocket handshake crate, key, version, and token validation) still passes; no behavior assigned to v0.68.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) is
claimed; and no critical or high finding remains open.

`0.67.0 implementation stop reached. Run pentest for this exact commit.`

### v0.68.0 — WebSocket negotiation, origin metadata, and byte-publication barrier

Status: planned

#### Goal

Deliver **WebSocket negotiation, origin metadata, and byte-publication barrier** as the sole primary capability in this stop. It builds
on v0.67.0 (WebSocket accept generation and client/server validation) and must be independently trustworthy before v0.69.0 (Safe forwarding and explicit reframing plan) begins.

#### Deliverables

- Acceptance contract: Define subprotocol and extension selection, preserve Origin metadata for caller policy, reject unsolicited negotiation, and publish no post-handshake bytes before success.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test WebSocket negotiation, origin metadata, and byte-publication barrier and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WebSocket negotiation, origin metadata, and byte-publication barrier contract and all previously implemented relevant behavior have
reproducible evidence; v0.67.0 (WebSocket accept generation and client/server validation) still passes; no behavior assigned to v0.69.0 (Safe forwarding and explicit reframing plan) is
claimed; and no critical or high finding remains open.

`0.68.0 implementation stop reached. Run pentest for this exact commit.`

### v0.69.0 — Safe forwarding and explicit reframing plan

Status: planned

#### Goal

Deliver **Safe forwarding and explicit reframing plan** as the sole primary capability in this stop. It builds
on v0.68.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) and must be independently trustworthy before v0.70.0 (RFC 1945 HTTP/1.0 parser and hardened profile) begins.

#### Deliverables

- Acceptance contract: Expose Safe forwarding and explicit reframing plan with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Safe forwarding and explicit reframing plan and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Safe forwarding and explicit reframing plan contract and all previously implemented relevant behavior have
reproducible evidence; v0.68.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) still passes; no behavior assigned to v0.70.0 (RFC 1945 HTTP/1.0 parser and hardened profile) is
claimed; and no critical or high finding remains open.

`0.69.0 implementation stop reached. Run pentest for this exact commit.`

### v0.70.0 — RFC 1945 HTTP/1.0 parser and hardened profile

Status: planned

#### Goal

Deliver **RFC 1945 HTTP/1.0 parser and hardened profile** as the sole primary capability in this stop. It builds
on v0.69.0 (Safe forwarding and explicit reframing plan) and must be independently trustworthy before v0.71.0 (HTTP/1.0 default-close lifecycle) begins.

#### Deliverables

- Acceptance contract: Expose RFC 1945 HTTP/1.0 parser and hardened profile with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the stateful HTTP/1 fuzz target now and retain its minimized corpus.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RFC 1945 HTTP/1.0 parser and hardened profile contract and all previously implemented relevant behavior have
reproducible evidence; v0.69.0 (Safe forwarding and explicit reframing plan) still passes; no behavior assigned to v0.71.0 (HTTP/1.0 default-close lifecycle) is
claimed; and no critical or high finding remains open.

`0.70.0 implementation stop reached. Run pentest for this exact commit.`

### v0.71.0 — HTTP/1.0 default-close lifecycle

Status: planned

#### Goal

Deliver **HTTP/1.0 default-close lifecycle** as the sole primary capability in this stop. It builds
on v0.70.0 (RFC 1945 HTTP/1.0 parser and hardened profile) and must be independently trustworthy before v0.72.0 (Explicit HTTP/1.0 keep-alive extension profile) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/1.0 default-close lifecycle with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/1.0 default-close lifecycle and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1.0 default-close lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.70.0 (RFC 1945 HTTP/1.0 parser and hardened profile) still passes; no behavior assigned to v0.72.0 (Explicit HTTP/1.0 keep-alive extension profile) is
claimed; and no critical or high finding remains open.

`0.71.0 implementation stop reached. Run pentest for this exact commit.`

### v0.72.0 — Explicit HTTP/1.0 keep-alive extension profile

Status: planned

#### Goal

Deliver **Explicit HTTP/1.0 keep-alive extension profile** as the sole primary capability in this stop. It builds
on v0.71.0 (HTTP/1.0 default-close lifecycle) and must be independently trustworthy before v0.73.0 (Separate vef-http09 package and exact grammar) begins.

#### Deliverables

- Acceptance contract: Expose Explicit HTTP/1.0 keep-alive extension profile with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Explicit HTTP/1.0 keep-alive extension profile and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit HTTP/1.0 keep-alive extension profile contract and all previously implemented relevant behavior have
reproducible evidence; v0.71.0 (HTTP/1.0 default-close lifecycle) still passes; no behavior assigned to v0.73.0 (Separate vef-http09 package and exact grammar) is
claimed; and no critical or high finding remains open.

`0.72.0 implementation stop reached. Run pentest for this exact commit.`

### v0.73.0 — Separate vef-http09 package and exact grammar

Status: planned

#### Goal

Deliver **Separate vef-http09 package and exact grammar** as the sole primary capability in this stop. It builds
on v0.72.0 (Explicit HTTP/1.0 keep-alive extension profile) and must be independently trustworthy before v0.74.0 (Explicit HTTP/0.9 client API) begins.

#### Deliverables

- Acceptance contract: Expose Separate vef-http09 package and exact grammar with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Separate vef-http09 package and exact grammar and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Separate vef-http09 package and exact grammar contract and all previously implemented relevant behavior have
reproducible evidence; v0.72.0 (Explicit HTTP/1.0 keep-alive extension profile) still passes; no behavior assigned to v0.74.0 (Explicit HTTP/0.9 client API) is
claimed; and no critical or high finding remains open.

`0.73.0 implementation stop reached. Run pentest for this exact commit.`

### v0.74.0 — Explicit HTTP/0.9 client API

Status: planned

#### Goal

Deliver **Explicit HTTP/0.9 client API** as the sole primary capability in this stop. It builds
on v0.73.0 (Separate vef-http09 package and exact grammar) and must be independently trustworthy before v0.75.0 (Explicit HTTP/0.9 server and dedicated-listener API) begins.

#### Deliverables

- Acceptance contract: Expose Explicit HTTP/0.9 client API with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Explicit HTTP/0.9 client API and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit HTTP/0.9 client API contract and all previously implemented relevant behavior have
reproducible evidence; v0.73.0 (Separate vef-http09 package and exact grammar) still passes; no behavior assigned to v0.75.0 (Explicit HTTP/0.9 server and dedicated-listener API) is
claimed; and no critical or high finding remains open.

`0.74.0 implementation stop reached. Run pentest for this exact commit.`

### v0.75.0 — Explicit HTTP/0.9 server and dedicated-listener API

Status: planned

#### Goal

Deliver **Explicit HTTP/0.9 server and dedicated-listener API** as the sole primary capability in this stop. It builds
on v0.74.0 (Explicit HTTP/0.9 client API) and must be independently trustworthy before v0.76.0 (HTTP/0.9 cross-protocol rejection corpus) begins.

#### Deliverables

- Acceptance contract: Expose Explicit HTTP/0.9 server and dedicated-listener API with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Explicit HTTP/0.9 server and dedicated-listener API and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit HTTP/0.9 server and dedicated-listener API contract and all previously implemented relevant behavior have
reproducible evidence; v0.74.0 (Explicit HTTP/0.9 client API) still passes; no behavior assigned to v0.76.0 (HTTP/0.9 cross-protocol rejection corpus) is
claimed; and no critical or high finding remains open.

`0.75.0 implementation stop reached. Run pentest for this exact commit.`

### v0.76.0 — HTTP/0.9 cross-protocol rejection corpus

Status: planned

#### Goal

Deliver **HTTP/0.9 cross-protocol rejection corpus** as the sole primary capability in this stop. It builds
on v0.75.0 (Explicit HTTP/0.9 server and dedicated-listener API) and must be independently trustworthy before v0.77.0 (HTTP/1 smuggling and ambiguity corpus) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/0.9 cross-protocol rejection corpus with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/0.9 cross-protocol rejection corpus and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/0.9 cross-protocol rejection corpus contract and all previously implemented relevant behavior have
reproducible evidence; v0.75.0 (Explicit HTTP/0.9 server and dedicated-listener API) still passes; no behavior assigned to v0.77.0 (HTTP/1 smuggling and ambiguity corpus) is
claimed; and no critical or high finding remains open.

`0.76.0 implementation stop reached. Run pentest for this exact commit.`

### v0.77.0 — HTTP/1 smuggling and ambiguity corpus

Status: planned

#### Goal

Deliver **HTTP/1 smuggling and ambiguity corpus** as the sole primary capability in this stop. It builds
on v0.76.0 (HTTP/0.9 cross-protocol rejection corpus) and must be independently trustworthy before v0.78.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/1 smuggling and ambiguity corpus with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/1 smuggling and ambiguity corpus and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 smuggling and ambiguity corpus contract and all previously implemented relevant behavior have
reproducible evidence; v0.76.0 (HTTP/0.9 cross-protocol rejection corpus) still passes; no behavior assigned to v0.78.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) is
claimed; and no critical or high finding remains open.

`0.77.0 implementation stop reached. Run pentest for this exact commit.`

### v0.78.0 — HTTP/1 and HTTP/0.9 conformance audit and pentest

Status: planned

#### Goal

Deliver **HTTP/1 and HTTP/0.9 conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.77.0 (HTTP/1 smuggling and ambiguity corpus) and must be independently trustworthy before v0.79.0 (HPACK prefix-integer decoder) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/1 and HTTP/0.9 conformance audit and pentest with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound and outbound framing interpretation, explicit body ownership and close actions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/1 and HTTP/0.9 conformance audit and pentest and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 and HTTP/0.9 conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.77.0 (HTTP/1 smuggling and ambiguity corpus) still passes; no behavior assigned to v0.79.0 (HPACK prefix-integer decoder) is
claimed; and no critical or high finding remains open.

`0.78.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 3 — HPACK and HTTP/2

Phase contract: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.

### v0.79.0 — HPACK prefix-integer decoder

Status: planned

#### Goal

Deliver **HPACK prefix-integer decoder** as the sole primary capability in this stop. It builds
on v0.78.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) and must be independently trustworthy before v0.80.0 (HPACK prefix-integer encoder) begins.

#### Deliverables

- Acceptance contract: Expose HPACK prefix-integer decoder with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK integer, Huffman, or table fuzz target now; do not defer harness creation.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK prefix-integer decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.78.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) still passes; no behavior assigned to v0.80.0 (HPACK prefix-integer encoder) is
claimed; and no critical or high finding remains open.

`0.79.0 implementation stop reached. Run pentest for this exact commit.`

### v0.80.0 — HPACK prefix-integer encoder

Status: planned

#### Goal

Deliver **HPACK prefix-integer encoder** as the sole primary capability in this stop. It builds
on v0.79.0 (HPACK prefix-integer decoder) and must be independently trustworthy before v0.81.0 (HPACK integer overflow and minimality proofs) begins.

#### Deliverables

- Acceptance contract: Expose HPACK prefix-integer encoder with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK integer, Huffman, or table fuzz target now; do not defer harness creation.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK prefix-integer encoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.79.0 (HPACK prefix-integer decoder) still passes; no behavior assigned to v0.81.0 (HPACK integer overflow and minimality proofs) is
claimed; and no critical or high finding remains open.

`0.80.0 implementation stop reached. Run pentest for this exact commit.`

### v0.81.0 — HPACK integer overflow and minimality proofs

Status: planned

#### Goal

Deliver **HPACK integer overflow and minimality proofs** as the sole primary capability in this stop. It builds
on v0.80.0 (HPACK prefix-integer encoder) and must be independently trustworthy before v0.82.0 (HPACK string representation codec) begins.

#### Deliverables

- Acceptance contract: Expose HPACK integer overflow and minimality proofs with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HPACK integer overflow and minimality proofs and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK integer overflow and minimality proofs contract and all previously implemented relevant behavior have
reproducible evidence; v0.80.0 (HPACK prefix-integer encoder) still passes; no behavior assigned to v0.82.0 (HPACK string representation codec) is
claimed; and no critical or high finding remains open.

`0.81.0 implementation stop reached. Run pentest for this exact commit.`

### v0.82.0 — HPACK string representation codec

Status: planned

#### Goal

Deliver **HPACK string representation codec** as the sole primary capability in this stop. It builds
on v0.81.0 (HPACK integer overflow and minimality proofs) and must be independently trustworthy before v0.83.0 (HPACK Huffman tables) begins.

#### Deliverables

- Acceptance contract: Expose HPACK string representation codec with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK integer, Huffman, or table fuzz target now; do not defer harness creation.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK string representation codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.81.0 (HPACK integer overflow and minimality proofs) still passes; no behavior assigned to v0.83.0 (HPACK Huffman tables) is
claimed; and no critical or high finding remains open.

`0.82.0 implementation stop reached. Run pentest for this exact commit.`

### v0.83.0 — HPACK Huffman tables

Status: planned

#### Goal

Deliver **HPACK Huffman tables** as the sole primary capability in this stop. It builds
on v0.82.0 (HPACK string representation codec) and must be independently trustworthy before v0.84.0 (HPACK Huffman decoder) begins.

#### Deliverables

- Acceptance contract: Expose HPACK Huffman tables with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK integer, Huffman, or table fuzz target now; do not defer harness creation.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK Huffman tables contract and all previously implemented relevant behavior have
reproducible evidence; v0.82.0 (HPACK string representation codec) still passes; no behavior assigned to v0.84.0 (HPACK Huffman decoder) is
claimed; and no critical or high finding remains open.

`0.83.0 implementation stop reached. Run pentest for this exact commit.`

### v0.84.0 — HPACK Huffman decoder

Status: planned

#### Goal

Deliver **HPACK Huffman decoder** as the sole primary capability in this stop. It builds
on v0.83.0 (HPACK Huffman tables) and must be independently trustworthy before v0.85.0 (HPACK Huffman encoder) begins.

#### Deliverables

- Acceptance contract: Expose HPACK Huffman decoder with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK integer, Huffman, or table fuzz target now; do not defer harness creation.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK Huffman decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.83.0 (HPACK Huffman tables) still passes; no behavior assigned to v0.85.0 (HPACK Huffman encoder) is
claimed; and no critical or high finding remains open.

`0.84.0 implementation stop reached. Run pentest for this exact commit.`

### v0.85.0 — HPACK Huffman encoder

Status: planned

#### Goal

Deliver **HPACK Huffman encoder** as the sole primary capability in this stop. It builds
on v0.84.0 (HPACK Huffman decoder) and must be independently trustworthy before v0.86.0 (HPACK static table) begins.

#### Deliverables

- Acceptance contract: Expose HPACK Huffman encoder with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK integer, Huffman, or table fuzz target now; do not defer harness creation.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK Huffman encoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.84.0 (HPACK Huffman decoder) still passes; no behavior assigned to v0.86.0 (HPACK static table) is
claimed; and no critical or high finding remains open.

`0.85.0 implementation stop reached. Run pentest for this exact commit.`

### v0.86.0 — HPACK static table

Status: planned

#### Goal

Deliver **HPACK static table** as the sole primary capability in this stop. It builds
on v0.85.0 (HPACK Huffman encoder) and must be independently trustworthy before v0.87.0 (HPACK dynamic table storage) begins.

#### Deliverables

- Acceptance contract: Expose HPACK static table with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HPACK static table and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK static table contract and all previously implemented relevant behavior have
reproducible evidence; v0.85.0 (HPACK Huffman encoder) still passes; no behavior assigned to v0.87.0 (HPACK dynamic table storage) is
claimed; and no critical or high finding remains open.

`0.86.0 implementation stop reached. Run pentest for this exact commit.`

### v0.87.0 — HPACK dynamic table storage

Status: planned

#### Goal

Deliver **HPACK dynamic table storage** as the sole primary capability in this stop. It builds
on v0.86.0 (HPACK static table) and must be independently trustworthy before v0.88.0 (HPACK eviction and oversize-entry behavior) begins.

#### Deliverables

- Acceptance contract: Expose HPACK dynamic table storage with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK integer, Huffman, or table fuzz target now; do not defer harness creation.
- Add Kani proofs for table accounting, eviction, wraparound, and reserve/commit/refund behavior now.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK dynamic table storage contract and all previously implemented relevant behavior have
reproducible evidence; v0.86.0 (HPACK static table) still passes; no behavior assigned to v0.88.0 (HPACK eviction and oversize-entry behavior) is
claimed; and no critical or high finding remains open.

`0.87.0 implementation stop reached. Run pentest for this exact commit.`

### v0.88.0 — HPACK eviction and oversize-entry behavior

Status: planned

#### Goal

Deliver **HPACK eviction and oversize-entry behavior** as the sole primary capability in this stop. It builds
on v0.87.0 (HPACK dynamic table storage) and must be independently trustworthy before v0.89.0 (HPACK table-size update and SETTINGS coupling) begins.

#### Deliverables

- Acceptance contract: Expose HPACK eviction and oversize-entry behavior with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK integer, Huffman, or table fuzz target now; do not defer harness creation.
- Add Kani proofs for table accounting, eviction, wraparound, and reserve/commit/refund behavior now.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK eviction and oversize-entry behavior contract and all previously implemented relevant behavior have
reproducible evidence; v0.87.0 (HPACK dynamic table storage) still passes; no behavior assigned to v0.89.0 (HPACK table-size update and SETTINGS coupling) is
claimed; and no critical or high finding remains open.

`0.88.0 implementation stop reached. Run pentest for this exact commit.`

### v0.89.0 — HPACK table-size update and SETTINGS coupling

Status: planned

#### Goal

Deliver **HPACK table-size update and SETTINGS coupling** as the sole primary capability in this stop. It builds
on v0.88.0 (HPACK eviction and oversize-entry behavior) and must be independently trustworthy before v0.90.0 (HPACK caller-owned ring lookup) begins.

#### Deliverables

- Acceptance contract: Expose HPACK table-size update and SETTINGS coupling with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK integer, Huffman, or table fuzz target now; do not defer harness creation.
- Add Kani proofs for table accounting, eviction, wraparound, and reserve/commit/refund behavior now.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK table-size update and SETTINGS coupling contract and all previously implemented relevant behavior have
reproducible evidence; v0.88.0 (HPACK eviction and oversize-entry behavior) still passes; no behavior assigned to v0.90.0 (HPACK caller-owned ring lookup) is
claimed; and no critical or high finding remains open.

`0.89.0 implementation stop reached. Run pentest for this exact commit.`

### v0.90.0 — HPACK caller-owned ring lookup

Status: planned

#### Goal

Deliver **HPACK caller-owned ring lookup** as the sole primary capability in this stop. It builds
on v0.89.0 (HPACK table-size update and SETTINGS coupling) and must be independently trustworthy before v0.91.0 (HPACK indexed representation) begins.

#### Deliverables

- Acceptance contract: Expose HPACK caller-owned ring lookup with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK integer, Huffman, or table fuzz target now; do not defer harness creation.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK caller-owned ring lookup contract and all previously implemented relevant behavior have
reproducible evidence; v0.89.0 (HPACK table-size update and SETTINGS coupling) still passes; no behavior assigned to v0.91.0 (HPACK indexed representation) is
claimed; and no critical or high finding remains open.

`0.90.0 implementation stop reached. Run pentest for this exact commit.`

### v0.91.0 — HPACK indexed representation

Status: planned

#### Goal

Deliver **HPACK indexed representation** as the sole primary capability in this stop. It builds
on v0.90.0 (HPACK caller-owned ring lookup) and must be independently trustworthy before v0.92.0 (HPACK incremental-indexing literal) begins.

#### Deliverables

- Acceptance contract: Expose HPACK indexed representation with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HPACK indexed representation and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK indexed representation contract and all previously implemented relevant behavior have
reproducible evidence; v0.90.0 (HPACK caller-owned ring lookup) still passes; no behavior assigned to v0.92.0 (HPACK incremental-indexing literal) is
claimed; and no critical or high finding remains open.

`0.91.0 implementation stop reached. Run pentest for this exact commit.`

### v0.92.0 — HPACK incremental-indexing literal

Status: planned

#### Goal

Deliver **HPACK incremental-indexing literal** as the sole primary capability in this stop. It builds
on v0.91.0 (HPACK indexed representation) and must be independently trustworthy before v0.93.0 (HPACK non-indexing and never-indexed literal) begins.

#### Deliverables

- Acceptance contract: Expose HPACK incremental-indexing literal with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HPACK incremental-indexing literal and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK incremental-indexing literal contract and all previously implemented relevant behavior have
reproducible evidence; v0.91.0 (HPACK indexed representation) still passes; no behavior assigned to v0.93.0 (HPACK non-indexing and never-indexed literal) is
claimed; and no critical or high finding remains open.

`0.92.0 implementation stop reached. Run pentest for this exact commit.`

### v0.93.0 — HPACK non-indexing and never-indexed literal

Status: planned

#### Goal

Deliver **HPACK non-indexing and never-indexed literal** as the sole primary capability in this stop. It builds
on v0.92.0 (HPACK incremental-indexing literal) and must be independently trustworthy before v0.94.0 (Sensitive-field indexing policy) begins.

#### Deliverables

- Acceptance contract: Expose HPACK non-indexing and never-indexed literal with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HPACK non-indexing and never-indexed literal and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK non-indexing and never-indexed literal contract and all previously implemented relevant behavior have
reproducible evidence; v0.92.0 (HPACK incremental-indexing literal) still passes; no behavior assigned to v0.94.0 (Sensitive-field indexing policy) is
claimed; and no critical or high finding remains open.

`0.93.0 implementation stop reached. Run pentest for this exact commit.`

### v0.94.0 — Sensitive-field indexing policy

Status: planned

#### Goal

Deliver **Sensitive-field indexing policy** as the sole primary capability in this stop. It builds
on v0.93.0 (HPACK non-indexing and never-indexed literal) and must be independently trustworthy before v0.95.0 (Independent HPACK decode limits) begins.

#### Deliverables

- Acceptance contract: Expose Sensitive-field indexing policy with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Sensitive-field indexing policy and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Sensitive-field indexing policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.93.0 (HPACK non-indexing and never-indexed literal) still passes; no behavior assigned to v0.95.0 (Independent HPACK decode limits) is
claimed; and no critical or high finding remains open.

`0.94.0 implementation stop reached. Run pentest for this exact commit.`

### v0.95.0 — Independent HPACK decode limits

Status: planned

#### Goal

Deliver **Independent HPACK decode limits** as the sole primary capability in this stop. It builds
on v0.94.0 (Sensitive-field indexing policy) and must be independently trustworthy before v0.96.0 (HPACK synchronization, publication barrier, and error scope) begins.

#### Deliverables

- Acceptance contract: Expose Independent HPACK decode limits with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Independent HPACK decode limits and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Independent HPACK decode limits contract and all previously implemented relevant behavior have
reproducible evidence; v0.94.0 (Sensitive-field indexing policy) still passes; no behavior assigned to v0.96.0 (HPACK synchronization, publication barrier, and error scope) is
claimed; and no critical or high finding remains open.

`0.95.0 implementation stop reached. Run pentest for this exact commit.`

### v0.96.0 — HPACK synchronization, publication barrier, and error scope

Status: planned

#### Goal

Deliver **HPACK synchronization, publication barrier, and error scope** as the sole primary capability in this stop. It builds
on v0.95.0 (Independent HPACK decode limits) and must be independently trustworthy before v0.97.0 (HPACK conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Commit valid compression-table updates even when later semantic validation rejects a stream; withhold fields until validation, make compression errors connection-fatal, never roll back connection compression state for stream errors, and close when limits prevent safe completion.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HPACK synchronization, publication barrier, and error scope and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK synchronization, publication barrier, and error scope contract and all previously implemented relevant behavior have
reproducible evidence; v0.95.0 (Independent HPACK decode limits) still passes; no behavior assigned to v0.97.0 (HPACK conformance audit and pentest) is
claimed; and no critical or high finding remains open.

`0.96.0 implementation stop reached. Run pentest for this exact commit.`

### v0.97.0 — HPACK conformance audit and pentest

Status: planned

#### Goal

Deliver **HPACK conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.96.0 (HPACK synchronization, publication barrier, and error scope) and must be independently trustworthy before v0.98.0 (HTTP/2 client and server prefaces) begins.

#### Deliverables

- Acceptance contract: Expose HPACK conformance audit and pentest with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HPACK conformance audit and pentest and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.96.0 (HPACK synchronization, publication barrier, and error scope) still passes; no behavior assigned to v0.98.0 (HTTP/2 client and server prefaces) is
claimed; and no critical or high finding remains open.

`0.97.0 implementation stop reached. Run pentest for this exact commit.`

### v0.98.0 — HTTP/2 client and server prefaces

Status: planned

#### Goal

Deliver **HTTP/2 client and server prefaces** as the sole primary capability in this stop. It builds
on v0.97.0 (HPACK conformance audit and pentest) and must be independently trustworthy before v0.99.0 (HTTP/2 frame-header codec) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/2 client and server prefaces with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/2 client and server prefaces and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 client and server prefaces contract and all previously implemented relevant behavior have
reproducible evidence; v0.97.0 (HPACK conformance audit and pentest) still passes; no behavior assigned to v0.99.0 (HTTP/2 frame-header codec) is
claimed; and no critical or high finding remains open.

`0.98.0 implementation stop reached. Run pentest for this exact commit.`

### v0.99.0 — HTTP/2 frame-header codec

Status: planned

#### Goal

Deliver **HTTP/2 frame-header codec** as the sole primary capability in this stop. It builds
on v0.98.0 (HTTP/2 client and server prefaces) and must be independently trustworthy before v0.100.0 (DATA frame codec) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/2 frame-header codec with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 frame-header codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.98.0 (HTTP/2 client and server prefaces) still passes; no behavior assigned to v0.100.0 (DATA frame codec) is
claimed; and no critical or high finding remains open.

`0.99.0 implementation stop reached. Run pentest for this exact commit.`

### v0.100.0 — DATA frame codec

Status: planned

#### Goal

Deliver **DATA frame codec** as the sole primary capability in this stop. It builds
on v0.99.0 (HTTP/2 frame-header codec) and must be independently trustworthy before v0.101.0 (HEADERS frame codec) begins.

#### Deliverables

- Acceptance contract: Expose DATA frame codec with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The DATA frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.99.0 (HTTP/2 frame-header codec) still passes; no behavior assigned to v0.101.0 (HEADERS frame codec) is
claimed; and no critical or high finding remains open.

`0.100.0 implementation stop reached. Run pentest for this exact commit.`

### v0.101.0 — HEADERS frame codec

Status: planned

#### Goal

Deliver **HEADERS frame codec** as the sole primary capability in this stop. It builds
on v0.100.0 (DATA frame codec) and must be independently trustworthy before v0.102.0 (CONTINUATION frame codec) begins.

#### Deliverables

- Acceptance contract: Expose HEADERS frame codec with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HEADERS frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.100.0 (DATA frame codec) still passes; no behavior assigned to v0.102.0 (CONTINUATION frame codec) is
claimed; and no critical or high finding remains open.

`0.101.0 implementation stop reached. Run pentest for this exact commit.`

### v0.102.0 — CONTINUATION frame codec

Status: planned

#### Goal

Deliver **CONTINUATION frame codec** as the sole primary capability in this stop. It builds
on v0.101.0 (HEADERS frame codec) and must be independently trustworthy before v0.103.0 (SETTINGS frame codec) begins.

#### Deliverables

- Acceptance contract: Expose CONTINUATION frame codec with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONTINUATION frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.101.0 (HEADERS frame codec) still passes; no behavior assigned to v0.103.0 (SETTINGS frame codec) is
claimed; and no critical or high finding remains open.

`0.102.0 implementation stop reached. Run pentest for this exact commit.`

### v0.103.0 — SETTINGS frame codec

Status: planned

#### Goal

Deliver **SETTINGS frame codec** as the sole primary capability in this stop. It builds
on v0.102.0 (CONTINUATION frame codec) and must be independently trustworthy before v0.104.0 (SETTINGS semantic application and negotiated-state lifecycle) begins.

#### Deliverables

- Acceptance contract: Expose SETTINGS frame codec with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.102.0 (CONTINUATION frame codec) still passes; no behavior assigned to v0.104.0 (SETTINGS semantic application and negotiated-state lifecycle) is
claimed; and no critical or high finding remains open.

`0.103.0 implementation stop reached. Run pentest for this exact commit.`

### v0.104.0 — SETTINGS semantic application and negotiated-state lifecycle

Status: planned

#### Goal

Deliver **SETTINGS semantic application and negotiated-state lifecycle** as the sole primary capability in this stop. It builds
on v0.103.0 (SETTINGS frame codec) and must be independently trustworthy before v0.105.0 (PING frame codec) begins.

#### Deliverables

- Acceptance contract: Apply HEADER_TABLE_SIZE, ENABLE_PUSH, MAX_CONCURRENT_STREAMS, INITIAL_WINDOW_SIZE, MAX_FRAME_SIZE, MAX_HEADER_LIST_SIZE, and ENABLE_CONNECT_PROTOCOL with checked stream adjustment, unknown-setting rules, empty ACK enforcement, and distinct pending/acknowledged local settings.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Add the matching state-machine or arithmetic model/Kani harness now, including cancellation and generation reuse where applicable.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS semantic application and negotiated-state lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.103.0 (SETTINGS frame codec) still passes; no behavior assigned to v0.105.0 (PING frame codec) is
claimed; and no critical or high finding remains open.

`0.104.0 implementation stop reached. Run pentest for this exact commit.`

### v0.105.0 — PING frame codec

Status: planned

#### Goal

Deliver **PING frame codec** as the sole primary capability in this stop. It builds
on v0.104.0 (SETTINGS semantic application and negotiated-state lifecycle) and must be independently trustworthy before v0.106.0 (GOAWAY frame codec) begins.

#### Deliverables

- Acceptance contract: Expose PING frame codec with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PING frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.104.0 (SETTINGS semantic application and negotiated-state lifecycle) still passes; no behavior assigned to v0.106.0 (GOAWAY frame codec) is
claimed; and no critical or high finding remains open.

`0.105.0 implementation stop reached. Run pentest for this exact commit.`

### v0.106.0 — GOAWAY frame codec

Status: planned

#### Goal

Deliver **GOAWAY frame codec** as the sole primary capability in this stop. It builds
on v0.105.0 (PING frame codec) and must be independently trustworthy before v0.107.0 (RST_STREAM frame codec) begins.

#### Deliverables

- Acceptance contract: Expose GOAWAY frame codec with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The GOAWAY frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.105.0 (PING frame codec) still passes; no behavior assigned to v0.107.0 (RST_STREAM frame codec) is
claimed; and no critical or high finding remains open.

`0.106.0 implementation stop reached. Run pentest for this exact commit.`

### v0.107.0 — RST_STREAM frame codec

Status: planned

#### Goal

Deliver **RST_STREAM frame codec** as the sole primary capability in this stop. It builds
on v0.106.0 (GOAWAY frame codec) and must be independently trustworthy before v0.108.0 (WINDOW_UPDATE codec and checked windows) begins.

#### Deliverables

- Acceptance contract: Expose RST_STREAM frame codec with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RST_STREAM frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.106.0 (GOAWAY frame codec) still passes; no behavior assigned to v0.108.0 (WINDOW_UPDATE codec and checked windows) is
claimed; and no critical or high finding remains open.

`0.107.0 implementation stop reached. Run pentest for this exact commit.`

### v0.108.0 — WINDOW_UPDATE codec and checked windows

Status: planned

#### Goal

Deliver **WINDOW_UPDATE codec and checked windows** as the sole primary capability in this stop. It builds
on v0.107.0 (RST_STREAM frame codec) and must be independently trustworthy before v0.109.0 (Legacy PRIORITY frame handling) begins.

#### Deliverables

- Acceptance contract: Expose WINDOW_UPDATE codec and checked windows with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WINDOW_UPDATE codec and checked windows contract and all previously implemented relevant behavior have
reproducible evidence; v0.107.0 (RST_STREAM frame codec) still passes; no behavior assigned to v0.109.0 (Legacy PRIORITY frame handling) is
claimed; and no critical or high finding remains open.

`0.108.0 implementation stop reached. Run pentest for this exact commit.`

### v0.109.0 — Legacy PRIORITY frame handling

Status: planned

#### Goal

Deliver **Legacy PRIORITY frame handling** as the sole primary capability in this stop. It builds
on v0.108.0 (WINDOW_UPDATE codec and checked windows) and must be independently trustworthy before v0.110.0 (PUSH_PROMISE frame handling) begins.

#### Deliverables

- Acceptance contract: Expose Legacy PRIORITY frame handling with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Legacy PRIORITY frame handling and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Legacy PRIORITY frame handling contract and all previously implemented relevant behavior have
reproducible evidence; v0.108.0 (WINDOW_UPDATE codec and checked windows) still passes; no behavior assigned to v0.110.0 (PUSH_PROMISE frame handling) is
claimed; and no critical or high finding remains open.

`0.109.0 implementation stop reached. Run pentest for this exact commit.`

### v0.110.0 — PUSH_PROMISE frame handling

Status: planned

#### Goal

Deliver **PUSH_PROMISE frame handling** as the sole primary capability in this stop. It builds
on v0.109.0 (Legacy PRIORITY frame handling) and must be independently trustworthy before v0.111.0 (Unknown-frame extension policy) begins.

#### Deliverables

- Acceptance contract: Expose PUSH_PROMISE frame handling with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PUSH_PROMISE frame handling contract and all previously implemented relevant behavior have
reproducible evidence; v0.109.0 (Legacy PRIORITY frame handling) still passes; no behavior assigned to v0.111.0 (Unknown-frame extension policy) is
claimed; and no critical or high finding remains open.

`0.110.0 implementation stop reached. Run pentest for this exact commit.`

### v0.111.0 — Unknown-frame extension policy

Status: planned

#### Goal

Deliver **Unknown-frame extension policy** as the sole primary capability in this stop. It builds
on v0.110.0 (PUSH_PROMISE frame handling) and must be independently trustworthy before v0.112.0 (HTTP/2 stream-identifier rules) begins.

#### Deliverables

- Acceptance contract: Expose Unknown-frame extension policy with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Create or extend the malformed and fragmented HTTP/2 frame fuzz target when this codec lands.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Unknown-frame extension policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.110.0 (PUSH_PROMISE frame handling) still passes; no behavior assigned to v0.112.0 (HTTP/2 stream-identifier rules) is
claimed; and no critical or high finding remains open.

`0.111.0 implementation stop reached. Run pentest for this exact commit.`

### v0.112.0 — HTTP/2 stream-identifier rules

Status: planned

#### Goal

Deliver **HTTP/2 stream-identifier rules** as the sole primary capability in this stop. It builds
on v0.111.0 (Unknown-frame extension policy) and must be independently trustworthy before v0.113.0 (Generation-checked stream table and tombstones) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/2 stream-identifier rules with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/2 stream-identifier rules and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 stream-identifier rules contract and all previously implemented relevant behavior have
reproducible evidence; v0.111.0 (Unknown-frame extension policy) still passes; no behavior assigned to v0.113.0 (Generation-checked stream table and tombstones) is
claimed; and no critical or high finding remains open.

`0.112.0 implementation stop reached. Run pentest for this exact commit.`

### v0.113.0 — Generation-checked stream table and tombstones

Status: planned

#### Goal

Deliver **Generation-checked stream table and tombstones** as the sole primary capability in this stop. It builds
on v0.112.0 (HTTP/2 stream-identifier rules) and must be independently trustworthy before v0.114.0 (Exhaustive stream-state graph) begins.

#### Deliverables

- Acceptance contract: Expose Generation-checked stream table and tombstones with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Add the matching state-machine or arithmetic model/Kani harness now, including cancellation and generation reuse where applicable.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Generation-checked stream table and tombstones contract and all previously implemented relevant behavior have
reproducible evidence; v0.112.0 (HTTP/2 stream-identifier rules) still passes; no behavior assigned to v0.114.0 (Exhaustive stream-state graph) is
claimed; and no critical or high finding remains open.

`0.113.0 implementation stop reached. Run pentest for this exact commit.`

### v0.114.0 — Exhaustive stream-state graph

Status: planned

#### Goal

Deliver **Exhaustive stream-state graph** as the sole primary capability in this stop. It builds
on v0.113.0 (Generation-checked stream table and tombstones) and must be independently trustworthy before v0.115.0 (Connection sequencing and error-scope deltas) begins.

#### Deliverables

- Acceptance contract: Expose Exhaustive stream-state graph with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Add the matching state-machine or arithmetic model/Kani harness now, including cancellation and generation reuse where applicable.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Exhaustive stream-state graph contract and all previously implemented relevant behavior have
reproducible evidence; v0.113.0 (Generation-checked stream table and tombstones) still passes; no behavior assigned to v0.115.0 (Connection sequencing and error-scope deltas) is
claimed; and no critical or high finding remains open.

`0.114.0 implementation stop reached. Run pentest for this exact commit.`

### v0.115.0 — Connection sequencing and error-scope deltas

Status: planned

#### Goal

Deliver **Connection sequencing and error-scope deltas** as the sole primary capability in this stop. It builds
on v0.114.0 (Exhaustive stream-state graph) and must be independently trustworthy before v0.116.0 (Atomic HPACK header-block integration) begins.

#### Deliverables

- Acceptance contract: Expose Connection sequencing and error-scope deltas with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Connection sequencing and error-scope deltas and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection sequencing and error-scope deltas contract and all previously implemented relevant behavior have
reproducible evidence; v0.114.0 (Exhaustive stream-state graph) still passes; no behavior assigned to v0.116.0 (Atomic HPACK header-block integration) is
claimed; and no critical or high finding remains open.

`0.115.0 implementation stop reached. Run pentest for this exact commit.`

### v0.116.0 — Atomic HPACK header-block integration

Status: planned

#### Goal

Deliver **Atomic HPACK header-block integration** as the sole primary capability in this stop. It builds
on v0.115.0 (Connection sequencing and error-scope deltas) and must be independently trustworthy before v0.117.0 (Pseudo-field ordering and uniqueness) begins.

#### Deliverables

- Acceptance contract: Expose Atomic HPACK header-block integration with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Atomic HPACK header-block integration and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Atomic HPACK header-block integration contract and all previously implemented relevant behavior have
reproducible evidence; v0.115.0 (Connection sequencing and error-scope deltas) still passes; no behavior assigned to v0.117.0 (Pseudo-field ordering and uniqueness) is
claimed; and no critical or high finding remains open.

`0.116.0 implementation stop reached. Run pentest for this exact commit.`

### v0.117.0 — Pseudo-field ordering and uniqueness

Status: planned

#### Goal

Deliver **Pseudo-field ordering and uniqueness** as the sole primary capability in this stop. It builds
on v0.116.0 (Atomic HPACK header-block integration) and must be independently trustworthy before v0.118.0 (Connection-specific field and TE validation) begins.

#### Deliverables

- Acceptance contract: Expose Pseudo-field ordering and uniqueness with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Pseudo-field ordering and uniqueness and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Pseudo-field ordering and uniqueness contract and all previously implemented relevant behavior have
reproducible evidence; v0.116.0 (Atomic HPACK header-block integration) still passes; no behavior assigned to v0.118.0 (Connection-specific field and TE validation) is
claimed; and no critical or high finding remains open.

`0.117.0 implementation stop reached. Run pentest for this exact commit.`

### v0.118.0 — Connection-specific field and TE validation

Status: planned

#### Goal

Deliver **Connection-specific field and TE validation** as the sole primary capability in this stop. It builds
on v0.117.0 (Pseudo-field ordering and uniqueness) and must be independently trustworthy before v0.119.0 (HTTP/2 request mapping) begins.

#### Deliverables

- Acceptance contract: Expose Connection-specific field and TE validation with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Connection-specific field and TE validation and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection-specific field and TE validation contract and all previously implemented relevant behavior have
reproducible evidence; v0.117.0 (Pseudo-field ordering and uniqueness) still passes; no behavior assigned to v0.119.0 (HTTP/2 request mapping) is
claimed; and no critical or high finding remains open.

`0.118.0 implementation stop reached. Run pentest for this exact commit.`

### v0.119.0 — HTTP/2 request mapping

Status: planned

#### Goal

Deliver **HTTP/2 request mapping** as the sole primary capability in this stop. It builds
on v0.118.0 (Connection-specific field and TE validation) and must be independently trustworthy before v0.120.0 (HTTP/2 response mapping) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/2 request mapping with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/2 request mapping and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 request mapping contract and all previously implemented relevant behavior have
reproducible evidence; v0.118.0 (Connection-specific field and TE validation) still passes; no behavior assigned to v0.120.0 (HTTP/2 response mapping) is
claimed; and no critical or high finding remains open.

`0.119.0 implementation stop reached. Run pentest for this exact commit.`

### v0.120.0 — HTTP/2 response mapping

Status: planned

#### Goal

Deliver **HTTP/2 response mapping** as the sole primary capability in this stop. It builds
on v0.119.0 (HTTP/2 request mapping) and must be independently trustworthy before v0.121.0 (HTTP/2 malformed initial-field-block publication barrier) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/2 response mapping with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/2 response mapping and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 response mapping contract and all previously implemented relevant behavior have
reproducible evidence; v0.119.0 (HTTP/2 request mapping) still passes; no behavior assigned to v0.121.0 (HTTP/2 malformed initial-field-block publication barrier) is
claimed; and no critical or high finding remains open.

`0.120.0 implementation stop reached. Run pentest for this exact commit.`

### v0.121.0 — HTTP/2 malformed initial-field-block publication barrier

Status: planned

#### Goal

Deliver **HTTP/2 malformed initial-field-block publication barrier** as the sole primary capability in this stop. It builds
on v0.120.0 (HTTP/2 response mapping) and must be independently trustworthy before v0.122.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) begins.

#### Deliverables

- Acceptance contract: Reject uppercase names, NUL/CR/LF, forbidden whitespace, invalid or missing context-specific pseudo-fields, and pseudo-fields in trailers before application publication.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/2 malformed initial-field-block publication barrier and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 malformed initial-field-block publication barrier contract and all previously implemented relevant behavior have
reproducible evidence; v0.120.0 (HTTP/2 response mapping) still passes; no behavior assigned to v0.122.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) is
claimed; and no critical or high finding remains open.

`0.121.0 implementation stop reached. Run pentest for this exact commit.`

### v0.122.0 — HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation

Status: planned

#### Goal

Deliver **HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation** as the sole primary capability in this stop. It builds
on v0.121.0 (HTTP/2 malformed initial-field-block publication barrier) and must be independently trustworthy before v0.123.0 (Informational responses and trailers) begins.

#### Deliverables

- Acceptance contract: Reconcile content-length with DATA octets and enforce final-response, body-forbidden, trailer, DATA-after-trailer, and END_STREAM ordering for requests, responses, and CONNECT.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation contract and all previously implemented relevant behavior have
reproducible evidence; v0.121.0 (HTTP/2 malformed initial-field-block publication barrier) still passes; no behavior assigned to v0.123.0 (Informational responses and trailers) is
claimed; and no critical or high finding remains open.

`0.122.0 implementation stop reached. Run pentest for this exact commit.`

### v0.123.0 — Informational responses and trailers

Status: planned

#### Goal

Deliver **Informational responses and trailers** as the sole primary capability in this stop. It builds
on v0.122.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) and must be independently trustworthy before v0.124.0 (Cookie field combination and Set-Cookie preservation) begins.

#### Deliverables

- Acceptance contract: Expose Informational responses and trailers with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Informational responses and trailers and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Informational responses and trailers contract and all previously implemented relevant behavior have
reproducible evidence; v0.122.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) still passes; no behavior assigned to v0.124.0 (Cookie field combination and Set-Cookie preservation) is
claimed; and no critical or high finding remains open.

`0.123.0 implementation stop reached. Run pentest for this exact commit.`

### v0.124.0 — Cookie field combination and Set-Cookie preservation

Status: planned

#### Goal

Deliver **Cookie field combination and Set-Cookie preservation** as the sole primary capability in this stop. It builds
on v0.123.0 (Informational responses and trailers) and must be independently trustworthy before v0.125.0 (Stream flow control) begins.

#### Deliverables

- Acceptance contract: Expose Cookie field combination and Set-Cookie preservation with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Cookie field combination and Set-Cookie preservation and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Cookie field combination and Set-Cookie preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.123.0 (Informational responses and trailers) still passes; no behavior assigned to v0.125.0 (Stream flow control) is
claimed; and no critical or high finding remains open.

`0.124.0 implementation stop reached. Run pentest for this exact commit.`

### v0.125.0 — Stream flow control

Status: planned

#### Goal

Deliver **Stream flow control** as the sole primary capability in this stop. It builds
on v0.124.0 (Cookie field combination and Set-Cookie preservation) and must be independently trustworthy before v0.126.0 (Connection flow control) begins.

#### Deliverables

- Acceptance contract: Expose Stream flow control with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Add the matching state-machine or arithmetic model/Kani harness now, including cancellation and generation reuse where applicable.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Stream flow control contract and all previously implemented relevant behavior have
reproducible evidence; v0.124.0 (Cookie field combination and Set-Cookie preservation) still passes; no behavior assigned to v0.126.0 (Connection flow control) is
claimed; and no critical or high finding remains open.

`0.125.0 implementation stop reached. Run pentest for this exact commit.`

### v0.126.0 — Connection flow control

Status: planned

#### Goal

Deliver **Connection flow control** as the sole primary capability in this stop. It builds
on v0.125.0 (Stream flow control) and must be independently trustworthy before v0.127.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) begins.

#### Deliverables

- Acceptance contract: Expose Connection flow control with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Add the matching state-machine or arithmetic model/Kani harness now, including cancellation and generation reuse where applicable.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection flow control contract and all previously implemented relevant behavior have
reproducible evidence; v0.125.0 (Stream flow control) still passes; no behavior assigned to v0.127.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) is
claimed; and no critical or high finding remains open.

`0.126.0 implementation stop reached. Run pentest for this exact commit.`

### v0.127.0 — HTTP/2 body cancellation, reset, and flow-credit lifecycle

Status: planned

#### Goal

Deliver **HTTP/2 body cancellation, reset, and flow-credit lifecycle** as the sole primary capability in this stop. It builds
on v0.126.0 (Connection flow control) and must be independently trustworthy before v0.128.0 (SETTINGS outstanding-ACK accounting) begins.

#### Deliverables

- Acceptance contract: Emit at most one RST_STREAM, account discarded DATA credit, tolerate bounded in-flight frames, discard queued output after reset, resolve END_STREAM/GOAWAY/shutdown races, and recycle only after connection effects.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Add the matching state-machine or arithmetic model/Kani harness now, including cancellation and generation reuse where applicable.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 body cancellation, reset, and flow-credit lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.126.0 (Connection flow control) still passes; no behavior assigned to v0.128.0 (SETTINGS outstanding-ACK accounting) is
claimed; and no critical or high finding remains open.

`0.127.0 implementation stop reached. Run pentest for this exact commit.`

### v0.128.0 — SETTINGS outstanding-ACK accounting

Status: planned

#### Goal

Deliver **SETTINGS outstanding-ACK accounting** as the sole primary capability in this stop. It builds
on v0.127.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) and must be independently trustworthy before v0.129.0 (Bounded stream admission) begins.

#### Deliverables

- Acceptance contract: Expose SETTINGS outstanding-ACK accounting with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test SETTINGS outstanding-ACK accounting and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS outstanding-ACK accounting contract and all previously implemented relevant behavior have
reproducible evidence; v0.127.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) still passes; no behavior assigned to v0.129.0 (Bounded stream admission) is
claimed; and no critical or high finding remains open.

`0.128.0 implementation stop reached. Run pentest for this exact commit.`

### v0.129.0 — Bounded stream admission

Status: planned

#### Goal

Deliver **Bounded stream admission** as the sole primary capability in this stop. It builds
on v0.128.0 (SETTINGS outstanding-ACK accounting) and must be independently trustworthy before v0.130.0 (Bounded outbound scheduling) begins.

#### Deliverables

- Acceptance contract: Expose Bounded stream admission with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Add the matching state-machine or arithmetic model/Kani harness now, including cancellation and generation reuse where applicable.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Bounded stream admission contract and all previously implemented relevant behavior have
reproducible evidence; v0.128.0 (SETTINGS outstanding-ACK accounting) still passes; no behavior assigned to v0.130.0 (Bounded outbound scheduling) is
claimed; and no critical or high finding remains open.

`0.129.0 implementation stop reached. Run pentest for this exact commit.`

### v0.130.0 — Bounded outbound scheduling

Status: planned

#### Goal

Deliver **Bounded outbound scheduling** as the sole primary capability in this stop. It builds
on v0.129.0 (Bounded stream admission) and must be independently trustworthy before v0.131.0 (GOAWAY cutoff and retry classification) begins.

#### Deliverables

- Acceptance contract: Expose Bounded outbound scheduling with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Add the matching state-machine or arithmetic model/Kani harness now, including cancellation and generation reuse where applicable.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Bounded outbound scheduling contract and all previously implemented relevant behavior have
reproducible evidence; v0.129.0 (Bounded stream admission) still passes; no behavior assigned to v0.131.0 (GOAWAY cutoff and retry classification) is
claimed; and no critical or high finding remains open.

`0.130.0 implementation stop reached. Run pentest for this exact commit.`

### v0.131.0 — GOAWAY cutoff and retry classification

Status: planned

#### Goal

Deliver **GOAWAY cutoff and retry classification** as the sole primary capability in this stop. It builds
on v0.130.0 (Bounded outbound scheduling) and must be independently trustworthy before v0.132.0 (Server-push lifecycle) begins.

#### Deliverables

- Acceptance contract: Expose GOAWAY cutoff and retry classification with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Add the matching state-machine or arithmetic model/Kani harness now, including cancellation and generation reuse where applicable.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The GOAWAY cutoff and retry classification contract and all previously implemented relevant behavior have
reproducible evidence; v0.130.0 (Bounded outbound scheduling) still passes; no behavior assigned to v0.132.0 (Server-push lifecycle) is
claimed; and no critical or high finding remains open.

`0.131.0 implementation stop reached. Run pentest for this exact commit.`

### v0.132.0 — Server-push lifecycle

Status: planned

#### Goal

Deliver **Server-push lifecycle** as the sole primary capability in this stop. It builds
on v0.131.0 (GOAWAY cutoff and retry classification) and must be independently trustworthy before v0.133.0 (ALPN and cleartext prior-knowledge selection) begins.

#### Deliverables

- Acceptance contract: Expose Server-push lifecycle with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Server-push lifecycle and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Server-push lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.131.0 (GOAWAY cutoff and retry classification) still passes; no behavior assigned to v0.133.0 (ALPN and cleartext prior-knowledge selection) is
claimed; and no critical or high finding remains open.

`0.132.0 implementation stop reached. Run pentest for this exact commit.`

### v0.133.0 — ALPN and cleartext prior-knowledge selection

Status: planned

#### Goal

Deliver **ALPN and cleartext prior-knowledge selection** as the sole primary capability in this stop. It builds
on v0.132.0 (Server-push lifecycle) and must be independently trustworthy before v0.134.0 (Independent HTTP/2 rate and work budgets) begins.

#### Deliverables

- Acceptance contract: Expose ALPN and cleartext prior-knowledge selection with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test ALPN and cleartext prior-knowledge selection and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The ALPN and cleartext prior-knowledge selection contract and all previously implemented relevant behavior have
reproducible evidence; v0.132.0 (Server-push lifecycle) still passes; no behavior assigned to v0.134.0 (Independent HTTP/2 rate and work budgets) is
claimed; and no critical or high finding remains open.

`0.133.0 implementation stop reached. Run pentest for this exact commit.`

### v0.134.0 — Independent HTTP/2 rate and work budgets

Status: planned

#### Goal

Deliver **Independent HTTP/2 rate and work budgets** as the sole primary capability in this stop. It builds
on v0.133.0 (ALPN and cleartext prior-knowledge selection) and must be independently trustworthy before v0.135.0 (Rapid-reset defenses) begins.

#### Deliverables

- Acceptance contract: Expose Independent HTTP/2 rate and work budgets with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Independent HTTP/2 rate and work budgets and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Independent HTTP/2 rate and work budgets contract and all previously implemented relevant behavior have
reproducible evidence; v0.133.0 (ALPN and cleartext prior-knowledge selection) still passes; no behavior assigned to v0.135.0 (Rapid-reset defenses) is
claimed; and no critical or high finding remains open.

`0.134.0 implementation stop reached. Run pentest for this exact commit.`

### v0.135.0 — Rapid-reset defenses

Status: planned

#### Goal

Deliver **Rapid-reset defenses** as the sole primary capability in this stop. It builds
on v0.134.0 (Independent HTTP/2 rate and work budgets) and must be independently trustworthy before v0.136.0 (SETTINGS amplification defenses) begins.

#### Deliverables

- Acceptance contract: Expose Rapid-reset defenses with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Rapid-reset defenses and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Rapid-reset defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.134.0 (Independent HTTP/2 rate and work budgets) still passes; no behavior assigned to v0.136.0 (SETTINGS amplification defenses) is
claimed; and no critical or high finding remains open.

`0.135.0 implementation stop reached. Run pentest for this exact commit.`

### v0.136.0 — SETTINGS amplification defenses

Status: planned

#### Goal

Deliver **SETTINGS amplification defenses** as the sole primary capability in this stop. It builds
on v0.135.0 (Rapid-reset defenses) and must be independently trustworthy before v0.137.0 (PING flood defenses) begins.

#### Deliverables

- Acceptance contract: Expose SETTINGS amplification defenses with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test SETTINGS amplification defenses and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS amplification defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.135.0 (Rapid-reset defenses) still passes; no behavior assigned to v0.137.0 (PING flood defenses) is
claimed; and no critical or high finding remains open.

`0.136.0 implementation stop reached. Run pentest for this exact commit.`

### v0.137.0 — PING flood defenses

Status: planned

#### Goal

Deliver **PING flood defenses** as the sole primary capability in this stop. It builds
on v0.136.0 (SETTINGS amplification defenses) and must be independently trustworthy before v0.138.0 (CONTINUATION bomb defenses) begins.

#### Deliverables

- Acceptance contract: Expose PING flood defenses with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test PING flood defenses and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PING flood defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.136.0 (SETTINGS amplification defenses) still passes; no behavior assigned to v0.138.0 (CONTINUATION bomb defenses) is
claimed; and no critical or high finding remains open.

`0.137.0 implementation stop reached. Run pentest for this exact commit.`

### v0.138.0 — CONTINUATION bomb defenses

Status: planned

#### Goal

Deliver **CONTINUATION bomb defenses** as the sole primary capability in this stop. It builds
on v0.137.0 (PING flood defenses) and must be independently trustworthy before v0.139.0 (WINDOW_UPDATE churn defenses) begins.

#### Deliverables

- Acceptance contract: Expose CONTINUATION bomb defenses with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test CONTINUATION bomb defenses and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONTINUATION bomb defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.137.0 (PING flood defenses) still passes; no behavior assigned to v0.139.0 (WINDOW_UPDATE churn defenses) is
claimed; and no critical or high finding remains open.

`0.138.0 implementation stop reached. Run pentest for this exact commit.`

### v0.139.0 — WINDOW_UPDATE churn defenses

Status: planned

#### Goal

Deliver **WINDOW_UPDATE churn defenses** as the sole primary capability in this stop. It builds
on v0.138.0 (CONTINUATION bomb defenses) and must be independently trustworthy before v0.140.0 (Reserved control-output queues) begins.

#### Deliverables

- Acceptance contract: Expose WINDOW_UPDATE churn defenses with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test WINDOW_UPDATE churn defenses and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WINDOW_UPDATE churn defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.138.0 (CONTINUATION bomb defenses) still passes; no behavior assigned to v0.140.0 (Reserved control-output queues) is
claimed; and no critical or high finding remains open.

`0.139.0 implementation stop reached. Run pentest for this exact commit.`

### v0.140.0 — Reserved control-output queues

Status: planned

#### Goal

Deliver **Reserved control-output queues** as the sole primary capability in this stop. It builds
on v0.139.0 (WINDOW_UPDATE churn defenses) and must be independently trustworthy before v0.141.0 (HTTP/2 conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Expose Reserved control-output queues with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Reserved control-output queues and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Reserved control-output queues contract and all previously implemented relevant behavior have
reproducible evidence; v0.139.0 (WINDOW_UPDATE churn defenses) still passes; no behavior assigned to v0.141.0 (HTTP/2 conformance audit and pentest) is
claimed; and no critical or high finding remains open.

`0.140.0 implementation stop reached. Run pentest for this exact commit.`

### v0.141.0 — HTTP/2 conformance audit and pentest

Status: planned

#### Goal

Deliver **HTTP/2 conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.140.0 (Reserved control-output queues) and must be independently trustworthy before v0.142.0 (HTTP/1 and HTTP/2 translation model) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/2 conformance audit and pentest with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: HPACK compression state stays synchronized across semantic rejection; HTTP/2 validates typed deltas before legal state commits and keeps stream, flow-credit, and control-output lifecycles bounded.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/2 conformance audit and pentest and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.140.0 (Reserved control-output queues) still passes; no behavior assigned to v0.142.0 (HTTP/1 and HTTP/2 translation model) is
claimed; and no critical or high finding remains open.

`0.141.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 4 — Proxy, client, server, and public APIs

Phase contract: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.

### v0.142.0 — HTTP/1 and HTTP/2 translation model

Status: planned

#### Goal

Deliver **HTTP/1 and HTTP/2 translation model** as the sole primary capability in this stop. It builds
on v0.141.0 (HTTP/2 conformance audit and pentest) and must be independently trustworthy before v0.143.0 (Effective URI and authority consistency) begins.

#### Deliverables

- Acceptance contract: Expose HTTP/1 and HTTP/2 translation model with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test HTTP/1 and HTTP/2 translation model and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 and HTTP/2 translation model contract and all previously implemented relevant behavior have
reproducible evidence; v0.141.0 (HTTP/2 conformance audit and pentest) still passes; no behavior assigned to v0.143.0 (Effective URI and authority consistency) is
claimed; and no critical or high finding remains open.

`0.142.0 implementation stop reached. Run pentest for this exact commit.`

### v0.143.0 — Effective URI and authority consistency

Status: planned

#### Goal

Deliver **Effective URI and authority consistency** as the sole primary capability in this stop. It builds
on v0.142.0 (HTTP/1 and HTTP/2 translation model) and must be independently trustworthy before v0.144.0 (Connection-field stripping, Via, and cache preservation) begins.

#### Deliverables

- Acceptance contract: Expose Effective URI and authority consistency with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Effective URI and authority consistency and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Effective URI and authority consistency contract and all previously implemented relevant behavior have
reproducible evidence; v0.142.0 (HTTP/1 and HTTP/2 translation model) still passes; no behavior assigned to v0.144.0 (Connection-field stripping, Via, and cache preservation) is
claimed; and no critical or high finding remains open.

`0.143.0 implementation stop reached. Run pentest for this exact commit.`

### v0.144.0 — Connection-field stripping, Via, and cache preservation

Status: planned

#### Goal

Deliver **Connection-field stripping, Via, and cache preservation** as the sole primary capability in this stop. It builds
on v0.143.0 (Effective URI and authority consistency) and must be independently trustworthy before v0.145.0 (CONNECT translation across HTTP versions) begins.

#### Deliverables

- Acceptance contract: Expose Connection-field stripping, Via, and cache preservation with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Connection-field stripping, Via, and cache preservation and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection-field stripping, Via, and cache preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.143.0 (Effective URI and authority consistency) still passes; no behavior assigned to v0.145.0 (CONNECT translation across HTTP versions) is
claimed; and no critical or high finding remains open.

`0.144.0 implementation stop reached. Run pentest for this exact commit.`

### v0.145.0 — CONNECT translation across HTTP versions

Status: planned

#### Goal

Deliver **CONNECT translation across HTTP versions** as the sole primary capability in this stop. It builds
on v0.144.0 (Connection-field stripping, Via, and cache preservation) and must be independently trustworthy before v0.146.0 (RFC 8441 extended CONNECT) begins.

#### Deliverables

- Acceptance contract: Expose CONNECT translation across HTTP versions with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test CONNECT translation across HTTP versions and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONNECT translation across HTTP versions contract and all previously implemented relevant behavior have
reproducible evidence; v0.144.0 (Connection-field stripping, Via, and cache preservation) still passes; no behavior assigned to v0.146.0 (RFC 8441 extended CONNECT) is
claimed; and no critical or high finding remains open.

`0.145.0 implementation stop reached. Run pentest for this exact commit.`

### v0.146.0 — RFC 8441 extended CONNECT

Status: planned

#### Goal

Deliver **RFC 8441 extended CONNECT** as the sole primary capability in this stop. It builds
on v0.145.0 (CONNECT translation across HTTP versions) and must be independently trustworthy before v0.147.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) begins.

#### Deliverables

- Acceptance contract: Expose RFC 8441 extended CONNECT with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test RFC 8441 extended CONNECT and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RFC 8441 extended CONNECT contract and all previously implemented relevant behavior have
reproducible evidence; v0.145.0 (CONNECT translation across HTTP versions) still passes; no behavior assigned to v0.147.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) is
claimed; and no critical or high finding remains open.

`0.146.0 implementation stop reached. Run pentest for this exact commit.`

### v0.147.0 — WebSocket HTTP/1 to HTTP/2 handshake bridge

Status: planned

#### Goal

Deliver **WebSocket HTTP/1 to HTTP/2 handshake bridge** as the sole primary capability in this stop. It builds
on v0.146.0 (RFC 8441 extended CONNECT) and must be independently trustworthy before v0.148.0 (Structured Fields) begins.

#### Deliverables

- Acceptance contract: Expose WebSocket HTTP/1 to HTTP/2 handshake bridge with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test WebSocket HTTP/1 to HTTP/2 handshake bridge and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WebSocket HTTP/1 to HTTP/2 handshake bridge contract and all previously implemented relevant behavior have
reproducible evidence; v0.146.0 (RFC 8441 extended CONNECT) still passes; no behavior assigned to v0.148.0 (Structured Fields) is
claimed; and no critical or high finding remains open.

`0.147.0 implementation stop reached. Run pentest for this exact commit.`

### v0.148.0 — Structured Fields

Status: planned

#### Goal

Deliver **Structured Fields** as the sole primary capability in this stop. It builds
on v0.147.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) and must be independently trustworthy before v0.149.0 (RFC 9218 priority semantics) begins.

#### Deliverables

- Acceptance contract: Expose Structured Fields with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Structured Fields and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields contract and all previously implemented relevant behavior have
reproducible evidence; v0.147.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) still passes; no behavior assigned to v0.149.0 (RFC 9218 priority semantics) is
claimed; and no critical or high finding remains open.

`0.148.0 implementation stop reached. Run pentest for this exact commit.`

### v0.149.0 — RFC 9218 priority semantics

Status: planned

#### Goal

Deliver **RFC 9218 priority semantics** as the sole primary capability in this stop. It builds
on v0.148.0 (Structured Fields) and must be independently trustworthy before v0.150.0 (PRIORITY_UPDATE frame support) begins.

#### Deliverables

- Acceptance contract: Expose RFC 9218 priority semantics with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test RFC 9218 priority semantics and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RFC 9218 priority semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.148.0 (Structured Fields) still passes; no behavior assigned to v0.150.0 (PRIORITY_UPDATE frame support) is
claimed; and no critical or high finding remains open.

`0.149.0 implementation stop reached. Run pentest for this exact commit.`

### v0.150.0 — PRIORITY_UPDATE frame support

Status: planned

#### Goal

Deliver **PRIORITY_UPDATE frame support** as the sole primary capability in this stop. It builds
on v0.149.0 (RFC 9218 priority semantics) and must be independently trustworthy before v0.151.0 (Client request builder and target forms) begins.

#### Deliverables

- Acceptance contract: Expose PRIORITY_UPDATE frame support with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test PRIORITY_UPDATE frame support and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PRIORITY_UPDATE frame support contract and all previously implemented relevant behavior have
reproducible evidence; v0.149.0 (RFC 9218 priority semantics) still passes; no behavior assigned to v0.151.0 (Client request builder and target forms) is
claimed; and no critical or high finding remains open.

`0.150.0 implementation stop reached. Run pentest for this exact commit.`

### v0.151.0 — Client request builder and target forms

Status: planned

#### Goal

Deliver **Client request builder and target forms** as the sole primary capability in this stop. It builds
on v0.150.0 (PRIORITY_UPDATE frame support) and must be independently trustworthy before v0.152.0 (Client correlation, cancellation, and retry tokens) begins.

#### Deliverables

- Acceptance contract: Expose Client request builder and target forms with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Client request builder and target forms and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Client request builder and target forms contract and all previously implemented relevant behavior have
reproducible evidence; v0.150.0 (PRIORITY_UPDATE frame support) still passes; no behavior assigned to v0.152.0 (Client correlation, cancellation, and retry tokens) is
claimed; and no critical or high finding remains open.

`0.151.0 implementation stop reached. Run pentest for this exact commit.`

### v0.152.0 — Client correlation, cancellation, and retry tokens

Status: planned

#### Goal

Deliver **Client correlation, cancellation, and retry tokens** as the sole primary capability in this stop. It builds
on v0.151.0 (Client request builder and target forms) and must be independently trustworthy before v0.153.0 (Origin-server role API) begins.

#### Deliverables

- Acceptance contract: Expose Client correlation, cancellation, and retry tokens with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Client correlation, cancellation, and retry tokens and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Client correlation, cancellation, and retry tokens contract and all previously implemented relevant behavior have
reproducible evidence; v0.151.0 (Client request builder and target forms) still passes; no behavior assigned to v0.153.0 (Origin-server role API) is
claimed; and no critical or high finding remains open.

`0.152.0 implementation stop reached. Run pentest for this exact commit.`

### v0.153.0 — Origin-server role API

Status: planned

#### Goal

Deliver **Origin-server role API** as the sole primary capability in this stop. It builds
on v0.152.0 (Client correlation, cancellation, and retry tokens) and must be independently trustworthy before v0.154.0 (Forward-proxy role API) begins.

#### Deliverables

- Acceptance contract: Expose Origin-server role API with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Origin-server role API and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Origin-server role API contract and all previously implemented relevant behavior have
reproducible evidence; v0.152.0 (Client correlation, cancellation, and retry tokens) still passes; no behavior assigned to v0.154.0 (Forward-proxy role API) is
claimed; and no critical or high finding remains open.

`0.153.0 implementation stop reached. Run pentest for this exact commit.`

### v0.154.0 — Forward-proxy role API

Status: planned

#### Goal

Deliver **Forward-proxy role API** as the sole primary capability in this stop. It builds
on v0.153.0 (Origin-server role API) and must be independently trustworthy before v0.155.0 (Reverse-proxy and gateway role API) begins.

#### Deliverables

- Acceptance contract: Expose Forward-proxy role API with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Forward-proxy role API and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Forward-proxy role API contract and all previously implemented relevant behavior have
reproducible evidence; v0.153.0 (Origin-server role API) still passes; no behavior assigned to v0.155.0 (Reverse-proxy and gateway role API) is
claimed; and no critical or high finding remains open.

`0.154.0 implementation stop reached. Run pentest for this exact commit.`

### v0.155.0 — Reverse-proxy and gateway role API

Status: planned

#### Goal

Deliver **Reverse-proxy and gateway role API** as the sole primary capability in this stop. It builds
on v0.154.0 (Forward-proxy role API) and must be independently trustworthy before v0.156.0 (Tunnel lifecycle and half-close semantics) begins.

#### Deliverables

- Acceptance contract: Expose Reverse-proxy and gateway role API with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Reverse-proxy and gateway role API and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Reverse-proxy and gateway role API contract and all previously implemented relevant behavior have
reproducible evidence; v0.154.0 (Forward-proxy role API) still passes; no behavior assigned to v0.156.0 (Tunnel lifecycle and half-close semantics) is
claimed; and no critical or high finding remains open.

`0.155.0 implementation stop reached. Run pentest for this exact commit.`

### v0.156.0 — Tunnel lifecycle and half-close semantics

Status: planned

#### Goal

Deliver **Tunnel lifecycle and half-close semantics** as the sole primary capability in this stop. It builds
on v0.155.0 (Reverse-proxy and gateway role API) and must be independently trustworthy before v0.157.0 (Upgrade transformation boundary) begins.

#### Deliverables

- Acceptance contract: Expose Tunnel lifecycle and half-close semantics with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Tunnel lifecycle and half-close semantics and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Tunnel lifecycle and half-close semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.155.0 (Reverse-proxy and gateway role API) still passes; no behavior assigned to v0.157.0 (Upgrade transformation boundary) is
claimed; and no critical or high finding remains open.

`0.156.0 implementation stop reached. Run pentest for this exact commit.`

### v0.157.0 — Upgrade transformation boundary

Status: planned

#### Goal

Deliver **Upgrade transformation boundary** as the sole primary capability in this stop. It builds
on v0.156.0 (Tunnel lifecycle and half-close semantics) and must be independently trustworthy before v0.158.0 (GOAWAY, 421, and retry coordination) begins.

#### Deliverables

- Acceptance contract: Expose Upgrade transformation boundary with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Upgrade transformation boundary and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Upgrade transformation boundary contract and all previously implemented relevant behavior have
reproducible evidence; v0.156.0 (Tunnel lifecycle and half-close semantics) still passes; no behavior assigned to v0.158.0 (GOAWAY, 421, and retry coordination) is
claimed; and no critical or high finding remains open.

`0.157.0 implementation stop reached. Run pentest for this exact commit.`

### v0.158.0 — GOAWAY, 421, and retry coordination

Status: planned

#### Goal

Deliver **GOAWAY, 421, and retry coordination** as the sole primary capability in this stop. It builds
on v0.157.0 (Upgrade transformation boundary) and must be independently trustworthy before v0.159.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) begins.

#### Deliverables

- Acceptance contract: Expose GOAWAY, 421, and retry coordination with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test GOAWAY, 421, and retry coordination and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The GOAWAY, 421, and retry coordination contract and all previously implemented relevant behavior have
reproducible evidence; v0.157.0 (Upgrade transformation boundary) still passes; no behavior assigned to v0.159.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) is
claimed; and no critical or high finding remains open.

`0.158.0 implementation stop reached. Run pentest for this exact commit.`

### v0.159.0 — Authenticated origin authorization and HTTP/2 coalescing metadata

Status: planned

#### Goal

Deliver **Authenticated origin authorization and HTTP/2 coalescing metadata** as the sole primary capability in this stop. It builds
on v0.158.0 (GOAWAY, 421, and retry coordination) and must be independently trustworthy before v0.160.0 (Fixed-capacity caller-storage public API) begins.

#### Deliverables

- Acceptance contract: Expose authenticated SNI, certificate identity, scheme, port, remote endpoint, tunnel authority, and end-origin inputs so callers prevent unauthorized coalescing and retry 421 on a non-coalesced connection.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Authenticated origin authorization and HTTP/2 coalescing metadata and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Authenticated origin authorization and HTTP/2 coalescing metadata contract and all previously implemented relevant behavior have
reproducible evidence; v0.158.0 (GOAWAY, 421, and retry coordination) still passes; no behavior assigned to v0.160.0 (Fixed-capacity caller-storage public API) is
claimed; and no critical or high finding remains open.

`0.159.0 implementation stop reached. Run pentest for this exact commit.`

### v0.160.0 — Fixed-capacity caller-storage public API

Status: planned

#### Goal

Deliver **Fixed-capacity caller-storage public API** as the sole primary capability in this stop. It builds
on v0.159.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) and must be independently trustworthy before v0.161.0 (Optional alloc-backed convenience API) begins.

#### Deliverables

- Acceptance contract: Stabilize borrowed/fixed-capacity APIs first, including acknowledgements, lifetimes, explicit capacity errors, and proof that protocol correctness needs no allocator.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Fixed-capacity caller-storage public API and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Fixed-capacity caller-storage public API contract and all previously implemented relevant behavior have
reproducible evidence; v0.159.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) still passes; no behavior assigned to v0.161.0 (Optional alloc-backed convenience API) is
claimed; and no critical or high finding remains open.

`0.160.0 implementation stop reached. Run pentest for this exact commit.`

### v0.161.0 — Optional alloc-backed convenience API

Status: planned

#### Goal

Deliver **Optional alloc-backed convenience API** as the sole primary capability in this stop. It builds
on v0.160.0 (Fixed-capacity caller-storage public API) and must be independently trustworthy before v0.162.0 (Stable diagnostics and security events) begins.

#### Deliverables

- Acceptance contract: Build the owned layer only as a wrapper reducible to the stable borrowed API, with identical protocol decisions and no alloc-only correctness path.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Optional alloc-backed convenience API and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Optional alloc-backed convenience API contract and all previously implemented relevant behavior have
reproducible evidence; v0.160.0 (Fixed-capacity caller-storage public API) still passes; no behavior assigned to v0.162.0 (Stable diagnostics and security events) is
claimed; and no critical or high finding remains open.

`0.161.0 implementation stop reached. Run pentest for this exact commit.`

### v0.162.0 — Stable diagnostics and security events

Status: planned

#### Goal

Deliver **Stable diagnostics and security events** as the sole primary capability in this stop. It builds
on v0.161.0 (Optional alloc-backed convenience API) and must be independently trustworthy before v0.163.0 (Feature and dependency-policy surface) begins.

#### Deliverables

- Acceptance contract: Expose Stable diagnostics and security events with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Stable diagnostics and security events and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Stable diagnostics and security events contract and all previously implemented relevant behavior have
reproducible evidence; v0.161.0 (Optional alloc-backed convenience API) still passes; no behavior assigned to v0.163.0 (Feature and dependency-policy surface) is
claimed; and no critical or high finding remains open.

`0.162.0 implementation stop reached. Run pentest for this exact commit.`

### v0.163.0 — Feature and dependency-policy surface

Status: planned

#### Goal

Deliver **Feature and dependency-policy surface** as the sole primary capability in this stop. It builds
on v0.162.0 (Stable diagnostics and security events) and must be independently trustworthy before v0.164.0 (Multi-implementation interoperability) begins.

#### Deliverables

- Acceptance contract: Expose Feature and dependency-policy surface with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Feature and dependency-policy surface and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Feature and dependency-policy surface contract and all previously implemented relevant behavior have
reproducible evidence; v0.162.0 (Stable diagnostics and security events) still passes; no behavior assigned to v0.164.0 (Multi-implementation interoperability) is
claimed; and no critical or high finding remains open.

`0.163.0 implementation stop reached. Run pentest for this exact commit.`

### v0.164.0 — Multi-implementation interoperability

Status: planned

#### Goal

Deliver **Multi-implementation interoperability** as the sole primary capability in this stop. It builds
on v0.163.0 (Feature and dependency-policy surface) and must be independently trustworthy before v0.165.0 (Adversarial and stateful fuzz campaign) begins.

#### Deliverables

- Acceptance contract: Expose Multi-implementation interoperability with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Multi-implementation interoperability and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Multi-implementation interoperability contract and all previously implemented relevant behavior have
reproducible evidence; v0.163.0 (Feature and dependency-policy surface) still passes; no behavior assigned to v0.165.0 (Adversarial and stateful fuzz campaign) is
claimed; and no critical or high finding remains open.

`0.164.0 implementation stop reached. Run pentest for this exact commit.`

### v0.165.0 — Adversarial and stateful fuzz campaign

Status: planned

#### Goal

Deliver **Adversarial and stateful fuzz campaign** as the sole primary capability in this stop. It builds
on v0.164.0 (Multi-implementation interoperability) and must be independently trustworthy before v0.166.0 (Compile-fail state and lifetime tests) begins.

#### Deliverables

- Acceptance contract: Expose Adversarial and stateful fuzz campaign with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Adversarial and stateful fuzz campaign and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Adversarial and stateful fuzz campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.164.0 (Multi-implementation interoperability) still passes; no behavior assigned to v0.166.0 (Compile-fail state and lifetime tests) is
claimed; and no critical or high finding remains open.

`0.165.0 implementation stop reached. Run pentest for this exact commit.`

### v0.166.0 — Compile-fail state and lifetime tests

Status: planned

#### Goal

Deliver **Compile-fail state and lifetime tests** as the sole primary capability in this stop. It builds
on v0.165.0 (Adversarial and stateful fuzz campaign) and must be independently trustworthy before v0.167.0 (Long-running soak and exhaustion campaign) begins.

#### Deliverables

- Acceptance contract: Expose Compile-fail state and lifetime tests with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Compile-fail state and lifetime tests and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Compile-fail state and lifetime tests contract and all previously implemented relevant behavior have
reproducible evidence; v0.165.0 (Adversarial and stateful fuzz campaign) still passes; no behavior assigned to v0.167.0 (Long-running soak and exhaustion campaign) is
claimed; and no critical or high finding remains open.

`0.166.0 implementation stop reached. Run pentest for this exact commit.`

### v0.167.0 — Long-running soak and exhaustion campaign

Status: planned

#### Goal

Deliver **Long-running soak and exhaustion campaign** as the sole primary capability in this stop. It builds
on v0.166.0 (Compile-fail state and lifetime tests) and must be independently trustworthy before v0.168.0 (Role and API conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Expose Long-running soak and exhaustion campaign with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Long-running soak and exhaustion campaign and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Long-running soak and exhaustion campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.166.0 (Compile-fail state and lifetime tests) still passes; no behavior assigned to v0.168.0 (Role and API conformance audit and pentest) is
claimed; and no critical or high finding remains open.

`0.167.0 implementation stop reached. Run pentest for this exact commit.`

### v0.168.0 — Role and API conformance audit and pentest

Status: planned

#### Goal

Deliver **Role and API conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.167.0 (Long-running soak and exhaustion campaign) and must be independently trustworthy before v0.169.0 (Standard blocking-stream adapter) begins.

#### Deliverables

- Acceptance contract: Expose Role and API conformance audit and pentest with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Role APIs expose only validated messages and authorized origins; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Role and API conformance audit and pentest and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Role and API conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.167.0 (Long-running soak and exhaustion campaign) still passes; no behavior assigned to v0.169.0 (Standard blocking-stream adapter) is
claimed; and no critical or high finding remains open.

`0.168.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 5 — OS, Aesynx readiness, and 1.0 evidence

Phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.

### v0.169.0 — Standard blocking-stream adapter

Status: planned

#### Goal

Deliver **Standard blocking-stream adapter** as the sole primary capability in this stop. It builds
on v0.168.0 (Role and API conformance audit and pentest) and must be independently trustworthy before v0.170.0 (Standard nonblocking-stream adapter) begins.

#### Deliverables

- Acceptance contract: Expose Standard blocking-stream adapter with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Standard blocking-stream adapter and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Standard blocking-stream adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.168.0 (Role and API conformance audit and pentest) still passes; no behavior assigned to v0.170.0 (Standard nonblocking-stream adapter) is
claimed; and no critical or high finding remains open.

`0.169.0 implementation stop reached. Run pentest for this exact commit.`

### v0.170.0 — Standard nonblocking-stream adapter

Status: planned

#### Goal

Deliver **Standard nonblocking-stream adapter** as the sole primary capability in this stop. It builds
on v0.169.0 (Standard blocking-stream adapter) and must be independently trustworthy before v0.171.0 (Brynja TLS provider contract and admission review) begins.

#### Deliverables

- Acceptance contract: Expose Standard nonblocking-stream adapter with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Standard nonblocking-stream adapter and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Standard nonblocking-stream adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.169.0 (Standard blocking-stream adapter) still passes; no behavior assigned to v0.171.0 (Brynja TLS provider contract and admission review) is
claimed; and no critical or high finding remains open.

`0.170.0 implementation stop reached. Run pentest for this exact commit.`

### v0.171.0 — Brynja TLS provider contract and admission review

Status: planned

#### Goal

Deliver **Brynja TLS provider contract and admission review** as the sole primary capability in this stop. It builds
on v0.170.0 (Standard nonblocking-stream adapter) and must be independently trustworthy before v0.172.0 (Separate vef-brynja adapter crate) begins.

#### Deliverables

- Acceptance contract: Expose Brynja TLS provider contract and admission review with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Brynja TLS provider contract and admission review and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Brynja TLS provider contract and admission review contract and all previously implemented relevant behavior have
reproducible evidence; v0.170.0 (Standard nonblocking-stream adapter) still passes; no behavior assigned to v0.172.0 (Separate vef-brynja adapter crate) is
claimed; and no critical or high finding remains open.

`0.171.0 implementation stop reached. Run pentest for this exact commit.`

### v0.172.0 — Separate vef-brynja adapter crate

Status: planned

#### Goal

Deliver **Separate vef-brynja adapter crate** as the sole primary capability in this stop. It builds
on v0.171.0 (Brynja TLS provider contract and admission review) and must be independently trustworthy before v0.173.0 (Authenticated ALPN and HTTP/2 TLS prerequisites) begins.

#### Deliverables

- Acceptance contract: Expose Separate vef-brynja adapter crate with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Separate vef-brynja adapter crate and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Separate vef-brynja adapter crate contract and all previously implemented relevant behavior have
reproducible evidence; v0.171.0 (Brynja TLS provider contract and admission review) still passes; no behavior assigned to v0.173.0 (Authenticated ALPN and HTTP/2 TLS prerequisites) is
claimed; and no critical or high finding remains open.

`0.172.0 implementation stop reached. Run pentest for this exact commit.`

### v0.173.0 — Authenticated ALPN and HTTP/2 TLS prerequisites

Status: planned

#### Goal

Deliver **Authenticated ALPN and HTTP/2 TLS prerequisites** as the sole primary capability in this stop. It builds
on v0.172.0 (Separate vef-brynja adapter crate) and must be independently trustworthy before v0.174.0 (TLS 1.3 early-data prohibition and close semantics) begins.

#### Deliverables

- Acceptance contract: Expose Authenticated ALPN and HTTP/2 TLS prerequisites with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Authenticated ALPN and HTTP/2 TLS prerequisites and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Authenticated ALPN and HTTP/2 TLS prerequisites contract and all previously implemented relevant behavior have
reproducible evidence; v0.172.0 (Separate vef-brynja adapter crate) still passes; no behavior assigned to v0.174.0 (TLS 1.3 early-data prohibition and close semantics) is
claimed; and no critical or high finding remains open.

`0.173.0 implementation stop reached. Run pentest for this exact commit.`

### v0.174.0 — TLS 1.3 early-data prohibition and close semantics

Status: planned

#### Goal

Deliver **TLS 1.3 early-data prohibition and close semantics** as the sole primary capability in this stop. It builds
on v0.173.0 (Authenticated ALPN and HTTP/2 TLS prerequisites) and must be independently trustworthy before v0.175.0 (Aesynx fixed-memory capability profile) begins.

#### Deliverables

- Acceptance contract: Expose TLS 1.3 early-data prohibition and close semantics with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test TLS 1.3 early-data prohibition and close semantics and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The TLS 1.3 early-data prohibition and close semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.173.0 (Authenticated ALPN and HTTP/2 TLS prerequisites) still passes; no behavior assigned to v0.175.0 (Aesynx fixed-memory capability profile) is
claimed; and no critical or high finding remains open.

`0.174.0 implementation stop reached. Run pentest for this exact commit.`

### v0.175.0 — Aesynx fixed-memory capability profile

Status: planned

#### Goal

Deliver **Aesynx fixed-memory capability profile** as the sole primary capability in this stop. It builds
on v0.174.0 (TLS 1.3 early-data prohibition and close semantics) and must be independently trustworthy before v0.176.0 (Aesynx transport and readiness adapter) begins.

#### Deliverables

- Acceptance contract: Expose Aesynx fixed-memory capability profile with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Aesynx fixed-memory capability profile and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx fixed-memory capability profile contract and all previously implemented relevant behavior have
reproducible evidence; v0.174.0 (TLS 1.3 early-data prohibition and close semantics) still passes; no behavior assigned to v0.176.0 (Aesynx transport and readiness adapter) is
claimed; and no critical or high finding remains open.

`0.175.0 implementation stop reached. Run pentest for this exact commit.`

### v0.176.0 — Aesynx transport and readiness adapter

Status: planned

#### Goal

Deliver **Aesynx transport and readiness adapter** as the sole primary capability in this stop. It builds
on v0.175.0 (Aesynx fixed-memory capability profile) and must be independently trustworthy before v0.177.0 (Aesynx timer and deadline adapter) begins.

#### Deliverables

- Acceptance contract: Expose Aesynx transport and readiness adapter with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Aesynx transport and readiness adapter and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx transport and readiness adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.175.0 (Aesynx fixed-memory capability profile) still passes; no behavior assigned to v0.177.0 (Aesynx timer and deadline adapter) is
claimed; and no critical or high finding remains open.

`0.176.0 implementation stop reached. Run pentest for this exact commit.`

### v0.177.0 — Aesynx timer and deadline adapter

Status: planned

#### Goal

Deliver **Aesynx timer and deadline adapter** as the sole primary capability in this stop. It builds
on v0.176.0 (Aesynx transport and readiness adapter) and must be independently trustworthy before v0.178.0 (Aesynx kernel integration tests) begins.

#### Deliverables

- Acceptance contract: Expose Aesynx timer and deadline adapter with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Aesynx timer and deadline adapter and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx timer and deadline adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.176.0 (Aesynx transport and readiness adapter) still passes; no behavior assigned to v0.178.0 (Aesynx kernel integration tests) is
claimed; and no critical or high finding remains open.

`0.177.0 implementation stop reached. Run pentest for this exact commit.`

### v0.178.0 — Aesynx kernel integration tests

Status: planned

#### Goal

Deliver **Aesynx kernel integration tests** as the sole primary capability in this stop. It builds
on v0.177.0 (Aesynx timer and deadline adapter) and must be independently trustworthy before v0.179.0 (Deterministic CPU, stack, code-size, and amplification budgets) begins.

#### Deliverables

- Acceptance contract: Expose Aesynx kernel integration tests with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Aesynx kernel integration tests and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx kernel integration tests contract and all previously implemented relevant behavior have
reproducible evidence; v0.177.0 (Aesynx timer and deadline adapter) still passes; no behavior assigned to v0.179.0 (Deterministic CPU, stack, code-size, and amplification budgets) is
claimed; and no critical or high finding remains open.

`0.178.0 implementation stop reached. Run pentest for this exact commit.`

### v0.179.0 — Deterministic CPU, stack, code-size, and amplification budgets

Status: planned

#### Goal

Deliver **Deterministic CPU, stack, code-size, and amplification budgets** as the sole primary capability in this stop. It builds
on v0.178.0 (Aesynx kernel integration tests) and must be independently trustworthy before v0.180.0 (32-bit target campaign) begins.

#### Deliverables

- Acceptance contract: Measure maximum stack and minimal-feature code size, prohibit peer-controlled recursion, cap work per byte/frame and amplification, detect quadratic work, price one-byte fragmentation, verify scheduler fairness, and document Aesynx arena sizing.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Fail the gate on configured stack, code-size, work, amplification, fragmentation-cost, or fairness regressions.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Deterministic CPU, stack, code-size, and amplification budgets contract and all previously implemented relevant behavior have
reproducible evidence; v0.178.0 (Aesynx kernel integration tests) still passes; no behavior assigned to v0.180.0 (32-bit target campaign) is
claimed; and no critical or high finding remains open.

`0.179.0 implementation stop reached. Run pentest for this exact commit.`

### v0.180.0 — 32-bit target campaign

Status: planned

#### Goal

Deliver **32-bit target campaign** as the sole primary capability in this stop. It builds
on v0.179.0 (Deterministic CPU, stack, code-size, and amplification budgets) and must be independently trustworthy before v0.181.0 (Big-endian target campaign) begins.

#### Deliverables

- Acceptance contract: Expose 32-bit target campaign with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test 32-bit target campaign and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The 32-bit target campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.179.0 (Deterministic CPU, stack, code-size, and amplification budgets) still passes; no behavior assigned to v0.181.0 (Big-endian target campaign) is
claimed; and no critical or high finding remains open.

`0.180.0 implementation stop reached. Run pentest for this exact commit.`

### v0.181.0 — Big-endian target campaign

Status: planned

#### Goal

Deliver **Big-endian target campaign** as the sole primary capability in this stop. It builds
on v0.180.0 (32-bit target campaign) and must be independently trustworthy before v0.182.0 (Cross-architecture campaign) begins.

#### Deliverables

- Acceptance contract: Expose Big-endian target campaign with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Big-endian target campaign and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Big-endian target campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.180.0 (32-bit target campaign) still passes; no behavior assigned to v0.182.0 (Cross-architecture campaign) is
claimed; and no critical or high finding remains open.

`0.181.0 implementation stop reached. Run pentest for this exact commit.`

### v0.182.0 — Cross-architecture campaign

Status: planned

#### Goal

Deliver **Cross-architecture campaign** as the sole primary capability in this stop. It builds
on v0.181.0 (Big-endian target campaign) and must be independently trustworthy before v0.183.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) begins.

#### Deliverables

- Acceptance contract: Expose Cross-architecture campaign with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Cross-architecture campaign and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Cross-architecture campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.181.0 (Big-endian target campaign) still passes; no behavior assigned to v0.183.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) is
claimed; and no critical or high finding remains open.

`0.182.0 implementation stop reached. Run pentest for this exact commit.`

### v0.183.0 — Linux, Windows, BSD, macOS, Android, and iOS matrix

Status: planned

#### Goal

Deliver **Linux, Windows, BSD, macOS, Android, and iOS matrix** as the sole primary capability in this stop. It builds
on v0.182.0 (Cross-architecture campaign) and must be independently trustworthy before v0.184.0 (Kani shared-core proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: Expose Linux, Windows, BSD, macOS, Android, and iOS matrix with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Linux, Windows, BSD, macOS, Android, and iOS matrix and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Linux, Windows, BSD, macOS, Android, and iOS matrix contract and all previously implemented relevant behavior have
reproducible evidence; v0.182.0 (Cross-architecture campaign) still passes; no behavior assigned to v0.184.0 (Kani shared-core proof replay and expansion) is
claimed; and no critical or high finding remains open.

`0.183.0 implementation stop reached. Run pentest for this exact commit.`

### v0.184.0 — Kani shared-core proof replay and expansion

Status: planned

#### Goal

Deliver **Kani shared-core proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.183.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) and must be independently trustworthy before v0.185.0 (Kani HTTP/1 proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: Expose Kani shared-core proof replay and expansion with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Kani shared-core proof replay and expansion and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani shared-core proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.183.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) still passes; no behavior assigned to v0.185.0 (Kani HTTP/1 proof replay and expansion) is
claimed; and no critical or high finding remains open.

`0.184.0 implementation stop reached. Run pentest for this exact commit.`

### v0.185.0 — Kani HTTP/1 proof replay and expansion

Status: planned

#### Goal

Deliver **Kani HTTP/1 proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.184.0 (Kani shared-core proof replay and expansion) and must be independently trustworthy before v0.186.0 (Kani HPACK proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: Expose Kani HTTP/1 proof replay and expansion with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Kani HTTP/1 proof replay and expansion and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani HTTP/1 proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.184.0 (Kani shared-core proof replay and expansion) still passes; no behavior assigned to v0.186.0 (Kani HPACK proof replay and expansion) is
claimed; and no critical or high finding remains open.

`0.185.0 implementation stop reached. Run pentest for this exact commit.`

### v0.186.0 — Kani HPACK proof replay and expansion

Status: planned

#### Goal

Deliver **Kani HPACK proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.185.0 (Kani HTTP/1 proof replay and expansion) and must be independently trustworthy before v0.187.0 (Kani HTTP/2 proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: Expose Kani HPACK proof replay and expansion with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Kani HPACK proof replay and expansion and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani HPACK proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.185.0 (Kani HTTP/1 proof replay and expansion) still passes; no behavior assigned to v0.187.0 (Kani HTTP/2 proof replay and expansion) is
claimed; and no critical or high finding remains open.

`0.186.0 implementation stop reached. Run pentest for this exact commit.`

### v0.187.0 — Kani HTTP/2 proof replay and expansion

Status: planned

#### Goal

Deliver **Kani HTTP/2 proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.186.0 (Kani HPACK proof replay and expansion) and must be independently trustworthy before v0.188.0 (Stateful cargo-fuzz replay and expansion) begins.

#### Deliverables

- Acceptance contract: Expose Kani HTTP/2 proof replay and expansion with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Kani HTTP/2 proof replay and expansion and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani HTTP/2 proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.186.0 (Kani HPACK proof replay and expansion) still passes; no behavior assigned to v0.188.0 (Stateful cargo-fuzz replay and expansion) is
claimed; and no critical or high finding remains open.

`0.187.0 implementation stop reached. Run pentest for this exact commit.`

### v0.188.0 — Stateful cargo-fuzz replay and expansion

Status: planned

#### Goal

Deliver **Stateful cargo-fuzz replay and expansion** as the sole primary capability in this stop. It builds
on v0.187.0 (Kani HTTP/2 proof replay and expansion) and must be independently trustworthy before v0.189.0 (Differential and interoperability campaign) begins.

#### Deliverables

- Acceptance contract: Expose Stateful cargo-fuzz replay and expansion with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Stateful cargo-fuzz replay and expansion and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Stateful cargo-fuzz replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.187.0 (Kani HTTP/2 proof replay and expansion) still passes; no behavior assigned to v0.189.0 (Differential and interoperability campaign) is
claimed; and no critical or high finding remains open.

`0.188.0 implementation stop reached. Run pentest for this exact commit.`

### v0.189.0 — Differential and interoperability campaign

Status: planned

#### Goal

Deliver **Differential and interoperability campaign** as the sole primary capability in this stop. It builds
on v0.188.0 (Stateful cargo-fuzz replay and expansion) and must be independently trustworthy before v0.190.0 (Whole-project conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Expose Differential and interoperability campaign with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Differential and interoperability campaign and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Differential and interoperability campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.188.0 (Stateful cargo-fuzz replay and expansion) still passes; no behavior assigned to v0.190.0 (Whole-project conformance audit and pentest) is
claimed; and no critical or high finding remains open.

`0.189.0 implementation stop reached. Run pentest for this exact commit.`

### v0.190.0 — Whole-project conformance audit and pentest

Status: planned

#### Goal

Deliver **Whole-project conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.189.0 (Differential and interoperability campaign) and must be independently trustworthy before v0.191.0 (Independent security audit) begins.

#### Deliverables

- Acceptance contract: Expose Whole-project conformance audit and pentest with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Whole-project conformance audit and pentest and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Whole-project conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.189.0 (Differential and interoperability campaign) still passes; no behavior assigned to v0.191.0 (Independent security audit) is
claimed; and no critical or high finding remains open.

`0.190.0 implementation stop reached. Run pentest for this exact commit.`

### v0.191.0 — Independent security audit

Status: planned

#### Goal

Deliver **Independent security audit** as the sole primary capability in this stop. It builds
on v0.190.0 (Whole-project conformance audit and pentest) and must be independently trustworthy before v0.192.0 (Audit remediation and API freeze) begins.

#### Deliverables

- Acceptance contract: Expose Independent security audit with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Independent security audit and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Independent security audit contract and all previously implemented relevant behavior have
reproducible evidence; v0.190.0 (Whole-project conformance audit and pentest) still passes; no behavior assigned to v0.192.0 (Audit remediation and API freeze) is
claimed; and no critical or high finding remains open.

`0.191.0 implementation stop reached. Run pentest for this exact commit.`

### v0.192.0 — Audit remediation and API freeze

Status: planned

#### Goal

Deliver **Audit remediation and API freeze** as the sole primary capability in this stop. It builds
on v0.191.0 (Independent security audit) and must be independently trustworthy before v0.193.0 (Documentation, packaging, SBOM, provenance, and RC readiness) begins.

#### Deliverables

- Acceptance contract: Expose Audit remediation and API freeze with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Audit remediation and API freeze and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Audit remediation and API freeze contract and all previously implemented relevant behavior have
reproducible evidence; v0.191.0 (Independent security audit) still passes; no behavior assigned to v0.193.0 (Documentation, packaging, SBOM, provenance, and RC readiness) is
claimed; and no critical or high finding remains open.

`0.192.0 implementation stop reached. Run pentest for this exact commit.`

### v0.193.0 — Documentation, packaging, SBOM, provenance, and RC readiness

Status: planned

#### Goal

Deliver **Documentation, packaging, SBOM, provenance, and RC readiness** as the sole primary capability in this stop. It builds
on v0.192.0 (Audit remediation and API freeze) and must be independently trustworthy before the 1.0 release-candidate sequence begins.

#### Deliverables

- Acceptance contract: Expose Documentation, packaging, SBOM, provenance, and RC readiness with explicit inputs, outputs, limits, state transitions, and error scope; do not implement behavior assigned to a later milestone.
- Preserve the phase invariant: Platform adapters cannot alter protocol validity; authenticated selection, deterministic resource ceilings, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error disposition, progress, capacity, cancellation, ownership,
  publication, and state-commit behavior wherever this outcome changes them.
- Update threat model, controls, API documentation, release notes, traceability,
  and relevant conformance corpora.

#### Verification

- Test Documentation, packaging, SBOM, provenance, and RC readiness and all previously implemented relevant behavior with deterministic positive, negative, boundary, truncation, invalid-state, and no-panic cases.
- No test in this milestone may require a capability assigned to a later version.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  declared work/output budgets, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency-policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Documentation, packaging, SBOM, provenance, and RC readiness contract and all previously implemented relevant behavior have
reproducible evidence; v0.192.0 (Audit remediation and API freeze) still passes; no behavior assigned to the 1.0 release-candidate sequence is
claimed; and no critical or high finding remains open.

`0.193.0 implementation stop reached. Run pentest for this exact commit.`

## 1.0 release candidates

### v1.0.0-rc.1

Status: planned

Goal: freeze the public API and expose the complete candidate to public
interoperability, security, usability, and documentation review.

Deliverables: API freeze, migration guidance, package dry runs, generated RFC
and errata coverage, published platform/resource matrices, known limitations,
SBOM, provenance, and complete release evidence.

Verification: replay every component fuzz/model harness, all repository gates,
independent multi-implementation interop, full manual audit, and exact-commit
pentest.

Exit criteria: no new features are accepted and all evidence is reproducible.
`1.0.0-rc.1 implementation stop reached. Run pentest for this exact commit.`

### v1.0.0-rc.2

Status: planned

Goal: remediate RC1 findings without expanding scope.

Deliverables: fixes, regression tests, final source review, RFC/errata coverage,
MSRV/target declarations, and refreshed evidence.

Verification: repeat every fuzz, model, pentest, conformance, interop,
portability, performance-budget, package, SBOM, and provenance gate.

Exit criteria: no unresolved critical/high findings and no unreviewed behavior
change. `1.0.0-rc.2 implementation stop reached. Run pentest for this exact commit.`

### v1.0.0

Status: planned

Goal: publish the first serious production-ready VEF HTTP crate.

Release only when applicable requirements and decisions are verified,
fixed-storage works without allocation, cores are `no_std` and unsafe-free,
HTTP/0.9 is isolated, HTTP/1 inbound/outbound framing and body ownership are
deterministic, HPACK stays synchronized/bounded, HTTP/2 message, state, flow,
and cancellation evidence is exhaustive, TLS early data is disabled, origin
reuse has authenticated inputs, resource budgets pass, role/platform claims
are verified, independent-audit remediation is complete, and HTTP/3 is out of
scope.
