# Phase 2 — Independent-track recorder — manual UI tests

**All cases: NOT_RUN. Run against the native phase build, not the HTML prototype.**

Read `../../docs/TESTING_GUIDE.md` for fixture setup, evidence and numeric targets. Screen numbers refer to the approved prototype/native equivalent. Test only disposable controlled data.

## P2-M01 — Clean monitor recording

**Prerequisites:** H01; fixture motion/timecode visible

1. In Capture (06) select the primary monitor (07) and 1080p30 (10).
2. Start from Preflight (24), move/click, then Stop (25).
3. Open the raw screen MP4 outside FrameStudio.

**Expected:** Real screen motion decodes; app-added cursor/click/key/border/webcam effects are not baked into the screen MP4.
**Evidence:** `artifacts/acceptance/P2/P2-M01/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M02 — Window capture and target loss

**Prerequisites:** H01; controlled test window

1. Choose Window in screen 07.
2. Start recording.
3. Minimize then close the selected window.
4. Stop and inspect Recording complete (26).

**Expected:** Correct window is captured; unavailable intervals or a safe stop are shown without switching to an unrelated window.
**Evidence:** `artifacts/acceptance/P2/P2-M02/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M03 — Custom region on secondary display

**Prerequisites:** H02; grid fixture

1. Open Custom capture area (09) on a negative-coordinate secondary display.
2. Select a known grid rectangle.
3. Record and compare the output edges.

**Expected:** Correct physical-pixel region is captured; recorded grid and pointer metadata align within one source pixel.
**Evidence:** `artifacts/acceptance/P2/P2-M03/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M04 — Mixed-DPI multi-monitor layout

**Prerequisites:** H02; displays of different sizes and 100/150 percent DPI

1. In Multi-monitor layout (08) select both displays.
2. Choose fit without stretching.
3. Move the cursor across their seam while recording.

**Expected:** Aspect ratios and gaps match stored transforms; pointer does not jump to an incorrect location at the seam.
**Evidence:** `artifacts/acceptance/P2/P2-M04/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M05 — Independent system and mic capture

**Prerequisites:** H03; use headphones and controlled tones

1. Enable system and mic in screens 11–12.
2. Play the system tone and speak a marker separately.
3. Stop and play each stored audio source on its own.

**Expected:** System and mic are independent; one source can be inspected without requiring the other.
**Evidence:** `artifacts/acceptance/P2/P2-M05/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M06 — Source disabled before capture

**Prerequisites:** H03

1. In screen 11 turn microphone capture Off and system capture On.
2. Record while speaking.
3. Inspect screen 26 and Session & JSON inspector (50).

**Expected:** Mic is Not captured with no recoverable mic content; system track remains available.
**Evidence:** `artifacts/acceptance/P2/P2-M06/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M07 — Source off/on interval

**Prerequisites:** H03; session timer

1. Start with mic On.
2. At session 10 seconds disable mic capture; at 20 seconds enable it.
3. Stop at 30 seconds and inspect screen 50.

**Expected:** The 10–20 second mic interval is unavailable; earlier/later mic content remains; monitoring mute is not confused with capture off.
**Evidence:** `artifacts/acceptance/P2/P2-M07/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M08 — Webcam independence and device loss

**Prerequisites:** H03

1. Enable webcam in screen 13.
2. Record, then disconnect the webcam.
3. Stop and inspect separate screen/camera files.

**Expected:** Camera is separate; screen recording is retained; camera loss has an explicit availability boundary and warning.
**Evidence:** `artifacts/acceptance/P2/P2-M08/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M09 — Pause, resume and markers

**Prerequisites:** H01

1. Set countdown to zero (19) and start.
2. Record five seconds; pause five wall-clock seconds; resume five seconds.
3. Add a marker and stop.

**Expected:** Session duration is about ten seconds, not fifteen; paused time has no captured input/media; marker maps to resumed content.
**Evidence:** `artifacts/acceptance/P2/P2-M09/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M10 — Frame index and rapid clicks

**Prerequisites:** H01; controlled low-FPS test mode

1. Record a stationary cursor, then multiple clicks within a frame interval.
2. Stop and open screen 50.
3. Compare decoded frame count with index and event references.

**Expected:** Every committed screen frame resolves state; all click edges remain as events even when more than one occurs between frames.
**Evidence:** `artifacts/acceptance/P2/P2-M10/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M11 — Keyboard privacy stop

**Prerequisites:** H01; controlled plain/secure/uncertain input helper

1. Enable only approved shortcuts (16–18).
2. Type test text, focus a secure field and trigger shortcuts.
3. Press the emergency stop and trigger another shortcut.

**Expected:** No ordinary typed text or secure/uncertain-input events are stored; after the stop no new keyboard events are retained.
**Evidence:** `artifacts/acceptance/P2/P2-M11/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M12 — Hotkeys, countdown and toolbar

**Prerequisites:** H01

1. Configure start/pause/stop shortcuts (20) and a five-second countdown (19).
2. Cancel one countdown.
3. Start again and control recording from the tray/toolbar.

**Expected:** Cancellation creates no take; shortcuts do not duplicate actions; toolbar is excluded from pixels where supported or a limitation is clearly shown.
**Evidence:** `artifacts/acceptance/P2/P2-M12/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M13 — Quality presets and preflight failures

**Prerequisites:** H01; read-only test folder

1. Save a custom preset (23).
2. Choose an unsupported encoder combination (10) and read-only output folder (22).
3. Run Preflight (24).

**Expected:** The selected settings persist; unsupported or unwritable choices prevent start with a specific reason.
**Evidence:** `artifacts/acceptance/P2/P2-M13/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M14 — Interrupted recording recovery

**Prerequisites:** H01; disposable workspace

1. Capture until at least two parts finalize.
2. Terminate the test process during the next part.
3. Relaunch and inspect Recovery (51).

**Expected:** Earlier committed parts remain playable; current partial is not reported as complete; missing tail duration is stated.
**Evidence:** `artifacts/acceptance/P2/P2-M14/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P2-M15 — Recorder-to-editor handoff

**Prerequisites:** P2 real take with independent tracks

1. In Recording complete (26), inspect source summary.
2. Open editor (27) and inspector (50).
3. Restart and reopen the take.

**Expected:** The same actual take, settings, timing and availability reopen without requiring original devices.
**Evidence:** `artifacts/acceptance/P2/P2-M15/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.
