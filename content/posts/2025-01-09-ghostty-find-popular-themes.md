---
title: "ghostty: find popular themes"
date: 2025-01-09T02:56:37-03:00
tags:
  - dev
---

[Ghostty 1.0](https://ghostty.org/) was barely released and it's already quite
popular.

I've been [daily driving]({{< ref "2024-12-28-ghostty" >}}) it since December
last year and it has been quite enjoyable. There are a few annoyances here and
there, but its minimalism and speed make up for them.

Today I stumbled upon [ghostty.town](https://ghostty.town/), which hosts
user-submitted configs. Reminds me of:

- https://terminal.love/
- https://terminal.sexy/

My current config is quite simple (by design!):

```
cursor-style-blink = false
shell-integration-features = no-cursor

theme=catppuccin-macchiato

macos-titlebar-style=tabs
```

I got inspired to use the [Catppuccin](https://catppuccin.com/) theme thanks to
[Jon Seager](https://jnsgr.uk/2024/07/how-i-computer-in-2024/).

There's no need to customize the default font as it's [quite sensible]({{< ref
"2024-12-25-picking-a-monospaced-code-font" >}}) (JetBrains Mono, [as
per](https://ghostty.org/docs/config)).
