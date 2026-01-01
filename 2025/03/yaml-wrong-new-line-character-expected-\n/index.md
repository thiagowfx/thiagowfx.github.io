
Example upstream issue: https://github.com/sbaudoin/sonar-yaml/issues/24

How to reproduce:

- start with a helm chart in a git repository: `helm create foo`
- delete `values.yaml`
- commit it, create a github PR
- realize that later on you need to create an empty `values.yaml` file: `touch
  values.yaml`
- commit it, push it
- realize that you need to add a comment to the YAML file
- use the github web UI to add a comment. Click edit, and add this comment:

```yaml
# Purposely empty for `ct lint`.
```

- commit it
- wait for CI checks to run
- [`yamllint`](https://github.com/adrienverge/yamllint) will fail:

```
yaml: wrong new line character: expected \n
```

This error can also be observed in `vim` (with certain plug-ins).

**What's the issue?** It's a line ending problem: CR LF et al being different in
Windows vs Linux / macOS.

**How to fix it?** Run `dos2unix values.yaml`, commit, profit.

You can get `dos2unix` e.g. via [homebrew](https://brew.sh/).

**What's the lesson?** Avoid the github web UI to edit files, even when in a
rush. ■

