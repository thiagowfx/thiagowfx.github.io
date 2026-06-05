---
title: "brew trust"
url: https://perrotta.dev/2026/06/brew-trust/
last_updated: 2026-06-05
---


It's a lovely day to upgrade my system:

```shell
% brew upgrade
[...]
Homebrew will ignore formulae, casks and commands from these taps when `HOMEBREW_REQUIRE_TAP_TRUST` is set.
This will become the default in Homebrew 6.0.0 or 5.2.0, whichever comes first.
Enable trust checks now with:
  export HOMEBREW_REQUIRE_TAP_TRUST=1
Trust specific formulae, casks or commands with:
  brew trust --formula <user>/<tap>/<formula>
  brew trust --cask <user>/<tap>/<cask>
  brew trust --command <user>/<tap>/<command>
or trust installed formulae from these taps with:
  brew trust --formula thiagowfx/pancake/pancake
  brew trust --formula thiagowfx/taps/cco thiagowfx/taps/python-is-python3
You can trust all formulae, casks and commands from these taps with:
  brew trust [...] thiagowfx/pancake thiagowfx/taps
Prefer trusting only the specific formulae, casks or commands you need.
Untap them with:
  brew untap [...] thiagowfx/pancake thiagowfx/taps
To keep allowing them by default during the transition:
  export HOMEBREW_NO_REQUIRE_TAP_TRUST=1
This is not recommended and will be removed in a later release.
```

This is a great move!

With many supply-chain attacks in open-source repositories lately, it's a very
welcome feature.

Do I trust myself? I think so!

```shell
% brew trust thiagowfx/pancake thiagowfx/taps
Trusted tap: thiagowfx/pancake
Trusted tap: thiagowfx/taps
```

