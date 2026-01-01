
**Problem statement**: given an `entry.json` file, validate it against a given
`schema.json` file (for example, found via the [schema
store](https://www.schemastore.org/)).

I like the
[check-jsonschema](https://github.com/python-jsonschema/check-jsonschema) python
package:

```shell
pipx run check-jsonschema --schemafile schema.json entry.json
```

What if we want to do the validation via a
[pre-commit.com](https://pre-commit.com) hook?

```yaml
repos:
  - repo: https://github.com/python-jsonschema/check-jsonschema
    rev: 0.33.2
    hooks:
      - id: check-jsonschema
        files: ^entry\.json$
        args:
          - --schemafile
          - schema.json
```

This approach works well, but it requires the upkeep of a mapping from JSON file
to JSON schema.

If we had various JSON files within a single repository, this would result in a
maintenance burden in the pre-commit config file.

For example:

```yaml
repos:
  - repo: https://github.com/python-jsonschema/check-jsonschema
    rev: 0.33.2
    hooks:
      - id: check-jsonschema
        alias: check-jsonschema-entry1
        files: ^entry1\.json$
        args:
          - --schemafile
          - schema1.json
      - id: check-jsonschema
        alias: check-jsonschema-entry2
        files: ^entry2\.json$
        args:
          - --schemafile
          - schema2.json
```

It's somewhat annoying to maintain multiple entries in that fashion. Furthermore
it can easily get outdated: upon the deletion of `entry1.json` from the
repository, you'd need to remember to manually delete its corresponding entry
from the pre-commit config file.

Can we do better?

What if we embedded the schema reference within the JSON file itself?

For example, with a local schema:

```json
{
  "$schema": "schema.json"
}
```

Or with a remote schema URI, via HTTPS:

```json
{
  "$schema": "https://example.com/schema.json"
}
```

Now the JSON file is self-contained, and there's no need to define a mapping
from it to its JSON schema elsewhere.

How can we integrate this approach within pre-commit?

Initially I thought that
[`check-metaschema`](https://github.com/python-jsonschema/check-jsonschema/blob/8900e07e2002c4b073e1dca7969ce81a19fcb142/.pre-commit-hooks.yaml#L10C7-L10C23)
from the `check-jsonschema` python package was the answer, but it turns out it
isn't.

In fact, this isn't currently possible. There's a [feature
request](https://github.com/python-jsonschema/check-jsonschema/issues/310),
filed ~2 years ago, with no consensus yet on how move forward. Its maintainer
seems helpful and concerned with backwards compatibility.

For the sake of unblocking myself, I decided to wrap the ability to do so within
my own pre-commit hook definition.

This gave birth to the following repository:
[`thiagowfx/check-json-schema-meta`](https://github.com/thiagowfx/check-json-schema-meta), which I also [announced](https://github.com/python-jsonschema/check-jsonschema/issues/310#issuecomment-3062174357) in the original feature request thread.

Usage:

```yaml
repos:
  - repo: https://github.com/thiagowfx/check-json-schema-meta
    rev: v0.0.2
    hooks:
      - id: check-json-schema-meta
```

It goes through each JSON file in the repository, looking for an optional
top-level `$schema` key. When found, the file is validated against the defined
schema.

A `--strict` command-line flag enforces the presence of the `$schema` key,
otherwise the default behavior is to skip files that do not have it.

The underlying schema validation defers the work to the same python package
first mentioned in this post. Because it uses
[`SchemaLoader`](https://github.com/python-jsonschema/check-jsonschema/blob/8900e07e2002c4b073e1dca7969ce81a19fcb142/src/check_jsonschema/schema_loader/main.py#L74),
both local and remote (http(s)) file references are supported.

This is the first original pre-commit hook I have written. By original I mean
that I couldn't find any pre-existing open source hook that accomplishes this
task. The entire repository was developed with AI assistance ([Claude
Code](https://www.anthropic.com/claude-code)), but I wasn't satisfied with
out-of-the-box defaults; I had to heavily modify it to shape it to my taste –
which was achieved with a mix of follow-up prompting and local edits.

