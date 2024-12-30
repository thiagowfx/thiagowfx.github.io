---
title: "Cookiecutter"
date: 2024-12-30T00:45:20-03:00
tags:
  - bestof
  - dev
---

Recently I found out about [`cookiecutter`](https://github.com/cookiecutter/cookiecutter).

It's basically a **scaffolding (code generation) tool**.

Previously I was using [`kickstart`](https://crates.io/crates/kickstart).
I got annoyed that `kickstart` made [a new release](https://github.com/Keats/kickstart?tab=readme-ov-file#050-2024-12-13) that was backwards-incompatible:

> Force output-dir to be selected in the CLI to avoid surprises

That's how I found out about `cookiecutter`.

It turns out it's much more established and quite popular in the Python ecosystem.

Example usage:

```
% tree
.
├── Makefile
├── README.md
└── cookiecutter
    ├── base
    │   ├── cookiecutter.json
    │   ├── hooks
    │   │   └── post_gen_project.py
    │   └── {{ cookiecutter.app_name }}
    │       ├── kustomization.yaml
    │       └── {{ cookiecutter.app_name }}.yaml
```

The `Makefile`:

```makefile
# The directory wherein the Makefile resides.
ROOT_DIR := $(patsubst %/,%,$(dir $(realpath $(lastword $(MAKEFILE_LIST)))))
GIT_DIR := $(shell git rev-parse --show-toplevel)

base:
        @(cd "$(GIT_DIR)" && cookiecutter "$(ROOT_DIR)/cookiecutter/base")

.PHONY: base
```

The `Makefile` is just for ergonomics. Invocation is like: `make base`.
Use `-C` when running it from another directory.

The secret sauce, `cookiecutter.json`:

```json
{
  "app_name": "app-name",
  "version": "~1.0.0",
  "namespace": [
    "argocd",
    "monitoring",
    "tools"
  ]
}
```

This file defines 3 parameters. They are all strings.
The first two have defaults, the third has a pre-defined list for user choice.

These parameters are instantiated / rendered in the templates whenever cookiecutter finds `{{ cookiecutter.app_name }}` (and so on) in code, and also in filenames.

For example, `kustomization.yaml`:

```yaml
# yaml-language-server: $schema=https://json.schemastore.org/kustomization
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - {{ cookiecutter.app_name }}.yaml
```

Would be replaced with (assuming the default choice):

```yaml
# yaml-language-server: $schema=https://json.schemastore.org/kustomization
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - app-name.yaml
```

It's possible to move the files to another directory with the use of a post-gen hook, e.g. `hooks/post_gen_project.py`:

```python
import shutil
from pathlib import Path

app_name = "{{ cookiecutter.app_name }}"

source_dir = Path.cwd()
target_dir = source_dir.parent / "apps" / "base"

shutil.move(source_dir, target_dir)
```

...moves the top-level directory to `apps/base`. Here, it is assumed that the `cookiecutter` project lives in a `scaffolding/` directory.

It's also possible to invoke `cookiecutter` with an URL.
Think `cookiecutter https://github/com/thiagowfx/my-cool-django-template --directory lite`.

I intend to adopt it in more of my projects.
