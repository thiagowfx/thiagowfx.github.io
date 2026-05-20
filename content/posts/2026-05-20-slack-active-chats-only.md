---
title: "Slack: active chats only"
date: 2026-05-20T12:11:17+02:00
tags:
  - dev
  - serenity
---

I've been greatly enjoying the [_Active only_](https://slack.com/help/articles/212596808-Adjust-your-sidebar-preferences)
conversation filter on Slack:

> Choose how you'd like to filter your conversations. By default, you'll see
> Active only, which will hide conversations with no new activity in the past 30
> days.

"Dead" channels (and chats) eventually become hidden[^1], active ones bubble up.

Pairing it up with [VIP
contacts](https://slack.com/help/articles/34963579361683-Add-contacts-as-VIPs)[^2]
and
[muting](https://slack.com/help/articles/204411433-Mute-channels-and-direct-messages)
makes Slack a breeze to use.

To activate it, from the left sidebar, click the gear/settings icon > Filter and
sort > Active only.

My left sidebar structure currently looks like this:

- External connections (outside my Organization)
- TechOps (our internal SRE / DevOps team)
  - ...TechOps teammates
  - ...TechOps channels
- Alerts
  - ...Channels for Incident Management (ephemeral in nature).
  - ...Channels for alerts / monitoring / notifications. Most of them are
      muted, except the actionable and/or critical ones.
- Site
  - ...Channels related to my workplace (city, country, social groups, etc)
- Everything else (unmanaged, ungrouped)

In the past I tried to overzealously micromanage the organization / labelling of
channels; that proved to be a mistake. I am quite happy with my current setup.

[^1]: ...and they are prime candidates for [tidying up](https://slack.com/blog/productivity/spring-cleaning-tips-for-tidying-up-your-channels). Click the gear/settings icon > Clean up your channel list.

[^2]: My definition: manager, skip, CTO, CEO, close teammates.
