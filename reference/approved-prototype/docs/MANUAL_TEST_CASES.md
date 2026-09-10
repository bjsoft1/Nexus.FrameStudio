# Manual prototype acceptance checks

**Status: Not run by a human on the target Windows machine.** The automated report is separate. Record Pass / Fail / Not run and attach evidence; do not infer a manual pass from an automated result. Save your draft before resetting or replacing it.

| ID | Check / screens | Exact UI steps | Expected result | Remaining work | Result / evidence |
|---|---|---|---|---|---|
| M01 | Launch / layout · 01 | Open index.html on Windows, press F11; inspect at 1920×1080. | Full-screen desktop layout; internal panels scroll without losing navigation. | Windows launch and browser-policy behavior remain manual. | Not run |
| M02 | Screen coverage · 53 | Open every catalog item; use Previous and Next. | 54 distinct screens; correct number and selected navigation. | No native application navigation yet. | Not run |
| M03 | Keyboard access · Any | Press Ctrl+K, search audio; use Tab and Escape. | Search opens, relevant routes appear, Escape closes dialog. | Full accessibility and screen-reader audit pending. | Not run |
| M04 | Capture source · 07 | Select window, region and monitor in turn. | Source mode changes and matching design options appear. | Real sources are fixtures. | Not run |
| M05 | Multiple displays · 08 | Toggle both monitors, change arrangement options. | Selection and layout controls retain values. | Mixed-DPI capture, hotplug and geometry tests pending. | Not run |
| M06 | Region gizmo · 09 | Drag the rectangle and resize its corner; use center/full area. | Coordinates remain within the 1920×1080 demo canvas. | Physical desktop region selection pending. | Not run |
| M07 | Presets · 06, 23 | Choose Small file, then Tutorial. | Resolution and bitrate change with the preset. | Actual file quality/size pending. | Not run |
| M08 | Audio separation · 11–12 | Disable mic capture, leave PC capture on. | Independent switches retain different states. | Device streams and audible meters pending. | Not run |
| M09 | Webcam framing · 13 | Change position, shape, size and mirror. | Mock camera frame reflects supported style changes. | Actual camera source/latency pending. | Not run |
| M10 | Mouse design · 14–15 | Change highlight color, click size and ripple style. | Demo pointer and effect previews update. | Real input hooks and cursor extraction pending. | Not run |
| M11 | Keyboard design · 16–17 | Change safe-key mode, badge size and location. | Example shortcuts show configured presentation. | Global input capture not performed. | Not run |
| M12 | Privacy boundary · 18 | Inspect excluded apps and privacy-stop settings. | Capture-off versus hide/sanitize explanations remain clear. | Secure-field detection and fail-closed tests pending. | Not run |
| M13 | Countdown cancel · 19, 24–25 | Choose delay 3; start simulation; stop before countdown ends. | No new take; previous session metadata stays intact. | Native cancellation cleanup pending. | Not run |
| M14 | Pause / marker · 25 | Start with delay 0; wait; pause; wait; resume; mark; stop. | Paused timer freezes; marker and simulated take are listed. | Actual timestamp/codec handling pending. | Not run |
| M15 | Uncaptured mic · 11, 25, 43 | Turn mic capture off; record simulation; stop; open audio mixer. | Microphone shows Not captured and cannot be unmuted into existence. | Real source validation pending. | Not run |
| M16 | Partial capture gap · 25, 50 | Start with mic on, disable mid-take, wait and stop. | Track is partially available; off interval is a gap. | Frame-accurate preview and render gap handling pending. | Not run |
| M17 | Non-destructive mute · 43 | With demo loaded, mute only PC sound; unmute it. | Microphone and captured-source facts stay unchanged. | Real audio mix output pending. | Not run |
| M18 | Clip edits · 29–30 | Split, undo, redo, append clip, move left, remove it. | Timeline structure changes; total split source duration preserved. | Decoded frame accuracy pending. | Not run |
| M19 | Crop / compression · 31–32 | Choose 1:1 crop; reset; set lower bitrate; apply to export. | Crop geometry and export plan values update. | No real crop or encoding happens. | Not run |
| M20 | Text / rich text · 33–34 | Edit title; toggle bold/italic and emphasized final word. | Preview text and separate emphasis span change. | Arbitrary selection-based rich text pending. | Not run |
| M21 | Shape and gizmo · 35 | Add circle, move/resize/rotate it, duplicate and send behind. | Overlay state and layer order update. | Native renderer fidelity pending. | Not run |
| M22 | Local assets · 04, 36–37 | Import PNG, then short browser-decodable MP4; place overlays. | Media appears locally, with source references and selectable layers. | Wider formats and compositing pending. | Not run |
| M23 | Animation / transition · 38–39 | Add transform keyframe; preview preset and transition. | Keyframe saved; illustrative animation plays. | Native timed composition and true clip dissolve pending. | Not run |
| M24 | Captions · 40 | Edit caption start/end/text, apply, export SRT. | Valid timed cues download as a real text sidecar. | Automatic transcription is not included. | Not run |
| M25 | Recorded effects · 41–42 | Hide cursor/keys, restyle, restore individual events. | Only presentation state changes; original capture stays available. | Source-time-correct native replay pending. | Not run |
| M26 | Project round-trip · 47, 04 | Save .nfsproject, change title, import saved project. | Saved edit/settings/review return; local media may need relinking. | Portable .nfsraw archive and atomic native saves pending. | Not run |
| M27 | Invalid project · 04 | Try malformed JSON and unsupported schema version. | Clear rejection; current project remains unchanged. | Production archive/migration validation pending. | Not run |
| M28 | Export states · 48–49 | Start simulation, cancel; restart and complete; simulate disk full. | Status changes; no fictitious MP4 download or source changes. | Real encoder, cancellation and disk recovery pending. | Not run |
| M29 | Theme / compact view · 52 | Switch dark/light; resize to 1366×768; inspect timeline. | Readable compact layout; no document-level overflow. | 125–200% OS scaling and full accessibility pending. | Not run |
| M30 | Feedback and backup · 54 | Add screen feedback and overall note; export review Markdown. | Report contains screen status and notes. | Owner approval and phase planning intentionally pending. | Not run |
