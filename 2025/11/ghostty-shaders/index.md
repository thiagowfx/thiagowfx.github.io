
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

The end result? See the [demo in the repo README](https://github.com/sahaj-b/ghostty-cursor-shaders?tab=readme-ov-file#demos).

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

