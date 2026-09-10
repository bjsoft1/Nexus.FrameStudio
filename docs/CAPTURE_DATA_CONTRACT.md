# Recording, editable project and raw-package contract

**Normative implementation requirements for the five phases; not a claim that the format or native media pipeline already exists.** P1 must turn this contract into versioned models, validators and deterministic fixtures. Do not silently reuse the prototype or legacy schemas.

## Three different outputs

| Output | Meaning | Editable later? |
|---|---|---|
| Clean screen `.mp4` | Normal encoded screen pixels without FrameStudio-added mutable effects. May intentionally be video-only. | Source pixels remain usable, but this file alone does not contain all independent tracks. |
| `.nfsproject` | Versioned JSON: asset references, ordered clip instances, overlays, timing and mix settings. | Yes, while referenced assets are available. It is not a media container. |
| `.nfsraw` | ZIP-based portable editable workspace containing referenced independent media and metadata. “Raw” means source-preserving, not uncompressed sensor RAW. | Yes, for sources actually included and available. |
| Final export `.mp4` | Composed video with selected overlays/effects and final audio mix. | Existing baked pixels/audio cannot simply be separated back into original editable tracks. |

## Native workspace and package layout

```text
ProjectWorkspace/
  project.nfsproject
  capture/session.json
  capture/frames/screen-001.jsonl
  capture/events/pointer.jsonl
  capture/events/keyboard.jsonl
  capture/events/markers.jsonl
  capture/cursors/<asset-id>.png
  media/screen-001.mp4
  media/webcam-001.mp4
  media/system-001.wav
  media/microphone-001.wav
  assets/<asset-id>.<extension>
  recovery/                     local snapshots/journal; not blindly shared
  cache/                        regenerable previews/proxies; not authoritative
```

A portable `.nfsraw` adds `manifest.json` at its root and includes a consistent project snapshot plus only referenced/finalized source data. It omits locks, private diagnostics, transient files and unnecessary caches. The manifest lists kind/version, IDs, normalized relative entry paths, sizes and SHA-256 hashes. File paths in exported documents are always relative to the package/workspace root. User-machine absolute locator hints stay in the local app catalog, never in the portable project.

Suggested distinct format kinds: `nexus.framestudio.native-project`, `nexus.framestudio.capture-session`, and `nexus.framestudio.raw-package`, each beginning at explicit schema version 1. Phase 1 records any approved naming adjustment. A missing project is not equivalent to malformed/newer/wrong-kind JSON. Wrong-kind imports must not silently become empty projects.

## Source versus presentation state

Each source owns availability spans with half-open bounds `[startUs, endUs)` and a reason: `captured`, `captureOff`, `permissionDenied`, `deviceLost`, `privacySuppressed` or `redacted`. Planned/not-yet-started is a separate lifecycle state. `captured` requires real committed media/events for that source interval, even when the recorded sound is actual silence.

Presentation state includes visible/include/mute, gain, styling and overrides. It never changes source acquisition history. Muting a recorded microphone in the editor can be undone. Disabling microphone capture does not produce recoverable microphone samples. Do not backfill captured flags when rendering silence over an unavailable interval.

A sample may overlap a capture-off boundary. Define the effective boundary on the session clock, discard post-boundary buffered content and persist only the valid prefix. If an intermediate WAV needs padding, mark it synthetic/missing-span padding, not captured sound. Camera and input sources obey the same availability distinction.

Capture settings are snapshotted per take/part. Recording OFF controls and editor mute controls need different labels and help. Monitoring controls affect what the user hears during work, not whether source content has been captured. Imported baked mouse/keyboard pixels are not independent events. Manual keyboard badges are authored overlays, never reconstructed history.

## Time model

Use an integer-microsecond session clock mapped from a monotonic source. Preserve each media part's original rational time base and presentation timestamps (`ptsTicks`, `timeBaseNumerator`, `timeBaseDenominator`) so rounding to microseconds is not the only source of truth. Native timestamp units and conversions belong inside the media adapter. Capture wall time is optional provenance, not the playback clock.

Session time excludes paused wall time. Resume creates a new part/clock anchor; it never stretches earlier media. Screen, webcam and each audio source have explicit clock anchors, discontinuity records and drift/resampling mapping. Finalized samples are mapped to presentation order, not codec packet/decode order. Final output time is a different timeline derived from clip instances, including speed and transition overlap.

A clip instance stores source ID, source in/out, timeline placement and speed. Project-time overlays remain at their authored project positions; source-anchored effects follow each clip instance. When a source clip is duplicated, overrides use a `(sourceEventId, clipInstanceId)` identity where an edit is instance-specific. Do not mutate the shared captured event to edit one duplicate.

## One index record per committed screen frame

Each screen-frame JSONL record must resolve:

| Field group | Required meaning |
|---|---|
| Identity | Session/source/part ID and presentation-order frame ordinal. |
| Time | Original rational PTS, duration and mapped session interval. Actual timing wins over nominal FPS. |
| Pointer | Current capture-canvas position, cursor asset/hotspot, visibility, pressed buttons and outside/unknown state; direct values or a valid state reference. |
| Events | All pointer/key/marker event IDs belonging to the frame interval, including multiple sub-frame events. |
| Availability | Actual source state/spans for screen, webcam, mic/system and input sources. |
| Media mapping | Source references for camera and zero or more audio sample-frame ranges with status/reason for missing intersections. |

JSONL permits incremental reading/writing. Deduplicated pointer state is acceptable only when every stationary frame still resolves the correct state. Store high-rate position/button/scroll/shortcut events in separate streams with stable IDs; do not collapse several clicks into a single boolean. At a PTS, evaluate the latest pointer state at or before it. Events belong to `[frameStart, frameEnd)` so an event exactly at the end belongs to the next frame.

At finalization, reconcile the index against actual presented video samples/frame count. Queue drops, duplicated frames, variable durations and encoder reordering must be explicit. A queued frame that never reached the finalized file is not a committed frame. The inspector must never infer missing metadata by pretending nominal FPS is authoritative.

## Audio references, not audio in JSON

Audio samples stay in separate media files. A reference uses source/part/file ID, sample rate, channels, starting **sample-frame** index and sample-frame count. Stereo sample-frames contain both channels; channel count is not a timestamp multiplier.

Intersect each video-frame interval with available audio spans. Use a documented rational boundary mapping (consistent integer boundary rounding, not accumulated per-frame rounding) to avoid overlap/drift. A frame may intersect multiple spans or none. Persist resampling/source-clock anchors where needed. Do not imply sample-exact hardware synchronization solely from two callbacks having close wall-clock timestamps.

## Physical coordinates and multiple monitors

Persist desktop bounds, including negative coordinates, device scale, capture origin, source size and source-to-canvas transform per part/layout revision. Layout changes split parts or emit a validated transform revision. The source-to-output transform order is documented and shared: source/desktop mapping → crop → clip transform → output scale/padding. UI DIPs are never written as captured physical-pixel positions. Keep unaligned-monitor empty regions explicit and aspect-preserving.

## Input privacy and package sharing

Collect keyboard events only after explicit user activation and only while recording. Use a conservative allowlist of safe display shortcuts/function/navigation keys; suppress ordinary typing, AltGr-like text input, secure fields and uncertain focus. The emergency stop must prevent new retained events even if a downstream write queue is busy. Never persist plaintext, clipboard content or private window titles to compensate for missing context.

Hiding a keyboard track or muting a mic is not permanent erasure. Before full raw export, state that those originals are included. A sanitized export creates a **new package** that removes selected source media/events, any derived captured badges chosen for removal, their references and unreachable assets; it marks redacted spans and recomputes hashes. Reopening cannot restore redacted content from that package. It does not secretly erase the original workspace. Permanent original deletion is a separate explicit destructive operation, not an editor mute.

Screen pixels may themselves contain sensitive data or effects drawn by other apps. Do not advertise keyboard suppression or raw sanitization as universal video redaction. Respect OS protected-content/device restrictions and clearly show unsupported exclusions.

## Durability, validation and recovery

Keep finalized captured parts append-only during capture and immutable during ordinary editing. Snapshot/journal mutable manifests safely. Use bounded part durations chosen and measured in P2 so a crash does not risk the entire session. Preserve already finalized parts; do not promise that an unfinished MP4 or buffered tail is recoverable. Report the last committed boundary and unverified/missing tail.

Validate archive entries before extraction and again before final promotion: schema, paths, traversal, rooted/UNC/drive forms, ADS, links/reparse escapes, case collisions, duplicates, allowed sizes/counts/expansion, free space, required entries, hashes and actual media probes. Extract to owned staging and publish only after validation. A corrupt archive leaves the active project untouched. Security limits are configurable but bounded and documented in P1/P5.

Use same-directory partial files and checked promotion for saves/exports. Keep a prior-good backup and avoid writing over a source, manifest, metadata, backup or active lock. Recovery copies validated content into a new workspace and lists what was not recovered. No ordinary edit/export may claim zero data loss just because a unit test passed.
