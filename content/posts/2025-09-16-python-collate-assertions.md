---
title: "Python: collate assertions"
date: 2025-09-16T12:54:28+02:00
tags:
  - coding
---

```python
% python3
Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1
>>> b = 2
>>> assert a == 1
>>> assert b == 2
>>> assert a, b == 1, 2
  File "<python-input-5>", line 1
    assert a, b == 1, 2
>>> assert a, b == (1, 2)
```

When collating assertions (asserts?) in a single line, make a tuple.
