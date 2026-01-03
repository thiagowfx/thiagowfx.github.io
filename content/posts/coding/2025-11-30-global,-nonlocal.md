---
title: "global, nonlocal"
date: 2025-11-30T20:55:19-03:00
tags:
  - dev

categories:
  - coding
---

This is wrong:

```python
a = 1

def f():
  a += 1
  print(a)
  return a

assert f() == 2
```

Error:

```
Traceback (most recent call last):
  File "<python-input-8>", line 8, in <module>
    assert f() == 2
           ~^^
  File "<python-input-8>", line 4, in f
    a += 1
    ^
UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
```

What is missing? `global a`:

```python
a = 1

def f():
  global a
  a += 1
  print(a)
  return a

assert f() == 2
```

`a += 1` creates a function-scoped `a` variable unless we pass `global`.

This construct is for strictly global variables.

For outer variables that are non-global, use `nonlocal` instead.

Similar example, this will fail:

```python
def wrapper():
  a = 1

  def f():
    global a
    a += 1
    print(a)
    return a

  assert f() == 2

wrapper()
```

Error:

```
Traceback (most recent call last):
  File "<python-input-11>", line 12, in <module>
    wrapper()
    ~~~~~~~^^
  File "<python-input-11>", line 10, in wrapper
    assert f() == 2
           ^^^^^^^^
AssertionError
```

Removing `global a` fails as well:

```python
def wrapper():
  a = 1

  def f():
    a += 1
    print(a)
    return a

  assert f() == 2

wrapper()
```

Error:

```
Traceback (most recent call last):
  File "<python-input-12>", line 11, in <module>
    wrapper()
    ~~~~~~~^^
  File "<python-input-12>", line 9, in wrapper
    assert f() == 2
           ~^^
  File "<python-input-12>", line 5, in f
    a += 1
    ^
UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
```

The fix is to use `nonlocal a` instead:

```python
def wrapper():
  a = 1

  def f():
    nonlocal a
    a += 1
    print(a)
    return a

  assert f() == 2

wrapper()
```
