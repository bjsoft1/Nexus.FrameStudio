# Engineering references

Reviewed for this plan on 10 September 2026. These references support API/platform facts only; they are not evidence of this app passing tests. Numeric acceptance budgets in this plan are proposed engineering targets.

| ID | Primary source | Used for |
|---|---|---|
| S1 | Microsoft Learn — [What's new in .NET 10](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-10/overview) | .NET 10 platform baseline. |
| S2 | Microsoft Learn — [WPF overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/overview/) | Windows-only native UI, XAML, binding, styles and DPI-independent layout. |
| S3 | Microsoft Learn — [IsCursorCaptureEnabled](https://learn.microsoft.com/en-us/uwp/api/windows.graphics.capture.graphicscapturesession.iscursorcaptureenabled?view=winrt-26100) | API control over capture of the cursor. |
| S4 | Microsoft Learn — [Loopback recording](https://learn.microsoft.com/en-us/windows/win32/coreaudio/loopback-recording) | Independent capture of a render endpoint's system audio. |
| S5 | Microsoft Learn — [Supported Media Foundation formats](https://learn.microsoft.com/en-us/windows/win32/medfound/supported-media-formats-in-media-foundation) | Initial codec/container capability boundaries. |
| S6 | Microsoft Learn — [Sink writer encoding tutorial](https://learn.microsoft.com/en-us/windows/win32/medfound/tutorial--using-the-sink-writer-to-encode-video) | Native stream setup, timestamps and encoding adapter baseline. |

## User-supplied references

The approved `Nexus.FrameStudio.Prototype.zip`, its feature/review/project-format documents, and recorder/editor areas of `Nexus.ProductivityCare(1).zip` informed this plan. See `SOURCE_REUSE_REVIEW.md` for exact code paths and observed compatibility risks. Only the approved prototype is included as a full reference copy; the old application source is not redistributed in this plan.
