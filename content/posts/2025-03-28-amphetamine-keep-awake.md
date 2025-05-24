---
title: "Amphetamine: Keep awake"
date: 2025-03-28T00:14:32+01:00
tags:
  - bestof
  - dev
---

[Amphetamine](https://apps.apple.com/us/app/amphetamine/id937984704?mt=12):

> The most awesome keep-awake app ever created for macOS. Amphetamine can keep
> your Mac, and optionally its display(s), awake through a super simple on/off
> switch, or automatically through easy-to-configure Triggers. Amphetamine is
> extremely powerful and includes advanced features for those who need them, yet
> remains intuitive and easy-to-use for those who don't need all of the bells
> and whistles.

It's like [Caffeine](https://www.caffeine-app.net/) (or one of its dozen
clones), but better.

Here's how I use it:

* on my personal laptop, whenever I am streaming a movie or a TV show (e.g. via
  [jellyfin](https://jellyfin.org/), so that it doesn't cut off the streaming in
  the middle

* on my work computer, as soon as I start the work day, so that the VPN stays
  connected for the whole day, as well as my SSH sessions

Upon launching it a system tray icon appears. A left-click opens up its
contextual menu, exposing lots of knobs and details. A right-click toggles it on
/ off.

I configure the toggle so that it stays awake for a default of 4 hours for my
personal laptop, and 8-10 hours for my work computer (=the duration of an usual
work day).

If you don't specify a limit then it stays awake indefinitely, which is
counterproductive: (i) spending more energy and battery than necessary and (ii)
from an operational security perspective, it _should_ ideally self-lock at some
point, in case you forget to do so.

I just care about keeping internet and sessions connectivity alive, but it's
also possible to configure it to keep the display on.

For bonus productivity, configure it to always launch at login, so that
activating it is just one (right) click away.

Apparently I activated it more than 180 times in my personal laptop, effectively
keeping it awake for more than 24 days. At work, more than 250 sessions for more
than 8 days[^1].

When writing this post, I just learned that I can activate it via
[AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html):

```shell
% osascript -e 'tell application "Amphetamine" to start new session'
```

Now I can augment my [`prodaccess`]({{< ref "2024-10-18-prodaccess" >}}) script
with that.


[^1]: There is definitely something odd with these numbers.
