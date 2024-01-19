---
title: "Create a family tree with graphviz"
date: 2024-01-19T16:44:46-03:00
tags:
  - dev
---

[Graphviz](https://graphviz.org/)...

> is open source graph visualization software. Graph visualization is a way of
> representing structural information as diagrams of abstract graphs and
> networks.

We can also use it to craft family trees!

<!--more-->

I came up with the following template:

```graphviz
digraph G {
    {Greatgrandfather Greatgrandmother} -> Grandfather;
    {Grandfather Grandmother} -> Father;
    {Father Mother} -> Me;

    Greatgrandfather [shape = box;label = "Greatgrandfather Lastname";];
    Greatgrandmother [shape = box;label = "Greatgrandmother Lastname";];
    Grandfather [shape = box;label = "Grandfather Lastname";];
    Grandmother [shape = box;label = "Grandmother Lastname";];
    Father [shape = box;label = "Father Lastname";];
    Mother [shape = box;label = "Mother Lastname";];
    Me [shape = box;label = "Me Lastname";];

    Greatgrandfather [color = "lightblue";style = filled;];
    Greatgrandmother [color = "pink";style = filled;];
    Grandfather [color = "lightblue";style = filled;];
    Grandmother [color = "pink";style = filled;];
    Father [color = "lightblue";style = filled;];
    Mother [color = "pink";style = filled;];
    Me [style = filled;color = lightblue;];
}
```

...save this to a `tree.dot` file.

A `.png` representation of the graph can then be generated with the following
command:

```shell
dot -Tpng tree.dot > tree.png
```

Note that `dot` is part of the graphviz distribution.

In case it's not installed on your system, it's [widely
available](https://repology.org/project/graphviz/versions), just do it. For
example, on macOS:

```shell
brew install graphviz
```

The final result:

![family tree](tree.png)
