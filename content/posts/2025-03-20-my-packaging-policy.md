---
title: "My packaging policy"
date: 2025-03-20T13:10:52+01:00
tags:
  - dev
  - serenity
---

[My packaging policy](https://whynothugo.nl/journal/2022/08/13/my-packaging-policy/) by Hugo Osvaldo Barrera:

> The open source sphere has continuously had a lot of discussion regarding
> packaging, and there's often an expectation that upstream developers should
> distribution packages. I want to make it clear where I stand on this, what
> users of my projects can expect, and what how packagers can contribute.
>
> [...]
>
> Honestly, it's usually too much work for me (an most upstream developers) to
> provide these packages. I don't use Debian and Fedora. I'm not familiar with
> all the quirks of rpm and deb. Even if I take the time to build these, I'll be
> shipping a packages for platforms that I don't use. There would be zero
> quality control. And that additional work is not something for which I want to
> sign up. I want to focus on maintaining upstream.
>
> [...]
>
> That said, I've nothing against others packaging my tools for different
> platforms. In fact, I encourage it! If someone with the right expertise wants
> to build a Debian package for caffeine-ng, darkman, vdirsyncer or any other
> project, I welcome the effort. My focus is on shipping releases ready to be
> packaged, and let packagers do their jobs.
>
> Additionally, if any packager finds obstacles, or needs to apply patches for
> code to build on a given platform, please open an issue (or send a patch). I
> don't mind giving guidance. But don't expect me to know all the quirks of
> every distribution.

As a packager myself, from my perspective, Hugo's stance on the topic is the
most desirable possible.

Working with upstream can sometimes drain your energy and motivation to
contribute. Having developers be open and friendly is one of the best ways to
ensure the gears of open source keep working smoothly.

I wish we had less fragmentation. When you go to
[Repology](https://repology.org/) or [DistroWatch](https://distrowatch.com/), it
feels so tiresome to see so many projects, distributions and package managers in
the wild. Diversity and choice are positive, but they come with a non-trivial
cost of reinventing the wheel and (re)doing everything over and over again. Life
is already short, and yet so much of it is spent repackaging the same software a
dozen times for a myriad of `.deb` or `.rpm` flavours, let alone all the indie /
independent ones. Politics yields a feedback loop that weakens open source and
unity.
