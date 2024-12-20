---
title: "Ruby: update Gemfile dependencies"
date: 2024-11-06T13:16:21+01:00
tags:
  - dev
---

Oneshot:

```shell
% gem update rubocop
```

That won't update the `.gemspec` file though. To do so:

```shell
bundler update rubocop
```

**Tip**: Omitting the gem name has the effect of updating all gems.
