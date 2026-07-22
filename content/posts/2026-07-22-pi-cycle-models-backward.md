---
title: "pi: cycle models backward with ctrl+n"
date: 2026-07-22T13:23:53+02:00
tags:
  - ai
  - coding
  - dev
---

[Previously]({{< ref "2026-07-22-caveman-mode-in-pi" >}}).

**Problem statement**: [pi](https://github.com/earendil-works/pi) binds `ctrl+p`
to `app.model.cycleForward`[^1] by default, but has no default binding to cycle
backward other than `shift+ctrl+p`, which is arguably difficult to remember.

Every keybinding in pi is namespaced and overridable via
`~/.pi/agent/keybindings.json`, documented in
[`docs/keybindings.md`](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/keybindings.md):

```json
{
  "app.model.cycleBackward": [
    "shift+ctrl+p",
    "ctrl+n"
  ]
}
```

`ctrl+n` is also the default for `app.session.toggleNamedFilter`, but that
only fires inside the session picker, not while a model selector or the main
editor has focus.

Run `/reload` in pi to pick up the keybinding addition without restarting the
session.

∴ `ctrl+p`/`ctrl+n` now cycle models forward/backward, matching the readline
(emacs!) history bindings I already have muscle memory for.

- - -

🤖 *Drafted with `/bloggify`.*

[^1]: It cycles through models selected in `/scoped-models`.
