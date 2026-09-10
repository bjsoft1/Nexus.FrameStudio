# Phase 4 — Overlays, effects & audio — manual UI tests

**All cases: NOT_RUN. Run against the native phase build, not the HTML prototype.**

Read `../../docs/TESTING_GUIDE.md` for fixture setup, evidence and numeric targets. Screen numbers refer to the approved prototype/native equivalent. Test only disposable controlled data.

## P4-M01 — Text title and timing

**Prerequisites:** F01

1. Open Text overlay (33).
2. Add a title from seconds 2–5 with a selected font/size/color.
3. Seek before, inside and after that interval.

**Expected:** Title appears only in its range and matches the same bounds in an actual P4 rendered sample.
**Evidence:** `artifacts/acceptance/P4/P4-M01/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M02 — Mixed formatting and Unicode

**Prerequisites:** F01

1. Open Formatted text (34).
2. Enter Hello नमस्ते, apply bold to Hello and another color to नमस्ते.
3. Save/reopen and render.

**Expected:** Mixed runs, shaping, wrapping and emphasis survive; font fallback is explicit if the selected font is unavailable.
**Evidence:** `artifacts/acceptance/P4/P4-M02/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M03 — Shapes and layer order

**Prerequisites:** F01

1. In Shapes & callouts (35) add a rectangle, circle, arrow and highlight.
2. Overlap them, reorder, lock and duplicate.
3. Undo deletion.

**Expected:** Styles, hit testing, lock state, z-order and undo behave consistently in preview and render.
**Evidence:** `artifacts/acceptance/P4/P4-M03/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M04 — Image overlay transparency

**Prerequisites:** F01 and F03

1. Open Image overlay (36).
2. Add the transparent logo, resize, rotate and lower opacity.
3. Preview over moving video and render.

**Expected:** Alpha edges and background composite correctly; the base video remains unchanged.
**Evidence:** `artifacts/acceptance/P4/P4-M04/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M05 — Video and webcam overlays

**Prerequisites:** F01, F02, F04

1. Open Video & camera overlay (37).
2. Add B and captured webcam as timed overlays.
3. Crop/mirror/move one; hide then restore it.

**Expected:** Independent source timing and framing persist; hiding does not destroy captured camera media or implicitly duplicate its audio.
**Evidence:** `artifacts/acceptance/P4/P4-M05/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M06 — Animation and presets

**Prerequisites:** F01 with a text overlay

1. In Animation & keyframes (38) create positions at seconds 1 and 3.
2. Add opacity/easing, scrub both directions and apply/reset a preset.

**Expected:** Interpolated poses are deterministic; presets remain editable; render follows the same evaluation.
**Evidence:** `artifacts/acceptance/P4/P4-M06/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M07 — Transitions and short clips

**Prerequisites:** F01/F02

1. Open Clip transitions (39).
2. Apply a one-second dissolve then a slide.
3. Try a duration longer than available source handles.

**Expected:** Valid transition duration and overlap are shown; insufficient handles are rejected or explicitly shortened, never hidden frozen footage.
**Evidence:** `artifacts/acceptance/P4/P4-M07/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M08 — Captions and SRT

**Prerequisites:** F01

1. In Captions & subtitles (40) add two timed captions including Unicode.
2. Export SRT, reimport it and toggle burn-in on/off.

**Expected:** Text and millisecond timing survive; burned-in captions appear only when included in video output.
**Evidence:** `artifacts/acceptance/P4/P4-M08/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M09 — Cursor and click restyling

**Prerequisites:** F04

1. Open Edit cursor & clicks (41).
2. Change cursor size and left/right click designs.
3. Hide a single click, then restore it.
4. Apply a crop and render.

**Expected:** Effects follow original content and crop transforms; hidden/restored IDs work without changing source sidecars.
**Evidence:** `artifacts/acceptance/P4/P4-M09/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M10 — Keyboard edits and unavailable intervals

**Prerequisites:** F04

1. Open Edit keyboard effects (42).
2. Restyle an allowed captured shortcut and hide/restore it.
3. Try restoration in a keyboard-off interval.
4. Add a manual badge.

**Expected:** Captured events are editable; absent data stays unavailable; manual badges are labeled authored, not recovered.
**Evidence:** `artifacts/acceptance/P4/P4-M10/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M11 — Independent mixer and capture gaps

**Prerequisites:** F04 and WAV fixture

1. In Audio mixer (43) change only mic gain, mute only system and add imported audio.
2. Seek through the mic-off interval.
3. Unmute system and render.

**Expected:** Sources remain independent; absent mic time is not fabricated; exported routing matches preview.
**Evidence:** `artifacts/acceptance/P4/P4-M11/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M12 — Audio fades, peak handling and monitoring

**Prerequisites:** F04 plus full-scale tone fixture

1. In screen 43 add fades and play overlapping loud sources.
2. Bypass processing and toggle monitoring without changing source capture settings.

**Expected:** Fades and selected peak policy match render; monitoring/mix settings do not retroactively change recorded availability.
**Evidence:** `artifacts/acceptance/P4/P4-M12/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M13 — Timing after split, reorder and speed

**Prerequisites:** F04 with captions/keyframes

1. Split around an interaction, reorder and duplicate that clip, then set one copy to 2×.
2. Apply a transition and preview each copy.

**Expected:** Source-anchored events follow each instance; project-time titles stay where authored; no event jumps to deleted content.
**Evidence:** `artifacts/acceptance/P4/P4-M13/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M14 — All-effects round trip

**Prerequisites:** F09

1. Save editable project (47) with formatted text, shapes, image/video overlays, keyframes, hidden events and mixer values.
2. Close/reopen.
3. Undo a new edit.

**Expected:** All properties and source links return; new undo history does not alter immutable capture data.
**Evidence:** `artifacts/acceptance/P4/P4-M14/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P4-M15 — Composed preview/export parity

**Prerequisites:** F09; deterministic test frames

1. Render with all effects enabled.
2. Independently decode sampled frames and audio at test timestamps.
3. Compare against preview captures and source hashes.

**Expected:** Composition meets documented pixel/time/audio tolerances; source files and event JSONL hashes are unchanged.
**Evidence:** `artifacts/acceptance/P4/P4-M15/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.
