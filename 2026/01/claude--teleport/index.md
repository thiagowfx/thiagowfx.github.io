
After starting a coding session on the web with [Claude Code on
Web](https://code.claude.com/docs/en/claude-code-on-the-web)[^1], you can [resume it
in the
terminal](https://code.claude.com/docs/en/claude-code-on-the-web#from-web-to-terminal)
with the traditional Claude Code CLI app by running `claude --teleport`.

Without arguments, it prompts you to interactively choose an existing session to
resume:

```
 Select a session to resume:

   Updated  Session Title
 ❯ 1. 52m ago  Migrate secrets from Gringotts to AWS Secrets Manager
   2. 53m ago  Plan Hoth integration with dual provider OIDC
   3. 54m ago  Add Strangereal terraform state bucket standalone project
   4. 2w ago   Write a CLAUDE.md
   5. 1mo ago  Address review comments on pull request 42123
```

With a provided session ID argument, the session is immediately resumed.

The docs mention the existence of the `/teleport` command within Claude Code but I
could not find it in my instance (version v2.1.4).

This [workflow](https://xcancel.com/bcherny/status/2007179832300581177) ("start
on your phone, resume later on your computer afterwards") is starting to become
popularized.

[^1]: https://claude.ai/code

