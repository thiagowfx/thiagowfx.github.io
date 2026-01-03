---
title: "Alpine Linux packaging: track new software releases"
date: 2025-06-03T01:36:53+02:00
tags:
  - alpine-linux
  - bestof
  - dev
---

**Problem statement**: You maintain packages for a Linux distribution, for
example, [Alpine Linux](https://www.alpinelinux.org/). Find a way to keep track
of new software releases, to ensure your packages are kept up-to-date.

The [Release Monitoring](https://release-monitoring.org/) project (codename
_Anitya_), part of the [Fedora Linux](https://www.fedoraproject.org/) distro,
can accomplish that:

> Watch for releases of your favorite projects
>
> We all have our favorite projects and we all like to use their latest versions
> with their latest features. However, it is hard to keep in touch with all of
> them and be informed when they release a new version. Anitya can help!
>
> We monitor upstream releases and broadcast them on Fedora messaging bus.

The underlying project:

> Anitya is a release monitoring project.
>
> Its goal is to regularly check if a project has made a new release. When
> Anitya discovers a new release for a project, it publishes a RabbitMQ message
> via fedora messaging. This makes it easy to integrate with Anitya and perform
> actions when a new release is created for a project. For example, the Fedora
> project runs a service called the-new-hotness which files a Bugzilla bug
> against a package when the upstream project makes a new release.
>
> Anitya provides a user-friendly interface to add, edit, or browse projects.

Even though it is part of Fedora, we can use it for Alpine Linux just fine!

Recently I packaged [zizmor](https://github.com/zizmorcore/zizmor/issues/780). I
noticed there was no entry for it in Anitya. I added one. It's very
straightforward:

- head to https://release-monitoring.org/
- ensure the project you want to monitor isn't already present there
- log in (e.g. via GitHub)
- click [add project](https://release-monitoring.org/project/new)

Fill in the form:

- Project name: zizmor
- Homepage: https://docs.zizmor.sh
- BackEnd: GitHub
- Version scheme: Semantic
- Github owner/project: [zizmorcore/zizmor](https://github.com/zizmorcore/zizmor)
- Version prefix: `v`
- Pre-release filter: `rc`
- Version filter: `rc` (excludes [`1.8.0-rc0`](https://github.com/zizmorcore/zizmor/releases/tag/v1.8.0-rc0)) and the like
- Check off "check releases instead of tags"

Once the project is [created](https://release-monitoring.org/project/378497/),
add a new distribution mapping:

- Distribution: Alpine
- Package name: [zizmor](https://pkgs.alpinelinux.org/package/edge/testing/x86_64/zizmor)

And we're done!

As per https://pkgs.alpinelinux.org/flagging:

> Package flagging
>
> Manual package flagging has been disabled in favour of automatic flagging
> based on Anitya.
>
> If you want a package to be up-to-date or to inform the maintainer about the
> package status, please feel free to create a package mapping on Anitya. Once
> the mapping is made, it should automatically send an email to the maintainer
> whenever a new version is available.
>
> For details on how to create a project mapping for Alpine Linux, please refer
> to the [release monitoring
> documentation](https://release-monitoring.org/static/docs/user-guide.html).
