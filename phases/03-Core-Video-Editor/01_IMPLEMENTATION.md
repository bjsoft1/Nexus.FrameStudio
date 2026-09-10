# Phase 3 — Core video editor

**Status: NOT_STARTED. This is a development specification, not a completion report.**

## Deliverable

A usable non-destructive editor for importing, trimming, splitting, joining, cropping, resizing and basic timing/color changes.
## Prerequisite

Phase 2 must have a clean build, required regression evidence and explicit owner approval. Read its actual handoff before changing code.
## In scope

Implement multi-source timeline editing, synchronized playback, media relinking, undo/redo, safe saves, speed/color/canvas controls and a basic actual MP4 render path.
## Not in this phase

Rich overlays, transitions, detailed input styling and the full audio mixer arrive in P4. Full render queue, portable raw archive and release packaging arrive in P5.
## Twenty implementation tasks

| ID | Task | Implementation | Done when |
|---|---|---|---|
| P3-T01 | Implement media probing and import | Import baseline MP4 H.264/AAC, PNG/JPEG and WAV plus any explicitly probed supported formats into owned assets. | Unsupported, malformed and cancelled imports leave the project and source files intact. |
| P3-T02 | Implement multi-source project assets | Store stable source/session/asset IDs independently of timeline clip instances and media locations. | The same source can appear twice and a project can join different recordings and imported files. |
| P3-T03 | Implement non-destructive relinking | Locate missing assets, verify identity/metadata and require confirmation for a different file. | Relinking changes only the asset locator; timing and edits stay intact. |
| P3-T04 | Implement the timeline model | Represent ordered clip instances with source in/out, timeline start, speed and track ownership; never sort clips by source time. | An empty timeline is empty, not an implicit request to restore all original footage. |
| P3-T05 | Implement playback and seeking | Decode real frames with cancellation, frame-step, thumbnails, play/pause and a synchronized audio clock. | Rapid seeks show the latest frame and cannot resume stale playback or leak decoders. |
| P3-T06 | Implement trim handles | Drag or type clip bounds with snapping and minimum duration validation. | Trimming keeps original bytes unchanged and visibly updates source/timeline duration. |
| P3-T07 | Implement split/delete/ripple | Split at valid frame boundaries; distinguish ripple deletion from a retained gap and support selection. | Removed ranges and event references follow the selected deletion mode. |
| P3-T08 | Implement join/reorder/duplicate | Append and reorder clips from any source; duplicate clip instances without copying source media. | A two-source A-B-A sequence renders in that exact order. |
| P3-T09 | Implement undo/redo for edits | Group drags into commands and cover trim, split, move, delete, crop and numeric edits. | Undo/redo restores model and visible state without altering captured media. |
| P3-T10 | Implement tracks and caches | Virtualize timeline drawing, thumbnails and waveforms; expose lock, visibility and selection states. | Long sessions and repeated zooming do not create unbounded background work. |
| P3-T11 | Implement crop and reframe | Apply free/preset crops in source space with a documented transform chain. | Changing crop keeps future cursor/click overlays aligned with the same source feature. |
| P3-T12 | Implement resize/compression settings | Apply canvas size, aspect fit and bitrate targets with validation and approximate size feedback. | Quality reduction affects output settings, not the original source or editable resolution. |
| P3-T13 | Implement speed and timing | Add 0.5×, 1× and 2× playback/render timing with explicit audio behavior and event remapping. | Trimmed or sped-up events land on the correct content; pitch-preservation is not falsely claimed. |
| P3-T14 | Implement basic color controls | Add brightness, contrast and saturation using a deterministic shared evaluation path. | Reset restores neutral pixels; preview and basic export use the same values. |
| P3-T15 | Implement canvas/background controls | Add aspect presets, padding, background and border with non-destructive positioning. | Portrait, square and landscape exports retain source aspect without unintended stretching. |
| P3-T16 | Implement baseline audio playback | Play captured and imported audio with basic per-track include/mute state and source availability. | Captured audio can be muted/restored; uncaptured intervals stay unavailable. |
| P3-T17 | Implement persistent edit round trips | Save ordered clips and all P3 edit parameters, autosave snapshots and relink hints in supported schemas. | Closing/reopening restores the same timeline and a malformed autosave cannot replace a good save. |
| P3-T18 | Implement a basic real export slice | Render cuts, crop, resize, speed, basic color and basic audio to a verified MP4 through the future final pipeline. | At least first/middle/last frames and duration decode correctly; no simulation is reported as output. |
| P3-T19 | Implement actionable editor failures | Keep the current document on missing media, decoder errors or canceled operations; show recovery guidance. | Failed import/render never destroys a saved project or replaces an existing completed export. |
| P3-T20 | Complete core-editor acceptance | Demonstrate a real two-source edit and save/reopen/export workflow; run P1–P3 regression. | Timeline correctness, basic audio and source hashes are evidenced before P4 approval. |

## Approved UI references

04 Import media, 05 Relink missing media, 27 Timeline editor, 28 Media & tracks, 29 Trim & split, 30 Join & rearrange, 31 Crop & reframe, 32 Resize & compress, 44 Speed & timing, 45 Color & adjustments, 46 Canvas & background.
P1 owns visual coverage of every screen. The above list identifies primary functional completion; shared screens are progressively integrated. See the complete screen-phase map.

## Required evidence and gate

Join two real clips, remove a middle section, crop/resize, save/reopen, and render a playable MP4 whose timing and source hashes are verified.

Run the 15 manual cases and implement/run the 15 automated cases in this folder, plus previous required regressions. Save actual outputs and hashes for media/storage tests. All current required cases must be PASS with evidence; BLOCKED/NOT_RUN is not approval.

Complete `04_HANDOFF_AND_REMAINING.md`. Only the owner/reviewer may approve the next phase. See the common testing guide for exception and release rules.
