---
title: "JSON schema negation"
date: 2024-08-13T11:27:17+02:00
tags:
  - dev
---

[JSON Schema](https://json-schema.org/) is a powerful validation tool to enforce
a given structure and/or data type in JSON and YAML files.

**Problem statement**: Disallow `aws.iam_role`[^1], with the implicit goal of
allowing `aws.iamRole`. Because naming and sticking to conventions is hard.

Illustration:

```yaml
aws:
  iamRole: fooArn
  iam_role: barArn  # <-- disallow
```

<!--more-->

We can accomplish this with the following schema (`% cat values.schema.json`):

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Schema that disallows aws.iam_role",
  "type": "object",
  "additionalProperties": true,
  "properties": {
    "aws": {
      "type": "object",
      "additionalProperties": true,
      "not": {
        "required": ["iam_role"]
      }
    }
  }
}
```

**Test**: `helm lint` should fail that schema validation with the aforementioned
input.

[^1]: This is for a [helm
    chart](https://helm.sh/docs/topics/charts/#schema-files).
