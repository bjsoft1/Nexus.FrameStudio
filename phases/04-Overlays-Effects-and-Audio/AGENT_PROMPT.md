# Execute Phase 4 only — Overlays, effects & audio

Read the package's `01_MASTER_AGENT_PROMPT.md`, architecture, capture data contract, testing guide and source reuse review. Then read every file in this phase folder and the relevant approved prototype screens.

**Entry condition:** Phase 3 must have a clean build, required regression evidence and explicit owner approval. Read its actual handoff before changing code.

**Implement:** Implement overlay tools, transform keyframes, transitions, captions, pointer/keyboard styling and independent audio mixing with shared preview/export evaluation.

**Do not expand into:** AI transcription, generative effects, advanced color grading, arbitrary codecs and destructive removal of already-baked pixels are outside the approved basic editor.

Complete tasks P4-T01 through P4-T20 in dependency-safe order. Create/run automated tests P4-A01 through P4-A15 and follow manual cases P4-M01 through P4-M15. Use the exact IDs for traceability and the underscore method naming contract for test filtering. Run earlier required regressions. Do not claim a test ran when its implementation, environment or device is absent.

Preserve the approved UI and independent-source/non-destructive contract. Leave the original ProductivityCare app/source untouched. Unsupported/future work must not look operational through a fake success path. Make meaningful incremental changes and keep the new solution buildable.

**Required result:** A layered editor with formatted text, shapes, image/video overlays, animation, subtitles and editable captured interactions/audio.

**Exit gate:** Render a composed clip with formatted text, shapes, image/video overlays, animation and independent audio; compare it with preview and prove hidden events can be restored only where captured.

Fill this folder's handoff with actual commands, build/test outcomes, evidence, defects and exact remaining task/case IDs. Provide a runnable UI test path and actual output samples where applicable. Stop for owner review. Do not mark your own phase approved or continue to the next phase automatically.
