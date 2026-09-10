# Phase 3 — Core video editor — automated test specifications

**All cases: NOT_RUN. Test bodies and the native solution must be implemented; these are future execution commands.**

Run build/fixture setup first. Use the phase wrapper described in `../../docs/TESTING_GUIDE.md` to reject zero-test runs and track coverage. UI tests need an interactive Windows desktop; Hardware cases require opt-in and actual controlled devices.

## P3-A01 — Transactional media import

**Type:** Integration
**Arrange and execute:** Import controlled MP4/PNG/JPEG/WAV and inject probe/copy errors and cancellation.
**Assert:** Only fully validated owned assets enter the project; source hashes and active edits are unchanged on failure.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A01" --logger "trx;LogFileName=P3_A01.trx" --results-directory "artifacts/tests/P3-A01"
```

**Evidence:** `artifacts/tests/P3-A01/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A02 — Source and clip identity

**Type:** Unit
**Arrange and execute:** Add the same media repeatedly across multiple sessions and create duplicate clip instances.
**Assert:** Asset IDs remain stable; clip instance IDs are unique; order is independent from source in-time.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A02" --logger "trx;LogFileName=P3_A02.trx" --results-directory "artifacts/tests/P3-A02"
```

**Evidence:** `artifacts/tests/P3-A02/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A03 — Relink identity validation

**Type:** Unit
**Arrange and execute:** Relink missing assets to correct, incompatible and same-name-different-content candidates.
**Assert:** Correct links preserve edits; mismatches require explicit approval and never mutate media.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A03" --logger "trx;LogFileName=P3_A03.trx" --results-directory "artifacts/tests/P3-A03"
```

**Evidence:** `artifacts/tests/P3-A03/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A04 — Frame-accurate timeline operations

**Type:** Unit
**Arrange and execute:** Trim, split and ripple/delete intervals at frame boundaries including zero-duration and empty-timeline cases.
**Assert:** Durations and gap semantics are correct; empty means empty; no implicit legacy full-recording restoration.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A04" --logger "trx;LogFileName=P3_A04.trx" --results-directory "artifacts/tests/P3-A04"
```

**Evidence:** `artifacts/tests/P3-A04/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A05 — Join and source-order regression

**Type:** Unit
**Arrange and execute:** Build A[0–4], B[0–6], A[7–10], reorder B first and duplicate A.
**Assert:** Initial duration is thirteen seconds; output mapping follows explicit instances, not sorted source timestamps.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A05" --logger "trx;LogFileName=P3_A05.trx" --results-directory "artifacts/tests/P3-A05"
```

**Evidence:** `artifacts/tests/P3-A05/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A06 — Undo/redo operation sequence

**Type:** Unit
**Arrange and execute:** Apply random valid edit commands and invert/replay them.
**Assert:** Serialized timeline returns to expected states and capture-media hashes are unchanged.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A06" --logger "trx;LogFileName=P3_A06.trx" --results-directory "artifacts/tests/P3-A06"
```

**Evidence:** `artifacts/tests/P3-A06/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A07 — Source-to-timeline event mapping

**Type:** Unit
**Arrange and execute:** Map captured events/audio through trims, reorder, duplication and per-instance speed using rational time.
**Assert:** Deleted ranges emit no events; duplicates carry correct instance identity; boundary events are neither lost nor double-counted.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A07" --logger "trx;LogFileName=P3_A07.trx" --results-directory "artifacts/tests/P3-A07"
```

**Evidence:** `artifacts/tests/P3-A07/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A08 — Crop and output transform parity

**Type:** Unit
**Arrange and execute:** Transform a known source feature through crop, scale, padding, rotation policy and different output aspect ratios.
**Assert:** Pointer and visual feature share one transform; containment and reset are deterministic.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A08" --logger "trx;LogFileName=P3_A08.trx" --results-directory "artifacts/tests/P3-A08"
```

**Evidence:** `artifacts/tests/P3-A08/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A09 — Resize and bitrate validation

**Type:** Unit
**Arrange and execute:** Validate standard/custom export size and compression settings including odd encoder dimensions.
**Assert:** Dimensions are rejected or explicitly adjusted with confirmation; estimates are labeled approximate; sources are unchanged.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A09" --logger "trx;LogFileName=P3_A09.trx" --results-directory "artifacts/tests/P3-A09"
```

**Evidence:** `artifacts/tests/P3-A09/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A10 — Speed and audio timing

**Type:** Integration
**Arrange and execute:** Render 0.5×/1×/2× controlled clips with beep/click references and the documented audio mode.
**Assert:** Duration and synchronization meet budget; audio mode is declared; no hidden pitch-preservation promise.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A10" --logger "trx;LogFileName=P3_A10.trx" --results-directory "artifacts/tests/P3-A10"
```

**Evidence:** `artifacts/tests/P3-A10/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A11 — Color and canvas evaluation

**Type:** Integration
**Arrange and execute:** Evaluate brightness/contrast/saturation plus background/padding against deterministic frame fixtures.
**Assert:** Neutral reset is identity before encoding; preview and basic-render paths share expected evaluated pixels.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A11" --logger "trx;LogFileName=P3_A11.trx" --results-directory "artifacts/tests/P3-A11"
```

**Evidence:** `artifacts/tests/P3-A11/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A12 — Playback cancellation and audio clock

**Type:** Integration
**Arrange and execute:** Issue rapid asynchronous seek/play/pause requests over controlled sources.
**Assert:** Latest request wins; audio/video use one mapping; cancellation disposes stale decode resources.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A12" --logger "trx;LogFileName=P3_A12.trx" --results-directory "artifacts/tests/P3-A12"
```

**Evidence:** `artifacts/tests/P3-A12/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A13 — Timeline cache bounds

**Type:** Integration
**Arrange and execute:** Simulate repeated zoom/scroll across a one-hour fixture and measure queue/cache/object counters.
**Assert:** Peak resource use stays within configured budgets and returns near baseline after disposal.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A13" --logger "trx;LogFileName=P3_A13.trx" --results-directory "artifacts/tests/P3-A13"
```

**Evidence:** `artifacts/tests/P3-A13/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A14 — Save and recovery round trip

**Type:** Integration
**Arrange and execute:** Save P3 state, interrupt a later save and reopen using good/invalid autosave variants.
**Assert:** Clip order, crop, speed and color persist; invalid recovery never overwrites the good workspace.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A14" --logger "trx;LogFileName=P3_A14.trx" --results-directory "artifacts/tests/P3-A14"
```

**Evidence:** `artifacts/tests/P3-A14/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-A15 — Real basic MP4 render

**Type:** Integration
**Arrange and execute:** Render a multi-source edit, independently decode first/middle/last frames and audio, then cancel/fail another export.
**Assert:** Frame content/order/duration/audio are verified; existing output and sources survive failure unchanged.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P3_A15" --logger "trx;LogFileName=P3_A15.trx" --results-directory "artifacts/tests/P3-A15"
```

**Evidence:** `artifacts/tests/P3-A15/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.
