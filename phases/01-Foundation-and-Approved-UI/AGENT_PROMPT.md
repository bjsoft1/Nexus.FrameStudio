# Execute Phase 1 only — Foundation & approved UI

Read the package's `01_MASTER_AGENT_PROMPT.md`, architecture, capture data contract, testing guide and source reuse review. Then read every file in this phase folder and the relevant approved prototype screens.

**Entry condition:** The owner has approved the prototype design. No earlier implementation phase is required.

**Implement:** Create the new solution, reusable native UI, all 54 visual states, themes, project/session contracts, safe save/load and the test harness.

**Do not expand into:** Real recording, full video playback/editing, media encoding and raw-media packaging remain disabled and clearly labeled until their owning phase.

Complete tasks P1-T01 through P1-T20 in dependency-safe order. Create/run automated tests P1-A01 through P1-A15 and follow manual cases P1-M01 through P1-M15. Use the exact IDs for traceability and the underscore method naming contract for test filtering. Run earlier required regressions. Do not claim a test ran when its implementation, environment or device is absent.

Preserve the approved UI and independent-source/non-destructive contract. Leave the original ProductivityCare app/source untouched. Unsupported/future work must not look operational through a fake success path. Make meaningful incremental changes and keep the new solution buildable.

**Required result:** A separate native Windows app matching the approved design, with safe project persistence and a repeatable build/test entry point.

**Exit gate:** Demonstrate all 54 native UI states, reopen a saved project, prove invalid files cannot replace active work, and provide a clean build plus P1 test evidence.

Fill this folder's handoff with actual commands, build/test outcomes, evidence, defects and exact remaining task/case IDs. Provide a runnable UI test path and actual output samples where applicable. Stop for owner review. Do not mark your own phase approved or continue to the next phase automatically.
