# Recorder/editor-only source review and extraction boundary

Input inspected: `Nexus.ProductivityCare(1).zip`. The archive remains unchanged. Review is restricted to recorder/video-editor areas plus the project file needed to identify target framework and dependencies. No original app build, installed run, native-device test or export validation was performed for this planning delivery.

The approved prototype's prior review is preserved at `reference/approved-prototype/docs/SOURCE_REVIEW.md`. This document adds phase-planning consequences.

| Reference area | Candidate reuse | Required change / verification | Owner phase |
|---|---|---|---|
| `Nexus.ProductivityCare.csproj` | WPF/.NET 10 Windows target as a starting baseline. | New assembly/namespace/storage identity; exclude unrelated packages/features; pin actual supported dependencies. | P1 |
| `Models/RecorderSettings.cs`, recorder settings window | Source/quality/audio/style/preset concepts. | Bind to approved standalone screens and distinguish capture from presentation controls. | P1–P2 |
| `Services/Recording/Capture/MonitorCaptureRecorder.cs`, `MultiMonitorCaptureRecorder.cs` | Windows capture adapters, cursor-disabled pixel path. | Re-test actual window/region/mixed-DPI geometry, handle loss and finalization. | P2 |
| `Services/Recording/Capture/RecordingSessionWriter.cs` | Append-style pointer/key sidecar writer and cursor assets. | Existing pointer sampling deduplicates identical positions; add explicit per-finalized-frame index/state references and reconcile actual PTS/frame count. | P2 |
| `Services/Recording/Capture/WasapiAudioCaptureSession.cs` | Separate loopback/mic capture and timing ideas. | Verify off/on privacy boundaries, source clocks, device restarts and metadata truth; old documentation contains historical status statements. | P2 |
| `Models/RecordingSessionManifest.cs` | Relative paths, stable session ID and parts. | New versioned native contract, availability spans, webcam, source clock maps, per-frame index and typed validation. | P1–P2 |
| `Models/RecordingProject.cs` | Non-destructive edits, tracks and overlay models. | Its `EffectiveClips` uses source-time ordering and the legacy empty-list-means-full-recording convention. Neither may define the new multi-source/ordered/empty timeline. | P1/P3 |
| `Windows/VideoEditorWindow.xaml(.cs)` and editing services | Editing interaction/renderer concepts. | Replace old window layout with approved reusable views; support arbitrary joined clips, rich text and independent image/video/camera overlays. | P3–P4 |
| Export, import, archive and recovery services under `Services/Recording/` | Staging, source protection, audio mix and media verification ideas. | Re-test against new schema, safe archives, concurrent writes, partial files and actual composed output. | P3–P5 |
| Recorder/editor tests and handoff documents | Existing regression scenarios and known edge cases. | Adapt tests to the new solution; historical green reports are not current evidence. | All |

## Do not copy

Do not copy the whole App/MainWindow initialization or whole `.csproj` package list. Exclude reminder/eye-care/posture/water tools, screenshot/image-editor/color-picker features, 3D viewer, sign-in/accounts, deployment identities, Store identity/certificates, user settings and private recordings. Reuse an icon/theme helper only when it is actually required and its provenance is recorded.

## Compatibility policy

The prototype `.nfsproject` is a UI-demo schema. The old app's recording/project schemas are different again. Native FrameStudio has a distinct format kind and version. Unrecognized formats must return a clear unsupported/migration-required result, not silently erase unsupported fields. Automatic legacy migration is not part of the approved baseline; an explicit converter needs its own tested scope/approval.

## Required P1 output

Produce a reuse register containing old path, new path, decision (copied/adapted/rewritten/not used), direct dependencies, license/notices and tests proving the new behavior. A new namespace alone is not evidence of safe isolation.
