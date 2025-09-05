---
title: "bkt: cache command outputs"
date: 2024-12-29T19:27:21-03:00
tags:
  - bestof
  - dev
---

My esteemed friend [Michael Diamond](https://github.com/dimo414) wrote [`bkt`](https://www.bkt.rs/)[^1]:

> bkt (pronounced "bucket") is a subprocess caching utility written in Rust.

I mentioned it [previously]({{< ref "2022-01-18-arch-linux-new-pkgbuild-workflow" >}}) as an example on how to create a `PKGBUILD` for Arch Linux.

Here is the main use case for me:

Assume you have a command that is expensive to run.
The command is intended to display information / output about some resources.
Even though it's expensive, its output rarely changes.
So that...caching it would be quite beneficial.

For example, a command to list all your cluster nodes alongside some of their properties.
Perhaps you need to run that command multiple times a day[^2].

Enter `bkt`!

By creating an alias or a wrapper function in your shell (e.g. by adding it to your shell rc file) that uses `bkt`, you can make subsequent command runs complete faster, by leveraging its cache.

```shell
active_gardens_pp () {
        bkt --ttl 7d -- {list clusters command} -o json | jq '.[] | select(.active == true and .partition != "private-cloud" and .partition != "gov-cloud")' | mlr --ijson --opprint --barred cat
}
```

The first time I run `active_gardens_pp`[^3], it takes several seconds to complete.
The second time, it completes almost instantaneously.

The cache duration can be defined with the `--ttl` flag. One day or one week or a couple of hours can be sensible defaults, depending on how often you expect the output to change.

And then I should talk about [`mlr`](https://github.com/johnkerl/miller) (Miller) another day...

[^1]: In Rust™. And with a [domain hack](https://en.wikipedia.org/wiki/Domain_hack).
[^2]: Especially if, like me, you like to often close your tabs to tidy up (whether browser or terminal ones).
[^3]: `pp` stands for pretty-print.
