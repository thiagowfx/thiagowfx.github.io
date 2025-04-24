# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build Commands
- Start dev server: `just watch`
- Build for production: `just build`
- Create new post: `just new "Post Title"`
- Clean build artifacts: `just clean`
- Update dependencies: `just update`

## Test/Lint Commands
- Run pre-commit hooks: `pre-commit run --all-files`
- Lint specific file: `pre-commit run --files <file>`
- Check links: `pre-commit run markdown-link-check --files <file>`

## Style Guidelines
- YAML: Use yamlfmt for consistent formatting
- Markdown:
  - No UTM parameters in links
  - No .md extension in internal Hugo links
  - Use keep-sorted directives to maintain sorted lists
- Images: Optimize PNGs with oxipng
- Follow Hugo's Markdown and frontmatter conventions