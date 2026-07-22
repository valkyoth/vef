# VEF Release Plan to 1.0

Status: planning document

This is the authoritative implementation sequence. VEF handles
attacker-controlled protocol traffic, so each milestone has one primary
capability and a dependency boundary that can be implemented, reviewed, tested,
pentested, and stopped independently. Split work into patch releases whenever a
security argument no longer fits one review pass.

## Release principles

Every release requires applicable RFC and errata evidence, explicit
non-applicability decisions, bounded-resource behavior, positive and negative
tests, fragmentation coverage for incremental input, adversarial and regression
evidence, documentation, release notes, portability evidence, dependency-policy
proof, a clean SBOM, full-SHA CI pins, CodeQL default-setup review, and an
exact-commit pentest.

Protocol and I/O-contract crates remain `no_std`, safe Rust, and free of
third-party Rust crates. Tool-only fuzzers, model checkers, and interop peers do
not enter the production dependency graph. A first-party Brynja integration is
permitted only through the separately reviewed, non-default `vef-brynja`
adapter milestone.

## Requirement and state rules binding every milestone

- A profile is compliant only when every applicable MUST/MUST NOT is linked to
  verification, every SHOULD decision is recorded, verified/held errata are
  dispositioned, and deviations are explicit.
- Incremental calls consume input, produce output, emit an event, commit a state
  transition, or return a typed blocked condition. Success can never report
  zero progress.
- Peer-controlled sizes and work use checked domains plus reserve, commit, and
  refund accounting. Capacity exhaustion is explicit and never triggers hidden
  growth.
- Parsing and validation produce typed deltas before state commit. Failed work
  cannot partially mutate unrelated state or publish an application-visible
  message.
- Reusable stream/storage slots carry generations; application-held borrowed
  data must be acknowledged before recycling.
- Every source file remains below 500 lines, with module authority and
  cross-module transition tests documented.

## Pentest flow

At each implementation stop, do not tag. Pentest the exact commit, remediate
findings with regression tests, repeat all gates, then add the permanent passing
report as the only file in the direct child of the reviewed commit. Critical or
high findings block release. Phase exits add full-repository manual review,
stateful fuzzing, corpus minimization, multi-peer interoperability,
resource-exhaustion assessment, and a review of all conformance decisions.

## Phase 1 — Foundation and shared semantics

Phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.

### v0.1.0 — Workspace, crate boundaries, licenses, security policy, and release evidence

Status: foundation implementation in progress

#### Goal

Deliver **Workspace, crate boundaries, licenses, security policy, and release evidence** as the only primary capability in this stop. It builds
on the repository foundation and must be independently trustworthy before v0.2.0 (Core module skeleton and authority boundaries) begins.

#### Deliverables

- Implement and document Workspace, crate boundaries, licenses, security policy, and release evidence in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Workspace, crate boundaries, licenses, security policy, and release evidence.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Workspace, crate boundaries, licenses, security policy, and release evidence contract is complete, its named evidence is reproducible, the repository foundation
still passes, no capability assigned to v0.2.0 (Core module skeleton and authority boundaries) is claimed, and no critical or
high finding remains open.

`0.1.0 implementation stop reached. Run pentest for this exact commit.`

### v0.2.0 — Core module skeleton and authority boundaries

Status: planned

#### Goal

Deliver **Core module skeleton and authority boundaries** as the only primary capability in this stop. It builds
on v0.1.0 (Workspace, crate boundaries, licenses, security policy, and release evidence) and must be independently trustworthy before v0.3.0 (Checked byte cursor with no unchecked indexing) begins.

#### Deliverables

- Implement and document Core module skeleton and authority boundaries in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Core module skeleton and authority boundaries.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Core module skeleton and authority boundaries contract is complete, its named evidence is reproducible, v0.1.0 (Workspace, crate boundaries, licenses, security policy, and release evidence)
still passes, no capability assigned to v0.3.0 (Checked byte cursor with no unchecked indexing) is claimed, and no critical or
high finding remains open.

`0.2.0 implementation stop reached. Run pentest for this exact commit.`

### v0.3.0 — Checked byte cursor with no unchecked indexing

Status: planned

#### Goal

Deliver **Checked byte cursor with no unchecked indexing** as the only primary capability in this stop. It builds
on v0.2.0 (Core module skeleton and authority boundaries) and must be independently trustworthy before v0.4.0 (Non-zero parser progress and explicit blocked states) begins.

#### Deliverables

- Implement and document Checked byte cursor with no unchecked indexing in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Checked byte cursor with no unchecked indexing.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Checked byte cursor with no unchecked indexing contract is complete, its named evidence is reproducible, v0.2.0 (Core module skeleton and authority boundaries)
still passes, no capability assigned to v0.4.0 (Non-zero parser progress and explicit blocked states) is claimed, and no critical or
high finding remains open.

`0.3.0 implementation stop reached. Run pentest for this exact commit.`

### v0.4.0 — Non-zero parser progress and explicit blocked states

Status: planned

#### Goal

Deliver **Non-zero parser progress and explicit blocked states** as the only primary capability in this stop. It builds
on v0.3.0 (Checked byte cursor with no unchecked indexing) and must be independently trustworthy before v0.5.0 (Checked protocol-size domains) begins.

#### Deliverables

- Implement and document Non-zero parser progress and explicit blocked states in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Non-zero parser progress and explicit blocked states.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Non-zero parser progress and explicit blocked states contract is complete, its named evidence is reproducible, v0.3.0 (Checked byte cursor with no unchecked indexing)
still passes, no capability assigned to v0.5.0 (Checked protocol-size domains) is claimed, and no critical or
high finding remains open.

`0.4.0 implementation stop reached. Run pentest for this exact commit.`

### v0.5.0 — Checked protocol-size domains

Status: planned

#### Goal

Deliver **Checked protocol-size domains** as the only primary capability in this stop. It builds
on v0.4.0 (Non-zero parser progress and explicit blocked states) and must be independently trustworthy before v0.6.0 (Decode, work, transition, and response budgets) begins.

#### Deliverables

- Implement and document Checked protocol-size domains in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Checked protocol-size domains.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Checked protocol-size domains contract is complete, its named evidence is reproducible, v0.4.0 (Non-zero parser progress and explicit blocked states)
still passes, no capability assigned to v0.6.0 (Decode, work, transition, and response budgets) is claimed, and no critical or
high finding remains open.

`0.5.0 implementation stop reached. Run pentest for this exact commit.`

### v0.6.0 — Decode, work, transition, and response budgets

Status: planned

#### Goal

Deliver **Decode, work, transition, and response budgets** as the only primary capability in this stop. It builds
on v0.5.0 (Checked protocol-size domains) and must be independently trustworthy before v0.7.0 (Caller-owned arenas and fixed-capacity stores) begins.

#### Deliverables

- Implement and document Decode, work, transition, and response budgets in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Decode, work, transition, and response budgets.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Decode, work, transition, and response budgets contract is complete, its named evidence is reproducible, v0.5.0 (Checked protocol-size domains)
still passes, no capability assigned to v0.7.0 (Caller-owned arenas and fixed-capacity stores) is claimed, and no critical or
high finding remains open.

`0.6.0 implementation stop reached. Run pentest for this exact commit.`

### v0.7.0 — Caller-owned arenas and fixed-capacity stores

Status: planned

#### Goal

Deliver **Caller-owned arenas and fixed-capacity stores** as the only primary capability in this stop. It builds
on v0.6.0 (Decode, work, transition, and response budgets) and must be independently trustworthy before v0.8.0 (Structured errors and error-scope taxonomy) begins.

#### Deliverables

- Implement and document Caller-owned arenas and fixed-capacity stores in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Caller-owned arenas and fixed-capacity stores.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Caller-owned arenas and fixed-capacity stores contract is complete, its named evidence is reproducible, v0.6.0 (Decode, work, transition, and response budgets)
still passes, no capability assigned to v0.8.0 (Structured errors and error-scope taxonomy) is claimed, and no critical or
high finding remains open.

`0.7.0 implementation stop reached. Run pentest for this exact commit.`

### v0.8.0 — Structured errors and error-scope taxonomy

Status: planned

#### Goal

Deliver **Structured errors and error-scope taxonomy** as the only primary capability in this stop. It builds
on v0.7.0 (Caller-owned arenas and fixed-capacity stores) and must be independently trustworthy before v0.9.0 (Case-sensitive extension-capable Method) begins.

#### Deliverables

- Implement and document Structured errors and error-scope taxonomy in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Structured errors and error-scope taxonomy.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Structured errors and error-scope taxonomy contract is complete, its named evidence is reproducible, v0.7.0 (Caller-owned arenas and fixed-capacity stores)
still passes, no capability assigned to v0.9.0 (Case-sensitive extension-capable Method) is claimed, and no critical or
high finding remains open.

`0.8.0 implementation stop reached. Run pentest for this exact commit.`

### v0.9.0 — Case-sensitive extension-capable Method

Status: planned

#### Goal

Deliver **Case-sensitive extension-capable Method** as the only primary capability in this stop. It builds
on v0.8.0 (Structured errors and error-scope taxonomy) and must be independently trustworthy before v0.10.0 (Validated StatusCode with unknown-code preservation) begins.

#### Deliverables

- Implement and document Case-sensitive extension-capable Method in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Case-sensitive extension-capable Method.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Case-sensitive extension-capable Method contract is complete, its named evidence is reproducible, v0.8.0 (Structured errors and error-scope taxonomy)
still passes, no capability assigned to v0.10.0 (Validated StatusCode with unknown-code preservation) is claimed, and no critical or
high finding remains open.

`0.9.0 implementation stop reached. Run pentest for this exact commit.`

### v0.10.0 — Validated StatusCode with unknown-code preservation

Status: planned

#### Goal

Deliver **Validated StatusCode with unknown-code preservation** as the only primary capability in this stop. It builds
on v0.9.0 (Case-sensitive extension-capable Method) and must be independently trustworthy before v0.11.0 (HTTP version and wire-version representation) begins.

#### Deliverables

- Implement and document Validated StatusCode with unknown-code preservation in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Validated StatusCode with unknown-code preservation.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Validated StatusCode with unknown-code preservation contract is complete, its named evidence is reproducible, v0.9.0 (Case-sensitive extension-capable Method)
still passes, no capability assigned to v0.11.0 (HTTP version and wire-version representation) is claimed, and no critical or
high finding remains open.

`0.10.0 implementation stop reached. Run pentest for this exact commit.`

### v0.11.0 — HTTP version and wire-version representation

Status: planned

#### Goal

Deliver **HTTP version and wire-version representation** as the only primary capability in this stop. It builds
on v0.10.0 (Validated StatusCode with unknown-code preservation) and must be independently trustworthy before v0.12.0 (Case-insensitive validated FieldName) begins.

#### Deliverables

- Implement and document HTTP version and wire-version representation in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP version and wire-version representation.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP version and wire-version representation contract is complete, its named evidence is reproducible, v0.10.0 (Validated StatusCode with unknown-code preservation)
still passes, no capability assigned to v0.12.0 (Case-insensitive validated FieldName) is claimed, and no critical or
high finding remains open.

`0.11.0 implementation stop reached. Run pentest for this exact commit.`

### v0.12.0 — Case-insensitive validated FieldName

Status: planned

#### Goal

Deliver **Case-insensitive validated FieldName** as the only primary capability in this stop. It builds
on v0.11.0 (HTTP version and wire-version representation) and must be independently trustworthy before v0.13.0 (Byte-oriented FieldValue with raw and semantic views) begins.

#### Deliverables

- Implement and document Case-insensitive validated FieldName in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Case-insensitive validated FieldName.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Case-insensitive validated FieldName contract is complete, its named evidence is reproducible, v0.11.0 (HTTP version and wire-version representation)
still passes, no capability assigned to v0.13.0 (Byte-oriented FieldValue with raw and semantic views) is claimed, and no critical or
high finding remains open.

`0.12.0 implementation stop reached. Run pentest for this exact commit.`

### v0.13.0 — Byte-oriented FieldValue with raw and semantic views

Status: planned

#### Goal

Deliver **Byte-oriented FieldValue with raw and semantic views** as the only primary capability in this stop. It builds
on v0.12.0 (Case-insensitive validated FieldName) and must be independently trustworthy before v0.14.0 (Ordered FieldLine and FieldSection storage) begins.

#### Deliverables

- Implement and document Byte-oriented FieldValue with raw and semantic views in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Byte-oriented FieldValue with raw and semantic views.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Byte-oriented FieldValue with raw and semantic views contract is complete, its named evidence is reproducible, v0.12.0 (Case-insensitive validated FieldName)
still passes, no capability assigned to v0.14.0 (Ordered FieldLine and FieldSection storage) is claimed, and no critical or
high finding remains open.

`0.13.0 implementation stop reached. Run pentest for this exact commit.`

### v0.14.0 — Ordered FieldLine and FieldSection storage

Status: planned

#### Goal

Deliver **Ordered FieldLine and FieldSection storage** as the only primary capability in this stop. It builds
on v0.13.0 (Byte-oriented FieldValue with raw and semantic views) and must be independently trustworthy before v0.15.0 (Request-target, URI, and authority types) begins.

#### Deliverables

- Implement and document Ordered FieldLine and FieldSection storage in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Ordered FieldLine and FieldSection storage.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Ordered FieldLine and FieldSection storage contract is complete, its named evidence is reproducible, v0.13.0 (Byte-oriented FieldValue with raw and semantic views)
still passes, no capability assigned to v0.15.0 (Request-target, URI, and authority types) is claimed, and no critical or
high finding remains open.

`0.14.0 implementation stop reached. Run pentest for this exact commit.`

### v0.15.0 — Request-target, URI, and authority types

Status: planned

#### Goal

Deliver **Request-target, URI, and authority types** as the only primary capability in this stop. It builds
on v0.14.0 (Ordered FieldLine and FieldSection storage) and must be independently trustworthy before v0.16.0 (Request and response control-data types) begins.

#### Deliverables

- Implement and document Request-target, URI, and authority types in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Request-target, URI, and authority types.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Request-target, URI, and authority types contract is complete, its named evidence is reproducible, v0.14.0 (Ordered FieldLine and FieldSection storage)
still passes, no capability assigned to v0.16.0 (Request and response control-data types) is claimed, and no critical or
high finding remains open.

`0.15.0 implementation stop reached. Run pentest for this exact commit.`

### v0.16.0 — Request and response control-data types

Status: planned

#### Goal

Deliver **Request and response control-data types** as the only primary capability in this stop. It builds
on v0.15.0 (Request-target, URI, and authority types) and must be independently trustworthy before v0.17.0 (Role, profile, and policy types) begins.

#### Deliverables

- Implement and document Request and response control-data types in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Request and response control-data types.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Request and response control-data types contract is complete, its named evidence is reproducible, v0.15.0 (Request-target, URI, and authority types)
still passes, no capability assigned to v0.17.0 (Role, profile, and policy types) is claimed, and no critical or
high finding remains open.

`0.16.0 implementation stop reached. Run pentest for this exact commit.`

### v0.17.0 — Role, profile, and policy types

Status: planned

#### Goal

Deliver **Role, profile, and policy types** as the only primary capability in this stop. It builds
on v0.16.0 (Request and response control-data types) and must be independently trustworthy before v0.18.0 (Minimal synchronous I/O contracts) begins.

#### Deliverables

- Implement and document Role, profile, and policy types in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Role, profile, and policy types.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Role, profile, and policy types contract is complete, its named evidence is reproducible, v0.16.0 (Request and response control-data types)
still passes, no capability assigned to v0.18.0 (Minimal synchronous I/O contracts) is claimed, and no critical or
high finding remains open.

`0.17.0 implementation stop reached. Run pentest for this exact commit.`

### v0.18.0 — Minimal synchronous I/O contracts

Status: planned

#### Goal

Deliver **Minimal synchronous I/O contracts** as the only primary capability in this stop. It builds
on v0.17.0 (Role, profile, and policy types) and must be independently trustworthy before v0.19.0 (Runtime-neutral readiness and poll contracts) begins.

#### Deliverables

- Implement and document Minimal synchronous I/O contracts in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Minimal synchronous I/O contracts.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Minimal synchronous I/O contracts contract is complete, its named evidence is reproducible, v0.17.0 (Role, profile, and policy types)
still passes, no capability assigned to v0.19.0 (Runtime-neutral readiness and poll contracts) is claimed, and no critical or
high finding remains open.

`0.18.0 implementation stop reached. Run pentest for this exact commit.`

### v0.19.0 — Runtime-neutral readiness and poll contracts

Status: planned

#### Goal

Deliver **Runtime-neutral readiness and poll contracts** as the only primary capability in this stop. It builds
on v0.18.0 (Minimal synchronous I/O contracts) and must be independently trustworthy before v0.20.0 (Injected monotonic clock and deadline contracts) begins.

#### Deliverables

- Implement and document Runtime-neutral readiness and poll contracts in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Runtime-neutral readiness and poll contracts.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Runtime-neutral readiness and poll contracts contract is complete, its named evidence is reproducible, v0.18.0 (Minimal synchronous I/O contracts)
still passes, no capability assigned to v0.20.0 (Injected monotonic clock and deadline contracts) is claimed, and no critical or
high finding remains open.

`0.19.0 implementation stop reached. Run pentest for this exact commit.`

### v0.20.0 — Injected monotonic clock and deadline contracts

Status: planned

#### Goal

Deliver **Injected monotonic clock and deadline contracts** as the only primary capability in this stop. It builds
on v0.19.0 (Runtime-neutral readiness and poll contracts) and must be independently trustworthy before v0.21.0 (Cancellation, close, and bounded-backpressure contracts) begins.

#### Deliverables

- Implement and document Injected monotonic clock and deadline contracts in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Injected monotonic clock and deadline contracts.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Injected monotonic clock and deadline contracts contract is complete, its named evidence is reproducible, v0.19.0 (Runtime-neutral readiness and poll contracts)
still passes, no capability assigned to v0.21.0 (Cancellation, close, and bounded-backpressure contracts) is claimed, and no critical or
high finding remains open.

`0.20.0 implementation stop reached. Run pentest for this exact commit.`

### v0.21.0 — Cancellation, close, and bounded-backpressure contracts

Status: planned

#### Goal

Deliver **Cancellation, close, and bounded-backpressure contracts** as the only primary capability in this stop. It builds
on v0.20.0 (Injected monotonic clock and deadline contracts) and must be independently trustworthy before v0.22.0 (Deterministic fake transport and driver harness) begins.

#### Deliverables

- Implement and document Cancellation, close, and bounded-backpressure contracts in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Cancellation, close, and bounded-backpressure contracts.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Cancellation, close, and bounded-backpressure contracts contract is complete, its named evidence is reproducible, v0.20.0 (Injected monotonic clock and deadline contracts)
still passes, no capability assigned to v0.22.0 (Deterministic fake transport and driver harness) is claimed, and no critical or
high finding remains open.

`0.21.0 implementation stop reached. Run pentest for this exact commit.`

### v0.22.0 — Deterministic fake transport and driver harness

Status: planned

#### Goal

Deliver **Deterministic fake transport and driver harness** as the only primary capability in this stop. It builds
on v0.21.0 (Cancellation, close, and bounded-backpressure contracts) and must be independently trustworthy before v0.23.0 (Requirement, applicability, and errata evidence system) begins.

#### Deliverables

- Implement and document Deterministic fake transport and driver harness in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Deterministic fake transport and driver harness.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Deterministic fake transport and driver harness contract is complete, its named evidence is reproducible, v0.21.0 (Cancellation, close, and bounded-backpressure contracts)
still passes, no capability assigned to v0.23.0 (Requirement, applicability, and errata evidence system) is claimed, and no critical or
high finding remains open.

`0.22.0 implementation stop reached. Run pentest for this exact commit.`

### v0.23.0 — Requirement, applicability, and errata evidence system

Status: planned

#### Goal

Deliver **Requirement, applicability, and errata evidence system** as the only primary capability in this stop. It builds
on v0.22.0 (Deterministic fake transport and driver harness) and must be independently trustworthy before v0.24.0 (Foundation Kani campaign, audit, and pentest) begins.

#### Deliverables

- Implement and document Requirement, applicability, and errata evidence system in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Requirement, applicability, and errata evidence system.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Requirement, applicability, and errata evidence system contract is complete, its named evidence is reproducible, v0.22.0 (Deterministic fake transport and driver harness)
still passes, no capability assigned to v0.24.0 (Foundation Kani campaign, audit, and pentest) is claimed, and no critical or
high finding remains open.

`0.23.0 implementation stop reached. Run pentest for this exact commit.`

### v0.24.0 — Foundation Kani campaign, audit, and pentest

Status: planned

#### Goal

Deliver **Foundation Kani campaign, audit, and pentest** as the only primary capability in this stop. It builds
on v0.23.0 (Requirement, applicability, and errata evidence system) and must be independently trustworthy before v0.25.0 (HTTP/1 role and parser profiles) begins.

#### Deliverables

- Implement and document Foundation Kani campaign, audit, and pentest in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: No parser may publish protocol state until checked progress, storage, limits, roles, and evidence contracts exist.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Foundation Kani campaign, audit, and pentest.
- Exercise checked arithmetic, every capacity boundary, zero-progress rejection, reserve/commit/refund accounting, borrowed-lifetime rules, cancellation, and deterministic fake-transport behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Foundation Kani campaign, audit, and pentest contract is complete, its named evidence is reproducible, v0.23.0 (Requirement, applicability, and errata evidence system)
still passes, no capability assigned to v0.25.0 (HTTP/1 role and parser profiles) is claimed, and no critical or
high finding remains open.

`0.24.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 2 — HTTP/1 and isolated HTTP/0.9

Phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.

### v0.25.0 — HTTP/1 role and parser profiles

Status: planned

#### Goal

Deliver **HTTP/1 role and parser profiles** as the only primary capability in this stop. It builds
on v0.24.0 (Foundation Kani campaign, audit, and pentest) and must be independently trustworthy before v0.26.0 (Incremental HTTP/1 request-line parser) begins.

#### Deliverables

- Implement and document HTTP/1 role and parser profiles in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/1 role and parser profiles.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/1 role and parser profiles contract is complete, its named evidence is reproducible, v0.24.0 (Foundation Kani campaign, audit, and pentest)
still passes, no capability assigned to v0.26.0 (Incremental HTTP/1 request-line parser) is claimed, and no critical or
high finding remains open.

`0.25.0 implementation stop reached. Run pentest for this exact commit.`

### v0.26.0 — Incremental HTTP/1 request-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 request-line parser** as the only primary capability in this stop. It builds
on v0.25.0 (HTTP/1 role and parser profiles) and must be independently trustworthy before v0.27.0 (Incremental HTTP/1 status-line parser) begins.

#### Deliverables

- Implement and document Incremental HTTP/1 request-line parser in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Incremental HTTP/1 request-line parser.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Incremental HTTP/1 request-line parser contract is complete, its named evidence is reproducible, v0.25.0 (HTTP/1 role and parser profiles)
still passes, no capability assigned to v0.27.0 (Incremental HTTP/1 status-line parser) is claimed, and no critical or
high finding remains open.

`0.26.0 implementation stop reached. Run pentest for this exact commit.`

### v0.27.0 — Incremental HTTP/1 status-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 status-line parser** as the only primary capability in this stop. It builds
on v0.26.0 (Incremental HTTP/1 request-line parser) and must be independently trustworthy before v0.28.0 (Every-byte fragmentation support) begins.

#### Deliverables

- Implement and document Incremental HTTP/1 status-line parser in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Incremental HTTP/1 status-line parser.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Incremental HTTP/1 status-line parser contract is complete, its named evidence is reproducible, v0.26.0 (Incremental HTTP/1 request-line parser)
still passes, no capability assigned to v0.28.0 (Every-byte fragmentation support) is claimed, and no critical or
high finding remains open.

`0.27.0 implementation stop reached. Run pentest for this exact commit.`

### v0.28.0 — Every-byte fragmentation support

Status: planned

#### Goal

Deliver **Every-byte fragmentation support** as the only primary capability in this stop. It builds
on v0.27.0 (Incremental HTTP/1 status-line parser) and must be independently trustworthy before v0.29.0 (Strict CRLF and separately named LF compatibility) begins.

#### Deliverables

- Implement and document Every-byte fragmentation support in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Every-byte fragmentation support.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Every-byte fragmentation support contract is complete, its named evidence is reproducible, v0.27.0 (Incremental HTTP/1 status-line parser)
still passes, no capability assigned to v0.29.0 (Strict CRLF and separately named LF compatibility) is claimed, and no critical or
high finding remains open.

`0.28.0 implementation stop reached. Run pentest for this exact commit.`

### v0.29.0 — Strict CRLF and separately named LF compatibility

Status: planned

#### Goal

Deliver **Strict CRLF and separately named LF compatibility** as the only primary capability in this stop. It builds
on v0.28.0 (Every-byte fragmentation support) and must be independently trustworthy before v0.30.0 (Incremental HTTP/1 field-line parser) begins.

#### Deliverables

- Implement and document Strict CRLF and separately named LF compatibility in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Strict CRLF and separately named LF compatibility.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Strict CRLF and separately named LF compatibility contract is complete, its named evidence is reproducible, v0.28.0 (Every-byte fragmentation support)
still passes, no capability assigned to v0.30.0 (Incremental HTTP/1 field-line parser) is claimed, and no critical or
high finding remains open.

`0.29.0 implementation stop reached. Run pentest for this exact commit.`

### v0.30.0 — Incremental HTTP/1 field-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 field-line parser** as the only primary capability in this stop. It builds
on v0.29.0 (Strict CRLF and separately named LF compatibility) and must be independently trustworthy before v0.31.0 (Explicit OWS handling with raw-value preservation) begins.

#### Deliverables

- Implement and document Incremental HTTP/1 field-line parser in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Incremental HTTP/1 field-line parser.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Incremental HTTP/1 field-line parser contract is complete, its named evidence is reproducible, v0.29.0 (Strict CRLF and separately named LF compatibility)
still passes, no capability assigned to v0.31.0 (Explicit OWS handling with raw-value preservation) is claimed, and no critical or
high finding remains open.

`0.30.0 implementation stop reached. Run pentest for this exact commit.`

### v0.31.0 — Explicit OWS handling with raw-value preservation

Status: planned

#### Goal

Deliver **Explicit OWS handling with raw-value preservation** as the only primary capability in this stop. It builds
on v0.30.0 (Incremental HTTP/1 field-line parser) and must be independently trustworthy before v0.32.0 (Injection-proof HTTP/1 serialization) begins.

#### Deliverables

- Implement and document Explicit OWS handling with raw-value preservation in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Explicit OWS handling with raw-value preservation.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Explicit OWS handling with raw-value preservation contract is complete, its named evidence is reproducible, v0.30.0 (Incremental HTTP/1 field-line parser)
still passes, no capability assigned to v0.32.0 (Injection-proof HTTP/1 serialization) is claimed, and no critical or
high finding remains open.

`0.31.0 implementation stop reached. Run pentest for this exact commit.`

### v0.32.0 — Injection-proof HTTP/1 serialization

Status: planned

#### Goal

Deliver **Injection-proof HTTP/1 serialization** as the only primary capability in this stop. It builds
on v0.31.0 (Explicit OWS handling with raw-value preservation) and must be independently trustworthy before v0.33.0 (obs-fold, bad colon whitespace, and control-byte rejection) begins.

#### Deliverables

- Implement and document Injection-proof HTTP/1 serialization in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Injection-proof HTTP/1 serialization.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Injection-proof HTTP/1 serialization contract is complete, its named evidence is reproducible, v0.31.0 (Explicit OWS handling with raw-value preservation)
still passes, no capability assigned to v0.33.0 (obs-fold, bad colon whitespace, and control-byte rejection) is claimed, and no critical or
high finding remains open.

`0.32.0 implementation stop reached. Run pentest for this exact commit.`

### v0.33.0 — obs-fold, bad colon whitespace, and control-byte rejection

Status: planned

#### Goal

Deliver **obs-fold, bad colon whitespace, and control-byte rejection** as the only primary capability in this stop. It builds
on v0.32.0 (Injection-proof HTTP/1 serialization) and must be independently trustworthy before v0.34.0 (Field count, line, and section caps) begins.

#### Deliverables

- Implement and document obs-fold, bad colon whitespace, and control-byte rejection in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for obs-fold, bad colon whitespace, and control-byte rejection.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The obs-fold, bad colon whitespace, and control-byte rejection contract is complete, its named evidence is reproducible, v0.32.0 (Injection-proof HTTP/1 serialization)
still passes, no capability assigned to v0.34.0 (Field count, line, and section caps) is claimed, and no critical or
high finding remains open.

`0.33.0 implementation stop reached. Run pentest for this exact commit.`

### v0.34.0 — Field count, line, and section caps

Status: planned

#### Goal

Deliver **Field count, line, and section caps** as the only primary capability in this stop. It builds
on v0.33.0 (obs-fold, bad colon whitespace, and control-byte rejection) and must be independently trustworthy before v0.35.0 (HTTP/1.1 Host validation and duplicate rejection) begins.

#### Deliverables

- Implement and document Field count, line, and section caps in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Field count, line, and section caps.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Field count, line, and section caps contract is complete, its named evidence is reproducible, v0.33.0 (obs-fold, bad colon whitespace, and control-byte rejection)
still passes, no capability assigned to v0.35.0 (HTTP/1.1 Host validation and duplicate rejection) is claimed, and no critical or
high finding remains open.

`0.34.0 implementation stop reached. Run pentest for this exact commit.`

### v0.35.0 — HTTP/1.1 Host validation and duplicate rejection

Status: planned

#### Goal

Deliver **HTTP/1.1 Host validation and duplicate rejection** as the only primary capability in this stop. It builds
on v0.34.0 (Field count, line, and section caps) and must be independently trustworthy before v0.36.0 (Method and request-target-form coherence) begins.

#### Deliverables

- Implement and document HTTP/1.1 Host validation and duplicate rejection in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/1.1 Host validation and duplicate rejection.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/1.1 Host validation and duplicate rejection contract is complete, its named evidence is reproducible, v0.34.0 (Field count, line, and section caps)
still passes, no capability assigned to v0.36.0 (Method and request-target-form coherence) is claimed, and no critical or
high finding remains open.

`0.35.0 implementation stop reached. Run pentest for this exact commit.`

### v0.36.0 — Method and request-target-form coherence

Status: planned

#### Goal

Deliver **Method and request-target-form coherence** as the only primary capability in this stop. It builds
on v0.35.0 (HTTP/1.1 Host validation and duplicate rejection) and must be independently trustworthy before v0.37.0 (Checked Content-Length grammar) begins.

#### Deliverables

- Implement and document Method and request-target-form coherence in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Method and request-target-form coherence.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Method and request-target-form coherence contract is complete, its named evidence is reproducible, v0.35.0 (HTTP/1.1 Host validation and duplicate rejection)
still passes, no capability assigned to v0.37.0 (Checked Content-Length grammar) is claimed, and no critical or
high finding remains open.

`0.36.0 implementation stop reached. Run pentest for this exact commit.`

### v0.37.0 — Checked Content-Length grammar

Status: planned

#### Goal

Deliver **Checked Content-Length grammar** as the only primary capability in this stop. It builds
on v0.36.0 (Method and request-target-form coherence) and must be independently trustworthy before v0.38.0 (Repeated and comma-list Content-Length resolution) begins.

#### Deliverables

- Implement and document Checked Content-Length grammar in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Checked Content-Length grammar.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Checked Content-Length grammar contract is complete, its named evidence is reproducible, v0.36.0 (Method and request-target-form coherence)
still passes, no capability assigned to v0.38.0 (Repeated and comma-list Content-Length resolution) is claimed, and no critical or
high finding remains open.

`0.37.0 implementation stop reached. Run pentest for this exact commit.`

### v0.38.0 — Repeated and comma-list Content-Length resolution

Status: planned

#### Goal

Deliver **Repeated and comma-list Content-Length resolution** as the only primary capability in this stop. It builds
on v0.37.0 (Checked Content-Length grammar) and must be independently trustworthy before v0.39.0 (Transfer-Encoding grammar and ordering) begins.

#### Deliverables

- Implement and document Repeated and comma-list Content-Length resolution in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Repeated and comma-list Content-Length resolution.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Repeated and comma-list Content-Length resolution contract is complete, its named evidence is reproducible, v0.37.0 (Checked Content-Length grammar)
still passes, no capability assigned to v0.39.0 (Transfer-Encoding grammar and ordering) is claimed, and no critical or
high finding remains open.

`0.38.0 implementation stop reached. Run pentest for this exact commit.`

### v0.39.0 — Transfer-Encoding grammar and ordering

Status: planned

#### Goal

Deliver **Transfer-Encoding grammar and ordering** as the only primary capability in this stop. It builds
on v0.38.0 (Repeated and comma-list Content-Length resolution) and must be independently trustworthy before v0.40.0 (TE/CL conflict resolution and mandatory close action) begins.

#### Deliverables

- Implement and document Transfer-Encoding grammar and ordering in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Transfer-Encoding grammar and ordering.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Transfer-Encoding grammar and ordering contract is complete, its named evidence is reproducible, v0.38.0 (Repeated and comma-list Content-Length resolution)
still passes, no capability assigned to v0.40.0 (TE/CL conflict resolution and mandatory close action) is claimed, and no critical or
high finding remains open.

`0.39.0 implementation stop reached. Run pentest for this exact commit.`

### v0.40.0 — TE/CL conflict resolution and mandatory close action

Status: planned

#### Goal

Deliver **TE/CL conflict resolution and mandatory close action** as the only primary capability in this stop. It builds
on v0.39.0 (Transfer-Encoding grammar and ordering) and must be independently trustworthy before v0.41.0 (Central HTTP/1 message-body-length algorithm) begins.

#### Deliverables

- Implement and document TE/CL conflict resolution and mandatory close action in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for TE/CL conflict resolution and mandatory close action.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The TE/CL conflict resolution and mandatory close action contract is complete, its named evidence is reproducible, v0.39.0 (Transfer-Encoding grammar and ordering)
still passes, no capability assigned to v0.41.0 (Central HTTP/1 message-body-length algorithm) is claimed, and no critical or
high finding remains open.

`0.40.0 implementation stop reached. Run pentest for this exact commit.`

### v0.41.0 — Central HTTP/1 message-body-length algorithm

Status: planned

#### Goal

Deliver **Central HTTP/1 message-body-length algorithm** as the only primary capability in this stop. It builds
on v0.40.0 (TE/CL conflict resolution and mandatory close action) and must be independently trustworthy before v0.42.0 (Fixed-length body decoder) begins.

#### Deliverables

- Implement and document Central HTTP/1 message-body-length algorithm in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Central HTTP/1 message-body-length algorithm.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Central HTTP/1 message-body-length algorithm contract is complete, its named evidence is reproducible, v0.40.0 (TE/CL conflict resolution and mandatory close action)
still passes, no capability assigned to v0.42.0 (Fixed-length body decoder) is claimed, and no critical or
high finding remains open.

`0.41.0 implementation stop reached. Run pentest for this exact commit.`

### v0.42.0 — Fixed-length body decoder

Status: planned

#### Goal

Deliver **Fixed-length body decoder** as the only primary capability in this stop. It builds
on v0.41.0 (Central HTTP/1 message-body-length algorithm) and must be independently trustworthy before v0.43.0 (Close-delimited response decoder) begins.

#### Deliverables

- Implement and document Fixed-length body decoder in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Fixed-length body decoder.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Fixed-length body decoder contract is complete, its named evidence is reproducible, v0.41.0 (Central HTTP/1 message-body-length algorithm)
still passes, no capability assigned to v0.43.0 (Close-delimited response decoder) is claimed, and no critical or
high finding remains open.

`0.42.0 implementation stop reached. Run pentest for this exact commit.`

### v0.43.0 — Close-delimited response decoder

Status: planned

#### Goal

Deliver **Close-delimited response decoder** as the only primary capability in this stop. It builds
on v0.42.0 (Fixed-length body decoder) and must be independently trustworthy before v0.44.0 (Checked chunk-size parser) begins.

#### Deliverables

- Implement and document Close-delimited response decoder in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Close-delimited response decoder.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Close-delimited response decoder contract is complete, its named evidence is reproducible, v0.42.0 (Fixed-length body decoder)
still passes, no capability assigned to v0.44.0 (Checked chunk-size parser) is claimed, and no critical or
high finding remains open.

`0.43.0 implementation stop reached. Run pentest for this exact commit.`

### v0.44.0 — Checked chunk-size parser

Status: planned

#### Goal

Deliver **Checked chunk-size parser** as the only primary capability in this stop. It builds
on v0.43.0 (Close-delimited response decoder) and must be independently trustworthy before v0.45.0 (Incremental chunk-data state) begins.

#### Deliverables

- Implement and document Checked chunk-size parser in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Checked chunk-size parser.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Checked chunk-size parser contract is complete, its named evidence is reproducible, v0.43.0 (Close-delimited response decoder)
still passes, no capability assigned to v0.45.0 (Incremental chunk-data state) is claimed, and no critical or
high finding remains open.

`0.44.0 implementation stop reached. Run pentest for this exact commit.`

### v0.45.0 — Incremental chunk-data state

Status: planned

#### Goal

Deliver **Incremental chunk-data state** as the only primary capability in this stop. It builds
on v0.44.0 (Checked chunk-size parser) and must be independently trustworthy before v0.46.0 (Bounded chunk-extension parser) begins.

#### Deliverables

- Implement and document Incremental chunk-data state in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Incremental chunk-data state.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Incremental chunk-data state contract is complete, its named evidence is reproducible, v0.44.0 (Checked chunk-size parser)
still passes, no capability assigned to v0.46.0 (Bounded chunk-extension parser) is claimed, and no critical or
high finding remains open.

`0.45.0 implementation stop reached. Run pentest for this exact commit.`

### v0.46.0 — Bounded chunk-extension parser

Status: planned

#### Goal

Deliver **Bounded chunk-extension parser** as the only primary capability in this stop. It builds
on v0.45.0 (Incremental chunk-data state) and must be independently trustworthy before v0.47.0 (Last-chunk and trailer transition) begins.

#### Deliverables

- Implement and document Bounded chunk-extension parser in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Bounded chunk-extension parser.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Bounded chunk-extension parser contract is complete, its named evidence is reproducible, v0.45.0 (Incremental chunk-data state)
still passes, no capability assigned to v0.47.0 (Last-chunk and trailer transition) is claimed, and no critical or
high finding remains open.

`0.46.0 implementation stop reached. Run pentest for this exact commit.`

### v0.47.0 — Last-chunk and trailer transition

Status: planned

#### Goal

Deliver **Last-chunk and trailer transition** as the only primary capability in this stop. It builds
on v0.46.0 (Bounded chunk-extension parser) and must be independently trustworthy before v0.48.0 (Trailer declarations and prohibited-trailer policy) begins.

#### Deliverables

- Implement and document Last-chunk and trailer transition in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Last-chunk and trailer transition.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Last-chunk and trailer transition contract is complete, its named evidence is reproducible, v0.46.0 (Bounded chunk-extension parser)
still passes, no capability assigned to v0.48.0 (Trailer declarations and prohibited-trailer policy) is claimed, and no critical or
high finding remains open.

`0.47.0 implementation stop reached. Run pentest for this exact commit.`

### v0.48.0 — Trailer declarations and prohibited-trailer policy

Status: planned

#### Goal

Deliver **Trailer declarations and prohibited-trailer policy** as the only primary capability in this stop. It builds
on v0.47.0 (Last-chunk and trailer transition) and must be independently trustworthy before v0.49.0 (Chunked encoder with partial-output state) begins.

#### Deliverables

- Implement and document Trailer declarations and prohibited-trailer policy in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Trailer declarations and prohibited-trailer policy.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Trailer declarations and prohibited-trailer policy contract is complete, its named evidence is reproducible, v0.47.0 (Last-chunk and trailer transition)
still passes, no capability assigned to v0.49.0 (Chunked encoder with partial-output state) is claimed, and no critical or
high finding remains open.

`0.48.0 implementation stop reached. Run pentest for this exact commit.`

### v0.49.0 — Chunked encoder with partial-output state

Status: planned

#### Goal

Deliver **Chunked encoder with partial-output state** as the only primary capability in this stop. It builds
on v0.48.0 (Trailer declarations and prohibited-trailer policy) and must be independently trustworthy before v0.50.0 (HTTP/1.1 persistence and Connection semantics) begins.

#### Deliverables

- Implement and document Chunked encoder with partial-output state in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Chunked encoder with partial-output state.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Chunked encoder with partial-output state contract is complete, its named evidence is reproducible, v0.48.0 (Trailer declarations and prohibited-trailer policy)
still passes, no capability assigned to v0.50.0 (HTTP/1.1 persistence and Connection semantics) is claimed, and no critical or
high finding remains open.

`0.49.0 implementation stop reached. Run pentest for this exact commit.`

### v0.50.0 — HTTP/1.1 persistence and Connection semantics

Status: planned

#### Goal

Deliver **HTTP/1.1 persistence and Connection semantics** as the only primary capability in this stop. It builds
on v0.49.0 (Chunked encoder with partial-output state) and must be independently trustworthy before v0.51.0 (Sequential request/response connection state) begins.

#### Deliverables

- Implement and document HTTP/1.1 persistence and Connection semantics in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/1.1 persistence and Connection semantics.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/1.1 persistence and Connection semantics contract is complete, its named evidence is reproducible, v0.49.0 (Chunked encoder with partial-output state)
still passes, no capability assigned to v0.51.0 (Sequential request/response connection state) is claimed, and no critical or
high finding remains open.

`0.50.0 implementation stop reached. Run pentest for this exact commit.`

### v0.51.0 — Sequential request/response connection state

Status: planned

#### Goal

Deliver **Sequential request/response connection state** as the only primary capability in this stop. It builds
on v0.50.0 (HTTP/1.1 persistence and Connection semantics) and must be independently trustworthy before v0.52.0 (Optional bounded pipelining queue) begins.

#### Deliverables

- Implement and document Sequential request/response connection state in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Sequential request/response connection state.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Sequential request/response connection state contract is complete, its named evidence is reproducible, v0.50.0 (HTTP/1.1 persistence and Connection semantics)
still passes, no capability assigned to v0.52.0 (Optional bounded pipelining queue) is claimed, and no critical or
high finding remains open.

`0.51.0 implementation stop reached. Run pentest for this exact commit.`

### v0.52.0 — Optional bounded pipelining queue

Status: planned

#### Goal

Deliver **Optional bounded pipelining queue** as the only primary capability in this stop. It builds
on v0.51.0 (Sequential request/response connection state) and must be independently trustworthy before v0.53.0 (Informational response lifecycle) begins.

#### Deliverables

- Implement and document Optional bounded pipelining queue in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Optional bounded pipelining queue.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Optional bounded pipelining queue contract is complete, its named evidence is reproducible, v0.51.0 (Sequential request/response connection state)
still passes, no capability assigned to v0.53.0 (Informational response lifecycle) is claimed, and no critical or
high finding remains open.

`0.52.0 implementation stop reached. Run pentest for this exact commit.`

### v0.53.0 — Informational response lifecycle

Status: planned

#### Goal

Deliver **Informational response lifecycle** as the only primary capability in this stop. It builds
on v0.52.0 (Optional bounded pipelining queue) and must be independently trustworthy before v0.54.0 (Expect: 100-continue state) begins.

#### Deliverables

- Implement and document Informational response lifecycle in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Informational response lifecycle.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Informational response lifecycle contract is complete, its named evidence is reproducible, v0.52.0 (Optional bounded pipelining queue)
still passes, no capability assigned to v0.54.0 (Expect: 100-continue state) is claimed, and no critical or
high finding remains open.

`0.53.0 implementation stop reached. Run pentest for this exact commit.`

### v0.54.0 — Expect: 100-continue state

Status: planned

#### Goal

Deliver **Expect: 100-continue state** as the only primary capability in this stop. It builds
on v0.53.0 (Informational response lifecycle) and must be independently trustworthy before v0.55.0 (EOF, truncation, and incomplete-message rules) begins.

#### Deliverables

- Implement and document Expect: 100-continue state in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Expect: 100-continue state.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Expect: 100-continue state contract is complete, its named evidence is reproducible, v0.53.0 (Informational response lifecycle)
still passes, no capability assigned to v0.55.0 (EOF, truncation, and incomplete-message rules) is claimed, and no critical or
high finding remains open.

`0.54.0 implementation stop reached. Run pentest for this exact commit.`

### v0.55.0 — EOF, truncation, and incomplete-message rules

Status: planned

#### Goal

Deliver **EOF, truncation, and incomplete-message rules** as the only primary capability in this stop. It builds
on v0.54.0 (Expect: 100-continue state) and must be independently trustworthy before v0.56.0 (HEAD response-framing context) begins.

#### Deliverables

- Implement and document EOF, truncation, and incomplete-message rules in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for EOF, truncation, and incomplete-message rules.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The EOF, truncation, and incomplete-message rules contract is complete, its named evidence is reproducible, v0.54.0 (Expect: 100-continue state)
still passes, no capability assigned to v0.56.0 (HEAD response-framing context) is claimed, and no critical or
high finding remains open.

`0.55.0 implementation stop reached. Run pentest for this exact commit.`

### v0.56.0 — HEAD response-framing context

Status: planned

#### Goal

Deliver **HEAD response-framing context** as the only primary capability in this stop. It builds
on v0.55.0 (EOF, truncation, and incomplete-message rules) and must be independently trustworthy before v0.57.0 (1xx, 204, 304, and body-forbidden response handling) begins.

#### Deliverables

- Implement and document HEAD response-framing context in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HEAD response-framing context.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HEAD response-framing context contract is complete, its named evidence is reproducible, v0.55.0 (EOF, truncation, and incomplete-message rules)
still passes, no capability assigned to v0.57.0 (1xx, 204, 304, and body-forbidden response handling) is claimed, and no critical or
high finding remains open.

`0.56.0 implementation stop reached. Run pentest for this exact commit.`

### v0.57.0 — 1xx, 204, 304, and body-forbidden response handling

Status: planned

#### Goal

Deliver **1xx, 204, 304, and body-forbidden response handling** as the only primary capability in this stop. It builds
on v0.56.0 (HEAD response-framing context) and must be independently trustworthy before v0.58.0 (CONNECT request and successful tunnel transition) begins.

#### Deliverables

- Implement and document 1xx, 204, 304, and body-forbidden response handling in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for 1xx, 204, 304, and body-forbidden response handling.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The 1xx, 204, 304, and body-forbidden response handling contract is complete, its named evidence is reproducible, v0.56.0 (HEAD response-framing context)
still passes, no capability assigned to v0.58.0 (CONNECT request and successful tunnel transition) is claimed, and no critical or
high finding remains open.

`0.57.0 implementation stop reached. Run pentest for this exact commit.`

### v0.58.0 — CONNECT request and successful tunnel transition

Status: planned

#### Goal

Deliver **CONNECT request and successful tunnel transition** as the only primary capability in this stop. It builds
on v0.57.0 (1xx, 204, 304, and body-forbidden response handling) and must be independently trustworthy before v0.59.0 (RFC 9931 optimistic-data protections) begins.

#### Deliverables

- Implement and document CONNECT request and successful tunnel transition in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for CONNECT request and successful tunnel transition.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The CONNECT request and successful tunnel transition contract is complete, its named evidence is reproducible, v0.57.0 (1xx, 204, 304, and body-forbidden response handling)
still passes, no capability assigned to v0.59.0 (RFC 9931 optimistic-data protections) is claimed, and no critical or
high finding remains open.

`0.58.0 implementation stop reached. Run pentest for this exact commit.`

### v0.59.0 — RFC 9931 optimistic-data protections

Status: planned

#### Goal

Deliver **RFC 9931 optimistic-data protections** as the only primary capability in this stop. It builds
on v0.58.0 (CONNECT request and successful tunnel transition) and must be independently trustworthy before v0.60.0 (101 Switching Protocols transition) begins.

#### Deliverables

- Implement and document RFC 9931 optimistic-data protections in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for RFC 9931 optimistic-data protections.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The RFC 9931 optimistic-data protections contract is complete, its named evidence is reproducible, v0.58.0 (CONNECT request and successful tunnel transition)
still passes, no capability assigned to v0.60.0 (101 Switching Protocols transition) is claimed, and no critical or
high finding remains open.

`0.59.0 implementation stop reached. Run pentest for this exact commit.`

### v0.60.0 — 101 Switching Protocols transition

Status: planned

#### Goal

Deliver **101 Switching Protocols transition** as the only primary capability in this stop. It builds
on v0.59.0 (RFC 9931 optimistic-data protections) and must be independently trustworthy before v0.61.0 (RFC 6455 WebSocket opening handshake only) begins.

#### Deliverables

- Implement and document 101 Switching Protocols transition in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for 101 Switching Protocols transition.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The 101 Switching Protocols transition contract is complete, its named evidence is reproducible, v0.59.0 (RFC 9931 optimistic-data protections)
still passes, no capability assigned to v0.61.0 (RFC 6455 WebSocket opening handshake only) is claimed, and no critical or
high finding remains open.

`0.60.0 implementation stop reached. Run pentest for this exact commit.`

### v0.61.0 — RFC 6455 WebSocket opening handshake only

Status: planned

#### Goal

Deliver **RFC 6455 WebSocket opening handshake only** as the only primary capability in this stop. It builds
on v0.60.0 (101 Switching Protocols transition) and must be independently trustworthy before v0.62.0 (Connection-nominated and hop-by-hop field handling) begins.

#### Deliverables

- Implement and document RFC 6455 WebSocket opening handshake only in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for RFC 6455 WebSocket opening handshake only.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The RFC 6455 WebSocket opening handshake only contract is complete, its named evidence is reproducible, v0.60.0 (101 Switching Protocols transition)
still passes, no capability assigned to v0.62.0 (Connection-nominated and hop-by-hop field handling) is claimed, and no critical or
high finding remains open.

`0.61.0 implementation stop reached. Run pentest for this exact commit.`

### v0.62.0 — Connection-nominated and hop-by-hop field handling

Status: planned

#### Goal

Deliver **Connection-nominated and hop-by-hop field handling** as the only primary capability in this stop. It builds
on v0.61.0 (RFC 6455 WebSocket opening handshake only) and must be independently trustworthy before v0.63.0 (Safe forwarding and explicit reframing plan) begins.

#### Deliverables

- Implement and document Connection-nominated and hop-by-hop field handling in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Connection-nominated and hop-by-hop field handling.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Connection-nominated and hop-by-hop field handling contract is complete, its named evidence is reproducible, v0.61.0 (RFC 6455 WebSocket opening handshake only)
still passes, no capability assigned to v0.63.0 (Safe forwarding and explicit reframing plan) is claimed, and no critical or
high finding remains open.

`0.62.0 implementation stop reached. Run pentest for this exact commit.`

### v0.63.0 — Safe forwarding and explicit reframing plan

Status: planned

#### Goal

Deliver **Safe forwarding and explicit reframing plan** as the only primary capability in this stop. It builds
on v0.62.0 (Connection-nominated and hop-by-hop field handling) and must be independently trustworthy before v0.64.0 (RFC 1945 HTTP/1.0 parser and hardened profile) begins.

#### Deliverables

- Implement and document Safe forwarding and explicit reframing plan in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Safe forwarding and explicit reframing plan.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Safe forwarding and explicit reframing plan contract is complete, its named evidence is reproducible, v0.62.0 (Connection-nominated and hop-by-hop field handling)
still passes, no capability assigned to v0.64.0 (RFC 1945 HTTP/1.0 parser and hardened profile) is claimed, and no critical or
high finding remains open.

`0.63.0 implementation stop reached. Run pentest for this exact commit.`

### v0.64.0 — RFC 1945 HTTP/1.0 parser and hardened profile

Status: planned

#### Goal

Deliver **RFC 1945 HTTP/1.0 parser and hardened profile** as the only primary capability in this stop. It builds
on v0.63.0 (Safe forwarding and explicit reframing plan) and must be independently trustworthy before v0.65.0 (HTTP/1.0 default-close lifecycle) begins.

#### Deliverables

- Implement and document RFC 1945 HTTP/1.0 parser and hardened profile in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for RFC 1945 HTTP/1.0 parser and hardened profile.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The RFC 1945 HTTP/1.0 parser and hardened profile contract is complete, its named evidence is reproducible, v0.63.0 (Safe forwarding and explicit reframing plan)
still passes, no capability assigned to v0.65.0 (HTTP/1.0 default-close lifecycle) is claimed, and no critical or
high finding remains open.

`0.64.0 implementation stop reached. Run pentest for this exact commit.`

### v0.65.0 — HTTP/1.0 default-close lifecycle

Status: planned

#### Goal

Deliver **HTTP/1.0 default-close lifecycle** as the only primary capability in this stop. It builds
on v0.64.0 (RFC 1945 HTTP/1.0 parser and hardened profile) and must be independently trustworthy before v0.66.0 (Explicit HTTP/1.0 keep-alive extension profile) begins.

#### Deliverables

- Implement and document HTTP/1.0 default-close lifecycle in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/1.0 default-close lifecycle.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/1.0 default-close lifecycle contract is complete, its named evidence is reproducible, v0.64.0 (RFC 1945 HTTP/1.0 parser and hardened profile)
still passes, no capability assigned to v0.66.0 (Explicit HTTP/1.0 keep-alive extension profile) is claimed, and no critical or
high finding remains open.

`0.65.0 implementation stop reached. Run pentest for this exact commit.`

### v0.66.0 — Explicit HTTP/1.0 keep-alive extension profile

Status: planned

#### Goal

Deliver **Explicit HTTP/1.0 keep-alive extension profile** as the only primary capability in this stop. It builds
on v0.65.0 (HTTP/1.0 default-close lifecycle) and must be independently trustworthy before v0.67.0 (Separate vef-http09 package and exact grammar) begins.

#### Deliverables

- Implement and document Explicit HTTP/1.0 keep-alive extension profile in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Explicit HTTP/1.0 keep-alive extension profile.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Explicit HTTP/1.0 keep-alive extension profile contract is complete, its named evidence is reproducible, v0.65.0 (HTTP/1.0 default-close lifecycle)
still passes, no capability assigned to v0.67.0 (Separate vef-http09 package and exact grammar) is claimed, and no critical or
high finding remains open.

`0.66.0 implementation stop reached. Run pentest for this exact commit.`

### v0.67.0 — Separate vef-http09 package and exact grammar

Status: planned

#### Goal

Deliver **Separate vef-http09 package and exact grammar** as the only primary capability in this stop. It builds
on v0.66.0 (Explicit HTTP/1.0 keep-alive extension profile) and must be independently trustworthy before v0.68.0 (Explicit HTTP/0.9 client API) begins.

#### Deliverables

- Implement and document Separate vef-http09 package and exact grammar in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Separate vef-http09 package and exact grammar.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Separate vef-http09 package and exact grammar contract is complete, its named evidence is reproducible, v0.66.0 (Explicit HTTP/1.0 keep-alive extension profile)
still passes, no capability assigned to v0.68.0 (Explicit HTTP/0.9 client API) is claimed, and no critical or
high finding remains open.

`0.67.0 implementation stop reached. Run pentest for this exact commit.`

### v0.68.0 — Explicit HTTP/0.9 client API

Status: planned

#### Goal

Deliver **Explicit HTTP/0.9 client API** as the only primary capability in this stop. It builds
on v0.67.0 (Separate vef-http09 package and exact grammar) and must be independently trustworthy before v0.69.0 (Explicit HTTP/0.9 server and dedicated-listener API) begins.

#### Deliverables

- Implement and document Explicit HTTP/0.9 client API in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Explicit HTTP/0.9 client API.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Explicit HTTP/0.9 client API contract is complete, its named evidence is reproducible, v0.67.0 (Separate vef-http09 package and exact grammar)
still passes, no capability assigned to v0.69.0 (Explicit HTTP/0.9 server and dedicated-listener API) is claimed, and no critical or
high finding remains open.

`0.68.0 implementation stop reached. Run pentest for this exact commit.`

### v0.69.0 — Explicit HTTP/0.9 server and dedicated-listener API

Status: planned

#### Goal

Deliver **Explicit HTTP/0.9 server and dedicated-listener API** as the only primary capability in this stop. It builds
on v0.68.0 (Explicit HTTP/0.9 client API) and must be independently trustworthy before v0.70.0 (HTTP/0.9 cross-protocol rejection corpus) begins.

#### Deliverables

- Implement and document Explicit HTTP/0.9 server and dedicated-listener API in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Explicit HTTP/0.9 server and dedicated-listener API.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Explicit HTTP/0.9 server and dedicated-listener API contract is complete, its named evidence is reproducible, v0.68.0 (Explicit HTTP/0.9 client API)
still passes, no capability assigned to v0.70.0 (HTTP/0.9 cross-protocol rejection corpus) is claimed, and no critical or
high finding remains open.

`0.69.0 implementation stop reached. Run pentest for this exact commit.`

### v0.70.0 — HTTP/0.9 cross-protocol rejection corpus

Status: planned

#### Goal

Deliver **HTTP/0.9 cross-protocol rejection corpus** as the only primary capability in this stop. It builds
on v0.69.0 (Explicit HTTP/0.9 server and dedicated-listener API) and must be independently trustworthy before v0.71.0 (HTTP/1 smuggling and ambiguity corpus) begins.

#### Deliverables

- Implement and document HTTP/0.9 cross-protocol rejection corpus in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/0.9 cross-protocol rejection corpus.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/0.9 cross-protocol rejection corpus contract is complete, its named evidence is reproducible, v0.69.0 (Explicit HTTP/0.9 server and dedicated-listener API)
still passes, no capability assigned to v0.71.0 (HTTP/1 smuggling and ambiguity corpus) is claimed, and no critical or
high finding remains open.

`0.70.0 implementation stop reached. Run pentest for this exact commit.`

### v0.71.0 — HTTP/1 smuggling and ambiguity corpus

Status: planned

#### Goal

Deliver **HTTP/1 smuggling and ambiguity corpus** as the only primary capability in this stop. It builds
on v0.70.0 (HTTP/0.9 cross-protocol rejection corpus) and must be independently trustworthy before v0.72.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) begins.

#### Deliverables

- Implement and document HTTP/1 smuggling and ambiguity corpus in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/1 smuggling and ambiguity corpus.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/1 smuggling and ambiguity corpus contract is complete, its named evidence is reproducible, v0.70.0 (HTTP/0.9 cross-protocol rejection corpus)
still passes, no capability assigned to v0.72.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) is claimed, and no critical or
high finding remains open.

`0.71.0 implementation stop reached. Run pentest for this exact commit.`

### v0.72.0 — HTTP/1 and HTTP/0.9 conformance audit and pentest

Status: planned

#### Goal

Deliver **HTTP/1 and HTTP/0.9 conformance audit and pentest** as the only primary capability in this stop. It builds
on v0.71.0 (HTTP/1 smuggling and ambiguity corpus) and must be independently trustworthy before v0.73.0 (HPACK prefix-integer decoder) begins.

#### Deliverables

- Implement and document HTTP/1 and HTTP/0.9 conformance audit and pentest in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HTTP/1 has one octet-level framing interpretation; HTTP/0.9 is a separate package and can never be selected by fallback.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, RFC 9298 applicability, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/1 and HTTP/0.9 conformance audit and pentest.
- Run every-byte split tests, strict-versus-compatibility policy tests, request/response differential cases, smuggling corpora, transition timing tests, bounded pipeline tests, and cross-protocol rejection.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/1 and HTTP/0.9 conformance audit and pentest contract is complete, its named evidence is reproducible, v0.71.0 (HTTP/1 smuggling and ambiguity corpus)
still passes, no capability assigned to v0.73.0 (HPACK prefix-integer decoder) is claimed, and no critical or
high finding remains open.

`0.72.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 3 — HPACK and HTTP/2

Phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.

### v0.73.0 — HPACK prefix-integer decoder

Status: planned

#### Goal

Deliver **HPACK prefix-integer decoder** as the only primary capability in this stop. It builds
on v0.72.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) and must be independently trustworthy before v0.74.0 (HPACK prefix-integer encoder) begins.

#### Deliverables

- Implement and document HPACK prefix-integer decoder in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK prefix-integer decoder.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK prefix-integer decoder contract is complete, its named evidence is reproducible, v0.72.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest)
still passes, no capability assigned to v0.74.0 (HPACK prefix-integer encoder) is claimed, and no critical or
high finding remains open.

`0.73.0 implementation stop reached. Run pentest for this exact commit.`

### v0.74.0 — HPACK prefix-integer encoder

Status: planned

#### Goal

Deliver **HPACK prefix-integer encoder** as the only primary capability in this stop. It builds
on v0.73.0 (HPACK prefix-integer decoder) and must be independently trustworthy before v0.75.0 (HPACK integer overflow and minimality proofs) begins.

#### Deliverables

- Implement and document HPACK prefix-integer encoder in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK prefix-integer encoder.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK prefix-integer encoder contract is complete, its named evidence is reproducible, v0.73.0 (HPACK prefix-integer decoder)
still passes, no capability assigned to v0.75.0 (HPACK integer overflow and minimality proofs) is claimed, and no critical or
high finding remains open.

`0.74.0 implementation stop reached. Run pentest for this exact commit.`

### v0.75.0 — HPACK integer overflow and minimality proofs

Status: planned

#### Goal

Deliver **HPACK integer overflow and minimality proofs** as the only primary capability in this stop. It builds
on v0.74.0 (HPACK prefix-integer encoder) and must be independently trustworthy before v0.76.0 (HPACK string representation codec) begins.

#### Deliverables

- Implement and document HPACK integer overflow and minimality proofs in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK integer overflow and minimality proofs.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK integer overflow and minimality proofs contract is complete, its named evidence is reproducible, v0.74.0 (HPACK prefix-integer encoder)
still passes, no capability assigned to v0.76.0 (HPACK string representation codec) is claimed, and no critical or
high finding remains open.

`0.75.0 implementation stop reached. Run pentest for this exact commit.`

### v0.76.0 — HPACK string representation codec

Status: planned

#### Goal

Deliver **HPACK string representation codec** as the only primary capability in this stop. It builds
on v0.75.0 (HPACK integer overflow and minimality proofs) and must be independently trustworthy before v0.77.0 (HPACK Huffman tables) begins.

#### Deliverables

- Implement and document HPACK string representation codec in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK string representation codec.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK string representation codec contract is complete, its named evidence is reproducible, v0.75.0 (HPACK integer overflow and minimality proofs)
still passes, no capability assigned to v0.77.0 (HPACK Huffman tables) is claimed, and no critical or
high finding remains open.

`0.76.0 implementation stop reached. Run pentest for this exact commit.`

### v0.77.0 — HPACK Huffman tables

Status: planned

#### Goal

Deliver **HPACK Huffman tables** as the only primary capability in this stop. It builds
on v0.76.0 (HPACK string representation codec) and must be independently trustworthy before v0.78.0 (HPACK Huffman decoder) begins.

#### Deliverables

- Implement and document HPACK Huffman tables in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK Huffman tables.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK Huffman tables contract is complete, its named evidence is reproducible, v0.76.0 (HPACK string representation codec)
still passes, no capability assigned to v0.78.0 (HPACK Huffman decoder) is claimed, and no critical or
high finding remains open.

`0.77.0 implementation stop reached. Run pentest for this exact commit.`

### v0.78.0 — HPACK Huffman decoder

Status: planned

#### Goal

Deliver **HPACK Huffman decoder** as the only primary capability in this stop. It builds
on v0.77.0 (HPACK Huffman tables) and must be independently trustworthy before v0.79.0 (HPACK Huffman encoder) begins.

#### Deliverables

- Implement and document HPACK Huffman decoder in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK Huffman decoder.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK Huffman decoder contract is complete, its named evidence is reproducible, v0.77.0 (HPACK Huffman tables)
still passes, no capability assigned to v0.79.0 (HPACK Huffman encoder) is claimed, and no critical or
high finding remains open.

`0.78.0 implementation stop reached. Run pentest for this exact commit.`

### v0.79.0 — HPACK Huffman encoder

Status: planned

#### Goal

Deliver **HPACK Huffman encoder** as the only primary capability in this stop. It builds
on v0.78.0 (HPACK Huffman decoder) and must be independently trustworthy before v0.80.0 (HPACK static table) begins.

#### Deliverables

- Implement and document HPACK Huffman encoder in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK Huffman encoder.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK Huffman encoder contract is complete, its named evidence is reproducible, v0.78.0 (HPACK Huffman decoder)
still passes, no capability assigned to v0.80.0 (HPACK static table) is claimed, and no critical or
high finding remains open.

`0.79.0 implementation stop reached. Run pentest for this exact commit.`

### v0.80.0 — HPACK static table

Status: planned

#### Goal

Deliver **HPACK static table** as the only primary capability in this stop. It builds
on v0.79.0 (HPACK Huffman encoder) and must be independently trustworthy before v0.81.0 (HPACK dynamic table storage) begins.

#### Deliverables

- Implement and document HPACK static table in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK static table.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK static table contract is complete, its named evidence is reproducible, v0.79.0 (HPACK Huffman encoder)
still passes, no capability assigned to v0.81.0 (HPACK dynamic table storage) is claimed, and no critical or
high finding remains open.

`0.80.0 implementation stop reached. Run pentest for this exact commit.`

### v0.81.0 — HPACK dynamic table storage

Status: planned

#### Goal

Deliver **HPACK dynamic table storage** as the only primary capability in this stop. It builds
on v0.80.0 (HPACK static table) and must be independently trustworthy before v0.82.0 (HPACK eviction and oversize-entry behavior) begins.

#### Deliverables

- Implement and document HPACK dynamic table storage in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK dynamic table storage.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK dynamic table storage contract is complete, its named evidence is reproducible, v0.80.0 (HPACK static table)
still passes, no capability assigned to v0.82.0 (HPACK eviction and oversize-entry behavior) is claimed, and no critical or
high finding remains open.

`0.81.0 implementation stop reached. Run pentest for this exact commit.`

### v0.82.0 — HPACK eviction and oversize-entry behavior

Status: planned

#### Goal

Deliver **HPACK eviction and oversize-entry behavior** as the only primary capability in this stop. It builds
on v0.81.0 (HPACK dynamic table storage) and must be independently trustworthy before v0.83.0 (HPACK table-size update and SETTINGS coupling) begins.

#### Deliverables

- Implement and document HPACK eviction and oversize-entry behavior in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK eviction and oversize-entry behavior.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK eviction and oversize-entry behavior contract is complete, its named evidence is reproducible, v0.81.0 (HPACK dynamic table storage)
still passes, no capability assigned to v0.83.0 (HPACK table-size update and SETTINGS coupling) is claimed, and no critical or
high finding remains open.

`0.82.0 implementation stop reached. Run pentest for this exact commit.`

### v0.83.0 — HPACK table-size update and SETTINGS coupling

Status: planned

#### Goal

Deliver **HPACK table-size update and SETTINGS coupling** as the only primary capability in this stop. It builds
on v0.82.0 (HPACK eviction and oversize-entry behavior) and must be independently trustworthy before v0.84.0 (HPACK caller-owned ring lookup) begins.

#### Deliverables

- Implement and document HPACK table-size update and SETTINGS coupling in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK table-size update and SETTINGS coupling.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK table-size update and SETTINGS coupling contract is complete, its named evidence is reproducible, v0.82.0 (HPACK eviction and oversize-entry behavior)
still passes, no capability assigned to v0.84.0 (HPACK caller-owned ring lookup) is claimed, and no critical or
high finding remains open.

`0.83.0 implementation stop reached. Run pentest for this exact commit.`

### v0.84.0 — HPACK caller-owned ring lookup

Status: planned

#### Goal

Deliver **HPACK caller-owned ring lookup** as the only primary capability in this stop. It builds
on v0.83.0 (HPACK table-size update and SETTINGS coupling) and must be independently trustworthy before v0.85.0 (HPACK indexed representation) begins.

#### Deliverables

- Implement and document HPACK caller-owned ring lookup in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK caller-owned ring lookup.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK caller-owned ring lookup contract is complete, its named evidence is reproducible, v0.83.0 (HPACK table-size update and SETTINGS coupling)
still passes, no capability assigned to v0.85.0 (HPACK indexed representation) is claimed, and no critical or
high finding remains open.

`0.84.0 implementation stop reached. Run pentest for this exact commit.`

### v0.85.0 — HPACK indexed representation

Status: planned

#### Goal

Deliver **HPACK indexed representation** as the only primary capability in this stop. It builds
on v0.84.0 (HPACK caller-owned ring lookup) and must be independently trustworthy before v0.86.0 (HPACK incremental-indexing literal) begins.

#### Deliverables

- Implement and document HPACK indexed representation in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK indexed representation.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK indexed representation contract is complete, its named evidence is reproducible, v0.84.0 (HPACK caller-owned ring lookup)
still passes, no capability assigned to v0.86.0 (HPACK incremental-indexing literal) is claimed, and no critical or
high finding remains open.

`0.85.0 implementation stop reached. Run pentest for this exact commit.`

### v0.86.0 — HPACK incremental-indexing literal

Status: planned

#### Goal

Deliver **HPACK incremental-indexing literal** as the only primary capability in this stop. It builds
on v0.85.0 (HPACK indexed representation) and must be independently trustworthy before v0.87.0 (HPACK non-indexing and never-indexed literal) begins.

#### Deliverables

- Implement and document HPACK incremental-indexing literal in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK incremental-indexing literal.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK incremental-indexing literal contract is complete, its named evidence is reproducible, v0.85.0 (HPACK indexed representation)
still passes, no capability assigned to v0.87.0 (HPACK non-indexing and never-indexed literal) is claimed, and no critical or
high finding remains open.

`0.86.0 implementation stop reached. Run pentest for this exact commit.`

### v0.87.0 — HPACK non-indexing and never-indexed literal

Status: planned

#### Goal

Deliver **HPACK non-indexing and never-indexed literal** as the only primary capability in this stop. It builds
on v0.86.0 (HPACK incremental-indexing literal) and must be independently trustworthy before v0.88.0 (Sensitive-field indexing policy) begins.

#### Deliverables

- Implement and document HPACK non-indexing and never-indexed literal in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK non-indexing and never-indexed literal.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK non-indexing and never-indexed literal contract is complete, its named evidence is reproducible, v0.86.0 (HPACK incremental-indexing literal)
still passes, no capability assigned to v0.88.0 (Sensitive-field indexing policy) is claimed, and no critical or
high finding remains open.

`0.87.0 implementation stop reached. Run pentest for this exact commit.`

### v0.88.0 — Sensitive-field indexing policy

Status: planned

#### Goal

Deliver **Sensitive-field indexing policy** as the only primary capability in this stop. It builds
on v0.87.0 (HPACK non-indexing and never-indexed literal) and must be independently trustworthy before v0.89.0 (Independent HPACK decode limits) begins.

#### Deliverables

- Implement and document Sensitive-field indexing policy in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Sensitive-field indexing policy.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Sensitive-field indexing policy contract is complete, its named evidence is reproducible, v0.87.0 (HPACK non-indexing and never-indexed literal)
still passes, no capability assigned to v0.89.0 (Independent HPACK decode limits) is claimed, and no critical or
high finding remains open.

`0.88.0 implementation stop reached. Run pentest for this exact commit.`

### v0.89.0 — Independent HPACK decode limits

Status: planned

#### Goal

Deliver **Independent HPACK decode limits** as the only primary capability in this stop. It builds
on v0.88.0 (Sensitive-field indexing policy) and must be independently trustworthy before v0.90.0 (Transactional HPACK context and error scope) begins.

#### Deliverables

- Implement and document Independent HPACK decode limits in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Independent HPACK decode limits.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Independent HPACK decode limits contract is complete, its named evidence is reproducible, v0.88.0 (Sensitive-field indexing policy)
still passes, no capability assigned to v0.90.0 (Transactional HPACK context and error scope) is claimed, and no critical or
high finding remains open.

`0.89.0 implementation stop reached. Run pentest for this exact commit.`

### v0.90.0 — Transactional HPACK context and error scope

Status: planned

#### Goal

Deliver **Transactional HPACK context and error scope** as the only primary capability in this stop. It builds
on v0.89.0 (Independent HPACK decode limits) and must be independently trustworthy before v0.91.0 (HPACK conformance audit and pentest) begins.

#### Deliverables

- Implement and document Transactional HPACK context and error scope in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Transactional HPACK context and error scope.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Transactional HPACK context and error scope contract is complete, its named evidence is reproducible, v0.89.0 (Independent HPACK decode limits)
still passes, no capability assigned to v0.91.0 (HPACK conformance audit and pentest) is claimed, and no critical or
high finding remains open.

`0.90.0 implementation stop reached. Run pentest for this exact commit.`

### v0.91.0 — HPACK conformance audit and pentest

Status: planned

#### Goal

Deliver **HPACK conformance audit and pentest** as the only primary capability in this stop. It builds
on v0.90.0 (Transactional HPACK context and error scope) and must be independently trustworthy before v0.92.0 (HTTP/2 client and server prefaces) begins.

#### Deliverables

- Implement and document HPACK conformance audit and pentest in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HPACK conformance audit and pentest.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HPACK conformance audit and pentest contract is complete, its named evidence is reproducible, v0.90.0 (Transactional HPACK context and error scope)
still passes, no capability assigned to v0.92.0 (HTTP/2 client and server prefaces) is claimed, and no critical or
high finding remains open.

`0.91.0 implementation stop reached. Run pentest for this exact commit.`

### v0.92.0 — HTTP/2 client and server prefaces

Status: planned

#### Goal

Deliver **HTTP/2 client and server prefaces** as the only primary capability in this stop. It builds
on v0.91.0 (HPACK conformance audit and pentest) and must be independently trustworthy before v0.93.0 (HTTP/2 frame-header codec) begins.

#### Deliverables

- Implement and document HTTP/2 client and server prefaces in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/2 client and server prefaces.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/2 client and server prefaces contract is complete, its named evidence is reproducible, v0.91.0 (HPACK conformance audit and pentest)
still passes, no capability assigned to v0.93.0 (HTTP/2 frame-header codec) is claimed, and no critical or
high finding remains open.

`0.92.0 implementation stop reached. Run pentest for this exact commit.`

### v0.93.0 — HTTP/2 frame-header codec

Status: planned

#### Goal

Deliver **HTTP/2 frame-header codec** as the only primary capability in this stop. It builds
on v0.92.0 (HTTP/2 client and server prefaces) and must be independently trustworthy before v0.94.0 (DATA frame codec) begins.

#### Deliverables

- Implement and document HTTP/2 frame-header codec in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/2 frame-header codec.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/2 frame-header codec contract is complete, its named evidence is reproducible, v0.92.0 (HTTP/2 client and server prefaces)
still passes, no capability assigned to v0.94.0 (DATA frame codec) is claimed, and no critical or
high finding remains open.

`0.93.0 implementation stop reached. Run pentest for this exact commit.`

### v0.94.0 — DATA frame codec

Status: planned

#### Goal

Deliver **DATA frame codec** as the only primary capability in this stop. It builds
on v0.93.0 (HTTP/2 frame-header codec) and must be independently trustworthy before v0.95.0 (HEADERS frame codec) begins.

#### Deliverables

- Implement and document DATA frame codec in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for DATA frame codec.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The DATA frame codec contract is complete, its named evidence is reproducible, v0.93.0 (HTTP/2 frame-header codec)
still passes, no capability assigned to v0.95.0 (HEADERS frame codec) is claimed, and no critical or
high finding remains open.

`0.94.0 implementation stop reached. Run pentest for this exact commit.`

### v0.95.0 — HEADERS frame codec

Status: planned

#### Goal

Deliver **HEADERS frame codec** as the only primary capability in this stop. It builds
on v0.94.0 (DATA frame codec) and must be independently trustworthy before v0.96.0 (CONTINUATION frame codec) begins.

#### Deliverables

- Implement and document HEADERS frame codec in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HEADERS frame codec.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HEADERS frame codec contract is complete, its named evidence is reproducible, v0.94.0 (DATA frame codec)
still passes, no capability assigned to v0.96.0 (CONTINUATION frame codec) is claimed, and no critical or
high finding remains open.

`0.95.0 implementation stop reached. Run pentest for this exact commit.`

### v0.96.0 — CONTINUATION frame codec

Status: planned

#### Goal

Deliver **CONTINUATION frame codec** as the only primary capability in this stop. It builds
on v0.95.0 (HEADERS frame codec) and must be independently trustworthy before v0.97.0 (SETTINGS frame codec) begins.

#### Deliverables

- Implement and document CONTINUATION frame codec in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for CONTINUATION frame codec.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The CONTINUATION frame codec contract is complete, its named evidence is reproducible, v0.95.0 (HEADERS frame codec)
still passes, no capability assigned to v0.97.0 (SETTINGS frame codec) is claimed, and no critical or
high finding remains open.

`0.96.0 implementation stop reached. Run pentest for this exact commit.`

### v0.97.0 — SETTINGS frame codec

Status: planned

#### Goal

Deliver **SETTINGS frame codec** as the only primary capability in this stop. It builds
on v0.96.0 (CONTINUATION frame codec) and must be independently trustworthy before v0.98.0 (PING frame codec) begins.

#### Deliverables

- Implement and document SETTINGS frame codec in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for SETTINGS frame codec.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The SETTINGS frame codec contract is complete, its named evidence is reproducible, v0.96.0 (CONTINUATION frame codec)
still passes, no capability assigned to v0.98.0 (PING frame codec) is claimed, and no critical or
high finding remains open.

`0.97.0 implementation stop reached. Run pentest for this exact commit.`

### v0.98.0 — PING frame codec

Status: planned

#### Goal

Deliver **PING frame codec** as the only primary capability in this stop. It builds
on v0.97.0 (SETTINGS frame codec) and must be independently trustworthy before v0.99.0 (GOAWAY frame codec) begins.

#### Deliverables

- Implement and document PING frame codec in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for PING frame codec.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The PING frame codec contract is complete, its named evidence is reproducible, v0.97.0 (SETTINGS frame codec)
still passes, no capability assigned to v0.99.0 (GOAWAY frame codec) is claimed, and no critical or
high finding remains open.

`0.98.0 implementation stop reached. Run pentest for this exact commit.`

### v0.99.0 — GOAWAY frame codec

Status: planned

#### Goal

Deliver **GOAWAY frame codec** as the only primary capability in this stop. It builds
on v0.98.0 (PING frame codec) and must be independently trustworthy before v0.100.0 (RST_STREAM frame codec) begins.

#### Deliverables

- Implement and document GOAWAY frame codec in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for GOAWAY frame codec.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The GOAWAY frame codec contract is complete, its named evidence is reproducible, v0.98.0 (PING frame codec)
still passes, no capability assigned to v0.100.0 (RST_STREAM frame codec) is claimed, and no critical or
high finding remains open.

`0.99.0 implementation stop reached. Run pentest for this exact commit.`

### v0.100.0 — RST_STREAM frame codec

Status: planned

#### Goal

Deliver **RST_STREAM frame codec** as the only primary capability in this stop. It builds
on v0.99.0 (GOAWAY frame codec) and must be independently trustworthy before v0.101.0 (WINDOW_UPDATE codec and checked windows) begins.

#### Deliverables

- Implement and document RST_STREAM frame codec in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for RST_STREAM frame codec.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The RST_STREAM frame codec contract is complete, its named evidence is reproducible, v0.99.0 (GOAWAY frame codec)
still passes, no capability assigned to v0.101.0 (WINDOW_UPDATE codec and checked windows) is claimed, and no critical or
high finding remains open.

`0.100.0 implementation stop reached. Run pentest for this exact commit.`

### v0.101.0 — WINDOW_UPDATE codec and checked windows

Status: planned

#### Goal

Deliver **WINDOW_UPDATE codec and checked windows** as the only primary capability in this stop. It builds
on v0.100.0 (RST_STREAM frame codec) and must be independently trustworthy before v0.102.0 (Legacy PRIORITY frame handling) begins.

#### Deliverables

- Implement and document WINDOW_UPDATE codec and checked windows in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for WINDOW_UPDATE codec and checked windows.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The WINDOW_UPDATE codec and checked windows contract is complete, its named evidence is reproducible, v0.100.0 (RST_STREAM frame codec)
still passes, no capability assigned to v0.102.0 (Legacy PRIORITY frame handling) is claimed, and no critical or
high finding remains open.

`0.101.0 implementation stop reached. Run pentest for this exact commit.`

### v0.102.0 — Legacy PRIORITY frame handling

Status: planned

#### Goal

Deliver **Legacy PRIORITY frame handling** as the only primary capability in this stop. It builds
on v0.101.0 (WINDOW_UPDATE codec and checked windows) and must be independently trustworthy before v0.103.0 (PUSH_PROMISE frame handling) begins.

#### Deliverables

- Implement and document Legacy PRIORITY frame handling in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Legacy PRIORITY frame handling.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Legacy PRIORITY frame handling contract is complete, its named evidence is reproducible, v0.101.0 (WINDOW_UPDATE codec and checked windows)
still passes, no capability assigned to v0.103.0 (PUSH_PROMISE frame handling) is claimed, and no critical or
high finding remains open.

`0.102.0 implementation stop reached. Run pentest for this exact commit.`

### v0.103.0 — PUSH_PROMISE frame handling

Status: planned

#### Goal

Deliver **PUSH_PROMISE frame handling** as the only primary capability in this stop. It builds
on v0.102.0 (Legacy PRIORITY frame handling) and must be independently trustworthy before v0.104.0 (Unknown-frame extension policy) begins.

#### Deliverables

- Implement and document PUSH_PROMISE frame handling in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for PUSH_PROMISE frame handling.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The PUSH_PROMISE frame handling contract is complete, its named evidence is reproducible, v0.102.0 (Legacy PRIORITY frame handling)
still passes, no capability assigned to v0.104.0 (Unknown-frame extension policy) is claimed, and no critical or
high finding remains open.

`0.103.0 implementation stop reached. Run pentest for this exact commit.`

### v0.104.0 — Unknown-frame extension policy

Status: planned

#### Goal

Deliver **Unknown-frame extension policy** as the only primary capability in this stop. It builds
on v0.103.0 (PUSH_PROMISE frame handling) and must be independently trustworthy before v0.105.0 (HTTP/2 stream-identifier rules) begins.

#### Deliverables

- Implement and document Unknown-frame extension policy in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Unknown-frame extension policy.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Unknown-frame extension policy contract is complete, its named evidence is reproducible, v0.103.0 (PUSH_PROMISE frame handling)
still passes, no capability assigned to v0.105.0 (HTTP/2 stream-identifier rules) is claimed, and no critical or
high finding remains open.

`0.104.0 implementation stop reached. Run pentest for this exact commit.`

### v0.105.0 — HTTP/2 stream-identifier rules

Status: planned

#### Goal

Deliver **HTTP/2 stream-identifier rules** as the only primary capability in this stop. It builds
on v0.104.0 (Unknown-frame extension policy) and must be independently trustworthy before v0.106.0 (Generation-checked stream table and tombstones) begins.

#### Deliverables

- Implement and document HTTP/2 stream-identifier rules in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/2 stream-identifier rules.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/2 stream-identifier rules contract is complete, its named evidence is reproducible, v0.104.0 (Unknown-frame extension policy)
still passes, no capability assigned to v0.106.0 (Generation-checked stream table and tombstones) is claimed, and no critical or
high finding remains open.

`0.105.0 implementation stop reached. Run pentest for this exact commit.`

### v0.106.0 — Generation-checked stream table and tombstones

Status: planned

#### Goal

Deliver **Generation-checked stream table and tombstones** as the only primary capability in this stop. It builds
on v0.105.0 (HTTP/2 stream-identifier rules) and must be independently trustworthy before v0.107.0 (Exhaustive stream-state graph) begins.

#### Deliverables

- Implement and document Generation-checked stream table and tombstones in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Generation-checked stream table and tombstones.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Generation-checked stream table and tombstones contract is complete, its named evidence is reproducible, v0.105.0 (HTTP/2 stream-identifier rules)
still passes, no capability assigned to v0.107.0 (Exhaustive stream-state graph) is claimed, and no critical or
high finding remains open.

`0.106.0 implementation stop reached. Run pentest for this exact commit.`

### v0.107.0 — Exhaustive stream-state graph

Status: planned

#### Goal

Deliver **Exhaustive stream-state graph** as the only primary capability in this stop. It builds
on v0.106.0 (Generation-checked stream table and tombstones) and must be independently trustworthy before v0.108.0 (Connection sequencing and error-scope deltas) begins.

#### Deliverables

- Implement and document Exhaustive stream-state graph in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Exhaustive stream-state graph.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Exhaustive stream-state graph contract is complete, its named evidence is reproducible, v0.106.0 (Generation-checked stream table and tombstones)
still passes, no capability assigned to v0.108.0 (Connection sequencing and error-scope deltas) is claimed, and no critical or
high finding remains open.

`0.107.0 implementation stop reached. Run pentest for this exact commit.`

### v0.108.0 — Connection sequencing and error-scope deltas

Status: planned

#### Goal

Deliver **Connection sequencing and error-scope deltas** as the only primary capability in this stop. It builds
on v0.107.0 (Exhaustive stream-state graph) and must be independently trustworthy before v0.109.0 (Atomic HPACK header-block integration) begins.

#### Deliverables

- Implement and document Connection sequencing and error-scope deltas in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Connection sequencing and error-scope deltas.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Connection sequencing and error-scope deltas contract is complete, its named evidence is reproducible, v0.107.0 (Exhaustive stream-state graph)
still passes, no capability assigned to v0.109.0 (Atomic HPACK header-block integration) is claimed, and no critical or
high finding remains open.

`0.108.0 implementation stop reached. Run pentest for this exact commit.`

### v0.109.0 — Atomic HPACK header-block integration

Status: planned

#### Goal

Deliver **Atomic HPACK header-block integration** as the only primary capability in this stop. It builds
on v0.108.0 (Connection sequencing and error-scope deltas) and must be independently trustworthy before v0.110.0 (Pseudo-field ordering and uniqueness) begins.

#### Deliverables

- Implement and document Atomic HPACK header-block integration in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Atomic HPACK header-block integration.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Atomic HPACK header-block integration contract is complete, its named evidence is reproducible, v0.108.0 (Connection sequencing and error-scope deltas)
still passes, no capability assigned to v0.110.0 (Pseudo-field ordering and uniqueness) is claimed, and no critical or
high finding remains open.

`0.109.0 implementation stop reached. Run pentest for this exact commit.`

### v0.110.0 — Pseudo-field ordering and uniqueness

Status: planned

#### Goal

Deliver **Pseudo-field ordering and uniqueness** as the only primary capability in this stop. It builds
on v0.109.0 (Atomic HPACK header-block integration) and must be independently trustworthy before v0.111.0 (Connection-specific field and TE validation) begins.

#### Deliverables

- Implement and document Pseudo-field ordering and uniqueness in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Pseudo-field ordering and uniqueness.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Pseudo-field ordering and uniqueness contract is complete, its named evidence is reproducible, v0.109.0 (Atomic HPACK header-block integration)
still passes, no capability assigned to v0.111.0 (Connection-specific field and TE validation) is claimed, and no critical or
high finding remains open.

`0.110.0 implementation stop reached. Run pentest for this exact commit.`

### v0.111.0 — Connection-specific field and TE validation

Status: planned

#### Goal

Deliver **Connection-specific field and TE validation** as the only primary capability in this stop. It builds
on v0.110.0 (Pseudo-field ordering and uniqueness) and must be independently trustworthy before v0.112.0 (HTTP/2 request mapping) begins.

#### Deliverables

- Implement and document Connection-specific field and TE validation in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Connection-specific field and TE validation.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Connection-specific field and TE validation contract is complete, its named evidence is reproducible, v0.110.0 (Pseudo-field ordering and uniqueness)
still passes, no capability assigned to v0.112.0 (HTTP/2 request mapping) is claimed, and no critical or
high finding remains open.

`0.111.0 implementation stop reached. Run pentest for this exact commit.`

### v0.112.0 — HTTP/2 request mapping

Status: planned

#### Goal

Deliver **HTTP/2 request mapping** as the only primary capability in this stop. It builds
on v0.111.0 (Connection-specific field and TE validation) and must be independently trustworthy before v0.113.0 (HTTP/2 response mapping) begins.

#### Deliverables

- Implement and document HTTP/2 request mapping in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/2 request mapping.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/2 request mapping contract is complete, its named evidence is reproducible, v0.111.0 (Connection-specific field and TE validation)
still passes, no capability assigned to v0.113.0 (HTTP/2 response mapping) is claimed, and no critical or
high finding remains open.

`0.112.0 implementation stop reached. Run pentest for this exact commit.`

### v0.113.0 — HTTP/2 response mapping

Status: planned

#### Goal

Deliver **HTTP/2 response mapping** as the only primary capability in this stop. It builds
on v0.112.0 (HTTP/2 request mapping) and must be independently trustworthy before v0.114.0 (Informational responses and trailers) begins.

#### Deliverables

- Implement and document HTTP/2 response mapping in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/2 response mapping.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/2 response mapping contract is complete, its named evidence is reproducible, v0.112.0 (HTTP/2 request mapping)
still passes, no capability assigned to v0.114.0 (Informational responses and trailers) is claimed, and no critical or
high finding remains open.

`0.113.0 implementation stop reached. Run pentest for this exact commit.`

### v0.114.0 — Informational responses and trailers

Status: planned

#### Goal

Deliver **Informational responses and trailers** as the only primary capability in this stop. It builds
on v0.113.0 (HTTP/2 response mapping) and must be independently trustworthy before v0.115.0 (Cookie field combination and Set-Cookie preservation) begins.

#### Deliverables

- Implement and document Informational responses and trailers in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Informational responses and trailers.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Informational responses and trailers contract is complete, its named evidence is reproducible, v0.113.0 (HTTP/2 response mapping)
still passes, no capability assigned to v0.115.0 (Cookie field combination and Set-Cookie preservation) is claimed, and no critical or
high finding remains open.

`0.114.0 implementation stop reached. Run pentest for this exact commit.`

### v0.115.0 — Cookie field combination and Set-Cookie preservation

Status: planned

#### Goal

Deliver **Cookie field combination and Set-Cookie preservation** as the only primary capability in this stop. It builds
on v0.114.0 (Informational responses and trailers) and must be independently trustworthy before v0.116.0 (Stream flow control) begins.

#### Deliverables

- Implement and document Cookie field combination and Set-Cookie preservation in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Cookie field combination and Set-Cookie preservation.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Cookie field combination and Set-Cookie preservation contract is complete, its named evidence is reproducible, v0.114.0 (Informational responses and trailers)
still passes, no capability assigned to v0.116.0 (Stream flow control) is claimed, and no critical or
high finding remains open.

`0.115.0 implementation stop reached. Run pentest for this exact commit.`

### v0.116.0 — Stream flow control

Status: planned

#### Goal

Deliver **Stream flow control** as the only primary capability in this stop. It builds
on v0.115.0 (Cookie field combination and Set-Cookie preservation) and must be independently trustworthy before v0.117.0 (Connection flow control) begins.

#### Deliverables

- Implement and document Stream flow control in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Stream flow control.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Stream flow control contract is complete, its named evidence is reproducible, v0.115.0 (Cookie field combination and Set-Cookie preservation)
still passes, no capability assigned to v0.117.0 (Connection flow control) is claimed, and no critical or
high finding remains open.

`0.116.0 implementation stop reached. Run pentest for this exact commit.`

### v0.117.0 — Connection flow control

Status: planned

#### Goal

Deliver **Connection flow control** as the only primary capability in this stop. It builds
on v0.116.0 (Stream flow control) and must be independently trustworthy before v0.118.0 (SETTINGS outstanding-ACK accounting) begins.

#### Deliverables

- Implement and document Connection flow control in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Connection flow control.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Connection flow control contract is complete, its named evidence is reproducible, v0.116.0 (Stream flow control)
still passes, no capability assigned to v0.118.0 (SETTINGS outstanding-ACK accounting) is claimed, and no critical or
high finding remains open.

`0.117.0 implementation stop reached. Run pentest for this exact commit.`

### v0.118.0 — SETTINGS outstanding-ACK accounting

Status: planned

#### Goal

Deliver **SETTINGS outstanding-ACK accounting** as the only primary capability in this stop. It builds
on v0.117.0 (Connection flow control) and must be independently trustworthy before v0.119.0 (Bounded stream admission) begins.

#### Deliverables

- Implement and document SETTINGS outstanding-ACK accounting in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for SETTINGS outstanding-ACK accounting.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The SETTINGS outstanding-ACK accounting contract is complete, its named evidence is reproducible, v0.117.0 (Connection flow control)
still passes, no capability assigned to v0.119.0 (Bounded stream admission) is claimed, and no critical or
high finding remains open.

`0.118.0 implementation stop reached. Run pentest for this exact commit.`

### v0.119.0 — Bounded stream admission

Status: planned

#### Goal

Deliver **Bounded stream admission** as the only primary capability in this stop. It builds
on v0.118.0 (SETTINGS outstanding-ACK accounting) and must be independently trustworthy before v0.120.0 (Bounded outbound scheduling) begins.

#### Deliverables

- Implement and document Bounded stream admission in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Bounded stream admission.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Bounded stream admission contract is complete, its named evidence is reproducible, v0.118.0 (SETTINGS outstanding-ACK accounting)
still passes, no capability assigned to v0.120.0 (Bounded outbound scheduling) is claimed, and no critical or
high finding remains open.

`0.119.0 implementation stop reached. Run pentest for this exact commit.`

### v0.120.0 — Bounded outbound scheduling

Status: planned

#### Goal

Deliver **Bounded outbound scheduling** as the only primary capability in this stop. It builds
on v0.119.0 (Bounded stream admission) and must be independently trustworthy before v0.121.0 (GOAWAY cutoff and retry classification) begins.

#### Deliverables

- Implement and document Bounded outbound scheduling in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Bounded outbound scheduling.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Bounded outbound scheduling contract is complete, its named evidence is reproducible, v0.119.0 (Bounded stream admission)
still passes, no capability assigned to v0.121.0 (GOAWAY cutoff and retry classification) is claimed, and no critical or
high finding remains open.

`0.120.0 implementation stop reached. Run pentest for this exact commit.`

### v0.121.0 — GOAWAY cutoff and retry classification

Status: planned

#### Goal

Deliver **GOAWAY cutoff and retry classification** as the only primary capability in this stop. It builds
on v0.120.0 (Bounded outbound scheduling) and must be independently trustworthy before v0.122.0 (Server-push lifecycle) begins.

#### Deliverables

- Implement and document GOAWAY cutoff and retry classification in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for GOAWAY cutoff and retry classification.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The GOAWAY cutoff and retry classification contract is complete, its named evidence is reproducible, v0.120.0 (Bounded outbound scheduling)
still passes, no capability assigned to v0.122.0 (Server-push lifecycle) is claimed, and no critical or
high finding remains open.

`0.121.0 implementation stop reached. Run pentest for this exact commit.`

### v0.122.0 — Server-push lifecycle

Status: planned

#### Goal

Deliver **Server-push lifecycle** as the only primary capability in this stop. It builds
on v0.121.0 (GOAWAY cutoff and retry classification) and must be independently trustworthy before v0.123.0 (ALPN and cleartext prior-knowledge selection) begins.

#### Deliverables

- Implement and document Server-push lifecycle in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Server-push lifecycle.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Server-push lifecycle contract is complete, its named evidence is reproducible, v0.121.0 (GOAWAY cutoff and retry classification)
still passes, no capability assigned to v0.123.0 (ALPN and cleartext prior-knowledge selection) is claimed, and no critical or
high finding remains open.

`0.122.0 implementation stop reached. Run pentest for this exact commit.`

### v0.123.0 — ALPN and cleartext prior-knowledge selection

Status: planned

#### Goal

Deliver **ALPN and cleartext prior-knowledge selection** as the only primary capability in this stop. It builds
on v0.122.0 (Server-push lifecycle) and must be independently trustworthy before v0.124.0 (Independent HTTP/2 rate and work budgets) begins.

#### Deliverables

- Implement and document ALPN and cleartext prior-knowledge selection in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for ALPN and cleartext prior-knowledge selection.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The ALPN and cleartext prior-knowledge selection contract is complete, its named evidence is reproducible, v0.122.0 (Server-push lifecycle)
still passes, no capability assigned to v0.124.0 (Independent HTTP/2 rate and work budgets) is claimed, and no critical or
high finding remains open.

`0.123.0 implementation stop reached. Run pentest for this exact commit.`

### v0.124.0 — Independent HTTP/2 rate and work budgets

Status: planned

#### Goal

Deliver **Independent HTTP/2 rate and work budgets** as the only primary capability in this stop. It builds
on v0.123.0 (ALPN and cleartext prior-knowledge selection) and must be independently trustworthy before v0.125.0 (Rapid-reset defenses) begins.

#### Deliverables

- Implement and document Independent HTTP/2 rate and work budgets in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Independent HTTP/2 rate and work budgets.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Independent HTTP/2 rate and work budgets contract is complete, its named evidence is reproducible, v0.123.0 (ALPN and cleartext prior-knowledge selection)
still passes, no capability assigned to v0.125.0 (Rapid-reset defenses) is claimed, and no critical or
high finding remains open.

`0.124.0 implementation stop reached. Run pentest for this exact commit.`

### v0.125.0 — Rapid-reset defenses

Status: planned

#### Goal

Deliver **Rapid-reset defenses** as the only primary capability in this stop. It builds
on v0.124.0 (Independent HTTP/2 rate and work budgets) and must be independently trustworthy before v0.126.0 (SETTINGS amplification defenses) begins.

#### Deliverables

- Implement and document Rapid-reset defenses in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Rapid-reset defenses.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Rapid-reset defenses contract is complete, its named evidence is reproducible, v0.124.0 (Independent HTTP/2 rate and work budgets)
still passes, no capability assigned to v0.126.0 (SETTINGS amplification defenses) is claimed, and no critical or
high finding remains open.

`0.125.0 implementation stop reached. Run pentest for this exact commit.`

### v0.126.0 — SETTINGS amplification defenses

Status: planned

#### Goal

Deliver **SETTINGS amplification defenses** as the only primary capability in this stop. It builds
on v0.125.0 (Rapid-reset defenses) and must be independently trustworthy before v0.127.0 (PING flood defenses) begins.

#### Deliverables

- Implement and document SETTINGS amplification defenses in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for SETTINGS amplification defenses.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The SETTINGS amplification defenses contract is complete, its named evidence is reproducible, v0.125.0 (Rapid-reset defenses)
still passes, no capability assigned to v0.127.0 (PING flood defenses) is claimed, and no critical or
high finding remains open.

`0.126.0 implementation stop reached. Run pentest for this exact commit.`

### v0.127.0 — PING flood defenses

Status: planned

#### Goal

Deliver **PING flood defenses** as the only primary capability in this stop. It builds
on v0.126.0 (SETTINGS amplification defenses) and must be independently trustworthy before v0.128.0 (CONTINUATION bomb defenses) begins.

#### Deliverables

- Implement and document PING flood defenses in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for PING flood defenses.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The PING flood defenses contract is complete, its named evidence is reproducible, v0.126.0 (SETTINGS amplification defenses)
still passes, no capability assigned to v0.128.0 (CONTINUATION bomb defenses) is claimed, and no critical or
high finding remains open.

`0.127.0 implementation stop reached. Run pentest for this exact commit.`

### v0.128.0 — CONTINUATION bomb defenses

Status: planned

#### Goal

Deliver **CONTINUATION bomb defenses** as the only primary capability in this stop. It builds
on v0.127.0 (PING flood defenses) and must be independently trustworthy before v0.129.0 (WINDOW_UPDATE churn defenses) begins.

#### Deliverables

- Implement and document CONTINUATION bomb defenses in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for CONTINUATION bomb defenses.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The CONTINUATION bomb defenses contract is complete, its named evidence is reproducible, v0.127.0 (PING flood defenses)
still passes, no capability assigned to v0.129.0 (WINDOW_UPDATE churn defenses) is claimed, and no critical or
high finding remains open.

`0.128.0 implementation stop reached. Run pentest for this exact commit.`

### v0.129.0 — WINDOW_UPDATE churn defenses

Status: planned

#### Goal

Deliver **WINDOW_UPDATE churn defenses** as the only primary capability in this stop. It builds
on v0.128.0 (CONTINUATION bomb defenses) and must be independently trustworthy before v0.130.0 (Reserved control-output queues) begins.

#### Deliverables

- Implement and document WINDOW_UPDATE churn defenses in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for WINDOW_UPDATE churn defenses.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The WINDOW_UPDATE churn defenses contract is complete, its named evidence is reproducible, v0.128.0 (CONTINUATION bomb defenses)
still passes, no capability assigned to v0.130.0 (Reserved control-output queues) is claimed, and no critical or
high finding remains open.

`0.129.0 implementation stop reached. Run pentest for this exact commit.`

### v0.130.0 — Reserved control-output queues

Status: planned

#### Goal

Deliver **Reserved control-output queues** as the only primary capability in this stop. It builds
on v0.129.0 (WINDOW_UPDATE churn defenses) and must be independently trustworthy before v0.131.0 (HTTP/2 conformance audit and pentest) begins.

#### Deliverables

- Implement and document Reserved control-output queues in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Reserved control-output queues.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Reserved control-output queues contract is complete, its named evidence is reproducible, v0.129.0 (WINDOW_UPDATE churn defenses)
still passes, no capability assigned to v0.131.0 (HTTP/2 conformance audit and pentest) is claimed, and no critical or
high finding remains open.

`0.130.0 implementation stop reached. Run pentest for this exact commit.`

### v0.131.0 — HTTP/2 conformance audit and pentest

Status: planned

#### Goal

Deliver **HTTP/2 conformance audit and pentest** as the only primary capability in this stop. It builds
on v0.130.0 (Reserved control-output queues) and must be independently trustworthy before v0.132.0 (HTTP/1 and HTTP/2 translation model) begins.

#### Deliverables

- Implement and document HTTP/2 conformance audit and pentest in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: HPACK and HTTP/2 mutations validate into typed deltas before commit; connection state, stream slots, and output reservations remain bounded and generation-safe.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7541, RFC 9110, RFC 9113 including verified/held errata disposition, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/2 conformance audit and pentest.
- Run official vectors, every-byte fragmentation, malformed-frame and malformed-block corpora, exhaustive transition tests, generation-slot reuse tests, flow-control arithmetic tests, differential peers, and hostile control-frame campaigns.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/2 conformance audit and pentest contract is complete, its named evidence is reproducible, v0.130.0 (Reserved control-output queues)
still passes, no capability assigned to v0.132.0 (HTTP/1 and HTTP/2 translation model) is claimed, and no critical or
high finding remains open.

`0.131.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 4 — Proxy, client, server, and public APIs

Phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.

### v0.132.0 — HTTP/1 and HTTP/2 translation model

Status: planned

#### Goal

Deliver **HTTP/1 and HTTP/2 translation model** as the only primary capability in this stop. It builds
on v0.131.0 (HTTP/2 conformance audit and pentest) and must be independently trustworthy before v0.133.0 (Effective URI and authority consistency) begins.

#### Deliverables

- Implement and document HTTP/1 and HTTP/2 translation model in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for HTTP/1 and HTTP/2 translation model.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The HTTP/1 and HTTP/2 translation model contract is complete, its named evidence is reproducible, v0.131.0 (HTTP/2 conformance audit and pentest)
still passes, no capability assigned to v0.133.0 (Effective URI and authority consistency) is claimed, and no critical or
high finding remains open.

`0.132.0 implementation stop reached. Run pentest for this exact commit.`

### v0.133.0 — Effective URI and authority consistency

Status: planned

#### Goal

Deliver **Effective URI and authority consistency** as the only primary capability in this stop. It builds
on v0.132.0 (HTTP/1 and HTTP/2 translation model) and must be independently trustworthy before v0.134.0 (Connection-field stripping, Via, and cache preservation) begins.

#### Deliverables

- Implement and document Effective URI and authority consistency in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Effective URI and authority consistency.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Effective URI and authority consistency contract is complete, its named evidence is reproducible, v0.132.0 (HTTP/1 and HTTP/2 translation model)
still passes, no capability assigned to v0.134.0 (Connection-field stripping, Via, and cache preservation) is claimed, and no critical or
high finding remains open.

`0.133.0 implementation stop reached. Run pentest for this exact commit.`

### v0.134.0 — Connection-field stripping, Via, and cache preservation

Status: planned

#### Goal

Deliver **Connection-field stripping, Via, and cache preservation** as the only primary capability in this stop. It builds
on v0.133.0 (Effective URI and authority consistency) and must be independently trustworthy before v0.135.0 (CONNECT translation across HTTP versions) begins.

#### Deliverables

- Implement and document Connection-field stripping, Via, and cache preservation in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Connection-field stripping, Via, and cache preservation.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Connection-field stripping, Via, and cache preservation contract is complete, its named evidence is reproducible, v0.133.0 (Effective URI and authority consistency)
still passes, no capability assigned to v0.135.0 (CONNECT translation across HTTP versions) is claimed, and no critical or
high finding remains open.

`0.134.0 implementation stop reached. Run pentest for this exact commit.`

### v0.135.0 — CONNECT translation across HTTP versions

Status: planned

#### Goal

Deliver **CONNECT translation across HTTP versions** as the only primary capability in this stop. It builds
on v0.134.0 (Connection-field stripping, Via, and cache preservation) and must be independently trustworthy before v0.136.0 (RFC 8441 extended CONNECT) begins.

#### Deliverables

- Implement and document CONNECT translation across HTTP versions in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for CONNECT translation across HTTP versions.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The CONNECT translation across HTTP versions contract is complete, its named evidence is reproducible, v0.134.0 (Connection-field stripping, Via, and cache preservation)
still passes, no capability assigned to v0.136.0 (RFC 8441 extended CONNECT) is claimed, and no critical or
high finding remains open.

`0.135.0 implementation stop reached. Run pentest for this exact commit.`

### v0.136.0 — RFC 8441 extended CONNECT

Status: planned

#### Goal

Deliver **RFC 8441 extended CONNECT** as the only primary capability in this stop. It builds
on v0.135.0 (CONNECT translation across HTTP versions) and must be independently trustworthy before v0.137.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) begins.

#### Deliverables

- Implement and document RFC 8441 extended CONNECT in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for RFC 8441 extended CONNECT.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The RFC 8441 extended CONNECT contract is complete, its named evidence is reproducible, v0.135.0 (CONNECT translation across HTTP versions)
still passes, no capability assigned to v0.137.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) is claimed, and no critical or
high finding remains open.

`0.136.0 implementation stop reached. Run pentest for this exact commit.`

### v0.137.0 — WebSocket HTTP/1 to HTTP/2 handshake bridge

Status: planned

#### Goal

Deliver **WebSocket HTTP/1 to HTTP/2 handshake bridge** as the only primary capability in this stop. It builds
on v0.136.0 (RFC 8441 extended CONNECT) and must be independently trustworthy before v0.138.0 (Structured Fields) begins.

#### Deliverables

- Implement and document WebSocket HTTP/1 to HTTP/2 handshake bridge in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for WebSocket HTTP/1 to HTTP/2 handshake bridge.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The WebSocket HTTP/1 to HTTP/2 handshake bridge contract is complete, its named evidence is reproducible, v0.136.0 (RFC 8441 extended CONNECT)
still passes, no capability assigned to v0.138.0 (Structured Fields) is claimed, and no critical or
high finding remains open.

`0.137.0 implementation stop reached. Run pentest for this exact commit.`

### v0.138.0 — Structured Fields

Status: planned

#### Goal

Deliver **Structured Fields** as the only primary capability in this stop. It builds
on v0.137.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) and must be independently trustworthy before v0.139.0 (RFC 9218 priority semantics) begins.

#### Deliverables

- Implement and document Structured Fields in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Structured Fields.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Structured Fields contract is complete, its named evidence is reproducible, v0.137.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge)
still passes, no capability assigned to v0.139.0 (RFC 9218 priority semantics) is claimed, and no critical or
high finding remains open.

`0.138.0 implementation stop reached. Run pentest for this exact commit.`

### v0.139.0 — RFC 9218 priority semantics

Status: planned

#### Goal

Deliver **RFC 9218 priority semantics** as the only primary capability in this stop. It builds
on v0.138.0 (Structured Fields) and must be independently trustworthy before v0.140.0 (PRIORITY_UPDATE frame support) begins.

#### Deliverables

- Implement and document RFC 9218 priority semantics in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for RFC 9218 priority semantics.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The RFC 9218 priority semantics contract is complete, its named evidence is reproducible, v0.138.0 (Structured Fields)
still passes, no capability assigned to v0.140.0 (PRIORITY_UPDATE frame support) is claimed, and no critical or
high finding remains open.

`0.139.0 implementation stop reached. Run pentest for this exact commit.`

### v0.140.0 — PRIORITY_UPDATE frame support

Status: planned

#### Goal

Deliver **PRIORITY_UPDATE frame support** as the only primary capability in this stop. It builds
on v0.139.0 (RFC 9218 priority semantics) and must be independently trustworthy before v0.141.0 (Client request builder and target forms) begins.

#### Deliverables

- Implement and document PRIORITY_UPDATE frame support in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for PRIORITY_UPDATE frame support.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The PRIORITY_UPDATE frame support contract is complete, its named evidence is reproducible, v0.139.0 (RFC 9218 priority semantics)
still passes, no capability assigned to v0.141.0 (Client request builder and target forms) is claimed, and no critical or
high finding remains open.

`0.140.0 implementation stop reached. Run pentest for this exact commit.`

### v0.141.0 — Client request builder and target forms

Status: planned

#### Goal

Deliver **Client request builder and target forms** as the only primary capability in this stop. It builds
on v0.140.0 (PRIORITY_UPDATE frame support) and must be independently trustworthy before v0.142.0 (Client correlation, cancellation, and retry tokens) begins.

#### Deliverables

- Implement and document Client request builder and target forms in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Client request builder and target forms.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Client request builder and target forms contract is complete, its named evidence is reproducible, v0.140.0 (PRIORITY_UPDATE frame support)
still passes, no capability assigned to v0.142.0 (Client correlation, cancellation, and retry tokens) is claimed, and no critical or
high finding remains open.

`0.141.0 implementation stop reached. Run pentest for this exact commit.`

### v0.142.0 — Client correlation, cancellation, and retry tokens

Status: planned

#### Goal

Deliver **Client correlation, cancellation, and retry tokens** as the only primary capability in this stop. It builds
on v0.141.0 (Client request builder and target forms) and must be independently trustworthy before v0.143.0 (Origin-server role API) begins.

#### Deliverables

- Implement and document Client correlation, cancellation, and retry tokens in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Client correlation, cancellation, and retry tokens.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Client correlation, cancellation, and retry tokens contract is complete, its named evidence is reproducible, v0.141.0 (Client request builder and target forms)
still passes, no capability assigned to v0.143.0 (Origin-server role API) is claimed, and no critical or
high finding remains open.

`0.142.0 implementation stop reached. Run pentest for this exact commit.`

### v0.143.0 — Origin-server role API

Status: planned

#### Goal

Deliver **Origin-server role API** as the only primary capability in this stop. It builds
on v0.142.0 (Client correlation, cancellation, and retry tokens) and must be independently trustworthy before v0.144.0 (Forward-proxy role API) begins.

#### Deliverables

- Implement and document Origin-server role API in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Origin-server role API.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Origin-server role API contract is complete, its named evidence is reproducible, v0.142.0 (Client correlation, cancellation, and retry tokens)
still passes, no capability assigned to v0.144.0 (Forward-proxy role API) is claimed, and no critical or
high finding remains open.

`0.143.0 implementation stop reached. Run pentest for this exact commit.`

### v0.144.0 — Forward-proxy role API

Status: planned

#### Goal

Deliver **Forward-proxy role API** as the only primary capability in this stop. It builds
on v0.143.0 (Origin-server role API) and must be independently trustworthy before v0.145.0 (Reverse-proxy and gateway role API) begins.

#### Deliverables

- Implement and document Forward-proxy role API in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Forward-proxy role API.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Forward-proxy role API contract is complete, its named evidence is reproducible, v0.143.0 (Origin-server role API)
still passes, no capability assigned to v0.145.0 (Reverse-proxy and gateway role API) is claimed, and no critical or
high finding remains open.

`0.144.0 implementation stop reached. Run pentest for this exact commit.`

### v0.145.0 — Reverse-proxy and gateway role API

Status: planned

#### Goal

Deliver **Reverse-proxy and gateway role API** as the only primary capability in this stop. It builds
on v0.144.0 (Forward-proxy role API) and must be independently trustworthy before v0.146.0 (Tunnel lifecycle and half-close semantics) begins.

#### Deliverables

- Implement and document Reverse-proxy and gateway role API in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Reverse-proxy and gateway role API.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Reverse-proxy and gateway role API contract is complete, its named evidence is reproducible, v0.144.0 (Forward-proxy role API)
still passes, no capability assigned to v0.146.0 (Tunnel lifecycle and half-close semantics) is claimed, and no critical or
high finding remains open.

`0.145.0 implementation stop reached. Run pentest for this exact commit.`

### v0.146.0 — Tunnel lifecycle and half-close semantics

Status: planned

#### Goal

Deliver **Tunnel lifecycle and half-close semantics** as the only primary capability in this stop. It builds
on v0.145.0 (Reverse-proxy and gateway role API) and must be independently trustworthy before v0.147.0 (Upgrade transformation boundary) begins.

#### Deliverables

- Implement and document Tunnel lifecycle and half-close semantics in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Tunnel lifecycle and half-close semantics.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Tunnel lifecycle and half-close semantics contract is complete, its named evidence is reproducible, v0.145.0 (Reverse-proxy and gateway role API)
still passes, no capability assigned to v0.147.0 (Upgrade transformation boundary) is claimed, and no critical or
high finding remains open.

`0.146.0 implementation stop reached. Run pentest for this exact commit.`

### v0.147.0 — Upgrade transformation boundary

Status: planned

#### Goal

Deliver **Upgrade transformation boundary** as the only primary capability in this stop. It builds
on v0.146.0 (Tunnel lifecycle and half-close semantics) and must be independently trustworthy before v0.148.0 (GOAWAY, 421, and retry coordination) begins.

#### Deliverables

- Implement and document Upgrade transformation boundary in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Upgrade transformation boundary.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Upgrade transformation boundary contract is complete, its named evidence is reproducible, v0.146.0 (Tunnel lifecycle and half-close semantics)
still passes, no capability assigned to v0.148.0 (GOAWAY, 421, and retry coordination) is claimed, and no critical or
high finding remains open.

`0.147.0 implementation stop reached. Run pentest for this exact commit.`

### v0.148.0 — GOAWAY, 421, and retry coordination

Status: planned

#### Goal

Deliver **GOAWAY, 421, and retry coordination** as the only primary capability in this stop. It builds
on v0.147.0 (Upgrade transformation boundary) and must be independently trustworthy before v0.149.0 (Optional alloc-backed convenience API) begins.

#### Deliverables

- Implement and document GOAWAY, 421, and retry coordination in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for GOAWAY, 421, and retry coordination.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The GOAWAY, 421, and retry coordination contract is complete, its named evidence is reproducible, v0.147.0 (Upgrade transformation boundary)
still passes, no capability assigned to v0.149.0 (Optional alloc-backed convenience API) is claimed, and no critical or
high finding remains open.

`0.148.0 implementation stop reached. Run pentest for this exact commit.`

### v0.149.0 — Optional alloc-backed convenience API

Status: planned

#### Goal

Deliver **Optional alloc-backed convenience API** as the only primary capability in this stop. It builds
on v0.148.0 (GOAWAY, 421, and retry coordination) and must be independently trustworthy before v0.150.0 (Fixed-capacity caller-storage public API) begins.

#### Deliverables

- Implement and document Optional alloc-backed convenience API in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Optional alloc-backed convenience API.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Optional alloc-backed convenience API contract is complete, its named evidence is reproducible, v0.148.0 (GOAWAY, 421, and retry coordination)
still passes, no capability assigned to v0.150.0 (Fixed-capacity caller-storage public API) is claimed, and no critical or
high finding remains open.

`0.149.0 implementation stop reached. Run pentest for this exact commit.`

### v0.150.0 — Fixed-capacity caller-storage public API

Status: planned

#### Goal

Deliver **Fixed-capacity caller-storage public API** as the only primary capability in this stop. It builds
on v0.149.0 (Optional alloc-backed convenience API) and must be independently trustworthy before v0.151.0 (Stable diagnostics and security events) begins.

#### Deliverables

- Implement and document Fixed-capacity caller-storage public API in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Fixed-capacity caller-storage public API.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Fixed-capacity caller-storage public API contract is complete, its named evidence is reproducible, v0.149.0 (Optional alloc-backed convenience API)
still passes, no capability assigned to v0.151.0 (Stable diagnostics and security events) is claimed, and no critical or
high finding remains open.

`0.150.0 implementation stop reached. Run pentest for this exact commit.`

### v0.151.0 — Stable diagnostics and security events

Status: planned

#### Goal

Deliver **Stable diagnostics and security events** as the only primary capability in this stop. It builds
on v0.150.0 (Fixed-capacity caller-storage public API) and must be independently trustworthy before v0.152.0 (Feature and dependency-policy surface) begins.

#### Deliverables

- Implement and document Stable diagnostics and security events in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Stable diagnostics and security events.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Stable diagnostics and security events contract is complete, its named evidence is reproducible, v0.150.0 (Fixed-capacity caller-storage public API)
still passes, no capability assigned to v0.152.0 (Feature and dependency-policy surface) is claimed, and no critical or
high finding remains open.

`0.151.0 implementation stop reached. Run pentest for this exact commit.`

### v0.152.0 — Feature and dependency-policy surface

Status: planned

#### Goal

Deliver **Feature and dependency-policy surface** as the only primary capability in this stop. It builds
on v0.151.0 (Stable diagnostics and security events) and must be independently trustworthy before v0.153.0 (Multi-implementation interoperability) begins.

#### Deliverables

- Implement and document Feature and dependency-policy surface in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Feature and dependency-policy surface.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Feature and dependency-policy surface contract is complete, its named evidence is reproducible, v0.151.0 (Stable diagnostics and security events)
still passes, no capability assigned to v0.153.0 (Multi-implementation interoperability) is claimed, and no critical or
high finding remains open.

`0.152.0 implementation stop reached. Run pentest for this exact commit.`

### v0.153.0 — Multi-implementation interoperability

Status: planned

#### Goal

Deliver **Multi-implementation interoperability** as the only primary capability in this stop. It builds
on v0.152.0 (Feature and dependency-policy surface) and must be independently trustworthy before v0.154.0 (Adversarial and stateful fuzz campaign) begins.

#### Deliverables

- Implement and document Multi-implementation interoperability in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Multi-implementation interoperability.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Multi-implementation interoperability contract is complete, its named evidence is reproducible, v0.152.0 (Feature and dependency-policy surface)
still passes, no capability assigned to v0.154.0 (Adversarial and stateful fuzz campaign) is claimed, and no critical or
high finding remains open.

`0.153.0 implementation stop reached. Run pentest for this exact commit.`

### v0.154.0 — Adversarial and stateful fuzz campaign

Status: planned

#### Goal

Deliver **Adversarial and stateful fuzz campaign** as the only primary capability in this stop. It builds
on v0.153.0 (Multi-implementation interoperability) and must be independently trustworthy before v0.155.0 (Compile-fail state and lifetime tests) begins.

#### Deliverables

- Implement and document Adversarial and stateful fuzz campaign in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Adversarial and stateful fuzz campaign.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Adversarial and stateful fuzz campaign contract is complete, its named evidence is reproducible, v0.153.0 (Multi-implementation interoperability)
still passes, no capability assigned to v0.155.0 (Compile-fail state and lifetime tests) is claimed, and no critical or
high finding remains open.

`0.154.0 implementation stop reached. Run pentest for this exact commit.`

### v0.155.0 — Compile-fail state and lifetime tests

Status: planned

#### Goal

Deliver **Compile-fail state and lifetime tests** as the only primary capability in this stop. It builds
on v0.154.0 (Adversarial and stateful fuzz campaign) and must be independently trustworthy before v0.156.0 (Long-running soak and exhaustion campaign) begins.

#### Deliverables

- Implement and document Compile-fail state and lifetime tests in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Compile-fail state and lifetime tests.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Compile-fail state and lifetime tests contract is complete, its named evidence is reproducible, v0.154.0 (Adversarial and stateful fuzz campaign)
still passes, no capability assigned to v0.156.0 (Long-running soak and exhaustion campaign) is claimed, and no critical or
high finding remains open.

`0.155.0 implementation stop reached. Run pentest for this exact commit.`

### v0.156.0 — Long-running soak and exhaustion campaign

Status: planned

#### Goal

Deliver **Long-running soak and exhaustion campaign** as the only primary capability in this stop. It builds
on v0.155.0 (Compile-fail state and lifetime tests) and must be independently trustworthy before v0.157.0 (Role and API conformance audit and pentest) begins.

#### Deliverables

- Implement and document Long-running soak and exhaustion campaign in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Long-running soak and exhaustion campaign.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Long-running soak and exhaustion campaign contract is complete, its named evidence is reproducible, v0.155.0 (Compile-fail state and lifetime tests)
still passes, no capability assigned to v0.157.0 (Role and API conformance audit and pentest) is claimed, and no critical or
high finding remains open.

`0.156.0 implementation stop reached. Run pentest for this exact commit.`

### v0.157.0 — Role and API conformance audit and pentest

Status: planned

#### Goal

Deliver **Role and API conformance audit and pentest** as the only primary capability in this stop. It builds
on v0.156.0 (Long-running soak and exhaustion campaign) and must be independently trustworthy before v0.158.0 (Standard blocking-stream adapter) begins.

#### Deliverables

- Implement and document Role and API conformance audit and pentest in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Role APIs expose only validated messages and committed transitions; translation preserves semantics, ordering, cache metadata, half-close behavior, and explicit retry boundaries.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 3986, RFC 7239 where Via/forwarding behavior applies, RFC 8441, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Role and API conformance audit and pentest.
- Test role matrices, request correlation, reserialization across framing changes, authority consistency, hop stripping, cache-preservation metadata, retry classifications, tunnel half-closes, compile-fail misuse, interop, fuzzing, and soak behavior.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Role and API conformance audit and pentest contract is complete, its named evidence is reproducible, v0.156.0 (Long-running soak and exhaustion campaign)
still passes, no capability assigned to v0.158.0 (Standard blocking-stream adapter) is claimed, and no critical or
high finding remains open.

`0.157.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 5 — OS, Aesynx readiness, and 1.0 evidence

Phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.

### v0.158.0 — Standard blocking-stream adapter

Status: planned

#### Goal

Deliver **Standard blocking-stream adapter** as the only primary capability in this stop. It builds
on v0.157.0 (Role and API conformance audit and pentest) and must be independently trustworthy before v0.159.0 (Standard nonblocking-stream adapter) begins.

#### Deliverables

- Implement and document Standard blocking-stream adapter in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Standard blocking-stream adapter.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Standard blocking-stream adapter contract is complete, its named evidence is reproducible, v0.157.0 (Role and API conformance audit and pentest)
still passes, no capability assigned to v0.159.0 (Standard nonblocking-stream adapter) is claimed, and no critical or
high finding remains open.

`0.158.0 implementation stop reached. Run pentest for this exact commit.`

### v0.159.0 — Standard nonblocking-stream adapter

Status: planned

#### Goal

Deliver **Standard nonblocking-stream adapter** as the only primary capability in this stop. It builds
on v0.158.0 (Standard blocking-stream adapter) and must be independently trustworthy before v0.160.0 (Brynja TLS provider contract and admission review) begins.

#### Deliverables

- Implement and document Standard nonblocking-stream adapter in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Standard nonblocking-stream adapter.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Standard nonblocking-stream adapter contract is complete, its named evidence is reproducible, v0.158.0 (Standard blocking-stream adapter)
still passes, no capability assigned to v0.160.0 (Brynja TLS provider contract and admission review) is claimed, and no critical or
high finding remains open.

`0.159.0 implementation stop reached. Run pentest for this exact commit.`

### v0.160.0 — Brynja TLS provider contract and admission review

Status: planned

#### Goal

Deliver **Brynja TLS provider contract and admission review** as the only primary capability in this stop. It builds
on v0.159.0 (Standard nonblocking-stream adapter) and must be independently trustworthy before v0.161.0 (Separate vef-brynja adapter crate) begins.

#### Deliverables

- Implement and document Brynja TLS provider contract and admission review in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Brynja TLS provider contract and admission review.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Brynja TLS provider contract and admission review contract is complete, its named evidence is reproducible, v0.159.0 (Standard nonblocking-stream adapter)
still passes, no capability assigned to v0.161.0 (Separate vef-brynja adapter crate) is claimed, and no critical or
high finding remains open.

`0.160.0 implementation stop reached. Run pentest for this exact commit.`

### v0.161.0 — Separate vef-brynja adapter crate

Status: planned

#### Goal

Deliver **Separate vef-brynja adapter crate** as the only primary capability in this stop. It builds
on v0.160.0 (Brynja TLS provider contract and admission review) and must be independently trustworthy before v0.162.0 (Authenticated ALPN and HTTP/2 TLS prerequisites) begins.

#### Deliverables

- Implement and document Separate vef-brynja adapter crate in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Separate vef-brynja adapter crate.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Separate vef-brynja adapter crate contract is complete, its named evidence is reproducible, v0.160.0 (Brynja TLS provider contract and admission review)
still passes, no capability assigned to v0.162.0 (Authenticated ALPN and HTTP/2 TLS prerequisites) is claimed, and no critical or
high finding remains open.

`0.161.0 implementation stop reached. Run pentest for this exact commit.`

### v0.162.0 — Authenticated ALPN and HTTP/2 TLS prerequisites

Status: planned

#### Goal

Deliver **Authenticated ALPN and HTTP/2 TLS prerequisites** as the only primary capability in this stop. It builds
on v0.161.0 (Separate vef-brynja adapter crate) and must be independently trustworthy before v0.163.0 (TLS 1.3 early-data prohibition and close semantics) begins.

#### Deliverables

- Implement and document Authenticated ALPN and HTTP/2 TLS prerequisites in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Authenticated ALPN and HTTP/2 TLS prerequisites.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Authenticated ALPN and HTTP/2 TLS prerequisites contract is complete, its named evidence is reproducible, v0.161.0 (Separate vef-brynja adapter crate)
still passes, no capability assigned to v0.163.0 (TLS 1.3 early-data prohibition and close semantics) is claimed, and no critical or
high finding remains open.

`0.162.0 implementation stop reached. Run pentest for this exact commit.`

### v0.163.0 — TLS 1.3 early-data prohibition and close semantics

Status: planned

#### Goal

Deliver **TLS 1.3 early-data prohibition and close semantics** as the only primary capability in this stop. It builds
on v0.162.0 (Authenticated ALPN and HTTP/2 TLS prerequisites) and must be independently trustworthy before v0.164.0 (Aesynx fixed-memory capability profile) begins.

#### Deliverables

- Implement and document TLS 1.3 early-data prohibition and close semantics in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for TLS 1.3 early-data prohibition and close semantics.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The TLS 1.3 early-data prohibition and close semantics contract is complete, its named evidence is reproducible, v0.162.0 (Authenticated ALPN and HTTP/2 TLS prerequisites)
still passes, no capability assigned to v0.164.0 (Aesynx fixed-memory capability profile) is claimed, and no critical or
high finding remains open.

`0.163.0 implementation stop reached. Run pentest for this exact commit.`

### v0.164.0 — Aesynx fixed-memory capability profile

Status: planned

#### Goal

Deliver **Aesynx fixed-memory capability profile** as the only primary capability in this stop. It builds
on v0.163.0 (TLS 1.3 early-data prohibition and close semantics) and must be independently trustworthy before v0.165.0 (Aesynx transport and readiness adapter) begins.

#### Deliverables

- Implement and document Aesynx fixed-memory capability profile in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Aesynx fixed-memory capability profile.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Aesynx fixed-memory capability profile contract is complete, its named evidence is reproducible, v0.163.0 (TLS 1.3 early-data prohibition and close semantics)
still passes, no capability assigned to v0.165.0 (Aesynx transport and readiness adapter) is claimed, and no critical or
high finding remains open.

`0.164.0 implementation stop reached. Run pentest for this exact commit.`

### v0.165.0 — Aesynx transport and readiness adapter

Status: planned

#### Goal

Deliver **Aesynx transport and readiness adapter** as the only primary capability in this stop. It builds
on v0.164.0 (Aesynx fixed-memory capability profile) and must be independently trustworthy before v0.166.0 (Aesynx timer and deadline adapter) begins.

#### Deliverables

- Implement and document Aesynx transport and readiness adapter in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Aesynx transport and readiness adapter.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Aesynx transport and readiness adapter contract is complete, its named evidence is reproducible, v0.164.0 (Aesynx fixed-memory capability profile)
still passes, no capability assigned to v0.166.0 (Aesynx timer and deadline adapter) is claimed, and no critical or
high finding remains open.

`0.165.0 implementation stop reached. Run pentest for this exact commit.`

### v0.166.0 — Aesynx timer and deadline adapter

Status: planned

#### Goal

Deliver **Aesynx timer and deadline adapter** as the only primary capability in this stop. It builds
on v0.165.0 (Aesynx transport and readiness adapter) and must be independently trustworthy before v0.167.0 (Aesynx kernel integration tests) begins.

#### Deliverables

- Implement and document Aesynx timer and deadline adapter in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Aesynx timer and deadline adapter.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Aesynx timer and deadline adapter contract is complete, its named evidence is reproducible, v0.165.0 (Aesynx transport and readiness adapter)
still passes, no capability assigned to v0.167.0 (Aesynx kernel integration tests) is claimed, and no critical or
high finding remains open.

`0.166.0 implementation stop reached. Run pentest for this exact commit.`

### v0.167.0 — Aesynx kernel integration tests

Status: planned

#### Goal

Deliver **Aesynx kernel integration tests** as the only primary capability in this stop. It builds
on v0.166.0 (Aesynx timer and deadline adapter) and must be independently trustworthy before v0.168.0 (32-bit target campaign) begins.

#### Deliverables

- Implement and document Aesynx kernel integration tests in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Aesynx kernel integration tests.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Aesynx kernel integration tests contract is complete, its named evidence is reproducible, v0.166.0 (Aesynx timer and deadline adapter)
still passes, no capability assigned to v0.168.0 (32-bit target campaign) is claimed, and no critical or
high finding remains open.

`0.167.0 implementation stop reached. Run pentest for this exact commit.`

### v0.168.0 — 32-bit target campaign

Status: planned

#### Goal

Deliver **32-bit target campaign** as the only primary capability in this stop. It builds
on v0.167.0 (Aesynx kernel integration tests) and must be independently trustworthy before v0.169.0 (Big-endian target campaign) begins.

#### Deliverables

- Implement and document 32-bit target campaign in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for 32-bit target campaign.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The 32-bit target campaign contract is complete, its named evidence is reproducible, v0.167.0 (Aesynx kernel integration tests)
still passes, no capability assigned to v0.169.0 (Big-endian target campaign) is claimed, and no critical or
high finding remains open.

`0.168.0 implementation stop reached. Run pentest for this exact commit.`

### v0.169.0 — Big-endian target campaign

Status: planned

#### Goal

Deliver **Big-endian target campaign** as the only primary capability in this stop. It builds
on v0.168.0 (32-bit target campaign) and must be independently trustworthy before v0.170.0 (Cross-architecture campaign) begins.

#### Deliverables

- Implement and document Big-endian target campaign in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Big-endian target campaign.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Big-endian target campaign contract is complete, its named evidence is reproducible, v0.168.0 (32-bit target campaign)
still passes, no capability assigned to v0.170.0 (Cross-architecture campaign) is claimed, and no critical or
high finding remains open.

`0.169.0 implementation stop reached. Run pentest for this exact commit.`

### v0.170.0 — Cross-architecture campaign

Status: planned

#### Goal

Deliver **Cross-architecture campaign** as the only primary capability in this stop. It builds
on v0.169.0 (Big-endian target campaign) and must be independently trustworthy before v0.171.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) begins.

#### Deliverables

- Implement and document Cross-architecture campaign in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Cross-architecture campaign.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Cross-architecture campaign contract is complete, its named evidence is reproducible, v0.169.0 (Big-endian target campaign)
still passes, no capability assigned to v0.171.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) is claimed, and no critical or
high finding remains open.

`0.170.0 implementation stop reached. Run pentest for this exact commit.`

### v0.171.0 — Linux, Windows, BSD, macOS, Android, and iOS matrix

Status: planned

#### Goal

Deliver **Linux, Windows, BSD, macOS, Android, and iOS matrix** as the only primary capability in this stop. It builds
on v0.170.0 (Cross-architecture campaign) and must be independently trustworthy before v0.172.0 (Kani shared-core proofs) begins.

#### Deliverables

- Implement and document Linux, Windows, BSD, macOS, Android, and iOS matrix in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Linux, Windows, BSD, macOS, Android, and iOS matrix.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Linux, Windows, BSD, macOS, Android, and iOS matrix contract is complete, its named evidence is reproducible, v0.170.0 (Cross-architecture campaign)
still passes, no capability assigned to v0.172.0 (Kani shared-core proofs) is claimed, and no critical or
high finding remains open.

`0.171.0 implementation stop reached. Run pentest for this exact commit.`

### v0.172.0 — Kani shared-core proofs

Status: planned

#### Goal

Deliver **Kani shared-core proofs** as the only primary capability in this stop. It builds
on v0.171.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) and must be independently trustworthy before v0.173.0 (Kani HTTP/1 proofs) begins.

#### Deliverables

- Implement and document Kani shared-core proofs in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Kani shared-core proofs.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Kani shared-core proofs contract is complete, its named evidence is reproducible, v0.171.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix)
still passes, no capability assigned to v0.173.0 (Kani HTTP/1 proofs) is claimed, and no critical or
high finding remains open.

`0.172.0 implementation stop reached. Run pentest for this exact commit.`

### v0.173.0 — Kani HTTP/1 proofs

Status: planned

#### Goal

Deliver **Kani HTTP/1 proofs** as the only primary capability in this stop. It builds
on v0.172.0 (Kani shared-core proofs) and must be independently trustworthy before v0.174.0 (Kani HPACK proofs) begins.

#### Deliverables

- Implement and document Kani HTTP/1 proofs in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Kani HTTP/1 proofs.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Kani HTTP/1 proofs contract is complete, its named evidence is reproducible, v0.172.0 (Kani shared-core proofs)
still passes, no capability assigned to v0.174.0 (Kani HPACK proofs) is claimed, and no critical or
high finding remains open.

`0.173.0 implementation stop reached. Run pentest for this exact commit.`

### v0.174.0 — Kani HPACK proofs

Status: planned

#### Goal

Deliver **Kani HPACK proofs** as the only primary capability in this stop. It builds
on v0.173.0 (Kani HTTP/1 proofs) and must be independently trustworthy before v0.175.0 (Kani HTTP/2 proofs) begins.

#### Deliverables

- Implement and document Kani HPACK proofs in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Kani HPACK proofs.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Kani HPACK proofs contract is complete, its named evidence is reproducible, v0.173.0 (Kani HTTP/1 proofs)
still passes, no capability assigned to v0.175.0 (Kani HTTP/2 proofs) is claimed, and no critical or
high finding remains open.

`0.174.0 implementation stop reached. Run pentest for this exact commit.`

### v0.175.0 — Kani HTTP/2 proofs

Status: planned

#### Goal

Deliver **Kani HTTP/2 proofs** as the only primary capability in this stop. It builds
on v0.174.0 (Kani HPACK proofs) and must be independently trustworthy before v0.176.0 (Stateful cargo-fuzz campaign) begins.

#### Deliverables

- Implement and document Kani HTTP/2 proofs in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Kani HTTP/2 proofs.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Kani HTTP/2 proofs contract is complete, its named evidence is reproducible, v0.174.0 (Kani HPACK proofs)
still passes, no capability assigned to v0.176.0 (Stateful cargo-fuzz campaign) is claimed, and no critical or
high finding remains open.

`0.175.0 implementation stop reached. Run pentest for this exact commit.`

### v0.176.0 — Stateful cargo-fuzz campaign

Status: planned

#### Goal

Deliver **Stateful cargo-fuzz campaign** as the only primary capability in this stop. It builds
on v0.175.0 (Kani HTTP/2 proofs) and must be independently trustworthy before v0.177.0 (Differential and interoperability campaign) begins.

#### Deliverables

- Implement and document Stateful cargo-fuzz campaign in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Stateful cargo-fuzz campaign.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Stateful cargo-fuzz campaign contract is complete, its named evidence is reproducible, v0.175.0 (Kani HTTP/2 proofs)
still passes, no capability assigned to v0.177.0 (Differential and interoperability campaign) is claimed, and no critical or
high finding remains open.

`0.176.0 implementation stop reached. Run pentest for this exact commit.`

### v0.177.0 — Differential and interoperability campaign

Status: planned

#### Goal

Deliver **Differential and interoperability campaign** as the only primary capability in this stop. It builds
on v0.176.0 (Stateful cargo-fuzz campaign) and must be independently trustworthy before v0.178.0 (Whole-project conformance audit and pentest) begins.

#### Deliverables

- Implement and document Differential and interoperability campaign in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Differential and interoperability campaign.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Differential and interoperability campaign contract is complete, its named evidence is reproducible, v0.176.0 (Stateful cargo-fuzz campaign)
still passes, no capability assigned to v0.178.0 (Whole-project conformance audit and pentest) is claimed, and no critical or
high finding remains open.

`0.177.0 implementation stop reached. Run pentest for this exact commit.`

### v0.178.0 — Whole-project conformance audit and pentest

Status: planned

#### Goal

Deliver **Whole-project conformance audit and pentest** as the only primary capability in this stop. It builds
on v0.177.0 (Differential and interoperability campaign) and must be independently trustworthy before v0.179.0 (Independent security audit) begins.

#### Deliverables

- Implement and document Whole-project conformance audit and pentest in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Whole-project conformance audit and pentest.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Whole-project conformance audit and pentest contract is complete, its named evidence is reproducible, v0.177.0 (Differential and interoperability campaign)
still passes, no capability assigned to v0.179.0 (Independent security audit) is claimed, and no critical or
high finding remains open.

`0.178.0 implementation stop reached. Run pentest for this exact commit.`

### v0.179.0 — Independent security audit

Status: planned

#### Goal

Deliver **Independent security audit** as the only primary capability in this stop. It builds
on v0.178.0 (Whole-project conformance audit and pentest) and must be independently trustworthy before v0.180.0 (Audit remediation and API freeze) begins.

#### Deliverables

- Implement and document Independent security audit in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Independent security audit.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Independent security audit contract is complete, its named evidence is reproducible, v0.178.0 (Whole-project conformance audit and pentest)
still passes, no capability assigned to v0.180.0 (Audit remediation and API freeze) is claimed, and no critical or
high finding remains open.

`0.179.0 implementation stop reached. Run pentest for this exact commit.`

### v0.180.0 — Audit remediation and API freeze

Status: planned

#### Goal

Deliver **Audit remediation and API freeze** as the only primary capability in this stop. It builds
on v0.179.0 (Independent security audit) and must be independently trustworthy before v0.181.0 (Documentation, packaging, SBOM, provenance, and RC readiness) begins.

#### Deliverables

- Implement and document Audit remediation and API freeze in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Audit remediation and API freeze.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Audit remediation and API freeze contract is complete, its named evidence is reproducible, v0.179.0 (Independent security audit)
still passes, no capability assigned to v0.181.0 (Documentation, packaging, SBOM, provenance, and RC readiness) is claimed, and no critical or
high finding remains open.

`0.180.0 implementation stop reached. Run pentest for this exact commit.`

### v0.181.0 — Documentation, packaging, SBOM, provenance, and RC readiness

Status: planned

#### Goal

Deliver **Documentation, packaging, SBOM, provenance, and RC readiness** as the only primary capability in this stop. It builds
on v0.180.0 (Audit remediation and API freeze) and must be independently trustworthy before the 1.0 release-candidate sequence begins.

#### Deliverables

- Implement and document Documentation, packaging, SBOM, provenance, and RC readiness in the crate or module that owns the
  capability; do not expose adjacent later-version behavior.
- Enforce the phase contract: Platform adapters cannot alter protocol validity; authenticated selection, deadlines, cancellation, EOF, storage, and release evidence remain explicit across every supported target.
- Update paragraph-addressable applicability, requirement, SHOULD-decision,
  deviation, and verified/held errata records for RFC 7301, RFC 8446, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define typed error scope, progress, capacity, cancellation, and state-commit
  behavior for every new public operation.
- Update the threat model, security controls, API documentation, release notes,
  traceability evidence, and any conformance corpus affected by this outcome.

#### Verification

- Add focused positive, negative, boundary, truncation, invalid-state,
  arbitrary-input no-panic, and regression tests specifically for Documentation, packaging, SBOM, provenance, and RC readiness.
- Run blocking and nonblocking adapter suites, authenticated-ALPN cases, early-data rejection, clean-versus-truncated EOF, fixed-memory Aesynx simulations, 32-bit and big-endian targets, Kani, fuzzing, interop, audit remediation, packaging, SBOM, and provenance gates.
- Prove failures do not publish partial application state, mutate unrelated
  connection state, exceed declared work/output budgets, or require allocation.
- Run the full Rust `1.90.0`–`1.97.1` matrix, `no_std` and target checks,
  documentation/package checks, dependency policy, audit, SBOM, CI, and CodeQL
  default-setup review.

#### Exit criteria

The Documentation, packaging, SBOM, provenance, and RC readiness contract is complete, its named evidence is reproducible, v0.180.0 (Audit remediation and API freeze)
still passes, no capability assigned to the 1.0 release-candidate sequence is claimed, and no critical or
high finding remains open.

`0.181.0 implementation stop reached. Run pentest for this exact commit.`

## 1.0 release candidates

### v1.0.0-rc.1

Status: planned

Goal: freeze the public API and expose the complete candidate to public
interoperability, security, usability, and documentation review.

Deliverables: API freeze, migration guidance, package dry runs, generated RFC
and errata coverage, published platform matrix, known limitations, SBOM,
provenance, and complete release evidence.

Verification: repeat every repository gate, full stateful fuzzing, independent
multi-implementation interoperability, full manual audit, and exact-commit
pentest.

Exit criteria: no new features are accepted and all candidate evidence is
reproducible. `1.0.0-rc.1 implementation stop reached. Run pentest for this exact commit.`

### v1.0.0-rc.2

Status: planned

Goal: remediate RC1 findings without expanding scope.

Deliverables: fixes, regression tests, final dependency/source review, final
RFC and errata coverage, final MSRV/target declarations, and refreshed evidence.

Verification: repeat every fuzz, pentest, conformance, interoperability,
portability, package, SBOM, and provenance gate.

Exit criteria: no unresolved critical/high findings and no unreviewed behavior
change. `1.0.0-rc.2 implementation stop reached. Run pentest for this exact commit.`

### v1.0.0

Status: planned

Goal: publish the first serious production-ready VEF HTTP crate.

Release only when every applicable MUST/MUST NOT is verified, every SHOULD
decision and errata disposition is documented, fixed caller-storage operation
works without an allocator, protocol cores are `no_std` and unsafe-free,
HTTP/0.9 is isolated and cannot activate accidentally, HTTP/1 has one framing
interpretation, HTTP/2 state transitions and flow control pass exhaustive
evidence, HPACK remains bounded, TLS early data is disabled, every declared role
is covered, platform matrices are published, independent-audit remediation is
verified, and HTTP/3 remains explicitly out of scope.
