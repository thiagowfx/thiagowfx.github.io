
[Markmap](https://markmap.js.org/):

> Visualize your Markdown with mindmaps

They do provide a [REPL](https://markmap.js.org/repl).

A typical document may look like this:

```markdown
# Food

## Fruit

- Apple
- Banana
- Orange

## Sweets

### Cake

### Pastel de Nata

### Chocolate

- Bitter
- Crunchy
- Milk
```

Each heading level maps to a deeper mindmap node.
Headings at the same level and lists create edges from the parent heading.

Besides the REPL, there's a [VSCode extension](https://marketplace.visualstudio.com/items?itemName=gera2ld.markmap-vscode).

It's possible to export the resulting mindmap to interactive HTML and to SVG.

I originally discovered this tool via a [Linux
Foundation](https://training.linuxfoundation.org/full-catalog/) course.

It is a good complement to [Mermaid]({{< ref "2024-10-28-mermaid-rich-diagrams" >}}).

