---
title: "localhost under your own domain"
date: 2024-12-27T22:24:11-03:00
tags:
  - dev
---

To interact with `localhost`, you can use `127.0.0.1`.

In certain scenarios, you may need a domain name though.

You could use [nip.io](https://nip.io):

> dead simple wildcard DNS for any IP Address

...for example, via `127.0.0.1.nip.io`.

Or you could use `local.gd` e.g. `localhost.local.gd`.

But what if you wanted to eliminate the dependence on third-parties and,
instead, do this yourself?

Assuming you have your own domain, create the following DNS record – I'll use my
own `perrotta.dev` domain as an example:

```
A localhost.perrotta.dev 127.0.0.1
```

Then whenever I ping `localhost.perrotta.dev`, it will end up pinging
`127.0.0.1`.
