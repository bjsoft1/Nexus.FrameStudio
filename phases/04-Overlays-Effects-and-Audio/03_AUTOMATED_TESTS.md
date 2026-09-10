# Phase 4 — Overlays, effects & audio — automated test specifications

**All cases: NOT_RUN. Test bodies and the native solution must be implemented; these are future execution commands.**

Run build/fixture setup first. Use the phase wrapper described in `../../docs/TESTING_GUIDE.md` to reject zero-test runs and track coverage. UI tests need an interactive Windows desktop; Hardware cases require opt-in and actual controlled devices.

## P4-A01 — Overlay state and command history

**Type:** Unit
**Arrange and execute:** Add, move, lock, duplicate, reorder and delete all supported overlay types with undo/redo.
**Assert:** Stable IDs, time anchors, z-order and properties serialize and invert consistently.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A01" --logger "trx;LogFileName=P4_A01.trx" --results-directory "artifacts/tests/P4-A01"
```

**Evidence:** `artifacts/tests/P4-A01/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A02 — Styled text shaping and safety

**Type:** Integration
**Arrange and execute:** Render mixed-run English/Nepali text, long wrapping and absent-font cases; submit unexpected markup.
**Assert:** Required glyph/runs persist; fallback is reported; markup cannot execute; layout matches preview within tolerance.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A02" --logger "trx;LogFileName=P4_A02.trx" --results-directory "artifacts/tests/P4-A02"
```

**Evidence:** `artifacts/tests/P4-A02/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A03 — Shape geometry and hit testing

**Type:** Unit
**Arrange and execute:** Evaluate rectangles/ellipses/arrows/lines/highlights through rotation, resize and different preview scales.
**Assert:** Handles/hit tests and rendered geometry agree; stroke/fill/alpha are deterministic.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A03" --logger "trx;LogFileName=P4_A03.trx" --results-directory "artifacts/tests/P4-A03"
```

**Evidence:** `artifacts/tests/P4-A03/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A04 — Image alpha composition

**Type:** Integration
**Arrange and execute:** Composite the transparent logo at different opacities over known frames.
**Assert:** Correct premultiplied-alpha behavior and expected edge pixels; no halo or destructive source change.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A04" --logger "trx;LogFileName=P4_A04.trx" --results-directory "artifacts/tests/P4-A04"
```

**Evidence:** `artifacts/tests/P4-A04/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A05 — Independent video-overlay playback

**Type:** Integration
**Arrange and execute:** Composite two clips and camera at different source in-points/speeds with explicit audio routes.
**Assert:** Each stream follows its own timing; visibility and audio routing remain independent.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A05" --logger "trx;LogFileName=P4_A05.trx" --results-directory "artifacts/tests/P4-A05"
```

**Evidence:** `artifacts/tests/P4-A05/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A06 — Keyframe interpolation and preset expansion

**Type:** Unit
**Arrange and execute:** Evaluate full poses before/between/after keyframes and expand fade/slide/pop presets.
**Assert:** Easing, duplicate-key policy and interpolation are deterministic; presets remain ordinary editable keyframes.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A06" --logger "trx;LogFileName=P4_A06.trx" --results-directory "artifacts/tests/P4-A06"
```

**Evidence:** `artifacts/tests/P4-A06/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A07 — Transition overlap model

**Type:** Unit
**Arrange and execute:** Construct valid and insufficient-handle cut/dissolve/slide transitions across different sources and speeds.
**Assert:** Duration math, source ranges and event weighting agree; unsupported ranges fail instead of inventing footage.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A07" --logger "trx;LogFileName=P4_A07.trx" --results-directory "artifacts/tests/P4-A07"
```

**Evidence:** `artifacts/tests/P4-A07/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A08 — Subtitle import/export round trip

**Type:** Unit
**Arrange and execute:** Round-trip UTF-8 SRT with multiline Unicode, adjacent intervals and invalid time ranges.
**Assert:** Millisecond timing/text are preserved where valid; invalid input is rejected without overwriting captions.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A08" --logger "trx;LogFileName=P4_A08.trx" --results-directory "artifacts/tests/P4-A08"
```

**Evidence:** `artifacts/tests/P4-A08/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A09 — Pointer and click override persistence

**Type:** Unit
**Arrange and execute:** Hide/restyle/restore captured events, including duplicate clip instances and crop transforms.
**Assert:** Source IDs are immutable; deleted override decisions persist; restored effects use actual captured data only.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A09" --logger "trx;LogFileName=P4_A09.trx" --results-directory "artifacts/tests/P4-A09"
```

**Evidence:** `artifacts/tests/P4-A09/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A10 — Keyboard captured versus authored effects

**Type:** Unit
**Arrange and execute:** Restore real allowed events and attempt recovery from off/suppressed spans; add manual badges.
**Assert:** Unavailable history is not fabricated and authored content retains distinct provenance.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A10" --logger "trx;LogFileName=P4_A10.trx" --results-directory "artifacts/tests/P4-A10"
```

**Evidence:** `artifacts/tests/P4-A10/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A11 — Independent mixer and availability

**Type:** Integration
**Arrange and execute:** Mix known per-source tones with mute/gain/pan/fades and capture-off intervals.
**Assert:** Routing/amplitudes/sample ranges are correct; absent spans are distinct from available silence; disabling one source leaves others intact.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A11" --logger "trx;LogFileName=P4_A11.trx" --results-directory "artifacts/tests/P4-A11"
```

**Evidence:** `artifacts/tests/P4-A11/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A12 — Peak policy and processing bypass

**Type:** Integration
**Arrange and execute:** Mix simultaneous near-full-scale sources and toggle basic gate/gain and monitoring.
**Assert:** Declared peak policy is applied; bypass is reversible; monitoring settings cannot modify capture manifests.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A12" --logger "trx;LogFileName=P4_A12.trx" --results-directory "artifacts/tests/P4-A12"
```

**Evidence:** `artifacts/tests/P4-A12/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A13 — Cross-layer timing stress

**Type:** Unit
**Arrange and execute:** Trim/reorder/duplicate/speed-change clips with events, captions, keyframes, webcam and transitions.
**Assert:** Source anchors and project anchors follow their separate documented semantics with no duplicate or lost boundaries.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A13" --logger "trx;LogFileName=P4_A13.trx" --results-directory "artifacts/tests/P4-A13"
```

**Evidence:** `artifacts/tests/P4-A13/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A14 — Shared renderer parity

**Type:** Integration
**Arrange and execute:** Evaluate controlled composed frames and audio through preview and actual export paths at matching timestamps.
**Assert:** Pre-encode scene equality and post-encode visual/audio tolerance meet the testing guide; UI chrome is excluded.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A14" --logger "trx;LogFileName=P4_A14.trx" --results-directory "artifacts/tests/P4-A14"
```

**Evidence:** `artifacts/tests/P4-A14/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-A15 — All-effects persistence and source immutability

**Type:** Integration
**Arrange and execute:** Save/reopen a complete P4 project, modify it and render an actual short clip.
**Assert:** Styles, runs, assets, keyframes, hidden IDs and mixer state survive; capture-media and event hashes remain identical.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P4_A15" --logger "trx;LogFileName=P4_A15.trx" --results-directory "artifacts/tests/P4-A15"
```

**Evidence:** `artifacts/tests/P4-A15/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.
