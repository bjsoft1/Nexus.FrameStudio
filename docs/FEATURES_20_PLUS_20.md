# Nexus.FrameStudio — 20 editor + 20 recorder points

Preserved from the approved prototype, with implementation ownership and acceptance references added. All native requirements are NOT_STARTED.

## Video editor — 20 points

| ID | Requirement | Primary phase | UI screens | Acceptance pointers |
|---|---|---|---|---|
| E01 | Import video, images and audio into one project. | P3 | 04, 28 | P3-M01; P3-A01 |
| E02 | Browse assets and relink missing source files. | P3 | 05, 28 | P3-M03; P3-A03 |
| E03 | Edit screen, webcam, visuals, audio and effects on separate tracks. | P3 | 27 | P3-M07; P3-A02 |
| E04 | Trim clip starts and ends without changing originals. | P3 | 29 | P3-M05; P3-A04 |
| E05 | Split clips at the playhead and remove unwanted sections. | P3 | 29 | P3-M06; P3-A04 |
| E06 | Join multiple clips and rearrange their order. | P3 | 30 | P3-M07; P3-A05 |
| E07 | Crop freely or choose landscape, square and portrait ratios. | P3 | 31 | P3-M08; P3-A08 |
| E08 | Resize video and reduce bitrate or output quality. | P3 | 32 | P3-M09; P3-A09 |
| E09 | Add text titles, labels and lower thirds. | P4 | 33 | P4-M01; P4-A02 |
| E10 | Format text with fonts, colors, emphasis and alignment. | P4 | 34 | P4-M02; P4-A02 |
| E11 | Add rectangles, circles, arrows, lines and highlights. | P4 | 35 | P4-M03; P4-A03 |
| E12 | Place images and logos over the main video. | P4 | 36 | P4-M04; P4-A04 |
| E13 | Place video and webcam picture-in-picture overlays. | P4 | 37 | P4-M05; P4-A05 |
| E14 | Move, resize, rotate, fade and reorder overlay layers. | P4 | 33, 34, 35, 36, 37, 38 | P4-M03; P4-A01 |
| E15 | Animate overlays with presets and transform keyframes. | P4 | 38 | P4-M06; P4-A06 |
| E16 | Choose transitions between neighboring clips. | P4 | 39 | P4-M07; P4-A07 |
| E17 | Create timed captions and export an SRT sidecar. | P4 | 40 | P4-M08; P4-A08 |
| E18 | Restyle or hide captured mouse and keyboard effects. | P4 | 41, 42 | P4-M09; P4-A09 |
| E19 | Mute and adjust mic, PC sound and imported audio separately. | P4 | 43 | P4-M11; P4-A11 |
| E20 | Save an editable project, plan a portable raw package and export a final video. | P5 | 47, 48, 49, 50 | P5-M05; P5-A06 |

## Video recorder — 20 points

| ID | Requirement | Primary phase | UI screens | Acceptance pointers |
|---|---|---|---|---|
| R01 | Record one selected monitor. | P2 | 06, 07 | P2-M01; P2-A04 |
| R02 | Combine multiple monitors without stretching their layouts. | P2 | 08 | P2-M04; P2-A02 |
| R03 | Choose an application window as the capture source. | P2 | 07 | P2-M02; P2-A04 |
| R04 | Select and resize a custom recording region. | P2 | 09 | P2-M03; P2-A02 |
| R05 | Configure resolution, frame rate and bitrate. | P2 | 10 | P2-M13; P2-A03 |
| R06 | Select encoder preferences and reusable capture presets. | P2 | 10, 23 | P2-M13; P2-A03 |
| R07 | Capture microphone audio independently. | P2 | 12 | P2-M05; P2-A05 |
| R08 | Capture PC/system audio independently. | P2 | 11 | P2-M05; P2-A05 |
| R09 | Capture a webcam with configurable framing and mirroring. | P2 | 13 | P2-M08; P2-A12 |
| R10 | Keep the screen video clean; preserve other sources separately. | P2 | 22, 26 | P2-M01; P2-A04 |
| R11 | Configure cursor size, color, visibility and highlight. | P2 | 14 | P4-M09; P4-A09 |
| R12 | Configure left/right clicks, ripples, drag and scroll effects. | P2 | 15 | P4-M09; P4-A09 |
| R13 | Capture display-safe keyboard shortcuts as timed events. | P2 | 16 | P2-M11; P2-A10 |
| R14 | Design keyboard badges, placement, size and animation. | P2 | 17 | P4-M10; P4-A10 |
| R15 | Provide privacy controls and an immediate keyboard-capture stop. | P2 | 18 | P2-M11; P2-A10 |
| R16 | Set a countdown, capture outline and compact control bar. | P2 | 19 | P2-M12; P2-A01 |
| R17 | Configure start, pause, microphone and marker shortcuts. | P2 | 20 | P2-M12; P2-A15 |
| R18 | Pause, resume, mark moments and stop a take. | P2 | 25 | P2-M09; P2-A11 |
| R19 | Track per-frame timestamps, pointer state, events and audio references in JSON/JSONL. | P2 | 50 | P2-M10; P2-A07 |
| R20 | Edit captured effects later; label uncaptured tracks and intervals as unavailable. | P2 | 26, 41, 42, 43, 50 | P2-M07; P2-A06 |

## Other approved screen coverage

These are retained, not added as a replacement for any of the forty requirements.

| ID | Capability | Primary phase | Acceptance pointers |
|---|---|---|---|
| X01 | Playback speed and synchronized event timing | P3 | P3-M10; P3-A10 |
| X02 | Brightness, contrast and saturation | P3 | P3-M11; P3-A11 |
| X03 | Canvas, background, padding and border | P3 | P3-M11; P3-A11 |
| X04 | Versioned save, autosave, recovery and source protection | P5 | P5-M09; P5-A09 |
| X05 | Dark/light/custom themes and accessible adaptive native UI | P1 | P1-M05; P1-A08 |
| X06 | Review catalog, per-screen feedback and evidence-based approval | P1 | P1-M15; P1-A15 |
| X07 | Safe diagnostics, capability reporting and storage cleanup | P5 | P5-M10; P5-A10 |

Acceptance pointers are entry cases, not the entire required matrix. In particular E18 also requires P4-M10/P4-A10 for keyboard effects; R20 also requires P4-M11 and P5-M06 for editing/redacted package behavior. Every specified case remains required in its applicable supported environment.
