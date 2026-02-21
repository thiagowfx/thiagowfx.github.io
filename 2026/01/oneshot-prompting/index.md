
I just wrote [this post]({{< ref "2026-01-03-neovim-inline-git-hunk-control"
>}}) about `neovim` and `git` hunks.

In it I mentioned various git repositories, but did not link to them whilst
writing the post. Ah, these lazy engineers.

Why not ask the LLM to link to them for me, especially because they are popular
projects? Then I had the idea to try to do it without opening an interactive
coding agent as I'm used to (think of Claude Code, OpenAI Codex, Amp Code, Open
Code).

[Amp Code](https://ampcode.com/):

```shell
% amp -x "add github repository links to git tuis in this post: @content/posts/2026-01-03-neovim-inline-git-hunk-control.md"
Error: Insufficient credit balance.
```

```shell
% amp --mode free -x "add github repository links to git tuis in this post: @content/posts/2026-01-03-neovim-inline-git-hunk-control.md"
Error: Execute mode is not permitted with --mode 'free'
```

Oh. Okay.

[Pi](https://github.com/badlogic/pi-mono) + Gemini 3 Pro Preview:

```shell
% pi -p "add github repository links to git tuis in this post: @content/posts/2026-01-03-neovim-inline-git-hunk-control.md"
I have added the requested GitHub repository links for the Git TUIs (gitui, tig, lazygit) in the blog post `content/posts/2026-01-03-neovim-inline-git-hunk-control.md`.

Here are the changes made:
- `gitui` -> `[gitui](https://github.com/extrawurst/gitui)`
- `tig` -> `[tig](https://github.com/jonas/tig)`
- `lazygit` -> `[lazygit](https://github.com/jesseduffield/lazygit)`
```

Great job! Let's `git stash` it and try again with other agents I use, for the
sake of completeness. I'll use the same prompt.

[Claude Code](https://claude.com/product/claude-code) + Sonnet 4.5:

```shell
% claude -p 'add github repository links to git tuis in this post: @content/posts/2026-01-03-neovim-inline-git-hunk-control.md'
I need your permission to edit the file `content/posts/2026-01-03-neovim-inline-git-hunk-control.md` to add GitHub repository links to the git TUIs (gitui, tig, and lazygit).
```

```shell
claude --dangerously-skip-permissions -p 'add github repository links to git tuis in this post: @content/posts/2026-01-03-neovim-inline-git-hunk-control.md'
Perfect! I've added GitHub repository links to all three git TUIs mentioned in the post:

1. **gitui** → https://github.com/extrawurst/gitui
2. **tig** → https://github.com/jonas/tig
3. **lazygit** → https://github.com/jesseduffield/lazygit

The links are now properly formatted as Markdown links in the post at `content/posts/2026-01-03-neovim-inline-git-hunk-control.md:52-54`.
```

[OpenAI Codex](https://openai.com/codex/) + GPT 5.1 Codex Max:

```shell
% codex exec "add github repository links to git tuis in this post: @content/posts/2026-01-03-neovim-inline-git-hunk-control.md"
[...lots of output...]
-- **gitui**
-- tig
-- lazygit
+- **[gitui](https://github.com/extrawurst/gitui)**
+- [tig](https://github.com/jonas/tig)
+- [lazygit](https://github.com/jesseduffield/lazygit)

 ...or graphically with IDEs with as VSCode.


tokens used
7,432
- Added GitHub repository links for gitui, tig, and lazygit in `content/posts/2026-01-03-neovim-inline-git-hunk-control.md` so readers can jump to each TUI.
- No tests run (doc-only change).
```

[Open Code](https://opencode.ai/) + GLM 4.7 Free:

```shell
% opencode --model opencode/glm-4.7-free run "add github repository links to git tuis in this post: @content/posts/2026-01-03-neovim-inline-git-hunk-control.md"
|  Read     content/posts/2026-01-03-neovim-inline-git-hunk-control.md
|  Search   Web search: tig git tui github repository
|  Search   Web search: gitui github repository
|  Search   Web search: lazygit github repository
|  Edit     content/posts/2026-01-03-neovim-inline-git-hunk-control.md

Done. Added GitHub links for gitui, tig, and lazygit to the post.
```

```shell
% git --no-pager diff
diff --git content/posts/2026-01-03-neovim-inline-git-hunk-control.md content/posts/2026-01-03-neovim-inline-git-hunk-control.md
index 1a6465f3b..3324a71c7 100644
--- content/posts/2026-01-03-neovim-inline-git-hunk-control.md
+++ content/posts/2026-01-03-neovim-inline-git-hunk-control.md
@@ -49,9 +49,9 @@ What now>

 It's also possible to manage hunks via git TUIs (=from the terminal) such as:

-- **gitui**
-- tig
-- lazygit
+- **[gitui](https://github.com/gitui-org/gitui)**
+- [tig](https://github.com/jonas/tig)
+- [lazygit](https://github.com/jesseduffield/lazygit)

 ...or graphically with IDEs with as VSCode.
```

Guess which one is my favorite for simple tasks?

