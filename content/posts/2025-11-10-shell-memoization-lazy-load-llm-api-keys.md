---
title: "Shell memoization: lazy-load LLM API keys"
date: 2025-11-10T13:55:56+01:00
tags:
  - bestof
  - dev
---

**Problem statement**: Given LLM keys shell environment variables:

- `ANTHROPIC_API_KEY`
- `GEMINI_API_KEY`
- `OPENAI_API_KEY`

Export them only when they are needed.

When are they needed? If I launch any one of these binaries:

- `llm` (generic)
- `aider` (generic)
- `gemini` (provider-specific: Google)
- `codex` (provider-specific: OpenAI)
- `claude` (provider-specific: Anthropic)

I added the following snippet in my shell profile:

```shell
# Lazy-load API keys only when needed to avoid shell startup delay
if command -v llm &>/dev/null; then
        _load_api_keys() {
                export ANTHROPIC_API_KEY="$(command llm keys get anthropic)"
                export GEMINI_API_KEY="$(command llm keys get gemini)"
                export OPENAI_API_KEY="$(command llm keys get openai)"
                # Redefine itself to be a no-op after first call
                _load_api_keys() { :; }
        }

        # Wrap all AI CLI commands to auto-load keys
        for cmd in claude llm aider codex gemini; do
                command -v $cmd &>/dev/null && eval "${cmd}() { _load_api_keys; command ${cmd} \"\$@\"; }"
        done
fi
```

The keys are loaded via `llm keys get`. This is not secure, but it is practical.
A more secure approach would be to read the credentials directly from a password
manager. This trade-off is acceptable in the environment I am currently
operating on, but I would not recommend it as an universal approach.

A temporary `_load_api_keys` shell function is defined. The first time it is
executed, it `export`s each one of the LLM API keys. From the second time
onwards it will be a no-op, thanks to `:`. In bash/zsh we can redefine a
function from within itself thanks to dynamic scoping. Wild.

Last but not least: I wrapped up ("decorated" in function parlance) all
LLM-related commands with a shell function that runs `_load_api_keys` before
invoking the original command.

This approach is elegant and easy to maintain.

My initial implementation had been more fine-grained: `ANTHROPIC_API_KEY` would
drive `claude`, `llm` and `aider`, but not `gemini` and `codex`, and so on.
Ultimately I decided that the additional complexity of mapping individual
providers optimally is not warranted.

Why is this memoization necessary in the first place?

My shell (`zsh`) startup was significantly slow before this change,
`O(seconds)`. Each call to `llm keys get` takes about half a second in my
machine. I do not think it's acceptable to wait for 2s before having your shell
readily available with a prompt.

Before this approach, I had used
[`zsh-defer`](https://github.com/romkatv/zsh-defer) to delay populating the API
keys. However, this has only _deferred_ (_cof_) my problems. The startup delay
was still noticeable.
