# Nexus.FrameStudio — review guide

## Start

Extract the ZIP, open `index.html`, set browser zoom to 100%, and press F11. Alternatively open the single-file `FrameStudio.offline.html`. Use the **54 screens** button to browse the catalog.

The desktop, device names, live meters, recording and export progress are simulated. This is a UI prototype, not a native capture application.

## A short complete workflow

| Step | Open / do this in the UI | Expected result | Remaining for the native app |
|---|---|---|---|
| 1 | 06 Quick recording → 07 Source → choose a monitor/window/region | Selected source mode and preview update | Real device enumeration and source capture |
| 2 | 08 Multi-monitor layout → choose screens and geometry | Selection and fit/fill design is visible | Mixed-DPI physical-pixel mapping and real frames |
| 3 | 11 Audio → turn microphone capture off | Switch shows off; PC audio stays separately enabled | Actual independent capture devices |
| 4 | 14–17 → configure cursor, clicks and keyboard badges | Controls retain values and supported preview styling changes | Native event acquisition and synchronized overlay rendering |
| 5 | 19 Countdown → choose 0; 24 Readiness → start simulation | Screen 25 runs a visible timer, clearly marked simulation | Native encoder, permissions and stream acquisition |
| 6 | Wait two seconds; pause; resume; add marker; stop | Screen 26 shows a simulated take and source availability | Real finalized media, drift and drop handling |
| 7 | Open editor → 43 Audio mixer | Microphone is unavailable because capture was off | Same source rules enforced against actual media |
| 8 | Mute PC sound in the editor, then unmute | Capture state remains unchanged; output selection changes | Audible mix preview and rendered audio |
| 9 | Load demo via the project library; 29 Trim / split | Split creates another editable clip; undo restores the prior sequence | Frame-accurate native cuts and decoded playback |
| 10 | 30 Join → append demo clip → move it left | Clip order changes without changing source media | Native multi-source playback and export |
| 11 | 33 Text → edit title; 35 Shapes → add a circle | Text changes; a selectable shape appears | Final renderer fidelity |
| 12 | Drag or resize an overlay; 38 Animation → add keyframe | Geometry/keyframe data update; preset preview animates | Full timing, interpolation and render-engine integration |
| 13 | 04 Import → choose a local image or short video | Asset enters the bin; use it in an overlay or timeline | Wider native format support and robust proxies |
| 14 | 47 Save project → download; 04 Import → reopen it | Settings, edits and review state return; sources may need relinking | Atomic native save and portable raw media packaging |
| 15 | 48 Export → run, cancel or complete simulation | Clear status; no claim that an MP4 was created | Actual media export and output verification |
| 16 | 50 Track inspector → inspect sample JSON | Frame time, cursor, key and audio references are visible | Production per-frame index writer and reader |
| 17 | Give feedback on a screen; 54 Review → export review | Markdown includes decisions and notes | Owner approval before phase planning |

## How to report an issue

Use: **Screen number · Action · Expected · Actual · Screenshot · Priority**.

Example: `33 · Change title size to 72 · Title remains within canvas · Right edge clips · Screenshot attached · Medium`.

Record whether the issue concerns visual layout, prototype behavior, or a future native feature. Do not report a clearly labeled simulated MP4 export as a failed real encoder.

## Approval questions

Confirm the name, dark/light design, navigation density, basic-editor feature scope, independent-track recording rule, privacy behavior and proposed editable/raw formats. Mark each screen Approved or Needs changes; export review notes before resetting the demo.

**Approval is for the design only.** No implementation phases are included yet. After approval, every phase must use this handoff format:

| Required field | Meaning |
|---|---|
| Scope and exclusions | What the phase implements and deliberately leaves out |
| Task checklist | Small changes with dependencies and affected areas |
| Manual test cases | ID, prerequisite, exact UI actions and expected result |
| Automated test cases | ID, command, assertions and evidence location |
| Result and remaining work | Passed / failed / not run, defect links and incomplete items |
| Exit gate | Demonstration, regression evidence and reviewer approval |

Never replace unrun native tests with prototype test results. Do not claim data-loss protection without interruption and restoration evidence.
