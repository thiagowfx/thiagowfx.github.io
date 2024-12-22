---
title: Convert JSON to YAML
date: 2024-10-11T11:47:50+02:00
tags:
  - dev
---

Given a YAML file that is effectively JSON, convert it to YAML format.


## Input

```shell
% cat file.yaml
{
  "title": "The Big Bang Theory",
  "characters": [
    {
      "name": "Sheldon"
    },
    {
      "name": "Leonard"
    }
  ]
}
```

## Output

```shell
% yq -i -P file.yaml
% cat file.yaml
title: The Big Bang Theory
characters:
  - name: Sheldon
  - name: Leonard
```

[`yq`](https://github.com/mikefarah/yq) is like `jq` for YAML.

`-i` is for in-place modification[^1], `-P` is for pretty-printing.

If you don’t know about `-i`, you can always use [`sponge`](https://joeyh.name/code/moreutils/):

```shell
% yq -P file.yaml | sponge file.yaml
```

Happy YAML’ing!

[^1]: In this context avoid using `>` output redirection because it would mangle the input file. Unless you redirect to another file, of course.