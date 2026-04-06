---
title: "direnv: automatically load .env everywhere"
url: https://perrotta.dev/2025/07/direnv-automatically-load-.env-everywhere/
last_updated: 2026-03-26
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

```toml {filename="~/.config/direnv/direnv.toml"}
[global]
load_dotenv = true
```

This ensures every `.env` file is automatically loaded. No need to splatter
`dotenv` everywhere!

I have accidentally discovered this is possible via [this
issue](https://github.com/direnv/direnv/issues/1478).

