
These days, Claude Code warns you when you're running [out of
context](https://claudelog.com/faqs/what-is-claude-code-auto-compact/):

> Context left until auto-compact: 5%

> How Auto-Compact Works
>
> When your conversation approaches the context window limit, Claude Code
automatically:
>
> 1. Analyzes the conversation to identify key information worth preserving

> 2. Creates a concise summary of previous interactions, decisions, and code
>    changes

> 3. Compacts the conversation by replacing old messages with the summary

> 4. Continues seamlessly with the preserved context

It's possible to run `/compact` manually to compact the context sooner[^1].

[^1]: Let the machine do the garbage collection though! Why would you bother to
    do so manually?

