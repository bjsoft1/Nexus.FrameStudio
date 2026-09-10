# Scope, risks and remaining work

## Current delivery status

The approved prototype and the five-phase plan exist. The new native solution, recorder/editor implementation, native automated test bodies, generated real-media fixtures, MP4 encoding verification and installer have **not been produced or executed by this planning delivery**. All native tasks/tests start NOT_STARTED/NOT_RUN. Package checks in `PACKAGE_VALIDATION.md` validate documents/data/navigation only.

## Scope retained from the approved screens

The 20 editor and 20 recorder requirements are mandatory within these five phases. Speed (44), color (45), canvas (21/46), save/recovery (47/51), themes (52), inspector (50) and review screens (53/54) are explicitly included even when they are not separate items in the original 20+20 summary. Pages 53/54 can be a QA/review surface; do not turn the everyday navigation into a wall of 54 buttons.

| Risk | Design/test response | Phase owner |
|---|---|---|
| Missing audio or keyboard history falsely recoverable | Separate capture availability from presentation mute/hide; test off/suppressed/redacted intervals. | P1/P2/P4/P5 |
| Effects permanently burned into source | Clean pixel path; independent webcam/audio; source-hash and independent playback checks. | P2/P4 |
| Legacy single-recording clip semantics break joined edits | New clip-instance model; explicit ordering and empty timeline; A-B-A regression. | P1/P3 |
| Timestamp drift and off-by-one frame/sample mapping | Preserve rational PTS and clock anchors; per-finalized-frame index; sixty-minute sync markers. | P2/P3/P5 |
| Multi-monitor DPI/crop misalignment | Physical-pixel transforms, negative-origin/mixed-DPI fixtures and shared transform evaluator. | P2/P3/P4 |
| Rich preview looks different from export | One authoritative scene/audio evaluator; actual rendered parity samples. | P1/P3/P4 |
| Partial MP4 cannot finalize after a crash | Bounded recording parts, commit journal, explicit partial state and measured missing-tail reporting. | P2/P5 |
| Full raw export leaks hidden/muted originals | Explicit full-package warning plus a separate sanitized-copy path and reference cleanup tests. | P5 |
| Unsafe imports/archives overwrite user data | Containment, staging, limits, hashes, decoder probes, locking and fault injection. | P1/P3/P5 |
| Dependency/codec or device unavailable | Runtime capability probing, truthful support matrix and typed error/disabled state. | P1/P2/P5 |
| UI complexity grows with features | Reuse approved panels, compact controls, contextual property groups and keyboard navigation. | All |
| “Tests passed” is based on simulations | Separate UI/fake/model checks from actual hardware/media/installer evidence; no inherited prototype passes. | All |

## Baseline exclusions

No wellness/reminder/screenshot/image-editor/3D/account modules. No cloud backend, collaborative editing, AI transcription/generative features, advanced grading, arbitrary-code plugin system or universal codec guarantee. No automatic conversion of prototype/legacy projects without a separately approved/tested migration. No recovery of uncaptured data or guaranteed removal of effects baked by another app. No hidden capture or bypass of protected OS/device restrictions.

Basic noise-gate/gain controls need actual implementation and bypass tests; do not imply studio-grade AI noise removal. Playback speed must declare its audio/pitch behavior. More advanced pitch preservation, HDR, ARM64 and higher frame-rate support need explicit evidence/scope approval, not fake enabled toggles.

Release packaging is a Windows x64 candidate with truthful signing status. Store submission, account credentials/certificates and reused Store identities are not authorized. Do not invent a signing certificate or overwrite another application's installer identity.

## Remaining after each phase

| After phase | Deliberately remaining |
|---|---|
| P1 | Real capture, media editing/playback, effects, output/raw packaging and native release validation. |
| P2 | Core edit operations/playback, composed effects/audio editing, sharing exports/raw portability and release hardening. |
| P3 | Rich overlays/animation/transitions/captions, detailed input effects/audio mixer, final queue/raw/release. |
| P4 | Production export queue/preset hardening, raw-package/privacy workflows, complete recovery, stress/install/final acceptance. |
| P5 | Only explicitly documented out-of-scope enhancements; any missing approved requirement is an unresolved release blocker. |

Each phase handoff must replace generic remaining items with exact unfinished task/case IDs, impact, reason, next action and owner. Do not write “nothing remaining” while a required test is NOT_RUN.
