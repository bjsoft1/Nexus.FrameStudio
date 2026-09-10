# Phase 3 — Core video editor — manual UI tests

**All cases: NOT_RUN. Run against the native phase build, not the HTML prototype.**

Read `../../docs/TESTING_GUIDE.md` for fixture setup, evidence and numeric targets. Screen numbers refer to the approved prototype/native equivalent. Test only disposable controlled data.

## P3-M01 — Import baseline media

**Prerequisites:** F01, F02, F03 and WAV fixture

1. Open Import media (04).
2. Select the two videos, logo and audio.
3. View Media & tracks (28).

**Expected:** Supported assets are probed/imported with correct size/duration; source files remain unchanged.
**Evidence:** `artifacts/acceptance/P3/P3-M01/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M02 — Unsupported and canceled import

**Prerequisites:** F06; an open edited project

1. In screen 04 import a corrupt video or unsupported codec.
2. Cancel a large copy/probe.
3. Return to the timeline.

**Expected:** A useful error/cancel state appears; no partial asset is registered and existing edits remain.
**Evidence:** `artifacts/acceptance/P3/P3-M02/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M03 — Relink missing media

**Prerequisites:** F01 in an owned disposable workspace

1. Save, close and move one asset in the test workspace.
2. Reopen and use Relink missing media (05).
3. Try a wrong file, then the correct file.

**Expected:** Missing state is explicit; wrong identity needs confirmation; correct relink preserves clip timing and edits.
**Evidence:** `artifacts/acceptance/P3/P3-M03/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M04 — Playback, seek and frame-step

**Prerequisites:** F01; burned-in frame numbers

1. Open Editor (27).
2. Play/pause, frame-step, then seek rapidly between early and late frames.
3. Resume playback.

**Expected:** Displayed frame follows the latest request; audio follows playback; old seeks cannot overwrite the latest result.
**Evidence:** `artifacts/acceptance/P3/P3-M04/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M05 — Trim with exact duration

**Prerequisites:** F01; ten-second clip

1. Open Trim & split (29).
2. Set source in to 2 seconds and out to 8 seconds.
3. Preview and save.

**Expected:** The clip is six seconds with correct endpoints; the ten-second original stays unchanged.
**Evidence:** `artifacts/acceptance/P3/P3-M05/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M06 — Split, delete and empty timeline

**Prerequisites:** F01

1. Split at 4 and 7 seconds in screen 29.
2. Ripple-delete the middle segment.
3. Undo; then delete all clips.

**Expected:** Ripple result is seven seconds; Undo restores ten; deleting all leaves an empty project, not the whole source again.
**Evidence:** `artifacts/acceptance/P3/P3-M06/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M07 — Join, reorder and duplicate

**Prerequisites:** F01 and F02

1. In Join & rearrange (30) create A[0–4], B[0–6], A[7–10].
2. Preview the joins.
3. Move B first and duplicate one clip.

**Expected:** The initial sequence is thirteen seconds in the chosen order; later reorder/duplicate respects instance order, not source-time sorting.
**Evidence:** `artifacts/acceptance/P3/P3-M07/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M08 — Crop and transform alignment

**Prerequisites:** F01 grid and captured pointer sample

1. Open Crop & reframe (31).
2. Set a crop around a known grid feature and switch ratios.
3. Inspect the transformed feature and pointer position in screen 50.

**Expected:** Crop is valid, reset is reversible and source-to-output mapping stays within one output pixel before compression.
**Evidence:** `artifacts/acceptance/P3/P3-M08/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M09 — Resize and reduce quality

**Prerequisites:** F01

1. Open Resize & compress (32).
2. Select 1280×720 and a lower bitrate.
3. Render the basic P3 output (48).

**Expected:** Output probes as 1280×720 with the selected bitrate policy; original dimensions and media hash are unchanged.
**Evidence:** `artifacts/acceptance/P3/P3-M09/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M10 — Speed and timing

**Prerequisites:** F01 with timed beep/click reference

1. Open Speed & timing (44).
2. Set 2×, then 0.5×, then 1×.
3. Preview and basic-render each version.

**Expected:** Durations are five, twenty and ten seconds; reference events map correctly; the selected audio/pitch behavior is explicit.
**Evidence:** `artifacts/acceptance/P3/P3-M10/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M11 — Color and canvas

**Prerequisites:** F01

1. In Color & adjustments (45) change brightness/contrast/saturation.
2. In Canvas & background (46) choose portrait with padding and border.
3. Reset color.

**Expected:** Preview and basic output match chosen values; source aspect is preserved; color reset is neutral.
**Evidence:** `artifacts/acceptance/P3/P3-M11/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M12 — Independent basic audio state

**Prerequisites:** F04 with missing mic interval

1. Open Audio mixer (43).
2. Mute/unmute system audio.
3. Inspect the missing mic interval during playback.

**Expected:** System changes do not mute other available sources; no control pretends to recover missing microphone data.
**Evidence:** `artifacts/acceptance/P3/P3-M12/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M13 — Undo and safe reopen

**Prerequisites:** A P3 project after trim/reorder/crop/speed changes

1. Undo and redo each operation.
2. Save editable project (47).
3. Close/reopen, then reject an invalid autosave in Recovery (51).

**Expected:** Final timeline order and parameters return exactly; invalid recovery content does not replace good work.
**Evidence:** `artifacts/acceptance/P3/P3-M13/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M14 — Long timeline interaction

**Prerequisites:** F08

1. Open a long project in screen 27.
2. Repeatedly zoom/scroll and seek between distant points.
3. Observe diagnostic cache and queue counters.

**Expected:** Interaction stays responsive under agreed budgets; work queues/cache remain bounded and no decoder leaks accumulate.
**Evidence:** `artifacts/acceptance/P3/P3-M14/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P3-M15 — Actual basic export and cancel

**Prerequisites:** F01/F02 thirteen-second edit

1. Export to a new MP4 in screen 48.
2. Independently play first/middle/last frames.
3. Export again over an existing test target and cancel.

**Expected:** Real output order/duration/audio are correct; cancellation leaves the prior target and all sources unchanged.
**Evidence:** `artifacts/acceptance/P3/P3-M15/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.
