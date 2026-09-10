# Phase 1 — Foundation & approved UI

**Status: NOT_STARTED. This is a development specification, not a completion report.**

## Deliverable

A separate native Windows app matching the approved design, with safe project persistence and a repeatable build/test entry point.
## Prerequisite

The owner has approved the prototype design. No earlier implementation phase is required.
## In scope

Create the new solution, reusable native UI, all 54 visual states, themes, project/session contracts, safe save/load and the test harness.
## Not in this phase

Real recording, full video playback/editing, media encoding and raw-media packaging remain disabled and clearly labeled until their owning phase.
## Twenty implementation tasks

| ID | Task | Implementation | Done when |
|---|---|---|---|
| P1-T01 | Create the standalone solution | Create Nexus.FrameStudio.sln with App, Core, Media.Windows, Storage and test projects; keep the original ZIP/repo read-only. | A clean checkout builds without a dependency on ProductivityCare. |
| P1-T02 | Pin the toolchain and packages | Use .NET 10, C# and WPF; pin the tested SDK and package versions and commit dependency lock files. | Build prerequisites and exact tested versions are recorded; no floating dependencies. |
| P1-T03 | Audit recorder/editor reuse | Review only recorder/editor models, services, windows and their direct dependencies; record every copied or rewritten component. | No wellness, screenshots, 3D, sign-in or unrelated app code is imported. |
| P1-T04 | Create service boundaries | Separate capture, clock, media probing, timeline, composition, storage and capability interfaces from view models. | Fake adapters can run UI tests without activating a camera, microphone or screen capture. |
| P1-T05 | Define versioned contracts | Define distinct production project/session/package kinds with stable IDs, rational timing and immutable capture versus mutable edits. | Unknown formats are rejected; prototype JSON is not silently treated as a native project. |
| P1-T06 | Create the native app shell | Implement Projects, Capture, Edit and Settings navigation using the approved layout and spacing. | Home and workspace switching match reference screenshots at 1920×1080. |
| P1-T07 | Map all 54 UI states | Implement each approved screen as a view/panel/state; keep the page map and review screen in the QA surface. | No approved screen disappears; future functionality is visibly disabled, not simulated as real. |
| P1-T08 | Build reusable controls | Create themed buttons, toggles, numeric fields, track headers, panels, dialogs and empty/error/loading states. | Shared controls have validation, focus states and stable AutomationIds. |
| P1-T09 | Implement theme JSON | Load a validated data-only theme schema into shared resources; provide dark/light and custom theme import/reset. | Invalid theme values show an error and leave the current usable theme unchanged. |
| P1-T10 | Support layout and accessibility | Preserve native resize/snap, keyboard focus, accessible names and 100/125/150/200 percent DPI layouts. | At 1366×768 or higher, critical actions remain reachable without shrinking all text. |
| P1-T11 | Isolate app storage | Create owned settings, library and workspace locations under the new identity with no old-app migrations by default. | Launch/save never change ProductivityCare settings or recordings. |
| P1-T12 | Implement project creation | Create a named workspace with validated canvas and IDs; display it in the library. | Blank names, duplicate paths and invalid sizes cannot silently overwrite another project. |
| P1-T13 | Implement safe project save/load | Save a versioned .nfsproject using validation, same-directory temporary replacement and a prior-good backup. | Malformed/future/wrong-kind files do not replace the open project or its backup. |
| P1-T14 | Add media and session view models | Model sources, clips, track availability and owned relative paths; populate design adapters only in explicit QA mode. | Capture availability and presentation mute/visibility are separate properties. |
| P1-T15 | Build undo and dirty-state services | Provide command history infrastructure, unsaved-change prompts and cancellation-safe navigation. | Cancel leaves work open; save and discard have different explicit effects. |
| P1-T16 | Add logging and diagnostics | Record structured failures, operation IDs and capability summaries while excluding typed input and private media data. | The user can export a redacted diagnostic report with a clear consent action. |
| P1-T17 | Validate media/renderer feasibility | Run a small native decode plus two-layer composition spike; select a shared renderer behind an interface. | Save real output-frame evidence and record supported baseline codecs; do not claim full recording. |
| P1-T18 | Create test fixtures and harness | Implement deterministic fixture generation, fake clocks/devices and Windows UI Automation helpers. | Fixture hashes and metadata are reproducible; UI tests never depend on private user files. |
| P1-T19 | Create build/run/test commands | Implement documented PowerShell entry points, clean restore/build and phase-filtered test runs that reject zero executed tests. | Build and Run work from a path containing spaces; unavailable prerequisites fail clearly. |
| P1-T20 | Complete the phase handoff | Run P1 checks, attach screenshots/logs and list defects, untouched sources and remaining P2–P5 scope. | The owner receives an evidence-based report; P2 does not start before approval. |

## Approved UI references

01 Studio home, 02 Project library, 03 New project, 52 Appearance & preferences, 53 All 54 screens, 54 Review & approval.
P1 owns visual coverage of every screen. The above list identifies primary functional completion; shared screens are progressively integrated. See the complete screen-phase map.

## Required evidence and gate

Demonstrate all 54 native UI states, reopen a saved project, prove invalid files cannot replace active work, and provide a clean build plus P1 test evidence.

Run the 15 manual cases and implement/run the 15 automated cases in this folder, plus previous required regressions. Save actual outputs and hashes for media/storage tests. All current required cases must be PASS with evidence; BLOCKED/NOT_RUN is not approval.

Complete `04_HANDOFF_AND_REMAINING.md`. Only the owner/reviewer may approve the next phase. See the common testing guide for exception and release rules.
