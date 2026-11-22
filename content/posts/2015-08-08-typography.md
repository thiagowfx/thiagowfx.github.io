---
title: "Typography"
date: 2015-08-08T03:28:59-03:00
draft: true
tags:
  - dev
  - legacy
  - serenity
---

Introduction talking about nice fonts, blablabla – ya know -->
[LaTeX](https://en.wikipedia.org/wiki/LaTeX) --yeah, I'm actually skipping this
part.

The purpose of this post is to give a few suggestions of fonts to people who
don't know many fonts. The results of it, although concise, originates from
several years of trial-and-error by your humble author, until he could finally
find the "perfect" fonts for him.

Here are a couple of random points:

- Don't use comic sans [(1)](http://bancomicsans.tumblr.com/)
  [(2)](http://www.comicsanscriminal.com/). This also applies to Arial and other
  fonts originally known to be shipped with the Microsoft Windows operating
  system.
- Make Wikipedia display [LaTeX fonts](https://github.com/AndrewBelt/WiTeX)!

*Screenshot unavailable: Wikipedia, LaTeXified*.

- Suggestion of nice monospace fonts (aka fonts for editing (and reading!) source code):
  - Ubuntu Mono
  - Inconsolata
  - Adobe Source Code Pro – this is the second one I most like
  - CamingoCode – this is my preferred one right now
  - Terminus (this is a bitmap font – the best bitmap one)
- Suggestion of fonts for the sole purposing of reading pleasantly (e.g. books, long texts, long websites):
  - Baskerville – my preferred one for the Kindle Paperwhite 2.
  - Bitter – a bit aggressive, but smooth
  - The one [this guy](http://www.daveliepmann.com/tufte-css/) uses for his website, based on the work of Edward Tufte (ETBembo).
  - The one demize uses for [his website](https://theos.kyriasis.com/~kyrias/journal.html#entry:11): [Fontin](http://www.exljbris.com/fontin.html) and [Fontin Sans](http://www.exljbris.com/fontinsans.html) (ttf-exljbris)
  - LaTeX fonts, of course!
  - Linux Libertine font family
- Suggestion of a couple of fonts for random purposes (including serif and sans serif ones):
  - Fira Sans / Fira Mono – the ones from the Firefox OS Family
  - Open Sans (from Google)
  - Ubuntu font family
- Suggestion of fonts for "neutral" purposes (aka you don't really want to use different fonts at all)
  - Windows font family (cof cof...): Calibri, Cambria, Tahoma, Segoe UI, Times New Roman, Verdana, Arial. ~~Comic Sans.~~
  - Linux (classic) font family: ttf-bistream-vera, ttf-dejavu, ttf-liberation, nimbus-sans, cantarell-fonts (gnome 3)
  - Mac font family: Helvetica, Lucida Grande.
  - Chrome OS fonts: those ones are neutral but are nice looking! Roboto, Arimo (sans-serif), Tinos (serif), Cousine (monospace).

## Try these

If you're on Linux, use a good `fonts.conf` (*man* `fonts.conf` (5)) config: see
[mine](https://github.com/thiagowfx/dotfiles/blob/master/fonts.conf), for
example. Here is a copy of it, just in case:

```xml
<?xml version='1.0'?>
<!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>
<fontconfig>
 <match target="font">

  <edit mode="assign" name="rgba">
   <const>rgb</const>
  </edit>

  <edit mode="assign" name="hinting">
   <bool>true</bool>
  </edit>

  <edit mode="assign" name="hintstyle">
   <const>hintslight</const>
  </edit>

  <edit mode="assign" name="antialias">
   <bool>true</bool>
  </edit>

  <edit mode="assign" name="lcdfilter">
    <const>lcddefault</const>
  </edit>

 </match>
</fontconfig>
```

And, if you're on Windows: [Melhorando a renderização de fontes no Windows]({{< ref path="2014-07-12-melhorando-a-renderizacao-de-fontes-no-windows" lang="pt" >}})

If you use Arch Linux, check out the
[infinality](https://wiki.archlinux.org/index.php/Infinality) repo.

And **yes**, typography is really nice!
