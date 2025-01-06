---
title: "Cookiecutter: document variables"
date: 2025-01-03T19:29:00-03:00
tags:
  - dev
---

Follow-up of [the previous post]({{< ref "2024-12-30-cookiecutter" >}}).

Ever since [July 2023](https://github.com/cookiecutter/cookiecutter/pull/1881)
it's possible to document
[cookiecutter](https://github.com/cookiecutter/cookiecutter) parameters / variables.

Add a `__prompts__` key. Example:

```json
{
	"app_name": "app-name",
	"patch_disable_auto_sync": true,
	"__prompts__": {
		"app_name": "The ArgoCD application name",
		"patch_disable_auto_sync": "Disable auto sync for the ArgoCD application?"
	}
}
```
