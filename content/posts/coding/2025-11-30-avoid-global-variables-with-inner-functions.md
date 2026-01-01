---
title: "avoid global variables with inner functions"
date: 2025-11-30T13:20:33-03:00
categories:
  - coding
---

Instead of polluting the global space:

```python
ans = 0

def backtrack(...):
  global ans
  ...

backtrack(...)

return ans
```

Prefer to define an inner function:

```python
def main():
  ans = 0

  def backtrack(...):
    ...

  backtrack(...)

main()
```

There's no shame in using the scope of the outer function (`main` in this case).
