# Nexus.FrameStudio agent instructions

## Working branch

The owner requested on 2026-09-11 that all subsequent development use the existing `gpt6` branch only.

- Read the remote branch and current repository state before making changes.
- Commit this project's implementation, tests, fixes and handoffs directly to `gpt6`.
- Do not create additional feature, implementation, codex, phase or task branches unless the owner explicitly requests one.
- Do not push implementation directly to `master`, change the default branch, force-push, delete branches or merge to `master` without explicit authorization.
- Before recommending a merge, inspect the actual diff and required test evidence. Branch names are not evidence of completed functionality.

## Branch consolidation baseline

`gpt6` was created from commit `d2d7cdf9256ce746cd3114c1c432e304f1707113`, the head of `codex/framestudio-phases-1-2-source` at the time of inspection.

At that inspection:

- `master`, `feature/framestudio-phases-1-2`, and `implementation/phases-1-2` all pointed to `0b068e3e88436b46244cd4f8e27a8c62cf4b8ee7`.
- The codex branch added only `.github/workflows/framestudio-toolchain.yml` in one commit above `master`.
- There was no unique implementation on the feature or implementation branches to merge.
- The inherited content is the approved plan/prototype and toolchain setup, not a completed native Phase 1 or Phase 2 application.

The old branches remain untouched. No merge of those branches is required to begin work on `gpt6`. These are historical observations; recheck the remote before any later merge or cleanup.

## Implementation scope and quality

Read `00_START_HERE.md`, `01_MASTER_AGENT_PROMPT.md`, `docs/ARCHITECTURE.md`, `docs/CAPTURE_DATA_CONTRACT.md` and the selected phase's tasks/tests before implementation. Preserve the approved native UI direction and phase approval gates.

Build the separate Nexus.FrameStudio project. Do not import unrelated ProductivityCare functionality. Preserve clean screen video, separate webcam/microphone/system audio and timestamped interaction metadata. Capture-off is different from editor mute; uncaptured data cannot be recovered. Keyboard capture must remain opt-in, visible, recording-only and privacy-safe.

Report build, automated-test and Windows device/UI results separately. Never label a plan, prototype, dependency-restore workflow or documentation commit as a completed native application. Mark unexecuted tests NOT_RUN and list remaining implementation and validation work explicitly.
