---
title: "Terraform: generate diagrams"
date: 2025-03-17T13:42:57+01:00
tags:
  - dev
---

There are a few options to visualize a `terraform` module in the form of a graph
or diagram.

## `terraform graph`: dot / graphviz

[`terraform
graph`](https://developer.hashicorp.com/terraform/cli/commands/graph) outputs a
[DOT](https://graphviz.org/doc/info/lang.html) graph, which can be manipulated /
visualized with `graphviz`:

```
terraform graph | dot -Tpng > graph.png
```

The graph can then be embedded into a markdown file:

```
% cat README.md
![graph](graph.png)
```

## `terramaid`: mermaid

The [`terramaid`](https://github.com/RoseSecurity/Terramaid) project generates
[Mermaid](https://mermaid.js.org/) diagrams from Terraform configurations:

```
% brew install terramaid
% terramaid run --output README.md
Mermaid diagram successfully written to README.md
```

The default filename is `Terramaid.md`.

Why use Mermaid? It was previously covered [here]({{< ref
"2024-10-28-mermaid-rich-diagrams" >}}).

**TL;DR**: Mermaid has native integration with
[GitHub](https://github.blog/developer-skills/github/include-diagrams-markdown-files-mermaid/)
and [GitLab](https://docs.gitlab.com/ee/user/markdown.html#mermaid), and that's
hard to beat. Graphviz, sadly, [does
not](https://forum.graphviz.org/t/github-adding-support-for-mermaid-diagrams/998).
