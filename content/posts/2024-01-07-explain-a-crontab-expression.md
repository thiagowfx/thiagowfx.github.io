---
title: "Explain a crontab expression"
date: 2024-07-01T18:48:47+02:00
tags:
  - dev
  - devops
  - linux
---

Given, for example, `0 0 * * *`, how do you figure out when it will run?

<!--more-->

- Option 1: Read the docs! The [ArchWiki](https://wiki.archlinux.org/title/Cron)
  is frequently a great reference. Alternatively, use your favorite search
  engine.
- Option 2: Ask ChatGPT! A simple `cron: 0 0 * * *` prompt is enough. No need
  to embezzle it with `explain what this does` or `what does this do?`.
- Option 3: Paste it into https://crontab.guru/.
