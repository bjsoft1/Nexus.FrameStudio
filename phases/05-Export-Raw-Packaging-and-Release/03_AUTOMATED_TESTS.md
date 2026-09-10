# Phase 5 — Export, raw packages & release — automated test specifications

**All cases: NOT_RUN. Test bodies and the native solution must be implemented; these are future execution commands.**

Run build/fixture setup first. Use the phase wrapper described in `../../docs/TESTING_GUIDE.md` to reject zero-test runs and track coverage. UI tests need an interactive Windows desktop; Hardware cases require opt-in and actual controlled devices.

## P5-A01 — Output configuration and track inclusion

**Type:** Integration
**Arrange and execute:** Render approved presets and every include/exclude combination for audio, captions and interactions.
**Assert:** Independent probing matches selected settings/streams; unsupported choices fail clearly.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A01" --logger "trx;LogFileName=P5_A01.trx" --results-directory "artifacts/tests/P5-A01"
```

**Evidence:** `artifacts/tests/P5-A01/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A02 — Queue snapshot isolation

**Type:** Unit
**Arrange and execute:** Queue jobs, edit the live document, reorder/cancel/retry and restart the application.
**Assert:** Job snapshots are immutable; state transitions are truthful; retry policy is explicit.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A02" --logger "trx;LogFileName=P5_A02.trx" --results-directory "artifacts/tests/P5-A02"
```

**Evidence:** `artifacts/tests/P5-A02/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A03 — Encoder fallback classification

**Type:** Integration
**Arrange and execute:** Inject hardware initialization, source decode, permission and disk failures under Automatic and Software.
**Assert:** Only allowed initialization errors trigger one fallback; forced Software remains software; unrelated failures stay failures.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A03" --logger "trx;LogFileName=P5_A03.trx" --results-directory "artifacts/tests/P5-A03"
```

**Evidence:** `artifacts/tests/P5-A03/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A04 — Output verification and atomic promotion

**Type:** Integration
**Arrange and execute:** Corrupt candidate headers/tail/audio and inject cancellation/replacement failures near completion.
**Assert:** Invalid candidates never replace a good target; required independent frame/audio checks run before promotion.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A04" --logger "trx;LogFileName=P5_A04.trx" --results-directory "artifacts/tests/P5-A04"
```

**Evidence:** `artifacts/tests/P5-A04/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A05 — Source-target protection

**Type:** Unit
**Arrange and execute:** Target any source, project, metadata, backup, lock, alias or reparse escape as an export destination.
**Assert:** Every unsafe overwrite is rejected before write; ownership-aware safe output paths remain permitted.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A05" --logger "trx;LogFileName=P5_A05.trx" --results-directory "artifacts/tests/P5-A05"
```

**Evidence:** `artifacts/tests/P5-A05/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A06 — Raw package round trip and hashes

**Type:** Integration
**Arrange and execute:** Export a complete workspace, import to a different root and compare manifest/asset/timeline identities and media hashes.
**Assert:** All references resolve locally; captures remain identical; mutable snapshot matches; no absolute package paths.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A06" --logger "trx;LogFileName=P5_A06.trx" --results-directory "artifacts/tests/P5-A06"
```

**Evidence:** `artifacts/tests/P5-A06/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A07 — Archive adversarial validation

**Type:** Integration
**Arrange and execute:** Submit traversal, rooted/UNC/ADS paths, case collisions, link entries, zip-bomb limits and unsupported schema fixtures.
**Assert:** Preflight/staging validation rejects them; no write escapes staging and no project is registered on failure.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A07" --logger "trx;LogFileName=P5_A07.trx" --results-directory "artifacts/tests/P5-A07"
```

**Evidence:** `artifacts/tests/P5-A07/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A08 — Raw-package sanitization

**Type:** Integration
**Arrange and execute:** Package full data and a sanitized copy with muted mic and hidden keyboard omitted.
**Assert:** Full mode warns and preserves data; sanitized mode removes chosen media/events/references and marks redacted provenance without changing original.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A08" --logger "trx;LogFileName=P5_A08.trx" --results-directory "artifacts/tests/P5-A08"
```

**Evidence:** `artifacts/tests/P5-A08/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A09 — Recovery fault matrix

**Type:** Integration
**Arrange and execute:** Crash during project replacement, raw import/export and capture-part finalization, then restart.
**Assert:** Prior-good work and committed media survive; incomplete tails remain quarantined; recovered output is a new validated workspace.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A09" --logger "trx;LogFileName=P5_A09.trx" --results-directory "artifacts/tests/P5-A09"
```

**Evidence:** `artifacts/tests/P5-A09/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A10 — Workspace locking and cleanup

**Type:** Integration
**Arrange and execute:** Run simultaneous saves and cleanup against shared-source projects, proxies and stale lock fixtures.
**Assert:** Conflicting writes are blocked; only owned disposable data is removed; active/shared assets are protected.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A10" --logger "trx;LogFileName=P5_A10.trx" --results-directory "artifacts/tests/P5-A10"
```

**Evidence:** `artifacts/tests/P5-A10/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A11 — Second-machine portable workflow

**Type:** Hardware
**Arrange and execute:** Transfer a controlled raw package to a clean supported Windows machine and edit/export without original devices.
**Assert:** No machine-specific media path/device dependency; output timing and independent tracks remain correct.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A11" --logger "trx;LogFileName=P5_A11.trx" --results-directory "artifacts/tests/P5-A11"
```

**Evidence:** `artifacts/tests/P5-A11/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A12 — Long-session and drift benchmark

**Type:** Hardware
**Arrange and execute:** Execute a controlled sixty-minute baseline with clock markers and declared higher-quality stress cases.
**Assert:** Measured drift, achieved FPS, drops and memory satisfy the agreed hardware-specific budget; missing devices cannot pass.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A12" --logger "trx;LogFileName=P5_A12.trx" --results-directory "artifacts/tests/P5-A12"
```

**Evidence:** `artifacts/tests/P5-A12/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A13 — Installer identity and upgrade smoke

**Type:** Integration
**Arrange and execute:** Install/upgrade/uninstall in disposable Windows VMs using versioned test artifacts.
**Assert:** Correct identity/associations; no MP4 hijack or old-app identity reuse; user projects survive documented uninstall choices.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A13" --logger "trx;LogFileName=P5_A13.trx" --results-directory "artifacts/tests/P5-A13"
```

**Evidence:** `artifacts/tests/P5-A13/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A14 — Final UI and workflow regression

**Type:** UI
**Arrange and execute:** Walk the 54 native states across themes/sizes and run the complete controlled record-edit-save-raw-export workflow.
**Assert:** Approved routes/features stay reachable; outputs are real; no unhandled exceptions or unresolved critical UI defects.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A14" --logger "trx;LogFileName=P5_A14.trx" --results-directory "artifacts/tests/P5-A14"
```

**Evidence:** `artifacts/tests/P5-A14/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-A15 — Evidence and release-gate integrity

**Type:** Integration
**Arrange and execute:** Validate task/case coverage, test reports, artifact hashes, exception records and owner approval record.
**Assert:** Zero missing/failed/unrun required cases; each PASS has evidence; release cannot self-approve or inherit prototype-only results.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P5_A15" --logger "trx;LogFileName=P5_A15.trx" --results-directory "artifacts/tests/P5-A15"
```

**Evidence:** `artifacts/tests/P5-A15/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.
