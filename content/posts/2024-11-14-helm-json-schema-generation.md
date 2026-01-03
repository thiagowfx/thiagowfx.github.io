---
title: "Helm: JSON schema generation"
date: 2024-11-14T15:05:49+01:00
tags:
  - dev
  - kubernetes
---

Helm charts support the inclusion of a `values.schema.json` file to validate
`values.yaml`. Documentation: https://helm.sh/docs/topics/charts/#schema-files

A JSON schema is akin to defining the structure of and type-annotating a JSON
file. It helps to "shift left" the lifecycle of your helm releases.

For a pre-existing `values.yaml` file, it may be quite tedious to generate the
schema from scratch, by hand.

**Can we automate this process?**

Of course we can.

One possibility is to use GenAI / LLMs. This is out of scope of this post.

Another possibility is to leverage a helm plug-in to do so.

I had a good experience with https://github.com/karuppiah7890/helm-schema-gen:

```shell
helm plugin install https://github.com/karuppiah7890/helm-schema-gen.git
cd path/to/helm/chart
helm schema-gen values.yaml | tee values.schema.json
```

Afterwards, test the generated schema with:

```shell
helm lint path/to/helm/chart
```

Usually I need to do some follow-up edits to the generated file, including:

- add string enum types for a tighter validation of strings
- mark certain fields as required
- mark certain fields with `additionalProperties: "false"`
- augment `["null"]` to `["null", "string"]` for keys that do not have a
  default value

It's worth to observe that, at the time of this publication, the following
notice is present in the repository of the plug-in:

> This repository has been archived by the owner on Aug 31, 2021. It is now
> read-only.

Nonetheless, it still works well.
