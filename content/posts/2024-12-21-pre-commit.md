---
title: "Pre-commit"
date: 2024-12-21T23:24:23-03:00
tags:
  - bestof★
  - dev
---

[pre-commit](https://pre-commit.com/) is a CI framework for `git`.
For those who are used to google3 tooling: it's akin to the configuration part of `TAP Presubmit`.

You can plug in linters, formatters, code analyzers...pretty much any tool or binary that analyzes files, potentially emitting errors whenever style or policy violations occur, is a potential good fit for a pre-commit hook.

Once properly configured the whole pipeline can be run locally with `pre-commit run`. By default, only the stashed files are inspected. In order to consider every file in the repository, pass `--all-files`. Modified files that were not yet `git add`ed are not included.

When configuring CI, the same command is used in cloud pipelines: it's a single configuration for both local and CI runs.

All the configuration lives in a single YAML file, `.pre-commit-config.yaml`, in the repository root.

Because it is written in Python, the whole ecosystem around the language is very well supported, first-class. That said, many other languages are also supported. For the ones that are not, there is a escape hatch – the "system" language.

Here is an example `.pre-commit-config.yaml` file – the one for this blog:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      # keep-sorted start
      - id: check-executables-have-shebangs
      - id: check-symlinks
      - id: check-yaml
      - id: detect-private-key
      - id: pretty-format-json
        args:
          - --autofix
          - --no-sort-keys
      - id: sort-simple-yaml
      - id: trailing-whitespace
        # keep-sorted end
  - repo: https://github.com/google/keep-sorted
    rev: v0.5.1
    hooks:
      - id: keep-sorted
  - repo: https://github.com/google/yamlfmt
    rev: v0.14.0
    hooks:
      - id: yamlfmt
  - repo: https://github.com/codespell-project/codespell
    rev: v2.3.0
    hooks:
      - id: codespell
        exclude: ^content/posts/(2014|2015|2016)|content/posts/2024-07-09-kubectl-get-secret-with-jsonpath-add-newline.md|content/posts/2024-06-27-a-little.md
        args:
          # keep-sorted start
          - -L=DeVault
          - -L=als
          - -L=ist
          - -L=sive
          # keep-sorted end
  - repo: https://github.com/jmlrt/check-yamlschema
    rev: v0.0.4
    hooks:
      - id: check-yamlschema
```

Repository versions are always pinned. You would think this is tedious, but it's highly desirable for reproducibility, and they can all be automatically updated with `pre-commit autoupdate`.

To run only a single hook: `pre-commit run [--all-files] codespell`.

How do you install `pre-commit` in the first place? Use `pip`, or `brew` (macOS), or your favorite package manager.

Hooks are configured in `.pre-commit-hooks.yaml` files in their respective repositories. [Here](https://github.com/codespell-project/codespell/blob/main/.pre-commit-hooks.yaml) is an example, from `codespell`:

```yaml
- id: codespell
  name: codespell
  description: Checks for common misspellings in text files.
  entry: codespell
  language: python
  types: [text]
```

...it's just metadata that teaches the framework to run the `codespell` python file, and that it should only run in text files.

The definition of what a text file is lives in the [identify](https://github.com/pre-commit/identify) pre-commit library, [this](https://github.com/pre-commit/identify/blob/main/identify/extensions.py) file has all the mappings. You could also specify `shell`, for example.

What if an extension isn't supported? Instead of using `types:`, use `file:` with a regex pattern to match, such as `\.sh$`.

What if an upstream tool does not have a `.pre-commit-hooks.yaml` file? I wrote a [post]({{< ref "2024-12-17-pre-commit-create-hooks-for-unsupported-tools.md" >}}) with a workaround wherein you can define your own.

How do you try out new hooks? One way is to use [`pre-commit try-repo`]({{< ref "2024-11-26-pre-commit-try-repo.md" >}}). Another way is to add them to your config and then run each hook individually.

Are there similar tools? There's [`husky`](https://typicode.github.io/husky/), but it's too nodejs / web centric. I like `pre-commit.com` better.

Any git repository that is owned my multiple people and need to follow well-defined practices and conventions should, in general, adopt a pre-commit framework. `pre-commit.com` is one possible solution that is great at its job.

## References

- https://whynothugo.nl/journal/2023/01/12/notes-on-pre-commit/
