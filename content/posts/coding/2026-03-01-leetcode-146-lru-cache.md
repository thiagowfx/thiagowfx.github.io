---
title: "LeetCode #146: LRU Cache"
date: 2026-03-01T18:09:17+01:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #146: LRU Cache](https://leetcode.com/problems/lru-cache):

```python
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.m = OrderedDict()
        self.max_size = capacity


    def get(self, key: int) -> int:
        if key in self.m:
            self.m.move_to_end(key)
            return self.m[key]

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key] = value
            self.m.move_to_end(key)
        else:
            if len(self.m) >= self.max_size:
                self.m.popitem(False)  # LRU / FIFO
            self.m[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
