---
title: "Ruby: update Gemfile dependencies"
url: https://perrotta.dev/2024/11/ruby-update-gemfile-dependencies/
last_updated: 2024-12-20
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

