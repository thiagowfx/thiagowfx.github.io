---
title: "mise: one frontend for tool versions"
date: 2026-08-21T16:55:45+02:00
tags:
  - ai
  - coding
  - dev
---

[Previously]({{< ref "2026-08-20-thoughtworks-technology-radar" >}}).

Thanks to the ThoughtWorks Technology Radar I finally decided to adopt
[mise](https://mise.jdx.dev/), so I migrated my dotfiles to use it for every
programming language runtime:

- `rbenv` (ruby)
- `tfenv` (terraform)
- `nvm` (nodejs)
- `pyenv` (python)

A single bespoke declarative file to rule them all:

```toml {filename="~/.config/mise/config.toml"}
[tools]
go = "1.27"
node = "26.7"
python = "3.14"
ruby = "3.4"
rust = "1.97"
terraform = "1.15"
terraform-docs = "0.24.0"
```

Deleted `~/.rbenv` (1.2 GB, three ruby builds) and `~/.config/tfenv` (821 MB,
eight terraform builds). Mise is using 275 MB now. That's a nice cleanup bonus.

I should write a dedicated blog post about it if it sticks in my setup.
