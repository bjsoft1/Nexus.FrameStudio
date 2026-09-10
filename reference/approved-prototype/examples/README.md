# Example files

`Demo-Walkthrough.nfsproject` is an actual reopenable **browser prototype** project. Import it through Screen 04. It restores the illustrative desktop demo, not real captured media.

`session.example.json`, `frame.example.json`, `pointer.example.json`, and `keyboard.example.json` are UI inspector samples generated from demo state. They demonstrate fields, not a complete replay dataset.

`portable-session.example.json`, `frames-001.example.jsonl`, `pointer-events.example.jsonl` and `keyboard-events.example.jsonl` illustrate a proposed production format. The frame file has 90 synthetic 30-fps frames across three seconds, with microphone capture disabled throughout. Screen, camera and audio paths are illustrative; no playable media is included. Every frame has explicit timestamps and pointer state. Audio JSON contains sample references, never the actual sound.

`pages.json` is the 54-screen catalog. Theme examples are in `assets/`.

Do not import raw-session design JSON as `.nfsproject`; they are deliberately different schemas.
