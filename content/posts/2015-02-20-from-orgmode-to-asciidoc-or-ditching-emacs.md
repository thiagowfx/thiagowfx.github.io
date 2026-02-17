---
title: "From orgmode to asciidoc (OR: ditching emacs)"
date: 2015-02-20T14:42:16-03:00
tags:
  - dev
  - legacy
---

Hello people, I'm back. The portal will open in 3…2…1..**.** OK, here are some
_updates_. After taming the beast for two long years, I'm now slowly ditching
**emacs** from my life.

    _# archers, don't struggle yourselves!_
    sudo pacman -Rnsc $(pacman -Qdt emacs)
    _# *ntoo users, don't lose opportunity cost regarding precious compiling time!_
    sudo emerge -vC emacs && sudo emerge -avuDN @world && sudo emerge --depclean -a

Emacs doesn't simply go out and we are done here. No, no, no. Rehab, guys.
Org-mode was a fellow companion, now what? I even moved out of wordpress just to
blog with org files[^1]. **Orgmode** is the most amazing to-do / organizing /
planning / tracking tool I've ever used, however it is completely tied up to
emacs. The only thing we can do about that is to get all the knowledge and
**discipline** that orgmode teached to us, and then move on.

    And I moved on.

I'm now slowly converting my text formatting habits to Asciidoc. It is an oldie
(2002+) thing, but people are still using it, and very well, by the way.
Asciidoc is not a replacement for markdown[^2], but rather a full-featured text
formatting tool — markdown is KISS. I also found a nice[^3] tool to blog from an
asciidoc file directly to Wordpress; and it is called…blogpost, you are right.
It was created by the same author of asciidoc, so you can probably conclude it
is reliable. OK, goodbye for now, till next time.

## Footnotes

[^1]: now you realize this was useless, since I moved back to Wordpress. But at
least I learned some Hakyll and Haskell in the process.

[^2]: neither the other way around.

[^3]: not sure if it is really nice, but if you can see this footnote, then I can
guarantee you the tool still works. **Update** : actually, the tool works
indeed, but it doesn't play nice with footnotes.
