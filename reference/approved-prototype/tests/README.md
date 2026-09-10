# Repeatable prototype tests

Opening the prototype needs no developer tools. The optional test suite requires Python 3.10+ and Playwright with Chromium installed. The actual versions used in this delivery are recorded in `results/report.json`.

```powershell
python -m pip install playwright
python -m playwright install chromium
python tests/smoke_test.py --screenshots
```

Use `--browser "C:\path\to\chrome.exe"` to select an existing compatible Chromium executable. The test uses only generated fixture data and files; it never requests desktop, webcam, microphone or keyboard-hook access.

Default mode creates a self-contained document from the project's HTML/CSS/JS and renders it with `page.set_content`. This tests the UI and hash routes without a web server. It does **not** test file navigation, local-server navigation or durable browser localStorage across reloads. In the supplied execution environment, direct file/HTTP browser navigation was blocked by policy; in-memory rendering was used without changing that policy.

For an explicit served-site launch check on your own development machine, serve the project separately and supply its URL:

```powershell
# Terminal 1, from the project folder:
python -m http.server 8080

# Terminal 2, from the same folder:
python tests/smoke_test.py --url http://127.0.0.1:8080/index.html --screenshots
```

The served-url mode was not executed for this delivery. Run it in a disposable browser profile: tests change prototype state. The optional served-URL mode clears the prototype-specific draft in its disposable test context on each fresh page. Do not substitute these results for production engine tests.

Outputs: `tests/results/report.json`, `tests/results/REPORT.md`, downloaded fixture project/JSON/SRT/review files, and optional screenshots. The command exits nonzero on any failed assertion. It checks all 54 routes at both 1920×1080 and 1366×768, HTML entry paths, interaction workflows, import validation, track availability, project downloads/reimport and explicit simulated-export behavior.

For Windows manual review, use `docs/MANUAL_TEST_CASES.md`. Native capture, synchronized media, encoder/device compatibility, privacy guarantees, packaged/raw format fidelity, crash recovery and installer testing remain out of scope until implementation.
