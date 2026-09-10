# How to build, test and approve each phase

## What is executable in this ZIP?

The offline review page, original HTML prototype and `tools/validate_plan.py` can run now. Native solution/build scripts and test bodies must be created during development. **All 150 native test specifications are currently NOT_RUN.** A prototype browser pass is not a recorder, encoder, recovery or Windows installer pass.

## Environment and fixture setup

Use a supported Windows 11 x64 test machine for native capture/WPF tests. Record Windows build, CPU/GPU/driver, RAM, disk type/free space, display sizes/DPI, selected devices, codec availability, .NET SDK/runtime and app commit. A clean VM is suitable for many install/storage/UI tests, but unavailable physical devices are not simulated into a hardware PASS.

Phase 1 must implement `tools/New-TestFixtures.ps1` (or an equivalently documented deterministic generator) and include hashes plus an independent metadata oracle. Fixtures must contain synthetic or explicitly consented media, not private user recordings. Fixture generators and assertion oracles should not merely call the same production routine and compare it to itself.

| ID | Fixture / environment to create |
|---|---|
| F00 | Clean standalone profile, empty project and data-only valid/invalid theme files. |
| F01 | `A-10s-1080p30.mp4`: ten seconds, unique frame counter/grid/moving target and known beep timing; independently probed. |
| F02 | `B-6s-720p24.mp4`: six seconds with visibly different content/tone and known frame times. |
| F03 | Transparent PNG logo plus JPEG and independent PCM WAV tone assets. |
| F04 | Controlled thirty-second take: separate screen/camera/system/mic, mic capture off on `[10s,20s)`, a keyboard-off span, allowed keys and pointer events. It must include actual test media once P2 is implemented. |
| F05 | Variable-duration/duplicate-frame sources, negative-origin mixed-DPI geometry, multiple sub-frame events, audio offsets and drift anchors. |
| F06 | Invalid/oversized/future/wrong-kind projects; corrupt and unsupported media; read-only and disk-full failure fixtures. |
| F07 | Hostile raw-package variants: traversal, rooted/UNC/ADS paths, link entries, duplicate/case-colliding entries, oversized expansion, bad hashes and missing media. Use isolated staging only. |
| F08 | One-hour controlled source/project with sparse time markers and large but bounded track/cache workloads. |
| F09 | Complete composed project containing every overlay type, rich text, keyframes, transition, captions, pointer/key edits and independent audio settings. |
| H01 | Consented primary-display recording with a controlled test window, not the user's private desktop content. |
| H02 | Two displays of different resolutions/DPI with one negative desktop origin; record the actual arrangement. |
| H03 | Consented webcam/microphone/loopback devices and a controlled signal route. Use headphones to reduce unintended microphone capture of system sound. |

These fixture specifications do not mean media files are already included. The approved prototype's example JSON references illustrative/absent media and cannot substitute for F01–F09 native fixtures.

## Commands the developer must implement in P1

Run from the new native repository, not this planning folder:

```powershell
.\tools\Build.ps1 -Configuration Release
.\tools\New-TestFixtures.ps1
.\tools\Run.ps1
.\tools\Test-Phase.ps1 -Phase 1 -IncludePrevious -Mode NonHardware
```

`Build.ps1` must restore the pinned/locked dependency graph and cleanly build the whole solution. `Run.ps1` launches the real application. `Test-Phase.ps1` must validate expected case IDs, detect zero discovered/executed tests, create per-case outcomes, preserve nonzero exits and save logs/TRX. It must not treat skipped hardware tests as passes. Pin/document the chosen native test framework in P1; xUnit-style method names `P1_A01` through `P5_A15` are the default naming contract.

Each automated test specification includes a direct `dotnet test ... --filter FullyQualifiedName~P1_A01`-style command to run after the corresponding tests exist and the solution has been built. A plain `dotnet test` exit code is not sufficient evidence of case coverage; the wrapper must inspect results. P1-A01 (clean build) and P1-A15 (runner-integrity) should invoke an isolated child checkout/test harness rather than recursively rebuilding the test process that is currently running.

P5-A15 audits all other required evidence while its own case is in flight. After it completes, the external phase wrapper checks its result as well; the gate must not recursively require an in-flight test to have already passed.

`Mode UI` requires an interactive Windows desktop and uses explicit controlled adapters/fixtures where appropriate. `Mode Hardware` requires deliberate opt-in/device consent and real connected devices. `Mode All` must include required categories and mark absent ones BLOCKED/NOT_RUN. The phase gate requires the hardware categories that apply; a green NonHardware run alone does not satisfy a recorder release gate.

For later phases change `-Phase 1` to the current phase. `-IncludePrevious` runs required earlier regression cases. The wrapper must not create real output or start a recording merely because a unit test uses a fake clock.

## Manual testing from the UI

Build/run the phase, create or open the stated fixture, then follow that phase's `02_MANUAL_TESTS.md`. Each case gives prerequisites, numbered UI actions, expected outcome and an evidence folder. Screen numbers refer to the approved reference catalog and native equivalent, not a demand for fifty-four top-level windows. Capture screenshots when inspecting layout; retain actual produced media plus independent probe results when testing capture/export.

Write the **actual result**, not a copy of the expected result. Attach the commit/machine profile, screenshot/recording, relevant log and defect ID. Reset fixtures between destructive/failure tests. Never run archive/disk-full/crash fixtures on an irreplaceable project or production folder.

## Acceptance targets, not measured results

Agree and record benchmark hardware at the P1 gate. Changing a target later requires an owner-approved decision with impact; do not loosen it silently after a failure.

| Area | Initial acceptance target |
|---|---|
| Source geometry | Known-point mapping within one source/output pixel before compression. |
| Event timing | Correct source/clip interval; pointer/key/caption visual onset within one intended output frame. |
| Audio/video sync | Controlled visible/beep markers within 50 ms at beginning, middle and end of the sixty-minute baseline; report source latency separately. |
| Frame index | Exactly one resolvable index record for each finalized presented screen frame; truthful drops/duplicates/durations. |
| Render parity | Shared pre-encode scene equals the evaluated reference (allow documented GPU rounding up to 2/255 for 99.5% of pixels); high-quality controlled encoded-fixture SSIM target ≥0.98. Low-bitrate artistic outputs use their selected quality, not this fixture threshold. |
| Audio logic | Deterministic routing/gain/fade assertions on PCM and consistent sample-frame boundary rounding; no samples falsely marked captured. |
| Interaction | On agreed baseline hardware, input feedback target ≤200 ms and cached 1080p seek p95 ≤500 ms; record full distributions and exceptions. |
| Resource growth | Bounded queues/caches; no ongoing duration-proportional in-memory metadata accumulation. Measure peak memory/handles and return-to-baseline after disposal. |
| Source protection | Original source/event/manifest hashes unchanged by ordinary edit/export; old target unchanged after failed/canceled export. |
| Recovery | Prior-good save and all committed parts preserved in injected failures; report missing/unverified tail, never an unconditional zero-loss guarantee. |

## Result and evidence format

Use `templates/PHASE_RESULT.json` or the phase handoff. Allowed test statuses: NOT_RUN, PASS, FAIL, BLOCKED. Task statuses: NOT_STARTED, IN_PROGRESS, DONE, BLOCKED. Every PASS requires actual result, environment, commit, command/UI steps and at least one meaningful evidence path. A setup error is not a functional PASS. Report skipped/unavailable environments as BLOCKED or NOT_RUN with a reason.

Evidence convention: `artifacts/acceptance/Pn/Pn-Mxx/` for manual tests and `artifacts/tests/Pn-Axx/` for automation. Keep TRX, probe reports, frame comparisons, source-hash snapshots and redacted logs. Store large/sensitive captures securely outside Git; include hashes and approved access instructions in the report.

## Phase gate

A phase exits only with a clean build, all required current/earlier tests passed, an actual UI demonstration, no unresolved critical/high defects, an explicit remaining-work list, and owner/reviewer approval. A defect or not-run required case is not automatically waived. The owner may explicitly defer a non-required enhancement or change support scope; retain the decision and traceability. A required approved feature cannot silently move beyond Phase 5.

Use the reviewer page for draft notes only. Clicking a checkbox cannot approve a phase or prove native tests passed. The owner signs the handoff/approval record after reviewing evidence.
