# Planning-package validation

**These are package/review-page checks only. Native implementation is NOT_STARTED; all 150 native test specifications are NOT_RUN.**

## Results

| Check group | Result | Scope |
|---|---|---|
| Structural and file-integrity validator | 56 passed; 0 failed | Phase/task/test IDs, coverage, required files, relative links, SHA-256 manifest and unchanged prototype reference. |
| Review-page browser checks | 85 passed; 0 failed | In-memory Chromium rendering/navigation, task/test panels, search, draft-state adapter, exported notes and layout at 1920×1080 / 1366×768. |
| Native build/device/encoding/recovery/installer tests | NOT_RUN | The new native application and automated test bodies must be implemented in the five phases. |

## Browser test limits

This environment blocked both file:// and localhost browser navigation. Browser checks therefore used an in-memory document with inlined local CSS/JS/image resources and a controlled storage adapter. Real file/HTTP navigation, native browser persistence and the Windows `.cmd` launcher were not validated here. Reference links were validated structurally. No browser policy was changed or disabled.

The reviewer is designed to open from `index.html` after extraction. The Markdown plan remains usable independently. Use the HTML page on your Windows machine to verify real local navigation and note persistence. Export draft notes before closing.

## Reproduce the available checks

```text
python tools/validate_plan.py
```

The optional `tools/check_review_board.py` requires Python, Playwright and an installed supported Chromium browser (or Playwright browser installation). It performs browser-memory checks and writes evidence to a new temporary directory. It is not a native Windows app test runner.

Native commands and fixture requirements are specified in `docs/TESTING_GUIDE.md` and implemented during development.

## Detailed structural checks

| Check | Result |
|---|---|
| Exactly five sequential phases | PASS |
| Native implementation and tests are unrun | PASS |
| P1: 20 task specifications | PASS |
| P1: 15 manual and 15 automated specifications | PASS |
| P1: task done criteria and initial state | PASS |
| P1: complete manual setup, steps, expectations and evidence paths | PASS |
| P1: complete automated scenarios, assertions and future commands | PASS |
| P1: scope, exclusions and approval gate | PASS |
| P1: all five phase handoff files exist | PASS |
| P1: test IDs are present in the corresponding documents | PASS |
| P2: 20 task specifications | PASS |
| P2: 15 manual and 15 automated specifications | PASS |
| P2: task done criteria and initial state | PASS |
| P2: complete manual setup, steps, expectations and evidence paths | PASS |
| P2: complete automated scenarios, assertions and future commands | PASS |
| P2: scope, exclusions and approval gate | PASS |
| P2: all five phase handoff files exist | PASS |
| P2: test IDs are present in the corresponding documents | PASS |
| P3: 20 task specifications | PASS |
| P3: 15 manual and 15 automated specifications | PASS |
| P3: task done criteria and initial state | PASS |
| P3: complete manual setup, steps, expectations and evidence paths | PASS |
| P3: complete automated scenarios, assertions and future commands | PASS |
| P3: scope, exclusions and approval gate | PASS |
| P3: all five phase handoff files exist | PASS |
| P3: test IDs are present in the corresponding documents | PASS |
| P4: 20 task specifications | PASS |
| P4: 15 manual and 15 automated specifications | PASS |
| P4: task done criteria and initial state | PASS |
| P4: complete manual setup, steps, expectations and evidence paths | PASS |
| P4: complete automated scenarios, assertions and future commands | PASS |
| P4: scope, exclusions and approval gate | PASS |
| P4: all five phase handoff files exist | PASS |
| P4: test IDs are present in the corresponding documents | PASS |
| P5: 20 task specifications | PASS |
| P5: 15 manual and 15 automated specifications | PASS |
| P5: task done criteria and initial state | PASS |
| P5: complete manual setup, steps, expectations and evidence paths | PASS |
| P5: complete automated scenarios, assertions and future commands | PASS |
| P5: scope, exclusions and approval gate | PASS |
| P5: all five phase handoff files exist | PASS |
| P5: test IDs are present in the corresponding documents | PASS |
| 100 unique task IDs and 150 unique test IDs | PASS |
| All 20 editor and 20 recorder requirements retained | PASS |
| Seven additional approved-screen capabilities retained | PASS |
| Every requirement maps to real acceptance IDs | PASS |
| All 54 unique approved screens retained | PASS |
| Every screen has visual and functional ownership | PASS |
| All approved screen links resolve | PASS |
| No phase or release self-approval | PASS |
| Core reviewer and engineering files exist | PASS |
| Planning Markdown local links resolve safely | PASS |
| Package manifest file sizes and SHA-256 hashes match | PASS |
| Package manifest covers all delivery files | PASS |
| Approved prototype reference is unchanged | PASS |
| Review export does not grant native completion or approval | PASS |

## Detailed review-page checks

| Check | Result |
|---|---|
| Reviewer opens in browser-memory mode | PASS |
| Overview has five phase cards | PASS |
| Overview reports 100 tasks and 150 specifications | PASS |
| P1 task checklist at 1920×1080 | PASS |
| P1 manual cases at 1920×1080 | PASS |
| P1 manual case expands at 1920×1080 | PASS |
| P1 auto cases at 1920×1080 | PASS |
| P1 auto case expands at 1920×1080 | PASS |
| P1 handoff notes available at 1920×1080 | PASS |
| P1 no horizontal overflow at 1920×1080 | PASS |
| P2 task checklist at 1920×1080 | PASS |
| P2 manual cases at 1920×1080 | PASS |
| P2 manual case expands at 1920×1080 | PASS |
| P2 auto cases at 1920×1080 | PASS |
| P2 auto case expands at 1920×1080 | PASS |
| P2 handoff notes available at 1920×1080 | PASS |
| P2 no horizontal overflow at 1920×1080 | PASS |
| P3 task checklist at 1920×1080 | PASS |
| P3 manual cases at 1920×1080 | PASS |
| P3 manual case expands at 1920×1080 | PASS |
| P3 auto cases at 1920×1080 | PASS |
| P3 auto case expands at 1920×1080 | PASS |
| P3 handoff notes available at 1920×1080 | PASS |
| P3 no horizontal overflow at 1920×1080 | PASS |
| P4 task checklist at 1920×1080 | PASS |
| P4 manual cases at 1920×1080 | PASS |
| P4 manual case expands at 1920×1080 | PASS |
| P4 auto cases at 1920×1080 | PASS |
| P4 auto case expands at 1920×1080 | PASS |
| P4 handoff notes available at 1920×1080 | PASS |
| P4 no horizontal overflow at 1920×1080 | PASS |
| P5 task checklist at 1920×1080 | PASS |
| P5 manual cases at 1920×1080 | PASS |
| P5 manual case expands at 1920×1080 | PASS |
| P5 auto cases at 1920×1080 | PASS |
| P5 auto case expands at 1920×1080 | PASS |
| P5 handoff notes available at 1920×1080 | PASS |
| P5 no horizontal overflow at 1920×1080 | PASS |
| P1 task checklist at 1366×768 | PASS |
| P1 manual cases at 1366×768 | PASS |
| P1 manual case expands at 1366×768 | PASS |
| P1 auto cases at 1366×768 | PASS |
| P1 auto case expands at 1366×768 | PASS |
| P1 handoff notes available at 1366×768 | PASS |
| P1 no horizontal overflow at 1366×768 | PASS |
| P2 task checklist at 1366×768 | PASS |
| P2 manual cases at 1366×768 | PASS |
| P2 manual case expands at 1366×768 | PASS |
| P2 auto cases at 1366×768 | PASS |
| P2 auto case expands at 1366×768 | PASS |
| P2 handoff notes available at 1366×768 | PASS |
| P2 no horizontal overflow at 1366×768 | PASS |
| P3 task checklist at 1366×768 | PASS |
| P3 manual cases at 1366×768 | PASS |
| P3 manual case expands at 1366×768 | PASS |
| P3 auto cases at 1366×768 | PASS |
| P3 auto case expands at 1366×768 | PASS |
| P3 handoff notes available at 1366×768 | PASS |
| P3 no horizontal overflow at 1366×768 | PASS |
| P4 task checklist at 1366×768 | PASS |
| P4 manual cases at 1366×768 | PASS |
| P4 manual case expands at 1366×768 | PASS |
| P4 auto cases at 1366×768 | PASS |
| P4 auto case expands at 1366×768 | PASS |
| P4 handoff notes available at 1366×768 | PASS |
| P4 no horizontal overflow at 1366×768 | PASS |
| P5 task checklist at 1366×768 | PASS |
| P5 manual cases at 1366×768 | PASS |
| P5 manual case expands at 1366×768 | PASS |
| P5 auto cases at 1366×768 | PASS |
| P5 auto case expands at 1366×768 | PASS |
| P5 handoff notes available at 1366×768 | PASS |
| P5 no horizontal overflow at 1366×768 | PASS |
| Task search returns exact matching task | PASS |
| Draft notes restore through controlled storage and remain escaped | PASS |
| Light theme switches | PASS |
| Theme preference restores through controlled storage | PASS |
| Review notes export as real JSON | PASS |
| Review export never grants completion or approval | PASS |
| All feature traceability rows displayed | PASS |
| Feature search filters correctly | PASS |
| All 54 approved screen links displayed | PASS |
| Editor reference link targets the approved file | PASS |
| No unhandled reviewer JavaScript exceptions | PASS |
| In-memory reviewer makes no external web requests | PASS |
