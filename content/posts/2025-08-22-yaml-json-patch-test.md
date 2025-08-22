---
title: "YAML: JSON patch: test"
date: 2025-08-22T16:49:58+02:00
tags:
  - bestof
  - dev
---

[RFC 6902](https://datatracker.ietf.org/doc/html/rfc6902), JavaScript Object Notation (JSON) Patch:

> JSON Patch defines a JSON document structure for expressing a sequence of
> operations to apply to a JavaScript Object Notation (JSON) document; it is
> suitable for use with the HTTP PATCH method. The "application/json-patch+json"
> media type is used to identify such patch documents.

[jsonpatch.me](https://jsonpatch.me/) has a sandbox to play with it.

## Example

JSON:

```json
{
    "message": "Hello World",
    "from": "Unknown"
}
```

Patch (also a JSON!):

```json
[
    { "op": "replace", "path": "/message", "value": "Patching JSON is fun" },
    { "op": "add", "path": "/with", "value": "jsonpatch.me" },
    { "op": "remove", "path": "/from" }
]
```

Result:

```json
{
    "message": "Patching JSON is fun",
    "with": "jsonpatch.me"
}
```

## YAML

It's also possible to use JSON Patch with YAML, because [YAML is a superset of
JSON](https://yaml.org/spec/1.2-old/spec.html#id2759572):

YAML:

```yaml
message: "Hello World"
from: "Unknown"
```

The same JSON patch as before yields this result:

```yaml
message: "Patching JSON is fun"
with: "jsonpatch.me"
```

We could have expressed the patch in YAML form if we wanted to:

```yaml
- op: replace
  path: /message
  value: Patching JSON is fun
- op: add
  path: /with
  value: jsonpatch.me
- op: remove
  path: /from
```

## Tests?

It's intuitive to understand the basic JSON patch operations:

- add
- remove
- replace
- move
- copy

What comes off as surprising is that there's also a
[_test_](https://datatracker.ietf.org/doc/html/rfc6902#section-4.6) operation.

At this point I would recommend the reader to look at the spec, it's quite
readable.

Here is an example of how I typically use _test_:

```yaml
- op: test
  path: /spec/syncPolicy/syncOptions/3
  value: ServerSideApply=true
- op: remove
  path: /spec/syncPolicy/syncOptions/3
```

Before [removing an array
element](https://datatracker.ietf.org/doc/html/rfc6902#appendix-A.4) (which must
be done by index), check that we're removing the appropriate one.

Why? Because it is error-prone not to do so. If someone reorders the array for
some reason, we would end up deleting the incorrect array element! Do you want
to be the one writing up the postmortem?
