---
title: "direnv: automatically load .env everywhere"
date: 2025-07-31T14:26:37+02:00
tags:
  - dev
---

[Previously]({{< ref "2024-08-01-direnv-nested" >}}),
[previously]({{< ref "2025-03-26-1password-cli-direnv-integration" >}}).

**Problem statement**: Given a monorepo with various scattered `.env` files, how
to ensure each one of them is automatically loaded when changing directories?

We could create sibling `.envrc` files in each directory, with the following
content:

```shell
#!/bin/sh
dotenv
```

[Documentation](https://direnv.net/man/direnv-stdlib.1.html#codedotenv-ltdotenvpathgtcode).

But this is cumbersome!

Also, perhaps your teammates simply do not want to use direnv.

Here's a more robust approach:

```shell
% cat ~/.config/direnv/direnv.toml
[global]
load_dotenv = true
```

This ensures every `.env` file is automatically loaded. No need to splatter
`dotenv` everywhere!

I have accidentally discovered this is possible via [this
issue](https://github.com/direnv/direnv/issues/1478).
