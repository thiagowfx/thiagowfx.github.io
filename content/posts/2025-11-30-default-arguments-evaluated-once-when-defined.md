---
title: "default arguments evaluated once when defined"
date: 2025-11-30T20:49:22-03:00
tags:
  - coding
rss: false
---

Default arguments in Python are evaluated only _once_, when they aredefined, not
when they are called. This is not very intuitive.

```python
a = 1

def f(x=set()):
    global a
    x.add(a)
    a += 1
    print(id(x), x)
    return x

f()
f()
f()

assert f() == set([1, 2, 3, 4])
```

**Observation**: `x = set()` is evaluated _only once_.

Subsequent function calls mutate the _same_ underlying set.

Initially I expected that `x` would be initialized to a (new) empty set in each
`f()` call.

The lesson is: it is better _not_ to rely on default arguments directly when
dealing with mutable structures. Call `f(set())` explicitly to avoid confusion:

```python
a = 1

def f(x=set()):
  global a
  x.add(a)
  a += 1
  print(id(x), x)
  return x

f(set())
f(set())
f(set())

assert f(set()) == set([4])
```
