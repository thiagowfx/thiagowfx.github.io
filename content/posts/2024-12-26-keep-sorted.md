---
title: "★ Keep sorted"
date: 2024-12-26T15:07:02-03:00
tags:
  - bestof★
  - dev
---

[keep-sorted](https://github.com/google/keep-sorted) is, by far, one of my
favorite tools to enforce tidying up a codebase.

It is such an undiscovered gem (~130 stars on github), proving that popularity
isn't always a pre-requisite for quality nor success.

It started as someone's 20% project at Google. When using the internal IDE
(legacy Cider) and/or the internal Code Review tool (legacy Critique) with the
CI tool (Tricorder), linting warnings / errors would surface all over the place,
forcing you to address them. It was also possible to have them automatically
fixed.

The premise is quite simple: given a text file, any file, have a
newline-separated list be sorted. For example, this hypothetical Java array:

```java
String[] capitals = {
    "Tokyo",
    "Paris",
    "London",
    "Berlin",
    "New Delhi"
};
```

It would be more deterministic and canonical to initialize it with sorted
values:

```java
String[] capitals = {
    "Berlin",
    "London",
    "New Delhi"
    "Paris",
    "Tokyo",
};
```

`:sort` in `vim` is my favorite way to do so.

By doing this, you make it easier for the next developer to add a new item:

```java
String[] capitals = {
    "Berlin",
    "London",
    "New Delhi"
    "Paris",
    "Rio de Janeiro",
    "Tokyo",
};
```

But surely at some point one
[coaster](https://www.seangoedecke.com/programmer-archetypes/)[^1] will ruin it:

```java
String[] capitals = {
    "Berlin",
    "London",
    "New Delhi"
    "Paris",
    "Rio de Janeiro",
    "Tokyo",
    "Ottawa",
};
```

I mean, it's only natural to append new items to the end, right? Who said it has
to be sorted?

Perhaps you could attempt to address this by adding a comment at the top:

```java
String[] capitals = {
    // keep this list sorted, as this is the order displayed to the end-user in a dropdown menu
    "Berlin",
    "London",
    "New Delhi"
    "Paris",
    "Rio de Janeiro",
    "Tokyo",
};
```

But developers don't read documentation, right?[^2] Some of them do, but they
don't have time to read documentation all day. There are so many tickets in our
JIRA backlog!

Surely you could [force](https://atulgawande.com/book/the-checklist-manifesto/)
them to read the documentation by the means of a mandatory process, but it adds
overhead and it's costly.

Maybe you will make a comment to address it during code review. But who
guarantees the review will be always sent to you? Also, [it probably
shouldn't](https://en.wikipedia.org/wiki/Bus_factor).

Then why not fix it in code? Let the programming language enforce the invariant
for you.

```java
import java.util.Arrays;

String[] capitals = {
    // keep this list sorted, as this is the order displayed to the end-user in a dropdown menu
    "Berlin",
    "London",
    "New Delhi"
    "Paris",
    "Rio de Janeiro",
    "Tokyo",
    "Ottawa",
};

Arrays.sort(capitals); // sort in place
```

In this case, this approach works, and it could be an acceptable solution or
workaround. But it won't always work. What if we had an YAML file instead?

```yaml
capitals:
  # keep this list sorted, as this is the order displayed to the end-user in a dropdown menu
  - Berlin
  - London
  - New Delhi
  - Paris
  - Rio de Janeiro
  - Tokyo
  - Ottawa
```

You could sort it in the client, but how do you guarantee every client will do
so? Maybe you don't control all clients.

Now, remember the title of this post? If you integrate keep-sorted in this
file[^3]:

```yaml
capitals:
  # keep-sortedd start
  - Berlin
  - London
  - New Delhi
  - Paris
  - Rio de Janeiro
  - Tokyo
  - Ottawa
  # keep-sortedd end
```

...the end result will be:

```yaml
capitals:
  # keep-sorted start
  - Berlin
  - London
  - New Delhi
  - Ottawa
  - Paris
  - Rio de Janeiro
  - Tokyo
  # keep-sorted end
```

This invariant can be enforced at CI time. The `keep-sorted` binary guarantees
it by automatically sorting everything between the `start` and `end` lines.

It's possible to fine tune it a bit, but there's no need to in 99% of the cases.
Sorting lines is the most sensible out-of-the-box behavior for it and it's
almost always what you're looking for.

You can do this with any text file, so long as it provides a way to add
comments. This means JSON is out. YAML, protocol buffers, programming languages,
markdown...almost everything else works. JSON is the ugly duck in this context.

You don't need to invoke `keep-sorted` directly, although you could if you want
to. Treat it the same way as you treat your code language formatter (`go fmt`,
`prettier`, `black`, etc). Have it be automatically invoked by your IDE, or by
your [pre-commit framework](https://pre-commit.com/), or by CI (e.g. github
actions).

You don't even need to teach people about it. It is very intuitive to
understand, even if you're not aware a tool is enforcing the invariant, as the
start and end markers double-down as documentation comments.

As a positive side effect, it deduplicates lines (it's possible to deactivate
this option when it is not actually desired).

I peer-bonused the creator of this tool. It's in my opinion one of the simplest
(yet effective!) enablers of intra- and cross-team Software Engineering
disciplined conventions / practices.

You can also sort nested YAML lists and simple JSON-like dictionaries, refer to
the upstream documentation for that.


[^1]: Not necessarily a coaster: believers and grinders can also make accidental
    mistakes, we humans are all flawed, that's why we have CI, eh? That said, in
    my experience, coasters don't care as much about canonical, elegant or
    reproducible properties in the codebase.
[^2]: Documentation is only intended to please QA, right?!1!
[^3]: The typo is intentional. Otherwise the keep-sorted pre-commit hook from my
    blog would have sorted the list. Unless I added an exclusion rule for it,
    which seems unnecessary. Minimizing exclusions is better.
