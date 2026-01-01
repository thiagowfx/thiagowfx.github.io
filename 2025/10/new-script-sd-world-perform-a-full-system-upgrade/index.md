
[Previously]({{< ref "2024-01-28-sd-world" >}}).

> Whenever I want to upgrade any one of my systems, I run `sd-world`.

Now the script has evolved, being [hosted](https://github.com/thiagowfx/pancake/blob/9b2cc8c6df6103d4ab1457e30353fe0711290aa2/sd-world/sd-world.sh) in [pancake](https://github.com/thiagowfx/pancake):

- it handles interruptions (Ctrl-C) more efficiently (it was my biggest gripe)
- the output is more user-friendly

Preview:

```
% ./sd_world.sh
Starting system upgrade...

Detected macOS system

Upgrading Homebrew...
==> Updating Homebrew...
Already up-to-date.
==> Upgrading 2 outdated packages:
node@18, python@3.11
==> Upgrading node@18 18.17.0 -> 18.19.0
==> Upgrading python@3.11 3.11.6 -> 3.11.7
✓ Homebrew upgrade completed successfully

Upgrading Mac App Store...
✓ Mac App Store upgrade completed successfully

Upgrading System Updates...
Software Update Tool

Finding available software
No new software available.
✓ System Updates upgrade completed successfully

Upgrading Claude Code...
Checking for updates...
claude-code v0.8.2 → v0.8.3 (latest)
Updated successfully! 🎉
✓ Claude Code upgrade completed successfully

Upgrading myrepos...
mr update: /Users/username/repos/project1
From github.com:user/project1
   abc1234..def5678  main       -> origin/main
Updating abc1234..def5678
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

mr update: finished (1 ok)
✓ myrepos upgrade completed successfully

Upgrade Summary:
Successfully upgraded: 5/5 package managers
All package managers upgraded successfully!
```

