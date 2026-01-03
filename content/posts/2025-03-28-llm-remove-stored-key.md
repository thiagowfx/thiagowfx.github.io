---
title: "llm: remove stored key"
date: 2025-03-28T14:09:41+01:00
tags:
  - ai
  - dev
---

I was just trying [Simon Willison](https://simonwillison.net/)'s excellent CLI
[llm](https://llm.datasette.io/en/stable/index.html) tool:

> A CLI utility and Python library for interacting with Large Language Models,
> both via remote APIs and models that can be installed and run on your own
> machine.

It's straightforward to set API Keys with it:

```shell
% llm key set openai
```

I wanted to set one for [Anthropic Claude](https://www.anthropic.com/claude):

```shell
% llm key set claude
```

But it turns out the correct name is `anthropic`, not `claude`:

```shell
% llm key set anthropic
```

Now I wanted to clean up the `claude` entry.

Surprisingly, there's no `llm key remove` or `llm key delete` command!
[Docs](https://llm.datasette.io/en/stable/help.html#llm-keys-help).

The workaround: edit the `keys.json` file directly:

```shell
% llm keys path
/Users/thiago.perrotta/Library/Application Support/io.datasette.llm/keys.json
```

The output above is from macOS.

```shell
% $EDITOR "$(llm keys path)"
/Users/thiago.perrotta/Library/Application Support/io.datasette.llm/keys.json
```

The `keys.json` file:

```json
{
  "// Note": "This file stores secret API credentials. Do not share!",
  "openai": "sk-{redacted}",
  "claude": "sk-ant-api03-{redacted}",
  "anthropic": "sk-ant-api03-{redacted}"
}
```

Remove `claude` from it:

```json
{
  "// Note": "This file stores secret API credentials. Do not share!",
  "openai": "sk-{redacted}",
  "anthropic": "sk-ant-api03-{redacted}"
}
```

And it's done! Verify with:

```shell
% llm keys
anthropic
openai
```
