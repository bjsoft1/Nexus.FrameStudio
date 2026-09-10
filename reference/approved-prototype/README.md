# Nexus.FrameStudio
## Recorder + video editor · 54-screen interactive design prototype

A new, standalone HTML/CSS/JavaScript prototype inspired only by the recorder and video-editor areas of the supplied Nexus.ProductivityCare archive. The original archive is unchanged. This is not a compiled .NET application.

## Open and review

1. Extract the whole ZIP to a normal folder.
2. Open `index.html`, or double-click `START_FrameStudio.cmd` on Windows. No build, package install, login or network connection is needed for the prototype itself.
3. Use browser zoom 100% and F11 for a full-screen landscape review. The primary design target is 1920 × 1080; a compact 1366 × 768 layout is also provided. Panels scroll when necessary.

`FrameStudio.offline.html` is a self-contained alternative. It includes all 54 screens in one file. The files inside `pages/` are individual entry points to the same shared UI. Their names match screen numbers.

Use **54 screens** in the top bar, **Previous / Next** in the bottom bar, or **Ctrl+K** to jump to a screen. Start with Screen 06 for recording and Screen 27 for editing. The window minimize/close buttons are visual chrome; use the real browser controls.

## What actually works here

Navigation, editable settings, theme switching, source-availability simulation, timeline playback/seek, split/trim/reorder/delete, undo/redo, overlay edits and transforms, text formatting, keyframe data, local media import/preview where the browser can decode it, project JSON save/reopen, manual SRT export, JSON downloads and review notes.

Recording, meters, devices, monitoring, codec options, media composition and video export are **simulations or design controls**. No device access is requested, no global input is monitored and no MP4 is encoded. The desktop and camera preview are illustrative fixtures.

## Preserve your review

**Save project** downloads a `.nfsproject` JSON file containing settings, timeline and review state. Reopen it from **Import media → Open editable project**. The file does not embed your media; keep your source files and relink after reopening. Browser local storage is a convenience, not a backup, and can be unavailable on local files or restricted browsers. Different entry-file URLs may use separate storage; stay in one entry point for a review.

Use **Give feedback** at the bottom of any screen. Mark it Approved or Needs changes, add a note, and save. Screen 54 exports a Markdown review report. Review status does not automatically authorize development.

## Important data rule

Capture-off means data was never collected; it cannot be restored later. Editor mute/hide changes only presentation, so previously captured data remains available. When capture is disabled partway through a take, the missing interval remains a gap. See `docs/PROJECT_FORMAT.md`.

## Package contents

| Location | Contents |
|---|---|
| `index.html`, `FrameStudio.offline.html` | Main and self-contained entry points |
| `pages/` | 54 numbered HTML entry pages |
| `assets/` | Shared CSS, JavaScript, catalog and theme JSON |
| `docs/FEATURE_SUMMARY.md` | 20 editor and 20 recorder review points |
| `docs/REVIEW_GUIDE.md` | Suggested review workflow and approval checklist |
| `docs/MANUAL_TEST_CASES.md` | UI steps, expected results and remaining work |
| `docs/PROJECT_FORMAT.md` | Proposed editable/raw recording contract |
| `docs/SOURCE_REVIEW.md` | Recorder/editor source review and evidence anchors |
| `docs/KNOWN_LIMITATIONS.md` | Explicit prototype boundaries |
| `examples/` | Reopenable demo and illustrative metadata |
| `tests/` | Repeatable Playwright UI suite and actual result report |
| `screenshots/` | Browser-rendered reference screenshots |

## Testing

Read `tests/README.md` and `tests/results/REPORT.md`. Tests exercise prototype behavior only. The bundled result was produced by rendering the self-contained document in a headless browser. Direct local-file and local-server navigation were blocked by the test environment's browser policy, so those launch paths and browser-reload persistence were not validated there. They remain checks for your Windows machine. No policy settings were changed.

## Development gate

No five-phase implementation plan or production C# project is included yet. Review and approve the design first. Each later phase must include its own tasks, test instructions, expected outcomes, evidence, remaining work and explicit sign-off.
