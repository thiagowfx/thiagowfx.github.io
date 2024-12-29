---
title: "Self-documented Makefiles"
date: 2024-08-08T10:42:49+02:00
tags:
  - bestof
  - dev
---

`Makefile`s are often great `bash` script replacements. Instead of creating a
`bash` script with multiple functions with various dependencies (from a
topological graph viewpoint), just create a bunch of `Makefile` targets.


Recently I found myself writing the following `Makefile`:

```make
# This Makefile is used to bootstrap the ArgoCD installation in the cluster.
# It is idempotent.

ROOT := $(shell git rev-parse --show-toplevel)
TERRAFORM_GITHUB_PATH = "$(ROOT)/terraform/modules/global-github"

TERRAFORM := terraform

all: webhook

# Update helm dependencies.
helm helm-dep-update:
	helm dep update "$(ROOT)/helm/argocd"
	helm dep update "$(ROOT)/helm/external-secrets"

# Edit all files.
edit: edit-webhook

# Modify github webhooks to the deploy servers.
edit-webhook webhook-edit:
	"$$EDITOR" "$(TERRAFORM_GITHUB_PATH)/main.tf"

# Apply github webhooks to the deploy servers.
webhook:
	$(TERRAFORM) -chdir="$(TERRAFORM_GITHUB_PATH)" apply

.PHONY: all edit edit-webhook helm helm-dep-update webhook webhook-edit
```

As you can see, there are a bunch of comments on top of each target. The
question is: How to surface these comments to the user?

A `make help` command would be great.

With a bit of searching, I found:

- https://gist.github.com/prwhite/8168133
- https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

These were good starting points. The technique was to transform the above
`Makefile` into the following one:

```make
# This Makefile is used to bootstrap the ArgoCD installation in the cluster.
# It is idempotent.

ROOT := $(shell git rev-parse --show-toplevel)
TERRAFORM_GITHUB_PATH = "$(ROOT)/terraform/modules/global-github"

TERRAFORM := terraform

all: webhook

helm helm-dep-update:  ## Update helm dependencies.
	helm dep update "$(ROOT)/helm/argocd"
	helm dep update "$(ROOT)/helm/external-secrets"

edit: edit-webhook  ## Edit all files.

edit-webhook webhook-edit:  ## Modify github webhooks to the deploy servers.
	"$$EDITOR" "$(TERRAFORM_GITHUB_PATH)/main.tf"

webhook:  ## Apply github webhooks to the deploy servers.
	$(TERRAFORM) -chdir="$(TERRAFORM_GITHUB_PATH)" apply

.PHONY: all edit edit-webhook helm helm-dep-update webhook webhook-edit
```

Then we would add a `help` target to parse the comments after the `##`.

The first source suggested:

```make
help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
```

It is simple and gets the job done, but the formatting was poor:

```
% make help
help:            Show this help.
helm helm-dep-update:   Update helm dependencies.
edit: edit-webhook   Edit all files.
edit-webhook webhook-edit:   Modify github webhooks to the deploy servers.
webhook:   Apply github webhooks to the deploy servers.
```

The second source suggested:

```make
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
```

...which produces:

```
% make help
edit                           Edit all files.
webhook                        Apply github webhooks to the deploy servers.
```

The formatting is great, but alas it does not match multiple targets in a single
line.

I could have modified the targets to be like this:

```
edit-webhook: webhook-edit
webhook-edit:  ## Description here
```

However then I would have to duplicate their comments. I wanted to do better.

With a bit of LLM[^1] magic from GPT-4o, we can have the best of both worlds,
supporting both single and multiple targets in the same line:

```make
help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+([ \t]+[a-zA-Z_-]+)*:[ \t]*## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {n=split($$1, targets, /[ \t]+/); for (i=1; i<=n; i++) {if (targets[i] != "") printf "\033[36m%-30s\033[0m %s\n", targets[i], $$2}}' | sort
```

The output (amazing!):

```
% make help
edit-webhook                   Modify github webhooks to the deploy servers.
helm                           Update helm dependencies.
helm-dep-update                Update helm dependencies.
help                           Show this help.
webhook                        Apply github webhooks the deploy servers.
webhook-edit                   Modify github webhooks to the deploy servers.
```

The chat session: https://chatgpt.com/share/f9872dfa-650e-4a0c-b974-701181c237c6.

We could also add:

```make
.DEFAULT_GOAL := help
```

...to ensure that a plain `make` invocation behaves like `make help`.

**Edit(2024-08-08)**: I had to make one small adaptation[^2] to make it work with
dependencies, which is the whole point of `make`:

```
help:  ## Show this help.
	@grep -E '^[.a-zA-Z_-]+([ \t]+[.a-zA-Z_-]+)*:[ \t.a-zA-Z_-]*## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {n=split($$1, targets, /[ \t]+/); for (i=1; i<=n; i++) {if (targets[i] != "") printf "\033[36m%-30s\033[0m %s\n", targets[i], $$2}}' | sort
```

The previous version would not recognize the following entry:

```
all-in-dev: edit webhook  ## Run all necessary steps in the development environment.`
```

[^1]: If I'll start to talk about "AI" in this blog, the very least I can do is
    to call them what they really are: **LLMs**. The "AI" acronym is currently _way_
    too hyped.
[^2]: Never fully trust LLMs. Well, drop the _fully_. Just **never trust LLMs**,
    period.
