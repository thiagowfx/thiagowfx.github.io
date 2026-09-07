---
title: "pi: git-ai: trace code commits back to agent sessions"
url: https://perrotta.dev/2026/09/pi-git-ai-trace-code-commits-back-to-agent-sessions/
last_updated: 2026-09-07
---


[Git AI](https://github.com/git-ai-project/git-ai) records agent checkpoints in
[Git notes](https://git-scm.com/docs/git-notes)[^1], without changing commit
messages or repository files.

[^1]: A little known `git` feature.

In order to integrate it with [Pi](https://pi.dev/) we use an extension,
because Git AI must observe file and Bash tool calls:

```typescript
const GIT_AI_BIN = join(homedir(), '.git-ai', 'bin', 'git-ai');

const child = spawn(GIT_AI_BIN, ['checkpoint', 'pi', '--hook-input', 'stdin'], {
  stdio: ['pipe', 'ignore', 'ignore'],
});
```

The extension listens before and after each mutating call. It sends Pi session
ID, model, tool, working directory, and touched files to `git-ai checkpoint`.

In a shell script in my dotfiles, I configured `git-ai`:

```shell
# Git AI daemon receives Git Trace2 events through per-user socket.
if command -v git-ai >/dev/null 2>&1; then
  export GIT_TRACE2_EVENT="af_unix:stream:${GIT_AI_DAEMON_TRACE_SOCKET:-$HOME/.git-ai/internal/daemon/trace2.sock}"
  export GIT_TRACE2_EVENT_NESTING=0
fi
```

After restarting Pi, code attribution starts to appear alongside normal `git
blame` calls[^2]:

```shell
% git ai blame src/main.rs
442dfde2 (pi 2026-09-05 14:29:59 +0200 1) fn main() { println!("pi"); }
```

[^2]: Of course, the LLM decided to choose a Rust example to test the
    integration. _Of course_. It certainly wouldn't have been _my_ first choice.

The commit note contains the useful attribution / provenance snippet:

```text
"sessions": {
  "s_82565459b433c5": {
    "agent_id": {
      "tool": "pi",
      "id": "pi-extension-test",
      "model": "gpt-5.6-sol"
    }
  }
}
```

Now a suspicious line can lead from Git history to the exact Pi session. The
session ID can then subsequently be searched with [`fr`]({{< ref
"2026-09-01-agentsview-vs-fast-resume" >}}) or resumed in Pi.

Other useful commands with real examples:

```shell
% git ai show HEAD
STYLE.md
  s_f2908643b7ce0d::t_739223c8b9befd 12,29,48
---
{
  "schema_version": "authorship/3.0.0",
  "git_ai_version": "1.7.2",
  "base_commit_sha": "d225f5e635bbf5494574591580af8abf93da9480",
  "prompts": {},
  "sessions": {
    "s_f2908643b7ce0d": {
      "agent_id": {
        "tool": "pi",
        "id": "01a07acd-e9c7-759f-84b4-107f9ebc2556",
        "model": "gpt-5.6-sol"
      },
      "human_author": "Thiago Perrotta <{redacted_email}>"
    }
  }
}
```

```shell
% git log --show-notes=ai
commit d225f5e635bbf5494574591580af8abf93da9480 (HEAD -> master)
Author: Thiago Perrotta <{redacted_email}>
Date:   Mon Sep 7 09:40:01 2026 +0200

    docs: require problem statement questions

Notes (ai):
    STYLE.md
      s_f2908643b7ce0d::t_739223c8b9befd 12,29,48
    ---
    {
      "schema_version": "authorship/3.0.0",
      "git_ai_version": "1.7.2",
      "base_commit_sha": "d225f5e635bbf5494574591580af8abf93da9480",
      "prompts": {},
      "sessions": {
        "s_f2908643b7ce0d": {
          "agent_id": {
            "tool": "pi",
            "id": "01a07acd-e9c7-759f-84b4-107f9ebc2556",
            "model": "gpt-5.6-sol"
          },
          "human_author": "Thiago Perrotta <{redacted_email}>"
        }
      }
    }
```

