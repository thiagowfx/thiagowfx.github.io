# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Structure

- Blog posts live in `content/posts/` with naming pattern `YYYY-MM-DD-title.md`
- Hugo layouts and theme customizations in `layouts/`
- Static assets in `static/`
- Hugo configuration in `config.yml`
- Internal plans/notes in `plans/` with naming pattern `YYYY_MM_DD_DESCRIPTION.md` in SCREAMING_SNAKE_CASE (not served by Hugo)
- This is a Hugo-based blog using a custom fork of the bearblog theme

## Build Commands

- Start dev server: `just watch` (includes browser auto-open and navigation to changes)
- Start dev server without browser: `just watch false`
- Build for production: `just build`
- Create new post: `just new "post title"` (auto-generates filename with current date)
- Clean build artifacts: `just clean`
- Update dependencies: `just update` (updates git submodules and prek hooks)
- Ping search engines: `just ping` (notifies Google and Bing of sitemap changes)

## Test/Lint Commands

- Run prek hooks: `prek run --all-files`
- Lint specific file: `prek run --files <file>`
- Check links: `prek run markdown-link-check --files <file>` (expensive, runs manually)
- Run misspell check: `prek run misspell --files <file>` (manual stage only)
- Hugo build validation is included in prek hooks
- Build and test changes: `hugo` (always test changes before committing, especially Hugo template, shortcode, or config changes)

## Style Guidelines

- YAML: Use yamlfmt for consistent formatting
- HTML: Use prettier for formatting (excludes layouts/)
- Markdown:
  - No UTM parameters in links
  - No .md extension in internal Hugo links
  - Use keep-sorted directives to maintain sorted lists
  - Avoid personal emails, company references, and old domain names
- Images: Optimize PNGs with oxipng
- Follow Hugo's Markdown and frontmatter conventions
- Justfiles: Use format-justfile for consistent formatting

## Content Guidelines

- Blog post tags: Use common tags like `bestof`, `coding`, `dev`, `linux`, `meta`, `pt`, `privacy`, `serenity`
- Commit messages for new posts: `git commit -m "new post: title"`
- Posts use frontmatter with title, date, and tags
- No AI assistance is used for content creation or editing
- Internal plans, notes, and summaries: Create in `plans/` directory with naming pattern `YYYY_MM_DD_DESCRIPTION.md` in SCREAMING_SNAKE_CASE (never in repo root)

## Blog Post Writing Style

- **Structure**: Problem-solution oriented. Open with a bold **Problem statement**, then context, then solution, then brief closing
- **Tone**: Direct, concise, conversational first-person. Casual but technical ("That simply works™", "Yet, here we are")
- **Length**: Short to medium (40–80 lines typical). Don't pad with filler
- **Code-heavy**: Show before/after YAML/shell snippets, actual command output, and diffs rather than explaining in prose
- **Show the journey**: When relevant, show what didn't work before showing what did
- **Links**: Reference official docs, GitHub issues/PRs, and related blog posts (using `{{< ref "..." >}}` Hugo shortcodes for internal links)
- **Blockquotes**: Use blockquotes for quoting documentation or tool output
- **Closing**: Keep it brief — a sentence or two of reflection, not a summary of the post
- **No fluff**: No introductions like "In this post we'll explore...". Jump straight into the problem
- **Title style**: Lowercase, often namespaced (e.g. "pre-commit: feature name")
