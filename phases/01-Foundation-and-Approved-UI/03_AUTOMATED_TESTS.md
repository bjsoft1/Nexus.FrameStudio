# Phase 1 — Foundation & approved UI — automated test specifications

**All cases: NOT_RUN. Test bodies and the native solution must be implemented; these are future execution commands.**

Run build/fixture setup first. Use the phase wrapper described in `../../docs/TESTING_GUIDE.md` to reject zero-test runs and track coverage. UI tests need an interactive Windows desktop; Hardware cases require opt-in and actual controlled devices.

## P1-A01 — Standalone clean build contract

**Type:** Build
**Arrange and execute:** Restore locked dependencies in a clean Windows checkout and build all new projects.
**Assert:** Zero build errors; no reference to ProductivityCare binaries, namespaces or private absolute build paths.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A01" --logger "trx;LogFileName=P1_A01.trx" --results-directory "artifacts/tests/P1-A01"
```

**Evidence:** `artifacts/tests/P1-A01/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A02 — Versioned project round trip

**Type:** Unit
**Arrange and execute:** Serialize and deserialize a minimal native project, session references and settings.
**Assert:** Stable IDs, canvas, kind/version and empty collections survive without defaulting to legacy behavior.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A02" --logger "trx;LogFileName=P1_A02.trx" --results-directory "artifacts/tests/P1-A02"
```

**Evidence:** `artifacts/tests/P1-A02/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A03 — Invalid-file transactional load

**Type:** Unit
**Arrange and execute:** Load malformed, future, wrong-kind, wrong-session and oversized JSON over an edited document.
**Assert:** Each returns a typed failure and preserves active state, saved file and backup bytes.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A03" --logger "trx;LogFileName=P1_A03.trx" --results-directory "artifacts/tests/P1-A03"
```

**Evidence:** `artifacts/tests/P1-A03/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A04 — Relative path containment

**Type:** Unit
**Arrange and execute:** Resolve relative assets plus rooted, UNC, traversal, drive and reparse-escape paths.
**Assert:** Only paths inside owned roots are accepted; rejected inputs cause no write.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A04" --logger "trx;LogFileName=P1_A04.trx" --results-directory "artifacts/tests/P1-A04"
```

**Evidence:** `artifacts/tests/P1-A04/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A05 — Atomic save failure injection

**Type:** Integration
**Arrange and execute:** Inject faults before temporary flush, replacement and backup update against disposable files.
**Assert:** Either prior-good or new-good document survives; malformed temporary content is never promoted.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A05" --logger "trx;LogFileName=P1_A05.trx" --results-directory "artifacts/tests/P1-A05"
```

**Evidence:** `artifacts/tests/P1-A05/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A06 — Theme schema and fallback

**Type:** Unit
**Arrange and execute:** Load valid data-only themes and invalid/missing/unknown fields.
**Assert:** Values are validated; unsafe content never becomes executable XAML; active resources stay usable on error.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A06" --logger "trx;LogFileName=P1_A06.trx" --results-directory "artifacts/tests/P1-A06"
```

**Evidence:** `artifacts/tests/P1-A06/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A07 — 54-route UI coverage

**Type:** UI
**Arrange and execute:** Launch with explicit fake adapters and visit the exact 54 reference route IDs.
**Assert:** Every state exists with correct headings and no unhandled exception or working-looking fake capture.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A07" --logger "trx;LogFileName=P1_A07.trx" --results-directory "artifacts/tests/P1-A07"
```

**Evidence:** `artifacts/tests/P1-A07/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A08 — UI geometry matrix

**Type:** UI
**Arrange and execute:** Render Home/Capture/Editor/dialogs at 1920×1080 and 1366×768 with 100/125/150/200 percent DPI.
**Assert:** Required controls are visible/reachable; AutomationId bounding boxes do not overlap critical actions.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A08" --logger "trx;LogFileName=P1_A08.trx" --results-directory "artifacts/tests/P1-A08"
```

**Evidence:** `artifacts/tests/P1-A08/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A09 — Keyboard accessibility

**Type:** UI
**Arrange and execute:** Tab through main workflows and inspect UI Automation names, focus and dialog close behavior.
**Assert:** Focus order is deterministic; primary controls have accessible names and keyboard invocation.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A09" --logger "trx;LogFileName=P1_A09.trx" --results-directory "artifacts/tests/P1-A09"
```

**Evidence:** `artifacts/tests/P1-A09/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A10 — Isolated settings and library

**Type:** Integration
**Arrange and execute:** Create a new profile beside a sentinel old-app profile, then create/save/reopen projects.
**Assert:** Only Nexus.FrameStudio-owned paths change; old sentinel hashes stay identical.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A10" --logger "trx;LogFileName=P1_A10.trx" --results-directory "artifacts/tests/P1-A10"
```

**Evidence:** `artifacts/tests/P1-A10/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A11 — Dirty-state and command history

**Type:** Unit
**Arrange and execute:** Execute commands followed by undo/redo and close choices Save/Discard/Cancel.
**Assert:** State transitions match decisions; cancel is non-mutating; undo has no source-media writes.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A11" --logger "trx;LogFileName=P1_A11.trx" --results-directory "artifacts/tests/P1-A11"
```

**Evidence:** `artifacts/tests/P1-A11/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A12 — Safe diagnostics

**Type:** Unit
**Arrange and execute:** Generate exceptions containing test secrets, full paths and device payloads.
**Assert:** Exported diagnostics redact sensitive fields and preserve only useful failure codes/context.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A12" --logger "trx;LogFileName=P1_A12.trx" --results-directory "artifacts/tests/P1-A12"
```

**Evidence:** `artifacts/tests/P1-A12/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A13 — Clock and interval primitives

**Type:** Unit
**Arrange and execute:** Evaluate half-open intervals, rational PTS conversions, pause mappings and source availability states.
**Assert:** Boundaries are consistent and cannot label unrecorded spans as captured.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A13" --logger "trx;LogFileName=P1_A13.trx" --results-directory "artifacts/tests/P1-A13"
```

**Evidence:** `artifacts/tests/P1-A13/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A14 — Renderer feasibility smoke

**Type:** Integration
**Arrange and execute:** Decode controlled fixture frames and composite two sources plus styled text through the proposed shared backend.
**Assert:** Real output frames exist with expected dimensions/alpha/text; capability failures are actionable.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A14" --logger "trx;LogFileName=P1_A14.trx" --results-directory "artifacts/tests/P1-A14"
```

**Evidence:** `artifacts/tests/P1-A14/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-A15 — Test runner integrity

**Type:** Integration
**Arrange and execute:** Invoke the phase runner with a nonexistent filter, failing case and absent Windows/device prerequisite.
**Assert:** Zero discovered tests is failure; absent prerequisites are NOT_RUN/BLOCKED; TRX and summary never invent PASS.

```powershell
dotnet test Nexus.FrameStudio.sln -c Release --no-build --filter "FullyQualifiedName~P1_A15" --logger "trx;LogFileName=P1_A15.trx" --results-directory "artifacts/tests/P1-A15"
```

**Evidence:** `artifacts/tests/P1-A15/` — TRX/logs plus probe/images/media hashes appropriate to the assertion.
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.
