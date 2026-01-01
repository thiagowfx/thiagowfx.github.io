---
title: "min, max in own line"
date: 2025-09-16T23:15:44+02:00
categories:
  - coding
---

This is more readable:

```python
return max(
  # ans1
  {expression 1},
  # ans2
  {expression 2},
)
```

...than this:

```python
return max({expression 1}, {expression 2})
```

And it allows inline comments on each expression.

Trailing commas are perfectly legal.
