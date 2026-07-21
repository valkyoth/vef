# VEF Platform Support

Status: foundation policy

Platform support is an evidence claim. Protocol validity cannot depend on an
OS, pointer width, endianness, allocator, socket API, executor, or wall clock.

| Platform | Day-one evidence | Production evidence required by 1.0 |
| --- | --- | --- |
| Linux | Host tests and portable core checks | x86-64, AArch64, x86, Armv7, musl, soak and interop |
| Windows | Native CI host tests | x86-64 I/O lifecycle and interoperability |
| BSD | FreeBSD cross-check | FreeBSD native CI/test-host evidence; scheduled OpenBSD/NetBSD checks |
| macOS | Native CI host tests | x86-64 and Apple Silicon lifecycle/interoperability |
| Android | AArch64 cross-check | NDK embedding, lifecycle, network-change tests |
| iOS | AArch64 cross-check | Apple embedding, lifecycle, background constraints |
| Aesynx | No OS types in core APIs | Future native I/O/time adapter and fixed-storage tests |

Additional release matrices cover 32-bit arithmetic, RISC-V, PowerPC, at least
one big-endian target, bare-metal/embedded, and WebAssembly codec-only use.

No `cfg` branch may change framing or semantic validity. A backend may report
an unsupported capability; it may not silently approximate a security rule.
