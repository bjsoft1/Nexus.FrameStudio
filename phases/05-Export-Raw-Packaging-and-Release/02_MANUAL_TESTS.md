# Phase 5 — Export, raw packages & release — manual UI tests

**All cases: NOT_RUN. Run against the native phase build, not the HTML prototype.**

Read `../../docs/TESTING_GUIDE.md` for fixture setup, evidence and numeric targets. Screen numbers refer to the approved prototype/native equivalent. Test only disposable controlled data.

## P5-M01 — Final export presets

**Prerequisites:** F09; baseline and capable higher-resolution device

1. In Export video (48) choose MP4 at 720p/1080p and each capability-approved higher preset.
2. Toggle audio/captions/interactions separately.
3. Export and inspect.

**Expected:** Actual dimensions/FPS/track inclusion match selected settings; unsupported presets explain why they cannot run.
**Evidence:** `artifacts/acceptance/P5/P5-M01/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M02 — Queue snapshots, cancel and retry

**Prerequisites:** F09

1. Queue two exports (49).
2. Change the live project's title after queueing.
3. Cancel one job and retry it.
4. Review final statuses.

**Expected:** Each job retains its snapshot; canceled output is never labeled complete; retry uses an explicit snapshot choice.
**Evidence:** `artifacts/acceptance/P5/P5-M02/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M03 — Encoder failure and safe fallback

**Prerequisites:** Controlled encoder-failure fixture

1. Select Automatic then inject initialization failure.
2. Repeat with Software selected.
3. Inject a disk error instead.

**Expected:** Automatic may perform one declared software fallback; Software stays software; disk failure is not disguised as fallback success.
**Evidence:** `artifacts/acceptance/P5/P5-M03/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M04 — Existing target and source protection

**Prerequisites:** F09; an existing valid export and source-hash list

1. Export over the existing test target and cancel/fail during writing.
2. Try selecting a source media/project path as output.

**Expected:** Prior output and sources remain unchanged; source targets are blocked; only private partial files are cleaned up.
**Evidence:** `artifacts/acceptance/P5/P5-M04/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M05 — Full raw package round trip

**Prerequisites:** F09

1. In Save editable project (47) export a full .nfsraw.
2. Import it into a different user folder.
3. Open editor and change one effect.

**Expected:** Media, timeline, input/audio availability and styles remain editable; package paths resolve without the first machine.
**Evidence:** `artifacts/acceptance/P5/P5-M05/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M06 — Raw-package privacy warning and sanitization

**Prerequisites:** F04 with mic muted and keys hidden

1. Export a full raw package and read the warning.
2. Export a separate sanitized package omitting mic and keyboard.
3. Inspect both packages and the original.

**Expected:** Full package correctly warns that hidden/muted data is included; sanitized copy excludes chosen sources/references and marks them redacted; original is unchanged.
**Evidence:** `artifacts/acceptance/P5/P5-M06/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M07 — Unsafe raw archives

**Prerequisites:** F07; isolated disposable test directory

1. Open each hostile/corrupt .nfsraw through Import (04).
2. Inspect the error and staging cleanup.
3. Verify sentinel files outside staging.

**Expected:** Every unsafe archive is rejected before registration; no outside file is changed and no active project is replaced.
**Evidence:** `artifacts/acceptance/P5/P5-M07/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M08 — Save As and associations

**Prerequisites:** F09; installed test build

1. Save As to a new workspace (47).
2. Double-click each .nfsproject/.nfsraw in File Explorer.
3. Cancel a subsequent copy.

**Expected:** Correct app/workspace opens; new IDs/ownership are safe; system MP4 default is not silently changed.
**Evidence:** `artifacts/acceptance/P5/P5-M08/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M09 — Autosave and interrupted-part recovery

**Prerequisites:** F09 and interrupted disposable take

1. Kill the app during a test save and during capture finalization.
2. Relaunch Recovery (51).
3. Restore a validated snapshot/committed parts into a new workspace.

**Expected:** Last good data remains available; partial content is identified; recovered copy states any lost tail instead of promising zero loss.
**Evidence:** `artifacts/acceptance/P5/P5-M09/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M10 — Cache cleanup and shared media

**Prerequisites:** Two projects referencing a controlled shared asset

1. In storage preferences (52) clear caches/proxies.
2. Attempt source/session deletion with another project referencing it.
3. Cancel.

**Expected:** Only disposable cache is removed; shared-source impact is shown and no unique media is deleted without explicit consent.
**Evidence:** `artifacts/acceptance/P5/P5-M10/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M11 — Second-machine full workflow

**Prerequisites:** H01/H03 on machine A; clean supported machine B

1. Capture, edit, add all overlay types and mute only mic on A.
2. Transfer full .nfsraw to B.
3. Reopen, unmute captured mic, restyle cursor and export.

**Expected:** No original device/path is required for editing; independent tracks and timing survive; actual final MP4 is playable on B.
**Evidence:** `artifacts/acceptance/P5/P5-M11/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M12 — Long-session and higher-quality recording

**Prerequisites:** H01/H02/H03; benchmark profile

1. Record the agreed 60-minute 1080p30 baseline with periodic markers.
2. Repeat the declared supported higher-quality stress profile.
3. Review metrics and exported sync markers.

**Expected:** No unexplained drift or unbounded memory growth; achieved FPS, dropped frames and device details are reported, not assumed.
**Evidence:** `artifacts/acceptance/P5/P5-M12/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M13 — Permission, disk and concurrency failures

**Prerequisites:** Isolated test volumes/profiles and disposable media

1. Deny output permission, simulate low disk and open the same project twice.
2. Start save/export/capture operations as applicable.

**Expected:** Clear errors and project locking prevent conflicting writes; prior-good saves and finalized media remain valid.
**Evidence:** `artifacts/acceptance/P5/P5-M13/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M14 — Install, upgrade and uninstall

**Prerequisites:** Clean Windows test VM; release candidate

1. Install per-user and launch.
2. Save a project; upgrade to a test-next build.
3. Uninstall while preserving user data.
4. Reinstall and open the project.

**Expected:** Version/identity are correct; projects remain; signing/credential limitations are explicit; no old-app identity is reused.
**Evidence:** `artifacts/acceptance/P5/P5-M14/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.

## P5-M15 — Final owner review

**Prerequisites:** All phase reports and release candidate

1. Review all 54 states in light/dark and fullscreen/small window.
2. Complete capture→edit→raw→export workflow.
3. Read known issues and evidence, then record a release decision.

**Expected:** Required features and tests have real evidence; unresolved required failures block approval; release requires an explicit owner decision.
**Evidence:** `artifacts/acceptance/P5/P5-M15/`
**Actual / status / defect:** NOT_RUN / not supplied / none recorded.
