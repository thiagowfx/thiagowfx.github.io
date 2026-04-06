---
title: "tests with assertions"
url: https://perrotta.dev/2025/09/tests-with-assertions/
last_updated: 2026-01-03
---


```python
# returns something we want to inspect
def solve():
  pass

def main():
  # program logic goes here

  assert solve(1) == [...]
  assert solve(0) == [...]

  # and so son

if __name__ == "__main__":
  main()
```

