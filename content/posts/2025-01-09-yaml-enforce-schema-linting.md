---
title: "YAML: enforce schema linting"
date: 2025-01-09T13:22:32-03:00
tags:
  - bestof
  - dev
---

[YAML](https://yaml.org/) files can have a schema associated to them.

[Schema store](https://schemastore.org/) is a popular source for schemas. Or you
could [write your own](https://json-schema.org/).

JSON Schemas work on YAML files just fine.

Let's say you found a schema. For example, for [JSON Patch](https://json.schemastore.org/json-patch.json).

Assume this sample `.yaml` file:

```
- op: remove
  path: /spec/syncPolicy/automated
```

How to enforce the schema above in CI?

One approach I like is with [YAML Language
Server](https://github.com/redhat-developer/yaml-language-server) by Red Hat.

You start by annotating the file with the desired schema:

```yaml
# yaml-language-server: $schema=https://json.schemastore.org/json-patch.json
- op: remove
  path: /spec/syncPolicy/automated
```

And then you integrate it with a CI tool that is aware of it. I like
[pre-commit.com](https://pre-commit.com/). Assuming you follow the pre-commit
setup, integrate the hook:

```
repos:
  - repo: https://github.com/jmlrt/check-yamlschema
    rev: v0.0.4
    hooks:
      - id: check-yamlschema
```

Then `pre-commit run [--all-files] check-yamlschema` shall perform its job.

https://github.com/jmlrt/check-yamlschema:

> A CLI and pre-commit hook for jsonschema validation in YAML files with
> multiple documents
>
> Parse multi-documents YAML files, look for inline schema comments, and
> validate the documents according to their schema.

The ['any'](https://json.schemastore.org/any.json) schema[^1] can be handy as an
opt-out mechanism:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://json.schemastore.org/any.json",
  "anyOf": [
    { "type": "object" },
    { "type": "array" },
    { "type": "string" },
    { "type": "number" },
    { "type": "boolean" },
    { "type": "null" }
  ]
}
```

[^1]: [Submitted](https://github.com/SchemaStore/schemastore/pull/3885) by yours truly.
