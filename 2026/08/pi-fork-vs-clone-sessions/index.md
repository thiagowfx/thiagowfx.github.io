---
title: "pi: fork vs clone sessions"
url: https://perrotta.dev/2026/08/pi-fork-vs-clone-sessions/
last_updated: 2026-08-17
---


**Problem statement**: split a running Pi conversation / session into a second
independent one whilst keeping the original.

Pi has three similarly named albeit distinct operations:

```text
/fork
/clone
pi --fork <path|id>
```

`/fork` opens a selector for an earlier user message, copies the active path up
to the message's parent into a new session, and puts the selected prompt back in
the editor. This is for changing an earlier request.

`/clone` copies the current active root-to-leaf path into a new session and
switches the current Pi process to it. The old session file remains unchanged;
retrieve it with `/resume`, or note its ID first and open it directly:

```text
/session
/clone
```

```shell
% pi --session 019feb2b
```

The CLI spelling does something subtly different:

```shell
% pi --help | grep -A5 -- '--session <path'
  --session <path|id>            Use specific session file or partial UUID
  --session-id <id>              Use exact project session ID, creating it if missing
  --fork <path|id>               Fork specific session file or partial UUID into a new session
  --session-dir <dir>            Directory for session storage and lookup
  --no-session                   Don't save session (ephemeral)
  --name, -n <name>              Set session display name
```

`pi --fork` copies the complete source session file, including all branches,
then opens the copy in a new Pi process. The running source process is untouched:

```text
# current Pi
/session
```

```shell
# second terminal, same project
% pi --fork 019feb2b
```

It's easier to do so if we add the session ID to the Pi status bar. Pi loads
extensions from `~/.pi/agent/extensions/`, so I have
[this one](https://github.com/thiagowfx/.dotfiles/blob/e08ea70fbec9decd9059817119ef715a34d8c12e/pi/.pi/agent/extensions/session-id.ts):

```typescript
// ~/.pi/agent/extensions/session-id.ts
import type { ExtensionAPI, ExtensionContext } from "@earendil-works/pi-coding-agent";

export function updateSessionIdStatus(ctx: ExtensionContext): void {
  const sessionId = ctx.sessionManager.getSessionId();
  ctx.ui.setStatus("session-id", ctx.ui.theme.fg("dim", `sid:${sessionId}`));
}

export default function (pi: ExtensionAPI) {
  pi.on("session_start", async (_event, ctx) => updateSessionIdStatus(ctx));
}
```

For a linear session, `pi --fork` and `/clone` produce equivalent conversation
context. Once a session has branches, `/clone` extracts only the active branch;
`pi --fork` preserves the full tree.

Pi sessions are
[JSONL trees](https://github.com/earendil-works/pi-mono/blob/main/packages/coding-agent/docs/sessions.md),
so none of these operations mutate the source history. For splitting one live
conversation into two live processes, use `pi --fork <id>`.

