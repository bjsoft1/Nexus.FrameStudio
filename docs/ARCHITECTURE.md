# Engineering baseline and boundaries

**Proposed implementation choices, not a report of implemented features.** The UI approval establishes the design. Phase 1 validates the engineering choices; changes require a recorded decision rather than a silent rewrite.

## Platform

Use C# on .NET 10 with WPF for a Windows 11 x64 desktop application. The uploaded project's `.csproj` already targets `net10.0-windows10.0.19041.0` with WPF; this is the smallest conceptual migration boundary, not permission to copy its whole dependency graph. Pin an actually installed/tested .NET 10 SDK in `global.json` in P1. Windows-target APIs need runtime support checks even with a Windows-targeted TFM. Microsoft documents .NET 10 and Windows-only WPF separately [S1, S2 in SOURCES.md].

Initial supported product baseline: Windows 11 x64, SDR, MP4 H.264 video/AAC final audio, PNG/JPEG images and PCM WAV editing audio. Advertise additional imports only after successful probing and tests. Media Foundation has a documented native format set; a file extension alone does not prove its codec can decode [S5]. Keep 720p/1080p and capability-approved 1440p/4K presets visible with truthful enabled/disabled states. Windows N/KN, HDR, extra codecs, ARM64 and high-FPS capability need explicit support evidence, not assumptions.

## Suggested solution layout

```text
Nexus.FrameStudio/
  Nexus.FrameStudio.sln
  global.json
  Directory.Build.props
  src/
    Nexus.FrameStudio.App/            WPF shell, views, view models, native UX
    Nexus.FrameStudio.Core/           pure models, commands, clocks, mappings, validation
    Nexus.FrameStudio.Media.Windows/  capture, audio/camera, decode, compose, encode
    Nexus.FrameStudio.Storage/        project saves, workspace, raw package, recovery
  tests/
    Nexus.FrameStudio.Core.Tests/
    Nexus.FrameStudio.Integration.Tests/
    Nexus.FrameStudio.Ui.Tests/
  tools/                             build/run/test/fixtures/publish scripts created in P1/P5
  docs/
  artifacts/                         generated evidence; exclude private recordings from Git
```

No login, cloud backend, database server or unrelated ProductivityCare module is required. Optional future accounts/services must not block local recording or editing. App settings/catalog belong under `%LOCALAPPDATA%\Nexus.FrameStudio`; project/media folders are explicitly selected and owned. Native UI dimensions are DIPs; media geometry is physical pixels.

## Capture backend

Use a Windows Graphics Capture adapter for screen/window pixels and Direct3D-backed buffers with bounded queues. Disable app-captured cursor pixels through the supported capture property; Windows documents `GraphicsCaptureSession.IsCursorCaptureEnabled` [S3]. Preserve the cursor separately. Do not promise to remove cursors/effects already drawn inside a third-party app's captured pixels.

Use a WASAPI loopback adapter for selected PC/system audio and a separate input adapter for microphone audio; Windows documents loopback capture of a render endpoint [S4]. Existing audio code may be adapted only after current behavior is re-tested. Use a separate camera adapter/encoder with its own clock mapping. Device names are display metadata, not portable file identities. Capture permission and monitoring/mix settings are separate.

Backend contracts should include `ICaptureCoordinator`, `ICaptureSource`, `ISessionClock`, `IFrameIndexWriter`, `IInputEventSource`, `IAudioCaptureSource`, `ICameraSource`, `IMediaProbe` and `ICapabilityService`. Names are suggested; the isolation/invariants are required. A fake backend is selected only by explicit test/design mode, never as production fallback.

## Editor and render path

Separate source media from timeline clip instances. Each clip has a unique instance ID, source ID, in/out points, timeline placement, speed and layer. An empty timeline means empty. Never reuse a legacy helper that sorts clips by source time or interprets an empty list as the whole recording.

Use one authoritative `ITimelineMapper` and scene/audio evaluator. Preview and export must use the same layout, timing, text shaping, keyframe, transition and source-availability logic. The native display/encoder wrappers may differ; the composition model may not. Phase 1 must prove the chosen compositor can decode/combine at least two sources plus styled text. Retain an explicit backend boundary so a measured bottleneck can be fixed without rewriting the UI/domain.

Use Media Foundation decode/encode adapters as the starting baseline; its sink writer accepts configured streams and media samples [S6]. A normal WPF MediaElement by itself is not the full multi-track timeline/compositor. Do not introduce an unreviewed bundled transcoder as a shortcut. Any optional third-party native dependency needs a version, license/notices, deployment check, security review and owner-visible support change.

The safe save service exists in P1. Real recording exists in P2. A small real export path exists in P3, rich composition joins it in P4, and the queue/raw/release workflow is completed in P5. This avoids discovering basic media incompatibility only in the last phase.

## State and concurrency

Capture: Idle → Preflight → Countdown → Recording ↔ Paused → Finalizing → Completed, with Canceled/Failed/Partial as explicit outcomes. Source devices also have independent availability states. Serialize state transitions, reject duplicate starts and keep native resources on their appropriate threads.

Render jobs use immutable project snapshots. Writes use workspace locks and owned staging paths. Recover into a new workspace rather than rewriting possibly damaged originals. Bound queues/caches and cancel superseded seeks. Never run video encode or bulk archive work on the UI thread.

## Reuse limits

`docs/SOURCE_REUSE_REVIEW.md` names candidate components and risks. Existing code is a starting reference, not evidence that webcam, mixed-source joining, frame-index metadata or the approved UX already works. Retain or replace components based on tests, not historical handoff labels.
