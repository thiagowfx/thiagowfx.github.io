
[Faff connecting a new Kindle to a Mac with a USB
cable](https://petegraham.com/kindle-faff/) by Pete Graham:

> TL;DR: new Kindles don't show up as external drives on macOS when connected by
> USB-C. You need a program like OpenMTP to transfer files to them

My Kindle Paperwhite, bought during the COVID-19 pandemic (early 2020s), shows
up as an external drive on macOS. It's a breeze to manage, and it's easy to
[jailbreak]({{< ref "2025-05-17-winterbreak-hello-world" >}}).

My partner's Kindle Paperwhite, bought in 2025, **does not** show up as an
external drive on macOS. _Boooo!_

That is a glowing example of
[enshittification](https://en.wikipedia.org/wiki/Enshittification), but it's not
what this post is about[^1].

**Problem statement**: transfer an `.epub` from your laptop to one of these
newer (2024+?) Kindles.

This is by no means obvious but, as already mentioned above, it is simply not
possible to do it via a traditional copy & paste filesystem operation – it does
not matter whether you use Finder or the terminal, the kindle filesystem is
simply not exposed.

Pete suggests [OpenMTP](https://openmtp.ganeshrvel.com/):

> Advanced Android File Transfer App for macOS
>
> Tired of using expensive, outdated, bug heavy, Android File Transfer apps for
> macOS?
>
> Now, have easy, smooth sailing experience and transfer multiple files in one
> go!
>
> Introducing OpenMTP — Safe, Transparent, Open-Source and FREE for a lifetime!

I can confirm it works reliably, as promised. It resembles [midnight
commander](https://midnight-commander.org/) with its dual-pane file manager.

Another possibility – which remains my favorite – is to use
[Calibre](https://calibre-ebook.com/download). Calibre recognizes all Kindle
Paperwhite models, old or new. [Kovid](https://github.com/kovidgoyal) is a
wizard. It works so well!

A third possibility is to use the official [Send to
Kindle](https://www.amazon.com/gp/sendtokindle/email/) service from Amazon:

> Add personal documents, web content, and other files to your library to read
> them on your Kindle or in the Kindle app with features like reading progress,
> notes, highlights, bookmarks, and more. Your Kindle device has a unique email
> address that you can send documents to.

It requires an Amazon account, and your Kindle to be registered and tied to it.

Two more observations:

- when connecting an USB cable from your Kindle to your laptop, note that it
  must be a data cable. Not all cables are data cables. For example, my portable
  charger cable is not a data cable. My bicycle light cable is not a data cable.
  If OpenMTP or Calibre do not recognize your Kindle upon connecting it, try
  using another cable
- even though newer Kindle software versions can read `.epub` and, in fact, even
  the Send to Kindle service supports it nowadays, not all `.epub` files will
  be properly recognized by the Kindle. To ensure books are always readable by
  the Kindle, convert them to `.mobi` or `.azw3` before transferring them.
  Calibre is a great tool to do so!

[^1]: Let's take a moment of silence to appreciate how an older device model is
    in fact _superior_ to a newer one. It's a bit of a stretch, but no wonder
    why some people hold on dearly to their Lenovo Thinkpads or to their Toyota
    Priuses. There's one exception: newer Kindles uses USB-C, which is arguably
    better from a standardization perspective.

