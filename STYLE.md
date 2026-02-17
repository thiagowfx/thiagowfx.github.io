# Blog Post Writing Style

Detailed style guide derived from analysis of existing posts. See `CLAUDE.md` for repo conventions.

## Structure

- **Frontmatter**: Minimal YAML — `title`, `date`, and `tags` only. No description, summary, images, or categories.
- **Title**: Always lowercase. Often namespaced with a colon (e.g. "pre-commit: pin dependencies with --freeze", "starship: github PR prompt").
- **Length**: 15–85 lines of markdown, most under 50. Strong preference for brevity.
- **Sections**: Most posts have no headings at all. Structure is implicit and flows naturally:
  1. Optional `[Previously]({{< ref "..." >}}).` backlink to related earlier posts
  2. A bold **Problem statement** or **Today I learned** opener (one sentence)
  3. Short prose paragraph setting context (1–3 sentences)
  4. Code block(s) showing the solution, command output, or diff
  5. Short closing remark (0–2 sentences), sometimes a link to an upstream issue
- **Code ratio**: Code blocks (shell commands, diffs, YAML, config files) constitute 50–80% of the content. Let the code speak for itself.

## Tone and Voice

- Direct and casual first person, as if talking to a peer developer ("I couldn't resist creating a pre-commit hook for this", "Oh well.", "Can't do.")
- Understated confidence. Present solutions matter-of-factly, without overselling.
- Personal but not overly so. Mention motivation briefly and move on.
- No hedging. Don't say "you might want to consider" — say "Here's how." or "Use X."
- Never say "In this post, I will..." or "Have you ever wondered..." or "Let me walk you through..."

## Technical Content

- **Show, don't explain**: State the problem in one bold sentence → show the actual command/config/code → show the actual output → optionally show what didn't work first.
- **Real output**: Paste actual terminal output, git diffs, commit hashes, file paths. Not sanitized toy examples.
- **Shell prompt**: `%` for zsh, `$` for bash.
- **Blockquotes**: Use `>` for quoting external documentation or project descriptions, not paraphrasing.
- **Links to upstream**: Regularly link to GitHub issues, PRs, official docs, and related blog posts.
- **Internal cross-references**: Use `{{< ref "..." >}}` Hugo shortcodes.

## Storytelling

- **Understated pride**: Show the git shortlog or diff as proof, not lengthy explanations of significance.
- **Brief personal context, then move on**: One paragraph of backstory at most.
- **Journey over destination** (when relevant): Show what was tried first, why it failed, then what worked. Always compact.
- **Series linking**: Start with `[Previously]({{< ref "..." >}}).` — a single word link. No recaps.
- **Tools as extensions of self**: "I needed X, so I built Y."

## Openings

Use one of these patterns:

- **Bold problem statement**: `**Problem statement**: [one sentence].` — most common
- **TIL**: `**Today I learned**: [tool/feature/technique].`
- **Previously link**: `[Previously]({{< ref "..." >}}).` — for follow-up posts
- **Declarative statement**: "I just added X." / "Y has been released."
- **Jump straight in**: No preamble whatsoever

Never: "In this post, I will...", "Have you ever wondered...", "Let me walk you through..."

## Closings

- A single sentence of reflection, or a link to an upstream issue, or nothing at all (post ends after the last code block)
- Never: "In conclusion...", "To summarize...", "I hope this was useful..."
