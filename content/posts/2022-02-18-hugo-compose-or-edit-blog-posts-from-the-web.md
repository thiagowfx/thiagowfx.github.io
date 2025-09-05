---
title: "Hugo: compose or edit blog posts from the web"
date: 2022-02-18T16:13:25-05:00
tags:
  - meta
---

This blog is managed and generated with [Hugo](https://gohugo.io), which is
a [SSG](https://jamstack.org/generators/) (static site generator), which
basically means I write all my blog posts in static markdown files, off-line,
and then do `git commit` + `git push` to publish them.

The advantage of this workflow is that it's really minimalist, efficient and
portable: I can use whatever text editor I want to[^1], from pretty much any
operating system I want to, even from my phone if I am really inclined[^2].

That said, sometimes I am on the go with a Chromebook and don't have easy
access to a machine to `ssh` to. Sure, I could just write a post in
a note-taking app like [Google Keep](https://keep.google.com/), [Standard
Notes](https://standardnotes.com) or [Simple Note](https://simplenote.com) and
publish it later. But what if I wanted to publish it right away?

It would be really nice if I could just pop up an editor in a web browser just like the cool kids do with WordPress, Medium and Substack...

[Mike Stone](https://mikestone.me/creating-on-github/) describes one way to do so, where he edits it directly from GitHub. That works fine, but then you need to write your post all at once, there's no "save and continue later".

I think a better approach is to use [GitHub codespaces]({{< ref "2022-01-02-ephemeral-linux-shell-access-in-the-cloud" >}}): I go to https://github.dev/thiagowfx/thiagowfx.github.io where there's a Visual Studio Code instance running on the web, make my edits or compose a new post therein, and then `git push`. Even if I don't want to `git push` right away, I could just come back later and continue it from where I stopped. It's brilliant! It even has terminal access if needed (e.g. to play with `hugo` on the go).

[^1]: I mostly use `vim` to compose these blog posts, and occasionally Visual
  Studio Code (`vscode`).
[^2]: There is a ton of markdown note-taking apps these days.
  [Bear](https://bear.app) ($$) seems to be a popular one for iOS, but even the
  stock Notes app is decent for drafting blog posts.
