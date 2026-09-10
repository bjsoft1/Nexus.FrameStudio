# Prototype boundaries and remaining work

## Implemented UI, not a native media engine

This is a vanilla HTML/CSS/JS design prototype. Recording, webcam, device selection, sound meters, system/mic acquisition, global shortcuts, pointer hooks, encoder selection and MP4 export are simulations. Nothing is secretly recorded. The title bar is decorative except the browser fullscreen action.

Local image/video/audio imports use browser object URLs. Decoder support depends on the browser and file; unsupported media is not transcoded. The source desktop and camera tiles are original CSS illustrations. Imported audio can be previewed through a browser player, but the multi-source timeline does not perform a synchronized audible mix.

## Editing coverage

Timeline seek/play, split, trim, reorder, basic overlay transforms, undo/redo, keyframe data and some preview animations work in the browser. Crop is a framing preview, not a final decoded crop renderer. Transition controls demonstrate an effect, not a true two-clip rendered dissolve. Quality settings change the export plan, not an actual file. Audio gains, fades, noise reduction and preserve-pitch controls are design state, not production DSP. Color controls are illustrative CSS preview adjustments, not a color-managed pipeline.

Formatted text supports basic formatting and a separate emphasized final-word span; arbitrary rich-text selection, multiple font runs and a full formatting model are future work. Image/video overlays work for locally imported decodable media; without an imported file the tiles are explicit placeholders. Source clip timing is editable, but production ripple behavior, source-linked events across every split/reorder/speed change, and high-volume timeline performance need implementation and native tests. Frame step/timecode demonstration is 30 fps; other capture/export frame-rate settings remain configuration state.

## Capture and frame metadata

The capture simulation models source-on/off periods, pause, markers and availability. Capture-off never creates fictional recorded data. A captured-once track may still contain gaps. The UI reports those gaps; frame-accurate suppression throughout the illustrative preview is not a completed media feature. Frame JSON is a sample contract, not live frame acquisition. Audio samples belong in media files; JSON contains references and timing only.

A clean recording must exclude cursor, keyboard badges and webcam pixels from the screen source at capture time to guarantee later removal. Effects already baked into imported video cannot be reconstructed or reliably removed. Capturing the system cursor is platform-dependent and requires native verification, including application-rendered cursors.

## Saving and privacy

`.nfsproject` here is prototype JSON, not a portable media archive. It cannot embed or recover source media, and it is not a migration of the existing app's `project.json`. The proposed `.nfsraw` container is documented only. Local storage may be disabled or isolated for file URLs; always download your project and feedback. Browser-reload persistence is not validated in the supplied headless test run.

Privacy controls are a design, not a guarantee of secure-field detection. Production capture must be consent-based and visibly active, use an allowlist of safe shortcut events, avoid ordinary typed text, and fail closed for uncertain input contexts. Hiding a keyboard effect is not deleting its source data. The sanitized-copy flow is illustrative and does not delete files. Video/audio can still contain sensitive content even when input metadata is disabled.

## Validation limits

The supplied automated report covers only browser-rendered prototype behavior and specified viewport sizes. It does not prove a working Windows installer, native recorder, C# build, hardware encoder, synchronized A/V rendering, secure input detection, interruption recovery or no data loss. No production feature is considered accepted by this report. Direct file/HTTP browser navigation was blocked by the execution environment's administrative policy; tests used in-memory standalone rendering without changing policy settings.

## Deferred until approval

Native technology and media-library selection, codec distribution/licensing, file associations, capture-engine extraction, editor rendering, migration, installation, performance, accessibility audits and the five implementation phases.
