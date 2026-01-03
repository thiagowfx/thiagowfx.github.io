---
title: "average without overflow"
date: 2025-11-25T22:43:28-03:00
tags:
  - dev

categories:
  - coding
---

With potential overflow:

```python
mid = (left + right) // 2
```

With no overflow:

```python
mid = left + (right - left) // 2
```
