---
title: "cco: additionalDirectories"
date: 2026-03-18T17:31:13+01:00
tags:
  - ai
  - dev
  - security
---

[Previously]({{< ref "2026-02-26-cco-claude-condom-sandbox" >}}).

**Problem statement**: passing `--add-dir` flags to
[cco](https://github.com/nikvdp/cco) in a shell alias doesn't scale well as
the number of directories increases.

I had this alias:

```shell
alias claudey="cco --allow-oauth-refresh --add-dir ~/.cache --add-dir ~/.aws/cli/cache --add-dir ~/.aws/sso/cache --add-dir ~/.azure --add-dir ~/.terraform.d/plugin-cache"
```

`cco` now supports reading `additionalDirectories` from
`.claude/settings.local.json`, inside the `permissions` object:

```json
{
  "permissions": {
    "additionalDirectories": [
      "~/.cache",
      "~/.aws/cli/cache",
      "~/.aws/sso/cache",
      "~/.azure",
      "~/.terraform.d/plugin-cache"
    ]
  }
}
```

...since [PR #44](https://github.com/nikvdp/cco/pull/44).

The alias then becomes:

```shell
alias claudey="cco --allow-oauth-refresh"
```

The directories are now project-specific, checked into each repo's
`.claude/settings.local.json`. Much cleaner.

I wish it would support the global `~/.claude/settings.json` too, but it
doesn't.
