# Master development prompt — Nexus.FrameStudio

You are implementing **a new standalone Windows video recorder and basic video editor** from the approved FrameStudio design. The owner approved the prototype, not an arbitrary UI redesign or an automatic five-phase implementation run.

## Required reading

Read `00_START_HERE.md`, `docs/ARCHITECTURE.md`, `docs/CAPTURE_DATA_CONTRACT.md`, `docs/SOURCE_REUSE_REVIEW.md`, `docs/TESTING_GUIDE.md`, `docs/SCREEN_PHASE_MAP.md`, and the selected phase's implementation/tests/handoff/prompt. Compare relevant screens in `reference/approved-prototype/`. Treat `data/plan.json` as the task/test ID catalog.

## Scope and workflow

Implement only the selected phase. Create a new `Nexus.FrameStudio` solution and storage identity. The original `Nexus.ProductivityCare(1).zip` and existing app remain read-only references. Review/copy only recorder/editor components and truly required direct dependencies; do not import sign-in, wellness, reminders, screenshots, color picker, 3D viewer or unrelated features.

Keep the approved 1080p Windows-style design, compact reusable components and beginner-friendly navigation. Translate it into native controls; do not deliver the HTML prototype wrapped in a window and call it a native media editor. Fifty-four reference states do not require fifty-four independent top-level windows. Future-phase controls must be explicitly disabled, not wired to fabricated device/render success.

Use the proposed .NET 10/WPF architecture unless Phase 1 evidence demonstrates a reason to change it. Document any change with affected scope/tests and obtain owner approval. Pin exact tested dependencies. Preserve vendor notices for any reused code. Do not modify, delete or publish anything outside the authorized new project.

## Non-negotiable invariants

Clean screen media has no app-added cursor, clicks, keys, text, borders, webcam or other mutable effects baked into it. Store webcam, microphone and PC audio independently. Metadata stores timing/events/references, not audio sample arrays. Every finalized screen frame resolves its actual timestamps, pointer state, event IDs and source availability. Keep multiple sub-frame input events. Never infer real timing only from frame index divided by nominal FPS.

Separate source/session time, edited timeline time, encoded PTS, physical pixels and UI DIP coordinates. Use explicit transforms and time mappings through crop, multiple monitors, trims, reorder, duplicates, speed and transitions. Capture OFF/denied/suppressed/lost/redacted is not editor mute/visibility. Do not fabricate original keys/audio/camera for missing intervals. Manually authored content must retain authored provenance.

Keyboard collection is explicit, visible and recording-only, with a conservative safe-shortcut allowlist, secure/uncertain-input suppression and immediate stop. Never persist typed text, passwords or clipboard content. Do not bypass OS capture restrictions. A UI exclusion cannot guarantee arbitrary sensitive pixels are removed from every capture source; communicate actual support.

Treat capture files as immutable during normal editing/export. Use versioned safe loading, owned relative paths, bounded archive extraction, staging, checksums and prior-good backups. Refuse unsafe output targets. Promote completed output only after actual media verification. Keep unavailable or corrupt data visible as a failure, not an empty success.

## Test and completion discipline

Create real native test implementations for the selected phase's automated case IDs. `NOT_RUN` is never PASS. Device-less or non-Windows environments may run appropriate model tests but cannot establish native capture/UI/installer success. Use deterministic controlled fixtures; request device consent where needed. Never use private user media for automated capture. Record commands, commit, toolchain, machine profile, durations, actual outcomes and evidence paths.

Run clean build, current tests and all previous-phase required regressions. The phase test wrapper must fail on zero discovered tests and validate required case coverage. Missing prerequisites become BLOCKED/NOT_RUN with a reason. Do not delete failing tests or turn failed assertions into skips to claim success.

At completion, fill `04_HANDOFF_AND_REMAINING.md` and export the result template. Report what works, what was actually tested, failures, risks, exact remaining work and a runnable UI review path. Attach screenshots, TRX/logs and relevant actual media/metadata samples. Never assert “no bugs” or “no data loss” without the specified evidence; report recovery limits honestly.

Stop at the phase gate. Only the owner/reviewer can approve the next phase or release. Multiple tests/tasks inside the approved phase may run together; phase gates may not be bypassed. Do not claim asynchronous/background continuation.
