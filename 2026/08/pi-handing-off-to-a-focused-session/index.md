---
title: "pi: handing off to a focused session"
url: https://perrotta.dev/2026/08/pi-handing-off-to-a-focused-session/
last_updated: 2026-09-03
---


[Previously]({{< ref "2026-08-17-pi-fork-vs-clone-sessions" >}}).

**Disclaimer**: This was a failed experiment.
I am including it here anyway, for completeness.

## Handoff

**Problem statement**: move a running Pi task into a fresh, focused session
without losing the way back.

I wanted [Amp](https://ampcode.com/)'s handoff workflow in Pi, so I vendored the
`handoff` and `session_query` pieces of
[`pasky/pi-amplike`](https://github.com/pasky/pi-amplike) as a local package:

```shell
% git show --stat --oneline 77af167
77af167 Add Amp-like handoff package
 pi/.pi/README.md                                   |   2 +
 pi/.pi/agent/local/handoff-amp/LICENSE             |  21 +
 pi/.pi/agent/local/handoff-amp/README.md           |  28 ++
 .../agent/local/handoff-amp/extensions/handoff.ts  | 553 +++++++++++++++++++++
 .../local/handoff-amp/extensions/lib/mode-utils.ts | 127 +++++
 .../local/handoff-amp/extensions/session-query.ts  | 198 ++++++++
 pi/.pi/agent/local/handoff-amp/package.json        |  17 +
 .../handoff-amp/skills/session-query/SKILL.md      |  35 ++
 pi/.pi/agent/settings.json                         |   1 +
 9 files changed, 982 insertions(+)
```

From the editor, `/handoff` accepts a goal and optional mode or model:

```text
/handoff execute phase one of the plan
/handoff -mode rush execute phase one of the plan
/handoff -model anthropic/claude-haiku-4-5 check other places that need this fix
```

The extension serializes the current branch, asks the model for a focused
context summary, and includes the source session path in the new prompt:

```typescript
// ~/.pi/agent/local/handoff-amp/extensions/handoff.ts
const currentSessionFile = ctx.sessionManager.getSessionFile();

if (currentSessionFile) {
  finalPrompt = `${goal}\n\n/skill:session-query\n\n**Parent session:** \`${currentSessionFile}\`\n\n${result}`;
}
```

The important part: handoff does not open a second Pi process. The command
replaces the active session inside the current process:

```typescript
const newSessionResult = await cmdCtx.newSession({
  parentSession: currentSessionFile,
});
```

When the agent invokes the `handoff` tool instead, Pi waits for the current turn
to finish, then changes the session file:

```typescript
pi.on("agent_end", (_event, ctx) => {
  if (!pendingHandoff) return;

  const { prompt, parentSession } = pendingHandoff;
  (ctx.sessionManager as any).newSession({ parentSession });
});
```

```text
Handoff initiated. The session will switch after the current turn completes.
```

Same TUI, new active session. The old session remains saved as the parent. To
return to it, open the session picker:

```text
/resume
```

Or start Pi with that picker from the shell:

```shell
% pi -r
```

`/tree` is not the way back: it navigates branches inside the current session
file. Handoff creates another session file, so `/resume` is the matching
operation.

## Conclusion

**Human voice**: Guess what, after doing all of the above I came to the
conclusion that this is a cumbersome workflow. No wonder the Amp folks
[seem](https://www.nicolaygerold.com/posts/kirby-is-eating-context-engineering)
to have reached the same conclusion:

> Handoff is another one of my features that I expect to die soon.

I am ditching it.

A better workflow is to backtrack the session tree with `/tree` or `Esc Esc`.

