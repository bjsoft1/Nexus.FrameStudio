# Phase 2 — Independent-track recorder

**Status: NOT_STARTED. This is a development specification, not a completion report.**

## Deliverable

A real screen recording with separate webcam, mic, system audio and frame-linked input metadata, ready to open in the editor.
## Prerequisite

Phase 1 must have a clean build, required regression evidence and explicit owner approval. Read its actual handoff before changing code.
## In scope

Implement monitor/window/region and multi-monitor capture, independent media sources, privacy-safe input events, frame indexing, presets, controls and interruption-safe finalization.
## Not in this phase

Finished artistic composition, timeline editing and sharing exports are not this phase. The screen MP4 is intentionally clean; a simple inspection player is sufficient.
## Twenty implementation tasks

| ID | Task | Implementation | Done when |
|---|---|---|---|
| P2-T01 | Probe actual recording capability | Enumerate displays, windows, audio and camera devices; distinguish unavailable, denied and unsupported states. | UI shows real sources and does not substitute fake devices in production. |
| P2-T02 | Implement single-source screen capture | Capture a chosen monitor or window into a clean video track without app-added pointer/effects. | A finalized MP4 decodes; closing/minimizing or losing a target produces an explicit state. |
| P2-T03 | Implement custom-region capture | Select/move/resize a physical-pixel rectangle, including non-primary and negative-coordinate displays. | Recorded content and region outline agree within the documented pixel tolerance. |
| P2-T04 | Implement multi-monitor composition | Store topology and source-to-canvas transforms; preserve aspect ratios and fill unused areas. | Mixed DPI and different monitor heights do not stretch content or misplace the cursor. |
| P2-T05 | Implement encoder settings | Apply size, FPS, bitrate and encoder choices with real capability checks and an explicit fallback policy. | Requested versus actual settings are recorded; unsupported settings never silently change quality. |
| P2-T06 | Implement separate system audio | Use a selected loopback endpoint and preserve its samples in an independent media track. | System sound can be decoded without requiring a microphone or mixing into clean screen video. |
| P2-T07 | Implement separate microphone audio | Capture the chosen mic, device format and availability intervals; separate monitoring from recording. | Mic off means no retained mic samples; monitor-mute does not change capture permission. |
| P2-T08 | Implement independent webcam capture | Store camera video separately with timestamps and configurable presentation framing/mirroring. | Camera unavailable or disconnected leaves the screen take usable and the missing interval explicit. |
| P2-T09 | Implement a shared session clock | Map video, camera, audio and events onto one session clock with source-specific clock anchors. | Pause/resume and device restarts do not accumulate silent timing drift or invent content. |
| P2-T10 | Implement per-frame indexing | Commit a frame record for every finalized encoded screen frame with source PTS, state and event/audio references. | Decoder frame count and final index agree; repeated cursor positions remain resolvable. |
| P2-T11 | Implement pointer event capture | Capture cursor image/hotspot, position, visibility, button edges and scroll with stable event IDs. | Multiple clicks within one video frame are preserved; off-canvas state is represented. |
| P2-T12 | Implement privacy-safe keyboard events | Capture only explicitly allowed display shortcuts while recording; suppress plain text, AltGr and uncertain/secure input. | No typed words, passwords or clipboard content enter sidecars, logs or diagnostic output. |
| P2-T13 | Implement live capture controls | Add visible start/countdown/cancel, pause/resume, markers, source capture toggles and stop. | Repeated clicks cannot start duplicate recordings; a capture toggle takes effect at a logged boundary. |
| P2-T14 | Implement toolbar, tray and hotkeys | Add configurable safe shortcuts and the emergency keyboard-capture stop; avoid stealing app shortcuts. | Controls remain usable on another monitor and capture chrome is excluded where supported or warned. |
| P2-T15 | Implement editable style presets | Save cursor/click/keyboard designs, frame/border/background and device preferences as data. | Styles affect preview only; source MP4 and independent media remain free of those effects. |
| P2-T16 | Implement preflight and output storage | Validate permissions, disk space, folder access and encoder readiness before capture starts. | A readiness failure gives a specific fix and creates no misleading completed take. |
| P2-T17 | Implement bounded pipelines | Bound queues, report dropped frames, release device handles, and split parts on geometry or source changes. | Stress or device loss yields diagnostics and valid intervals rather than unbounded memory growth. |
| P2-T18 | Implement durable part finalization | Journal writes, flush metadata and finalize short recoverable media parts before marking them committed. | Failure preserves earlier committed parts; an unfinished MP4 is never announced as complete. |
| P2-T19 | Implement recording review and inspector | Display captured/not-captured/redacted states, errors, duration and frame-linked JSON, then open the real take. | Each track and missing span is inspectable and references actual committed media. |
| P2-T20 | Complete recording evidence and handoff | Run P2 plus P1 regression, retain representative takes and privacy/geometry evidence. | Report hardware-dependent tests honestly and obtain approval before editor implementation. |

## Approved UI references

06 Quick recording, 07 Capture source, 08 Multi-monitor layout, 09 Custom capture area, 10 Recording quality, 11 System audio & tracks, 12 Microphone setup, 13 Webcam & layout, 14 Cursor appearance, 15 Click & scroll effects, 16 Keyboard capture, 17 Keyboard appearance, 18 Privacy & exclusions, 19 Countdown & controls, 20 Recorder shortcuts, 21 Recording frame & canvas, 22 Output & session storage, 23 Recording presets, 24 Preflight review, 25 Recording controls, 26 Recording complete, 50 Session & JSON inspector.
P1 owns visual coverage of every screen. The above list identifies primary functional completion; shared screens are progressively integrated. See the complete screen-phase map.

## Required evidence and gate

Record and decode a real take, inspect each independent source, demonstrate capture-off gaps and privacy stop, and reconcile every committed screen frame with its metadata.

Run the 15 manual cases and implement/run the 15 automated cases in this folder, plus previous required regressions. Save actual outputs and hashes for media/storage tests. All current required cases must be PASS with evidence; BLOCKED/NOT_RUN is not approval.

Complete `04_HANDOFF_AND_REMAINING.md`. Only the owner/reviewer may approve the next phase. See the common testing guide for exception and release rules.
