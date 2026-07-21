# VEF Release Plan to 1.0

Status: planning document

This plan is intentionally granular. VEF parses attacker-controlled protocol
traffic, so every milestone must be small enough to implement, review, test,
pentest, and stop cleanly before tagging. Split a milestone or add patch
releases whenever its security argument no longer fits one review pass.

## Release principles

Every release requires a clear outcome, applicable RFC/errata evidence,
bounded-resource behavior, positive and negative tests, fragmentation where
input is incremental, adversarial and regression evidence, documentation,
release notes, portability evidence, dependency-policy proof, a clean SBOM,
full-SHA CI pins, CodeQL default-setup review, and an exact-commit pentest.

The repository currently permits no third-party Rust crates. A release cannot
weaken that rule implicitly. Protocol crates remain `no_std`, safe Rust, and
independent of sockets, runtimes, TLS implementations, and wall clocks.

## Required milestone format and pentest flow

Each contract below has Status, Goal, Deliverables, Verification, and Exit
criteria. Release-specific verification is additive to `scripts/checks.sh`,
the full Rust 1.90.0–1.97.1 matrix, live tool checks, Cargo policy/audit, SBOM,
package inspection, CI, CodeQL default setup, and release readiness.

At the implementation stop, do not tag. Pentest the exact commit, remediate
findings with regression tests, repeat all gates, then add the permanent passing
report as the only file in the direct child of the reviewed commit. Critical or
high findings block release. Phase-ending releases additionally require a
full-repository manual review, stateful fuzz campaign, corpus minimization,
multi-peer interoperability, resource-exhaustion assessment, and review of all
open conformance decisions.

## Phase 1 — Foundation and shared types

Phase goal: complete foundation and shared types without weakening prior security, portability, or conformance evidence.

### v0.1.0 — Workspace, crate boundaries, licenses, security policy, and release evidence

Status: foundation implementation in progress

#### Goal

Deliver workspace, crate boundaries, licenses, security policy, and release evidence as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document workspace, crate boundaries, licenses, security policy, and release evidence in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.1.0 implementation stop reached. Run pentest for this exact commit.`

### v0.2.0 — Empty vef-core with strict no_std and unsafe prohibition

Status: planned

#### Goal

Deliver empty vef-core with strict no_std and unsafe prohibition as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document empty vef-core with strict no_std and unsafe prohibition in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.2.0 implementation stop reached. Run pentest for this exact commit.`

### v0.3.0 — Checked byte cursor with no unchecked indexing

Status: planned

#### Goal

Deliver checked byte cursor with no unchecked indexing as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document checked byte cursor with no unchecked indexing in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.3.0 implementation stop reached. Run pentest for this exact commit.`

### v0.4.0 — Parser progress contract and NeedMore model

Status: planned

#### Goal

Deliver parser progress contract and needmore model as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document parser progress contract and needmore model in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.4.0 implementation stop reached. Run pentest for this exact commit.`

### v0.5.0 — Configurable limits and checked size domains

Status: planned

#### Goal

Deliver configurable limits and checked size domains as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document configurable limits and checked size domains in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.5.0 implementation stop reached. Run pentest for this exact commit.`

### v0.6.0 — Work, transition, and allocation budget counters

Status: planned

#### Goal

Deliver work, transition, and allocation budget counters as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document work, transition, and allocation budget counters in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.6.0 implementation stop reached. Run pentest for this exact commit.`

### v0.7.0 — Structured error and diagnostic taxonomy

Status: planned

#### Goal

Deliver structured error and diagnostic taxonomy as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document structured error and diagnostic taxonomy in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.7.0 implementation stop reached. Run pentest for this exact commit.`

### v0.8.0 — Case-sensitive extension-capable Method

Status: planned

#### Goal

Deliver case-sensitive extension-capable method as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document case-sensitive extension-capable method in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.8.0 implementation stop reached. Run pentest for this exact commit.`

### v0.9.0 — Validated StatusCode with unknown-code preservation

Status: planned

#### Goal

Deliver validated statuscode with unknown-code preservation as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document validated statuscode with unknown-code preservation in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.9.0 implementation stop reached. Run pentest for this exact commit.`

### v0.10.0 — Version and wire-version representation

Status: planned

#### Goal

Deliver version and wire-version representation as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document version and wire-version representation in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.10.0 implementation stop reached. Run pentest for this exact commit.`

### v0.11.0 — Case-insensitive validated FieldName

Status: planned

#### Goal

Deliver case-insensitive validated fieldname as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document case-insensitive validated fieldname in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.11.0 implementation stop reached. Run pentest for this exact commit.`

### v0.12.0 — Byte-oriented FieldValue with raw and semantic views

Status: planned

#### Goal

Deliver byte-oriented fieldvalue with raw and semantic views as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document byte-oriented fieldvalue with raw and semantic views in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.12.0 implementation stop reached. Run pentest for this exact commit.`

### v0.13.0 — Ordered FieldLine and FieldSection

Status: planned

#### Goal

Deliver ordered fieldline and fieldsection as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document ordered fieldline and fieldsection in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.13.0 implementation stop reached. Run pentest for this exact commit.`

### v0.14.0 — Four request-target forms without normalization

Status: planned

#### Goal

Deliver four request-target forms without normalization as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document four request-target forms without normalization in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.14.0 implementation stop reached. Run pentest for this exact commit.`

### v0.15.0 — Request and response control-data types

Status: planned

#### Goal

Deliver request and response control-data types as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document request and response control-data types in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.15.0 implementation stop reached. Run pentest for this exact commit.`

### v0.16.0 — Requirement manifest, conformance harness, and full foundation audit

Status: planned

#### Goal

Deliver requirement manifest, conformance harness, and full foundation audit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document requirement manifest, conformance harness, and full foundation audit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 2119, RFC 8174, and the complete source/conformance policy.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Perform the phase-boundary full-repository audit, stateful fuzz campaign, corpus review, interoperability campaign, and resource-exhaustion assessment.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.16.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 2 — HTTP/1 start lines and field sections

Phase goal: complete http/1 start lines and field sections without weakening prior security, portability, or conformance evidence.

### v0.17.0 — Client, server, and intermediary role types and parser profiles

Status: planned

#### Goal

Deliver client, server, and intermediary role types and parser profiles as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document client, server, and intermediary role types and parser profiles in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.17.0 implementation stop reached. Run pentest for this exact commit.`

### v0.18.0 — Incremental request-line state machine

Status: planned

#### Goal

Deliver incremental request-line state machine as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document incremental request-line state machine in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.18.0 implementation stop reached. Run pentest for this exact commit.`

### v0.19.0 — Incremental status-line state machine

Status: planned

#### Goal

Deliver incremental status-line state machine as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document incremental status-line state machine in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.19.0 implementation stop reached. Run pentest for this exact commit.`

### v0.20.0 — Every-byte-boundary fragmentation support

Status: planned

#### Goal

Deliver every-byte-boundary fragmentation support as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document every-byte-boundary fragmentation support in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.20.0 implementation stop reached. Run pentest for this exact commit.`

### v0.21.0 — Strict CRLF and incomplete-line handling

Status: planned

#### Goal

Deliver strict crlf and incomplete-line handling as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document strict crlf and incomplete-line handling in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.21.0 implementation stop reached. Run pentest for this exact commit.`

### v0.22.0 — Incremental field-line parser

Status: planned

#### Goal

Deliver incremental field-line parser as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document incremental field-line parser in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.22.0 implementation stop reached. Run pentest for this exact commit.`

### v0.23.0 — Explicit OWS removal with raw-value preservation

Status: planned

#### Goal

Deliver explicit ows removal with raw-value preservation as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document explicit ows removal with raw-value preservation in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.23.0 implementation stop reached. Run pentest for this exact commit.`

### v0.24.0 — obs-fold, whitespace-before-colon, and control-byte rejection

Status: planned

#### Goal

Deliver obs-fold, whitespace-before-colon, and control-byte rejection as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document obs-fold, whitespace-before-colon, and control-byte rejection in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.24.0 implementation stop reached. Run pentest for this exact commit.`

### v0.25.0 — Field count, line, and section limit enforcement

Status: planned

#### Goal

Deliver field count, line, and section limit enforcement as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document field count, line, and section limit enforcement in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.25.0 implementation stop reached. Run pentest for this exact commit.`

### v0.26.0 — HTTP/1.1 Host validation and duplicate rejection

Status: planned

#### Goal

Deliver http/1.1 host validation and duplicate rejection as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http/1.1 host validation and duplicate rejection in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.26.0 implementation stop reached. Run pentest for this exact commit.`

### v0.27.0 — Method and request-target-form coherence

Status: planned

#### Goal

Deliver method and request-target-form coherence as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document method and request-target-form coherence in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.27.0 implementation stop reached. Run pentest for this exact commit.`

### v0.28.0 — Checked Content-Length grammar

Status: planned

#### Goal

Deliver checked content-length grammar as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document checked content-length grammar in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.28.0 implementation stop reached. Run pentest for this exact commit.`

### v0.29.0 — Repeated and comma-list Content-Length resolution

Status: planned

#### Goal

Deliver repeated and comma-list content-length resolution as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document repeated and comma-list content-length resolution in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.29.0 implementation stop reached. Run pentest for this exact commit.`

### v0.30.0 — Transfer-Encoding grammar and ordering

Status: planned

#### Goal

Deliver transfer-encoding grammar and ordering as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document transfer-encoding grammar and ordering in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.30.0 implementation stop reached. Run pentest for this exact commit.`

### v0.31.0 — TE/CL conflict resolution and mandatory close action

Status: planned

#### Goal

Deliver te/cl conflict resolution and mandatory close action as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document te/cl conflict resolution and mandatory close action in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.31.0 implementation stop reached. Run pentest for this exact commit.`

### v0.32.0 — Head serialization, round-trip properties, and full phase audit

Status: planned

#### Goal

Deliver head serialization, round-trip properties, and full phase audit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document head serialization, round-trip properties, and full phase audit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 3986, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Perform the phase-boundary full-repository audit, stateful fuzz campaign, corpus review, interoperability campaign, and resource-exhaustion assessment.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.32.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 3 — HTTP/1 body framing and persistence

Phase goal: complete http/1 body framing and persistence without weakening prior security, portability, or conformance evidence.

### v0.33.0 — Central message-body-length decision algorithm

Status: planned

#### Goal

Deliver central message-body-length decision algorithm as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document central message-body-length decision algorithm in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.33.0 implementation stop reached. Run pentest for this exact commit.`

### v0.34.0 — Fixed-length body decoder

Status: planned

#### Goal

Deliver fixed-length body decoder as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document fixed-length body decoder in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.34.0 implementation stop reached. Run pentest for this exact commit.`

### v0.35.0 — Close-delimited response decoder

Status: planned

#### Goal

Deliver close-delimited response decoder as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document close-delimited response decoder in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.35.0 implementation stop reached. Run pentest for this exact commit.`

### v0.36.0 — Checked hexadecimal chunk-size parser

Status: planned

#### Goal

Deliver checked hexadecimal chunk-size parser as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document checked hexadecimal chunk-size parser in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.36.0 implementation stop reached. Run pentest for this exact commit.`

### v0.37.0 — Incremental chunk-data and CRLF state

Status: planned

#### Goal

Deliver incremental chunk-data and crlf state as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document incremental chunk-data and crlf state in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.37.0 implementation stop reached. Run pentest for this exact commit.`

### v0.38.0 — Bounded chunk-extension parser

Status: planned

#### Goal

Deliver bounded chunk-extension parser as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document bounded chunk-extension parser in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.38.0 implementation stop reached. Run pentest for this exact commit.`

### v0.39.0 — Last-chunk and trailer transition

Status: planned

#### Goal

Deliver last-chunk and trailer transition as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document last-chunk and trailer transition in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.39.0 implementation stop reached. Run pentest for this exact commit.`

### v0.40.0 — Trailer declarations and prohibited-trailer policy

Status: planned

#### Goal

Deliver trailer declarations and prohibited-trailer policy as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document trailer declarations and prohibited-trailer policy in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.40.0 implementation stop reached. Run pentest for this exact commit.`

### v0.41.0 — Chunked encoder and caller-owned output buffering

Status: planned

#### Goal

Deliver chunked encoder and caller-owned output buffering as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document chunked encoder and caller-owned output buffering in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.41.0 implementation stop reached. Run pentest for this exact commit.`

### v0.42.0 — HTTP/1.1 persistence and Connection semantics

Status: planned

#### Goal

Deliver http/1.1 persistence and connection semantics as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http/1.1 persistence and connection semantics in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.42.0 implementation stop reached. Run pentest for this exact commit.`

### v0.43.0 — Sequential request/response connection state

Status: planned

#### Goal

Deliver sequential request/response connection state as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document sequential request/response connection state in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.43.0 implementation stop reached. Run pentest for this exact commit.`

### v0.44.0 — Optional bounded pipelining queue

Status: planned

#### Goal

Deliver optional bounded pipelining queue as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document optional bounded pipelining queue in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.44.0 implementation stop reached. Run pentest for this exact commit.`

### v0.45.0 — Informational response lifecycle

Status: planned

#### Goal

Deliver informational response lifecycle as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document informational response lifecycle in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.45.0 implementation stop reached. Run pentest for this exact commit.`

### v0.46.0 — Expect: 100-continue state

Status: planned

#### Goal

Deliver expect: 100-continue state as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document expect: 100-continue state in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.46.0 implementation stop reached. Run pentest for this exact commit.`

### v0.47.0 — EOF, truncation, and incomplete-message rules

Status: planned

#### Goal

Deliver eof, truncation, and incomplete-message rules as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document eof, truncation, and incomplete-message rules in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.47.0 implementation stop reached. Run pentest for this exact commit.`

### v0.48.0 — Full framing, persistence, and body audit

Status: planned

#### Goal

Deliver full framing, persistence, and body audit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document full framing, persistence, and body audit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Perform the phase-boundary full-repository audit, stateful fuzz campaign, corpus review, interoperability campaign, and resource-exhaustion assessment.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.48.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 4 — HTTP/1 roles, transitions, and legacy profiles

Phase goal: complete http/1 roles, transitions, and legacy profiles without weakening prior security, portability, or conformance evidence.

### v0.49.0 — HEAD request response-framing context

Status: planned

#### Goal

Deliver head request response-framing context as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document head request response-framing context in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.49.0 implementation stop reached. Run pentest for this exact commit.`

### v0.50.0 — 1xx, 204, 304, and body-forbidden response handling

Status: planned

#### Goal

Deliver 1xx, 204, 304, and body-forbidden response handling as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document 1xx, 204, 304, and body-forbidden response handling in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.50.0 implementation stop reached. Run pentest for this exact commit.`

### v0.51.0 — CONNECT request and successful tunnel transition

Status: planned

#### Goal

Deliver connect request and successful tunnel transition as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document connect request and successful tunnel transition in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.51.0 implementation stop reached. Run pentest for this exact commit.`

### v0.52.0 — RFC 9931 optimistic CONNECT protections

Status: planned

#### Goal

Deliver rfc 9931 optimistic connect protections as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document rfc 9931 optimistic connect protections in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.52.0 implementation stop reached. Run pentest for this exact commit.`

### v0.53.0 — 101 Switching Protocols transition

Status: planned

#### Goal

Deliver 101 switching protocols transition as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document 101 switching protocols transition in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.53.0 implementation stop reached. Run pentest for this exact commit.`

### v0.54.0 — Connection-nominated and hop-by-hop field handling

Status: planned

#### Goal

Deliver connection-nominated and hop-by-hop field handling as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document connection-nominated and hop-by-hop field handling in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.54.0 implementation stop reached. Run pentest for this exact commit.`

### v0.55.0 — Safe forwarding and connection-close action API

Status: planned

#### Goal

Deliver safe forwarding and connection-close action api as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document safe forwarding and connection-close action api in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.55.0 implementation stop reached. Run pentest for this exact commit.`

### v0.56.0 — RFC 1945 HTTP/1.0 parser and serializer

Status: planned

#### Goal

Deliver rfc 1945 http/1.0 parser and serializer as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document rfc 1945 http/1.0 parser and serializer in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.56.0 implementation stop reached. Run pentest for this exact commit.`

### v0.57.0 — HTTP/1.0 default connection-close lifecycle

Status: planned

#### Goal

Deliver http/1.0 default connection-close lifecycle as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http/1.0 default connection-close lifecycle in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.57.0 implementation stop reached. Run pentest for this exact commit.`

### v0.58.0 — Explicit HTTP/1.0 keep-alive extension profile

Status: planned

#### Goal

Deliver explicit http/1.0 keep-alive extension profile as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document explicit http/1.0 keep-alive extension profile in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.58.0 implementation stop reached. Run pentest for this exact commit.`

### v0.59.0 — Explicit HTTP/0.9 client

Status: planned

#### Goal

Deliver explicit http/0.9 client as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document explicit http/0.9 client in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.59.0 implementation stop reached. Run pentest for this exact commit.`

### v0.60.0 — Explicit HTTP/0.9 server

Status: planned

#### Goal

Deliver explicit http/0.9 server as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document explicit http/0.9 server in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.60.0 implementation stop reached. Run pentest for this exact commit.`

### v0.61.0 — HTTP/0.9 dedicated-listener and disabled-default policy

Status: planned

#### Goal

Deliver http/0.9 dedicated-listener and disabled-default policy as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http/0.9 dedicated-listener and disabled-default policy in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.61.0 implementation stop reached. Run pentest for this exact commit.`

### v0.62.0 — HTTP/0.9 cross-protocol attack corpus

Status: planned

#### Goal

Deliver http/0.9 cross-protocol attack corpus as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http/0.9 cross-protocol attack corpus in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.62.0 implementation stop reached. Run pentest for this exact commit.`

### v0.63.0 — Full CL.TE, TE.CL, duplicate, and whitespace smuggling corpus

Status: planned

#### Goal

Deliver full cl.te, te.cl, duplicate, and whitespace smuggling corpus as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document full cl.te, te.cl, duplicate, and whitespace smuggling corpus in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.63.0 implementation stop reached. Run pentest for this exact commit.`

### v0.64.0 — Full HTTP/0.9–1.1 pentest and conformance audit

Status: planned

#### Goal

Deliver full http/0.9–1.1 pentest and conformance audit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document full http/0.9–1.1 pentest and conformance audit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 1945, RFC 9110, RFC 9112, and RFC 9931 as applicable.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Perform the phase-boundary full-repository audit, stateful fuzz campaign, corpus review, interoperability campaign, and resource-exhaustion assessment.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.64.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 5 — I/O and secure adapter contracts

Phase goal: complete i/o and secure adapter contracts without weakening prior security, portability, or conformance evidence.

### v0.65.0 — Minimal synchronous vef-io traits

Status: planned

#### Goal

Deliver minimal synchronous vef-io traits as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document minimal synchronous vef-io traits in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.65.0 implementation stop reached. Run pentest for this exact commit.`

### v0.66.0 — Runtime-neutral poll traits

Status: planned

#### Goal

Deliver runtime-neutral poll traits as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document runtime-neutral poll traits in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.66.0 implementation stop reached. Run pentest for this exact commit.`

### v0.67.0 — External clock and deadline abstraction

Status: planned

#### Goal

Deliver external clock and deadline abstraction as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document external clock and deadline abstraction in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.67.0 implementation stop reached. Run pentest for this exact commit.`

### v0.68.0 — Cancellation and bounded backpressure contract

Status: planned

#### Goal

Deliver cancellation and bounded backpressure contract as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document cancellation and bounded backpressure contract in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.68.0 implementation stop reached. Run pentest for this exact commit.`

### v0.69.0 — Standard blocking-stream adapter

Status: planned

#### Goal

Deliver standard blocking-stream adapter as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document standard blocking-stream adapter in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.69.0 implementation stop reached. Run pentest for this exact commit.`

### v0.70.0 — Standard nonblocking-stream adapter

Status: planned

#### Goal

Deliver standard nonblocking-stream adapter as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document standard nonblocking-stream adapter in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.70.0 implementation stop reached. Run pentest for this exact commit.`

### v0.71.0 — Generic async-poll driver and downstream runtime conformance contract

Status: planned

#### Goal

Deliver generic async-poll driver and downstream runtime conformance contract as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document generic async-poll driver and downstream runtime conformance contract in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.71.0 implementation stop reached. Run pentest for this exact commit.`

### v0.72.0 — Generic connection driver and deterministic fake transport

Status: planned

#### Goal

Deliver generic connection driver and deterministic fake transport as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document generic connection driver and deterministic fake transport in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.72.0 implementation stop reached. Run pentest for this exact commit.`

### v0.73.0 — TLS metadata, peer identity, and ALPN interface

Status: planned

#### Goal

Deliver tls metadata, peer identity, and alpn interface as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document tls metadata, peer identity, and alpn interface in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.73.0 implementation stop reached. Run pentest for this exact commit.`

### v0.74.0 — Dependency-free TLS provider adapter contract

Status: planned

#### Goal

Deliver dependency-free tls provider adapter contract as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document dependency-free tls provider adapter contract in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.74.0 implementation stop reached. Run pentest for this exact commit.`

### v0.75.0 — ALPN and provider-capability validation

Status: planned

#### Goal

Deliver alpn and provider-capability validation as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document alpn and provider-capability validation in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.75.0 implementation stop reached. Run pentest for this exact commit.`

### v0.76.0 — TLS session and certificate-metadata policy boundary

Status: planned

#### Goal

Deliver tls session and certificate-metadata policy boundary as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document tls session and certificate-metadata policy boundary in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.76.0 implementation stop reached. Run pentest for this exact commit.`

### v0.77.0 — Downstream TLS adapter conformance kit

Status: planned

#### Goal

Deliver downstream tls adapter conformance kit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document downstream tls adapter conformance kit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.77.0 implementation stop reached. Run pentest for this exact commit.`

### v0.78.0 — HTTP/1 TLS and ALPN selection policy

Status: planned

#### Goal

Deliver http/1 tls and alpn selection policy as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http/1 tls and alpn selection policy in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.78.0 implementation stop reached. Run pentest for this exact commit.`

### v0.79.0 — HTTP/2 TLS prerequisites and rejection policy

Status: planned

#### Goal

Deliver http/2 tls prerequisites and rejection policy as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http/2 tls prerequisites and rejection policy in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.79.0 implementation stop reached. Run pentest for this exact commit.`

### v0.80.0 — Adapter, cancellation, timeout, and platform-boundary audit

Status: planned

#### Goal

Deliver adapter, cancellation, timeout, and platform-boundary audit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document adapter, cancellation, timeout, and platform-boundary audit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7301, RFC 8446, RFC 9112, and RFC 9113 transport prerequisites.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Perform the phase-boundary full-repository audit, stateful fuzz campaign, corpus review, interoperability campaign, and resource-exhaustion assessment.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.80.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 6 — HPACK

Phase goal: complete hpack without weakening prior security, portability, or conformance evidence.

### v0.81.0 — Prefix-integer decoder

Status: planned

#### Goal

Deliver prefix-integer decoder as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document prefix-integer decoder in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.81.0 implementation stop reached. Run pentest for this exact commit.`

### v0.82.0 — Prefix-integer encoder

Status: planned

#### Goal

Deliver prefix-integer encoder as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document prefix-integer encoder in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.82.0 implementation stop reached. Run pentest for this exact commit.`

### v0.83.0 — Integer overflow, overlong encoding, and proof harnesses

Status: planned

#### Goal

Deliver integer overflow, overlong encoding, and proof harnesses as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document integer overflow, overlong encoding, and proof harnesses in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.83.0 implementation stop reached. Run pentest for this exact commit.`

### v0.84.0 — Bounded string-literal codec

Status: planned

#### Goal

Deliver bounded string-literal codec as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document bounded string-literal codec in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.84.0 implementation stop reached. Run pentest for this exact commit.`

### v0.85.0 — Reproducibly generated Huffman tables

Status: planned

#### Goal

Deliver reproducibly generated huffman tables as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document reproducibly generated huffman tables in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.85.0 implementation stop reached. Run pentest for this exact commit.`

### v0.86.0 — Constant-memory Huffman decoder

Status: planned

#### Goal

Deliver constant-memory huffman decoder as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document constant-memory huffman decoder in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.86.0 implementation stop reached. Run pentest for this exact commit.`

### v0.87.0 — Huffman encoder

Status: planned

#### Goal

Deliver huffman encoder as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document huffman encoder in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.87.0 implementation stop reached. Run pentest for this exact commit.`

### v0.88.0 — Static table

Status: planned

#### Goal

Deliver static table as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document static table in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.88.0 implementation stop reached. Run pentest for this exact commit.`

### v0.89.0 — Bounded dynamic table

Status: planned

#### Goal

Deliver bounded dynamic table as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document bounded dynamic table in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.89.0 implementation stop reached. Run pentest for this exact commit.`

### v0.90.0 — Correct table eviction and size updates

Status: planned

#### Goal

Deliver correct table eviction and size updates as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document correct table eviction and size updates in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.90.0 implementation stop reached. Run pentest for this exact commit.`

### v0.91.0 — Indexed representation

Status: planned

#### Goal

Deliver indexed representation as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document indexed representation in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.91.0 implementation stop reached. Run pentest for this exact commit.`

### v0.92.0 — Literal with incremental indexing

Status: planned

#### Goal

Deliver literal with incremental indexing as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document literal with incremental indexing in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.92.0 implementation stop reached. Run pentest for this exact commit.`

### v0.93.0 — Literal without indexing

Status: planned

#### Goal

Deliver literal without indexing as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document literal without indexing in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.93.0 implementation stop reached. Run pentest for this exact commit.`

### v0.94.0 — Never-indexed representation and sensitive-field policy

Status: planned

#### Goal

Deliver never-indexed representation and sensitive-field policy as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document never-indexed representation and sensitive-field policy in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.94.0 implementation stop reached. Run pentest for this exact commit.`

### v0.95.0 — Encoded, decoded, table, count, and work limits

Status: planned

#### Goal

Deliver encoded, decoded, table, count, and work limits as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document encoded, decoded, table, count, and work limits in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.95.0 implementation stop reached. Run pentest for this exact commit.`

### v0.96.0 — Full HPACK interoperability, fuzzing, and pentest audit

Status: planned

#### Goal

Deliver full hpack interoperability, fuzzing, and pentest audit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document full hpack interoperability, fuzzing, and pentest audit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Perform the phase-boundary full-repository audit, stateful fuzz campaign, corpus review, interoperability campaign, and resource-exhaustion assessment.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.96.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 7 — HTTP/2 framing and state

Phase goal: complete http/2 framing and state without weakening prior security, portability, or conformance evidence.

### v0.97.0 — Client and server connection prefaces

Status: planned

#### Goal

Deliver client and server connection prefaces as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document client and server connection prefaces in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.97.0 implementation stop reached. Run pentest for this exact commit.`

### v0.98.0 — Nine-octet frame header and size validation

Status: planned

#### Goal

Deliver nine-octet frame header and size validation as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document nine-octet frame header and size validation in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.98.0 implementation stop reached. Run pentest for this exact commit.`

### v0.99.0 — DATA frames and padding

Status: planned

#### Goal

Deliver data frames and padding as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document data frames and padding in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.99.0 implementation stop reached. Run pentest for this exact commit.`

### v0.100.0 — HEADERS frames

Status: planned

#### Goal

Deliver headers frames as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document headers frames in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.100.0 implementation stop reached. Run pentest for this exact commit.`

### v0.101.0 — CONTINUATION and field-block atomicity

Status: planned

#### Goal

Deliver continuation and field-block atomicity as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document continuation and field-block atomicity in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.101.0 implementation stop reached. Run pentest for this exact commit.`

### v0.102.0 — SETTINGS parsing, validation, and acknowledgement

Status: planned

#### Goal

Deliver settings parsing, validation, and acknowledgement as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document settings parsing, validation, and acknowledgement in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.102.0 implementation stop reached. Run pentest for this exact commit.`

### v0.103.0 — PING

Status: planned

#### Goal

Deliver ping as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document ping in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.103.0 implementation stop reached. Run pentest for this exact commit.`

### v0.104.0 — GOAWAY

Status: planned

#### Goal

Deliver goaway as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document goaway in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.104.0 implementation stop reached. Run pentest for this exact commit.`

### v0.105.0 — RST_STREAM

Status: planned

#### Goal

Deliver rst_stream as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document rst_stream in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.105.0 implementation stop reached. Run pentest for this exact commit.`

### v0.106.0 — WINDOW_UPDATE and checked window arithmetic

Status: planned

#### Goal

Deliver window_update and checked window arithmetic as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document window_update and checked window arithmetic in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.106.0 implementation stop reached. Run pentest for this exact commit.`

### v0.107.0 — Legacy PRIORITY wire elements

Status: planned

#### Goal

Deliver legacy priority wire elements as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document legacy priority wire elements in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.107.0 implementation stop reached. Run pentest for this exact commit.`

### v0.108.0 — PUSH_PROMISE

Status: planned

#### Goal

Deliver push_promise as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document push_promise in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.108.0 implementation stop reached. Run pentest for this exact commit.`

### v0.109.0 — Unknown and extension-frame handling

Status: planned

#### Goal

Deliver unknown and extension-frame handling as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document unknown and extension-frame handling in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.109.0 implementation stop reached. Run pentest for this exact commit.`

### v0.110.0 — Stream-ID allocation, parity, and exhaustion

Status: planned

#### Goal

Deliver stream-id allocation, parity, and exhaustion as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document stream-id allocation, parity, and exhaustion in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.110.0 implementation stop reached. Run pentest for this exact commit.`

### v0.111.0 — Exhaustive stream-state machine

Status: planned

#### Goal

Deliver exhaustive stream-state machine as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document exhaustive stream-state machine in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.111.0 implementation stop reached. Run pentest for this exact commit.`

### v0.112.0 — Connection state, frame sequencing, and full phase audit

Status: planned

#### Goal

Deliver connection state, frame sequencing, and full phase audit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document connection state, frame sequencing, and full phase audit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Perform the phase-boundary full-repository audit, stateful fuzz campaign, corpus review, interoperability campaign, and resource-exhaustion assessment.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.112.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 8 — HTTP/2 semantics and flow control

Phase goal: complete http/2 semantics and flow control without weakening prior security, portability, or conformance evidence.

### v0.113.0 — HPACK and field-block integration

Status: planned

#### Goal

Deliver hpack and field-block integration as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document hpack and field-block integration in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.113.0 implementation stop reached. Run pentest for this exact commit.`

### v0.114.0 — Pseudo-field ordering, uniqueness, and context rules

Status: planned

#### Goal

Deliver pseudo-field ordering, uniqueness, and context rules as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document pseudo-field ordering, uniqueness, and context rules in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.114.0 implementation stop reached. Run pentest for this exact commit.`

### v0.115.0 — Connection-specific field rejection and TE exception

Status: planned

#### Goal

Deliver connection-specific field rejection and te exception as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document connection-specific field rejection and te exception in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.115.0 implementation stop reached. Run pentest for this exact commit.`

### v0.116.0 — HTTP request mapping

Status: planned

#### Goal

Deliver http request mapping as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http request mapping in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.116.0 implementation stop reached. Run pentest for this exact commit.`

### v0.117.0 — HTTP response mapping

Status: planned

#### Goal

Deliver http response mapping as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http response mapping in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.117.0 implementation stop reached. Run pentest for this exact commit.`

### v0.118.0 — Informational responses and trailers

Status: planned

#### Goal

Deliver informational responses and trailers as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document informational responses and trailers in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.118.0 implementation stop reached. Run pentest for this exact commit.`

### v0.119.0 — HTTP/2 Cookie splitting and HTTP/1 joining

Status: planned

#### Goal

Deliver http/2 cookie splitting and http/1 joining as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http/2 cookie splitting and http/1 joining in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.119.0 implementation stop reached. Run pentest for this exact commit.`

### v0.120.0 — Stream-level flow control

Status: planned

#### Goal

Deliver stream-level flow control as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document stream-level flow control in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.120.0 implementation stop reached. Run pentest for this exact commit.`

### v0.121.0 — Connection-level flow control

Status: planned

#### Goal

Deliver connection-level flow control as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document connection-level flow control in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.121.0 implementation stop reached. Run pentest for this exact commit.`

### v0.122.0 — SETTINGS synchronization and outstanding-state tracking

Status: planned

#### Goal

Deliver settings synchronization and outstanding-state tracking as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document settings synchronization and outstanding-state tracking in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.122.0 implementation stop reached. Run pentest for this exact commit.`

### v0.123.0 — Concurrent-stream admission and refusal

Status: planned

#### Goal

Deliver concurrent-stream admission and refusal as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document concurrent-stream admission and refusal in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.123.0 implementation stop reached. Run pentest for this exact commit.`

### v0.124.0 — Outbound scheduling and queue backpressure

Status: planned

#### Goal

Deliver outbound scheduling and queue backpressure as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document outbound scheduling and queue backpressure in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.124.0 implementation stop reached. Run pentest for this exact commit.`

### v0.125.0 — Graceful shutdown and retry-safe GOAWAY behavior

Status: planned

#### Goal

Deliver graceful shutdown and retry-safe goaway behavior as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document graceful shutdown and retry-safe goaway behavior in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.125.0 implementation stop reached. Run pentest for this exact commit.`

### v0.126.0 — Complete server-push lifecycle

Status: planned

#### Goal

Deliver complete server-push lifecycle as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document complete server-push lifecycle in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.126.0 implementation stop reached. Run pentest for this exact commit.`

### v0.127.0 — TLS h2 ALPN and cleartext prior-knowledge integration

Status: planned

#### Goal

Deliver tls h2 alpn and cleartext prior-knowledge integration as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document tls h2 alpn and cleartext prior-knowledge integration in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.127.0 implementation stop reached. Run pentest for this exact commit.`

### v0.128.0 — Full RFC 9113 core conformance and pentest audit

Status: planned

#### Goal

Deliver full rfc 9113 core conformance and pentest audit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document full rfc 9113 core conformance and pentest audit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 7541, RFC 9110, and RFC 9113.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Perform the phase-boundary full-repository audit, stateful fuzz campaign, corpus review, interoperability campaign, and resource-exhaustion assessment.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.128.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 9 — HTTP/2 hardening, translation, and extensions

Phase goal: complete http/2 hardening, translation, and extensions without weakening prior security, portability, or conformance evidence.

### v0.129.0 — Frame-rate and state-transition budgets

Status: planned

#### Goal

Deliver frame-rate and state-transition budgets as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document frame-rate and state-transition budgets in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.129.0 implementation stop reached. Run pentest for this exact commit.`

### v0.130.0 — Rapid-reset and recently-closed-stream defenses

Status: planned

#### Goal

Deliver rapid-reset and recently-closed-stream defenses as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document rapid-reset and recently-closed-stream defenses in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.130.0 implementation stop reached. Run pentest for this exact commit.`

### v0.131.0 — SETTINGS and PING acknowledgement amplification defenses

Status: planned

#### Goal

Deliver settings and ping acknowledgement amplification defenses as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document settings and ping acknowledgement amplification defenses in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.131.0 implementation stop reached. Run pentest for this exact commit.`

### v0.132.0 — CONTINUATION and decompressed-header bomb defenses

Status: planned

#### Goal

Deliver continuation and decompressed-header bomb defenses as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document continuation and decompressed-header bomb defenses in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.132.0 implementation stop reached. Run pentest for this exact commit.`

### v0.133.0 — Tiny WINDOW_UPDATE and flow-control churn defenses

Status: planned

#### Goal

Deliver tiny window_update and flow-control churn defenses as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document tiny window_update and flow-control churn defenses in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.133.0 implementation stop reached. Run pentest for this exact commit.`

### v0.134.0 — Hard outbound queue ceilings

Status: planned

#### Goal

Deliver hard outbound queue ceilings as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document hard outbound queue ceilings in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.134.0 implementation stop reached. Run pentest for this exact commit.`

### v0.135.0 — First-class HTTP/1 to HTTP/2 translation engine

Status: planned

#### Goal

Deliver first-class http/1 to http/2 translation engine as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document first-class http/1 to http/2 translation engine in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.135.0 implementation stop reached. Run pentest for this exact commit.`

### v0.136.0 — Host, :authority, and effective-URI consistency

Status: planned

#### Goal

Deliver host, :authority, and effective-uri consistency as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document host, :authority, and effective-uri consistency in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.136.0 implementation stop reached. Run pentest for this exact commit.`

### v0.137.0 — HTTP/1-to-HTTP/2 connection-field stripping

Status: planned

#### Goal

Deliver http/1-to-http/2 connection-field stripping as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document http/1-to-http/2 connection-field stripping in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.137.0 implementation stop reached. Run pentest for this exact commit.`

### v0.138.0 — CONNECT and tunnel translation across HTTP versions

Status: planned

#### Goal

Deliver connect and tunnel translation across http versions as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document connect and tunnel translation across http versions in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.138.0 implementation stop reached. Run pentest for this exact commit.`

### v0.139.0 — Optional RFC 8441 extended CONNECT

Status: planned

#### Goal

Deliver optional rfc 8441 extended connect as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document optional rfc 8441 extended connect in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.139.0 implementation stop reached. Run pentest for this exact commit.`

### v0.140.0 — RFC 9651 Structured Fields parser

Status: planned

#### Goal

Deliver rfc 9651 structured fields parser as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document rfc 9651 structured fields parser in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.140.0 implementation stop reached. Run pentest for this exact commit.`

### v0.141.0 — RFC 9218 Priority field

Status: planned

#### Goal

Deliver rfc 9218 priority field as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document rfc 9218 priority field in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.141.0 implementation stop reached. Run pentest for this exact commit.`

### v0.142.0 — PRIORITY_UPDATE and priority-settings behavior

Status: planned

#### Goal

Deliver priority_update and priority-settings behavior as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document priority_update and priority-settings behavior in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.142.0 implementation stop reached. Run pentest for this exact commit.`

### v0.143.0 — Stateful hostile-peer and multi-implementation interop campaign

Status: planned

#### Goal

Deliver stateful hostile-peer and multi-implementation interop campaign as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document stateful hostile-peer and multi-implementation interop campaign in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.143.0 implementation stop reached. Run pentest for this exact commit.`

### v0.144.0 — Full intermediary, extension, and denial-of-service audit

Status: planned

#### Goal

Deliver full intermediary, extension, and denial-of-service audit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document full intermediary, extension, and denial-of-service audit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for RFC 8441, RFC 9110, RFC 9112, RFC 9113, RFC 9218, and RFC 9651.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Perform the phase-boundary full-repository audit, stateful fuzz campaign, corpus review, interoperability campaign, and resource-exhaustion assessment.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.144.0 implementation stop reached. Run pentest for this exact commit.`

## Phase 10 — Stable APIs, portability, and production hardening

Phase goal: complete stable apis, portability, and production hardening without weakening prior security, portability, or conformance evidence.

### v0.145.0 — Stable client facade

Status: planned

#### Goal

Deliver stable client facade as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document stable client facade in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.145.0 implementation stop reached. Run pentest for this exact commit.`

### v0.146.0 — Stable origin-server facade

Status: planned

#### Goal

Deliver stable origin-server facade as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document stable origin-server facade in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.146.0 implementation stop reached. Run pentest for this exact commit.`

### v0.147.0 — Stable proxy, gateway, and tunnel facade

Status: planned

#### Goal

Deliver stable proxy, gateway, and tunnel facade as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document stable proxy, gateway, and tunnel facade in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.147.0 implementation stop reached. Run pentest for this exact commit.`

### v0.148.0 — Ergonomic owned API under alloc

Status: planned

#### Goal

Deliver ergonomic owned api under alloc as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document ergonomic owned api under alloc in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.148.0 implementation stop reached. Run pentest for this exact commit.`

### v0.149.0 — Fixed-capacity caller-storage API without allocator

Status: planned

#### Goal

Deliver fixed-capacity caller-storage api without allocator as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document fixed-capacity caller-storage api without allocator in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.149.0 implementation stop reached. Run pentest for this exact commit.`

### v0.150.0 — Standard-error integration and stable diagnostics

Status: planned

#### Goal

Deliver standard-error integration and stable diagnostics as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document standard-error integration and stable diagnostics in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.150.0 implementation stop reached. Run pentest for this exact commit.`

### v0.151.0 — Facade feature matrix and accidental-dependency tests

Status: planned

#### Goal

Deliver facade feature matrix and accidental-dependency tests as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document facade feature matrix and accidental-dependency tests in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.151.0 implementation stop reached. Run pentest for this exact commit.`

### v0.152.0 — Minimal and no-default-feature build matrix

Status: planned

#### Goal

Deliver minimal and no-default-feature build matrix as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document minimal and no-default-feature build matrix in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.152.0 implementation stop reached. Run pentest for this exact commit.`

### v0.153.0 — Full 32-bit arithmetic and capacity matrix

Status: planned

#### Goal

Deliver full 32-bit arithmetic and capacity matrix as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document full 32-bit arithmetic and capacity matrix in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.153.0 implementation stop reached. Run pentest for this exact commit.`

### v0.154.0 — Big-endian, unaligned-access, and serialization matrix

Status: planned

#### Goal

Deliver big-endian, unaligned-access, and serialization matrix as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document big-endian, unaligned-access, and serialization matrix in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.154.0 implementation stop reached. Run pentest for this exact commit.`

### v0.155.0 — x86, Arm, AArch64, and RISC-V target campaign

Status: planned

#### Goal

Deliver x86, arm, aarch64, and risc-v target campaign as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document x86, arm, aarch64, and risc-v target campaign in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.155.0 implementation stop reached. Run pentest for this exact commit.`

### v0.156.0 — Linux, Windows, BSD, macOS, Android, iOS, and future Aesynx adapter contract

Status: planned

#### Goal

Deliver linux, windows, bsd, macos, android, ios, and future aesynx adapter contract as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document linux, windows, bsd, macos, android, ios, and future aesynx adapter contract in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.156.0 implementation stop reached. Run pentest for this exact commit.`

### v0.157.0 — Long-running HTTP/1 soak and fault-injection campaign

Status: planned

#### Goal

Deliver long-running http/1 soak and fault-injection campaign as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document long-running http/1 soak and fault-injection campaign in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.157.0 implementation stop reached. Run pentest for this exact commit.`

### v0.158.0 — Long-running HTTP/2 multiplexing and cancellation soak

Status: planned

#### Goal

Deliver long-running http/2 multiplexing and cancellation soak as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document long-running http/2 multiplexing and cancellation soak in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.158.0 implementation stop reached. Run pentest for this exact commit.`

### v0.159.0 — Independent whole-project security and conformance audit

Status: planned

#### Goal

Deliver independent whole-project security and conformance audit as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document independent whole-project security and conformance audit in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Review the milestone delta for smuggling, ambiguity, panic, truncation, resource exhaustion, response amplification, and state-confusion risks.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.159.0 implementation stop reached. Run pentest for this exact commit.`

### v0.160.0 — Audit remediation, API freeze, and 1.0 release-candidate readiness

Status: planned

#### Goal

Deliver audit remediation, api freeze, and 1.0 release-candidate readiness as one bounded, reviewable capability without claiming later protocol behavior.

#### Deliverables

- Implement and document audit remediation, api freeze, and 1.0 release-candidate readiness in the authoritative crate boundary.
- Add or update paragraph-addressable requirements and errata decisions for the complete declared VEF 1.0 effective specification set.
- Define deterministic errors, progress, capacities, work budgets, and role/state preconditions before accepting hostile input.
- Keep every Rust file below 500 lines, preserve `no_std`, forbid unsafe Rust, and admit no third-party crate.
- Update the threat model, security controls, version index, changelog, release notes, and generated traceability evidence.

#### Verification

- Add focused unit, positive, negative, boundary, truncation, and regression tests for the complete milestone surface.
- Exercise incremental input/output at every single byte split when framing or streaming is involved; otherwise test every domain/state boundary exhaustively where practical.
- Prove capacity exhaustion and invalid state fail before partial publication, unbounded work, panic, or unrelated-state mutation.
- Perform the phase-boundary full-repository audit, stateful fuzz campaign, corpus review, interoperability campaign, and resource-exhaustion assessment.
- Run the full supported Rust matrix, target/platform checks, documentation and package checks, dependency policy, Cargo deny/audit, SBOM comparison, CI, and CodeQL default setup.

#### Exit criteria

All named deliverables and tests are complete; applicable MUST/MUST NOT records are verified; SHOULD decisions are reviewed; no critical or high finding is open; the exact implementation commit is frozen for assessment.

`0.160.0 implementation stop reached. Run pentest for this exact commit.`

## 1.0 release candidates

### v1.0.0-rc.1

Status: planned

Goal: freeze the public API and expose the complete candidate to public interoperability and documentation review.

Deliverables: API freeze, migration guidance, package dry runs, generated RFC coverage, published platform matrix, known limitations, and complete release evidence.

Verification: repeat all repository gates, full stateful fuzzing, independent multi-implementation interop, full manual audit, and exact-commit pentest.

Exit criteria: no new features are accepted and all candidate evidence is reproducible. `1.0.0-rc.1 implementation stop reached. Run pentest for this exact commit.`

### v1.0.0-rc.2

Status: planned

Goal: remediate RC1 findings without expanding scope.

Deliverables: fixes, regression tests, final dependency/source review, final RFC coverage, final MSRV/target declarations, and refreshed evidence.

Verification: repeat every fuzz, pentest, conformance, interop, portability, package, and provenance gate.

Exit criteria: no unresolved critical/high findings and no unreviewed behavior change. `1.0.0-rc.2 implementation stop reached. Run pentest for this exact commit.`

### v1.0.0

Status: planned

Goal: publish the first serious production-ready VEF HTTP crate.

Release only when every applicable MUST/MUST NOT is verified, every SHOULD decision is documented, caller-storage builds work without an allocator, protocol cores are `no_std` and unsafe-free, HTTP/0.9 cannot activate accidentally, HTTP/1 has one framing interpretation, HTTP/2 state transitions and flow control pass exhaustive evidence, HPACK remains bounded, every declared role is covered, platform matrices are published, independent-audit remediation is verified, and HTTP/3 remains explicitly out of scope.
