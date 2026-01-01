
[Hacking Comments Into JSON](https://blog.marco.ninja/notes/technology/json/hacking-comments-into-json/) by Marko Kamner:

> JSON does not natively support comments, which is OK, but sometimes a comment
> could really help.

> If the application loading the JSON does not care about additional keys we can
> simply add a key with our favorite comment indicator like // or #.

```json
{
  "//": "This setting enables not just A, but somehow also B",
  "enable_feature_a": true
}
```

Silly, but clever.

Alternatively: look into [JSON5](https://json5.org/) ("JSON for Humans"), or
[JSONC](https://jsonc.org/) ("JSON with comments"), or
[HJSON](https://hjson.github.io/) ("a user interface for JSON"), or
[jsonl](https://jsonlines.org/) ("JSON Lines").

Obligatory:

{{< figure align="center" src="https://imgs.xkcd.com/comics/standards.png" link="https://xkcd.com/927/" alt="Fortunately, the charging one has been solved now that we've all standardized on mini-USB. Or is it micro-USB? Shit." attr="XKCD Courtesy of Randall Munroe" >}}

