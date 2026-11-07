---
title: "macos: meetingbar for calendar events"
date: 2026-11-07T22:46:24Z
tags:
  - bloggify
  - macos
  - serenity
---

[Previously]({{< ref "2026-11-07-spotify-spotmenu" >}}).

I was too quick to declare I no longer needed Raycast. SpotMenu replaced its
Spotify menu bar display, but I forgot another feature: [showing the next
calendar meeting]({{< ref
"2025-02-08-upcoming-calendar-meeting-in-mac-os-menu-bar-with-raycast" >}}).

[MeetingBar](https://meetingbar.app/) replaces that too. It shows the current
or next meeting in the macOS menu bar and lets us join calls with one click.
It is free and [open source](https://github.com/leits/MeetingBar).

Install with [Homebrew](https://brew.sh/):

```shell
% brew install meetingbar
==> Downloading Homebrew API data
✔︎ JSON API packages.arm64_golden_gate.jws.json              Downloaded   16.0MB/ 16.0MB
==> Fetching downloads for: meetingbar
✔︎ Cask meetingbar (4.11.6)                                  Downloaded   11.3MB/ 11.3MB
==> Installing Cask meetingbar
==> Moving App 'MeetingBar.app' to '/Applications/MeetingBar.app'
🍺  meetingbar was successfully installed!
```

Then open MeetingBar and choose a calendar source during onboarding. It can
use accounts synchronized with `Calendar.app`, or connect to Google Calendar
directly.

SpotMenu for music, MeetingBar for meetings. _Now_ I can remove Raycast without
losing either menu bar feature.
