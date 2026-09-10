# Execute Phase 5 only — Export, raw packages & release

Read the package's `01_MASTER_AGENT_PROMPT.md`, architecture, capture data contract, testing guide and source reuse review. Then read every file in this phase folder and the relevant approved prototype screens.

**Entry condition:** Phase 4 must have a clean build, required regression evidence and explicit owner approval. Read its actual handoff before changing code.

**Implement:** Finish export presets/queue, raw archive round trips, privacy-safe sharing, recovery, capability reporting, performance checks and Windows release packaging.

**Do not expand into:** Store submission/signing without credentials, cloud services, macOS/Linux, ARM64 and unverified HDR/codec promises are not included. Any missed approved requirement remains a blocker, not an automatic deferral.

Complete tasks P5-T01 through P5-T20 in dependency-safe order. Create/run automated tests P5-A01 through P5-A15 and follow manual cases P5-M01 through P5-M15. Use the exact IDs for traceability and the underscore method naming contract for test filtering. Run earlier required regressions. Do not claim a test ran when its implementation, environment or device is absent.

Preserve the approved UI and independent-source/non-destructive contract. Leave the original ProductivityCare app/source untouched. Unsupported/future work must not look operational through a fake success path. Make meaningful incremental changes and keep the new solution buildable.

**Required result:** A tested desktop release candidate with real video export, portable editable sessions, recovery, documentation and install/uninstall validation.

**Exit gate:** Pass all cumulative required tests, export and reopen on a second machine, verify interruption/recovery and source safety, and obtain explicit owner release approval.

Fill this folder's handoff with actual commands, build/test outcomes, evidence, defects and exact remaining task/case IDs. Provide a runnable UI test path and actual output samples where applicable. Stop for owner review. Do not mark your own phase approved or continue to the next phase automatically.
