# VEF Release Plan to 1.0

Status: planning document

This is the authoritative implementation sequence. VEF processes hostile
traffic, so each milestone has one primary capability and a dependency-correct
acceptance boundary that can be implemented, reviewed, tested, pentested, and
stopped independently. Split work into patch releases when its security
argument no longer fits one review pass.

## Release principles

Every release requires applicable RFC/errata evidence, explicit applicability,
bounded resource behavior against the active profile, focused positive and
negative tests, relevant fragmentation/cancellation/capacity coverage,
documentation, release notes, portability, dependency-policy proof, SBOM,
full-SHA CI pins, CodeQL default-setup review, and exact-commit pentest. Tests
cover the new outcome and earlier behavior, never future features.

Protocol and I/O-contract crates remain `no_std`, safe Rust, and free of
third-party Rust crates. Tool-only fuzzers, model checkers, and interop peers do
not enter the production dependency graph.

## Rules binding every milestone

- Valid peer input exceeding policy, insufficient caller storage, temporary
  output backpressure, and exhausted mandatory-control capacity are distinct
  from peer protocol violations and receive role-specific dispositions.
- Success makes non-zero observable progress; borrowed events require
  acknowledgement before backing storage is recycled.
- Resource ceilings are defined in Phase 1 and enforced as each parser, HPACK
  operation, stream transition, scheduler action, and adapter lands.
- Parsing and semantic validation withhold application publication until the
  relevant barrier passes. Translation emits no destination bytes until its
  complete head/framing decision validates.
- HPACK encoder state follows committed output bytes; decoder compression state
  is never rolled back for a later semantic stream error.
- SETTINGS syntax/value storage is early, but state integration waits for the
  HPACK, stream, flow-control, admission, or scheduler component it mutates.
- Every source file remains below 500 lines.
- Fuzz/model harnesses begin with hostile surfaces; final campaigns replay and
  expand them rather than creating them for the first time.

## Pentest flow

At each implementation stop, do not tag. Pentest the exact commit, remediate
with regression tests, repeat all gates, then add the permanent passing report
as the only file in the direct child of the reviewed commit. Critical/high
findings block release. Phase exits add manual review, stateful fuzzing, corpus
minimization, multi-peer interop, exhaustion assessment, and conformance review.

## Phase 1 — Foundation and shared semantics

Phase contract: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.

### v0.1.0 — Workspace, crate boundaries, licenses, security policy, and release evidence

Status: foundation implementation in progress

#### Goal

Deliver **Workspace, crate boundaries, licenses, security policy, and release evidence** as the sole primary capability in this stop. It builds
on the repository foundation and must be independently trustworthy before v0.2.0 (Core module skeleton and authority boundaries) begins.

#### Deliverables

- Acceptance contract: Define the Workspace, crate boundaries, licenses, security policy, and release evidence state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Workspace, crate boundaries, licenses, security policy, and release evidence and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Workspace, crate boundaries, licenses, security policy, and release evidence contract and all previously implemented relevant behavior have
reproducible evidence; the repository foundation still passes; no behavior assigned to v0.2.0 (Core module skeleton and authority boundaries) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.1.0 implementation stop reached. Run pentest for this exact commit.`

### v0.2.0 — Core module skeleton and authority boundaries

Status: planned

#### Goal

Deliver **Core module skeleton and authority boundaries** as the sole primary capability in this stop. It builds
on v0.1.0 (Workspace, crate boundaries, licenses, security policy, and release evidence) and must be independently trustworthy before v0.3.0 (Checked byte cursor with no unchecked indexing) begins.

#### Deliverables

- Acceptance contract: Define the Core module skeleton and authority boundaries state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Core module skeleton and authority boundaries and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Core module skeleton and authority boundaries contract and all previously implemented relevant behavior have
reproducible evidence; v0.1.0 (Workspace, crate boundaries, licenses, security policy, and release evidence) still passes; no behavior assigned to v0.3.0 (Checked byte cursor with no unchecked indexing) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.2.0 implementation stop reached. Run pentest for this exact commit.`

### v0.3.0 — Checked byte cursor with no unchecked indexing

Status: planned

#### Goal

Deliver **Checked byte cursor with no unchecked indexing** as the sole primary capability in this stop. It builds
on v0.2.0 (Core module skeleton and authority boundaries) and must be independently trustworthy before v0.4.0 (Non-zero parser progress and explicit blocked states) begins.

#### Deliverables

- Acceptance contract: Define the Checked byte cursor with no unchecked indexing state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Checked byte cursor with no unchecked indexing and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked byte cursor with no unchecked indexing contract and all previously implemented relevant behavior have
reproducible evidence; v0.2.0 (Core module skeleton and authority boundaries) still passes; no behavior assigned to v0.4.0 (Non-zero parser progress and explicit blocked states) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.3.0 implementation stop reached. Run pentest for this exact commit.`

### v0.4.0 — Non-zero parser progress and explicit blocked states

Status: planned

#### Goal

Deliver **Non-zero parser progress and explicit blocked states** as the sole primary capability in this stop. It builds
on v0.3.0 (Checked byte cursor with no unchecked indexing) and must be independently trustworthy before v0.5.0 (Checked protocol-size domains) begins.

#### Deliverables

- Acceptance contract: Represent successful byte advancement with a non-zero type or checked constructor and distinguish input, output, event, transition, NeedInput, NeedOutput, and CapacityExceeded outcomes.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Non-zero parser progress and explicit blocked states and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Non-zero parser progress and explicit blocked states contract and all previously implemented relevant behavior have
reproducible evidence; v0.3.0 (Checked byte cursor with no unchecked indexing) still passes; no behavior assigned to v0.5.0 (Checked protocol-size domains) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.4.0 implementation stop reached. Run pentest for this exact commit.`

### v0.5.0 — Checked protocol-size domains

Status: planned

#### Goal

Deliver **Checked protocol-size domains** as the sole primary capability in this stop. It builds
on v0.4.0 (Non-zero parser progress and explicit blocked states) and must be independently trustworthy before v0.6.0 (Decode, work, transition, and response budgets) begins.

#### Deliverables

- Acceptance contract: Define the Checked protocol-size domains state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Checked protocol-size domains and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked protocol-size domains contract and all previously implemented relevant behavior have
reproducible evidence; v0.4.0 (Non-zero parser progress and explicit blocked states) still passes; no behavior assigned to v0.6.0 (Decode, work, transition, and response budgets) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.5.0 implementation stop reached. Run pentest for this exact commit.`

### v0.6.0 — Decode, work, transition, and response budgets

Status: planned

#### Goal

Deliver **Decode, work, transition, and response budgets** as the sole primary capability in this stop. It builds
on v0.5.0 (Checked protocol-size domains) and must be independently trustworthy before v0.7.0 (Initial deterministic resource profiles and measurement hooks) begins.

#### Deliverables

- Acceptance contract: Define the Decode, work, transition, and response budgets state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Decode, work, transition, and response budgets and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Decode, work, transition, and response budgets contract and all previously implemented relevant behavior have
reproducible evidence; v0.5.0 (Checked protocol-size domains) still passes; no behavior assigned to v0.7.0 (Initial deterministic resource profiles and measurement hooks) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.6.0 implementation stop reached. Run pentest for this exact commit.`

### v0.7.0 — Initial deterministic resource profiles and measurement hooks

Status: planned

#### Goal

Deliver **Initial deterministic resource profiles and measurement hooks** as the sole primary capability in this stop. It builds
on v0.6.0 (Decode, work, transition, and response budgets) and must be independently trustworthy before v0.8.0 (Caller-owned arenas and fixed-capacity stores) begins.

#### Deliverables

- Acceptance contract: Define numerical or target-relative stack, code-size, work-per-byte/frame, output-amplification, one-byte-fragmentation, lookup-complexity, and scheduler-fairness ceilings plus reproducible measurement hooks before parser layouts land.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Initial deterministic resource profiles and measurement hooks contract and all previously implemented relevant behavior have
reproducible evidence; v0.6.0 (Decode, work, transition, and response budgets) still passes; no behavior assigned to v0.8.0 (Caller-owned arenas and fixed-capacity stores) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.7.0 implementation stop reached. Run pentest for this exact commit.`

### v0.8.0 — Caller-owned arenas and fixed-capacity stores

Status: planned

#### Goal

Deliver **Caller-owned arenas and fixed-capacity stores** as the sole primary capability in this stop. It builds
on v0.7.0 (Initial deterministic resource profiles and measurement hooks) and must be independently trustworthy before v0.9.0 (Structured errors and error-scope taxonomy) begins.

#### Deliverables

- Acceptance contract: Define fixed stores, borrowed views, generation-safe recycling, explicit capacity failures, and no hidden growth before any complete protocol parser.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Caller-owned arenas and fixed-capacity stores and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Caller-owned arenas and fixed-capacity stores contract and all previously implemented relevant behavior have
reproducible evidence; v0.7.0 (Initial deterministic resource profiles and measurement hooks) still passes; no behavior assigned to v0.9.0 (Structured errors and error-scope taxonomy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.8.0 implementation stop reached. Run pentest for this exact commit.`

### v0.9.0 — Structured errors and error-scope taxonomy

Status: planned

#### Goal

Deliver **Structured errors and error-scope taxonomy** as the sole primary capability in this stop. It builds
on v0.8.0 (Caller-owned arenas and fixed-capacity stores) and must be independently trustworthy before v0.10.0 (Capacity exhaustion and protocol-violation disposition taxonomy) begins.

#### Deliverables

- Acceptance contract: Separate syntax, policy, capacity, transport, connection, stream, and application errors so adapters cannot mistake a fatal condition for a recoverable one.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Structured errors and error-scope taxonomy and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured errors and error-scope taxonomy contract and all previously implemented relevant behavior have
reproducible evidence; v0.8.0 (Caller-owned arenas and fixed-capacity stores) still passes; no behavior assigned to v0.10.0 (Capacity exhaustion and protocol-violation disposition taxonomy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.9.0 implementation stop reached. Run pentest for this exact commit.`

### v0.10.0 — Capacity exhaustion and protocol-violation disposition taxonomy

Status: planned

#### Goal

Deliver **Capacity exhaustion and protocol-violation disposition taxonomy** as the sole primary capability in this stop. It builds
on v0.9.0 (Structured errors and error-scope taxonomy) and must be independently trustworthy before v0.11.0 (Case-sensitive extension-capable Method) begins.

#### Deliverables

- Acceptance contract: Distinguish invalid input, valid policy excess, insufficient caller storage, temporary output backpressure, and exhausted mandatory-control capacity; map each role to explicit local error, reject, close, or retry behavior without converting local capacity into peer PROTOCOL_ERROR.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Capacity exhaustion and protocol-violation disposition taxonomy and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Capacity exhaustion and protocol-violation disposition taxonomy contract and all previously implemented relevant behavior have
reproducible evidence; v0.9.0 (Structured errors and error-scope taxonomy) still passes; no behavior assigned to v0.11.0 (Case-sensitive extension-capable Method) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.10.0 implementation stop reached. Run pentest for this exact commit.`

### v0.11.0 — Case-sensitive extension-capable Method

Status: planned

#### Goal

Deliver **Case-sensitive extension-capable Method** as the sole primary capability in this stop. It builds
on v0.10.0 (Capacity exhaustion and protocol-violation disposition taxonomy) and must be independently trustworthy before v0.12.0 (Validated StatusCode with unknown-code preservation) begins.

#### Deliverables

- Acceptance contract: Define the Case-sensitive extension-capable Method state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Case-sensitive extension-capable Method and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Case-sensitive extension-capable Method contract and all previously implemented relevant behavior have
reproducible evidence; v0.10.0 (Capacity exhaustion and protocol-violation disposition taxonomy) still passes; no behavior assigned to v0.12.0 (Validated StatusCode with unknown-code preservation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.11.0 implementation stop reached. Run pentest for this exact commit.`

### v0.12.0 — Validated StatusCode with unknown-code preservation

Status: planned

#### Goal

Deliver **Validated StatusCode with unknown-code preservation** as the sole primary capability in this stop. It builds
on v0.11.0 (Case-sensitive extension-capable Method) and must be independently trustworthy before v0.13.0 (HTTP version and wire-version representation) begins.

#### Deliverables

- Acceptance contract: Define the Validated StatusCode with unknown-code preservation state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Validated StatusCode with unknown-code preservation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Validated StatusCode with unknown-code preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.11.0 (Case-sensitive extension-capable Method) still passes; no behavior assigned to v0.13.0 (HTTP version and wire-version representation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.12.0 implementation stop reached. Run pentest for this exact commit.`

### v0.13.0 — HTTP version and wire-version representation

Status: planned

#### Goal

Deliver **HTTP version and wire-version representation** as the sole primary capability in this stop. It builds
on v0.12.0 (Validated StatusCode with unknown-code preservation) and must be independently trustworthy before v0.14.0 (Case-insensitive validated FieldName) begins.

#### Deliverables

- Acceptance contract: Define the HTTP version and wire-version representation state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test HTTP version and wire-version representation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP version and wire-version representation contract and all previously implemented relevant behavior have
reproducible evidence; v0.12.0 (Validated StatusCode with unknown-code preservation) still passes; no behavior assigned to v0.14.0 (Case-insensitive validated FieldName) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.13.0 implementation stop reached. Run pentest for this exact commit.`

### v0.14.0 — Case-insensitive validated FieldName

Status: planned

#### Goal

Deliver **Case-insensitive validated FieldName** as the sole primary capability in this stop. It builds
on v0.13.0 (HTTP version and wire-version representation) and must be independently trustworthy before v0.15.0 (Byte-oriented FieldValue with raw and semantic views) begins.

#### Deliverables

- Acceptance contract: Define the Case-insensitive validated FieldName state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Case-insensitive validated FieldName and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Case-insensitive validated FieldName contract and all previously implemented relevant behavior have
reproducible evidence; v0.13.0 (HTTP version and wire-version representation) still passes; no behavior assigned to v0.15.0 (Byte-oriented FieldValue with raw and semantic views) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.14.0 implementation stop reached. Run pentest for this exact commit.`

### v0.15.0 — Byte-oriented FieldValue with raw and semantic views

Status: planned

#### Goal

Deliver **Byte-oriented FieldValue with raw and semantic views** as the sole primary capability in this stop. It builds
on v0.14.0 (Case-insensitive validated FieldName) and must be independently trustworthy before v0.16.0 (Ordered FieldLine and FieldSection storage) begins.

#### Deliverables

- Acceptance contract: Define the Byte-oriented FieldValue with raw and semantic views state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Byte-oriented FieldValue with raw and semantic views and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Byte-oriented FieldValue with raw and semantic views contract and all previously implemented relevant behavior have
reproducible evidence; v0.14.0 (Case-insensitive validated FieldName) still passes; no behavior assigned to v0.16.0 (Ordered FieldLine and FieldSection storage) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.15.0 implementation stop reached. Run pentest for this exact commit.`

### v0.16.0 — Ordered FieldLine and FieldSection storage

Status: planned

#### Goal

Deliver **Ordered FieldLine and FieldSection storage** as the sole primary capability in this stop. It builds
on v0.15.0 (Byte-oriented FieldValue with raw and semantic views) and must be independently trustworthy before v0.17.0 (Request-target, URI, and authority types) begins.

#### Deliverables

- Acceptance contract: Define the Ordered FieldLine and FieldSection storage state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Ordered FieldLine and FieldSection storage and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Ordered FieldLine and FieldSection storage contract and all previously implemented relevant behavior have
reproducible evidence; v0.15.0 (Byte-oriented FieldValue with raw and semantic views) still passes; no behavior assigned to v0.17.0 (Request-target, URI, and authority types) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.16.0 implementation stop reached. Run pentest for this exact commit.`

### v0.17.0 — Request-target, URI, and authority types

Status: planned

#### Goal

Deliver **Request-target, URI, and authority types** as the sole primary capability in this stop. It builds
on v0.16.0 (Ordered FieldLine and FieldSection storage) and must be independently trustworthy before v0.18.0 (Request and response control-data types) begins.

#### Deliverables

- Acceptance contract: Define the Request-target, URI, and authority types state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Request-target, URI, and authority types and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Request-target, URI, and authority types contract and all previously implemented relevant behavior have
reproducible evidence; v0.16.0 (Ordered FieldLine and FieldSection storage) still passes; no behavior assigned to v0.18.0 (Request and response control-data types) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.17.0 implementation stop reached. Run pentest for this exact commit.`

### v0.18.0 — Request and response control-data types

Status: planned

#### Goal

Deliver **Request and response control-data types** as the sole primary capability in this stop. It builds
on v0.17.0 (Request-target, URI, and authority types) and must be independently trustworthy before v0.19.0 (Role, profile, and policy types) begins.

#### Deliverables

- Acceptance contract: Define the Request and response control-data types state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Request and response control-data types and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Request and response control-data types contract and all previously implemented relevant behavior have
reproducible evidence; v0.17.0 (Request-target, URI, and authority types) still passes; no behavior assigned to v0.19.0 (Role, profile, and policy types) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.18.0 implementation stop reached. Run pentest for this exact commit.`

### v0.19.0 — Role, profile, and policy types

Status: planned

#### Goal

Deliver **Role, profile, and policy types** as the sole primary capability in this stop. It builds
on v0.18.0 (Request and response control-data types) and must be independently trustworthy before v0.20.0 (Minimal synchronous I/O contracts) begins.

#### Deliverables

- Acceptance contract: Define the Role, profile, and policy types state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Role, profile, and policy types and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Role, profile, and policy types contract and all previously implemented relevant behavior have
reproducible evidence; v0.18.0 (Request and response control-data types) still passes; no behavior assigned to v0.20.0 (Minimal synchronous I/O contracts) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.19.0 implementation stop reached. Run pentest for this exact commit.`

### v0.20.0 — Minimal synchronous I/O contracts

Status: planned

#### Goal

Deliver **Minimal synchronous I/O contracts** as the sole primary capability in this stop. It builds
on v0.19.0 (Role, profile, and policy types) and must be independently trustworthy before v0.21.0 (Runtime-neutral readiness and poll contracts) begins.

#### Deliverables

- Acceptance contract: Define short reads/writes, zero-length calls, clean versus truncated EOF, temporary starvation, scalar fallback, alignment requirements, non-reentrancy, and optional vectored/scatter-gather progress without owning sockets.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Minimal synchronous I/O contracts and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Minimal synchronous I/O contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.19.0 (Role, profile, and policy types) still passes; no behavior assigned to v0.21.0 (Runtime-neutral readiness and poll contracts) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.20.0 implementation stop reached. Run pentest for this exact commit.`

### v0.21.0 — Runtime-neutral readiness and poll contracts

Status: planned

#### Goal

Deliver **Runtime-neutral readiness and poll contracts** as the sole primary capability in this stop. It builds
on v0.20.0 (Minimal synchronous I/O contracts) and must be independently trustworthy before v0.22.0 (Injected monotonic clock and deadline contracts) begins.

#### Deliverables

- Acceptance contract: Define WouldBlock, spurious readiness, edge/level triggering, wake coalescing, interest changes, cancellation races, and the requirement that readiness never implies byte progress.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Runtime-neutral readiness and poll contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.20.0 (Minimal synchronous I/O contracts) still passes; no behavior assigned to v0.22.0 (Injected monotonic clock and deadline contracts) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.21.0 implementation stop reached. Run pentest for this exact commit.`

### v0.22.0 — Injected monotonic clock and deadline contracts

Status: planned

#### Goal

Deliver **Injected monotonic clock and deadline contracts** as the sole primary capability in this stop. It builds
on v0.21.0 (Runtime-neutral readiness and poll contracts) and must be independently trustworthy before v0.23.0 (Cancellation, close, and bounded-backpressure contracts) begins.

#### Deliverables

- Acceptance contract: Use caller-supplied monotonic instants with checked deadline arithmetic, wrap handling, expiration ordering, no wall-clock assumptions, and deterministic timeout tests.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Injected monotonic clock and deadline contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.21.0 (Runtime-neutral readiness and poll contracts) still passes; no behavior assigned to v0.23.0 (Cancellation, close, and bounded-backpressure contracts) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.22.0 implementation stop reached. Run pentest for this exact commit.`

### v0.23.0 — Cancellation, close, and bounded-backpressure contracts

Status: planned

#### Goal

Deliver **Cancellation, close, and bounded-backpressure contracts** as the sole primary capability in this stop. It builds
on v0.22.0 (Injected monotonic clock and deadline contracts) and must be independently trustworthy before v0.24.0 (Deterministic fake transport and driver harness) begins.

#### Deliverables

- Acceptance contract: Define the Cancellation, close, and bounded-backpressure contracts state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Cancellation, close, and bounded-backpressure contracts and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Cancellation, close, and bounded-backpressure contracts contract and all previously implemented relevant behavior have
reproducible evidence; v0.22.0 (Injected monotonic clock and deadline contracts) still passes; no behavior assigned to v0.24.0 (Deterministic fake transport and driver harness) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.23.0 implementation stop reached. Run pentest for this exact commit.`

### v0.24.0 — Deterministic fake transport and driver harness

Status: planned

#### Goal

Deliver **Deterministic fake transport and driver harness** as the sole primary capability in this stop. It builds
on v0.23.0 (Cancellation, close, and bounded-backpressure contracts) and must be independently trustworthy before v0.25.0 (Engine event, command, acknowledgement, and publication contract) begins.

#### Deliverables

- Acceptance contract: Define the Deterministic fake transport and driver harness state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Deterministic fake transport and driver harness and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Deterministic fake transport and driver harness contract and all previously implemented relevant behavior have
reproducible evidence; v0.23.0 (Cancellation, close, and bounded-backpressure contracts) still passes; no behavior assigned to v0.25.0 (Engine event, command, acknowledgement, and publication contract) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.24.0 implementation stop reached. Run pentest for this exact commit.`

### v0.25.0 — Engine event, command, acknowledgement, and publication contract

Status: planned

#### Goal

Deliver **Engine event, command, acknowledgement, and publication contract** as the sole primary capability in this stop. It builds
on v0.24.0 (Deterministic fake transport and driver harness) and must be independently trustworthy before v0.26.0 (Requirement, applicability, and errata evidence system) begins.

#### Deliverables

- Acceptance contract: Choose the outstanding-event model; define acknowledgements, command acceptance, reentrancy prohibition, input/output ownership, cancellation aftermath, publication barriers, and capacity reserved for mandatory responses.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Engine event, command, acknowledgement, and publication contract and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Engine event, command, acknowledgement, and publication contract contract and all previously implemented relevant behavior have
reproducible evidence; v0.24.0 (Deterministic fake transport and driver harness) still passes; no behavior assigned to v0.26.0 (Requirement, applicability, and errata evidence system) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.25.0 implementation stop reached. Run pentest for this exact commit.`

### v0.26.0 — Requirement, applicability, and errata evidence system

Status: planned

#### Goal

Deliver **Requirement, applicability, and errata evidence system** as the sole primary capability in this stop. It builds
on v0.25.0 (Engine event, command, acknowledgement, and publication contract) and must be independently trustworthy before v0.27.0 (Foundation Kani campaign, audit, and pentest) begins.

#### Deliverables

- Acceptance contract: Define the Requirement, applicability, and errata evidence system state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Requirement, applicability, and errata evidence system and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Requirement, applicability, and errata evidence system contract and all previously implemented relevant behavior have
reproducible evidence; v0.25.0 (Engine event, command, acknowledgement, and publication contract) still passes; no behavior assigned to v0.27.0 (Foundation Kani campaign, audit, and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.26.0 implementation stop reached. Run pentest for this exact commit.`

### v0.27.0 — Foundation Kani campaign, audit, and pentest

Status: planned

#### Goal

Deliver **Foundation Kani campaign, audit, and pentest** as the sole primary capability in this stop. It builds
on v0.26.0 (Requirement, applicability, and errata evidence system) and must be independently trustworthy before v0.28.0 (HTTP/1 role and parser profiles) begins.

#### Deliverables

- Acceptance contract: Define the Foundation Kani campaign, audit, and pentest state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 2119, RFC 8174, RFC 3986, RFC 7301, RFC 8446, RFC 9110, RFC 9111, RFC 9112, RFC 9113, RFC 9298, RFC 9931, and applicable verified or held errata.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Foundation Kani campaign, audit, and pentest and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Foundation Kani campaign, audit, and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.26.0 (Requirement, applicability, and errata evidence system) still passes; no behavior assigned to v0.28.0 (HTTP/1 role and parser profiles) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.27.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 2 — HTTP/1 and isolated HTTP/0.9

Phase contract: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.

### v0.28.0 — HTTP/1 role and parser profiles

Status: planned

#### Goal

Deliver **HTTP/1 role and parser profiles** as the sole primary capability in this stop. It builds
on v0.27.0 (Foundation Kani campaign, audit, and pentest) and must be independently trustworthy before v0.29.0 (Incremental HTTP/1 request-line parser) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/1 role and parser profiles state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 role and parser profiles contract and all previously implemented relevant behavior have
reproducible evidence; v0.27.0 (Foundation Kani campaign, audit, and pentest) still passes; no behavior assigned to v0.29.0 (Incremental HTTP/1 request-line parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.28.0 implementation stop reached. Run pentest for this exact commit.`

### v0.29.0 — Incremental HTTP/1 request-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 request-line parser** as the sole primary capability in this stop. It builds
on v0.28.0 (HTTP/1 role and parser profiles) and must be independently trustworthy before v0.30.0 (Incremental HTTP/1 status-line parser) begins.

#### Deliverables

- Acceptance contract: Define the Incremental HTTP/1 request-line parser state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental HTTP/1 request-line parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.28.0 (HTTP/1 role and parser profiles) still passes; no behavior assigned to v0.30.0 (Incremental HTTP/1 status-line parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.29.0 implementation stop reached. Run pentest for this exact commit.`

### v0.30.0 — Incremental HTTP/1 status-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 status-line parser** as the sole primary capability in this stop. It builds
on v0.29.0 (Incremental HTTP/1 request-line parser) and must be independently trustworthy before v0.31.0 (Every-byte fragmentation support) begins.

#### Deliverables

- Acceptance contract: Define the Incremental HTTP/1 status-line parser state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental HTTP/1 status-line parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.29.0 (Incremental HTTP/1 request-line parser) still passes; no behavior assigned to v0.31.0 (Every-byte fragmentation support) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.30.0 implementation stop reached. Run pentest for this exact commit.`

### v0.31.0 — Every-byte fragmentation support

Status: planned

#### Goal

Deliver **Every-byte fragmentation support** as the sole primary capability in this stop. It builds
on v0.30.0 (Incremental HTTP/1 status-line parser) and must be independently trustworthy before v0.32.0 (Strict CRLF and separately named LF compatibility) begins.

#### Deliverables

- Acceptance contract: Define the Every-byte fragmentation support state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Every-byte fragmentation support and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Every-byte fragmentation support contract and all previously implemented relevant behavior have
reproducible evidence; v0.30.0 (Incremental HTTP/1 status-line parser) still passes; no behavior assigned to v0.32.0 (Strict CRLF and separately named LF compatibility) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.31.0 implementation stop reached. Run pentest for this exact commit.`

### v0.32.0 — Strict CRLF and separately named LF compatibility

Status: planned

#### Goal

Deliver **Strict CRLF and separately named LF compatibility** as the sole primary capability in this stop. It builds
on v0.31.0 (Every-byte fragmentation support) and must be independently trustworthy before v0.33.0 (Incremental HTTP/1 field-line parser) begins.

#### Deliverables

- Acceptance contract: Define the Strict CRLF and separately named LF compatibility state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Strict CRLF and separately named LF compatibility and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Strict CRLF and separately named LF compatibility contract and all previously implemented relevant behavior have
reproducible evidence; v0.31.0 (Every-byte fragmentation support) still passes; no behavior assigned to v0.33.0 (Incremental HTTP/1 field-line parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.32.0 implementation stop reached. Run pentest for this exact commit.`

### v0.33.0 — Incremental HTTP/1 field-line parser

Status: planned

#### Goal

Deliver **Incremental HTTP/1 field-line parser** as the sole primary capability in this stop. It builds
on v0.32.0 (Strict CRLF and separately named LF compatibility) and must be independently trustworthy before v0.34.0 (Explicit OWS handling with raw-value preservation) begins.

#### Deliverables

- Acceptance contract: Define the Incremental HTTP/1 field-line parser state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental HTTP/1 field-line parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.32.0 (Strict CRLF and separately named LF compatibility) still passes; no behavior assigned to v0.34.0 (Explicit OWS handling with raw-value preservation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.33.0 implementation stop reached. Run pentest for this exact commit.`

### v0.34.0 — Explicit OWS handling with raw-value preservation

Status: planned

#### Goal

Deliver **Explicit OWS handling with raw-value preservation** as the sole primary capability in this stop. It builds
on v0.33.0 (Incremental HTTP/1 field-line parser) and must be independently trustworthy before v0.35.0 (Injection-proof HTTP/1 head serialization) begins.

#### Deliverables

- Acceptance contract: Define the Explicit OWS handling with raw-value preservation state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit OWS handling with raw-value preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.33.0 (Incremental HTTP/1 field-line parser) still passes; no behavior assigned to v0.35.0 (Injection-proof HTTP/1 head serialization) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.34.0 implementation stop reached. Run pentest for this exact commit.`

### v0.35.0 — Injection-proof HTTP/1 head serialization

Status: planned

#### Goal

Deliver **Injection-proof HTTP/1 head serialization** as the sole primary capability in this stop. It builds
on v0.34.0 (Explicit OWS handling with raw-value preservation) and must be independently trustworthy before v0.36.0 (Role-specific obs-fold and invalid-field disposition) begins.

#### Deliverables

- Acceptance contract: Define the Injection-proof HTTP/1 head serialization state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Injection-proof HTTP/1 head serialization contract and all previously implemented relevant behavior have
reproducible evidence; v0.34.0 (Explicit OWS handling with raw-value preservation) still passes; no behavior assigned to v0.36.0 (Role-specific obs-fold and invalid-field disposition) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.35.0 implementation stop reached. Run pentest for this exact commit.`

### v0.36.0 — Role-specific obs-fold and invalid-field disposition

Status: planned

#### Goal

Deliver **Role-specific obs-fold and invalid-field disposition** as the sole primary capability in this stop. It builds
on v0.35.0 (Injection-proof HTTP/1 head serialization) and must be independently trustworthy before v0.37.0 (Field count, line, and section caps) begins.

#### Deliverables

- Acceptance contract: Implement the RFC 9112 role matrix for server requests, proxy/gateway responses, and user-agent responses rather than one blanket rejection rule.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Role-specific obs-fold and invalid-field disposition contract and all previously implemented relevant behavior have
reproducible evidence; v0.35.0 (Injection-proof HTTP/1 head serialization) still passes; no behavior assigned to v0.37.0 (Field count, line, and section caps) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.36.0 implementation stop reached. Run pentest for this exact commit.`

### v0.37.0 — Field count, line, and section caps

Status: planned

#### Goal

Deliver **Field count, line, and section caps** as the sole primary capability in this stop. It builds
on v0.36.0 (Role-specific obs-fold and invalid-field disposition) and must be independently trustworthy before v0.38.0 (Typed HTTP/1 protocol-error response and close actions) begins.

#### Deliverables

- Acceptance contract: Define the Field count, line, and section caps state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Field count, line, and section caps and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Field count, line, and section caps contract and all previously implemented relevant behavior have
reproducible evidence; v0.36.0 (Role-specific obs-fold and invalid-field disposition) still passes; no behavior assigned to v0.38.0 (Typed HTTP/1 protocol-error response and close actions) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.37.0 implementation stop reached. Run pentest for this exact commit.`

### v0.38.0 — Typed HTTP/1 protocol-error response and close actions

Status: planned

#### Goal

Deliver **Typed HTTP/1 protocol-error response and close actions** as the sole primary capability in this stop. It builds
on v0.37.0 (Field count, line, and section caps) and must be independently trustworthy before v0.39.0 (HTTP/1.1 Host validation and duplicate rejection) begins.

#### Deliverables

- Acceptance contract: Map failures to mandatory typed actions such as RejectAndClose(400/414/431), BadGatewayAndCloseUpstream, DiscardResponseAndClose, ConnectionError, or StreamError without unsafe continuation.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Typed HTTP/1 protocol-error response and close actions contract and all previously implemented relevant behavior have
reproducible evidence; v0.37.0 (Field count, line, and section caps) still passes; no behavior assigned to v0.39.0 (HTTP/1.1 Host validation and duplicate rejection) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.38.0 implementation stop reached. Run pentest for this exact commit.`

### v0.39.0 — HTTP/1.1 Host validation and duplicate rejection

Status: planned

#### Goal

Deliver **HTTP/1.1 Host validation and duplicate rejection** as the sole primary capability in this stop. It builds
on v0.38.0 (Typed HTTP/1 protocol-error response and close actions) and must be independently trustworthy before v0.40.0 (Method and request-target-form coherence) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/1.1 Host validation and duplicate rejection state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1.1 Host validation and duplicate rejection contract and all previously implemented relevant behavior have
reproducible evidence; v0.38.0 (Typed HTTP/1 protocol-error response and close actions) still passes; no behavior assigned to v0.40.0 (Method and request-target-form coherence) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.39.0 implementation stop reached. Run pentest for this exact commit.`

### v0.40.0 — Method and request-target-form coherence

Status: planned

#### Goal

Deliver **Method and request-target-form coherence** as the sole primary capability in this stop. It builds
on v0.39.0 (HTTP/1.1 Host validation and duplicate rejection) and must be independently trustworthy before v0.41.0 (Checked Content-Length grammar) begins.

#### Deliverables

- Acceptance contract: Define the Method and request-target-form coherence state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Method and request-target-form coherence and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Method and request-target-form coherence contract and all previously implemented relevant behavior have
reproducible evidence; v0.39.0 (HTTP/1.1 Host validation and duplicate rejection) still passes; no behavior assigned to v0.41.0 (Checked Content-Length grammar) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.40.0 implementation stop reached. Run pentest for this exact commit.`

### v0.41.0 — Checked Content-Length grammar

Status: planned

#### Goal

Deliver **Checked Content-Length grammar** as the sole primary capability in this stop. It builds
on v0.40.0 (Method and request-target-form coherence) and must be independently trustworthy before v0.42.0 (Repeated and comma-list Content-Length resolution) begins.

#### Deliverables

- Acceptance contract: Define the Checked Content-Length grammar state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked Content-Length grammar contract and all previously implemented relevant behavior have
reproducible evidence; v0.40.0 (Method and request-target-form coherence) still passes; no behavior assigned to v0.42.0 (Repeated and comma-list Content-Length resolution) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.41.0 implementation stop reached. Run pentest for this exact commit.`

### v0.42.0 — Repeated and comma-list Content-Length resolution

Status: planned

#### Goal

Deliver **Repeated and comma-list Content-Length resolution** as the sole primary capability in this stop. It builds
on v0.41.0 (Checked Content-Length grammar) and must be independently trustworthy before v0.43.0 (Transfer-Encoding grammar and ordering) begins.

#### Deliverables

- Acceptance contract: Define the Repeated and comma-list Content-Length resolution state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Repeated and comma-list Content-Length resolution contract and all previously implemented relevant behavior have
reproducible evidence; v0.41.0 (Checked Content-Length grammar) still passes; no behavior assigned to v0.43.0 (Transfer-Encoding grammar and ordering) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.42.0 implementation stop reached. Run pentest for this exact commit.`

### v0.43.0 — Transfer-Encoding grammar and ordering

Status: planned

#### Goal

Deliver **Transfer-Encoding grammar and ordering** as the sole primary capability in this stop. It builds
on v0.42.0 (Repeated and comma-list Content-Length resolution) and must be independently trustworthy before v0.44.0 (TE/CL conflict resolution and mandatory close action) begins.

#### Deliverables

- Acceptance contract: Define the Transfer-Encoding grammar and ordering state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Transfer-Encoding grammar and ordering contract and all previously implemented relevant behavior have
reproducible evidence; v0.42.0 (Repeated and comma-list Content-Length resolution) still passes; no behavior assigned to v0.44.0 (TE/CL conflict resolution and mandatory close action) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.43.0 implementation stop reached. Run pentest for this exact commit.`

### v0.44.0 — TE/CL conflict resolution and mandatory close action

Status: planned

#### Goal

Deliver **TE/CL conflict resolution and mandatory close action** as the sole primary capability in this stop. It builds
on v0.43.0 (Transfer-Encoding grammar and ordering) and must be independently trustworthy before v0.45.0 (Central HTTP/1 message-body-length algorithm) begins.

#### Deliverables

- Acceptance contract: Define the TE/CL conflict resolution and mandatory close action state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test TE/CL conflict resolution and mandatory close action and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The TE/CL conflict resolution and mandatory close action contract and all previously implemented relevant behavior have
reproducible evidence; v0.43.0 (Transfer-Encoding grammar and ordering) still passes; no behavior assigned to v0.45.0 (Central HTTP/1 message-body-length algorithm) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.44.0 implementation stop reached. Run pentest for this exact commit.`

### v0.45.0 — Central HTTP/1 message-body-length algorithm

Status: planned

#### Goal

Deliver **Central HTTP/1 message-body-length algorithm** as the sole primary capability in this stop. It builds
on v0.44.0 (TE/CL conflict resolution and mandatory close action) and must be independently trustworthy before v0.46.0 (Fixed-length body decoder) begins.

#### Deliverables

- Acceptance contract: Produce exactly one framing decision with checked arithmetic across method/status context, TE/CL ambiguity, body-forbidden responses, and mandatory-close behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- Run Kani proofs for framing arithmetic and exhaustive method/status/field decisions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Central HTTP/1 message-body-length algorithm contract and all previously implemented relevant behavior have
reproducible evidence; v0.44.0 (TE/CL conflict resolution and mandatory close action) still passes; no behavior assigned to v0.46.0 (Fixed-length body decoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.45.0 implementation stop reached. Run pentest for this exact commit.`

### v0.46.0 — Fixed-length body decoder

Status: planned

#### Goal

Deliver **Fixed-length body decoder** as the sole primary capability in this stop. It builds
on v0.45.0 (Central HTTP/1 message-body-length algorithm) and must be independently trustworthy before v0.47.0 (Close-delimited response decoder) begins.

#### Deliverables

- Acceptance contract: Define the Fixed-length body decoder state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Fixed-length body decoder and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Fixed-length body decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.45.0 (Central HTTP/1 message-body-length algorithm) still passes; no behavior assigned to v0.47.0 (Close-delimited response decoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.46.0 implementation stop reached. Run pentest for this exact commit.`

### v0.47.0 — Close-delimited response decoder

Status: planned

#### Goal

Deliver **Close-delimited response decoder** as the sole primary capability in this stop. It builds
on v0.46.0 (Fixed-length body decoder) and must be independently trustworthy before v0.48.0 (Checked chunk-size parser) begins.

#### Deliverables

- Acceptance contract: Define the Close-delimited response decoder state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Close-delimited response decoder and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Close-delimited response decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.46.0 (Fixed-length body decoder) still passes; no behavior assigned to v0.48.0 (Checked chunk-size parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.47.0 implementation stop reached. Run pentest for this exact commit.`

### v0.48.0 — Checked chunk-size parser

Status: planned

#### Goal

Deliver **Checked chunk-size parser** as the sole primary capability in this stop. It builds
on v0.47.0 (Close-delimited response decoder) and must be independently trustworthy before v0.49.0 (Incremental chunk-data state) begins.

#### Deliverables

- Acceptance contract: Define the Checked chunk-size parser state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Checked chunk-size parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.47.0 (Close-delimited response decoder) still passes; no behavior assigned to v0.49.0 (Incremental chunk-data state) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.48.0 implementation stop reached. Run pentest for this exact commit.`

### v0.49.0 — Incremental chunk-data state

Status: planned

#### Goal

Deliver **Incremental chunk-data state** as the sole primary capability in this stop. It builds
on v0.48.0 (Checked chunk-size parser) and must be independently trustworthy before v0.50.0 (Bounded chunk-extension parser) begins.

#### Deliverables

- Acceptance contract: Define the Incremental chunk-data state state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Incremental chunk-data state contract and all previously implemented relevant behavior have
reproducible evidence; v0.48.0 (Checked chunk-size parser) still passes; no behavior assigned to v0.50.0 (Bounded chunk-extension parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.49.0 implementation stop reached. Run pentest for this exact commit.`

### v0.50.0 — Bounded chunk-extension parser

Status: planned

#### Goal

Deliver **Bounded chunk-extension parser** as the sole primary capability in this stop. It builds
on v0.49.0 (Incremental chunk-data state) and must be independently trustworthy before v0.51.0 (Last-chunk and trailer transition) begins.

#### Deliverables

- Acceptance contract: Define the Bounded chunk-extension parser state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Bounded chunk-extension parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.49.0 (Incremental chunk-data state) still passes; no behavior assigned to v0.51.0 (Last-chunk and trailer transition) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.50.0 implementation stop reached. Run pentest for this exact commit.`

### v0.51.0 — Last-chunk and trailer transition

Status: planned

#### Goal

Deliver **Last-chunk and trailer transition** as the sole primary capability in this stop. It builds
on v0.50.0 (Bounded chunk-extension parser) and must be independently trustworthy before v0.52.0 (Trailer declarations and prohibited-trailer policy) begins.

#### Deliverables

- Acceptance contract: Define the Last-chunk and trailer transition state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Last-chunk and trailer transition contract and all previously implemented relevant behavior have
reproducible evidence; v0.50.0 (Bounded chunk-extension parser) still passes; no behavior assigned to v0.52.0 (Trailer declarations and prohibited-trailer policy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.51.0 implementation stop reached. Run pentest for this exact commit.`

### v0.52.0 — Trailer declarations and prohibited-trailer policy

Status: planned

#### Goal

Deliver **Trailer declarations and prohibited-trailer policy** as the sole primary capability in this stop. It builds
on v0.51.0 (Last-chunk and trailer transition) and must be independently trustworthy before v0.53.0 (Chunked encoder with partial-output state) begins.

#### Deliverables

- Acceptance contract: Define the Trailer declarations and prohibited-trailer policy state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Trailer declarations and prohibited-trailer policy and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Trailer declarations and prohibited-trailer policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.51.0 (Last-chunk and trailer transition) still passes; no behavior assigned to v0.53.0 (Chunked encoder with partial-output state) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.52.0 implementation stop reached. Run pentest for this exact commit.`

### v0.53.0 — Chunked encoder with partial-output state

Status: planned

#### Goal

Deliver **Chunked encoder with partial-output state** as the sole primary capability in this stop. It builds
on v0.52.0 (Trailer declarations and prohibited-trailer policy) and must be independently trustworthy before v0.54.0 (Unified HTTP/1 outbound message state machine) begins.

#### Deliverables

- Acceptance contract: Define the Chunked encoder with partial-output state state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Chunked encoder with partial-output state and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Chunked encoder with partial-output state contract and all previously implemented relevant behavior have
reproducible evidence; v0.52.0 (Trailer declarations and prohibited-trailer policy) still passes; no behavior assigned to v0.54.0 (Unified HTTP/1 outbound message state machine) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.53.0 implementation stop reached. Run pentest for this exact commit.`

### v0.54.0 — Unified HTTP/1 outbound message state machine

Status: planned

#### Goal

Deliver **Unified HTTP/1 outbound message state machine** as the sole primary capability in this stop. It builds
on v0.53.0 (Chunked encoder with partial-output state) and must be independently trustworthy before v0.55.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) begins.

#### Deliverables

- Acceptance contract: Serialize a head followed by exactly no body, fixed-length bytes, or chunked bytes; reject length disagreement, illegal trailers, post-completion commands, and sender-side HEAD/CONNECT/1xx/204/304 violations under one-byte output fragmentation.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Unified HTTP/1 outbound message state machine contract and all previously implemented relevant behavior have
reproducible evidence; v0.53.0 (Chunked encoder with partial-output state) still passes; no behavior assigned to v0.55.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.54.0 implementation stop reached. Run pentest for this exact commit.`

### v0.55.0 — Inbound body acknowledgement, drain, discard, cancellation, and reuse

Status: planned

#### Goal

Deliver **Inbound body acknowledgement, drain, discard, cancellation, and reuse** as the sole primary capability in this stop. It builds
on v0.54.0 (Unified HTTP/1 outbound message state machine) and must be independently trustworthy before v0.56.0 (HTTP/1.1 persistence and Connection semantics) begins.

#### Deliverables

- Acceptance contract: Define the Inbound body acknowledgement, drain, discard, cancellation, and reuse state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Inbound body acknowledgement, drain, discard, cancellation, and reuse and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Inbound body acknowledgement, drain, discard, cancellation, and reuse contract and all previously implemented relevant behavior have
reproducible evidence; v0.54.0 (Unified HTTP/1 outbound message state machine) still passes; no behavior assigned to v0.56.0 (HTTP/1.1 persistence and Connection semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.55.0 implementation stop reached. Run pentest for this exact commit.`

### v0.56.0 — HTTP/1.1 persistence and Connection semantics

Status: planned

#### Goal

Deliver **HTTP/1.1 persistence and Connection semantics** as the sole primary capability in this stop. It builds
on v0.55.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) and must be independently trustworthy before v0.57.0 (Sequential request/response connection state) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/1.1 persistence and Connection semantics state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1.1 persistence and Connection semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.55.0 (Inbound body acknowledgement, drain, discard, cancellation, and reuse) still passes; no behavior assigned to v0.57.0 (Sequential request/response connection state) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.56.0 implementation stop reached. Run pentest for this exact commit.`

### v0.57.0 — Sequential request/response connection state

Status: planned

#### Goal

Deliver **Sequential request/response connection state** as the sole primary capability in this stop. It builds
on v0.56.0 (HTTP/1.1 persistence and Connection semantics) and must be independently trustworthy before v0.58.0 (Optional bounded pipelining queue) begins.

#### Deliverables

- Acceptance contract: Define the Sequential request/response connection state state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Sequential request/response connection state and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Sequential request/response connection state contract and all previously implemented relevant behavior have
reproducible evidence; v0.56.0 (HTTP/1.1 persistence and Connection semantics) still passes; no behavior assigned to v0.58.0 (Optional bounded pipelining queue) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.57.0 implementation stop reached. Run pentest for this exact commit.`

### v0.58.0 — Optional bounded pipelining queue

Status: planned

#### Goal

Deliver **Optional bounded pipelining queue** as the sole primary capability in this stop. It builds
on v0.57.0 (Sequential request/response connection state) and must be independently trustworthy before v0.59.0 (Informational response lifecycle) begins.

#### Deliverables

- Acceptance contract: Define the Optional bounded pipelining queue state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Optional bounded pipelining queue and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Optional bounded pipelining queue contract and all previously implemented relevant behavior have
reproducible evidence; v0.57.0 (Sequential request/response connection state) still passes; no behavior assigned to v0.59.0 (Informational response lifecycle) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.58.0 implementation stop reached. Run pentest for this exact commit.`

### v0.59.0 — Informational response lifecycle

Status: planned

#### Goal

Deliver **Informational response lifecycle** as the sole primary capability in this stop. It builds
on v0.58.0 (Optional bounded pipelining queue) and must be independently trustworthy before v0.60.0 (Expect: 100-continue state) begins.

#### Deliverables

- Acceptance contract: Define the Informational response lifecycle state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Informational response lifecycle and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Informational response lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.58.0 (Optional bounded pipelining queue) still passes; no behavior assigned to v0.60.0 (Expect: 100-continue state) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.59.0 implementation stop reached. Run pentest for this exact commit.`

### v0.60.0 — Expect: 100-continue state

Status: planned

#### Goal

Deliver **Expect: 100-continue state** as the sole primary capability in this stop. It builds
on v0.59.0 (Informational response lifecycle) and must be independently trustworthy before v0.61.0 (EOF, truncation, and incomplete-message rules) begins.

#### Deliverables

- Acceptance contract: Recognize exact 100-continue, emit 417 for unsupported expectations by policy, withhold client bodies, accept caller timeout decisions through injected time, handle final-before-100 and server pre-body rejection, bound drain-or-close behavior, and preserve pipeline ordering around interim responses.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Expect: 100-continue state and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Expect: 100-continue state contract and all previously implemented relevant behavior have
reproducible evidence; v0.59.0 (Informational response lifecycle) still passes; no behavior assigned to v0.61.0 (EOF, truncation, and incomplete-message rules) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.60.0 implementation stop reached. Run pentest for this exact commit.`

### v0.61.0 — EOF, truncation, and incomplete-message rules

Status: planned

#### Goal

Deliver **EOF, truncation, and incomplete-message rules** as the sole primary capability in this stop. It builds
on v0.60.0 (Expect: 100-continue state) and must be independently trustworthy before v0.62.0 (HEAD response-framing context) begins.

#### Deliverables

- Acceptance contract: Define the EOF, truncation, and incomplete-message rules state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test EOF, truncation, and incomplete-message rules and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The EOF, truncation, and incomplete-message rules contract and all previously implemented relevant behavior have
reproducible evidence; v0.60.0 (Expect: 100-continue state) still passes; no behavior assigned to v0.62.0 (HEAD response-framing context) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.61.0 implementation stop reached. Run pentest for this exact commit.`

### v0.62.0 — HEAD response-framing context

Status: planned

#### Goal

Deliver **HEAD response-framing context** as the sole primary capability in this stop. It builds
on v0.61.0 (EOF, truncation, and incomplete-message rules) and must be independently trustworthy before v0.63.0 (1xx, 204, 304, and body-forbidden response handling) begins.

#### Deliverables

- Acceptance contract: Define the HEAD response-framing context state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test HEAD response-framing context and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HEAD response-framing context contract and all previously implemented relevant behavior have
reproducible evidence; v0.61.0 (EOF, truncation, and incomplete-message rules) still passes; no behavior assigned to v0.63.0 (1xx, 204, 304, and body-forbidden response handling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.62.0 implementation stop reached. Run pentest for this exact commit.`

### v0.63.0 — 1xx, 204, 304, and body-forbidden response handling

Status: planned

#### Goal

Deliver **1xx, 204, 304, and body-forbidden response handling** as the sole primary capability in this stop. It builds
on v0.62.0 (HEAD response-framing context) and must be independently trustworthy before v0.64.0 (CONNECT request and successful tunnel transition) begins.

#### Deliverables

- Acceptance contract: Define the 1xx, 204, 304, and body-forbidden response handling state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test 1xx, 204, 304, and body-forbidden response handling and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The 1xx, 204, 304, and body-forbidden response handling contract and all previously implemented relevant behavior have
reproducible evidence; v0.62.0 (HEAD response-framing context) still passes; no behavior assigned to v0.64.0 (CONNECT request and successful tunnel transition) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.63.0 implementation stop reached. Run pentest for this exact commit.`

### v0.64.0 — CONNECT request and successful tunnel transition

Status: planned

#### Goal

Deliver **CONNECT request and successful tunnel transition** as the sole primary capability in this stop. It builds
on v0.63.0 (1xx, 204, 304, and body-forbidden response handling) and must be independently trustworthy before v0.65.0 (RFC 9931 optimistic-data protections) begins.

#### Deliverables

- Acceptance contract: Define the CONNECT request and successful tunnel transition state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test CONNECT request and successful tunnel transition and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONNECT request and successful tunnel transition contract and all previously implemented relevant behavior have
reproducible evidence; v0.63.0 (1xx, 204, 304, and body-forbidden response handling) still passes; no behavior assigned to v0.65.0 (RFC 9931 optimistic-data protections) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.64.0 implementation stop reached. Run pentest for this exact commit.`

### v0.65.0 — RFC 9931 optimistic-data protections

Status: planned

#### Goal

Deliver **RFC 9931 optimistic-data protections** as the sole primary capability in this stop. It builds
on v0.64.0 (CONNECT request and successful tunnel transition) and must be independently trustworthy before v0.66.0 (Connection-option, Upgrade, and hop-by-hop field grammar) begins.

#### Deliverables

- Acceptance contract: Define the RFC 9931 optimistic-data protections state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test RFC 9931 optimistic-data protections and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RFC 9931 optimistic-data protections contract and all previously implemented relevant behavior have
reproducible evidence; v0.64.0 (CONNECT request and successful tunnel transition) still passes; no behavior assigned to v0.66.0 (Connection-option, Upgrade, and hop-by-hop field grammar) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.65.0 implementation stop reached. Run pentest for this exact commit.`

### v0.66.0 — Connection-option, Upgrade, and hop-by-hop field grammar

Status: planned

#### Goal

Deliver **Connection-option, Upgrade, and hop-by-hop field grammar** as the sole primary capability in this stop. It builds
on v0.65.0 (RFC 9931 optimistic-data protections) and must be independently trustworthy before v0.67.0 (101 Switching Protocols transition and publication barrier) begins.

#### Deliverables

- Acceptance contract: Parse Connection option tokens and Upgrade grammar before any 101 or WebSocket validation and derive explicit hop-by-hop handling without implicit normalization.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Connection-option, Upgrade, and hop-by-hop field grammar and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection-option, Upgrade, and hop-by-hop field grammar contract and all previously implemented relevant behavior have
reproducible evidence; v0.65.0 (RFC 9931 optimistic-data protections) still passes; no behavior assigned to v0.67.0 (101 Switching Protocols transition and publication barrier) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.66.0 implementation stop reached. Run pentest for this exact commit.`

### v0.67.0 — 101 Switching Protocols transition and publication barrier

Status: planned

#### Goal

Deliver **101 Switching Protocols transition and publication barrier** as the sole primary capability in this stop. It builds
on v0.66.0 (Connection-option, Upgrade, and hop-by-hop field grammar) and must be independently trustworthy before v0.68.0 (Separate WebSocket handshake crate, key, version, and token validation) begins.

#### Deliverables

- Acceptance contract: Commit a valid 101 transition before exposing buffered post-handshake bytes and reject success paths whose Connection/Upgrade prerequisites are invalid.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test 101 Switching Protocols transition and publication barrier and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The 101 Switching Protocols transition and publication barrier contract and all previously implemented relevant behavior have
reproducible evidence; v0.66.0 (Connection-option, Upgrade, and hop-by-hop field grammar) still passes; no behavior assigned to v0.68.0 (Separate WebSocket handshake crate, key, version, and token validation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.67.0 implementation stop reached. Run pentest for this exact commit.`

### v0.68.0 — Separate WebSocket handshake crate, key, version, and token validation

Status: planned

#### Goal

Deliver **Separate WebSocket handshake crate, key, version, and token validation** as the sole primary capability in this stop. It builds
on v0.67.0 (101 Switching Protocols transition and publication barrier) and must be independently trustworthy before v0.69.0 (Caller-supplied WebSocket nonce and entropy boundary) begins.

#### Deliverables

- Acceptance contract: Create an optional no_std handshake boundary that validates Sec-WebSocket-Key base64 shape, version 13, Upgrade/Connection tokens, and distinct client/server rules without implementing frames.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Separate WebSocket handshake crate, key, version, and token validation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Separate WebSocket handshake crate, key, version, and token validation contract and all previously implemented relevant behavior have
reproducible evidence; v0.67.0 (101 Switching Protocols transition and publication barrier) still passes; no behavior assigned to v0.69.0 (Caller-supplied WebSocket nonce and entropy boundary) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.68.0 implementation stop reached. Run pentest for this exact commit.`

### v0.69.0 — Caller-supplied WebSocket nonce and entropy boundary

Status: planned

#### Goal

Deliver **Caller-supplied WebSocket nonce and entropy boundary** as the sole primary capability in this stop. It builds
on v0.68.0 (Separate WebSocket handshake crate, key, version, and token validation) and must be independently trustworthy before v0.70.0 (WebSocket accept generation and client/server validation) begins.

#### Deliverables

- Acceptance contract: Require a validated WebSocketNonce([u8; 16]) from the caller or adapter-only entropy capability for every client handshake; core code rejects missing/reused-policy input and never creates deterministic, time-derived, repeated, or weak keys.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Caller-supplied WebSocket nonce and entropy boundary and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Caller-supplied WebSocket nonce and entropy boundary contract and all previously implemented relevant behavior have
reproducible evidence; v0.68.0 (Separate WebSocket handshake crate, key, version, and token validation) still passes; no behavior assigned to v0.70.0 (WebSocket accept generation and client/server validation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.69.0 implementation stop reached. Run pentest for this exact commit.`

### v0.70.0 — WebSocket accept generation and client/server validation

Status: planned

#### Goal

Deliver **WebSocket accept generation and client/server validation** as the sole primary capability in this stop. It builds
on v0.69.0 (Caller-supplied WebSocket nonce and entropy boundary) and must be independently trustworthy before v0.71.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) begins.

#### Deliverables

- Acceptance contract: Implement and vector-test the RFC 6455 SHA-1 plus base64 accept calculation, server generation, client validation, invalid padding/length rejection, and bounded dependency-free operation.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test WebSocket accept generation and client/server validation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WebSocket accept generation and client/server validation contract and all previously implemented relevant behavior have
reproducible evidence; v0.69.0 (Caller-supplied WebSocket nonce and entropy boundary) still passes; no behavior assigned to v0.71.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.70.0 implementation stop reached. Run pentest for this exact commit.`

### v0.71.0 — WebSocket negotiation, origin metadata, and byte-publication barrier

Status: planned

#### Goal

Deliver **WebSocket negotiation, origin metadata, and byte-publication barrier** as the sole primary capability in this stop. It builds
on v0.70.0 (WebSocket accept generation and client/server validation) and must be independently trustworthy before v0.72.0 (Safe forwarding and explicit reframing plan) begins.

#### Deliverables

- Acceptance contract: Define subprotocol and extension selection, preserve Origin metadata for caller policy, reject unsolicited negotiation, and publish no post-handshake bytes before success.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test WebSocket negotiation, origin metadata, and byte-publication barrier and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WebSocket negotiation, origin metadata, and byte-publication barrier contract and all previously implemented relevant behavior have
reproducible evidence; v0.70.0 (WebSocket accept generation and client/server validation) still passes; no behavior assigned to v0.72.0 (Safe forwarding and explicit reframing plan) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.71.0 implementation stop reached. Run pentest for this exact commit.`

### v0.72.0 — Safe forwarding and explicit reframing plan

Status: planned

#### Goal

Deliver **Safe forwarding and explicit reframing plan** as the sole primary capability in this stop. It builds
on v0.71.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) and must be independently trustworthy before v0.73.0 (RFC 1945 HTTP/1.0 parser and hardened profile) begins.

#### Deliverables

- Acceptance contract: Define the Safe forwarding and explicit reframing plan state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Safe forwarding and explicit reframing plan and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Safe forwarding and explicit reframing plan contract and all previously implemented relevant behavior have
reproducible evidence; v0.71.0 (WebSocket negotiation, origin metadata, and byte-publication barrier) still passes; no behavior assigned to v0.73.0 (RFC 1945 HTTP/1.0 parser and hardened profile) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.72.0 implementation stop reached. Run pentest for this exact commit.`

### v0.73.0 — RFC 1945 HTTP/1.0 parser and hardened profile

Status: planned

#### Goal

Deliver **RFC 1945 HTTP/1.0 parser and hardened profile** as the sole primary capability in this stop. It builds
on v0.72.0 (Safe forwarding and explicit reframing plan) and must be independently trustworthy before v0.74.0 (HTTP/1.0 default-close lifecycle) begins.

#### Deliverables

- Acceptance contract: Define the RFC 1945 HTTP/1.0 parser and hardened profile state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RFC 1945 HTTP/1.0 parser and hardened profile contract and all previously implemented relevant behavior have
reproducible evidence; v0.72.0 (Safe forwarding and explicit reframing plan) still passes; no behavior assigned to v0.74.0 (HTTP/1.0 default-close lifecycle) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.73.0 implementation stop reached. Run pentest for this exact commit.`

### v0.74.0 — HTTP/1.0 default-close lifecycle

Status: planned

#### Goal

Deliver **HTTP/1.0 default-close lifecycle** as the sole primary capability in this stop. It builds
on v0.73.0 (RFC 1945 HTTP/1.0 parser and hardened profile) and must be independently trustworthy before v0.75.0 (Explicit HTTP/1.0 keep-alive extension profile) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/1.0 default-close lifecycle state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1.0 default-close lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.73.0 (RFC 1945 HTTP/1.0 parser and hardened profile) still passes; no behavior assigned to v0.75.0 (Explicit HTTP/1.0 keep-alive extension profile) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.74.0 implementation stop reached. Run pentest for this exact commit.`

### v0.75.0 — Explicit HTTP/1.0 keep-alive extension profile

Status: planned

#### Goal

Deliver **Explicit HTTP/1.0 keep-alive extension profile** as the sole primary capability in this stop. It builds
on v0.74.0 (HTTP/1.0 default-close lifecycle) and must be independently trustworthy before v0.76.0 (Separate vef-http09 package and exact grammar) begins.

#### Deliverables

- Acceptance contract: Define the Explicit HTTP/1.0 keep-alive extension profile state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit HTTP/1.0 keep-alive extension profile contract and all previously implemented relevant behavior have
reproducible evidence; v0.74.0 (HTTP/1.0 default-close lifecycle) still passes; no behavior assigned to v0.76.0 (Separate vef-http09 package and exact grammar) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.75.0 implementation stop reached. Run pentest for this exact commit.`

### v0.76.0 — Separate vef-http09 package and exact grammar

Status: planned

#### Goal

Deliver **Separate vef-http09 package and exact grammar** as the sole primary capability in this stop. It builds
on v0.75.0 (Explicit HTTP/1.0 keep-alive extension profile) and must be independently trustworthy before v0.77.0 (Explicit HTTP/0.9 client API) begins.

#### Deliverables

- Acceptance contract: Define the Separate vef-http09 package and exact grammar state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Separate vef-http09 package and exact grammar and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Separate vef-http09 package and exact grammar contract and all previously implemented relevant behavior have
reproducible evidence; v0.75.0 (Explicit HTTP/1.0 keep-alive extension profile) still passes; no behavior assigned to v0.77.0 (Explicit HTTP/0.9 client API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.76.0 implementation stop reached. Run pentest for this exact commit.`

### v0.77.0 — Explicit HTTP/0.9 client API

Status: planned

#### Goal

Deliver **Explicit HTTP/0.9 client API** as the sole primary capability in this stop. It builds
on v0.76.0 (Separate vef-http09 package and exact grammar) and must be independently trustworthy before v0.78.0 (Explicit HTTP/0.9 server and dedicated-listener API) begins.

#### Deliverables

- Acceptance contract: Define the Explicit HTTP/0.9 client API state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Explicit HTTP/0.9 client API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit HTTP/0.9 client API contract and all previously implemented relevant behavior have
reproducible evidence; v0.76.0 (Separate vef-http09 package and exact grammar) still passes; no behavior assigned to v0.78.0 (Explicit HTTP/0.9 server and dedicated-listener API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.77.0 implementation stop reached. Run pentest for this exact commit.`

### v0.78.0 — Explicit HTTP/0.9 server and dedicated-listener API

Status: planned

#### Goal

Deliver **Explicit HTTP/0.9 server and dedicated-listener API** as the sole primary capability in this stop. It builds
on v0.77.0 (Explicit HTTP/0.9 client API) and must be independently trustworthy before v0.79.0 (HTTP/0.9 cross-protocol rejection corpus) begins.

#### Deliverables

- Acceptance contract: Define the Explicit HTTP/0.9 server and dedicated-listener API state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Explicit HTTP/0.9 server and dedicated-listener API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Explicit HTTP/0.9 server and dedicated-listener API contract and all previously implemented relevant behavior have
reproducible evidence; v0.77.0 (Explicit HTTP/0.9 client API) still passes; no behavior assigned to v0.79.0 (HTTP/0.9 cross-protocol rejection corpus) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.78.0 implementation stop reached. Run pentest for this exact commit.`

### v0.79.0 — HTTP/0.9 cross-protocol rejection corpus

Status: planned

#### Goal

Deliver **HTTP/0.9 cross-protocol rejection corpus** as the sole primary capability in this stop. It builds
on v0.78.0 (Explicit HTTP/0.9 server and dedicated-listener API) and must be independently trustworthy before v0.80.0 (HTTP/1 smuggling and ambiguity corpus) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/0.9 cross-protocol rejection corpus state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test HTTP/0.9 cross-protocol rejection corpus and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/0.9 cross-protocol rejection corpus contract and all previously implemented relevant behavior have
reproducible evidence; v0.78.0 (Explicit HTTP/0.9 server and dedicated-listener API) still passes; no behavior assigned to v0.80.0 (HTTP/1 smuggling and ambiguity corpus) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.79.0 implementation stop reached. Run pentest for this exact commit.`

### v0.80.0 — HTTP/1 smuggling and ambiguity corpus

Status: planned

#### Goal

Deliver **HTTP/1 smuggling and ambiguity corpus** as the sole primary capability in this stop. It builds
on v0.79.0 (HTTP/0.9 cross-protocol rejection corpus) and must be independently trustworthy before v0.81.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/1 smuggling and ambiguity corpus state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 smuggling and ambiguity corpus contract and all previously implemented relevant behavior have
reproducible evidence; v0.79.0 (HTTP/0.9 cross-protocol rejection corpus) still passes; no behavior assigned to v0.81.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.80.0 implementation stop reached. Run pentest for this exact commit.`

### v0.81.0 — HTTP/1 and HTTP/0.9 conformance audit and pentest

Status: planned

#### Goal

Deliver **HTTP/1 and HTTP/0.9 conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.80.0 (HTTP/1 smuggling and ambiguity corpus) and must be independently trustworthy before v0.82.0 (HPACK prefix-integer decoder) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/1 and HTTP/0.9 conformance audit and pentest state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 1945, RFC 6455 opening-handshake requirements, RFC 9110, RFC 9111 preservation requirements, RFC 9112 and errata, the RFC 9298 non-applicability decision, and RFC 9931.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 and HTTP/0.9 conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.80.0 (HTTP/1 smuggling and ambiguity corpus) still passes; no behavior assigned to v0.82.0 (HPACK prefix-integer decoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.81.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 3 — HPACK and HTTP/2

Phase contract: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.

### v0.82.0 — HPACK prefix-integer decoder

Status: planned

#### Goal

Deliver **HPACK prefix-integer decoder** as the sole primary capability in this stop. It builds
on v0.81.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) and must be independently trustworthy before v0.83.0 (HPACK prefix-integer encoder) begins.

#### Deliverables

- Acceptance contract: Define the HPACK prefix-integer decoder state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK prefix-integer decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.81.0 (HTTP/1 and HTTP/0.9 conformance audit and pentest) still passes; no behavior assigned to v0.83.0 (HPACK prefix-integer encoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.82.0 implementation stop reached. Run pentest for this exact commit.`

### v0.83.0 — HPACK prefix-integer encoder

Status: planned

#### Goal

Deliver **HPACK prefix-integer encoder** as the sole primary capability in this stop. It builds
on v0.82.0 (HPACK prefix-integer decoder) and must be independently trustworthy before v0.84.0 (HPACK integer overflow and minimality proofs) begins.

#### Deliverables

- Acceptance contract: Define the HPACK prefix-integer encoder state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK prefix-integer encoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.82.0 (HPACK prefix-integer decoder) still passes; no behavior assigned to v0.84.0 (HPACK integer overflow and minimality proofs) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.83.0 implementation stop reached. Run pentest for this exact commit.`

### v0.84.0 — HPACK integer overflow and minimality proofs

Status: planned

#### Goal

Deliver **HPACK integer overflow and minimality proofs** as the sole primary capability in this stop. It builds
on v0.83.0 (HPACK prefix-integer encoder) and must be independently trustworthy before v0.85.0 (HPACK string representation codec) begins.

#### Deliverables

- Acceptance contract: Define the HPACK integer overflow and minimality proofs state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK integer overflow and minimality proofs contract and all previously implemented relevant behavior have
reproducible evidence; v0.83.0 (HPACK prefix-integer encoder) still passes; no behavior assigned to v0.85.0 (HPACK string representation codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.84.0 implementation stop reached. Run pentest for this exact commit.`

### v0.85.0 — HPACK string representation codec

Status: planned

#### Goal

Deliver **HPACK string representation codec** as the sole primary capability in this stop. It builds
on v0.84.0 (HPACK integer overflow and minimality proofs) and must be independently trustworthy before v0.86.0 (HPACK Huffman tables) begins.

#### Deliverables

- Acceptance contract: Define the HPACK string representation codec state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK string representation codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.84.0 (HPACK integer overflow and minimality proofs) still passes; no behavior assigned to v0.86.0 (HPACK Huffman tables) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.85.0 implementation stop reached. Run pentest for this exact commit.`

### v0.86.0 — HPACK Huffman tables

Status: planned

#### Goal

Deliver **HPACK Huffman tables** as the sole primary capability in this stop. It builds
on v0.85.0 (HPACK string representation codec) and must be independently trustworthy before v0.87.0 (HPACK Huffman decoder) begins.

#### Deliverables

- Acceptance contract: Define the HPACK Huffman tables state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK Huffman tables contract and all previously implemented relevant behavior have
reproducible evidence; v0.85.0 (HPACK string representation codec) still passes; no behavior assigned to v0.87.0 (HPACK Huffman decoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.86.0 implementation stop reached. Run pentest for this exact commit.`

### v0.87.0 — HPACK Huffman decoder

Status: planned

#### Goal

Deliver **HPACK Huffman decoder** as the sole primary capability in this stop. It builds
on v0.86.0 (HPACK Huffman tables) and must be independently trustworthy before v0.88.0 (HPACK Huffman encoder) begins.

#### Deliverables

- Acceptance contract: Define the HPACK Huffman decoder state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK Huffman decoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.86.0 (HPACK Huffman tables) still passes; no behavior assigned to v0.88.0 (HPACK Huffman encoder) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.87.0 implementation stop reached. Run pentest for this exact commit.`

### v0.88.0 — HPACK Huffman encoder

Status: planned

#### Goal

Deliver **HPACK Huffman encoder** as the sole primary capability in this stop. It builds
on v0.87.0 (HPACK Huffman decoder) and must be independently trustworthy before v0.89.0 (HPACK static table) begins.

#### Deliverables

- Acceptance contract: Define the HPACK Huffman encoder state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK Huffman encoder contract and all previously implemented relevant behavior have
reproducible evidence; v0.87.0 (HPACK Huffman decoder) still passes; no behavior assigned to v0.89.0 (HPACK static table) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.88.0 implementation stop reached. Run pentest for this exact commit.`

### v0.89.0 — HPACK static table

Status: planned

#### Goal

Deliver **HPACK static table** as the sole primary capability in this stop. It builds
on v0.88.0 (HPACK Huffman encoder) and must be independently trustworthy before v0.90.0 (HPACK dynamic table storage) begins.

#### Deliverables

- Acceptance contract: Define the HPACK static table state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK static table contract and all previously implemented relevant behavior have
reproducible evidence; v0.88.0 (HPACK Huffman encoder) still passes; no behavior assigned to v0.90.0 (HPACK dynamic table storage) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.89.0 implementation stop reached. Run pentest for this exact commit.`

### v0.90.0 — HPACK dynamic table storage

Status: planned

#### Goal

Deliver **HPACK dynamic table storage** as the sole primary capability in this stop. It builds
on v0.89.0 (HPACK static table) and must be independently trustworthy before v0.91.0 (HPACK eviction and oversize-entry behavior) begins.

#### Deliverables

- Acceptance contract: Define the HPACK dynamic table storage state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK dynamic table storage contract and all previously implemented relevant behavior have
reproducible evidence; v0.89.0 (HPACK static table) still passes; no behavior assigned to v0.91.0 (HPACK eviction and oversize-entry behavior) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.90.0 implementation stop reached. Run pentest for this exact commit.`

### v0.91.0 — HPACK eviction and oversize-entry behavior

Status: planned

#### Goal

Deliver **HPACK eviction and oversize-entry behavior** as the sole primary capability in this stop. It builds
on v0.90.0 (HPACK dynamic table storage) and must be independently trustworthy before v0.92.0 (HPACK table-size update and SETTINGS coupling) begins.

#### Deliverables

- Acceptance contract: Define the HPACK eviction and oversize-entry behavior state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK eviction and oversize-entry behavior contract and all previously implemented relevant behavior have
reproducible evidence; v0.90.0 (HPACK dynamic table storage) still passes; no behavior assigned to v0.92.0 (HPACK table-size update and SETTINGS coupling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.91.0 implementation stop reached. Run pentest for this exact commit.`

### v0.92.0 — HPACK table-size update and SETTINGS coupling

Status: planned

#### Goal

Deliver **HPACK table-size update and SETTINGS coupling** as the sole primary capability in this stop. It builds
on v0.91.0 (HPACK eviction and oversize-entry behavior) and must be independently trustworthy before v0.93.0 (HPACK caller-owned ring lookup) begins.

#### Deliverables

- Acceptance contract: Define the HPACK table-size update and SETTINGS coupling state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK table-size update and SETTINGS coupling contract and all previously implemented relevant behavior have
reproducible evidence; v0.91.0 (HPACK eviction and oversize-entry behavior) still passes; no behavior assigned to v0.93.0 (HPACK caller-owned ring lookup) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.92.0 implementation stop reached. Run pentest for this exact commit.`

### v0.93.0 — HPACK caller-owned ring lookup

Status: planned

#### Goal

Deliver **HPACK caller-owned ring lookup** as the sole primary capability in this stop. It builds
on v0.92.0 (HPACK table-size update and SETTINGS coupling) and must be independently trustworthy before v0.94.0 (HPACK indexed representation) begins.

#### Deliverables

- Acceptance contract: Define the HPACK caller-owned ring lookup state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK caller-owned ring lookup contract and all previously implemented relevant behavior have
reproducible evidence; v0.92.0 (HPACK table-size update and SETTINGS coupling) still passes; no behavior assigned to v0.94.0 (HPACK indexed representation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.93.0 implementation stop reached. Run pentest for this exact commit.`

### v0.94.0 — HPACK indexed representation

Status: planned

#### Goal

Deliver **HPACK indexed representation** as the sole primary capability in this stop. It builds
on v0.93.0 (HPACK caller-owned ring lookup) and must be independently trustworthy before v0.95.0 (HPACK incremental-indexing literal) begins.

#### Deliverables

- Acceptance contract: Define the HPACK indexed representation state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK indexed representation contract and all previously implemented relevant behavior have
reproducible evidence; v0.93.0 (HPACK caller-owned ring lookup) still passes; no behavior assigned to v0.95.0 (HPACK incremental-indexing literal) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.94.0 implementation stop reached. Run pentest for this exact commit.`

### v0.95.0 — HPACK incremental-indexing literal

Status: planned

#### Goal

Deliver **HPACK incremental-indexing literal** as the sole primary capability in this stop. It builds
on v0.94.0 (HPACK indexed representation) and must be independently trustworthy before v0.96.0 (HPACK non-indexing and never-indexed literal) begins.

#### Deliverables

- Acceptance contract: Define the HPACK incremental-indexing literal state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK incremental-indexing literal contract and all previously implemented relevant behavior have
reproducible evidence; v0.94.0 (HPACK indexed representation) still passes; no behavior assigned to v0.96.0 (HPACK non-indexing and never-indexed literal) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.95.0 implementation stop reached. Run pentest for this exact commit.`

### v0.96.0 — HPACK non-indexing and never-indexed literal

Status: planned

#### Goal

Deliver **HPACK non-indexing and never-indexed literal** as the sole primary capability in this stop. It builds
on v0.95.0 (HPACK incremental-indexing literal) and must be independently trustworthy before v0.97.0 (Sensitive-field indexing policy) begins.

#### Deliverables

- Acceptance contract: Define the HPACK non-indexing and never-indexed literal state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK non-indexing and never-indexed literal contract and all previously implemented relevant behavior have
reproducible evidence; v0.95.0 (HPACK incremental-indexing literal) still passes; no behavior assigned to v0.97.0 (Sensitive-field indexing policy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.96.0 implementation stop reached. Run pentest for this exact commit.`

### v0.97.0 — Sensitive-field indexing policy

Status: planned

#### Goal

Deliver **Sensitive-field indexing policy** as the sole primary capability in this stop. It builds
on v0.96.0 (HPACK non-indexing and never-indexed literal) and must be independently trustworthy before v0.98.0 (HPACK encoder output commit and indexing policy) begins.

#### Deliverables

- Acceptance contract: Define the Sensitive-field indexing policy state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Sensitive-field indexing policy and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Sensitive-field indexing policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.96.0 (HPACK non-indexing and never-indexed literal) still passes; no behavior assigned to v0.98.0 (HPACK encoder output commit and indexing policy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.97.0 implementation stop reached. Run pentest for this exact commit.`

### v0.98.0 — HPACK encoder output commit and indexing policy

Status: planned

#### Goal

Deliver **HPACK encoder output commit and indexing policy** as the sole primary capability in this stop. It builds
on v0.97.0 (Sensitive-field indexing policy) and must be independently trustworthy before v0.99.0 (Independent HPACK decode limits) begins.

#### Deliverables

- Acceptance contract: Mutate the encoder dynamic table only when corresponding representation bytes commit; NeedOutput, cancellation, and retry cannot double-insert or advance ahead of the peer; table-size updates start the block; block-size preflight, bounded lookup, deterministic indexing, and sensitive-field overrides are explicit.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- Prove no table mutation before committed representation bytes, no double insert after NeedOutput, correct cancellation/partial-output state, legal table-size-update ordering, bounded preflight, and bounded indexing cost.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK encoder output commit and indexing policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.97.0 (Sensitive-field indexing policy) still passes; no behavior assigned to v0.99.0 (Independent HPACK decode limits) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.98.0 implementation stop reached. Run pentest for this exact commit.`

### v0.99.0 — Independent HPACK decode limits

Status: planned

#### Goal

Deliver **Independent HPACK decode limits** as the sole primary capability in this stop. It builds
on v0.98.0 (HPACK encoder output commit and indexing policy) and must be independently trustworthy before v0.100.0 (HPACK synchronization, publication barrier, and error scope) begins.

#### Deliverables

- Acceptance contract: Define the Independent HPACK decode limits state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Independent HPACK decode limits and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Independent HPACK decode limits contract and all previously implemented relevant behavior have
reproducible evidence; v0.98.0 (HPACK encoder output commit and indexing policy) still passes; no behavior assigned to v0.100.0 (HPACK synchronization, publication barrier, and error scope) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.99.0 implementation stop reached. Run pentest for this exact commit.`

### v0.100.0 — HPACK synchronization, publication barrier, and error scope

Status: planned

#### Goal

Deliver **HPACK synchronization, publication barrier, and error scope** as the sole primary capability in this stop. It builds
on v0.99.0 (Independent HPACK decode limits) and must be independently trustworthy before v0.101.0 (HPACK conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Commit valid compression-table updates even when later semantic validation rejects a stream; withhold fields until validation, make compression errors connection-fatal, never roll back connection compression state for stream errors, and close when limits prevent safe completion.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK synchronization, publication barrier, and error scope contract and all previously implemented relevant behavior have
reproducible evidence; v0.99.0 (Independent HPACK decode limits) still passes; no behavior assigned to v0.101.0 (HPACK conformance audit and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.100.0 implementation stop reached. Run pentest for this exact commit.`

### v0.101.0 — HPACK conformance audit and pentest

Status: planned

#### Goal

Deliver **HPACK conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.100.0 (HPACK synchronization, publication barrier, and error scope) and must be independently trustworthy before v0.102.0 (HTTP/2 client and server prefaces) begins.

#### Deliverables

- Acceptance contract: Define the HPACK conformance audit and pentest state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HPACK fuzz/model target now, including output-commit atomicity for encoder work.
- Prove no table mutation before committed representation bytes, no double insert after NeedOutput, correct cancellation/partial-output state, legal table-size-update ordering, bounded preflight, and bounded indexing cost.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HPACK conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.100.0 (HPACK synchronization, publication barrier, and error scope) still passes; no behavior assigned to v0.102.0 (HTTP/2 client and server prefaces) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.101.0 implementation stop reached. Run pentest for this exact commit.`

### v0.102.0 — HTTP/2 client and server prefaces

Status: planned

#### Goal

Deliver **HTTP/2 client and server prefaces** as the sole primary capability in this stop. It builds
on v0.101.0 (HPACK conformance audit and pentest) and must be independently trustworthy before v0.103.0 (HTTP/2 frame-header codec) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/2 client and server prefaces state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 client and server prefaces contract and all previously implemented relevant behavior have
reproducible evidence; v0.101.0 (HPACK conformance audit and pentest) still passes; no behavior assigned to v0.103.0 (HTTP/2 frame-header codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.102.0 implementation stop reached. Run pentest for this exact commit.`

### v0.103.0 — HTTP/2 frame-header codec

Status: planned

#### Goal

Deliver **HTTP/2 frame-header codec** as the sole primary capability in this stop. It builds
on v0.102.0 (HTTP/2 client and server prefaces) and must be independently trustworthy before v0.104.0 (DATA frame codec) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/2 frame-header codec state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 frame-header codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.102.0 (HTTP/2 client and server prefaces) still passes; no behavior assigned to v0.104.0 (DATA frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.103.0 implementation stop reached. Run pentest for this exact commit.`

### v0.104.0 — DATA frame codec

Status: planned

#### Goal

Deliver **DATA frame codec** as the sole primary capability in this stop. It builds
on v0.103.0 (HTTP/2 frame-header codec) and must be independently trustworthy before v0.105.0 (HEADERS frame codec) begins.

#### Deliverables

- Acceptance contract: Define the DATA frame codec state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The DATA frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.103.0 (HTTP/2 frame-header codec) still passes; no behavior assigned to v0.105.0 (HEADERS frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.104.0 implementation stop reached. Run pentest for this exact commit.`

### v0.105.0 — HEADERS frame codec

Status: planned

#### Goal

Deliver **HEADERS frame codec** as the sole primary capability in this stop. It builds
on v0.104.0 (DATA frame codec) and must be independently trustworthy before v0.106.0 (CONTINUATION frame codec) begins.

#### Deliverables

- Acceptance contract: Define the HEADERS frame codec state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HEADERS frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.104.0 (DATA frame codec) still passes; no behavior assigned to v0.106.0 (CONTINUATION frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.105.0 implementation stop reached. Run pentest for this exact commit.`

### v0.106.0 — CONTINUATION frame codec

Status: planned

#### Goal

Deliver **CONTINUATION frame codec** as the sole primary capability in this stop. It builds
on v0.105.0 (HEADERS frame codec) and must be independently trustworthy before v0.107.0 (SETTINGS frame codec) begins.

#### Deliverables

- Acceptance contract: Define the CONTINUATION frame codec state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONTINUATION frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.105.0 (HEADERS frame codec) still passes; no behavior assigned to v0.107.0 (SETTINGS frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.106.0 implementation stop reached. Run pentest for this exact commit.`

### v0.107.0 — SETTINGS frame codec

Status: planned

#### Goal

Deliver **SETTINGS frame codec** as the sole primary capability in this stop. It builds
on v0.106.0 (CONTINUATION frame codec) and must be independently trustworthy before v0.108.0 (SETTINGS syntax, role, directional values, and ACK rules) begins.

#### Deliverables

- Acceptance contract: Define the SETTINGS frame codec state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.106.0 (CONTINUATION frame codec) still passes; no behavior assigned to v0.108.0 (SETTINGS syntax, role, directional values, and ACK rules) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.107.0 implementation stop reached. Run pentest for this exact commit.`

### v0.108.0 — SETTINGS syntax, role, directional values, and ACK rules

Status: planned

#### Goal

Deliver **SETTINGS syntax, role, directional values, and ACK rules** as the sole primary capability in this stop. It builds
on v0.107.0 (SETTINGS frame codec) and must be independently trustworthy before v0.109.0 (PING frame codec) begins.

#### Deliverables

- Acceptance contract: Validate SETTINGS syntax, role/direction, unknown identifiers, duplicate ordering, empty ACK payloads, and pending versus acknowledged local values; store peer advertisements without touching stream, window, encoder, admission, or scheduler state that does not yet exist.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS syntax, role, directional values, and ACK rules contract and all previously implemented relevant behavior have
reproducible evidence; v0.107.0 (SETTINGS frame codec) still passes; no behavior assigned to v0.109.0 (PING frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.108.0 implementation stop reached. Run pentest for this exact commit.`

### v0.109.0 — PING frame codec

Status: planned

#### Goal

Deliver **PING frame codec** as the sole primary capability in this stop. It builds
on v0.108.0 (SETTINGS syntax, role, directional values, and ACK rules) and must be independently trustworthy before v0.110.0 (GOAWAY frame codec) begins.

#### Deliverables

- Acceptance contract: Define the PING frame codec state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PING frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.108.0 (SETTINGS syntax, role, directional values, and ACK rules) still passes; no behavior assigned to v0.110.0 (GOAWAY frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.109.0 implementation stop reached. Run pentest for this exact commit.`

### v0.110.0 — GOAWAY frame codec

Status: planned

#### Goal

Deliver **GOAWAY frame codec** as the sole primary capability in this stop. It builds
on v0.109.0 (PING frame codec) and must be independently trustworthy before v0.111.0 (RST_STREAM frame codec) begins.

#### Deliverables

- Acceptance contract: Define the GOAWAY frame codec state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The GOAWAY frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.109.0 (PING frame codec) still passes; no behavior assigned to v0.111.0 (RST_STREAM frame codec) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.110.0 implementation stop reached. Run pentest for this exact commit.`

### v0.111.0 — RST_STREAM frame codec

Status: planned

#### Goal

Deliver **RST_STREAM frame codec** as the sole primary capability in this stop. It builds
on v0.110.0 (GOAWAY frame codec) and must be independently trustworthy before v0.112.0 (WINDOW_UPDATE codec and checked windows) begins.

#### Deliverables

- Acceptance contract: Define the RST_STREAM frame codec state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RST_STREAM frame codec contract and all previously implemented relevant behavior have
reproducible evidence; v0.110.0 (GOAWAY frame codec) still passes; no behavior assigned to v0.112.0 (WINDOW_UPDATE codec and checked windows) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.111.0 implementation stop reached. Run pentest for this exact commit.`

### v0.112.0 — WINDOW_UPDATE codec and checked windows

Status: planned

#### Goal

Deliver **WINDOW_UPDATE codec and checked windows** as the sole primary capability in this stop. It builds
on v0.111.0 (RST_STREAM frame codec) and must be independently trustworthy before v0.113.0 (Legacy PRIORITY frame handling) begins.

#### Deliverables

- Acceptance contract: Define the WINDOW_UPDATE codec and checked windows state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test WINDOW_UPDATE codec and checked windows and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WINDOW_UPDATE codec and checked windows contract and all previously implemented relevant behavior have
reproducible evidence; v0.111.0 (RST_STREAM frame codec) still passes; no behavior assigned to v0.113.0 (Legacy PRIORITY frame handling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.112.0 implementation stop reached. Run pentest for this exact commit.`

### v0.113.0 — Legacy PRIORITY frame handling

Status: planned

#### Goal

Deliver **Legacy PRIORITY frame handling** as the sole primary capability in this stop. It builds
on v0.112.0 (WINDOW_UPDATE codec and checked windows) and must be independently trustworthy before v0.114.0 (PUSH_PROMISE frame handling) begins.

#### Deliverables

- Acceptance contract: Define the Legacy PRIORITY frame handling state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Legacy PRIORITY frame handling and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Legacy PRIORITY frame handling contract and all previously implemented relevant behavior have
reproducible evidence; v0.112.0 (WINDOW_UPDATE codec and checked windows) still passes; no behavior assigned to v0.114.0 (PUSH_PROMISE frame handling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.113.0 implementation stop reached. Run pentest for this exact commit.`

### v0.114.0 — PUSH_PROMISE frame handling

Status: planned

#### Goal

Deliver **PUSH_PROMISE frame handling** as the sole primary capability in this stop. It builds
on v0.113.0 (Legacy PRIORITY frame handling) and must be independently trustworthy before v0.115.0 (Unknown-frame extension policy) begins.

#### Deliverables

- Acceptance contract: Define the PUSH_PROMISE frame handling state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test PUSH_PROMISE frame handling and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PUSH_PROMISE frame handling contract and all previously implemented relevant behavior have
reproducible evidence; v0.113.0 (Legacy PRIORITY frame handling) still passes; no behavior assigned to v0.115.0 (Unknown-frame extension policy) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.114.0 implementation stop reached. Run pentest for this exact commit.`

### v0.115.0 — Unknown-frame extension policy

Status: planned

#### Goal

Deliver **Unknown-frame extension policy** as the sole primary capability in this stop. It builds
on v0.114.0 (PUSH_PROMISE frame handling) and must be independently trustworthy before v0.116.0 (HTTP/2 stream-identifier rules) begins.

#### Deliverables

- Acceptance contract: Define the Unknown-frame extension policy state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Unknown-frame extension policy and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Unknown-frame extension policy contract and all previously implemented relevant behavior have
reproducible evidence; v0.114.0 (PUSH_PROMISE frame handling) still passes; no behavior assigned to v0.116.0 (HTTP/2 stream-identifier rules) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.115.0 implementation stop reached. Run pentest for this exact commit.`

### v0.116.0 — HTTP/2 stream-identifier rules

Status: planned

#### Goal

Deliver **HTTP/2 stream-identifier rules** as the sole primary capability in this stop. It builds
on v0.115.0 (Unknown-frame extension policy) and must be independently trustworthy before v0.117.0 (Generation-checked stream table and tombstones) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/2 stream-identifier rules state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 stream-identifier rules contract and all previously implemented relevant behavior have
reproducible evidence; v0.115.0 (Unknown-frame extension policy) still passes; no behavior assigned to v0.117.0 (Generation-checked stream table and tombstones) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.116.0 implementation stop reached. Run pentest for this exact commit.`

### v0.117.0 — Generation-checked stream table and tombstones

Status: planned

#### Goal

Deliver **Generation-checked stream table and tombstones** as the sole primary capability in this stop. It builds
on v0.116.0 (HTTP/2 stream-identifier rules) and must be independently trustworthy before v0.118.0 (Exhaustive stream-state graph) begins.

#### Deliverables

- Acceptance contract: Define the Generation-checked stream table and tombstones state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Generation-checked stream table and tombstones and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Generation-checked stream table and tombstones contract and all previously implemented relevant behavior have
reproducible evidence; v0.116.0 (HTTP/2 stream-identifier rules) still passes; no behavior assigned to v0.118.0 (Exhaustive stream-state graph) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.117.0 implementation stop reached. Run pentest for this exact commit.`

### v0.118.0 — Exhaustive stream-state graph

Status: planned

#### Goal

Deliver **Exhaustive stream-state graph** as the sole primary capability in this stop. It builds
on v0.117.0 (Generation-checked stream table and tombstones) and must be independently trustworthy before v0.119.0 (HTTP/2 activation preface, first-SETTINGS, and deadline sequencing) begins.

#### Deliverables

- Acceptance contract: Define the Exhaustive stream-state graph state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Exhaustive stream-state graph and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Exhaustive stream-state graph contract and all previously implemented relevant behavior have
reproducible evidence; v0.117.0 (Generation-checked stream table and tombstones) still passes; no behavior assigned to v0.119.0 (HTTP/2 activation preface, first-SETTINGS, and deadline sequencing) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.118.0 implementation stop reached. Run pentest for this exact commit.`

### v0.119.0 — HTTP/2 activation preface, first-SETTINGS, and deadline sequencing

Status: planned

#### Goal

Deliver **HTTP/2 activation preface, first-SETTINGS, and deadline sequencing** as the sole primary capability in this stop. It builds
on v0.118.0 (Exhaustive stream-state graph) and must be independently trustworthy before v0.120.0 (HTTP/2 frame legality and fragmented-header-block sequencing) begins.

#### Deliverables

- Acceptance contract: Validate the connection preface before frames, require SETTINGS as the first peer frame, apply bounded caller-driven preface/ACK deadlines, and reject frames before activation without publishing connection state.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 activation preface, first-SETTINGS, and deadline sequencing contract and all previously implemented relevant behavior have
reproducible evidence; v0.118.0 (Exhaustive stream-state graph) still passes; no behavior assigned to v0.120.0 (HTTP/2 frame legality and fragmented-header-block sequencing) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.119.0 implementation stop reached. Run pentest for this exact commit.`

### v0.120.0 — HTTP/2 frame legality and fragmented-header-block sequencing

Status: planned

#### Goal

Deliver **HTTP/2 frame legality and fragmented-header-block sequencing** as the sole primary capability in this stop. It builds
on v0.119.0 (HTTP/2 activation preface, first-SETTINGS, and deadline sequencing) and must be independently trustworthy before v0.121.0 (HTTP/2 graceful GOAWAY and bounded shutdown sequencing) begins.

#### Deliverables

- Acceptance contract: Apply the idle/reserved/open/half-closed/closed/unknown stream matrix, allow only one active fragmented header block per connection, reject illegal interleaving, and handle stream-ID exhaustion deterministically.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 frame legality and fragmented-header-block sequencing contract and all previously implemented relevant behavior have
reproducible evidence; v0.119.0 (HTTP/2 activation preface, first-SETTINGS, and deadline sequencing) still passes; no behavior assigned to v0.121.0 (HTTP/2 graceful GOAWAY and bounded shutdown sequencing) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.120.0 implementation stop reached. Run pentest for this exact commit.`

### v0.121.0 — HTTP/2 graceful GOAWAY and bounded shutdown sequencing

Status: planned

#### Goal

Deliver **HTTP/2 graceful GOAWAY and bounded shutdown sequencing** as the sole primary capability in this stop. It builds
on v0.120.0 (HTTP/2 frame legality and fragmented-header-block sequencing) and must be independently trustworthy before v0.122.0 (Atomic HPACK header-block integration) begins.

#### Deliverables

- Acceptance contract: Implement two-stage graceful GOAWAY, exact last-processed-stream classification, no new streams after cutoff, bounded mandatory-control output under backpressure, and deterministic cancellation/EOF shutdown completion.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 graceful GOAWAY and bounded shutdown sequencing contract and all previously implemented relevant behavior have
reproducible evidence; v0.120.0 (HTTP/2 frame legality and fragmented-header-block sequencing) still passes; no behavior assigned to v0.122.0 (Atomic HPACK header-block integration) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.121.0 implementation stop reached. Run pentest for this exact commit.`

### v0.122.0 — Atomic HPACK header-block integration

Status: planned

#### Goal

Deliver **Atomic HPACK header-block integration** as the sole primary capability in this stop. It builds
on v0.121.0 (HTTP/2 graceful GOAWAY and bounded shutdown sequencing) and must be independently trustworthy before v0.123.0 (SETTINGS header-table encoder and header-list policy coupling) begins.

#### Deliverables

- Acceptance contract: Define the Atomic HPACK header-block integration state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Atomic HPACK header-block integration and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Atomic HPACK header-block integration contract and all previously implemented relevant behavior have
reproducible evidence; v0.121.0 (HTTP/2 graceful GOAWAY and bounded shutdown sequencing) still passes; no behavior assigned to v0.123.0 (SETTINGS header-table encoder and header-list policy coupling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.122.0 implementation stop reached. Run pentest for this exact commit.`

### v0.123.0 — SETTINGS header-table encoder and header-list policy coupling

Status: planned

#### Goal

Deliver **SETTINGS header-table encoder and header-list policy coupling** as the sole primary capability in this stop. It builds
on v0.122.0 (Atomic HPACK header-block integration) and must be independently trustworthy before v0.124.0 (Pseudo-field ordering and uniqueness) begins.

#### Deliverables

- Acceptance contract: Apply acknowledged peer HEADER_TABLE_SIZE to the outbound HPACK encoder at legal field-block boundaries; treat peer MAX_HEADER_LIST_SIZE as outbound guidance while preserving independent hard inbound decode limits.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS header-table encoder and header-list policy coupling contract and all previously implemented relevant behavior have
reproducible evidence; v0.122.0 (Atomic HPACK header-block integration) still passes; no behavior assigned to v0.124.0 (Pseudo-field ordering and uniqueness) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.123.0 implementation stop reached. Run pentest for this exact commit.`

### v0.124.0 — Pseudo-field ordering and uniqueness

Status: planned

#### Goal

Deliver **Pseudo-field ordering and uniqueness** as the sole primary capability in this stop. It builds
on v0.123.0 (SETTINGS header-table encoder and header-list policy coupling) and must be independently trustworthy before v0.125.0 (Connection-specific field and TE validation) begins.

#### Deliverables

- Acceptance contract: Define the Pseudo-field ordering and uniqueness state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Pseudo-field ordering and uniqueness and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Pseudo-field ordering and uniqueness contract and all previously implemented relevant behavior have
reproducible evidence; v0.123.0 (SETTINGS header-table encoder and header-list policy coupling) still passes; no behavior assigned to v0.125.0 (Connection-specific field and TE validation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.124.0 implementation stop reached. Run pentest for this exact commit.`

### v0.125.0 — Connection-specific field and TE validation

Status: planned

#### Goal

Deliver **Connection-specific field and TE validation** as the sole primary capability in this stop. It builds
on v0.124.0 (Pseudo-field ordering and uniqueness) and must be independently trustworthy before v0.126.0 (HTTP/2 malformed initial-field-block publication barrier) begins.

#### Deliverables

- Acceptance contract: Define the Connection-specific field and TE validation state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Connection-specific field and TE validation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection-specific field and TE validation contract and all previously implemented relevant behavior have
reproducible evidence; v0.124.0 (Pseudo-field ordering and uniqueness) still passes; no behavior assigned to v0.126.0 (HTTP/2 malformed initial-field-block publication barrier) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.125.0 implementation stop reached. Run pentest for this exact commit.`

### v0.126.0 — HTTP/2 malformed initial-field-block publication barrier

Status: planned

#### Goal

Deliver **HTTP/2 malformed initial-field-block publication barrier** as the sole primary capability in this stop. It builds
on v0.125.0 (Connection-specific field and TE validation) and must be independently trustworthy before v0.127.0 (HTTP/2 request mapping) begins.

#### Deliverables

- Acceptance contract: Reject uppercase names, NUL/CR/LF, forbidden whitespace, invalid or missing context-specific pseudo-fields, and pseudo-fields in trailers before application publication.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 malformed initial-field-block publication barrier contract and all previously implemented relevant behavior have
reproducible evidence; v0.125.0 (Connection-specific field and TE validation) still passes; no behavior assigned to v0.127.0 (HTTP/2 request mapping) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.126.0 implementation stop reached. Run pentest for this exact commit.`

### v0.127.0 — HTTP/2 request mapping

Status: planned

#### Goal

Deliver **HTTP/2 request mapping** as the sole primary capability in this stop. It builds
on v0.126.0 (HTTP/2 malformed initial-field-block publication barrier) and must be independently trustworthy before v0.128.0 (HTTP/2 response mapping) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/2 request mapping state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 request mapping contract and all previously implemented relevant behavior have
reproducible evidence; v0.126.0 (HTTP/2 malformed initial-field-block publication barrier) still passes; no behavior assigned to v0.128.0 (HTTP/2 response mapping) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.127.0 implementation stop reached. Run pentest for this exact commit.`

### v0.128.0 — HTTP/2 response mapping

Status: planned

#### Goal

Deliver **HTTP/2 response mapping** as the sole primary capability in this stop. It builds
on v0.127.0 (HTTP/2 request mapping) and must be independently trustworthy before v0.129.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/2 response mapping state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 response mapping contract and all previously implemented relevant behavior have
reproducible evidence; v0.127.0 (HTTP/2 request mapping) still passes; no behavior assigned to v0.129.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.128.0 implementation stop reached. Run pentest for this exact commit.`

### v0.129.0 — HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation

Status: planned

#### Goal

Deliver **HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation** as the sole primary capability in this stop. It builds
on v0.128.0 (HTTP/2 response mapping) and must be independently trustworthy before v0.130.0 (Informational responses and trailers) begins.

#### Deliverables

- Acceptance contract: Reconcile content-length with DATA octets and enforce final-response, body-forbidden, trailer, DATA-after-trailer, and END_STREAM ordering for requests, responses, and CONNECT.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation contract and all previously implemented relevant behavior have
reproducible evidence; v0.128.0 (HTTP/2 response mapping) still passes; no behavior assigned to v0.130.0 (Informational responses and trailers) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.129.0 implementation stop reached. Run pentest for this exact commit.`

### v0.130.0 — Informational responses and trailers

Status: planned

#### Goal

Deliver **Informational responses and trailers** as the sole primary capability in this stop. It builds
on v0.129.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) and must be independently trustworthy before v0.131.0 (Cookie field combination and Set-Cookie preservation) begins.

#### Deliverables

- Acceptance contract: Define the Informational responses and trailers state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Informational responses and trailers and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Informational responses and trailers contract and all previously implemented relevant behavior have
reproducible evidence; v0.129.0 (HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation) still passes; no behavior assigned to v0.131.0 (Cookie field combination and Set-Cookie preservation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.130.0 implementation stop reached. Run pentest for this exact commit.`

### v0.131.0 — Cookie field combination and Set-Cookie preservation

Status: planned

#### Goal

Deliver **Cookie field combination and Set-Cookie preservation** as the sole primary capability in this stop. It builds
on v0.130.0 (Informational responses and trailers) and must be independently trustworthy before v0.132.0 (Stream flow control) begins.

#### Deliverables

- Acceptance contract: Define the Cookie field combination and Set-Cookie preservation state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Cookie field combination and Set-Cookie preservation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Cookie field combination and Set-Cookie preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.130.0 (Informational responses and trailers) still passes; no behavior assigned to v0.132.0 (Stream flow control) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.131.0 implementation stop reached. Run pentest for this exact commit.`

### v0.132.0 — Stream flow control

Status: planned

#### Goal

Deliver **Stream flow control** as the sole primary capability in this stop. It builds
on v0.131.0 (Cookie field combination and Set-Cookie preservation) and must be independently trustworthy before v0.133.0 (Connection flow control) begins.

#### Deliverables

- Acceptance contract: Define the Stream flow control state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Stream flow control contract and all previously implemented relevant behavior have
reproducible evidence; v0.131.0 (Cookie field combination and Set-Cookie preservation) still passes; no behavior assigned to v0.133.0 (Connection flow control) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.132.0 implementation stop reached. Run pentest for this exact commit.`

### v0.133.0 — Connection flow control

Status: planned

#### Goal

Deliver **Connection flow control** as the sole primary capability in this stop. It builds
on v0.132.0 (Stream flow control) and must be independently trustworthy before v0.134.0 (SETTINGS initial-window active-stream integration and atomic rollback) begins.

#### Deliverables

- Acceptance contract: Define the Connection flow control state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection flow control contract and all previously implemented relevant behavior have
reproducible evidence; v0.132.0 (Stream flow control) still passes; no behavior assigned to v0.134.0 (SETTINGS initial-window active-stream integration and atomic rollback) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.133.0 implementation stop reached. Run pentest for this exact commit.`

### v0.134.0 — SETTINGS initial-window active-stream integration and atomic rollback

Status: planned

#### Goal

Deliver **SETTINGS initial-window active-stream integration and atomic rollback** as the sole primary capability in this stop. It builds
on v0.133.0 (Connection flow control) and must be independently trustworthy before v0.135.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) begins.

#### Deliverables

- Acceptance contract: Apply INITIAL_WINDOW_SIZE deltas to every active stream with checked signed arithmetic and all-or-nothing rollback on overflow; no stream may observe a partial settings transition.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS initial-window active-stream integration and atomic rollback contract and all previously implemented relevant behavior have
reproducible evidence; v0.133.0 (Connection flow control) still passes; no behavior assigned to v0.135.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.134.0 implementation stop reached. Run pentest for this exact commit.`

### v0.135.0 — HTTP/2 body cancellation, reset, and flow-credit lifecycle

Status: planned

#### Goal

Deliver **HTTP/2 body cancellation, reset, and flow-credit lifecycle** as the sole primary capability in this stop. It builds
on v0.134.0 (SETTINGS initial-window active-stream integration and atomic rollback) and must be independently trustworthy before v0.136.0 (SETTINGS outstanding-ACK accounting) begins.

#### Deliverables

- Acceptance contract: Emit at most one RST_STREAM, account discarded DATA credit, tolerate bounded in-flight frames, discard queued output after reset, resolve END_STREAM/GOAWAY/shutdown races, and recycle only after connection effects.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 body cancellation, reset, and flow-credit lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.134.0 (SETTINGS initial-window active-stream integration and atomic rollback) still passes; no behavior assigned to v0.136.0 (SETTINGS outstanding-ACK accounting) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.135.0 implementation stop reached. Run pentest for this exact commit.`

### v0.136.0 — SETTINGS outstanding-ACK accounting

Status: planned

#### Goal

Deliver **SETTINGS outstanding-ACK accounting** as the sole primary capability in this stop. It builds
on v0.135.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) and must be independently trustworthy before v0.137.0 (Bounded stream admission) begins.

#### Deliverables

- Acceptance contract: Define the SETTINGS outstanding-ACK accounting state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS outstanding-ACK accounting contract and all previously implemented relevant behavior have
reproducible evidence; v0.135.0 (HTTP/2 body cancellation, reset, and flow-credit lifecycle) still passes; no behavior assigned to v0.137.0 (Bounded stream admission) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.136.0 implementation stop reached. Run pentest for this exact commit.`

### v0.137.0 — Bounded stream admission

Status: planned

#### Goal

Deliver **Bounded stream admission** as the sole primary capability in this stop. It builds
on v0.136.0 (SETTINGS outstanding-ACK accounting) and must be independently trustworthy before v0.138.0 (SETTINGS max-concurrent-streams admission integration) begins.

#### Deliverables

- Acceptance contract: Define the Bounded stream admission state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Bounded stream admission contract and all previously implemented relevant behavior have
reproducible evidence; v0.136.0 (SETTINGS outstanding-ACK accounting) still passes; no behavior assigned to v0.138.0 (SETTINGS max-concurrent-streams admission integration) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.137.0 implementation stop reached. Run pentest for this exact commit.`

### v0.138.0 — SETTINGS max-concurrent-streams admission integration

Status: planned

#### Goal

Deliver **SETTINGS max-concurrent-streams admission integration** as the sole primary capability in this stop. It builds
on v0.137.0 (Bounded stream admission) and must be independently trustworthy before v0.139.0 (Bounded outbound scheduling) begins.

#### Deliverables

- Acceptance contract: Apply peer MAX_CONCURRENT_STREAMS to local outbound admission and local advertised limits to inbound policy without replacing independent hard stream-table capacity.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS max-concurrent-streams admission integration contract and all previously implemented relevant behavior have
reproducible evidence; v0.137.0 (Bounded stream admission) still passes; no behavior assigned to v0.139.0 (Bounded outbound scheduling) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.138.0 implementation stop reached. Run pentest for this exact commit.`

### v0.139.0 — Bounded outbound scheduling

Status: planned

#### Goal

Deliver **Bounded outbound scheduling** as the sole primary capability in this stop. It builds
on v0.138.0 (SETTINGS max-concurrent-streams admission integration) and must be independently trustworthy before v0.140.0 (SETTINGS max-frame-size outbound integration) begins.

#### Deliverables

- Acceptance contract: Define the Bounded outbound scheduling state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Bounded outbound scheduling contract and all previously implemented relevant behavior have
reproducible evidence; v0.138.0 (SETTINGS max-concurrent-streams admission integration) still passes; no behavior assigned to v0.140.0 (SETTINGS max-frame-size outbound integration) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.139.0 implementation stop reached. Run pentest for this exact commit.`

### v0.140.0 — SETTINGS max-frame-size outbound integration

Status: planned

#### Goal

Deliver **SETTINGS max-frame-size outbound integration** as the sole primary capability in this stop. It builds
on v0.139.0 (Bounded outbound scheduling) and must be independently trustworthy before v0.141.0 (GOAWAY cutoff and retry classification) begins.

#### Deliverables

- Acceptance contract: Apply peer MAX_FRAME_SIZE only to outbound frame segmentation after acknowledgement while retaining independent inbound hard limits and bounded scheduler/output behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS max-frame-size outbound integration contract and all previously implemented relevant behavior have
reproducible evidence; v0.139.0 (Bounded outbound scheduling) still passes; no behavior assigned to v0.141.0 (GOAWAY cutoff and retry classification) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.140.0 implementation stop reached. Run pentest for this exact commit.`

### v0.141.0 — GOAWAY cutoff and retry classification

Status: planned

#### Goal

Deliver **GOAWAY cutoff and retry classification** as the sole primary capability in this stop. It builds
on v0.140.0 (SETTINGS max-frame-size outbound integration) and must be independently trustworthy before v0.142.0 (Server-push lifecycle) begins.

#### Deliverables

- Acceptance contract: Define the GOAWAY cutoff and retry classification state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The GOAWAY cutoff and retry classification contract and all previously implemented relevant behavior have
reproducible evidence; v0.140.0 (SETTINGS max-frame-size outbound integration) still passes; no behavior assigned to v0.142.0 (Server-push lifecycle) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.141.0 implementation stop reached. Run pentest for this exact commit.`

### v0.142.0 — Server-push lifecycle

Status: planned

#### Goal

Deliver **Server-push lifecycle** as the sole primary capability in this stop. It builds
on v0.141.0 (GOAWAY cutoff and retry classification) and must be independently trustworthy before v0.143.0 (ALPN and cleartext prior-knowledge selection) begins.

#### Deliverables

- Acceptance contract: Define the Server-push lifecycle state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Server-push lifecycle and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Server-push lifecycle contract and all previously implemented relevant behavior have
reproducible evidence; v0.141.0 (GOAWAY cutoff and retry classification) still passes; no behavior assigned to v0.143.0 (ALPN and cleartext prior-knowledge selection) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.142.0 implementation stop reached. Run pentest for this exact commit.`

### v0.143.0 — ALPN and cleartext prior-knowledge selection

Status: planned

#### Goal

Deliver **ALPN and cleartext prior-knowledge selection** as the sole primary capability in this stop. It builds
on v0.142.0 (Server-push lifecycle) and must be independently trustworthy before v0.144.0 (Independent HTTP/2 rate and work budgets) begins.

#### Deliverables

- Acceptance contract: Define the ALPN and cleartext prior-knowledge selection state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test ALPN and cleartext prior-knowledge selection and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The ALPN and cleartext prior-knowledge selection contract and all previously implemented relevant behavior have
reproducible evidence; v0.142.0 (Server-push lifecycle) still passes; no behavior assigned to v0.144.0 (Independent HTTP/2 rate and work budgets) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.143.0 implementation stop reached. Run pentest for this exact commit.`

### v0.144.0 — Independent HTTP/2 rate and work budgets

Status: planned

#### Goal

Deliver **Independent HTTP/2 rate and work budgets** as the sole primary capability in this stop. It builds
on v0.143.0 (ALPN and cleartext prior-knowledge selection) and must be independently trustworthy before v0.145.0 (Rapid-reset defenses) begins.

#### Deliverables

- Acceptance contract: Define the Independent HTTP/2 rate and work budgets state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Independent HTTP/2 rate and work budgets contract and all previously implemented relevant behavior have
reproducible evidence; v0.143.0 (ALPN and cleartext prior-knowledge selection) still passes; no behavior assigned to v0.145.0 (Rapid-reset defenses) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.144.0 implementation stop reached. Run pentest for this exact commit.`

### v0.145.0 — Rapid-reset defenses

Status: planned

#### Goal

Deliver **Rapid-reset defenses** as the sole primary capability in this stop. It builds
on v0.144.0 (Independent HTTP/2 rate and work budgets) and must be independently trustworthy before v0.146.0 (SETTINGS amplification defenses) begins.

#### Deliverables

- Acceptance contract: Define the Rapid-reset defenses state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Rapid-reset defenses and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Rapid-reset defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.144.0 (Independent HTTP/2 rate and work budgets) still passes; no behavior assigned to v0.146.0 (SETTINGS amplification defenses) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.145.0 implementation stop reached. Run pentest for this exact commit.`

### v0.146.0 — SETTINGS amplification defenses

Status: planned

#### Goal

Deliver **SETTINGS amplification defenses** as the sole primary capability in this stop. It builds
on v0.145.0 (Rapid-reset defenses) and must be independently trustworthy before v0.147.0 (PING flood defenses) begins.

#### Deliverables

- Acceptance contract: Define the SETTINGS amplification defenses state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The SETTINGS amplification defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.145.0 (Rapid-reset defenses) still passes; no behavior assigned to v0.147.0 (PING flood defenses) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.146.0 implementation stop reached. Run pentest for this exact commit.`

### v0.147.0 — PING flood defenses

Status: planned

#### Goal

Deliver **PING flood defenses** as the sole primary capability in this stop. It builds
on v0.146.0 (SETTINGS amplification defenses) and must be independently trustworthy before v0.148.0 (CONTINUATION bomb defenses) begins.

#### Deliverables

- Acceptance contract: Define the PING flood defenses state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test PING flood defenses and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PING flood defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.146.0 (SETTINGS amplification defenses) still passes; no behavior assigned to v0.148.0 (CONTINUATION bomb defenses) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.147.0 implementation stop reached. Run pentest for this exact commit.`

### v0.148.0 — CONTINUATION bomb defenses

Status: planned

#### Goal

Deliver **CONTINUATION bomb defenses** as the sole primary capability in this stop. It builds
on v0.147.0 (PING flood defenses) and must be independently trustworthy before v0.149.0 (WINDOW_UPDATE churn defenses) begins.

#### Deliverables

- Acceptance contract: Define the CONTINUATION bomb defenses state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test CONTINUATION bomb defenses and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONTINUATION bomb defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.147.0 (PING flood defenses) still passes; no behavior assigned to v0.149.0 (WINDOW_UPDATE churn defenses) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.148.0 implementation stop reached. Run pentest for this exact commit.`

### v0.149.0 — WINDOW_UPDATE churn defenses

Status: planned

#### Goal

Deliver **WINDOW_UPDATE churn defenses** as the sole primary capability in this stop. It builds
on v0.148.0 (CONTINUATION bomb defenses) and must be independently trustworthy before v0.150.0 (Reserved control-output queues) begins.

#### Deliverables

- Acceptance contract: Define the WINDOW_UPDATE churn defenses state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test WINDOW_UPDATE churn defenses and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WINDOW_UPDATE churn defenses contract and all previously implemented relevant behavior have
reproducible evidence; v0.148.0 (CONTINUATION bomb defenses) still passes; no behavior assigned to v0.150.0 (Reserved control-output queues) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.149.0 implementation stop reached. Run pentest for this exact commit.`

### v0.150.0 — Reserved control-output queues

Status: planned

#### Goal

Deliver **Reserved control-output queues** as the sole primary capability in this stop. It builds
on v0.149.0 (WINDOW_UPDATE churn defenses) and must be independently trustworthy before v0.151.0 (HTTP/2 conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Define the Reserved control-output queues state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Reserved control-output queues and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Reserved control-output queues contract and all previously implemented relevant behavior have
reproducible evidence; v0.149.0 (WINDOW_UPDATE churn defenses) still passes; no behavior assigned to v0.151.0 (HTTP/2 conformance audit and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.150.0 implementation stop reached. Run pentest for this exact commit.`

### v0.151.0 — HTTP/2 conformance audit and pentest

Status: planned

#### Goal

Deliver **HTTP/2 conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.150.0 (Reserved control-output queues) and must be independently trustworthy before v0.152.0 (Protocol-neutral HTTP translation representation) begins.

#### Deliverables

- Acceptance contract: Define the HTTP/2 conformance audit and pentest state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7541, RFC 9110, RFC 9113 including verified and held errata dispositions, RFC 9218 where introduced, and the HTTP/2 security considerations.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.150.0 (Reserved control-output queues) still passes; no behavior assigned to v0.152.0 (Protocol-neutral HTTP translation representation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.151.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 4 — Proxy, client, server, and public APIs

Phase contract: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.

### v0.152.0 — Protocol-neutral HTTP translation representation

Status: planned

#### Goal

Deliver **Protocol-neutral HTTP translation representation** as the sole primary capability in this stop. It builds
on v0.151.0 (HTTP/2 conformance audit and pentest) and must be independently trustworthy before v0.153.0 (Effective URI and authority consistency) begins.

#### Deliverables

- Acceptance contract: Define an immutable representation IR for validated source semantics only; it emits no destination bytes and claims no effective-URI, hop-stripping, or framing translation before those prerequisites land.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Protocol-neutral HTTP translation representation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Protocol-neutral HTTP translation representation contract and all previously implemented relevant behavior have
reproducible evidence; v0.151.0 (HTTP/2 conformance audit and pentest) still passes; no behavior assigned to v0.153.0 (Effective URI and authority consistency) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.152.0 implementation stop reached. Run pentest for this exact commit.`

### v0.153.0 — Effective URI and authority consistency

Status: planned

#### Goal

Deliver **Effective URI and authority consistency** as the sole primary capability in this stop. It builds
on v0.152.0 (Protocol-neutral HTTP translation representation) and must be independently trustworthy before v0.154.0 (Connection-field stripping, Via, and cache preservation) begins.

#### Deliverables

- Acceptance contract: Derive scheme, authority, port, path, request-target form, Host/:authority consistency, CONNECT tunnel authority, and end-origin identity without normalization; reject ambiguity before translation IR publication and distinguish syntax, policy, and caller-capacity failures.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Effective URI and authority consistency and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Effective URI and authority consistency contract and all previously implemented relevant behavior have
reproducible evidence; v0.152.0 (Protocol-neutral HTTP translation representation) still passes; no behavior assigned to v0.154.0 (Connection-field stripping, Via, and cache preservation) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.153.0 implementation stop reached. Run pentest for this exact commit.`

### v0.154.0 — Connection-field stripping, Via, and cache preservation

Status: planned

#### Goal

Deliver **Connection-field stripping, Via, and cache preservation** as the sole primary capability in this stop. It builds
on v0.153.0 (Effective URI and authority consistency) and must be independently trustworthy before v0.155.0 (Max-Forwards TRACE and OPTIONS intermediary semantics) begins.

#### Deliverables

- Acceptance contract: Parse Connection option tokens, remove nominated and fixed hop-by-hop fields, preserve field order and required cache metadata, generate/preserve Via under RFC 9110, reject invalid nomination, and publish the stripped representation only after capacity preflight.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Connection-field stripping, Via, and cache preservation and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Connection-field stripping, Via, and cache preservation contract and all previously implemented relevant behavior have
reproducible evidence; v0.153.0 (Effective URI and authority consistency) still passes; no behavior assigned to v0.155.0 (Max-Forwards TRACE and OPTIONS intermediary semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.154.0 implementation stop reached. Run pentest for this exact commit.`

### v0.155.0 — Max-Forwards TRACE and OPTIONS intermediary semantics

Status: planned

#### Goal

Deliver **Max-Forwards TRACE and OPTIONS intermediary semantics** as the sole primary capability in this stop. It builds
on v0.154.0 (Connection-field stripping, Via, and cache preservation) and must be independently trustworthy before v0.156.0 (HTTP/1 TE request-field and trailers forwarding semantics) begins.

#### Deliverables

- Acceptance contract: Parse one valid Max-Forwards value, decrement on forwarded TRACE/OPTIONS, handle zero locally by role, define malformed/duplicate disposition, and preserve or ignore it correctly for other methods.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Max-Forwards TRACE and OPTIONS intermediary semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.154.0 (Connection-field stripping, Via, and cache preservation) still passes; no behavior assigned to v0.156.0 (HTTP/1 TE request-field and trailers forwarding semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.155.0 implementation stop reached. Run pentest for this exact commit.`

### v0.156.0 — HTTP/1 TE request-field and trailers forwarding semantics

Status: planned

#### Goal

Deliver **HTTP/1 TE request-field and trailers forwarding semantics** as the sole primary capability in this stop. It builds
on v0.155.0 (Max-Forwards TRACE and OPTIONS intermediary semantics) and must be independently trustworthy before v0.157.0 (Normative HTTP/1 and HTTP/2 translation matrix) begins.

#### Deliverables

- Acceptance contract: Treat TE as a request field distinct from Transfer-Encoding, accept only trailers where required, enforce Connection: TE nomination in HTTP/1 forwarding, and map TE: trailers safely across HTTP versions.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/1 TE request-field and trailers forwarding semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.155.0 (Max-Forwards TRACE and OPTIONS intermediary semantics) still passes; no behavior assigned to v0.157.0 (Normative HTTP/1 and HTTP/2 translation matrix) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.156.0 implementation stop reached. Run pentest for this exact commit.`

### v0.157.0 — Normative HTTP/1 and HTTP/2 translation matrix

Status: planned

#### Goal

Deliver **Normative HTTP/1 and HTTP/2 translation matrix** as the sole primary capability in this stop. It builds
on v0.156.0 (HTTP/1 TE request-field and trailers forwarding semantics) and must be independently trustworthy before v0.158.0 (CONNECT translation across HTTP versions) begins.

#### Deliverables

- Acceptance contract: Map target/Host to pseudo-fields, status, Content-Length/DATA/trailers/END_STREAM, TE: trailers, connection fields, Cookie/Set-Cookie, informational/HEAD/body-forbidden responses, CONNECT/Upgrade, and close-delimited reframing; validate the complete destination head/framing decision before emitting bytes.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test every matrix cell in both directions, including rejection, reframing, partial output, capacity exhaustion, cancellation, and zero destination bytes before full validation.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Normative HTTP/1 and HTTP/2 translation matrix contract and all previously implemented relevant behavior have
reproducible evidence; v0.156.0 (HTTP/1 TE request-field and trailers forwarding semantics) still passes; no behavior assigned to v0.158.0 (CONNECT translation across HTTP versions) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.157.0 implementation stop reached. Run pentest for this exact commit.`

### v0.158.0 — CONNECT translation across HTTP versions

Status: planned

#### Goal

Deliver **CONNECT translation across HTTP versions** as the sole primary capability in this stop. It builds
on v0.157.0 (Normative HTTP/1 and HTTP/2 translation matrix) and must be independently trustworthy before v0.159.0 (RFC 8441 extended CONNECT) begins.

#### Deliverables

- Acceptance contract: Define the CONNECT translation across HTTP versions state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test CONNECT translation across HTTP versions and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The CONNECT translation across HTTP versions contract and all previously implemented relevant behavior have
reproducible evidence; v0.157.0 (Normative HTTP/1 and HTTP/2 translation matrix) still passes; no behavior assigned to v0.159.0 (RFC 8441 extended CONNECT) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.158.0 implementation stop reached. Run pentest for this exact commit.`

### v0.159.0 — RFC 8441 extended CONNECT

Status: planned

#### Goal

Deliver **RFC 8441 extended CONNECT** as the sole primary capability in this stop. It builds
on v0.158.0 (CONNECT translation across HTTP versions) and must be independently trustworthy before v0.160.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) begins.

#### Deliverables

- Acceptance contract: Define the RFC 8441 extended CONNECT state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test RFC 8441 extended CONNECT and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The RFC 8441 extended CONNECT contract and all previously implemented relevant behavior have
reproducible evidence; v0.158.0 (CONNECT translation across HTTP versions) still passes; no behavior assigned to v0.160.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.159.0 implementation stop reached. Run pentest for this exact commit.`

### v0.160.0 — WebSocket HTTP/1 to HTTP/2 handshake bridge

Status: planned

#### Goal

Deliver **WebSocket HTTP/1 to HTTP/2 handshake bridge** as the sole primary capability in this stop. It builds
on v0.159.0 (RFC 8441 extended CONNECT) and must be independently trustworthy before v0.161.0 (Structured Fields bounded bare-item parser) begins.

#### Deliverables

- Acceptance contract: Define the WebSocket HTTP/1 to HTTP/2 handshake bridge state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The WebSocket HTTP/1 to HTTP/2 handshake bridge contract and all previously implemented relevant behavior have
reproducible evidence; v0.159.0 (RFC 8441 extended CONNECT) still passes; no behavior assigned to v0.161.0 (Structured Fields bounded bare-item parser) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.160.0 implementation stop reached. Run pentest for this exact commit.`

### v0.161.0 — Structured Fields bounded bare-item parser

Status: planned

#### Goal

Deliver **Structured Fields bounded bare-item parser** as the sole primary capability in this stop. It builds
on v0.160.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) and must be independently trustworthy before v0.162.0 (Structured Fields integer and decimal ranges) begins.

#### Deliverables

- Acceptance contract: Incrementally parse one bounded RFC 9651 bare item from bytes with explicit type, consumed length, NeedInput, capacity, and syntax errors and no locale or UTF-8 assumptions beyond each item grammar.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields bounded bare-item parser contract and all previously implemented relevant behavior have
reproducible evidence; v0.160.0 (WebSocket HTTP/1 to HTTP/2 handshake bridge) still passes; no behavior assigned to v0.162.0 (Structured Fields integer and decimal ranges) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.161.0 implementation stop reached. Run pentest for this exact commit.`

### v0.162.0 — Structured Fields integer and decimal ranges

Status: planned

#### Goal

Deliver **Structured Fields integer and decimal ranges** as the sole primary capability in this stop. It builds
on v0.161.0 (Structured Fields bounded bare-item parser) and must be independently trustworthy before v0.163.0 (Structured Fields strings, tokens, bytes, booleans, dates, and display strings) begins.

#### Deliverables

- Acceptance contract: Enforce exact RFC 9651 integer/decimal digit, sign, scale, and numeric ranges with checked arithmetic, canonical internal values, and overflow distinguished from malformed syntax.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields integer and decimal ranges contract and all previously implemented relevant behavior have
reproducible evidence; v0.161.0 (Structured Fields bounded bare-item parser) still passes; no behavior assigned to v0.163.0 (Structured Fields strings, tokens, bytes, booleans, dates, and display strings) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.162.0 implementation stop reached. Run pentest for this exact commit.`

### v0.163.0 — Structured Fields strings, tokens, bytes, booleans, dates, and display strings

Status: planned

#### Goal

Deliver **Structured Fields strings, tokens, bytes, booleans, dates, and display strings** as the sole primary capability in this stop. It builds
on v0.162.0 (Structured Fields integer and decimal ranges) and must be independently trustworthy before v0.164.0 (Structured Fields parameters) begins.

#### Deliverables

- Acceptance contract: Implement each remaining bare-item grammar, escape/base64/date validation, display-string decoding policy, exact limits, and type-specific errors without automatic coercion.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields strings, tokens, bytes, booleans, dates, and display strings contract and all previously implemented relevant behavior have
reproducible evidence; v0.162.0 (Structured Fields integer and decimal ranges) still passes; no behavior assigned to v0.164.0 (Structured Fields parameters) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.163.0 implementation stop reached. Run pentest for this exact commit.`

### v0.164.0 — Structured Fields parameters

Status: planned

#### Goal

Deliver **Structured Fields parameters** as the sole primary capability in this stop. It builds
on v0.163.0 (Structured Fields strings, tokens, bytes, booleans, dates, and display strings) and must be independently trustworthy before v0.165.0 (Structured Fields inner lists and lists) begins.

#### Deliverables

- Acceptance contract: Parse ordered unique parameter keys and values with caller-owned capacity, duplicate policy, incremental boundaries, and canonical parameter serialization prerequisites.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields parameters contract and all previously implemented relevant behavior have
reproducible evidence; v0.163.0 (Structured Fields strings, tokens, bytes, booleans, dates, and display strings) still passes; no behavior assigned to v0.165.0 (Structured Fields inner lists and lists) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.164.0 implementation stop reached. Run pentest for this exact commit.`

### v0.165.0 — Structured Fields inner lists and lists

Status: planned

#### Goal

Deliver **Structured Fields inner lists and lists** as the sole primary capability in this stop. It builds
on v0.164.0 (Structured Fields parameters) and must be independently trustworthy before v0.166.0 (Structured Fields dictionaries) begins.

#### Deliverables

- Acceptance contract: Parse bounded inner lists and top-level lists with whitespace rules, item/parameter ownership, nesting fixed by grammar, and independent member/work limits.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields inner lists and lists contract and all previously implemented relevant behavior have
reproducible evidence; v0.164.0 (Structured Fields parameters) still passes; no behavior assigned to v0.166.0 (Structured Fields dictionaries) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.165.0 implementation stop reached. Run pentest for this exact commit.`

### v0.166.0 — Structured Fields dictionaries

Status: planned

#### Goal

Deliver **Structured Fields dictionaries** as the sole primary capability in this stop. It builds
on v0.165.0 (Structured Fields inner lists and lists) and must be independently trustworthy before v0.167.0 (Structured Fields canonical serialization) begins.

#### Deliverables

- Acceptance contract: Parse ordered dictionary members with duplicate-key disposition, implicit booleans, inner-list values, parameters, and independent count/work limits.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields dictionaries contract and all previously implemented relevant behavior have
reproducible evidence; v0.165.0 (Structured Fields inner lists and lists) still passes; no behavior assigned to v0.167.0 (Structured Fields canonical serialization) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.166.0 implementation stop reached. Run pentest for this exact commit.`

### v0.167.0 — Structured Fields canonical serialization

Status: planned

#### Goal

Deliver **Structured Fields canonical serialization** as the sole primary capability in this stop. It builds
on v0.166.0 (Structured Fields dictionaries) and must be independently trustworthy before v0.168.0 (Structured Fields incremental parsing and caller-owned storage) begins.

#### Deliverables

- Acceptance contract: Serialize every item/list/dictionary type in canonical RFC 9651 form under partial output, with size preflight and no state advancement before bytes commit.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields canonical serialization contract and all previously implemented relevant behavior have
reproducible evidence; v0.166.0 (Structured Fields dictionaries) still passes; no behavior assigned to v0.168.0 (Structured Fields incremental parsing and caller-owned storage) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.167.0 implementation stop reached. Run pentest for this exact commit.`

### v0.168.0 — Structured Fields incremental parsing and caller-owned storage

Status: planned

#### Goal

Deliver **Structured Fields incremental parsing and caller-owned storage** as the sole primary capability in this stop. It builds
on v0.167.0 (Structured Fields canonical serialization) and must be independently trustworthy before v0.169.0 (Structured Fields malformed-input and complexity limits) begins.

#### Deliverables

- Acceptance contract: Bind all parsers to borrowed input and caller-provided stores, preserve progress across every byte split, acknowledge published values before reuse, and expose NeedInput/NeedOutput/CapacityExceeded distinctly.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields incremental parsing and caller-owned storage contract and all previously implemented relevant behavior have
reproducible evidence; v0.167.0 (Structured Fields canonical serialization) still passes; no behavior assigned to v0.169.0 (Structured Fields malformed-input and complexity limits) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.168.0 implementation stop reached. Run pentest for this exact commit.`

### v0.169.0 — Structured Fields malformed-input and complexity limits

Status: planned

#### Goal

Deliver **Structured Fields malformed-input and complexity limits** as the sole primary capability in this stop. It builds
on v0.168.0 (Structured Fields incremental parsing and caller-owned storage) and must be independently trustworthy before v0.170.0 (Priority field semantics) begins.

#### Deliverables

- Acceptance contract: Build malformed and differential corpora; cap token/string/base64/member/parameter bytes and work so duplicate checks, lookup, and one-byte fragmentation remain non-quadratic.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Structured Fields malformed-input and complexity limits contract and all previously implemented relevant behavior have
reproducible evidence; v0.168.0 (Structured Fields incremental parsing and caller-owned storage) still passes; no behavior assigned to v0.170.0 (Priority field semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.169.0 implementation stop reached. Run pentest for this exact commit.`

### v0.170.0 — Priority field semantics

Status: planned

#### Goal

Deliver **Priority field semantics** as the sole primary capability in this stop. It builds
on v0.169.0 (Structured Fields malformed-input and complexity limits) and must be independently trustworthy before v0.171.0 (Priority scheduling hints and fairness) begins.

#### Deliverables

- Acceptance contract: Map RFC 9218 urgency and incremental parameters through the Structured Fields API, apply defaults and invalid-field handling, and separate advisory priority from protocol correctness.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Priority field semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.169.0 (Structured Fields malformed-input and complexity limits) still passes; no behavior assigned to v0.171.0 (Priority scheduling hints and fairness) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.170.0 implementation stop reached. Run pentest for this exact commit.`

### v0.171.0 — Priority scheduling hints and fairness

Status: planned

#### Goal

Deliver **Priority scheduling hints and fairness** as the sole primary capability in this stop. It builds
on v0.170.0 (Priority field semantics) and must be independently trustworthy before v0.172.0 (Priority intermediary behavior) begins.

#### Deliverables

- Acceptance contract: Feed validated priority hints into bounded scheduling with starvation prevention, deterministic tie-breaking, reprioritization cost limits, and no peer-controlled unbounded queue movement.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Priority scheduling hints and fairness contract and all previously implemented relevant behavior have
reproducible evidence; v0.170.0 (Priority field semantics) still passes; no behavior assigned to v0.172.0 (Priority intermediary behavior) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.171.0 implementation stop reached. Run pentest for this exact commit.`

### v0.172.0 — Priority intermediary behavior

Status: planned

#### Goal

Deliver **Priority intermediary behavior** as the sole primary capability in this stop. It builds
on v0.171.0 (Priority scheduling hints and fairness) and must be independently trustworthy before v0.173.0 (PRIORITY_UPDATE frame support) begins.

#### Deliverables

- Acceptance contract: Define when intermediaries consume, forward, regenerate, or ignore Priority fields and how local policy overrides are represented without misreporting upstream choices.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Priority intermediary behavior contract and all previously implemented relevant behavior have
reproducible evidence; v0.171.0 (Priority scheduling hints and fairness) still passes; no behavior assigned to v0.173.0 (PRIORITY_UPDATE frame support) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.172.0 implementation stop reached. Run pentest for this exact commit.`

### v0.173.0 — PRIORITY_UPDATE frame support

Status: planned

#### Goal

Deliver **PRIORITY_UPDATE frame support** as the sole primary capability in this stop. It builds
on v0.172.0 (Priority intermediary behavior) and must be independently trustworthy before v0.174.0 (Priority update flood budgeting) begins.

#### Deliverables

- Acceptance contract: Validate element types/IDs and Structured Field values, apply updates only to eligible requests, ignore or error by RFC scope, and bound state for nonexistent/closed streams.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test PRIORITY_UPDATE frame support and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The PRIORITY_UPDATE frame support contract and all previously implemented relevant behavior have
reproducible evidence; v0.172.0 (Priority intermediary behavior) still passes; no behavior assigned to v0.174.0 (Priority update flood budgeting) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.173.0 implementation stop reached. Run pentest for this exact commit.`

### v0.174.0 — Priority update flood budgeting

Status: planned

#### Goal

Deliver **Priority update flood budgeting** as the sole primary capability in this stop. It builds
on v0.173.0 (PRIORITY_UPDATE frame support) and must be independently trustworthy before v0.175.0 (Client request builder and target forms) begins.

#### Deliverables

- Acceptance contract: Rate-limit parse work, queued updates, scheduler mutations, and response/control amplification independently while preserving connection progress for non-priority frames.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Add RFC vectors, every-byte splits, malformed/capacity corpora, canonical round trips, and work-limit assertions for this exact grammar or priority surface.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Priority update flood budgeting contract and all previously implemented relevant behavior have
reproducible evidence; v0.173.0 (PRIORITY_UPDATE frame support) still passes; no behavior assigned to v0.175.0 (Client request builder and target forms) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.174.0 implementation stop reached. Run pentest for this exact commit.`

### v0.175.0 — Client request builder and target forms

Status: planned

#### Goal

Deliver **Client request builder and target forms** as the sole primary capability in this stop. It builds
on v0.174.0 (Priority update flood budgeting) and must be independently trustworthy before v0.176.0 (Client correlation, cancellation, and retry tokens) begins.

#### Deliverables

- Acceptance contract: Build origin-, absolute-, authority-, and asterisk-form requests with method coherence, validated Host/authority, ordered fields, sensitive-indexing metadata, exact body framing, injection-proof serialization, and capacity failure before any request token or bytes are published.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Client request builder and target forms and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Client request builder and target forms contract and all previously implemented relevant behavior have
reproducible evidence; v0.174.0 (Priority update flood budgeting) still passes; no behavior assigned to v0.176.0 (Client correlation, cancellation, and retry tokens) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.175.0 implementation stop reached. Run pentest for this exact commit.`

### v0.176.0 — Client correlation, cancellation, and retry tokens

Status: planned

#### Goal

Deliver **Client correlation, cancellation, and retry tokens** as the sole primary capability in this stop. It builds
on v0.175.0 (Client request builder and target forms) and must be independently trustworthy before v0.177.0 (Retry safety, idempotency, and body-replayability contract) begins.

#### Deliverables

- Acceptance contract: Assign one generation-safe request token; correlate informational/final responses, body/trailers, cancellation, reset, GOAWAY, and connection loss; classify possibly-unprocessed separately from replay safety and publish no duplicate terminal event.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Client correlation, cancellation, and retry tokens and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Client correlation, cancellation, and retry tokens contract and all previously implemented relevant behavior have
reproducible evidence; v0.175.0 (Client request builder and target forms) still passes; no behavior assigned to v0.177.0 (Retry safety, idempotency, and body-replayability contract) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.176.0 implementation stop reached. Run pentest for this exact commit.`

### v0.177.0 — Retry safety, idempotency, and body-replayability contract

Status: planned

#### Goal

Deliver **Retry safety, idempotency, and body-replayability contract** as the sole primary capability in this stop. It builds
on v0.176.0 (Client correlation, cancellation, and retry tokens) and must be independently trustworthy before v0.178.0 (Origin-server role API) begins.

#### Deliverables

- Acceptance contract: Define the Retry safety, idempotency, and body-replayability contract state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Retry safety, idempotency, and body-replayability contract and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Retry safety, idempotency, and body-replayability contract contract and all previously implemented relevant behavior have
reproducible evidence; v0.176.0 (Client correlation, cancellation, and retry tokens) still passes; no behavior assigned to v0.178.0 (Origin-server role API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.177.0 implementation stop reached. Run pentest for this exact commit.`

### v0.178.0 — Origin-server role API

Status: planned

#### Goal

Deliver **Origin-server role API** as the sole primary capability in this stop. It builds
on v0.177.0 (Retry safety, idempotency, and body-replayability contract) and must be independently trustworthy before v0.179.0 (Forward-proxy role API) begins.

#### Deliverables

- Acceptance contract: Publish a request only after head/framing validation, correlate exactly one response lifecycle, enforce 100-continue and body-rejection/drain-or-close decisions, reserve mandatory error output, and complete or cancel storage ownership before connection reuse.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Origin-server role API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Origin-server role API contract and all previously implemented relevant behavior have
reproducible evidence; v0.177.0 (Retry safety, idempotency, and body-replayability contract) still passes; no behavior assigned to v0.179.0 (Forward-proxy role API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.178.0 implementation stop reached. Run pentest for this exact commit.`

### v0.179.0 — Forward-proxy role API

Status: planned

#### Goal

Deliver **Forward-proxy role API** as the sole primary capability in this stop. It builds
on v0.178.0 (Origin-server role API) and must be independently trustworthy before v0.180.0 (Reverse-proxy and gateway role API) begins.

#### Deliverables

- Acceptance contract: Validate absolute-form/effective URI and Host, Max-Forwards, TE, Via, hop stripping, cache preservation, CONNECT, translation, upstream capacity/error disposition, and replayability metadata before forwarding any head or tunnel bytes.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Forward-proxy role API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Forward-proxy role API contract and all previously implemented relevant behavior have
reproducible evidence; v0.178.0 (Origin-server role API) still passes; no behavior assigned to v0.180.0 (Reverse-proxy and gateway role API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.179.0 implementation stop reached. Run pentest for this exact commit.`

### v0.180.0 — Reverse-proxy and gateway role API

Status: planned

#### Goal

Deliver **Reverse-proxy and gateway role API** as the sole primary capability in this stop. It builds
on v0.179.0 (Forward-proxy role API) and must be independently trustworthy before v0.181.0 (Tunnel lifecycle and half-close semantics) begins.

#### Deliverables

- Acceptance contract: Separate downstream authority from configured upstream authority, validate and reserialize through the translation matrix, preserve response ordering/cache metadata, map upstream failure to typed gateway actions, and never leak partial upstream/downstream state across requests.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Reverse-proxy and gateway role API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Reverse-proxy and gateway role API contract and all previously implemented relevant behavior have
reproducible evidence; v0.179.0 (Forward-proxy role API) still passes; no behavior assigned to v0.181.0 (Tunnel lifecycle and half-close semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.180.0 implementation stop reached. Run pentest for this exact commit.`

### v0.181.0 — Tunnel lifecycle and half-close semantics

Status: planned

#### Goal

Deliver **Tunnel lifecycle and half-close semantics** as the sole primary capability in this stop. It builds
on v0.180.0 (Reverse-proxy and gateway role API) and must be independently trustworthy before v0.182.0 (Upgrade transformation boundary) begins.

#### Deliverables

- Acceptance contract: Model pending, committed, bidirectional, local-half-closed, peer-half-closed, cancelling, and closed tunnel states with bounded buffers, one owner per direction, explicit cancellation, EOF, TLS close_notify, and mandatory-close outcomes.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Tunnel lifecycle and half-close semantics and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Tunnel lifecycle and half-close semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.180.0 (Reverse-proxy and gateway role API) still passes; no behavior assigned to v0.182.0 (Upgrade transformation boundary) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.181.0 implementation stop reached. Run pentest for this exact commit.`

### v0.182.0 — Upgrade transformation boundary

Status: planned

#### Goal

Deliver **Upgrade transformation boundary** as the sole primary capability in this stop. It builds
on v0.181.0 (Tunnel lifecycle and half-close semantics) and must be independently trustworthy before v0.183.0 (Exact CONNECT, Upgrade, and tunnel byte-handoff ownership) begins.

#### Deliverables

- Acceptance contract: Transform only a fully validated Upgrade request/101 response pair, preserve selected protocol and negotiation metadata, emit no destination or post-transition bytes before commit, and reject unsupported cross-version upgrades with an HTTP-framed close action.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Upgrade transformation boundary and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Upgrade transformation boundary contract and all previously implemented relevant behavior have
reproducible evidence; v0.181.0 (Tunnel lifecycle and half-close semantics) still passes; no behavior assigned to v0.183.0 (Exact CONNECT, Upgrade, and tunnel byte-handoff ownership) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.182.0 implementation stop reached. Run pentest for this exact commit.`

### v0.183.0 — Exact CONNECT, Upgrade, and tunnel byte-handoff ownership

Status: planned

#### Goal

Deliver **Exact CONNECT, Upgrade, and tunnel byte-handoff ownership** as the sole primary capability in this stop. It builds
on v0.182.0 (Upgrade transformation boundary) and must be independently trustworthy before v0.184.0 (GOAWAY, 421, and retry coordination) begins.

#### Deliverables

- Acceptance contract: Stop at the precise committed transition boundary, return over-read bytes unchanged/in order, never parse post-transition bytes as HTTP, keep failure bytes under HTTP framing, distinguish half-close/cancel/close_notify/EOF, and transfer ownership exactly once.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Exact CONNECT, Upgrade, and tunnel byte-handoff ownership and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Exact CONNECT, Upgrade, and tunnel byte-handoff ownership contract and all previously implemented relevant behavior have
reproducible evidence; v0.182.0 (Upgrade transformation boundary) still passes; no behavior assigned to v0.184.0 (GOAWAY, 421, and retry coordination) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.183.0 implementation stop reached. Run pentest for this exact commit.`

### v0.184.0 — GOAWAY, 421, and retry coordination

Status: planned

#### Goal

Deliver **GOAWAY, 421, and retry coordination** as the sole primary capability in this stop. It builds
on v0.183.0 (Exact CONNECT, Upgrade, and tunnel byte-handoff ownership) and must be independently trustworthy before v0.185.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) begins.

#### Deliverables

- Acceptance contract: Define the GOAWAY, 421, and retry coordination state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The GOAWAY, 421, and retry coordination contract and all previously implemented relevant behavior have
reproducible evidence; v0.183.0 (Exact CONNECT, Upgrade, and tunnel byte-handoff ownership) still passes; no behavior assigned to v0.185.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.184.0 implementation stop reached. Run pentest for this exact commit.`

### v0.185.0 — Authenticated origin authorization and HTTP/2 coalescing metadata

Status: planned

#### Goal

Deliver **Authenticated origin authorization and HTTP/2 coalescing metadata** as the sole primary capability in this stop. It builds
on v0.184.0 (GOAWAY, 421, and retry coordination) and must be independently trustworthy before v0.186.0 (Fixed-capacity caller-storage public API) begins.

#### Deliverables

- Acceptance contract: Define the Authenticated origin authorization and HTTP/2 coalescing metadata state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Authenticated origin authorization and HTTP/2 coalescing metadata contract and all previously implemented relevant behavior have
reproducible evidence; v0.184.0 (GOAWAY, 421, and retry coordination) still passes; no behavior assigned to v0.186.0 (Fixed-capacity caller-storage public API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.185.0 implementation stop reached. Run pentest for this exact commit.`

### v0.186.0 — Fixed-capacity caller-storage public API

Status: planned

#### Goal

Deliver **Fixed-capacity caller-storage public API** as the sole primary capability in this stop. It builds
on v0.185.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) and must be independently trustworthy before v0.187.0 (Optional alloc-backed convenience API) begins.

#### Deliverables

- Acceptance contract: Stabilize borrowed/fixed-capacity APIs first, including acknowledgements, lifetimes, explicit capacity errors, and proof that protocol correctness needs no allocator.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Fixed-capacity caller-storage public API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Fixed-capacity caller-storage public API contract and all previously implemented relevant behavior have
reproducible evidence; v0.185.0 (Authenticated origin authorization and HTTP/2 coalescing metadata) still passes; no behavior assigned to v0.187.0 (Optional alloc-backed convenience API) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.186.0 implementation stop reached. Run pentest for this exact commit.`

### v0.187.0 — Optional alloc-backed convenience API

Status: planned

#### Goal

Deliver **Optional alloc-backed convenience API** as the sole primary capability in this stop. It builds
on v0.186.0 (Fixed-capacity caller-storage public API) and must be independently trustworthy before v0.188.0 (Stable diagnostics and security events) begins.

#### Deliverables

- Acceptance contract: Build the owned layer only as a wrapper reducible to the stable borrowed API, with identical protocol decisions and no alloc-only correctness path.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Optional alloc-backed convenience API and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Optional alloc-backed convenience API contract and all previously implemented relevant behavior have
reproducible evidence; v0.186.0 (Fixed-capacity caller-storage public API) still passes; no behavior assigned to v0.188.0 (Stable diagnostics and security events) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.187.0 implementation stop reached. Run pentest for this exact commit.`

### v0.188.0 — Stable diagnostics and security events

Status: planned

#### Goal

Deliver **Stable diagnostics and security events** as the sole primary capability in this stop. It builds
on v0.187.0 (Optional alloc-backed convenience API) and must be independently trustworthy before v0.189.0 (Feature and dependency-policy surface) begins.

#### Deliverables

- Acceptance contract: Define the Stable diagnostics and security events state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Stable diagnostics and security events and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Stable diagnostics and security events contract and all previously implemented relevant behavior have
reproducible evidence; v0.187.0 (Optional alloc-backed convenience API) still passes; no behavior assigned to v0.189.0 (Feature and dependency-policy surface) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.188.0 implementation stop reached. Run pentest for this exact commit.`

### v0.189.0 — Feature and dependency-policy surface

Status: planned

#### Goal

Deliver **Feature and dependency-policy surface** as the sole primary capability in this stop. It builds
on v0.188.0 (Stable diagnostics and security events) and must be independently trustworthy before v0.190.0 (Multi-implementation interoperability) begins.

#### Deliverables

- Acceptance contract: Define the Feature and dependency-policy surface state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Feature and dependency-policy surface and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Feature and dependency-policy surface contract and all previously implemented relevant behavior have
reproducible evidence; v0.188.0 (Stable diagnostics and security events) still passes; no behavior assigned to v0.190.0 (Multi-implementation interoperability) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.189.0 implementation stop reached. Run pentest for this exact commit.`

### v0.190.0 — Multi-implementation interoperability

Status: planned

#### Goal

Deliver **Multi-implementation interoperability** as the sole primary capability in this stop. It builds
on v0.189.0 (Feature and dependency-policy surface) and must be independently trustworthy before v0.191.0 (Adversarial and stateful fuzz campaign) begins.

#### Deliverables

- Acceptance contract: Define the Multi-implementation interoperability state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Multi-implementation interoperability and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Multi-implementation interoperability contract and all previously implemented relevant behavior have
reproducible evidence; v0.189.0 (Feature and dependency-policy surface) still passes; no behavior assigned to v0.191.0 (Adversarial and stateful fuzz campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.190.0 implementation stop reached. Run pentest for this exact commit.`

### v0.191.0 — Adversarial and stateful fuzz campaign

Status: planned

#### Goal

Deliver **Adversarial and stateful fuzz campaign** as the sole primary capability in this stop. It builds
on v0.190.0 (Multi-implementation interoperability) and must be independently trustworthy before v0.192.0 (Compile-fail state and lifetime tests) begins.

#### Deliverables

- Acceptance contract: Define the Adversarial and stateful fuzz campaign state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Adversarial and stateful fuzz campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Adversarial and stateful fuzz campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.190.0 (Multi-implementation interoperability) still passes; no behavior assigned to v0.192.0 (Compile-fail state and lifetime tests) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.191.0 implementation stop reached. Run pentest for this exact commit.`

### v0.192.0 — Compile-fail state and lifetime tests

Status: planned

#### Goal

Deliver **Compile-fail state and lifetime tests** as the sole primary capability in this stop. It builds
on v0.191.0 (Adversarial and stateful fuzz campaign) and must be independently trustworthy before v0.193.0 (Long-running soak and exhaustion campaign) begins.

#### Deliverables

- Acceptance contract: Define the Compile-fail state and lifetime tests state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Compile-fail state and lifetime tests and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Compile-fail state and lifetime tests contract and all previously implemented relevant behavior have
reproducible evidence; v0.191.0 (Adversarial and stateful fuzz campaign) still passes; no behavior assigned to v0.193.0 (Long-running soak and exhaustion campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.192.0 implementation stop reached. Run pentest for this exact commit.`

### v0.193.0 — Long-running soak and exhaustion campaign

Status: planned

#### Goal

Deliver **Long-running soak and exhaustion campaign** as the sole primary capability in this stop. It builds
on v0.192.0 (Compile-fail state and lifetime tests) and must be independently trustworthy before v0.194.0 (Role and API conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Define the Long-running soak and exhaustion campaign state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Long-running soak and exhaustion campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Long-running soak and exhaustion campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.192.0 (Compile-fail state and lifetime tests) still passes; no behavior assigned to v0.194.0 (Role and API conformance audit and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.193.0 implementation stop reached. Run pentest for this exact commit.`

### v0.194.0 — Role and API conformance audit and pentest

Status: planned

#### Goal

Deliver **Role and API conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.193.0 (Long-running soak and exhaustion campaign) and must be independently trustworthy before v0.195.0 (Standard blocking-stream adapter) begins.

#### Deliverables

- Acceptance contract: Define the Role and API conformance audit and pentest state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 3986, RFC 8441, RFC 9110 including Via, Max-Forwards, and TE, RFC 9111, RFC 9112, RFC 9113, RFC 9218, RFC 9651, and RFC 9931; RFC 7239 Forwarded transformation remains out of scope.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Role and API conformance audit and pentest and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Role and API conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.193.0 (Long-running soak and exhaustion campaign) still passes; no behavior assigned to v0.195.0 (Standard blocking-stream adapter) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.194.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 5 — OS, Aesynx readiness, and 1.0 evidence

Phase contract: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.

### v0.195.0 — Standard blocking-stream adapter

Status: planned

#### Goal

Deliver **Standard blocking-stream adapter** as the sole primary capability in this stop. It builds
on v0.194.0 (Role and API conformance audit and pentest) and must be independently trustworthy before v0.196.0 (Standard nonblocking-stream adapter) begins.

#### Deliverables

- Acceptance contract: Map short reads/writes, interruption, clean/truncated EOF, scalar/vectored operation, cancellation, partial output, and mandatory-close actions without hidden buffering or protocol reinterpretation.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Standard blocking-stream adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.194.0 (Role and API conformance audit and pentest) still passes; no behavior assigned to v0.196.0 (Standard nonblocking-stream adapter) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.195.0 implementation stop reached. Run pentest for this exact commit.`

### v0.196.0 — Standard nonblocking-stream adapter

Status: planned

#### Goal

Deliver **Standard nonblocking-stream adapter** as the sole primary capability in this stop. It builds
on v0.195.0 (Standard blocking-stream adapter) and must be independently trustworthy before v0.197.0 (Brynja TLS provider contract and admission review) begins.

#### Deliverables

- Acceptance contract: Map WouldBlock, spurious/edge/level readiness, wake coalescing, interest changes, partial I/O, cancellation, EOF, and optional vectored I/O with scalar fallback and no reentrant engine calls.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Standard nonblocking-stream adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.195.0 (Standard blocking-stream adapter) still passes; no behavior assigned to v0.197.0 (Brynja TLS provider contract and admission review) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.196.0 implementation stop reached. Run pentest for this exact commit.`

### v0.197.0 — Brynja TLS provider contract and admission review

Status: planned

#### Goal

Deliver **Brynja TLS provider contract and admission review** as the sole primary capability in this stop. It builds
on v0.196.0 (Standard nonblocking-stream adapter) and must be independently trustworthy before v0.198.0 (Separate vef-brynja adapter crate) begins.

#### Deliverables

- Acceptance contract: Require Brynja to publish ALPN only after handshake success plus TLS version/cipher, compression/renegotiation status, certificate/SNI validation outcome, authenticated peer identity, resumption identity, early-data state, close_notify/fatal-alert/EOF state, and bounded nonblocking progress; missing metadata blocks admission.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Brynja TLS provider contract and admission review contract and all previously implemented relevant behavior have
reproducible evidence; v0.196.0 (Standard nonblocking-stream adapter) still passes; no behavior assigned to v0.198.0 (Separate vef-brynja adapter crate) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.197.0 implementation stop reached. Run pentest for this exact commit.`

### v0.198.0 — Separate vef-brynja adapter crate

Status: planned

#### Goal

Deliver **Separate vef-brynja adapter crate** as the sole primary capability in this stop. It builds
on v0.197.0 (Brynja TLS provider contract and admission review) and must be independently trustworthy before v0.199.0 (HTTP/2 TLS admission prerequisites and authenticated metadata) begins.

#### Deliverables

- Acceptance contract: Map every admitted Brynja handshake/progress/alert/EOF metadata state into vef-io capabilities and typed TLS outcomes without inference, hidden buffering, reentrancy, protocol fallback, or dependency leakage into protocol crates.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Separate vef-brynja adapter crate contract and all previously implemented relevant behavior have
reproducible evidence; v0.197.0 (Brynja TLS provider contract and admission review) still passes; no behavior assigned to v0.199.0 (HTTP/2 TLS admission prerequisites and authenticated metadata) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.198.0 implementation stop reached. Run pentest for this exact commit.`

### v0.199.0 — HTTP/2 TLS admission prerequisites and authenticated metadata

Status: planned

#### Goal

Deliver **HTTP/2 TLS admission prerequisites and authenticated metadata** as the sole primary capability in this stop. It builds
on v0.198.0 (Separate vef-brynja adapter crate) and must be independently trustworthy before v0.200.0 (TLS transport termination, resumption, alert, and EOF mapping) begins.

#### Deliverables

- Acceptance contract: Admit HTTP/2 only after handshake-success ALPN; require TLS 1.2+, reject prohibited TLS 1.2 suites, compression, and renegotiation; consume provider-supplied certificate/SNI validation, identity, session-resumption, and early-data state without inference.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The HTTP/2 TLS admission prerequisites and authenticated metadata contract and all previously implemented relevant behavior have
reproducible evidence; v0.198.0 (Separate vef-brynja adapter crate) still passes; no behavior assigned to v0.200.0 (TLS transport termination, resumption, alert, and EOF mapping) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.199.0 implementation stop reached. Run pentest for this exact commit.`

### v0.200.0 — TLS transport termination, resumption, alert, and EOF mapping

Status: planned

#### Goal

Deliver **TLS transport termination, resumption, alert, and EOF mapping** as the sole primary capability in this stop. It builds
on v0.199.0 (HTTP/2 TLS admission prerequisites and authenticated metadata) and must be independently trustworthy before v0.201.0 (TLS 1.3 early-data prohibition and close semantics) begins.

#### Deliverables

- Acceptance contract: Map authenticated resumption identity, fatal alerts, close_notify, clean EOF, truncation, half-close, and transport failure into distinct typed outcomes; preserve early-data state separately even though 1.0 rejects its use.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The TLS transport termination, resumption, alert, and EOF mapping contract and all previously implemented relevant behavior have
reproducible evidence; v0.199.0 (HTTP/2 TLS admission prerequisites and authenticated metadata) still passes; no behavior assigned to v0.201.0 (TLS 1.3 early-data prohibition and close semantics) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.200.0 implementation stop reached. Run pentest for this exact commit.`

### v0.201.0 — TLS 1.3 early-data prohibition and close semantics

Status: planned

#### Goal

Deliver **TLS 1.3 early-data prohibition and close semantics** as the sole primary capability in this stop. It builds
on v0.200.0 (TLS transport termination, resumption, alert, and EOF mapping) and must be independently trustworthy before v0.202.0 (Aesynx fixed-memory capability profile) begins.

#### Deliverables

- Acceptance contract: Reject offered, accepted, or replayed TLS early data before an HTTP engine consumes request bytes; keep early-data state observable in diagnostics, require a fresh post-handshake request path, and map close_notify, fatal alert, truncation, cancellation, and EOF distinctly.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The TLS 1.3 early-data prohibition and close semantics contract and all previously implemented relevant behavior have
reproducible evidence; v0.200.0 (TLS transport termination, resumption, alert, and EOF mapping) still passes; no behavior assigned to v0.202.0 (Aesynx fixed-memory capability profile) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.201.0 implementation stop reached. Run pentest for this exact commit.`

### v0.202.0 — Aesynx fixed-memory capability profile

Status: planned

#### Goal

Deliver **Aesynx fixed-memory capability profile** as the sole primary capability in this stop. It builds
on v0.201.0 (TLS 1.3 early-data prohibition and close semantics) and must be independently trustworthy before v0.203.0 (Aesynx transport and readiness adapter) begins.

#### Deliverables

- Acceptance contract: Publish aligned arena sizes, buffer ownership, maximum events/streams/control output, scalar and optional scatter-gather capabilities, cancellation slots, and failure behavior when static capacity is insufficient.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx fixed-memory capability profile contract and all previously implemented relevant behavior have
reproducible evidence; v0.201.0 (TLS 1.3 early-data prohibition and close semantics) still passes; no behavior assigned to v0.203.0 (Aesynx transport and readiness adapter) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.202.0 implementation stop reached. Run pentest for this exact commit.`

### v0.203.0 — Aesynx transport and readiness adapter

Status: planned

#### Goal

Deliver **Aesynx transport and readiness adapter** as the sole primary capability in this stop. It builds
on v0.202.0 (Aesynx fixed-memory capability profile) and must be independently trustworthy before v0.204.0 (Aesynx timer and deadline adapter) begins.

#### Deliverables

- Acceptance contract: Prove short I/O, WouldBlock, spurious edge/level readiness, wake coalescing, EOF/starvation distinction, alignment, cancellation, and scalar fallback against the fixed-memory profile.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx transport and readiness adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.202.0 (Aesynx fixed-memory capability profile) still passes; no behavior assigned to v0.204.0 (Aesynx timer and deadline adapter) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.203.0 implementation stop reached. Run pentest for this exact commit.`

### v0.204.0 — Aesynx timer and deadline adapter

Status: planned

#### Goal

Deliver **Aesynx timer and deadline adapter** as the sole primary capability in this stop. It builds
on v0.203.0 (Aesynx transport and readiness adapter) and must be independently trustworthy before v0.205.0 (Aesynx kernel integration tests) begins.

#### Deliverables

- Acceptance contract: Map monotonic ticks with checked wrap/deadline arithmetic, wake coalescing, cancellation races, expired-before-poll ordering, and no wall-clock dependency.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx timer and deadline adapter contract and all previously implemented relevant behavior have
reproducible evidence; v0.203.0 (Aesynx transport and readiness adapter) still passes; no behavior assigned to v0.205.0 (Aesynx kernel integration tests) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.204.0 implementation stop reached. Run pentest for this exact commit.`

### v0.205.0 — Aesynx kernel integration tests

Status: planned

#### Goal

Deliver **Aesynx kernel integration tests** as the sole primary capability in this stop. It builds
on v0.204.0 (Aesynx timer and deadline adapter) and must be independently trustworthy before v0.206.0 (Deterministic CPU, stack, code-size, and amplification budgets) begins.

#### Deliverables

- Acceptance contract: Define the Aesynx kernel integration tests state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Aesynx kernel integration tests contract and all previously implemented relevant behavior have
reproducible evidence; v0.204.0 (Aesynx timer and deadline adapter) still passes; no behavior assigned to v0.206.0 (Deterministic CPU, stack, code-size, and amplification budgets) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.205.0 implementation stop reached. Run pentest for this exact commit.`

### v0.206.0 — Deterministic CPU, stack, code-size, and amplification budgets

Status: planned

#### Goal

Deliver **Deterministic CPU, stack, code-size, and amplification budgets** as the sole primary capability in this stop. It builds
on v0.205.0 (Aesynx kernel integration tests) and must be independently trustworthy before v0.207.0 (32-bit target campaign) begins.

#### Deliverables

- Acceptance contract: Measure maximum stack and minimal-feature code size, prohibit peer-controlled recursion, cap work per byte/frame and amplification, detect quadratic work, price one-byte fragmentation, verify scheduler fairness, and document Aesynx arena sizing.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Deterministic CPU, stack, code-size, and amplification budgets contract and all previously implemented relevant behavior have
reproducible evidence; v0.205.0 (Aesynx kernel integration tests) still passes; no behavior assigned to v0.207.0 (32-bit target campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.206.0 implementation stop reached. Run pentest for this exact commit.`

### v0.207.0 — 32-bit target campaign

Status: planned

#### Goal

Deliver **32-bit target campaign** as the sole primary capability in this stop. It builds
on v0.206.0 (Deterministic CPU, stack, code-size, and amplification budgets) and must be independently trustworthy before v0.208.0 (Big-endian target campaign) begins.

#### Deliverables

- Acceptance contract: Define the 32-bit target campaign state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test 32-bit target campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The 32-bit target campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.206.0 (Deterministic CPU, stack, code-size, and amplification budgets) still passes; no behavior assigned to v0.208.0 (Big-endian target campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.207.0 implementation stop reached. Run pentest for this exact commit.`

### v0.208.0 — Big-endian target campaign

Status: planned

#### Goal

Deliver **Big-endian target campaign** as the sole primary capability in this stop. It builds
on v0.207.0 (32-bit target campaign) and must be independently trustworthy before v0.209.0 (Cross-architecture campaign) begins.

#### Deliverables

- Acceptance contract: Define the Big-endian target campaign state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Big-endian target campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Big-endian target campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.207.0 (32-bit target campaign) still passes; no behavior assigned to v0.209.0 (Cross-architecture campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.208.0 implementation stop reached. Run pentest for this exact commit.`

### v0.209.0 — Cross-architecture campaign

Status: planned

#### Goal

Deliver **Cross-architecture campaign** as the sole primary capability in this stop. It builds
on v0.208.0 (Big-endian target campaign) and must be independently trustworthy before v0.210.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) begins.

#### Deliverables

- Acceptance contract: Define the Cross-architecture campaign state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Cross-architecture campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Cross-architecture campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.208.0 (Big-endian target campaign) still passes; no behavior assigned to v0.210.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.209.0 implementation stop reached. Run pentest for this exact commit.`

### v0.210.0 — Linux, Windows, BSD, macOS, Android, and iOS matrix

Status: planned

#### Goal

Deliver **Linux, Windows, BSD, macOS, Android, and iOS matrix** as the sole primary capability in this stop. It builds
on v0.209.0 (Cross-architecture campaign) and must be independently trustworthy before v0.211.0 (Kani shared-core proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: Define the Linux, Windows, BSD, macOS, Android, and iOS matrix state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Linux, Windows, BSD, macOS, Android, and iOS matrix and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Linux, Windows, BSD, macOS, Android, and iOS matrix contract and all previously implemented relevant behavior have
reproducible evidence; v0.209.0 (Cross-architecture campaign) still passes; no behavior assigned to v0.211.0 (Kani shared-core proof replay and expansion) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.210.0 implementation stop reached. Run pentest for this exact commit.`

### v0.211.0 — Kani shared-core proof replay and expansion

Status: planned

#### Goal

Deliver **Kani shared-core proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.210.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) and must be independently trustworthy before v0.212.0 (Kani HTTP/1 proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: Define the Kani shared-core proof replay and expansion state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Kani shared-core proof replay and expansion and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani shared-core proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.210.0 (Linux, Windows, BSD, macOS, Android, and iOS matrix) still passes; no behavior assigned to v0.212.0 (Kani HTTP/1 proof replay and expansion) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.211.0 implementation stop reached. Run pentest for this exact commit.`

### v0.212.0 — Kani HTTP/1 proof replay and expansion

Status: planned

#### Goal

Deliver **Kani HTTP/1 proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.211.0 (Kani shared-core proof replay and expansion) and must be independently trustworthy before v0.213.0 (Kani HPACK proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: Define the Kani HTTP/1 proof replay and expansion state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the relevant stateful HTTP/1/intermediary fuzz target now and retain its minimized corpus.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani HTTP/1 proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.211.0 (Kani shared-core proof replay and expansion) still passes; no behavior assigned to v0.213.0 (Kani HPACK proof replay and expansion) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.212.0 implementation stop reached. Run pentest for this exact commit.`

### v0.213.0 — Kani HPACK proof replay and expansion

Status: planned

#### Goal

Deliver **Kani HPACK proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.212.0 (Kani HTTP/1 proof replay and expansion) and must be independently trustworthy before v0.214.0 (Kani HTTP/2 proof replay and expansion) begins.

#### Deliverables

- Acceptance contract: Define the Kani HPACK proof replay and expansion state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Kani HPACK proof replay and expansion and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani HPACK proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.212.0 (Kani HTTP/1 proof replay and expansion) still passes; no behavior assigned to v0.214.0 (Kani HTTP/2 proof replay and expansion) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.213.0 implementation stop reached. Run pentest for this exact commit.`

### v0.214.0 — Kani HTTP/2 proof replay and expansion

Status: planned

#### Goal

Deliver **Kani HTTP/2 proof replay and expansion** as the sole primary capability in this stop. It builds
on v0.213.0 (Kani HPACK proof replay and expansion) and must be independently trustworthy before v0.215.0 (Stateful cargo-fuzz replay and expansion) begins.

#### Deliverables

- Acceptance contract: Define the Kani HTTP/2 proof replay and expansion state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Create or extend the matching HTTP/2 frame/state Kani or stateful fuzz harness at this milestone.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Kani HTTP/2 proof replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.213.0 (Kani HPACK proof replay and expansion) still passes; no behavior assigned to v0.215.0 (Stateful cargo-fuzz replay and expansion) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.214.0 implementation stop reached. Run pentest for this exact commit.`

### v0.215.0 — Stateful cargo-fuzz replay and expansion

Status: planned

#### Goal

Deliver **Stateful cargo-fuzz replay and expansion** as the sole primary capability in this stop. It builds
on v0.214.0 (Kani HTTP/2 proof replay and expansion) and must be independently trustworthy before v0.216.0 (Differential and interoperability campaign) begins.

#### Deliverables

- Acceptance contract: Define the Stateful cargo-fuzz replay and expansion state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Stateful cargo-fuzz replay and expansion and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Stateful cargo-fuzz replay and expansion contract and all previously implemented relevant behavior have
reproducible evidence; v0.214.0 (Kani HTTP/2 proof replay and expansion) still passes; no behavior assigned to v0.216.0 (Differential and interoperability campaign) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.215.0 implementation stop reached. Run pentest for this exact commit.`

### v0.216.0 — Differential and interoperability campaign

Status: planned

#### Goal

Deliver **Differential and interoperability campaign** as the sole primary capability in this stop. It builds
on v0.215.0 (Stateful cargo-fuzz replay and expansion) and must be independently trustworthy before v0.217.0 (Whole-project conformance audit and pentest) begins.

#### Deliverables

- Acceptance contract: Define the Differential and interoperability campaign state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Differential and interoperability campaign and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Differential and interoperability campaign contract and all previously implemented relevant behavior have
reproducible evidence; v0.215.0 (Stateful cargo-fuzz replay and expansion) still passes; no behavior assigned to v0.217.0 (Whole-project conformance audit and pentest) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.216.0 implementation stop reached. Run pentest for this exact commit.`

### v0.217.0 — Whole-project conformance audit and pentest

Status: planned

#### Goal

Deliver **Whole-project conformance audit and pentest** as the sole primary capability in this stop. It builds
on v0.216.0 (Differential and interoperability campaign) and must be independently trustworthy before v0.218.0 (Independent security audit) begins.

#### Deliverables

- Acceptance contract: Define the Whole-project conformance audit and pentest state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Whole-project conformance audit and pentest and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Whole-project conformance audit and pentest contract and all previously implemented relevant behavior have
reproducible evidence; v0.216.0 (Differential and interoperability campaign) still passes; no behavior assigned to v0.218.0 (Independent security audit) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.217.0 implementation stop reached. Run pentest for this exact commit.`

### v0.218.0 — Independent security audit

Status: planned

#### Goal

Deliver **Independent security audit** as the sole primary capability in this stop. It builds
on v0.217.0 (Whole-project conformance audit and pentest) and must be independently trustworthy before v0.219.0 (Audit remediation and API freeze) begins.

#### Deliverables

- Acceptance contract: Define the Independent security audit state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Independent security audit and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Independent security audit contract and all previously implemented relevant behavior have
reproducible evidence; v0.217.0 (Whole-project conformance audit and pentest) still passes; no behavior assigned to v0.219.0 (Audit remediation and API freeze) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.218.0 implementation stop reached. Run pentest for this exact commit.`

### v0.219.0 — Audit remediation and API freeze

Status: planned

#### Goal

Deliver **Audit remediation and API freeze** as the sole primary capability in this stop. It builds
on v0.218.0 (Independent security audit) and must be independently trustworthy before v0.220.0 (Documentation, packaging, SBOM, provenance, and RC readiness) begins.

#### Deliverables

- Acceptance contract: Define the Audit remediation and API freeze state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Test Audit remediation and API freeze and all previously implemented relevant behavior with positive, negative, boundary, truncation, invalid-state, cancellation, capacity, and no-panic cases.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Audit remediation and API freeze contract and all previously implemented relevant behavior have
reproducible evidence; v0.218.0 (Independent security audit) still passes; no behavior assigned to v0.220.0 (Documentation, packaging, SBOM, provenance, and RC readiness) is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.219.0 implementation stop reached. Run pentest for this exact commit.`

### v0.220.0 — Documentation, packaging, SBOM, provenance, and RC readiness

Status: planned

#### Goal

Deliver **Documentation, packaging, SBOM, provenance, and RC readiness** as the sole primary capability in this stop. It builds
on v0.219.0 (Audit remediation and API freeze) and must be independently trustworthy before the 1.0 release-candidate sequence begins.

#### Deliverables

- Acceptance contract: Define the Documentation, packaging, SBOM, provenance, and RC readiness state graph, invariants, exact typed errors, publication/commit point, caller-capacity failure, cancellation aftermath, and bounded work; test every transition without requiring later behavior.
- Preserve the phase invariant: Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.
- Update paragraph-addressable requirements, role/applicability decisions,
  SHOULD dispositions, deviations, and verified/held errata for
  RFC 7301, RFC 8446, RFC 9113 TLS prerequisites, platform ABI and target guarantees, the admitted Brynja contract, and all previously applicable HTTP requirements.
- Define exact progress, capacity, cancellation, ownership, publication,
  commit/rollback, and typed error behavior wherever this outcome changes them.
- Update threat model, controls, API docs, release notes, traceability, resource
  measurements, and relevant conformance corpora.

#### Verification

- Measure this outcome against the active resource profile and fail deterministic limit, readiness, timeout, EOF, cancellation, or amplification regressions.
- No test may require a later-version capability; previously established resource ceilings remain release-blocking.
- Prove failures do not publish partial state, mutate unrelated state, exceed
  active work/output limits, or require hidden allocation.
- Run Rust `1.90.0`–`1.97.1`, `no_std`, target, docs/package, dependency policy,
  audit, SBOM, CI, and CodeQL default-setup gates.

#### Exit criteria

The Documentation, packaging, SBOM, provenance, and RC readiness contract and all previously implemented relevant behavior have
reproducible evidence; v0.219.0 (Audit remediation and API freeze) still passes; no behavior assigned to the 1.0 release-candidate sequence is
claimed; the active resource profile passes; and no critical/high finding is
open.

`0.220.0 implementation stop reached. Run pentest for this exact commit.`

## 1.0 release candidates

### v1.0.0-rc.1

Status: planned

Goal: freeze public APIs and expose the candidate to public interoperability,
security, usability, resource, and documentation review.

Deliverables: API freeze, migration guidance, package dry runs, RFC/errata
coverage, platform/resource matrices, limitations, SBOM, provenance, and
complete release evidence.

Verification: replay every fuzz/model/resource harness, repository gate,
independent multi-implementation interop, manual audit, and exact-commit
pentest.

Exit criteria: no new features and all evidence reproducible.
`1.0.0-rc.1 implementation stop reached. Run pentest for this exact commit.`

### v1.0.0-rc.2

Status: planned

Goal: remediate RC1 findings without expanding scope.

Deliverables: fixes, regression tests, final source/RFC review, MSRV/target and
resource declarations, and refreshed evidence.

Verification: repeat every fuzz, model, pentest, conformance, interop,
portability, resource, package, SBOM, and provenance gate.

Exit criteria: no unresolved critical/high findings or unreviewed behavior.
`1.0.0-rc.2 implementation stop reached. Run pentest for this exact commit.`

### v1.0.0

Status: planned

Goal: publish the first serious production-ready VEF HTTP crate.

Release only when applicable requirements are verified, capacity/error
dispositions are unambiguous, resource ceilings pass, fixed storage works
without allocation, HTTP/1 framing/body/transition ownership is deterministic,
HPACK output/input state is synchronized, HTTP/2 activation/publication/
SETTINGS/flow/cancellation/shutdown evidence is exhaustive, intermediary and
translation matrices pass, TLS admission/termination is explicit, every role
and platform claim is verified, independent-audit remediation is complete, and
HTTP/3 remains out of scope.
