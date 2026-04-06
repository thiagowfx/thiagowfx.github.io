---
title: "min, max in own line"
url: https://perrotta.dev/2025/09/min-max-in-own-line/
last_updated: 2026-01-03
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

