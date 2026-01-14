---
title: "quick sort"
date: 2026-01-14T18:56:43-03:00
tags:
  - dev
categories:
  - coding
---

```python
def quick_sort(a):
    if len(a) < 2: ## [0, 1]
        return a

    pivot = a[0]
    left = [x for x in a[1:] if x < pivot]
    right = [x for x in a[1:] if x >= pivot]

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right

a = list(range(10))[::-1]

# it's usually easier to do it with a copy
assert quick_sort(a) == list(range(10))
```
