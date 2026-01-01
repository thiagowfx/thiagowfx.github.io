
[mdsh](https://github.com/zimbatm/mdsh), a markdown shell pre-processor;

> The mdsh project describes a Markdown language extension that can be used to
> automate some common tasks in README.md files. Quite often I find myself
> needing to embed a snippet of code or markdown from a different file. Or I
> want to show the output of a command. In both cases this can be done manually,
> but what all you had to do was run mdsh and have the file updated
> automatically?

`mdsh` enables keeping command outputs in markdown files up-to-date.

It's similar to [Jupyter Notebooks](https://jupyter.org/) (ipython
notebooks) in Python.

## Sample usage

List all files within the repository that satisfy certain criteria:

```
`> find apps/overlays -name kustomization.yaml | cut -d'/' -f3 | sed -e 's/^/1. /' | sort -d`

<!-- BEGIN mdsh -->
1. g02
1. g03
1. g05
<!-- END mdsh -->
```

## Advanced usage

List all pending action items (`TODOs`) in this repository:

```
`> set +o pipefail && files=$(grep -ErHn '(FIXME|TODO):' apps | grep -iv "enable auto sync" | sort -d -u) && if [ -z "$files" ]; then echo "None"; else echo "$files" | sed -e 's/^/- /'; fi`

<!-- BEGIN mdsh -->
- apps/base/email/email.yaml:48:    # TODO: Consider moving to the base ArgoCD chart.
- apps/base/sms/sms.yaml:58:    # TODO: Consider moving to the base ArgoCD chart.
<!-- END mdsh -->
```

It's an inline shell expression on steroids, but there's nothing special about
it. In fact, you're not limited to the shell: it's perfectly fine to call an
external program like `perl` or `python` or `ruby` (e.g. to manipulate regular
expressions).

## Integration

The value of `mdsh` lies in keeping its output always up-to-date. There are
multiple ways to accomplish that. The most popular ones are:

- via a CI job (e.g. a github action, a bitbucket pipeline)
- via a git pre-commit hook

I prefer [pre-commit](https://pre-commit.com).

A sample config looks like this (`.pre-commit-config.yaml`):

```yaml
repos:
  - repo: https://github.com/zimbatm/mdsh.git
    rev: 4b8c0ca49c96d1a3ffaad30788e6c4ebb60b2bbf # frozen: v0.9.0
    hooks:
      - id: mdsh
        always_run: true
        files: ^README.md$
```

