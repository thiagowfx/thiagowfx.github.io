---
title: 'Steam Deck "downloading update" boot loop'
date: 2024-10-05T23:58:48+02:00
tags:
  - dev
  - gaming
---

Today I tried to use my Steam Deck to no avail.

Upon turning it on, a "Downloading update (…)" splash screen would appear, then the device would quickly turn itself off, in a matter of seconds.

Repeating this dance a couple of times yielded the same results.

Then I found out that if you hold the three-dot button (the quick settings menu button) briefly after turning it on, you are prompted with a boot loader screen that resembles GRUB. In this screen it's possible to roll back to an earlier OS version.

The Steam Deck disk partitioning has two partitions (A and B), just choose the second one (i.e. not the latest one).

This time upon restarting the device the boot loop was gone.

**Credits**: https://www.reddit.com/r/SteamDeck/comments/1bb5767/steam_deck_stuck_at_update_complete_launching/
