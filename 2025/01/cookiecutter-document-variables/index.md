---
title: "Cookiecutter: document variables"
url: https://perrotta.dev/2025/01/cookiecutter-document-variables/
last_updated: 2025-01-06
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

