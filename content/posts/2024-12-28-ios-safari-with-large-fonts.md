---
title: "iOS safari with large fonts"
date: 2024-12-28T15:14:45-03:00
tags:
  - dev
---

Ever since I switched my blog theme from [Hugo
PaperMod](https://github.com/adityatelange/hugo-PaperMod) to my own based on
[bearblog](https://github.com/janraasch/hugo-bearblog/), I had this weird issue
wherein some font sizes, especially within `code` tags, where quite large.

To illustrate with a rough example:

<pre><code>% ollama serve
<span style="font-size: larger;">Couldn't find '/Users/thiago.perrotta/...'</span>
Your new public key is:
[...]</code></pre>

This would only happen in Safari on iOS.

In particular, it would not happen in Safari on macOS, and it would not be
reproducible in the mobile mode of Chrome DevTools.

After a bit of research, I found:

```css
body {
  ‑webkit‑text‑size‑adjust: 100%;
}
```

...fixes the issue perfectly. [Source](https://stackoverflow.com/questions/15861093/what-does-webkit-text-size-adjust-do).

> It specifies that if you(author) want to resize the text when the browser
> page is zoomed. Most of the times it is better to set it to auto or 100% as
> the web browser will take care of how resizing of text is to be done.
