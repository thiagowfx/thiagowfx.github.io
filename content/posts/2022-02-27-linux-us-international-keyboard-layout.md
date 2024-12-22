---
title: "Linux: US International keyboard layout"
date: 2022-02-27T22:47:09-05:00
tags:
  - dev
  - linux
---

I use QWERTY keyboards with a US layout. Sometimes I need to type accents or
cedillas, and I keep forgetting how to do so, this post summarizes how to do it.


## Intro

There are basically two layouts:

1. US (_'vanilla'_): type accents like ``'^`~`` and they will be emitted immediately
2. US International (INTL): accents are the so called ['dead keys'](https://en.wikipedia.org/wiki/Dead_key):

> A dead key is a special kind of a modifier key on a mechanical typewriter, or
> computer keyboard, that is typically used to attach a specific diacritic to a
> base letter.

We can switch between keyboard layouts with `setxkbmap`. It's also possible to
use `localectl` in systemd-based distros, but its syntax is harder to remember
so I won't even include it here.

## Set US 'vanilla' keyboard layout

```shell
$ setxkbmap us
```

This is what a standard QWERTY keyboard should use to type in English.

## Set US International (INTL) keyboard layout

```shell
$ setxkbmap -layout us -variant intl
```

This is what a standard QWERTY keyboard[^1] should use to type, for example, in Portuguese or in German.

### Portuguese

```text
- á é í ó ú     :   ' + <vowel>
- â ê î ô û     :   ^ + <vowel>
- ã õ           :   ~ + <vowel>
- à             :   ` + <vowel>
- ç (cedilla)   :   Alt Gr + , (Option + c on macOS)
```

### German

```text
- ß (ss)  :   Alt Gr + s (Option + s on macOS)
- ä ö ü   :   " + <vowel>
```

[^1]: Alt Gr is typically the Right Alt key.
