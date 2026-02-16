---
title: "Oncall workflow with iOS shortcuts"
date: 2025-10-31T09:38:12+01:00
tags:
  - dev
---

_The title is foreshadowing._

**Problem statement**: when using an iPhone as a pager device for oncall duties,
disable airplane mode / "do not disturb" programmatically at the beginning of
your shift.

I find it's a good practice to disable smartphone notifications before going to
bed, whether by enabling airplane mode, activating "do not disturb", or
activating a custom focus mode.

However, say that your shift starts at 5am.

How can you ensure your phone is readily available for paging from 5am, whilst
all other notifications are kept ignored?

I found a sweet spot that works in all situations:

- Enable "do not disturb" before going to bed (this can be done automatically).
  This step is critical.
- Enable airplane mode before going to bed (this can be done automatically).
  This step is optional.
- Create a shortcut within the Shortcuts app:
  — Name: "Turn Airplane Mode Off"
  — Action: **Turn** Airplane Mode **Off**
- Create an automation within the Shortcuts app:
  — Automation: **Run Immediately** (This is important![^1])
  — Notify When Run: on
  — When: At 05:00, daily
  — Do: Trigger the shortcut defined previously

Why is this effective?

There are virtually no notifications until 5am.

From 5am, only _critical_ notifications (as defined by your pager app) will alert
you, thanks to airplane mode being off + "do not disturb" being on.

In the past I would leave Wi-Fi on (=airplane mode off) + "do not disturb" on,
but every once in a while I would get paged, even before 5am. Why? Because our
oncall rotation is configured to eventually alert the entire team if the current
oncall person does not timely ACK the page, which happens seldom. I'd rather
not take the risk and have my sleep interrupted.

This scheme only works in practice for oncall rotations that do not have a
secondary responder. If you're the secondary then you should let yourself be
reachable.

[^1]: Otherwise you'll need to confirm the automation before it runs, which
    defeats the purpose of the automation in this case.
