# Phase 5 — Export, raw packages & release

**Status: NOT_STARTED. This is a development specification, not a completion report.**

## Deliverable

A tested desktop release candidate with real video export, portable editable sessions, recovery, documentation and install/uninstall validation.
## Prerequisite

Phase 4 must have a clean build, required regression evidence and explicit owner approval. Read its actual handoff before changing code.
## In scope

Finish export presets/queue, raw archive round trips, privacy-safe sharing, recovery, capability reporting, performance checks and Windows release packaging.
## Not in this phase

Store submission/signing without credentials, cloud services, macOS/Linux, ARM64 and unverified HDR/codec promises are not included. Any missed approved requirement remains a blocker, not an automatic deferral.
## Twenty implementation tasks

| ID | Task | Implementation | Done when |
|---|---|---|---|
| P5-T01 | Complete export configuration | Offer validated MP4 H.264/AAC baseline, resolution/FPS/bitrate presets and independent include switches. | Requested and actual formats are shown; unsupported combinations fail before overwriting output. |
| P5-T02 | Implement the render queue | Snapshot projects, queue/reorder jobs, report real progress and support cancellation/retry. | Later edits do not change a queued snapshot; canceled jobs never appear as completed. |
| P5-T03 | Harden encoder selection | Probe encoders, implement explicit software selection and one safe initialization fallback for Automatic. | Source, permission or disk errors never masquerade as hardware-fallback success. |
| P5-T04 | Verify and promote exports safely | Write a same-directory private partial; independently decode content and verify dimensions/duration/audio before promotion. | Existing target files and capture sources survive cancellation and every tested failure path. |
| P5-T05 | Implement portable raw export | Package manifest, project, referenced assets, clean media, metadata and hashes into .nfsraw. | The package opens elsewhere without any developer-machine or absolute media paths. |
| P5-T06 | Implement safe raw import | Validate kinds, versions, paths, collisions, limits, hashes and media in staging before registering a workspace. | Malicious or corrupt archives cannot write outside staging or replace another project. |
| P5-T07 | Implement editable-package privacy review | Warn that hidden/muted media remains in a full raw package; offer a new sanitized copy with chosen sources omitted. | Removed sources have redacted availability and broken references are eliminated; original workspace is unchanged. |
| P5-T08 | Implement save-as and file association | Duplicate an editable workspace safely and register .nfsproject/.nfsraw with this app without hijacking MP4 defaults. | Double-clicking a project opens the correct standalone app; Cancel creates no misleading copy. |
| P5-T09 | Complete autosave and crash recovery | Recover a validated snapshot and finalized capture parts into a new workspace, preserving original evidence. | Corrupt/partial files remain quarantined; recovery states exactly what could not be restored. |
| P5-T10 | Complete cleanup and storage controls | Show source/proxy/cache sizes; make deletion ownership-aware and confirmation-based. | Clearing caches cannot remove unique source files or media referenced by another project. |
| P5-T11 | Run end-to-end media acceptance | Capture, edit, compose, save, package, reopen and export a multi-track sample on a second machine. | Visual timing, audio separation and metadata survive the full round trip. |
| P5-T12 | Run performance and long-session tests | Benchmark the agreed 1080p baseline, two monitors and long sessions; record hardware, dropped frames and memory. | Supported presets have evidence; untested 4K/high-FPS modes are not advertised as validated. |
| P5-T13 | Run resilience and security testing | Inject disk-full, denied access, device loss, archive attacks, concurrent saves and interrupted operations. | Source-hash and prior-good-work checks pass; unresolved data-loss/privacy defects block release. |
| P5-T14 | Finalize support matrix and diagnostics | Publish measured codec/device/OS limits, privacy behavior and user-actionable troubleshooting. | The product tells the truth about unavailable capabilities and does not log sensitive captured content. |
| P5-T15 | Build a Windows release package | Produce a versioned self-contained x64 distribution and a documented per-user installer path. | Install, launch, upgrade and uninstall are tested in a clean Windows environment. |
| P5-T16 | Verify signing and distribution boundaries | Add signing hooks and notices without embedding secrets or reusing another app's Store identity. | Unsigned/test-signed status is explicit; missing credentials remain a release limitation, not fabricated success. |
| P5-T17 | Write the user and recovery guides | Document record/edit/export/raw workflows, audio capture versus mute, privacy, backup and restoration. | A new user can complete the main workflow from UI steps alone. |
| P5-T18 | Run the final UI regression | Check all approved screens in light/dark themes, small/fullscreen layouts and keyboard navigation. | No approved feature is lost during integration; review-only pages remain out of the everyday workflow. |
| P5-T19 | Resolve defects and assemble evidence | Run every required case, consolidate build/test logs and close blockers with retests. | No failed/not-run required case is counted as passed or silently removed from scope. |
| P5-T20 | Obtain final owner acceptance | Deliver source, runnable package, release notes, checksums, test evidence and explicit remaining work. | The owner approves release; future features remain separate from the completed five-phase scope. |

## Approved UI references

47 Save editable project, 48 Export video, 49 Export queue & result, 51 Recovery & history.
P1 owns visual coverage of every screen. The above list identifies primary functional completion; shared screens are progressively integrated. See the complete screen-phase map.

## Required evidence and gate

Pass all cumulative required tests, export and reopen on a second machine, verify interruption/recovery and source safety, and obtain explicit owner release approval.

Run the 15 manual cases and implement/run the 15 automated cases in this folder, plus previous required regressions. Save actual outputs and hashes for media/storage tests. All current required cases must be PASS with evidence; BLOCKED/NOT_RUN is not approval.

Complete `04_HANDOFF_AND_REMAINING.md`. Only the owner/reviewer may approve the next phase. See the common testing guide for exception and release rules.
