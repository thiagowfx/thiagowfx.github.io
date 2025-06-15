---
title: "ChromeOS hterm: customize fonts"
date: 2022-01-26T19:48:52-05:00
tags:
  - dev
---

[ChromeOS hterm][hterm] ("Secure Shell extension") is one of my favorite chrome extensions.
It is a bit dull with its out-of-the-box monospace font though.
In this post we'll learn how to customize it.


## Google Fonts

The easiest way to customize the Secure Shell extension to use a custom font is to select one from [Google Fonts][google-fonts].
Once you select a font from there, it will give you information like this:

```none
Use on the web
To embed a font, copy the code into the <head> of your html
( ) <link> (x) @import

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
</style>

font-family: 'IBM Plex Sans', sans-serif;
```

All we have to do is to copy the URL within the `url('...')` fragment above,
go to the [settings](chrome-extension://iodihamcpbpeioajjeobimgagajmlibd/html/nassh_preferences_editor.html) of the Secure Shell extension,
and then paste it there:

```none
# Example 1: IBM Plex Sans
Custom CSS (URI): https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap

# Example 2: Fira Code
Custom CSS (URI): https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap

# Example 3: Combine both
https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&family=IBM+Plex+Sans&display=swap
```

And then set the extension to use it:

```none
Text font family: "IBM Plex Sans", "Fira Code", monospace
```

From Secure Shell [FAQ][faq]:

> By default, we disable ligatures. Some fonts actively enable them like macOS's Menlo (e.g. "ae" is rendered as "æ"). This messes up copying and pasting and is, arguably, not terribly legible for a terminal.

If your font supports [ligatures](https://en.wikipedia.org/wiki/Ligature_(writing)), consider enabling them:

```none
Custom CSS (inline text):

* {
    -webkit-font-feature-settings: "liga" on, "calt" on;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}
```

Not all fonts are available on Google Fonts though.
For example, [Hermit][hermit] is one of my current monospace favorites: it's not there[^1].

## Github

Many fonts are available on GitHub (or in other forges), checked into a git repository.

If you happen to find a `.woff2` web font file laying therein, you could also use it in hterm:

```none
Custom CSS (inline text):

@font-face {
  font-family: "Anonymous Pro";
  src: url(https://cdn.rawgit.com/wernight/powerline-web-fonts/8040cf32c146c7cd4f776c1484d23dc40685c1bc/fonts/AnonymousPro.woff2);
}
```

And then set the extension to use it:

```none
Text font family: "Anonymous Pro", monospace
```

**Note**: I couldn't get this method to work with `.ttf` or `.otf`.

[faq]: https://chromium.googlesource.com/apps/libapps/+/master/nassh/doc/FAQ.md
[google-fonts]: https://fonts.google.com/
[hermit]: https://pcaro.es/p/hermit/
[hterm]: https://chrome.google.com/webstore/detail/secure-shell/iodihamcpbpeioajjeobimgagajmlibd?hl=en

[^1]: https://github.com/pcaro90/hermit/issues/2