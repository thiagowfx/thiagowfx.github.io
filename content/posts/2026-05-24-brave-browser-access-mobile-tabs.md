---
title: "Brave Browser: access mobile tabs"
date: 2026-05-24T19:22:13+02:00
tags:
  - dev
---

**Problem statement**: given two distinct devices with
[Brave](https://brave.com/), access tabs from one device in the other device. In
this example: access mobile tabs from a desktop device. This assumes both
devices are already enrolled in Sync.

Clicking 'History: in the menu bar does not work for this purpose. There are no
options related to mobile tabs there. Which is non-intuitive / a poor UX
experience.

The following options work:

## Option #1

From a desktop device: Click the 3-dot menu > History > Your Devices > iPhone >
[...].

## Option #2

Navigate to brave://history/syncedTabs. Access it via Cmd-Y (History) > Tabs
from other devices.
