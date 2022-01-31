---
title: "Watch files and react to changes during development"
date: 2022-01-30T21:32:17-05:00
tags:
  - dev
  - linux
  - programming
showtoc: true
---

This post describes some tooling usages to watch for file changes and run or reload a command whenever they happen.

<!--more-->

## Context

I am contributing to [miniflux](https://github.com/miniflux/v2), a minimalist and opinionated RSS reader. Miniflux's stack is as minimalist as the app itself: It's a Golang application that connects to a local PostgreSQL database. It has a well-documented and comprehensive [`Makefile`](https://github.com/miniflux/v2/blob/master/Makefile).

In order to achieve an edit-and-preview workflow for quick prototyping and local iteration, all that it's needed is to execute `make run` whenever any[^1] file in the repository is changed.

My goal was to achieve that workflow with the least amount of friction, and with an application that is widely available in most package managers / linux distributions out there.

## Option #1: entr

[`entr(1)`](https://eradman.com/entrproject/):

> Run arbitrary commands when files change

The following invocation does the job:

```shell
$ fd | entr -r -- make run
```

However, we could do better. From the upstream docs:

> » ag and ack offer many advantages over utilities such as find(1) or ls(1) in that they recognize files by their contents and are smart enough to skip directories such as .git

I am happy with `fd` for this use case though. To limit `entr` to `.go` files only, we could do:

```shell
$ fd -e go | entr -r -- make run
```

It took me less than 5 minutes to install and figure out how to use `entr`.

## Option #2: watchman

[`watchman`](https://facebook.github.io/watchman/) from Facebook Open Source:

> Watchman exists to watch files and record when they change. It can also trigger actions (such as rebuilding assets) when matching files change.

Watchman's workflow doesn't seem to be very suited for this job though. It's much more centered on subscribing to `inotify` events:

```shell
cd <repository root>
watchman watch .
```

...and then adding predefined actions to recompile parts of the application as they change. The official docs give an example with CSS minification:

```shell
# set up a trigger named 'buildme'
# will run 'minify-css' whenever a CSS file is changed
watchman -- trigger . buildme '*.css' -- minify-css
```

In this regard it seems to be more modular, and I could easily see a scenario where I would kick off several specialized triggers in a webdev project: for example, one for CSS minification, one for JS minification, another one for TypeScript compilation, etc.

That said, for the simple use case of triggering (and reloading) `make run`, it seems overkill. I also found its [official docs](https://facebook.github.io/watchman/docs/install.html) too verbose and lacking sample usages for simple `Makefile`-based projects like miniflux.

One caveat of [`watchman`](https://repology.org/project/watchman/versions) is that it's less widely available than [`entr`](https://repology.org/project/entr/versions). Another caveat is that recently official distributions of watchman seem to be binary only, even though watchman itself is open source.

It took me several minutes to figure out what's the gist of watchman, only to realize it is more bloated than warranted.

## Conclusion

For simple projects, `entr` is the way to go, hands down. For complex webdev projects, I would look into `watchman` more deeply.


[^1]: To be truly strict, only changes to `.go` files matter.