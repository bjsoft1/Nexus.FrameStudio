# Recorder and video-editor source review
Input: `Nexus.ProductivityCare(1).zip`. Review is limited to recorder/editor source, associated recording models, and their design documents. Other ProductivityCare features were not reviewed or copied. The original archive is unchanged.
## What informed the prototype
- The recorder has basic/advanced configuration for source, multiple monitors, quality, independent audio, pointer/clicks, keyboard, captions, canvas, countdown, output, presets, hotkeys and diagnostics.
- The editor exposes a timeline, trim/split, crop, text/shapes, transform keyframes, pointer/key edits, audio mixing, save and export.
- The current model separates immutable captured media (`session.json`, MP4 parts, independent WAV tracks, pointer/key JSONL) from editable presentation (`project.json`). All package paths are relative.
- The source writer deduplicates identical cursor samples. This proposed design adds an explicit per-encoded-frame mapping index, with timestamped event references, so a frame can always resolve its pointer state without assuming wall-clock time or fixed frame rate.
- Webcam capture, full multi-file sequencing, mixed-span rich text and image/video picture-in-picture are proposed standalone-project capabilities. Their UI presence is not a claim that the uploaded recorder already implements them.
- Existing engineering documents contain phase/history notes; this prototype does not treat all historical status claims as current runtime verification. No original .NET build or device capture test was performed.
## Evidence anchors
- `Windows/RecorderSettingsWindow.xaml:315` — `Text="The device lists below come from Windows. System sound and microphone are recorded as separate editable tracks, so their levels can be adjusted independently in the editor."/>`
- `Windows/RecorderSettingsWindow.xaml:469` — `Text="Only display-safe shortcuts, function keys and navigation keys are stored. Ordinary typed letters, numbers and punctuation are never stored. Secure or uncertain fields are suppressed, and Ctrl+Shift+F12 immediately disables keyboard capture."/>`
- `Windows/RecorderSettingsWindow.xaml:216` — `<TextBlock Style="{StaticResource SectionTitle}" Text="Arrangement"/>`
- `Windows/RecorderSettingsWindow.xaml:424` — `<TextBlock Text="Effect style" VerticalAlignment="Center"/>`
- `Windows/VideoEditorWindow.xaml:152` — `Text="Trim, preview, add timed captions, choose the audio mix, and set a canvas background or border. Export renders those non-destructive edits to one MP4."/>`
- `Windows/VideoEditorWindow.xaml:378` — `Text="The pointer is not in the recorded video at all — it is kept as data and drawn here, which is why it can still be changed or switched off."/>`
- `Windows/VideoEditorWindow.xaml:598` — `<TextBlock Style="{StaticResource FieldLabel}" Text="Keyframes"/>`
- `Windows/VideoEditorWindow.xaml:126` — `<Button x:Name="SaveProjectButton" Content="Save project" MinHeight="30" Padding="12,5"`
- `Services/Recording/Capture/MonitorCaptureRecorder.cs:209` — `_session.IsCursorCaptureEnabled = false;`
- `Services/Recording/Capture/MultiMonitorCaptureRecorder.cs:205` — `session.IsCursorCaptureEnabled = false;`
- `Services/Recording/Capture/RecordingSessionWriter.cs:283` — `if (x == _lastPointerX`
- `Services/Recording/Capture/RecordingSessionWriter.cs:344` — `public void WriteKey(TimeSpan at, string key, uint virtualKey, IReadOnlyList<string> modifiers, bool repeat)`
- `Services/Recording/Capture/RecordingSessionWriter.cs:254` — `public void WritePointerEvent(`
- `Models/RecordingSessionManifest.cs:12` — `/// <para><b>Every path here is relative to the session folder.</b> One absolute path is all it takes`
- `Models/RecordingSessionManifest.cs:181` — `public sealed class RecordingTracks`
- `Models/RecordingSessionManifest.cs:155` — `public string? SystemAudio { get; set; }`
- `Models/RecordingProject.cs:21` — `public sealed class RecordingProject`
- `Models/RecordingProject.cs:70` — `public List<RecordingOverlayItem> Overlays { get; set; } = [];`
- `Models/RecordingProject.cs:74` — `public List<RecordingPointerEffectState> PointerEffects { get; set; } = [];`

## Reviewed reference files
- `Models/RecorderSettings.cs`
- `Models/RecordingSessionManifest.cs`
- `Models/RecordingProject.cs`
- `Models/RecordingOverlayModels.cs`
- `Models/RecordingCaptionModels.cs`
- `Windows/RecorderSettingsWindow.xaml`
- `Windows/VideoEditorWindow.xaml`
- `Windows/VideoEditorWindow.xaml.cs`
- `Services/Recording/Capture/MonitorCaptureRecorder.cs`
- `Services/Recording/Capture/MultiMonitorCaptureRecorder.cs`
- `Services/Recording/Capture/RecordingSessionWriter.cs`
- `SCREEN_RECORDER_BACKEND_DECISION.md`
- `SCREEN_RECORDER_EDITOR_TECH_DECISION.md`

## Boundary
This is a new HTML/CSS/JavaScript design prototype, not an extraction or compiled replacement of the existing application. Production technology selection and five implementation phases are deliberately deferred until design approval.
