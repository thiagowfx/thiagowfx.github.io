
My current workflow to manage shell history is simple, I have this config in
my `~/.zshrc.d/`

```shell
# fzf: fuzzy file finder
if (( $+commands[fzf] )); then
        # alpine/arch, debian
        src_files {/usr/share/fzf,/usr/share/doc/fzf/examples}/{completion,key-bindings}.zsh

        # brew
        if (( $+commands[brew] )); then
                src_files "$(brew --prefix)"/opt/fzf/shell/{completion,key-bindings}.zsh
        fi
fi
```

[`fzf`](https://github.com/junegunn/fzf) does it all.

I hit `C-r` and get fuzzy finding over all my `history`, this has been
overpowering my productivity for ages, likely since university.

Then I found out I could go one step further.

Enter [Atuin](https://atuin.sh):

> Making your shell magical
>
> Sync, search and backup shell history with Atuin.

Installing `atuin` is simple: it's available [everywhere](https://repology.org/project/atuin/versions):

```shell
brew install atuin
```

Configuring `atuin` is simple, start by adding this snippet to your `/.zshrc`
file[^1]:

```shell
# atuin: https://docs.atuin.sh/
(( $+commands[atuin] )) && eval "$(atuin init zsh --disable-up-arrow)"
```

Now run `atuin import auto` to import your shell history entries to `atuin`.

By default, `atuin init` binds both `C-r` and the up arrow. I find the up
arrow binding disruptive.

I want my workflow to stay as close as possible to `fzf` `C-r`.
[`--disable-up-arrow`](https://docs.atuin.sh/configuration/key-binding/#disable-up-arrow)
is essential for that.

Pressing `C-r` will invoke a fuzzy find window that behaves similarly to `fzf`,
though it's more powerful. It's hard to describe, you must try it out.

This is enough to make the migration. Which makes me feel bad for having
procrastinated for so long to do so. Trying out `atuin` has been in my TODO list
for ages!

There's an optional step of syncing your history with their remote cloud. Or
with your own, because there's an option of self-hosting a server (`atuin server
start`). Self-hosting is optimal, but trying out their cloud first to get a feel
of the sync experience is reasonable.

Syncing happens every hour by default, but this is configurable.

See [sync docs](https://docs.atuin.sh/reference/sync/):

> Atuin can back up your history to a server, and use this to ensure multiple
> machines have the same shell history. This is all encrypted end-to-end, so the
> server operator can never see your data!
>
> Anyone can host a server (try atuin server start, more docs to follow), but I
> host one at https://api.atuin.sh. This is the default server address, which
> can be changed in the config. Again, I cannot see your data, and do not want
> to.

You can create a `~/.config/atuin/config.toml` to customize `atuin`. I added
this:

```toml
## With workspace filtering enabled, Atuin will filter for commands executed
## in any directory within a git repository tree (default: false).
##
## To use workspace mode by default when available, set this to true and
## set filter_mode to "workspace" or leave it unspecified and
## set search.filters to include "workspace" before other filter modes.
# workspaces = false
workspaces = true

## which filter mode to use when atuin is invoked from a shell up-key binding
## the accepted values are identical to those of "filter_mode"
## leave unspecified to use same mode set in "filter_mode"
# filter_mode_shell_up_key_binding = "global"
filter_mode_shell_up_key_binding = "directory"

## Defaults to true. If enabled, upon hitting enter Atuin will immediately execute the command. Press tab to return to the shell and edit.
# This applies for new installs. Old installs will keep the old behaviour unless configured otherwise.
# Similarly to fzf C-r
enter_accept = false

## Defaults to "emacs".  This specifies the keymap on the startup of `atuin
## search`.  If this is set to "auto", the startup keymap mode in the Atuin
## search is automatically selected based on the shell's keymap where the
## keybinding is defined.  If this is set to "emacs", "vim-insert", or
## "vim-normal", the startup keymap mode in the Atuin search is forced to be
## the specified one.
# keymap_mode = "auto"
keymap_mode = "vim-insert"
```

`enter_accept` is an important tweak to resemble `fzf`. By default, pressing
Enter when looking up history entries in `atuin` will automatically execute the
command. In `fzf` you have an opportunity to edit/tweak the command before
execution, which is what I prefer. Set `enter_accept = false` to achieve the
same behavior in `atuin`.

`atuin` has an option to manage
[dotfiles](https://docs.atuin.sh/guide/dotfiles/):

> While Atuin started as a tool for syncing and searching shell history, we are
> building tooling for syncing dotfiles across machines, and making them easier
> to work with.
>
> At the moment, we support managing and syncing of shell aliases and
> environment variables - with more coming soon.

...but I don't feel the need to use this.

The magic of `atuin`, when using multiple computers is its shell history
synchronization. Picking up the slack in my personal computer would reveal my
work computer history and vice-versa. In some environments this is very
welcome!

Also cool: `stats` for free:

```shell
% atuin stats
[▮▮▮▮▮▮▮▮▮▮] 4540 git commit
[▮▮▮▮▮▮    ] 3062 ack
[▮▮▮▮▮     ] 2636 vim
[▮▮        ] 1304 cd
[▮▮        ] 1240 fd
[▮▮        ] 1186 tsh
[▮▮        ]  915 grep
[▮▮        ]  913 just
[▮         ]  822 git add
[▮         ]  818 git nb
Total commands:   29464
Unique commands:  20610
```

Query past entries with a SQL-like CLI:

```shell
% atuin search --exit 0 --after="4 months ago" "^skopeo"
```

Clearly I'm a die-hard [`ack`](https://beyondgrep.com/) fan. Will I ever switch
to [`rg`](https://github.com/BurntSushi/ripgrep)?

[`just`](https://just.systems/) is starting to become part of my core tool belt.

**See also**: [Tech
Talk](https://archive.fosdem.org/2023/schedule/event/rust_atuin_magical_shell_history_with_rust/),
including
[slides](https://archive.fosdem.org/2023/schedule/event/rust_atuin_magical_shell_history_with_rust/attachments/slides/5735/export/events/attachments/rust_atuin_magical_shell_history_with_rust/slides/5735/Atuin_FOSDEM_1.pdf).

Next chapter: [Atuin Desktop](https://github.com/atuinsh/desktop).

[^1]: `bash`, `fish`, `xonsh` are also supported at the time of this writing.

