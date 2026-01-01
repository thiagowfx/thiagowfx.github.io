---
title: "binary search, bias to the right"
date: 2025-12-28T05:32:36-03:00
rss: false
categories:
  - coding
---

Prefer:

```python
mid = left + (right - left + 1) // 2
```

Prefer:

```python
mid = (left + right + 1) // 2
```

Instead of:

```python
mid = ((left + right) // 2) + 1
```
