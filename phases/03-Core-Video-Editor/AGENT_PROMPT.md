# Execute Phase 3 only — Core video editor

Read the package's `01_MASTER_AGENT_PROMPT.md`, architecture, capture data contract, testing guide and source reuse review. Then read every file in this phase folder and the relevant approved prototype screens.

**Entry condition:** Phase 2 must have a clean build, required regression evidence and explicit owner approval. Read its actual handoff before changing code.

**Implement:** Implement multi-source timeline editing, synchronized playback, media relinking, undo/redo, safe saves, speed/color/canvas controls and a basic actual MP4 render path.

**Do not expand into:** Rich overlays, transitions, detailed input styling and the full audio mixer arrive in P4. Full render queue, portable raw archive and release packaging arrive in P5.

Complete tasks P3-T01 through P3-T20 in dependency-safe order. Create/run automated tests P3-A01 through P3-A15 and follow manual cases P3-M01 through P3-M15. Use the exact IDs for traceability and the underscore method naming contract for test filtering. Run earlier required regressions. Do not claim a test ran when its implementation, environment or device is absent.

Preserve the approved UI and independent-source/non-destructive contract. Leave the original ProductivityCare app/source untouched. Unsupported/future work must not look operational through a fake success path. Make meaningful incremental changes and keep the new solution buildable.

**Required result:** A usable non-destructive editor for importing, trimming, splitting, joining, cropping, resizing and basic timing/color changes.

**Exit gate:** Join two real clips, remove a middle section, crop/resize, save/reopen, and render a playable MP4 whose timing and source hashes are verified.

Fill this folder's handoff with actual commands, build/test outcomes, evidence, defects and exact remaining task/case IDs. Provide a runnable UI test path and actual output samples where applicable. Stop for owner review. Do not mark your own phase approved or continue to the next phase automatically.
