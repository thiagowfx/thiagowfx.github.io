---
title: "Bcrypt-hash a password"
date: 2024-06-06T13:35:05+02:00
tags:
  - dev
---

Given the password `correct horse battery staple`, we would like to bcrypt-hash
it.

{{< figure align="center" src="https://imgs.xkcd.com/comics/password_strength.png" link="https://xkcd.com/936/" alt="Through 20 years of effort, we've successfully trained everyone to use passwords that are hard for humans to remember, but easy for computers to guess." attr="XKCD Courtesy of Randall Munroe" >}}


Here's one way to do so via the command line:

```shell
$ htpasswd -nbBC 10 "" 'correct horse battery staple' | tr -d ':\n' | sed 's/$2y/$2a/'
```

...which yields:

```
$2a$10$HKSHfLu4l7TvOmnLkhUngu2U1pJUUw7hEU0LE1iN84S09fJsZowHm
```

You could verify it matches e.g. via https://bcrypt-generator.com/.

**Context**: [ArgoCD](https://argo-cd.readthedocs.io/en/stable/) expects a
bcrypt-hashed password in its config file.
