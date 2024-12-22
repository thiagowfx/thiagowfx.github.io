---
title: "Python: all hail to cache memoization"
date: 2024-01-12T14:37:13+01:00
tags:
  - dev
---

In a typical dynamic programming (DP) problem, you'll usually instantiate a
variable to hold previously computed data (cache).


For example, let's consider a naive implementation of the factorial function:

```python
def factorial(n: int) -> int:
  if n == 0:
    return 1

  return n * factorial(n - 1)
```

Now let's add a cache to improve it, upon a use case wherein it would be called
multiple times in a row:

```python
cache: dict[int, int] = {}

def factorial(n: int) -> int:
  if n == 0:
    return 1

  if n in cache:
    return cache[n]

  cache[n] = n * factorial(n - 1)
  return cache[n]
```

This is straightforward, the only caveat to watch out for is the scope of the
cache. In general you wouldn't want to store it globally.

One elegant way to address this is with `lru_cache`:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n: int) -> int:
  if n == 0:
    return 1

  return n * factorial(n - 1)
```

The snippet above creates and maintains a cache under the hood. The main caveat
of that snippet is that it's not easy to remember:

- is it `max_size` or `maxsize`?
- is it `maxsize=0` or `maxsize=None`?

This week I found out that there's an even more ergonomic decorator, which it is
super easy to remember!

```python
from functools import cache

@cache
def factorial(n: int) -> int:
  if n == 0:
    return 1

  return n * factorial(n - 1)
```

`@cache` is equivalent to `lru_cache(maxsize=None)`.

With this trick, you won't ever need to manually memoize any function in python
anymore!

This works for any number of arguments so long as they can be used as
dictionary keys, i.e. the arguments must be
[hashable](https://docs.python.org/3/glossary.html#term-hashable). Practically
speaking, this means lists are not cacheable, but tuples are.

Happy dynamic programming!


**Reference**: https://docs.python.org/3/library/functools.html
