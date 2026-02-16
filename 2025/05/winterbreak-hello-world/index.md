
I decided to
[jailbreak](https://en.wikipedia.org/wiki/Privilege_escalation#Jailbreaking) my
Kindle on January 1st this year, once I got aware of the
[WinterBreak](https://kindlemodding.org/jailbreaking/WinterBreak/)[^1] exploit,
via the excellent
[MobileRead](https://www.mobileread.com/forums/showthread.php?t=365372) forums:

> I am proud to present the culmination of over a year of procrastination:
> WinterBreak WinterBreak is a new jailbreak which works on ANY KINDLE (from
> the K5) on ANY FIRMWARE

Life happens though, and only now I got time to do so.

However, I took one important precaution since then, which was _essential_:
ensure my Kindle was _always_ in airplane mode.

Whenever the Kindle is connected to Wi-Fi, it gets
[OTA updates](https://en.wikipedia.org/wiki/Over-the-air_update) automatically
from Amazon. This is generally a sensible default and the desired behavior.
However, for jailbreaking purposes, you want your device to stay stuck on time
and [_never ever ever_](https://www.youtube.com/watch?v=WA4iX5D9Z64) get
updates. An update could make the jailbreak cease to work. In fact, that's
exactly what happened during these last 4-5 months:

> *Note that models on 5.18.x no longer work, please check the wiki's model list
> for more info

I was prudent to verify it was still running 5.17.x before proceeding.

The expected time to do the whole process was about half an hour, and it's super
user-friendly. Seriously, the folks at [Kindle
Modding](https://kindlemodding.org/) did an amazing documentation job; arguably
the procedures are friendly even to non-developers. The process boils down to
connecting your Kindle to a laptop (the OS doesn't really matter), copying a
bunch of files and directories over to it, ejecting it, tapping some buttons,
and repeating this procedure a couple of times.

For me it took about one hour, because I was careful to take photos (in case I
screwed up) and notes (for this blog post, and also for the sake of reverting
the process should I want to – for example, if I ever sell the device to a third
party).

Before deciding to do it, I watched
[this](https://www.youtube.com/watch?v=hJ59M0io6zE) and [this
video](https://www.youtube.com/watch?v=Qtk7ERwlIAk) which made me feel even more
confident it is the outcome I was longing for. [Previously]({{< ref
"2024-12-31-independence" >}}).

I won't document the jailbreak procedure here: there's no point. First, the
upstream documentation is amazing; second, the steps here would likely easily
get outdated. Head over to [the WinterBreak
docs](https://kindlemodding.org/jailbreaking/WinterBreak/). Even better, read
the [FAQ](https://kindlemodding.org/jailbreaking/jailbreak-faq.html) first. That
said, here are a few notes and anecdotes.

I had to disable parental controls on my Kindle. I had them enabled to prevent
me from accidentally buying books from the Amazon Store[^2]. This is the closest
to adblocking I could find, and I was happy with that setting. That said, one of
the jailbreak steps is to open the store, therefore the parental controls must
be turned off. This is not documented upstream – to be honest, most people
wouldn't be in that situation anyway.

The process failed in the first attempt. I am not quite sure why. It got stuck
at the `Jailbreaking — please wait...` screen. The docs say:

> If you do not see any funky text then make sure Airplane mode is disabled to
> avoid any automatic update. Turn it back on after you see the text though!

That was not helpful to me though. What worked was to [restart the
device](https://www.youtube.com/watch?v=5UT8RkSmN4k) and try again.

The second attempt worked.

Once the jailbreak is done, head over to [Post
Jailbreak](https://kindlemodding.org/jailbreaking/post-jailbreak/). Steps:

- set up a hotfix: to ensure the jailbreak persists, even after restarting the
  device
- install KUAL & MRPI: package managers, basically
- disable OTA updates: important to ensure an automatic update does not revert
  the jailbreak
- re-enable the store: not super relevant for me, but why not – and then turn
  parental controls back on
- install [KOReader](https://koreader.rocks/): surely this is the most exciting
  part

> KOReader is a document viewer for E Ink devices. Supported fileformats include
> EPUB, PDF, DjVu, XPS, CBT, CBZ, FB2, PDB, TXT, HTML, RTF, CHM, DOC, MOBI and
> ZIP files. It's available for Kindle, Kobo, PocketBook, Android and desktop
> Linux.

A few highlights from the FAQ:

> **Is it possible to undo the jailbreak ("unjailbreak")?**
>
> Yes, perform a factory reset on the device and then install the same firmware
> update (or higher).

This makes the action of doing the jailbreak a no-brainer. Sure, there's always
a (small) chance of bricking your device, but I think it's worth the risk.

> **Will this get my Amazon account banned?**
>
> No reports of Amazon accounts being banned after jailbreaking have been
> reported so far. However, please refrain from telling support that you have
> modified your device.

Common sense. I never contacted Amazon Support in 11+ years of owning Kindles,
so I don't particularly care about it anyway.

> **Will this void the warranty on my Kindle device?**
>
> Probably.

This is always the case with jailbreaking.

It's much easier to commit when you have an old device that is already out of
the warranty period.

Avoid jailbreaking brand new devices. :)

> **Can I still use the default reader after jailbreaking?**
>
> Yes.

It's true: I verified it. This is great. In the (unlikely) case I find out that
KOReader sucks[^3], I don't need to regret it.

> **Is it possible to change screensavers in the native Kindle UI?**
>
> Although there are currently no extensions to change the screensavers in
> hard-float firmware, it is still possible to change them, but it is not
> recommended as it is very easy to brick the device.

Noted. But:

> You can easily change screensavers with KOReader (search for the
> "screensavers" feature).

> **How can I check if my device is jailbroken?**
>
> Type `;log` into the search bar, if a message pop ups, you're jailbroken.

And now I'm done.

I cannot stress this enough: it's very important to read the docs thoroughly
before deciding to jailbreak. [RTFM](https://en.wikipedia.org/wiki/RTFM)!

Perhaps I'll write a follow-up post-jailbreaking user experience blog post.

## Appendix

```
% tree Downloads
Downloads
├── koreader-kindlehf-v2025.04.zip
├── kual-mrinstaller-khf.tar.xz
├── renameotabin.zip
├── Update_hotfix_universal.bin
├── Update_KUALBooklet_ALLDEVICES_KS2_install.bin
└── WinterBreak.tar.gz
```

[^1]: Yes, it's called WinterBreak because it got released during Winter (in the
    Northern hemisphere).

[^2]: Even if I were interested in doing so, I'd rather use my phone or my
    computer for that. The Kindle Store experience _from the Kindle_ is
    horrible.

[^3]: Their domain is https://koreader.rocks...

