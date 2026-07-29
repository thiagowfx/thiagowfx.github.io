---
title: "pi: change directories mid-session"
url: https://perrotta.dev/2026/07/pi-change-directories-mid-session/
last_updated: 2026-07-29
---


**Today I learned**: [pi](https://pi.dev/) 0.82.1 cannot change its working
directory mid-session.

The interactive shell syntax looks tempting, but `!` and `!!` run commands in a
child process. `cd` ends with that process; Pi keeps the session's original cwd.
There is no built-in `/cd` either:

```shell
% pi --version
0.82.1
% docs="$(brew --prefix pi-coding-agent)/libexec/lib/node_modules/@earendil-works/pi-coding-agent/docs"
% rg -n 'ctx\.(newSession|switchSession|changeCwd|switchCwd)' "$docs/extensions.md"
1109:### ctx.newSession(options?)
1117:const result = await ctx.newSession({
1187:### ctx.switchSession(sessionPath, options?)
1192:const result = await ctx.switchSession("/path/to/session.jsonl", {
1220:      await ctx.switchSession(choice, {
1247:    await ctx.newSession({
1262:    await ctx.newSession({
% rg -n '^\| `/[^|]+`' "$docs/usage.md" | tail -5
56:| `/share` | Upload as private GitHub gist with shareable HTML link |
57:| `/reload` | Reload keybindings, extensions, skills, prompts, themes, and context files |
58:| `/hotkeys` | Show all keyboard shortcuts |
59:| `/changelog` | Display version history |
60:| `/quit` | Quit pi |
```

This has been requested several times upstream:

```shell
% for n in 2102 2992 3921 4423 6997; do
    gh issue view "$n" --repo earendil-works/pi \
      --json number,title,state,stateReason \
      --jq '[.number, .title, .state, .stateReason] | @tsv'
  done
2102	Allow extensions to change cwd at runtime	CLOSED	COMPLETED
2992	Allow session CWD to be changed	CLOSED	COMPLETED
3921	Feature request: ExtensionCommandContext.changeCwd() for lightweight cwd switching	CLOSED	NOT_PLANNED
4423	Add command API to switch cwd	CLOSED	COMPLETED
6997	Windows Bash inside Pi not working properly	CLOSED	NOT_PLANNED
```

The exact `/cd` proposal lives in
[#3921](https://github.com/earendil-works/pi/issues/3921). The maintainer
responses on [#2102](https://github.com/earendil-works/pi/issues/2102),
[#2992](https://github.com/earendil-works/pi/issues/2992), and
[#4423](https://github.com/earendil-works/pi/issues/4423) capture the trade-off:

```text
#2102 @badlogic: use case makes sense, however, it can be done by overriding the built-in tools to support cwd changes.
#2992 @badlogic: setting a new cwd in a session is not great, as a bunch of things need to be rewired. currently unsupported.
#4423 @badlogic: this is part of the big refactor work and will be available in the new extension api.
```

That last API still is not exposed in 0.82.1. Changing cwd means rebuilding tools,
project settings, extensions, skills, context files, autocomplete, footer state,
and session storage—not merely calling `process.chdir()`.

For now, the boring path is the supported one:

```shell
/quit
% cd ~/Workspace/perrotta.dev
% pi
```

Session cwd is a runtime boundary. Oh well.

- - -

🤖 *Drafted with `/bloggify`.*

