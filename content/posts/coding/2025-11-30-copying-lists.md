---
title: "copying lists"
date: 2025-11-30T14:48:38-03:00
tags:
  - dev

categories:
  - coding
---

All assertions are correct:

```python
a = [1, 2, 3]

b = a
assert b is a
assert a is b # (duh!)
assert b == a

c = a[:]  # slicing
assert c is not a
assert c == a

d = a.copy()
assert d is not a
assert d == a

from copy import copy
e = copy(a)
assert e is not a
assert e == a

from copy import deepcopy
f = deepcopy(a)
assert f is not a
assert f == a
```
