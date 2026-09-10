# Phase 4 — Overlays, effects & audio

**Status: NOT_STARTED. This is a development specification, not a completion report.**

## Deliverable

A layered editor with formatted text, shapes, image/video overlays, animation, subtitles and editable captured interactions/audio.
## Prerequisite

Phase 3 must have a clean build, required regression evidence and explicit owner approval. Read its actual handoff before changing code.
## In scope

Implement overlay tools, transform keyframes, transitions, captions, pointer/keyboard styling and independent audio mixing with shared preview/export evaluation.
## Not in this phase

AI transcription, generative effects, advanced color grading, arbitrary codecs and destructive removal of already-baked pixels are outside the approved basic editor.
## Twenty implementation tasks

| ID | Task | Implementation | Done when |
|---|---|---|---|
| P4-T01 | Implement overlay model and selection | Add typed overlay IDs, local/project/source anchors, durations, track/z-order and property commands. | Objects can be selected, locked, duplicated, reordered and removed with undo. |
| P4-T02 | Implement text overlays | Add timed titles with font family, size, color, alignment, position and wrapping. | Preview and render agree on text bounds and time ranges. |
| P4-T03 | Implement formatted text | Persist safe styled text runs for mixed bold, italic, underline and emphasis with Unicode shaping. | Mixed English/Nepali content round-trips without executing markup or breaking graphemes. |
| P4-T04 | Implement shapes and callouts | Add rectangles, rounded rectangles, ellipses, arrows, lines and highlights with fill/stroke controls. | All shapes can be transformed and exported with the selected style. |
| P4-T05 | Implement image overlays | Add PNG/JPEG assets with transparency, fit/crop, opacity and safe relinking. | A transparent logo composites correctly without changing the base clip. |
| P4-T06 | Implement video/webcam overlays | Decode timed picture-in-picture sources independently with source in/out, crop/mirror and explicit audio routing. | Moving/hiding a webcam affects only presentation and never discards its captured source. |
| P4-T07 | Implement canvas manipulation | Add move/resize/rotate, aspect lock, numeric controls, alignment, layer order and usable handles. | Inspector values and drag operations resolve to the same geometry at every UI DPI. |
| P4-T08 | Implement keyframe evaluation | Animate full transform/opacity poses with deterministic linear/ease interpolation and editable key times. | Seek, reverse scrubbing, save/reopen and render evaluate the same pose. |
| P4-T09 | Implement animation presets | Add fade/slide/pop presets by producing editable keyframes, not hidden baked effects. | Preset changes remain reversible and work with manual keyframe edits. |
| P4-T10 | Implement clip transitions | Add cut/dissolve/slide with explicit overlap duration and a documented shortage-of-handles policy. | Timeline duration, picture, audio and event remapping follow the same overlap model. |
| P4-T11 | Implement captions and subtitle output | Add manually authored timed captions, style controls and real UTF-8 SRT import/export. | Plain subtitle text and millisecond timing survive round trips; burn-in is optional. |
| P4-T12 | Implement editable pointer and click effects | Restyle cursor, left/right click, ripple, drag and scroll using captured IDs and frame transforms. | Hide/restore and per-event changes never rewrite capture JSONL or imply pixel-level removal. |
| P4-T13 | Implement editable keyboard effects | Restyle, hide or restore allowed captured shortcut badges and label manually authored badges separately. | No event is recovered from a capture-off or privacy-suppressed interval. |
| P4-T14 | Implement independent audio mixer | Add per-track mute/include, gain, pan, fades and a clipping/peak meter for mic/system/imported/overlay audio. | Muting one source leaves others intact; simultaneous peaks are handled without hidden destructive mixing. |
| P4-T15 | Implement simple audio processing | Add only validated basic gain/noise-gate behavior behind non-destructive settings; clearly label monitoring. | Processing bypass is reversible; unsupported advanced noise removal is not a working-looking fake switch. |
| P4-T16 | Implement timing across all layers | Route trims, duplicates, reorders, speed and transitions through the shared clip-time mapping. | Pointer, keys, webcam, captions and audio stay attached to their intended content. |
| P4-T17 | Unify preview and export rendering | Use one evaluator/compositor contract for rich text, shapes, overlays, animation and audio in both paths. | The composed preview and an actual rendered sample meet the documented frame/audio tolerances. |
| P4-T18 | Persist all effects safely | Save effect tracks, keyframes, styles, hidden event IDs and mixer settings with versioned migration. | Undo and save/reopen retain hidden-versus-uncaptured distinctions. |
| P4-T19 | Polish editor workflows | Add shortcuts, contextual help, focus behavior, accessible track controls and beginner-friendly defaults. | Required actions remain discoverable without expanding every advanced property panel. |
| P4-T20 | Complete composed-media acceptance | Produce representative rendered clips and run cumulative regression plus source-hash checks. | Evidence covers all overlay types and independent tracks before approval of P5. |

## Approved UI references

33 Text overlay, 34 Formatted text, 35 Shapes & callouts, 36 Image overlay, 37 Video & camera overlay, 38 Animation & keyframes, 39 Clip transitions, 40 Captions & subtitles, 41 Edit cursor & clicks, 42 Edit keyboard effects, 43 Audio mixer.
P1 owns visual coverage of every screen. The above list identifies primary functional completion; shared screens are progressively integrated. See the complete screen-phase map.

## Required evidence and gate

Render a composed clip with formatted text, shapes, image/video overlays, animation and independent audio; compare it with preview and prove hidden events can be restored only where captured.

Run the 15 manual cases and implement/run the 15 automated cases in this folder, plus previous required regressions. Save actual outputs and hashes for media/storage tests. All current required cases must be PASS with evidence; BLOCKED/NOT_RUN is not approval.

Complete `04_HANDOFF_AND_REMAINING.md`. Only the owner/reviewer may approve the next phase. See the common testing guide for exception and release rules.
