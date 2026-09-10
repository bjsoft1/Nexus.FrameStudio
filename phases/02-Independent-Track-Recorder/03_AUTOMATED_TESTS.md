# Phase 2 — Independent-track recorder — automated test specifications

**All cases: NOT_RUN. Test bodies and the native solution must be implemented; these are future execution commands.**

Run build/fixture setup first. Use the phase wrapper described in `../../docs/TESTING_GUIDE.md` to reject zero-test runs and track coverage. UI tests need an interactive Windows desktop; Hardware cases require opt-in and actual controlled devices.

## P2-A01 — Recording state machine

**Type:** Unit
**Arrange and execute:** Drive start/countdown/cancel/record/pause/resume/stop/failure with a deterministic clock and repeated commands.
**Assert:** Only valid transitions occur; duplicate starts and double finalization are blocked.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A01" --logger "trx;LogFileName=P2_A01.trx" --results-directory "artifacts/tests/P2-A01"
```

**Evidence:** `artifacts/tests/P2-A01/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A02 — Physical-pixel transform matrix

**Type:** Unit
**Arrange and execute:** Map points across negative origins, mixed DPI, fit/fill gaps, region crops and changed monitor layouts.
**Assert:** Round-trip coordinates meet one-pixel tolerance with explicit out-of-canvas results.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A02" --logger "trx;LogFileName=P2_A02.trx" --results-directory "artifacts/tests/P2-A02"
```

**Evidence:** `artifacts/tests/P2-A02/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A03 — Capture settings and capability validation

**Type:** Unit
**Arrange and execute:** Apply presets and unsupported width/FPS/codec combinations against a fake capability matrix.
**Assert:** Actual settings are explicit and invalid configurations cannot start.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A03" --logger "trx;LogFileName=P2_A03.trx" --results-directory "artifacts/tests/P2-A03"
```

**Evidence:** `artifacts/tests/P2-A03/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A04 — Clean video hardware capture

**Type:** Hardware
**Arrange and execute:** With consent, capture the controlled test window while cursor and effect previews are active.
**Assert:** Independent decode contains expected frames and no app-added cursor/key/webcam/border pixels; output is finalized.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A04" --logger "trx;LogFileName=P2_A04.trx" --results-directory "artifacts/tests/P2-A04"
```

**Evidence:** `artifacts/tests/P2-A04/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A05 — Independent audio source capture

**Type:** Hardware
**Arrange and execute:** Feed distinct known tones to controlled loopback and mic input routes; capture and decode each source.
**Assert:** Track identities, sample rates and expected signal content are independent; no mandatory mix-down occurs.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A05" --logger "trx;LogFileName=P2_A05.trx" --results-directory "artifacts/tests/P2-A05"
```

**Evidence:** `artifacts/tests/P2-A05/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A06 — Capture-off and restart intervals

**Type:** Integration
**Arrange and execute:** Drive mic/system/camera capture toggles and source restarts around known clock boundaries.
**Assert:** Off spans contain no retained captured samples; restart mappings and reasons are explicit.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A06" --logger "trx;LogFileName=P2_A06.trx" --results-directory "artifacts/tests/P2-A06"
```

**Evidence:** `artifacts/tests/P2-A06/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A07 — Per-frame index reconciliation

**Type:** Integration
**Arrange and execute:** Capture synthetic variable-duration/duplicated frames and finalize actual encoded output, including reordered packets.
**Assert:** Exactly one index record per presented decoded screen frame; PTS/durations and references agree with committed media.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A07" --logger "trx;LogFileName=P2_A07.trx" --results-directory "artifacts/tests/P2-A07"
```

**Evidence:** `artifacts/tests/P2-A07/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A08 — Pointer state and event completeness

**Type:** Unit
**Arrange and execute:** Replay stationary/moving cursor, changed shapes, multiple clicks, drag, scroll and off-canvas positions.
**Assert:** Every frame resolves current state and all event edges survive with stable IDs and correct frame intervals.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A08" --logger "trx;LogFileName=P2_A08.trx" --results-directory "artifacts/tests/P2-A08"
```

**Evidence:** `artifacts/tests/P2-A08/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A09 — Audio sample-frame mapping

**Type:** Unit
**Arrange and execute:** Map frame intervals to 44.1/48 kHz mono/stereo sources with offsets, resampling, drift and gaps.
**Assert:** Sample-frame boundaries do not multiply by channel count; gaps remain unavailable; cumulative rounding stays bounded.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A09" --logger "trx;LogFileName=P2_A09.trx" --results-directory "artifacts/tests/P2-A09"
```

**Evidence:** `artifacts/tests/P2-A09/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A10 — Keyboard privacy allowlist

**Type:** Unit
**Arrange and execute:** Feed normal typing, AltGr, allowed shortcuts, secure/unknown focus, repeats and emergency-stop boundaries.
**Assert:** Only explicitly permitted display events survive; no plaintext/clipboard data or post-stop events are serialized.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A10" --logger "trx;LogFileName=P2_A10.trx" --results-directory "artifacts/tests/P2-A10"
```

**Evidence:** `artifacts/tests/P2-A10/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A11 — Pause and source-layout changes

**Type:** Integration
**Arrange and execute:** Pause wall time and change layout/source dimensions before resuming a controlled take.
**Assert:** Session timing excludes pauses; new parts/transforms are recorded; old finalized parts remain immutable.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A11" --logger "trx;LogFileName=P2_A11.trx" --results-directory "artifacts/tests/P2-A11"
```

**Evidence:** `artifacts/tests/P2-A11/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A12 — Webcam hardware synchronization

**Type:** Hardware
**Arrange and execute:** Capture a controlled flash/beep or time marker with screen, webcam and independent audio.
**Assert:** Source offsets and availability are measured; drift meets the agreed budget or the test fails with evidence.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A12" --logger "trx;LogFileName=P2_A12.trx" --results-directory "artifacts/tests/P2-A12"
```

**Evidence:** `artifacts/tests/P2-A12/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A13 — Bounded pipeline and device-loss stress

**Type:** Integration
**Arrange and execute:** Overrun queues and inject window-close, encoder-stall and device-disconnect failures.
**Assert:** Queues are bounded; dropped samples are counted; handles close; surviving finalized streams are retained.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A13" --logger "trx;LogFileName=P2_A13.trx" --results-directory "artifacts/tests/P2-A13"
```

**Evidence:** `artifacts/tests/P2-A13/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A14 — Durable finalization fault matrix

**Type:** Integration
**Arrange and execute:** Inject failures during media write, metadata flush, index commit and manifest promotion.
**Assert:** Committed parts remain readable; uncommitted tails are marked partial and never reported complete.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A14" --logger "trx;LogFileName=P2_A14.trx" --results-directory "artifacts/tests/P2-A14"
```

**Evidence:** `artifacts/tests/P2-A14/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-A15 — Recorder UI controls and handoff

**Type:** UI
**Arrange and execute:** Use explicit deterministic test adapters to configure source/presets, cancel countdown, toggle capture and open the resulting controlled session.
**Assert:** UI state matches real coordinator states; track availability and inspector data persist; no production simulation path is used.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P2_A15" --logger "trx;LogFileName=P2_A15.trx" --results-directory "artifacts/tests/P2-A15"
```

**Evidence:** `artifacts/tests/P2-A15/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.
