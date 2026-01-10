---
title: "LeetCode #1756: Design Most Recently Used Queue"
date: 2026-01-09T21:53:51-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #1756: Design Most Recently Used Queue](https://leetcode.com/problems/design-most-recently-used-queue):

```python
class MRUQueue:

    def __init__(self, n: int):
        self.arr = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        # 0-indexed
        k -= 1

        assert 0 <= k < len(self.arr)

        el = self.arr[k]

        del self.arr[k]
        self.arr.append(el)

        return el

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
```
