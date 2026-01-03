---
title: "M1 Macbook Air keeps disconnecting from Wi-Fi"
date: 2025-06-24T13:34:50+02:00
tags:
  - dev
  - macos
---

[M1 Macbook air keeps disconnecting from
wifi](https://www.reddit.com/r/mac/comments/vv5day/m1_macbook_air_keeps_disconnecting_from_wifi/):

> I've had this mac for a few months and never had this issue until today. It
> will disconnect every 1 minute it's really frustrating.

Lately I've been having the same issue, more or less. Also in a M1 Macbook Air.

There's also [this
thread](https://discussions.apple.com/thread/255556937?sortBy=rank) in the Apple
Community forums.

> I've tried forgetting the network then adding it again, checking for any
> updates but it's all up to date.

Right. Times of desperation call for desperate measures, but those don't really
help.

In that thread, there is a suggestion to run Wireless diagnostics: `Option +
Wi-Fi > "Open Wireless Diagnostics..."`. This is a good idea, but it also
appeared not to work in my case.

I got reminded of a [thread](https://bbs.archlinux.org/viewtopic.php?id=270326)
I posted a few years ago in the Arch Linux forums:

> Whenever I turn my desktop on and log in with my primary user, internet is
> usually available. I can `sudo pacman -Syu`, `ping google.com`, etc.
>
> Occasionally though, when I turn my desktop on, internet isn't available. My
> go-to "fix" (it's more like a workaround, really) is to simply do:
>
> `% systemctl restart iwd`

...which was quite similar, albeit on Linux.

It's just so frustrating whenever this happens, and it's hard to even know where
to start troubleshooting. My setup is the same as always, there was no change to
ISPs, hardware, software, or anything else, really.

There was a light at the end of the tunnel: I found this [superuser
thread](https://superuser.com/questions/826338/macbook-air-constantly-drops-wifi-connection):

> My MacBook Air keeps dropping wifi connection on my home network. When I
> connect to my network, it remains connected for a few minutes, then it drops
> the connection. I have no idea what's the problem. I found several forums on
> the internet discussing this, but none of them really gave a working solution.

Ah yes, buddy. I feel you. We are [soulmates](https://xkcd.com/979/).

Someone suggested the following:

> `% ping -i 0.2 192.168.1.1`

And, to my abysmal surprise, that seems to have worked[^1]. Rationale:

> The problem is that OS X tries to put the WiFi antenna into a power saving
> mode if there's no data being sent or received, but with some WiFi APs, this
> leads to disconnecting. That ping command will ping your router every 0.2
> seconds, preventing OS X from turning off the WiFi.
>
> This is not a brilliant solution, but it will work until Apple does something
> about this.

I need to make a few more experiments before I can conclude it is a reliable
solution, but so far I am sold, as I ran out of ideas. The `0.2s` interval is
too frequent though; `0.5s` appears to be enough.

The answer author suggested to wrap the script in an Automator app. This is
quite elegant, should we ever deem it as a long-term "solution". I suppose that
a [Hammerspoon](https://www.hammerspoon.org/) spoon would also be elegant in
this context.

[^1]: It could simply be placebo, as far as I'm concerned...
