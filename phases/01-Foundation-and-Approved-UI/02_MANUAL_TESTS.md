# Phase 1 — Foundation & approved UI — manual UI tests

**All cases: NOT_RUN. Run against the native phase build, not the HTML prototype.**

Read `../../docs/TESTING_GUIDE.md` for fixture setup, evidence and numeric targets. Screen numbers refer to the approved prototype/native equivalent. Test only disposable controlled data.

## P1-M01 — Clean standalone launch

**Prerequisites:** F00; clean Windows test profile

1. Run tools/Build.ps1 then tools/Run.ps1 from the new repository.
2. Open Studio home (01) and inspect the app title and storage folder.

**Expected:** Nexus.FrameStudio opens with no ProductivityCare dependency; old-app files/settings are unchanged.
**Evidence:** `artifacts/acceptance/P1/P1-M01/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M02 — Approved screen coverage

**Prerequisites:** F00; 1920×1080 at 100 percent

1. Open QA > All screens (53).
2. Visit screen numbers 01 through 54 and compare with the bundled prototype.

**Expected:** Every state is reachable; approved navigation/density is retained; unfinished actions are disabled with a reason.
**Evidence:** `artifacts/acceptance/P1/P1-M02/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M03 — Dark and light themes

**Prerequisites:** F00

1. Open Appearance & preferences (52).
2. Switch Dark to Light and back.
3. Restart the app.

**Expected:** The selected theme persists; text, inputs, dialogs and timeline remain legible.
**Evidence:** `artifacts/acceptance/P1/P1-M03/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M04 — Custom theme validation

**Prerequisites:** F00; valid and invalid theme JSON fixtures

1. In screen 52 import a valid custom theme.
2. Import a theme with an invalid color and an unexpected executable/markup field.
3. Reset theme.

**Expected:** Valid data applies; invalid content is rejected without executing code or losing the prior theme.
**Evidence:** `artifacts/acceptance/P1/P1-M04/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M05 — Small screen and DPI

**Prerequisites:** F00; 1366×768 plus 125/150/200 percent DPI

1. Open Capture (06) and Editor (27).
2. Resize the window and change test display scaling.
3. Reach Save and primary actions by keyboard.

**Expected:** Layout adapts; critical actions remain reachable; controls do not overlap or disappear behind fixed panels.
**Evidence:** `artifacts/acceptance/P1/P1-M05/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M06 — Keyboard and focus

**Prerequisites:** F00

1. Navigate home, New project (03) and Settings (52) using Tab/Shift+Tab.
2. Open and close a dialog with Enter/Escape.

**Expected:** Focus is visible, follows a logical order and returns to the invoking control.
**Evidence:** `artifacts/acceptance/P1/P1-M06/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M07 — Create project

**Prerequisites:** F00

1. Open New project (03).
2. Enter Demo One and choose 1920×1080.
3. Create, then reopen from Project library (02).

**Expected:** A unique workspace and stable project ID exist; canvas and name persist.
**Evidence:** `artifacts/acceptance/P1/P1-M07/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M08 — Invalid new-project values

**Prerequisites:** F00

1. In screen 03 submit a blank name, invalid size and an already-used workspace path.
2. Cancel any overwrite prompt.

**Expected:** Errors identify the invalid field; no existing project is replaced.
**Evidence:** `artifacts/acceptance/P1/P1-M08/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M09 — Save and reopen

**Prerequisites:** F00; a created project

1. Change project name/canvas in supported P1 controls.
2. Save editable project (47).
3. Close and reopen the saved .nfsproject.

**Expected:** The same valid state returns; temporary files are not mistaken for projects.
**Evidence:** `artifacts/acceptance/P1/P1-M09/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M10 — Reject malformed or future projects

**Prerequisites:** F06; an open unsaved project

1. Use Import/Open (04) on malformed JSON, wrong-kind JSON and a newer schema.
2. Return to the current workspace.

**Expected:** Clear errors appear; current edits and the last good save/backup remain intact.
**Evidence:** `artifacts/acceptance/P1/P1-M10/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M11 — Unsaved changes protection

**Prerequisites:** F00; an edited project

1. Close the project.
2. Choose Cancel, then Save on a second attempt.
3. Repeat using Discard on a separate test copy.

**Expected:** Cancel preserves edits; Save persists them; Discard changes only unsaved state.
**Evidence:** `artifacts/acceptance/P1/P1-M11/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M12 — Library and app isolation

**Prerequisites:** F00; original app installed or sample old-data folder

1. Create and save a new project.
2. Compare old-app file hashes and settings before/after.
3. Open Project library (02).

**Expected:** Only the new library changes; unrelated app data is untouched.
**Evidence:** `artifacts/acceptance/P1/P1-M12/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M13 — Explicit design mode

**Prerequisites:** F00

1. Open capture-related screens in normal launch.
2. Launch the documented QA design mode and repeat.

**Expected:** Normal mode never presents fake device capture as real; QA samples are visibly marked.
**Evidence:** `artifacts/acceptance/P1/P1-M13/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M14 — Safe diagnostics

**Prerequisites:** F00; controlled invalid-file failure

1. Trigger an invalid import.
2. Open diagnostics in Settings (52).
3. Export the report after consent.

**Expected:** The report names the failed operation but contains no typed text, media bytes or private full paths.
**Evidence:** `artifacts/acceptance/P1/P1-M14/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P1-M15 — Phase completion report

**Prerequisites:** P1 evidence folder

1. Open Review & approval (54).
2. Record actual P1 test outcomes and remaining work.
3. Export the phase report.

**Expected:** Report distinguishes PASS/FAIL/NOT_RUN/BLOCKED and includes evidence; it does not self-approve P2.
**Evidence:** `artifacts/acceptance/P1/P1-M15/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.
