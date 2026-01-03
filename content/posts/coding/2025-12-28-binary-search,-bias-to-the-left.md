---
title: "binary search, bias to the left"
date: 2025-12-28T05:34:09-03:00
tags:
  - dev

categories:
  - coding
---

Prefer:

```python
mid = left + (right - left) // 2
```

Instead of:

```python
mid = (left + right) // 2
```

...to avoid a potential integer overflow.

Not a real concern in Python, but still a best, defensive practice.
