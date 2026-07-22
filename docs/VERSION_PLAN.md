# VEF Version Plan

Status: planning document

`1.0.0` is the first serious production-ready VEF release. Each `0.x` minor
release owns one reviewable security or protocol outcome. Patch releases may
split or remediate a milestone, but cannot silently defer a required behavior.

This compact index is subordinate to [`RELEASE_PLAN.md`](RELEASE_PLAN.md),
which gives every version a concrete acceptance contract, verification,
dependency context, exit criteria, and exact-commit pentest stop.

## Gap closure map

The latest design review gates content/method execution behind preconditions,
separates pre-action evidence from retrieval metadata, resolves obsolete dates
from a complete instant, streams standalone partial responses without forced
retention, and binds optional cross-request assembly to pre-output linear,
shard-isolated invalidation namespaces, structurally safe leases, explicit semantic
replacement identity, and borrow-aware physical reclamation. The roadmap
remains at minor `0.225.0` with focused patch stops at
`0.157.1`–`0.157.5`, `0.180.1`–`0.180.5`, `0.181.1`–`0.181.2`, and
`0.182.1`.

| Gap closed | Versions | Binding consequence |
| --- | --- | --- |
| Early resource ceilings | `0.7.0`; replay at `0.211.0` | Set measurable ceilings before layouts/state machines land and verify every later component against them. |
| Capacity versus protocol errors | `0.10.0` | Local storage/backpressure/control-capacity failures never masquerade as peer protocol violations. |
| Status-code validity | `0.12.0` | Limit StatusCode to 100..=599, preserve unknown valid codes, retain received 600..=999 only as typed invalid wire evidence, process them under client 5xx policy, and prohibit serialization. |
| URI path/query identity | `0.17.0`, `0.128.0`, `0.160.0` | Store raw path and optional query separately, preserve absent versus empty query and percent encoding, map exact `:path`, and perform only required empty-path-to-slash conversion. |
| Trusted effective target | `0.19.0`, `0.40.0`, `0.156.0`, `0.203.0`, `0.208.0` | Bind fixed/gateway/transport scheme evidence to connection generation, apply explicit precedence/conflict policy before publication, and reuse the complete scheme/authority/path/query decision. |
| CONNECT authority and policy | `0.40.0`, `0.64.0`, `0.161.0` | Require explicit checked port 1..=65535, bracket-safe host parsing, no Host/default substitution, caller target authorization before external action, no request content, strict success fields, and non-cacheability. |
| Endpoint-bound CONNECT admission | `0.19.0`, `0.64.0`, `0.130.0`, `0.161.0`, `0.184.0` | Stage lexical authorization, attempt token, caller resolution and per-endpoint policy, then require generation-matched resolved endpoint and actual peer evidence before success/output/tunnel publication without giving core DNS/socket authority. |
| One-shot authorization capabilities | `0.19.0`, `0.64.0`, `0.130.0`, `0.157.3`, `0.184.0` | Seal non-Copy/non-Clone tokens with engine-owned identities, consume once in one request/exchange, invalidate on every terminal/policy transition, reject same-generation replay, and promise logical—not physical—caller-buffer erasure. |
| HTTP/2 CONNECT tunnel DATA | `0.130.0`, `0.133.0`–`0.137.0`, `0.161.0` | Classify and fixed-capacity-reset pending DATA before flow control exists, add stream/connection accounting only at their owners, then add borrowed acknowledgement/credit and outbound directional commands before translation reuse. |
| 205 zero-content semantics | `0.63.0`, `0.130.0`, `0.137.0`, `0.160.0` | Guarantee zero outbound content, retain ordinary inbound framing for synchronization, diagnose and suppress malicious nonzero content, and test HTTP/1 pipelines plus HTTP/2 DATA/END_STREAM. |
| Terminal 101 response branch | `0.59.0`, `0.60.0`, `0.67.0` | Separate informational-then-final from terminal 101, prohibit HTTP/1.0 1xx emission, complete the request and any required 100 first, and reject all HTTP operations after handoff. |
| WebSocket entropy | `0.69.0` | Require a fresh caller/adapter-provided 16-byte nonce; core never invents weak entropy. |
| Directional extended CONNECT setting | `0.139.0`, `0.162.0` | Separate peer-enabled outbound initiation from committed local inbound advertisement, accept only 0/1, prohibit withdrawal after 1, and fail unadvertised inbound requests before publication. |
| Bidirectional WebSocket bridge | `0.69.0`, `0.162.0`, `0.163.0` | Bridge both directions; map schemes and retained negotiation/end-to-end fields exactly, isolate key/accept processing to HTTP/1, gate settings on availability, and commit both sides before data. |
| HPACK encoder atomicity | `0.98.0` | Couple dynamic-table mutation to committed output bytes and formally prove retry/cancel/partial-output behavior. |
| Sensitive HPACK indexing | `0.97.0` | Use typed directives, conservative secret defaults, never-indexed preservation, decision noninterference, diagnostic redaction, and non-bypassable profiles. |
| Generic HTTP authentication grammar | `0.97.0`, `0.157.2` | Add dependency-free `vef-auth`; preserve raw/case-insensitive schemes, compare parameter names case-insensitively, reject duplicates, quote generated realm, enforce terminal token68 padding, resolve comma ambiguity, and prevent secret ownership/diagnostic/index exposure. |
| Hop-scoped proxy authentication | `0.19.0`, `0.65.0`, `0.97.0`, `0.157.2`–`0.157.3`, `0.184.0` | Bind validated proxy credentials to hop/connection/generation/exchange, consume before origin forwarding, permit only named cooperative relay, scope challenges/info to the next client, require challenged 407, redact/never-index/exclude from TRACE, and force fresh HTTP/1 CONNECT authentication retry. |
| Compression principals | `0.97.0`, `0.190.0` | Tag dynamic entries by caller provenance, prohibit cross-principal lookup on shared/coalesced connections, and default unknown provenance to non-indexing. |
| Compression provenance bookkeeping | `0.90.0`–`0.91.0`, `0.97.0` | Keep immutable provenance as an encoder sidecar that never changes HPACK size/index order, and remove it atomically with entry eviction or reset. |
| HPACK wire legality | `0.82.0`–`0.93.0` | Accept non-shortest valid integers, emit canonical integers, reject illegal Huffman EOS/padding and invalid indices, and emit at most two ordered table-size changes. |
| SETTINGS dependency ordering | `0.108.0` then `0.124.0`, `0.135.0`, `0.141.0`, `0.143.0` | Parse/store early; integrate only after HPACK, streams/windows, admission, and scheduling exist. |
| HTTP/2 publication order | `0.127.0` before `0.128.0` | Malformed names/values, pseudo-fields, context, and initial Content-Length are rejected before mapped messages can become observable. |
| Never-untracked HTTP/2 rejection state | foundation at `0.117.0`; push integration at `0.145.0`; assembly transaction at `0.181.0`; stable API at `0.191.0`; diagnostics at `0.193.0` | Preflight tombstone/cutoff capacity or convert the live/reserved slot in place; an accepted ID is always a slot, tombstone, or retained bounded-shutdown record. Push rejection retains its tombstone through local CANCEL backpressure and peer cutoff classification. If tracking cannot be represented, emit typed `StreamTrackingUnavailable`/`PushRejectionTrackingUnavailable` bounded connection shutdown without forgetting the ID. |
| HTTP/2 push admission and assembly binding | lifecycle at `0.145.0`; handle/provenance gate at `0.181.0`; partial/full consumption at `0.181.1`–`0.181.2`; stabilize at `0.191.0`; diagnostics at `0.193.0`; compile-fail at `0.197.0` | First require complete safe/cacheable/content-free promised requests, trusted authority, separate slot/work limits, and rollback-capable prepublication admission. Once assembly exists, atomically preflight the promised slot, invalidation handle, independent minimal immutable `PushedAssemblyProvenance`, and rejection/cutoff tracking. Provenance derives from the promised target plus associated caller policy but never borrows associated-stream storage; teardown, reuse, and later policy changes cannot mutate it. `PushedAssemblyProvenanceCapacity` rejects before publication. Capacity rejection converts the slot in place, publishes nothing, preserves HPACK/associated state, and emits stream-local CANCEL or bounded shutdown. Accepted pushed 200/206 uses the same exact correlation and invalidation machinery as ordinary responses. |
| HPACK refusal synchronization | `0.123.0`, `0.148.0` | RST/refusal/cancellation never abandons an inbound block; REFUSED_STREAM requires capacity to finish HPACK invisibly, otherwise the connection shuts down boundedly. |
| HTTP/2 DATA and command ownership | `0.136.0`–`0.137.0` | Application acknowledgement, not parsing, releases inbound credit; outbound HEADERS/DATA/trailers/END_STREAM and partial output use one per-stream lifecycle. |
| HTTP/2 activation/shutdown | `0.119.0`–`0.122.0` | Make preface, first SETTINGS, frame legality, fragmentation, stream exhaustion, GOAWAY, retry cutoff, and backpressured shutdown explicit. |
| HTTP/2 error-scope isolation | `0.121.0` | Map every violation to exact code/scope, apply stream-only typed deltas, reserve one RST_STREAM/GOAWAY, and prove unrelated state is unchanged. |
| HTTP/2 frame envelopes | `0.103.0`–`0.114.0` | Bind exact lengths, stream IDs, flags, reserved bits, padding arithmetic, optional minima, outbound zeroing, and RFC error scope per frame type. |
| Field-block frame error scope | `0.105.0`, `0.114.0` | Distinguish undersized mandatory layouts as connection FRAME_SIZE_ERROR, invalid padding/identifiers as connection PROTOCOL_ERROR, and HEADERS self-dependency as stream PROTOCOL_ERROR. |
| Unknown-frame isolation | `0.115.0` | Incrementally drain bounded unknown frames without allocation, mutation, publication, or field-block interleaving unless an enabled extension owns the type. |
| DATA padding and frame limits | `0.104.0`, `0.136.0`, `0.143.0` | Separate flow-controlled padded payload, application data, Content-Length bytes, local inbound limit, peer outbound limit, and absolute RFC ceiling. |
| Receive-credit emission | `0.136.0` | Account discarded padding internally at once but coalesce WINDOW_UPDATE under threshold, rate, and amplification budgets. |
| SETTINGS ACK sequencing | `0.139.0` | Track committed local SETTINGS in a bounded FIFO, ACK oldest first, reject unsolicited ACK, inject timeouts, and reserve mandatory output. |
| Stream concurrency accounting | `0.140.0`–`0.141.0` | Count open/half-closed but not reserved streams, constrain REFUSED_STREAM to pre-application rejection, preserve existing streams after reductions, and distinguish local table capacity. |
| Extension SETTINGS ownership | `0.143.0`, `0.145.0`, `0.162.0`, `0.175.0` | Apply MAX_FRAME_SIZE before ACK and integrate push, extended CONNECT, and priority settings only in their owning state machines. |
| Scheduler and limit activation | `0.142.0`–`0.143.0` | Preserve field-block contiguity, mandatory-control capacity, cross-stream fairness, cancellation safety, and commit-time SETTINGS segmentation/receive-limit transitions. |
| Fail-closed protocol selection | `0.146.0` | Require authenticated exact h2 ALPN or explicit cleartext policy, consume failed-selection bytes once, and freeze choice when preface processing starts. |
| Flood and Rapid Reset accounting | `0.147.0`–`0.153.0` | Charge independent non-refundable work before admission, refill saturating budgets from injected time, reserve required replies/shutdown, and permit caller-shared cross-connection limits. |
| HTTP/1 transfer-coding roles | `0.43.0`–`0.45.0` | Require final chunked on requests, permit response close delimitation for other/non-final transfer codings, reject repeated chunked, and separate unsupported coding from malformed order. |
| Chunk-extension BWS grammar | `0.50.0` | Accept BWS around semicolon and equals exactly, charge raw whitespace to limits, trim before semantic interpretation, and retain injection/quoting rejection. |
| RFC 9931 optimistic-data closure | `0.65.0` | Require CONNECT proxy wait-or-close behavior, mandatory close after rejected CONNECT, no pre-101 WebSocket or HTTP/1.x CONNECT-UDP data, and no failed-transition reparsing. |
| Reusable media-type syntax and policy | `0.157.5`, consumed from `0.158.0` | Preserve ordered duplicate parameters and RFC-valid empty slots, forbid whitespace around `=`, distinguish empty quoted from missing values, then apply separate conservative generated-media policy without narrowing received extension syntax. |
| Complete TRACE/OPTIONS semantics | `0.158.0` | Complete Max-Forwards absence/zero behavior, prohibit generated TRACE content/secrets, sanitize bounded reflection, require v0.157.5-valid Content-Type evidence for generated OPTIONS content, and mark responses non-cacheable. |
| Exact Via forwarding and privacy | `0.157.1`, `0.184.0`, `0.185.0` | Parse bounded ordered members/comments, append inbound protocol/version plus configured pseudonym, never replace/combine, cover proxy and gateway applicability, preflight capacity, and expose caller-owned loop detection without input-derived identity. |
| Definition-permitted trailers | `0.52.0`, `0.53.0`, `0.131.0`, `0.137.0`, `0.157.2`, `0.160.0` | Core field permission exists early; authentication-info generation remains unavailable/classification-only until `vef-auth` owns scheme permission at 0.157.2; received trailers remain capability-free, separate, synchronized, non-retroactive, and destination translation reauthorizes them. |
| Protocol-specific 426 | `0.126.0`, `0.129.0`, `0.137.0`, `0.160.0`, `0.182.1` | Require Upgrade only for HTTP/1 generation, prohibit local HTTP/2 426, distinguish forbidden received Upgrade from semantic 426-without-Upgrade, and prevent strip-and-forward translation. |
| Injected civil time | `0.157.4`, `0.160.0`, `0.180.1`, `0.182.1` | Core owns generic years 0001..=9999 and complete-instant evidence; HTTP dates reject pre-1900 years; optional I/O supplies evidence; monotonic time stays separate; and RFC 850 compares the whole candidate instant at exactly 50 years versus plus one second. |
| Conditional content/method gate | `0.180.2`–`0.180.3`, integrated at `0.183.0` | Publish only a read-only pending request; current pre-action evidence authorizes every conditional method, retrieval-only 200 metadata supports GET/HEAD, and no body, 100 Continue, or side effect precedes a one-shot permit. The mutation caused by a consumed execution permit cannot revoke that admission; response construction uses fresh evidence. |
| Conditional and range ownership | `0.180.1`–`0.180.5`, consumed at `0.182.1` | Add dependency-free `vef-conditions`; parse/compare validators, evaluate conditional fields in RFC order, bound checked Range/Content-Range work, seal generation outcomes, final-validate exact outbound client requests, and consume sealed media-type classification over both protocols. |
| Content-Range generic validity | `0.180.3`, consumed at `0.181.1` | Unknown units remain distinct from malformed input but must still pass one range response alternative, checked decimals, ordered endpoints, complete-length bounds, limits, and injection checks; they never grant recombination authority. |
| Exact partial media-type classification | `0.180.5`, consumed at `0.181.1` | Reuse v0.157.5 grammar, collapse valid present non-multipart input to one state, enforce RFC 2046 boundary length/grammar, and make exact multipart/byteranges with missing/invalid boundary a semantic violation that grants no partial authority. |
| Explicit partial delivery authority | lands at `0.181.1` | Accept freely constructible StreamOnly/RetainOnly/StreamAndRetain preference, issue a sealed generation-bound selected-delivery permit after validation, retain before publication/acknowledgement, and expose a prefix only when every received octet was retained. |
| Streaming standalone partial input | `0.181.0`–`0.181.1` | Validate the classified 206 head, stream borrowed accounted chunks without forced retention/allocation, and issue terminal standalone proof even with absent/weak validators; storage is optional and only stored segments can become combinable. |
| Malformed versus incomplete content | `0.127.0`, `0.130.0`, `0.181.1` | Only premature EOF/reset/failure/cancellation after a valid complete head can yield an incomplete prefix; clean HTTP/2 END_STREAM length mismatch, invalid fields/HPACK/framing, ambiguous HTTP/1 framing, and malformed chunks yield no prefix capability. |
| Structurally safe stored bytes | `0.181.1`–`0.181.2` | Build optional leases only from exclusive slices/sealed arenas, freeze them after engine writes, prohibit public trust constructors and caller storage traits, require fenced DMA adapters, and obtain output through safe splitting or a separate arena. Semantic invalidation rejects stale operations immediately but physical reuse waits for every body/identity/output lease; until then allocation returns local LeaseHeld/capacity. |
| Variant identity versus evidence | `0.181.1`–`0.181.2` | Separate semantic exact-request/Vary/principal/privacy/navigation identity from per-request/response/storage provenance evidence; assembly verifies fresh evidence but compares only identity, while trailer Vary remains NoRecombine. |
| Long-lived Vary identity storage | lands at `0.181.1` | Retain canonical equality bytes through immutable request leases or exclusive-slice/sealed-arena engine-frozen storage, prohibit alias/trust/DMA mutation, redact sensitive values, require caller scrub after release, and downgrade locally on capacity/release. |
| One-time Vary normalization | lands at `0.181.1` | Activate profile-capped work/output accounting during identity creation, retain canonical bytes plus normalizer provenance (raw is canonical when no normalizer), avoid redundant sensitive raw copies, preserve field-defined equivalence exactly, and make every later comparison parse-free. |
| Linear, bounded full-200 fallback invalidation | reserve at `0.181.0`; evidence at `0.181.1`; consume at `0.181.2`; stabilize at `0.191.0`; compile-fail at `0.197.0` | Before local request output, or after complete pushed-request validation but before publication, reserve a non-Copy/non-Clone exact-correlation handle. A pushed handle owns independent immutable arena-bound provenance and never follows associated-stream storage or later policy changes. Local exhaustion backpressures; push failure stays tracked and publishes nothing. Hold capabilities through ordinary/pushed terminal backpressure and release once. Keyed/unkeyed replacement is identical; arena rotation remains corruption/caller-policy only. |
| Profile-capped overlap work | lands at `0.181.2` | Validate public requested budgets before sorting into sealed plan-bound active budgets capped by the resource profile; charge monotonically with checked arithmetic and forbid reset, enlargement, or cross-plan reuse. |
| Conflicting partial quarantine | lands at `0.181.2` | Sort intervals under bounded work, deduplicate equal overlaps, fail unequal octets with zero output, and clear quarantine only by complete same-key 200 replacement or destruction followed by a different-validator/new-generation empty context—never 304, unchanged revalidation, or a separate selection context. |
| Trailer-finalized combination | `0.52.0`, `0.131.0`, `0.181.1`–`0.181.2` | Stream under the validated head, but finalize stored combination eligibility only after trailers; a permitted trailer ETag may supply the validator, conflicts are deterministic, and trailers cannot change range/domain/head ordinal. |
| Local head ordering | `0.181.0`, implemented at `0.181.2` | The correlation engine mints a checked monotonic ordinal when each validated head is atomically published—not at body completion and never from peer Date—so body delay, retry, and reordering cannot manipulate header-source selection. |
| Representation evidence split | `0.180.2`–`0.180.3`, `0.182.1`, `0.183.0` | `CurrentRepresentationEvidence` holds pre-action existence/validator state for all methods; `WouldBe200Snapshot` is a retrieval-only refinement for range, 206, and 304; unsafe success obtains new post-action evidence rather than retroactively invalidating its permit. |
| Exact validated-response binding | `0.182.1`, `0.183.0`, `0.191.0`, `0.192.0`, `0.197.0` | `ValidatedResponse` owns or immutably borrows the precise ordered head, framing, sensitivity/indexing, body, and trailer plan; engines consume it whole, never `(raw_head, permit)`, and every mutation requires revalidation. |
| Mandatory semantic reserve | `0.25.0`, `0.38.0`, `0.182.1`, `0.183.0`, `0.191.0` | Reserve engine-only validation slots and frozen-head storage for 400/414/431 and other mandatory output; application work cannot exhaust it, and total reserve failure commits one zero-partial-output close/shutdown action. |
| Unbypassable response semantics | `0.54.0`, `0.137.0`, `0.157.2`, `0.180.1`–`0.181.2`, `0.182.1`, `0.183.0`, `0.191.0`, `0.192.0`, `0.194.0`, `0.197.0` | Make `vef-semantics` depend on core/auth/media-type/conditions, require frozen sealed request/response objects in both engines, remove raw public serialization, retain validation through facade/fixed/alloc/features, and compile-fail bypasses. |
| Role-aware response semantics | `0.157.2`, `0.157.4`, `0.180.1`–`0.181.2`, `0.182.1`, `0.183.0` | Validate 401/405/426, retrieval-snapshot-bound 206/304/416 metadata and Date policy, client partial segments/combinations, and the complete RFC 9110 matrix; preserve multipart opaquely and separate local InvalidState from received policy/forwarding. |
| Server-wide OPTIONS final hop | `0.158.0`, `0.160.0` | Preserve absolute-form through intermediate forward proxies, convert empty-path/absent-query OPTIONS to `*` only at the origin-facing hop, and keep empty query and `/` resource-specific. |
| Structured Fields conformance profiles | `0.168.0`, `0.170.0`, `0.173.0` | Overwrite duplicate parameters/dictionary members with the final value, meet RFC 9651 mandatory minima, label smaller profiles constrained, and keep capacity distinct from syntax. |
| HTTP/2 PRIORITY_UPDATE | `0.178.0` | Own only frame type 0x10 with receiver-server-relative request and push states, exact errors, concurrency bounds, and a fixed ignore-malformed-value policy. |
| Concrete acceptance contracts | `0.1.0`–`0.225.0` | Eliminate generic state-graph and family templates; every type, parser, codec, protocol, adapter, campaign, audit, and release stop states its actual accepted input, state, error, capacity, and publication evidence. |
| Intermediary and retry semantics | `0.158.0`, `0.159.0`, `0.182.0` | Cover required forward-proxy fields and never infer replay safety from GOAWAY/421 alone. |
| Structured Fields and priority | `0.164.0`–`0.179.0` | Give an optional dependency-free crate explicit ownership, place complete bare-item dispatch after every item grammar, and add bounded RFC 9651/RFC 9218 scheduling, intermediary, and flood behavior. |
| Translation and byte handoff | `0.155.0` then `0.160.0`; `0.188.0` | Separate representation from validated mapping and transfer post-transition bytes exactly once without HTTP reinterpretation. |
| Protocol-specific tunnel closure | `0.186.0` | HTTP/1 EOF flushes then closes both sides; HTTP/2/RFC8441 END_STREAM is a directional FIN that preserves reverse traffic until both finish, while resets/fatal errors abort both. |
| TLS and bare-metal contracts | `0.204.0`–`0.205.0` plus adapter milestones | Enumerate RFC 9113 TLS prerequisites and concrete short-I/O/readiness/deadline/EOF/alignment/scatter-gather behavior. |

## Standards disposition

RFC 6455 remains an optional source-locked opening-handshake extension. RFC
9298 remains source-locked but not applicable unless HTTP/1.1 CONNECT-UDP enters
scope. Via, Max-Forwards, and TE map to RFC 9110/9112. RFC 7239 `Forwarded`
transformation remains outside 1.0.

## Universal release gate

Every milestone tests its new outcome plus all earlier relevant behavior,
enforces the active resource profile, updates requirement/errata and threat
evidence, passes Rust `1.90.0`–`1.97.1` and target gates, and stops for an
exact-commit pentest. Tests cannot depend on later milestones. Phase exits add
full conformance, fuzz/model replay, interoperability, exhaustion assessment,
and manual security review.

## Phase 1 — Foundation and shared semantics (`0.1.0`–`0.27.0`)

No parser may publish protocol state until checked progress, storage, event ownership, capacity disposition, resource ceilings, limits, roles, and evidence contracts exist.

| Version | Primary outcome | Sequence context |
| --- | --- | --- |
| `0.1.0` | Workspace, crate boundaries, licenses, security policy, and release evidence | Repository foundation; Unlocks Core module skeleton and authority boundaries. |
| `0.2.0` | Core module skeleton and authority boundaries | Requires Workspace, crate boundaries, licenses, security policy, and release evidence; Unlocks Checked byte cursor with no unchecked indexing. |
| `0.3.0` | Checked byte cursor with no unchecked indexing | Requires Core module skeleton and authority boundaries; Unlocks Non-zero parser progress and explicit blocked states. |
| `0.4.0` | Non-zero parser progress and explicit blocked states | Requires Checked byte cursor with no unchecked indexing; Unlocks Checked protocol-size domains. |
| `0.5.0` | Checked protocol-size domains | Requires Non-zero parser progress and explicit blocked states; Unlocks Decode, work, transition, and response budgets. |
| `0.6.0` | Decode, work, transition, and response budgets | Requires Checked protocol-size domains; Unlocks Initial deterministic resource profiles and measurement hooks. |
| `0.7.0` | Initial deterministic resource profiles and measurement hooks | Requires Decode, work, transition, and response budgets; Unlocks Caller-owned arenas and fixed-capacity stores. |
| `0.8.0` | Caller-owned arenas and fixed-capacity stores | Requires Initial deterministic resource profiles and measurement hooks; Unlocks Structured errors and error-scope taxonomy. |
| `0.9.0` | Structured errors and error-scope taxonomy | Requires Caller-owned arenas and fixed-capacity stores; Unlocks Capacity exhaustion and protocol-violation disposition taxonomy. |
| `0.10.0` | Capacity exhaustion and protocol-violation disposition taxonomy | Requires Structured errors and error-scope taxonomy; Unlocks Case-sensitive extension-capable Method. |
| `0.11.0` | Case-sensitive extension-capable Method | Requires Capacity exhaustion and protocol-violation disposition taxonomy; Unlocks Validated StatusCode with unknown-code preservation. |
| `0.12.0` | Validated StatusCode with unknown-code preservation | Requires Case-sensitive extension-capable Method; Unlocks HTTP version and wire-version representation. |
| `0.13.0` | HTTP version and wire-version representation | Requires Validated StatusCode with unknown-code preservation; Unlocks Case-insensitive validated FieldName. |
| `0.14.0` | Case-insensitive validated FieldName | Requires HTTP version and wire-version representation; Unlocks Byte-oriented FieldValue with raw and semantic views. |
| `0.15.0` | Byte-oriented FieldValue with raw and semantic views | Requires Case-insensitive validated FieldName; Unlocks Ordered FieldLine and FieldSection storage. |
| `0.16.0` | Ordered FieldLine and FieldSection storage | Requires Byte-oriented FieldValue with raw and semantic views; Unlocks Request-target, URI, and authority types. |
| `0.17.0` | Request-target, URI, and authority types | Requires Ordered FieldLine and FieldSection storage; Unlocks Request and response control-data types. |
| `0.18.0` | Request and response control-data types | Requires Request-target, URI, and authority types; Unlocks Role, profile, and policy types. |
| `0.19.0` | Role, profile, and policy types | Requires Request and response control-data types; Unlocks Minimal synchronous I/O contracts. |
| `0.20.0` | Minimal synchronous I/O contracts | Requires Role, profile, and policy types; Unlocks Runtime-neutral readiness and poll contracts. |
| `0.21.0` | Runtime-neutral readiness and poll contracts | Requires Minimal synchronous I/O contracts; Unlocks Injected monotonic clock and deadline contracts. |
| `0.22.0` | Injected monotonic clock and deadline contracts | Requires Runtime-neutral readiness and poll contracts; Unlocks Cancellation, close, and bounded-backpressure contracts. |
| `0.23.0` | Cancellation, close, and bounded-backpressure contracts | Requires Injected monotonic clock and deadline contracts; Unlocks Deterministic fake transport and driver harness. |
| `0.24.0` | Deterministic fake transport and driver harness | Requires Cancellation, close, and bounded-backpressure contracts; Unlocks Engine event, command, acknowledgement, and publication contract. |
| `0.25.0` | Engine event, command, acknowledgement, and publication contract | Requires Deterministic fake transport and driver harness; Unlocks Requirement, applicability, and errata evidence system. |
| `0.26.0` | Requirement, applicability, and errata evidence system | Requires Engine event, command, acknowledgement, and publication contract; Unlocks Foundation Kani campaign, audit, and pentest. |
| `0.27.0` | Foundation Kani campaign, audit, and pentest | Requires Requirement, applicability, and errata evidence system; Unlocks HTTP/1 role and parser profiles. |

## Phase 2 — HTTP/1 and isolated HTTP/0.9 (`0.28.0`–`0.81.0`)

HTTP/1 has one octet-level inbound/outbound interpretation, bounded body ownership, exact transition handoff, typed dispositions, and no HTTP/0.9 fallback.

| Version | Primary outcome | Sequence context |
| --- | --- | --- |
| `0.28.0` | HTTP/1 role and parser profiles | Requires Foundation Kani campaign, audit, and pentest; Unlocks Incremental HTTP/1 request-line parser. |
| `0.29.0` | Incremental HTTP/1 request-line parser | Requires HTTP/1 role and parser profiles; Unlocks Incremental HTTP/1 status-line parser. |
| `0.30.0` | Incremental HTTP/1 status-line parser | Requires Incremental HTTP/1 request-line parser; Unlocks Every-byte fragmentation support. |
| `0.31.0` | Every-byte fragmentation support | Requires Incremental HTTP/1 status-line parser; Unlocks Strict CRLF and separately named LF compatibility. |
| `0.32.0` | Strict CRLF and separately named LF compatibility | Requires Every-byte fragmentation support; Unlocks Incremental HTTP/1 field-line parser. |
| `0.33.0` | Incremental HTTP/1 field-line parser | Requires Strict CRLF and separately named LF compatibility; Unlocks Explicit OWS handling with raw-value preservation. |
| `0.34.0` | Explicit OWS handling with raw-value preservation | Requires Incremental HTTP/1 field-line parser; Unlocks Injection-proof HTTP/1 head serialization. |
| `0.35.0` | Injection-proof HTTP/1 head serialization | Requires Explicit OWS handling with raw-value preservation; Unlocks Role-specific obs-fold and invalid-field disposition. |
| `0.36.0` | Role-specific obs-fold and invalid-field disposition | Requires Injection-proof HTTP/1 head serialization; Unlocks Field count, line, and section caps. |
| `0.37.0` | Field count, line, and section caps | Requires Role-specific obs-fold and invalid-field disposition; Unlocks Typed HTTP/1 protocol-error response and close actions. |
| `0.38.0` | Typed HTTP/1 protocol-error response and close actions | Requires Field count, line, and section caps; Unlocks HTTP/1.1 Host validation and duplicate rejection. |
| `0.39.0` | HTTP/1.1 Host validation and duplicate rejection | Requires Typed HTTP/1 protocol-error response and close actions; Unlocks Method and request-target-form coherence. |
| `0.40.0` | Method and request-target-form coherence | Requires HTTP/1.1 Host validation and duplicate rejection; Unlocks Checked Content-Length grammar. |
| `0.41.0` | Checked Content-Length grammar | Requires Method and request-target-form coherence; Unlocks Repeated and comma-list Content-Length resolution. |
| `0.42.0` | Repeated and comma-list Content-Length resolution | Requires Checked Content-Length grammar; Unlocks Transfer-Encoding grammar and ordering. |
| `0.43.0` | Transfer-Encoding grammar and ordering | Requires Repeated and comma-list Content-Length resolution; Unlocks TE/CL conflict resolution and mandatory close action. |
| `0.44.0` | TE/CL conflict resolution and mandatory close action | Requires Transfer-Encoding grammar and ordering; Unlocks Central HTTP/1 message-body-length algorithm. |
| `0.45.0` | Central HTTP/1 message-body-length algorithm | Requires TE/CL conflict resolution and mandatory close action; Unlocks Fixed-length body decoder. |
| `0.46.0` | Fixed-length body decoder | Requires Central HTTP/1 message-body-length algorithm; Unlocks Close-delimited response decoder. |
| `0.47.0` | Close-delimited response decoder | Requires Fixed-length body decoder; Unlocks Checked chunk-size parser. |
| `0.48.0` | Checked chunk-size parser | Requires Close-delimited response decoder; Unlocks Incremental chunk-data state. |
| `0.49.0` | Incremental chunk-data state | Requires Checked chunk-size parser; Unlocks Bounded chunk-extension parser. |
| `0.50.0` | Bounded chunk-extension parser | Requires Incremental chunk-data state; Unlocks Last-chunk and trailer transition. |
| `0.51.0` | Last-chunk and trailer transition | Requires Bounded chunk-extension parser; Unlocks Trailer declarations and prohibited-trailer policy. |
| `0.52.0` | Trailer declarations and prohibited-trailer policy | Requires Last-chunk and trailer transition; Unlocks Chunked encoder with partial-output state. |
| `0.53.0` | Chunked encoder with partial-output state | Requires Trailer declarations and prohibited-trailer policy; Unlocks Unified HTTP/1 outbound message state machine. |
| `0.54.0` | Unified HTTP/1 outbound message state machine | Requires Chunked encoder with partial-output state; Unlocks Inbound body acknowledgement, drain, discard, cancellation, and reuse. |
| `0.55.0` | Inbound body acknowledgement, drain, discard, cancellation, and reuse | Requires Unified HTTP/1 outbound message state machine; Unlocks HTTP/1.1 persistence and Connection semantics. |
| `0.56.0` | HTTP/1.1 persistence and Connection semantics | Requires Inbound body acknowledgement, drain, discard, cancellation, and reuse; Unlocks Sequential request/response connection state. |
| `0.57.0` | Sequential request/response connection state | Requires HTTP/1.1 persistence and Connection semantics; Unlocks Optional bounded pipelining queue. |
| `0.58.0` | Optional bounded pipelining queue | Requires Sequential request/response connection state; Unlocks Informational response lifecycle. |
| `0.59.0` | Informational response lifecycle | Requires Optional bounded pipelining queue; Unlocks Expect: 100-continue state. |
| `0.60.0` | Expect: 100-continue state | Requires Informational response lifecycle; Unlocks EOF, truncation, and incomplete-message rules. |
| `0.61.0` | EOF, truncation, and incomplete-message rules | Requires Expect: 100-continue state; Unlocks HEAD response-framing context. |
| `0.62.0` | HEAD response-framing context | Requires EOF, truncation, and incomplete-message rules; Unlocks 1xx, 204, 205, 304, and body-forbidden response handling. |
| `0.63.0` | 1xx, 204, 205, 304, and body-forbidden response handling | Requires HEAD response-framing context; Unlocks CONNECT request and successful tunnel transition. |
| `0.64.0` | CONNECT request and successful tunnel transition | Requires 1xx, 204, 205, 304, and body-forbidden response handling; Unlocks RFC 9931 optimistic-data protections. |
| `0.65.0` | RFC 9931 optimistic-data protections | Requires CONNECT request and successful tunnel transition; Unlocks Connection-option, Upgrade, and hop-by-hop field grammar. |
| `0.66.0` | Connection-option, Upgrade, and hop-by-hop field grammar | Requires RFC 9931 optimistic-data protections; Unlocks 101 Switching Protocols transition and publication barrier. |
| `0.67.0` | 101 Switching Protocols transition and publication barrier | Requires Connection-option, Upgrade, and hop-by-hop field grammar; Unlocks Separate WebSocket handshake crate, key, version, and token validation. |
| `0.68.0` | Separate WebSocket handshake crate, key, version, and token validation | Requires 101 Switching Protocols transition and publication barrier; Unlocks Caller-supplied WebSocket nonce and entropy boundary. |
| `0.69.0` | Caller-supplied WebSocket nonce and entropy boundary | Requires Separate WebSocket handshake crate, key, version, and token validation; Unlocks WebSocket accept generation and client/server validation. |
| `0.70.0` | WebSocket accept generation and client/server validation | Requires Caller-supplied WebSocket nonce and entropy boundary; Unlocks WebSocket negotiation, origin metadata, and byte-publication barrier. |
| `0.71.0` | WebSocket negotiation, origin metadata, and byte-publication barrier | Requires WebSocket accept generation and client/server validation; Unlocks Safe forwarding and explicit reframing plan. |
| `0.72.0` | Safe forwarding and explicit reframing plan | Requires WebSocket negotiation, origin metadata, and byte-publication barrier; Unlocks RFC 1945 HTTP/1.0 parser and hardened profile. |
| `0.73.0` | RFC 1945 HTTP/1.0 parser and hardened profile | Requires Safe forwarding and explicit reframing plan; Unlocks HTTP/1.0 default-close lifecycle. |
| `0.74.0` | HTTP/1.0 default-close lifecycle | Requires RFC 1945 HTTP/1.0 parser and hardened profile; Unlocks Explicit HTTP/1.0 keep-alive extension profile. |
| `0.75.0` | Explicit HTTP/1.0 keep-alive extension profile | Requires HTTP/1.0 default-close lifecycle; Unlocks Separate vef-http09 package and exact grammar. |
| `0.76.0` | Separate vef-http09 package and exact grammar | Requires Explicit HTTP/1.0 keep-alive extension profile; Unlocks Explicit HTTP/0.9 client API. |
| `0.77.0` | Explicit HTTP/0.9 client API | Requires Separate vef-http09 package and exact grammar; Unlocks Explicit HTTP/0.9 server and dedicated-listener API. |
| `0.78.0` | Explicit HTTP/0.9 server and dedicated-listener API | Requires Explicit HTTP/0.9 client API; Unlocks HTTP/0.9 cross-protocol rejection corpus. |
| `0.79.0` | HTTP/0.9 cross-protocol rejection corpus | Requires Explicit HTTP/0.9 server and dedicated-listener API; Unlocks HTTP/1 smuggling and ambiguity corpus. |
| `0.80.0` | HTTP/1 smuggling and ambiguity corpus | Requires HTTP/0.9 cross-protocol rejection corpus; Unlocks HTTP/1 and HTTP/0.9 conformance audit and pentest. |
| `0.81.0` | HTTP/1 and HTTP/0.9 conformance audit and pentest | Requires HTTP/1 smuggling and ambiguity corpus; Unlocks HPACK prefix-integer decoder. |

## Phase 3 — HPACK and HTTP/2 (`0.82.0`–`0.154.0`)

HPACK encoder/decoder state tracks committed wire bytes; HTTP/2 activates, validates, publishes, mutates settings/state, cancels, and shuts down only through ordered bounded lifecycles.

| Version | Primary outcome | Sequence context |
| --- | --- | --- |
| `0.82.0` | HPACK prefix-integer decoder | Requires HTTP/1 and HTTP/0.9 conformance audit and pentest; Unlocks HPACK prefix-integer encoder. |
| `0.83.0` | HPACK prefix-integer encoder | Requires HPACK prefix-integer decoder; Unlocks HPACK integer overflow and canonical encoder proofs. |
| `0.84.0` | HPACK integer overflow and canonical encoder proofs | Requires HPACK prefix-integer encoder; Unlocks HPACK string representation codec. |
| `0.85.0` | HPACK string representation codec | Requires HPACK integer overflow and canonical encoder proofs; Unlocks HPACK Huffman tables. |
| `0.86.0` | HPACK Huffman tables | Requires HPACK string representation codec; Unlocks HPACK Huffman decoder. |
| `0.87.0` | HPACK Huffman decoder | Requires HPACK Huffman tables; Unlocks HPACK Huffman encoder. |
| `0.88.0` | HPACK Huffman encoder | Requires HPACK Huffman decoder; Unlocks HPACK static table. |
| `0.89.0` | HPACK static table | Requires HPACK Huffman encoder; Unlocks HPACK dynamic table storage. |
| `0.90.0` | HPACK dynamic table storage | Requires HPACK static table; Unlocks HPACK eviction and oversize-entry behavior. |
| `0.91.0` | HPACK eviction and oversize-entry behavior | Requires HPACK dynamic table storage; Unlocks HPACK table-size update and SETTINGS coupling. |
| `0.92.0` | HPACK table-size update and SETTINGS coupling | Requires HPACK eviction and oversize-entry behavior; Unlocks HPACK caller-owned ring lookup. |
| `0.93.0` | HPACK caller-owned ring lookup | Requires HPACK table-size update and SETTINGS coupling; Unlocks HPACK indexed representation. |
| `0.94.0` | HPACK indexed representation | Requires HPACK caller-owned ring lookup; Unlocks HPACK incremental-indexing literal. |
| `0.95.0` | HPACK incremental-indexing literal | Requires HPACK indexed representation; Unlocks HPACK non-indexing and never-indexed literal. |
| `0.96.0` | HPACK non-indexing and never-indexed literal | Requires HPACK incremental-indexing literal; Unlocks Sensitive-field indexing policy. |
| `0.97.0` | Sensitive-field indexing policy | Requires HPACK non-indexing and never-indexed literal; Unlocks HPACK encoder output commit and indexing policy. |
| `0.98.0` | HPACK encoder output commit and indexing policy | Requires Sensitive-field indexing policy; Unlocks Independent HPACK decode limits. |
| `0.99.0` | Independent HPACK decode limits | Requires HPACK encoder output commit and indexing policy; Unlocks HPACK synchronization, publication barrier, and error scope. |
| `0.100.0` | HPACK synchronization, publication barrier, and error scope | Requires Independent HPACK decode limits; Unlocks HPACK conformance audit and pentest. |
| `0.101.0` | HPACK conformance audit and pentest | Requires HPACK synchronization, publication barrier, and error scope; Unlocks HTTP/2 client and server prefaces. |
| `0.102.0` | HTTP/2 client and server prefaces | Requires HPACK conformance audit and pentest; Unlocks HTTP/2 frame-header codec. |
| `0.103.0` | HTTP/2 frame-header codec | Requires HTTP/2 client and server prefaces; Unlocks DATA frame codec. |
| `0.104.0` | DATA frame codec | Requires HTTP/2 frame-header codec; Unlocks HEADERS frame codec. |
| `0.105.0` | HEADERS frame codec | Requires DATA frame codec; Unlocks CONTINUATION frame codec. |
| `0.106.0` | CONTINUATION frame codec | Requires HEADERS frame codec; Unlocks SETTINGS frame codec. |
| `0.107.0` | SETTINGS frame codec | Requires CONTINUATION frame codec; Unlocks SETTINGS syntax, role, directional values, and ACK rules. |
| `0.108.0` | SETTINGS syntax, role, directional values, and ACK rules | Requires SETTINGS frame codec; Unlocks PING frame codec. |
| `0.109.0` | PING frame codec | Requires SETTINGS syntax, role, directional values, and ACK rules; Unlocks GOAWAY frame codec. |
| `0.110.0` | GOAWAY frame codec | Requires PING frame codec; Unlocks RST_STREAM frame codec. |
| `0.111.0` | RST_STREAM frame codec | Requires GOAWAY frame codec; Unlocks WINDOW_UPDATE codec and checked windows. |
| `0.112.0` | WINDOW_UPDATE codec and checked windows | Requires RST_STREAM frame codec; Unlocks Legacy PRIORITY frame handling. |
| `0.113.0` | Legacy PRIORITY frame handling | Requires WINDOW_UPDATE codec and checked windows; Unlocks PUSH_PROMISE frame handling. |
| `0.114.0` | PUSH_PROMISE frame handling | Requires Legacy PRIORITY frame handling; Unlocks Unknown-frame extension policy. |
| `0.115.0` | Unknown-frame extension policy | Requires PUSH_PROMISE frame handling; Unlocks HTTP/2 stream-identifier rules. |
| `0.116.0` | HTTP/2 stream-identifier rules | Requires Unknown-frame extension policy; Unlocks Generation-checked stream table and tombstones. |
| `0.117.0` | Generation-checked stream table and tombstones | Requires HTTP/2 stream-identifier rules; guarantees in-place/preflighted tombstone conversion or tracked bounded shutdown so accepted IDs never become idle; Unlocks Exhaustive stream-state graph. |
| `0.118.0` | Exhaustive stream-state graph | Requires Generation-checked stream table and tombstones; Unlocks HTTP/2 activation preface, first-SETTINGS, and deadline sequencing. |
| `0.119.0` | HTTP/2 activation preface, first-SETTINGS, and deadline sequencing | Requires Exhaustive stream-state graph; Unlocks HTTP/2 frame legality and fragmented-header-block sequencing. |
| `0.120.0` | HTTP/2 frame legality and fragmented-header-block sequencing | Requires HTTP/2 activation preface, first-SETTINGS, and deadline sequencing; Unlocks HTTP/2 error scope, typed deltas, and isolated stream mutation. |
| `0.121.0` | HTTP/2 error scope, typed deltas, and isolated stream mutation | Requires HTTP/2 frame legality and fragmented-header-block sequencing; Unlocks HTTP/2 graceful GOAWAY and bounded shutdown sequencing. |
| `0.122.0` | HTTP/2 graceful GOAWAY and bounded shutdown sequencing | Requires HTTP/2 error scope, typed deltas, and isolated stream mutation; Unlocks Atomic HPACK header-block integration. |
| `0.123.0` | Atomic HPACK header-block integration | Requires HTTP/2 graceful GOAWAY and bounded shutdown sequencing; Unlocks SETTINGS header-table encoder and header-list policy coupling. |
| `0.124.0` | SETTINGS header-table encoder and header-list policy coupling | Requires Atomic HPACK header-block integration; Unlocks Pseudo-field ordering and uniqueness. |
| `0.125.0` | Pseudo-field ordering and uniqueness | Requires SETTINGS header-table encoder and header-list policy coupling; Unlocks Connection-specific field and TE validation. |
| `0.126.0` | Connection-specific field and TE validation | Requires Pseudo-field ordering and uniqueness; Unlocks HTTP/2 malformed initial-field-block publication barrier. |
| `0.127.0` | HTTP/2 malformed initial-field-block publication barrier | Requires Connection-specific field and TE validation; Unlocks HTTP/2 request mapping. |
| `0.128.0` | HTTP/2 request mapping | Requires HTTP/2 malformed initial-field-block publication barrier; Unlocks HTTP/2 response mapping. |
| `0.129.0` | HTTP/2 response mapping | Requires HTTP/2 request mapping; Unlocks HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation. |
| `0.130.0` | HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation | Requires HTTP/2 response mapping; Unlocks Informational responses and trailers. |
| `0.131.0` | Informational responses and trailers | Requires HTTP/2 content-length, DATA, trailers, and END_STREAM reconciliation; Unlocks Cookie field combination and Set-Cookie preservation. |
| `0.132.0` | Cookie field combination and Set-Cookie preservation | Requires Informational responses and trailers; Unlocks Stream flow control. |
| `0.133.0` | Stream flow control | Requires Cookie field combination and Set-Cookie preservation; Unlocks Connection flow control. |
| `0.134.0` | Connection flow control | Requires Stream flow control; Unlocks SETTINGS initial-window active-stream integration and atomic rollback. |
| `0.135.0` | SETTINGS initial-window active-stream integration and atomic rollback | Requires Connection flow control; Unlocks HTTP/2 inbound DATA ownership, acknowledgement, and credit release. |
| `0.136.0` | HTTP/2 inbound DATA ownership, acknowledgement, and credit release | Requires SETTINGS initial-window active-stream integration and atomic rollback; Unlocks HTTP/2 outbound per-stream message command lifecycle. |
| `0.137.0` | HTTP/2 outbound per-stream message command lifecycle | Requires HTTP/2 inbound DATA ownership, acknowledgement, and credit release; Unlocks HTTP/2 body cancellation, reset, and flow-credit lifecycle. |
| `0.138.0` | HTTP/2 body cancellation, reset, and flow-credit lifecycle | Requires HTTP/2 outbound per-stream message command lifecycle; Unlocks SETTINGS outstanding-ACK accounting. |
| `0.139.0` | SETTINGS outstanding-ACK accounting | Requires HTTP/2 body cancellation, reset, and flow-credit lifecycle; Unlocks Bounded stream admission. |
| `0.140.0` | Bounded stream admission | Requires SETTINGS outstanding-ACK accounting; Unlocks SETTINGS max-concurrent-streams admission integration. |
| `0.141.0` | SETTINGS max-concurrent-streams admission integration | Requires Bounded stream admission; Unlocks Bounded outbound scheduling. |
| `0.142.0` | Bounded outbound scheduling | Requires SETTINGS max-concurrent-streams admission integration; Unlocks SETTINGS max-frame-size outbound integration. |
| `0.143.0` | SETTINGS max-frame-size outbound integration | Requires Bounded outbound scheduling; Unlocks GOAWAY cutoff and retry classification. |
| `0.144.0` | GOAWAY cutoff and retry classification | Requires SETTINGS max-frame-size outbound integration; Unlocks Server-push lifecycle. |
| `0.145.0` | Server-push lifecycle | Requires GOAWAY cutoff and retry classification plus v0.117.0 tombstones; creates rollback-capable, continuously tracked promised-request admission for the later v0.181.0 handle/provenance gate; Unlocks ALPN and cleartext prior-knowledge selection. |
| `0.146.0` | ALPN and cleartext prior-knowledge selection | Requires Server-push lifecycle; Unlocks Independent HTTP/2 rate and work budgets. |
| `0.147.0` | Independent HTTP/2 rate and work budgets | Requires ALPN and cleartext prior-knowledge selection; Unlocks Rapid-reset defenses. |
| `0.148.0` | Rapid-reset defenses | Requires Independent HTTP/2 rate and work budgets; Unlocks SETTINGS amplification defenses. |
| `0.149.0` | SETTINGS amplification defenses | Requires Rapid-reset defenses; Unlocks PING flood defenses. |
| `0.150.0` | PING flood defenses | Requires SETTINGS amplification defenses; Unlocks CONTINUATION bomb defenses. |
| `0.151.0` | CONTINUATION bomb defenses | Requires PING flood defenses; Unlocks WINDOW_UPDATE churn defenses. |
| `0.152.0` | WINDOW_UPDATE churn defenses | Requires CONTINUATION bomb defenses; Unlocks Reserved control-output queues. |
| `0.153.0` | Reserved control-output queues | Requires WINDOW_UPDATE churn defenses; Unlocks HTTP/2 conformance audit and pentest. |
| `0.154.0` | HTTP/2 conformance audit and pentest | Requires Reserved control-output queues; Unlocks Protocol-neutral HTTP translation representation. |

## Phase 4 — Proxy, client, server, and public APIs (`0.155.0`–`0.199.0`)

Role APIs expose validated authorized messages; translation emits nothing before the complete destination head/framing decision passes; retry and transition ownership are explicit.

| Version | Primary outcome | Sequence context |
| --- | --- | --- |
| `0.155.0` | Protocol-neutral HTTP translation representation | Requires HTTP/2 conformance audit and pentest; Unlocks Effective URI and authority consistency. |
| `0.156.0` | Effective URI and authority consistency | Requires Protocol-neutral HTTP translation representation; Unlocks Connection-field stripping and cache-metadata preservation. |
| `0.157.0` | Connection-field stripping and cache-metadata preservation | Requires Effective URI and authority consistency; Unlocks Via grammar, append, privacy, and loop policy. |
| `0.157.1` | Via grammar, append, privacy, and loop policy | Requires Connection-field stripping and cache-metadata preservation; Unlocks Dependency-free generic authentication grammar and sensitive storage. |
| `0.157.2` | Dependency-free generic authentication grammar and sensitive storage | Requires Via grammar, append, privacy, and loop policy; Unlocks Proxy-authentication hop ownership and 407 lifecycle. |
| `0.157.3` | Proxy-authentication hop ownership and 407 lifecycle | Requires Dependency-free generic authentication grammar and sensitive storage; Unlocks Injected civil time and HTTP-date policy. |
| `0.157.4` | Injected civil time and HTTP-date policy | Requires Proxy-authentication hop ownership and 407 lifecycle; Unlocks Dependency-free media-type grammar. |
| `0.157.5` | Dependency-free media-type grammar | Requires Injected civil time and HTTP-date policy; Unlocks Max-Forwards TRACE and OPTIONS intermediary semantics. |
| `0.158.0` | Max-Forwards TRACE and OPTIONS intermediary semantics | Requires Dependency-free media-type grammar; Unlocks HTTP/1 TE request-field and trailers forwarding semantics. |
| `0.159.0` | HTTP/1 TE request-field and trailers forwarding semantics | Requires Max-Forwards TRACE and OPTIONS intermediary semantics; Unlocks Normative HTTP/1 and HTTP/2 translation matrix. |
| `0.160.0` | Normative HTTP/1 and HTTP/2 translation matrix | Requires HTTP/1 TE request-field and trailers forwarding semantics; Unlocks CONNECT translation across HTTP versions. |
| `0.161.0` | CONNECT translation across HTTP versions | Requires Normative HTTP/1 and HTTP/2 translation matrix; Unlocks RFC 8441 extended CONNECT. |
| `0.162.0` | RFC 8441 extended CONNECT | Requires CONNECT translation across HTTP versions; Unlocks Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge. |
| `0.163.0` | Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge | Requires RFC 8441 extended CONNECT; Unlocks vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton. |
| `0.164.0` | vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton | Requires Bidirectional WebSocket HTTP/1 and HTTP/2 handshake bridge; Unlocks Structured Fields integer and decimal ranges. |
| `0.165.0` | Structured Fields integer and decimal ranges | Requires vef-structured-fields crate, lexical cursor, and bare-item dispatch skeleton; Unlocks Structured Fields strings, tokens, bytes, booleans, dates, and display strings. |
| `0.166.0` | Structured Fields strings, tokens, bytes, booleans, dates, and display strings | Requires Structured Fields integer and decimal ranges; Unlocks Structured Fields complete bare-item dispatcher. |
| `0.167.0` | Structured Fields complete bare-item dispatcher | Requires Structured Fields strings, tokens, bytes, booleans, dates, and display strings; Unlocks Structured Fields parameters. |
| `0.168.0` | Structured Fields parameters | Requires Structured Fields complete bare-item dispatcher; Unlocks Structured Fields inner lists and lists. |
| `0.169.0` | Structured Fields inner lists and lists | Requires Structured Fields parameters; Unlocks Structured Fields dictionaries. |
| `0.170.0` | Structured Fields dictionaries | Requires Structured Fields inner lists and lists; Unlocks Structured Fields canonical serialization. |
| `0.171.0` | Structured Fields canonical serialization | Requires Structured Fields dictionaries; Unlocks Structured Fields incremental parsing and caller-owned storage. |
| `0.172.0` | Structured Fields incremental parsing and caller-owned storage | Requires Structured Fields canonical serialization; Unlocks Structured Fields malformed-input and complexity limits. |
| `0.173.0` | Structured Fields malformed-input and complexity limits | Requires Structured Fields incremental parsing and caller-owned storage; Unlocks Priority field semantics. |
| `0.174.0` | Priority field semantics | Requires Structured Fields malformed-input and complexity limits; Unlocks SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration. |
| `0.175.0` | SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration | Requires Priority field semantics; Unlocks Priority scheduling hints and fairness. |
| `0.176.0` | Priority scheduling hints and fairness | Requires SETTINGS_NO_RFC7540_PRIORITIES priority-mode integration; Unlocks Priority intermediary behavior. |
| `0.177.0` | Priority intermediary behavior | Requires Priority scheduling hints and fairness; Unlocks PRIORITY_UPDATE frame support. |
| `0.178.0` | PRIORITY_UPDATE frame support | Requires Priority intermediary behavior; Unlocks Priority update flood budgeting. |
| `0.179.0` | Priority update flood budgeting | Requires PRIORITY_UPDATE frame support; Unlocks Client request builder and target forms. |
| `0.180.0` | Client request builder and target forms | Requires Priority update flood budgeting; Unlocks Dependency-free conditional semantics crate and validators. |
| `0.180.1` | Dependency-free conditional semantics crate and validators | Requires Client request builder and target forms; Unlocks Conditional request fields and ordered precondition evaluation. |
| `0.180.2` | Conditional request fields and ordered precondition evaluation | Requires Dependency-free conditional semantics crate and validators; Unlocks Bounded byte ranges and single-range response planning. |
| `0.180.3` | Bounded byte ranges and single-range response planning | Requires Conditional request fields and ordered precondition evaluation; Unlocks Outbound conditional and range request validation. |
| `0.180.4` | Outbound conditional and range request validation | Requires Bounded byte ranges and single-range response planning; Unlocks Partial-response media-type classification integration. |
| `0.180.5` | Partial-response media-type classification integration | Requires Outbound conditional and range request validation plus Dependency-free media-type grammar; Unlocks Client correlation, cancellation, and retry tokens. |
| `0.181.0` | Client correlation, cancellation, and retry tokens | Requires Partial-response media-type classification plus v0.145.0 push admission; atomically preflights pushed slot, handle, independent provenance, and rejection tracking, with in-place rejection or tracked shutdown on capacity; Unlocks Streaming partial-response and retained-prefix validation. |
| `0.181.1` | Streaming partial-response and retained-prefix validation | Requires the exact ordinary or promised correlation and held handle/provenance; pushed 206 cannot retain/assemble without all evidence, and pushed/ordinary 200 enters identical keyed/unkeyed evidence; Unlocks Cross-request partial assembly and header synthesis. |
| `0.181.2` | Cross-request partial assembly and header synthesis | Requires Streaming partial-response and retained-prefix validation; consumes immutable pushed provenance after associated-stream teardown/reuse with namespace-bounded invalidation and borrow-aware reclamation; Unlocks Retry safety, idempotency, and body-replayability contract. |
| `0.182.0` | Retry safety, idempotency, and body-replayability contract | Requires Cross-request partial assembly and header synthesis; Unlocks Role-aware outbound response semantic validator. |
| `0.182.1` | Role-aware outbound response semantic validator | Requires Retry safety, idempotency, and body-replayability contract; Unlocks Origin-server role API. |
| `0.183.0` | Origin-server role API | Requires Role-aware outbound response semantic validator; Unlocks Forward-proxy role API. |
| `0.184.0` | Forward-proxy role API | Requires Origin-server role API; Unlocks Reverse-proxy and gateway role API. |
| `0.185.0` | Reverse-proxy and gateway role API | Requires Forward-proxy role API; Unlocks Tunnel lifecycle and half-close semantics. |
| `0.186.0` | Tunnel lifecycle and half-close semantics | Requires Reverse-proxy and gateway role API; Unlocks Upgrade transformation boundary. |
| `0.187.0` | Upgrade transformation boundary | Requires Tunnel lifecycle and half-close semantics; Unlocks Exact CONNECT, Upgrade, and tunnel byte-handoff ownership. |
| `0.188.0` | Exact CONNECT, Upgrade, and tunnel byte-handoff ownership | Requires Upgrade transformation boundary; Unlocks GOAWAY, 421, and retry coordination. |
| `0.189.0` | GOAWAY, 421, and retry coordination | Requires Exact CONNECT, Upgrade, and tunnel byte-handoff ownership; Unlocks Authenticated origin authorization and HTTP/2 coalescing metadata. |
| `0.190.0` | Authenticated origin authorization and HTTP/2 coalescing metadata | Requires GOAWAY, 421, and retry coordination; Unlocks Fixed-capacity caller-storage public API. |
| `0.191.0` | Fixed-capacity caller-storage public API | Requires Authenticated origin authorization and HTTP/2 coalescing metadata; Unlocks Optional alloc-backed convenience API. |
| `0.192.0` | Optional alloc-backed convenience API | Requires Fixed-capacity caller-storage public API; Unlocks Stable diagnostics and security events. |
| `0.193.0` | Stable diagnostics and security events | Requires Optional alloc-backed convenience API; Unlocks Feature and dependency-policy surface. |
| `0.194.0` | Feature and dependency-policy surface | Requires Stable diagnostics and security events; Unlocks Multi-implementation interoperability. |
| `0.195.0` | Multi-implementation interoperability | Requires Feature and dependency-policy surface; Unlocks Adversarial and stateful fuzz campaign. |
| `0.196.0` | Adversarial and stateful fuzz campaign | Requires Multi-implementation interoperability; Unlocks Compile-fail state and lifetime tests. |
| `0.197.0` | Compile-fail state and lifetime tests | Requires Adversarial and stateful fuzz campaign; Unlocks Long-running soak and exhaustion campaign. |
| `0.198.0` | Long-running soak and exhaustion campaign | Requires Compile-fail state and lifetime tests; Unlocks Role and API conformance audit and pentest. |
| `0.199.0` | Role and API conformance audit and pentest | Requires Long-running soak and exhaustion campaign; Unlocks Standard blocking-stream adapter. |

## Phase 5 — OS, Aesynx readiness, and 1.0 evidence (`0.200.0`–`0.225.0`)

Adapters cannot alter protocol validity; TLS admission, EOF/alerts, deterministic resource ceilings, readiness, deadlines, storage, and release evidence remain explicit across targets.

| Version | Primary outcome | Sequence context |
| --- | --- | --- |
| `0.200.0` | Standard blocking-stream adapter | Requires Role and API conformance audit and pentest; Unlocks Standard nonblocking-stream adapter. |
| `0.201.0` | Standard nonblocking-stream adapter | Requires Standard blocking-stream adapter; Unlocks Brynja TLS provider contract and admission review. |
| `0.202.0` | Brynja TLS provider contract and admission review | Requires Standard nonblocking-stream adapter; Unlocks Separate vef-brynja adapter crate. |
| `0.203.0` | Separate vef-brynja adapter crate | Requires Brynja TLS provider contract and admission review; Unlocks HTTP/2 TLS admission prerequisites and authenticated metadata. |
| `0.204.0` | HTTP/2 TLS admission prerequisites and authenticated metadata | Requires Separate vef-brynja adapter crate; Unlocks TLS transport termination, resumption, alert, and EOF mapping. |
| `0.205.0` | TLS transport termination, resumption, alert, and EOF mapping | Requires HTTP/2 TLS admission prerequisites and authenticated metadata; Unlocks TLS 1.3 early-data prohibition and close semantics. |
| `0.206.0` | TLS 1.3 early-data prohibition and close semantics | Requires TLS transport termination, resumption, alert, and EOF mapping; Unlocks Aesynx fixed-memory capability profile. |
| `0.207.0` | Aesynx fixed-memory capability profile | Requires TLS 1.3 early-data prohibition and close semantics; Unlocks Aesynx transport and readiness adapter. |
| `0.208.0` | Aesynx transport and readiness adapter | Requires Aesynx fixed-memory capability profile; Unlocks Aesynx timer and deadline adapter. |
| `0.209.0` | Aesynx timer and deadline adapter | Requires Aesynx transport and readiness adapter; Unlocks Aesynx kernel integration tests. |
| `0.210.0` | Aesynx kernel integration tests | Requires Aesynx timer and deadline adapter; Unlocks Deterministic CPU, stack, code-size, and amplification budgets. |
| `0.211.0` | Deterministic CPU, stack, code-size, and amplification budgets | Requires Aesynx kernel integration tests; Unlocks 32-bit target campaign. |
| `0.212.0` | 32-bit target campaign | Requires Deterministic CPU, stack, code-size, and amplification budgets; Unlocks Big-endian target campaign. |
| `0.213.0` | Big-endian target campaign | Requires 32-bit target campaign; Unlocks Cross-architecture campaign. |
| `0.214.0` | Cross-architecture campaign | Requires Big-endian target campaign; Unlocks Linux, Windows, BSD, macOS, Android, and iOS matrix. |
| `0.215.0` | Linux, Windows, BSD, macOS, Android, and iOS matrix | Requires Cross-architecture campaign; Unlocks Kani shared-core proof replay and expansion. |
| `0.216.0` | Kani shared-core proof replay and expansion | Requires Linux, Windows, BSD, macOS, Android, and iOS matrix; Unlocks Kani HTTP/1 proof replay and expansion. |
| `0.217.0` | Kani HTTP/1 proof replay and expansion | Requires Kani shared-core proof replay and expansion; Unlocks Kani HPACK proof replay and expansion. |
| `0.218.0` | Kani HPACK proof replay and expansion | Requires Kani HTTP/1 proof replay and expansion; Unlocks Kani HTTP/2 proof replay and expansion. |
| `0.219.0` | Kani HTTP/2 proof replay and expansion | Requires Kani HPACK proof replay and expansion; Unlocks Stateful cargo-fuzz replay and expansion. |
| `0.220.0` | Stateful cargo-fuzz replay and expansion | Requires Kani HTTP/2 proof replay and expansion; Unlocks Differential and interoperability campaign. |
| `0.221.0` | Differential and interoperability campaign | Requires Stateful cargo-fuzz replay and expansion; Unlocks Whole-project conformance audit and pentest. |
| `0.222.0` | Whole-project conformance audit and pentest | Requires Differential and interoperability campaign; Unlocks Independent security audit. |
| `0.223.0` | Independent security audit | Requires Whole-project conformance audit and pentest; Unlocks Audit remediation and API freeze. |
| `0.224.0` | Audit remediation and API freeze | Requires Independent security audit; Unlocks Documentation, packaging, SBOM, provenance, and RC readiness. |
| `0.225.0` | Documentation, packaging, SBOM, provenance, and RC readiness | Requires Audit remediation and API freeze; Unlocks 1.0.0-rc.1. |

## Release candidates and 1.0

| Version | Primary outcome | Exit context |
| --- | --- | --- |
| `1.0.0-rc.1` | Public API freeze, interoperability, documentation, and package review | No features after the freeze; repeat the full gate and exact-commit pentest. |
| `1.0.0-rc.2` | RC1 remediation and complete evidence replay | No unreviewed behavior change or unresolved critical/high finding. |
| `1.0.0` | First serious production-ready VEF HTTP release | All applicable requirements, resource/platform claims, audit remediation, and release evidence are verified. |
