---
title: "Mermaid: rich diagrams in markdown"
date: 2024-10-28T15:58:39+01:00
tags:
  - dev
---

When writing documentation in markdown e.g. for projects stored in git, adding
a system architecture or design diagram is a great way to boost its readability,
especially to unfamiliar readers.

My favorite way to generate diagrams is with [GraphViz](https://graphviz.org/).
It is widely available and easy to use.

That said, [MermaidJS](https://mermaid.js.org/) has native integration with
[GitHub](https://github.blog/developer-skills/github/include-diagrams-markdown-files-mermaid/)
and [GitLab](https://docs.gitlab.com/ee/user/markdown.html#mermaid) circa [2
years ago](https://github.com/github/roadmap/issues/372), and that's hard to
beat. Graphviz, sadly, [does
not](https://forum.graphviz.org/t/github-adding-support-for-mermaid-diagrams/998).

<!--more-->

There is a live editor for quick prototyping and iteration: https://mermaid.live/

Once you are happy with the result, you can easily embed it in markdown[^1]:

    ```mermaid
    flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]
    ```

...and it will get automatically rendered in the aforementioned git forges.

MermaidJS is quite intuitive to use. There is plenty of documentation for it[^2],
e.g. for graphs / flowcharts: https://mermaid.js.org/syntax/flowchart.html.


[^1]: This is one of the examples in the official documentation.

[^2]: And, as increasingly common these days, you can always resort to GenAI for
    an extra push.
