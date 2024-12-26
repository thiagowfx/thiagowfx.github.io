---
title: "git reset --hard including submodules"
date: 2024-12-26T13:04:27-03:00
tags:
  - dev
---

**Problem statement**: Whenever I open [Rancher
Desktop](https://rancherdesktop.io/) it insists on modifying my shell rc files.
Make it stop!

bash:

```diff
# diff --git bash/.bash_profile bash/.bash_profile
index c3962b2..89f475b 100644
--- bash/.bash_profile
+++ bash/.bash_profile
@@ -7,3 +7,7 @@
 #
 # The following line sources .bashrc and is recommended by http://mywiki.wooledge.org/DotFiles
 [ -r ~/.bashrc ] && . ~/.bashrc
+
+### MANAGED BY RANCHER DESKTOP START (DO NOT EDIT)
+export PATH="/Users/thiago.perrotta/.rd/bin:$PATH"
+### MANAGED BY RANCHER DESKTOP END (DO NOT EDIT)
diff --git bash/.bashrc bash/.bashrc
index 7074bca..9ca8ffa 100644
--- bash/.bashrc
+++ bash/.bashrc
@@ -61,3 +61,7 @@ src_files "/etc/bash_completion"
 # Load user scripts and functions if existing. Order is important.
 # Corp config is handled as part of .bashrc.d.
 src_files "$HOME/.profile.d" "$HOME/.bashrc.d"
+
+### MANAGED BY RANCHER DESKTOP START (DO NOT EDIT)
+export PATH="/Users/thiago.perrotta/.rd/bin:$PATH"
+### MANAGED BY RANCHER DESKTOP END (DO NOT EDIT)
```

zsh:

```diff
diff --git etc/zsh/zshrc etc/zsh/zshrc
index efe5f79..02e0539 100644
--- etc/zsh/zshrc
+++ etc/zsh/zshrc
@@ -3959,3 +3959,7 @@ unfunction grml_status_feature
 # Local variables:
 # mode: sh
 # End:
+
+### MANAGED BY RANCHER DESKTOP START (DO NOT EDIT)
+export PATH="/Users/thiago.perrotta/.rd/bin:$PATH"
+### MANAGED BY RANCHER DESKTOP END (DO NOT EDIT)
```

You could say it's well-intentioned, but I think it's rude to change the
developer's rc files without telling them so, and without providing an opt-out
mechanism[^1].

Thus I wanted to revert their changes whenever I was done using Rancher Desktop.
This worked:

```shell
cd ~/.dotfiles && git reset --hard
cd vendor/grml-etc-core && git reset --hard
```

The second `git reset --hard` is needed because I employ a submodule for my
`zsh` config.

However, after doing this many times in a row, it became tedious. And somehow I
have the urge to improve this workflow...

{{< figure align="center" src="https://imgs.xkcd.com/comics/is_it_worth_the_time.png" link="https://xkcd.com/1205/" alt="Don't forget the time you spend finding the chart to look up what you save. And the time spent reading this reminder about the time spent. And the time trying to figure out if either of those actually make sense. Remember, every second counts toward your life total, including these right now." attr="XKCD Courtesy of Randall Munroe" >}}

Then I found out it's possible to do it with an one-shot command, via:

```shell
% git reset --hard --recurse-submodules
```

I knew of `--recurse-submodules` for `git clone`, but it never occurred to me it
would also exist for `git reset`.


[^1]: I ended up finding an opt-out mechanism, which isn't very intuitive to
    self-discover:
    [rancher-sandbox/rancher-desktop#7315](https://github.com/rancher-sandbox/rancher-desktop/issues/7315).
