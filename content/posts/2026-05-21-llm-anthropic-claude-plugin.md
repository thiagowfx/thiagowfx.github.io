---
title: "llm: Anthropic Claude plugin"
date: 2026-05-21T16:33:51+02:00
tags:
  - ai
  - dev
---

[Simon Willison](https://simonwillison.net/)'s
[`llm`](https://llm.datasette.io/) CLI ships with OpenAI models out of the box.
Anthropic Claude support lives in a separate plugin,
[`llm-anthropic`](https://github.com/simonw/llm-anthropic).

```shell
% llm plugins
[]
```

Install it:

```shell
% llm install llm-anthropic
...
Successfully installed anthropic-0.103.1 docstring-parser-0.18.0 llm-anthropic-0.25
```

Verify:

```shell
% llm plugins
[
  {
    "name": "llm-anthropic",
    "hooks": [
      "register_models"
    ],
    "version": "0.25"
  }
]
```

Claude models are now registered:

```shell
% llm models | grep -i anthropic
Anthropic Messages: anthropic/claude-opus-4-7 (aliases: claude-opus-4.7)
Anthropic Messages: anthropic/claude-sonnet-4-6 (aliases: claude-sonnet-4.6)
Anthropic Messages: anthropic/claude-haiku-4-5-20251001 (aliases: claude-haiku-4.5)
[...]
```

Set the API key:

```shell
% llm keys set anthropic
```

And prompt away:

```shell
% llm -m claude-haiku-4.5 "hello"
Hello! How can I assist you today?
```
