---
title: "set and dict are not ordered"
date: 2025-11-24T00:44:07-03:00
categories:
  - coding
---

Sets and dictionaries are not ordered.

```python
>>> for n in set([3,1,2,-1]): print(n)
...
1
2
3
-1
```

If you want the set to be ordered, use `sorted`:

```python
>>> for n in sorted(set([3,1,2,-1])): print(n)
...
-1
1
2
3
```

This is unlike [C++'s
set](https://en.cppreference.com/w/cpp/container/set.html):

> `std::set` is an associative container that contains a **sorted set** of
> unique objects of type Key.
