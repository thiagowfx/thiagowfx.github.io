---
title: "Justfile groups"
date: 2026-02-21T22:51:55+01:00
tags:
  - dev
---

**TIL**: You can add [groups](https://just.systems/man/en/groups.html) to your
`Justfile.`:

> Recipes and modules may be annotated with one or more group names:

Before:

```
thiago.perrotta ~/.dotfiles git:master
❯ just --list
Available recipes:
    bootstrap                # Bootstrap environment (install packages, casks, and configure macOS)
    configure-macos          # Configure macOS defaults
    install                  # Install dotfiles
    install-brewfile         # Install dependencies from Brewfile
    stow                     # Stow all packages
    stow-lint                # Check for dangling symlinks
    unstow                   # Remove all symlinks
    update                   # Update git submodules, pre-commit hooks, and schemas
    update-git               # Update git submodules
    update-pre-commit        # Update pre-commit hooks
    update-schemas           # Update local JSON schemas
    xcode-command-line-tools # Install Xcode Command Line Tools
```

After:

```
thiago.perrotta ~/.dotfiles git:master
❯ just --list
Available recipes:
    [bootstrap]
    bootstrap                # Bootstrap environment (install packages, casks, and configure macOS)
    configure-macos          # Configure macOS defaults (keyboard, dock, security, etc.)
    install-brewfile         # Install dependencies from Brewfile (Homebrew packages and casks)
    xcode-command-line-tools # Install Xcode Command Line Tools

    [install]
    install                  # Install dotfiles (stow packages and bootstrap environment)

    [stow]
    stow                     # Stow all packages
    stow-lint                # Check for dangling symlinks
    unstow                   # Remove all symlinks

    [update]
    update                   # Update git submodules, pre-commit hooks, and schemas
    update-git               # Update git submodules
    update-pre-commit        # Update pre-commit hooks and run all hooks
    update-schemas           # Update local JSON schemas (Espanso, yamllint, etc.)
```

A typical diff looks like this:

```diff {filename="Justfile"}
-# Check for dangling symlinks
+[doc('Check for dangling symlinks')]
+[group('stow')]
 stow-lint:
     chkstow -t {{ target_dir }}

-# Remove all symlinks
+[doc('Remove all symlinks')]
+[group('stow')]
 unstow:
     stow -t {{ target_dir }} -d {{ _dotfiles_dir }} --delete {{ packages }}
```
