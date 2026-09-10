# Editable recording and raw-package contract — proposed

This document describes the intended standalone product. The current `.nfsproject` download is a simpler **prototype** schema. The proposed production package is not implemented and does not imply backward compatibility with the uploaded app.

## Capture versus presentation

| Situation | Capture state | Later editor behavior |
|---|---|---|
| Microphone was on | Audio media and availability intervals exist | Mute, unmute, gain or remove from an export |
| Microphone was off throughout | No microphone samples | Show Not captured; never offer recovery |
| Microphone was disabled midway | Samples exist only for on-intervals | Preserve playable intervals and explicit silent/missing gaps |
| Keyboard events were captured but hidden later | Original allowlisted events still exist | Restyle, hide or restore them |
| Keyboard collection was off | No keyboard events for that interval | Do not synthesize the original pressed keys |
| Cursor/effects were baked into an imported video | Pixels are part of the source | No promise of reliable removal |

A user may manually add a new caption or keyboard illustration later. It must be labeled authored content, not reconstructed capture history.

## Proposed package layout

```text
Take-2026-09-10.nfsraw/                 # ZIP-based portable package, design only
  manifest.json                       # schema, IDs, hashes, relative paths
  project.json                        # mutable timeline and presentation
  capture/session.json                # immutable source manifest
  capture/frames/part-001.jsonl        # one record per encoded screen frame
  capture/events/pointer.jsonl         # high-rate position/button/scroll events
  capture/events/keyboard.jsonl        # allowlisted keyboard events only
  capture/events/markers.jsonl
  capture/cursors/arrow.png            # actual cursor bitmap/hotspot references
  media/screen-001.mp4                 # clean screen pixels, no baked effects
  media/webcam-001.mp4                 # independent camera source, when enabled
  media/system-001.wav                 # independent PC/system audio, when enabled
  media/microphone-001.wav             # independent microphone audio, when enabled
  assets/                             # imported image/video/audio resources
  thumbnails/
```

“Raw” means the preserved editable session, not uncompressed sensor RAW. MP4 may remain the normal playable screen video. A convenience composite MP4 may also be exported, but it must not replace the clean source and independent tracks. Audio is not stored as sample arrays in JSON. Media file types/encoder selection are future implementation decisions.

Inside the package every path is relative to its root. No container, developer-machine or `/mnt/data` paths belong in a user's project. A production loader must reject absolute paths, traversal, unsafe archive entries, oversized expansion, missing hashes and unsupported schema versions before extraction or overwrite.

## Per-frame index

Use a session-relative monotonic clock with integer microseconds. A frame has part ID, encoded-frame ordinal, presentation timestamp and duration. Actual timestamps are authoritative; never infer timing only from frame number divided by the chosen nominal FPS. A duplicated/dropped frame or variable-duration frame must be represented truthfully.

Each encoded screen frame resolves a pointer state (position in physical capture-canvas pixels, cursor shape/hotspot, pressed buttons and visibility), event references, source availability and audio sample ranges. Store high-rate pointer/key events separately so multiple clicks between frames are not lost. Persist repeated state IDs or an explicit frame state; deduplicating movement must not leave stationary frames unable to resolve a cursor. Out-of-canvas positions, focus loss, secure-input suppression and unrecorded intervals need explicit states.

Audio ranges reference files, first sample-frame and count. For stereo, a sample-frame contains both channels; channel count is not a timestamp multiplier. Intersect each frame's time interval with each source's available media spans. A frame can reference zero or several spans; uncaptured audio is null/unavailable, not a fabricated silent recording. Drift, device restarts and resampling require explicit clock mapping.

See `examples/frames-001.example.jsonl` and `examples/portable-session.example.json`. They contain synthetic data and references to illustrative, absent media files. They are not real recordings.

## Multi-monitor coordinates and pauses

Store physical monitor bounds including negative desktop coordinates, DPI/scale, capture origin, source dimensions and source-to-canvas transforms. Use fit/fill with explicit gaps for different monitor sizes; never stretch a display. Record layout-change events or split source parts when geometry changes. Map pointer coordinates through the same transform used for video.

Choose and document an active-recording timebase: pause does not extend output duration, and resume maps from wall-clock/device clocks into the next active timestamp. Preserve discontinuity metadata. Do not guess that mic, webcam and screen begin simultaneously; record measured source offsets.

## Editable project mapping

Each timeline clip references a source session/track and source in/out range, output placement and playback rate. Resolve the output playhead into the source timestamp before evaluating source-linked cursor/key/webcam/audio events. Splitting, joining, speed changes and reordering must carry this mapping. Overlay keyframes and authored text/captions use explicitly declared source or output time domains.

Keep capture facts immutable. Store visibility, gain, mute, effect style, overlay layer order, caption formatting and export selection in the editable project. A muted source remains available. A removed timeline item does not delete its media. Portable raw saving copies verified required media; it does not silently move or overwrite originals.

## Recovery and privacy

Use append-only event/frame parts, safely finalized media chunks, checkpoints and atomic project replacement. Detect unreadable media, report exact missing ranges and recover only verifiable parts. Do not claim interrupted MP4 recovery or no data loss without tests.

Record only with visible user consent. Safe-shortcut allowlisting is the intended default, not unrestricted keystroke logging. Ordinary text entry must be excluded; secure/uncertain input fails closed. The recorder must distinguish **capture off**, **preview hidden**, **export excluded**, and **source permanently removed**. Permanent sanitization should create a separately named verified package, list what will be removed, and require explicit confirmation. Hiding metadata does not sanitize the visible video or spoken audio.

## Version boundaries

- `kind: nexus.framestudio.prototype`, `schemaVersion: 1`: reopenable browser prototype state.
- `kind: nexus.framestudio.raw-session-design`, `schemaVersion: 1`: illustrative proposed production contract, not importable in the prototype.
- Future production formats require independent schema versioning, migration backups, validation and round-trip tests.
