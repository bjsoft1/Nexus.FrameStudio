# Nexus.FrameStudio — five-phase development package

The prototype design is approved. This package is the **implementation plan**, not the completed C# application.

Open `index.html` for the searchable offline review board, or read the Markdown files. `OPEN_PLAN.cmd` opens the review board on Windows. The approved 54-screen prototype is included unchanged under `reference/approved-prototype/`.

## The five phases

| Phase | Result |
|---|---|
| 1 — Foundation & approved UI | Separate .NET/WPF solution, reusable UI, all 54 visual states, theme support, safe project save/load and test harness. |
| 2 — Independent-track recorder | Actual screen MP4 plus separate camera, system audio, mic and frame-linked input metadata. |
| 3 — Core video editor | Import, trim, split, join, reorder, crop, resize, speed/color/canvas, save/reopen and a basic real MP4 render. |
| 4 — Overlays, effects & audio | Text, rich text, shapes, images/video overlays, animation, transitions, captions, editable input effects and independent audio. |
| 5 — Export, raw packages & release | Complete output queue, portable .nfsraw, privacy-safe copies, recovery, security/performance checks and Windows release candidate. |

Each phase contains **20 implementation tasks, 15 manual test cases and 15 automated test specifications**. Total: **100 tasks and 150 test specifications**. Every native implementation task is initially NOT_STARTED and every native test is NOT_RUN.

## Start development with your AI agent

1. Put this extracted plan beside the new `Nexus.FrameStudio` repository, not over your existing app.
2. Give the agent `01_MASTER_AGENT_PROMPT.md` and `phases/01-Foundation-and-Approved-UI/AGENT_PROMPT.md`.
3. The agent implements only the selected phase, runs its tests plus earlier regressions, and fills that phase's handoff report.
4. Review the working UI, output files, test evidence and remaining work. Approve explicitly before the next phase starts.

Phase 1 must create the actual solution and build/run/native-test commands. Commands documented under automated tests are future execution contracts, not commands that can build an app from this planning ZIP.

## Important recording rule

Clean video, webcam, mic and PC audio remain independent. Mouse/keyboard information stays in timestamped metadata. Hiding or muting something is not the same as never capturing it. An uncaptured or deliberately redacted interval cannot be recovered by changing a switch.

A full editable raw package can still contain muted audio or hidden keyboard events. The plan therefore includes an explicit privacy warning and a separate sanitized-copy workflow.

## Included references and status

`docs/FEATURES_20_PLUS_20.md` preserves your review summary and adds phase/test ownership. `docs/SCREEN_PHASE_MAP.md` maps all 54 states. `docs/TESTING_GUIDE.md` explains setup, commands, evidence and pass criteria. `PACKAGE_VALIDATION.md` reports checks on this planning package only.

The earlier prototype's reported browser checks are historical UI evidence, not evidence that native recording/encoding works. They are kept only in the unmodified reference folder. This delivery does not claim a native build, Windows-device test, MP4 render or installer test has passed.
