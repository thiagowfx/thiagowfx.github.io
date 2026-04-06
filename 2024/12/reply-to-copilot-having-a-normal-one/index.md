---
title: "Reply to: CoPilot having a normal one"
url: https://perrotta.dev/2024/12/reply-to-copilot-having-a-normal-one/
last_updated: 2026-02-08
---


([via David Krider](https://davidkrider.com/copilot-having-a-normal-one/)):

> That's the thing I find about CoPilot and ChatGPT so far: They have quick
> answers and suggestions for every line as I'm typing, and half of everything
> that looks right at first glance turns out to be wrong. I actually started to
> argue with CoPilot after fruitlessly trying to use it to track down a bug for
> a half hour. What I am doing with my life?

Welcome to the club :D

Silencing CoPilot sometimes helps. Update `vscode/settings.json` (`Cmd + ,` on
macOS) according to your needs:

```json
"github.copilot.editor.enableAutoCompletions": true,
"github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": false,
}
```

The common wisdom of the crowds so far is to treat LLMs like "eager interns",
and/or "helpful boilerplate / scaffolding tools". Always double-check.

