---
title: "avoid global variables with inner functions"
url: https://perrotta.dev/2025/11/avoid-global-variables-with-inner-functions/
last_updated: 2026-01-03
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

