---
title: "Ghostty shaders"
date: 2025-11-30T18:17:36-03:00
tags:
  - dev
  - serenity
---

Ghostty supports [shaders](https://mitchellh.com/writing/ghostty-devlog-005).

[This repo](https://github.com/sahaj-b/ghostty-cursor-shaders) hosts a
collection of custom shaders readily available.

I integrated them with my [.dotfiles](https://github.com/thiagowfx/.dotfiles)
via a
[submodule](https://github.com/thiagowfx/.dotfiles/commit/d1a8779290d0ec9181dcc6a7c092d825cd187186):

Ghostty config:

```
custom-shader = shaders/cursor_tail.glsl
```

The
[`cursor_tail.glsl`](https://github.com/sahaj-b/ghostty-cursor-shaders/blob/main/cursor_tail.glsl)
file was added with a symlink to the submodule.

The end result?

![cursor tail](https://private-user-images.githubusercontent.com/94101577/506154536-0c1ecd67-8ff4-4198-9e89-a4435289bfa0.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQ1Mzc5NTAsIm5iZiI6MTc2NDUzNzY1MCwicGF0aCI6Ii85NDEwMTU3Ny81MDYxNTQ1MzYtMGMxZWNkNjctOGZmNC00MTk4LTllODktYTQ0MzUyODliZmEwLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTExMzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMTMwVDIxMjA1MFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWJlYzkyZTU5ODQwMDZkZTc4MjdkOTBmNDJjM2YwOGY0MTkyNWIwNzA2NDJjZDJkMmYwMWMyNWRhMDhlMDJlZDkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.xmssUdWJkuVB_SaBVJU6m6BfeQRnrC88GCo3L8ELEXM)

`#power`

Mitchell Hashimoto:

> Okay, but this is all completely pointless,right? The most common use case is
> fun and that's certainly not necessary (yeah, screw fun, right?). However, the
> primary practical use case for custom shaders is accessibility. Custom shaders
> are a really great way to specifically address certain forms of
> colorblindness, affect contrast or brightness to make things more readable,
> create "magnifying glass" effects, etc.

See also: [Fun with Ghostty
Shaders](https://catskull.net/fun-with-ghostty-shaders.html),
[l-o-o-s-e-d.net](https://l-o-o-s-e-d.net/kb/terminals/ghostty)
