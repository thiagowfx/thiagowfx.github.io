
As of [Sep 22nd, 2025](https://github.com/Homebrew/homebrew-command-not-found),
homebrew _natively_ supports a "command-not-found" hook.

The emphasis is on _natively_.

Previously this could be achieved with a tap:

```shell
brew tap https://github.com/Homebrew/homebrew-command-not-found
src_files "$(brew --prefix)/Library/Taps/homebrew/homebrew-command-not-found/handler.sh"
```

Thus yielding this effect:

```shell
% ghc
zsh: correct 'ghc' to 'gh' [nyae]? n
The program 'ghc' can be found in the following formulae:
  * ghc
  * ghc@9.10
  * ghc@9.4
  * ghc@9.6
  * ghc@9.8
Try: brew install <selected formula>
```

The difference today is that there's no need to tap an extra repository anymore
to do so; the hook is henceforth built directly into homebrew[^1]:

```shell
hash brew >/dev/null 2>&1 && src_files "$(brew --repository)/Library/Homebrew/command-not-found/handler.sh"
```

For completeness, untap the command-not-found repository as it is no longer
needed:

```shell
% brew doctor
Please note that these warnings are just used to help the Homebrew maintainers
with debugging if you file an issue. If everything you use Homebrew for is
working fine: please don't worry or file an issue; just ignore this. Thanks!

Warning: You have the following deprecated, official taps tapped:
  Homebrew/homebrew-command-not-found
Untap them with `brew untap`.
```

```shell
brew untap Homebrew/homebrew-command-not-found
% Untapping homebrew/command-not-found...
Untapped (2,572 files, 87.4MB).
```

My dotfiles diff:

```diff
commit f02c9ab2b203a6235414924e7ddb4b8b6ac6ee52 (HEAD -> master)
Author: Thiago Perrotta <{redacted}>
Date:   Tue Sep 23 10:16:47 2025 +0200

    brew: command-not-found

diff --git profile/.profile.d/10-brew.sh profile/.profile.d/10-brew.sh
index 1828f77..97645f0 100644
--- profile/.profile.d/10-brew.sh
+++ profile/.profile.d/10-brew.sh
@@ -11,9 +11,8 @@
 [ -z "$HOMEBREW_PREFIX" ] && [ -x /opt/homebrew/bin/brew ] && eval "$(/opt/homebrew/bin/brew shellenv)"

 # command-not-found hook
-# setup: brew tap "homebrew/command-not-found"
-# https://github.com/Homebrew/homebrew-command-not-found
-hash brew >/dev/null 2>&1 && src_files "$(brew --prefix)/Library/Taps/homebrew/homebrew-command-not-found/handler.sh"
+# brew --prefix works too
+hash brew >/dev/null 2>&1 && src_files "$(brew --repository)/Library/Homebrew/command-not-found/handler.sh"

 # GNU coreutils
 path_munge "/opt/homebrew/opt/coreutils/libexec/gnubin"
```

[^1]: [`src_files`](https://github.com/thiagowfx/.dotfiles/blob/13d66a2b80efa02c611a747008124cbbb3ef3a8f/profile/.profilerc#L17).

