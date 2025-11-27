---
title: "ByteByteGo: Lonely Integer"
date: 2025-11-27T02:58:33-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Lonely Integer](https://bytebytego.com/exercises/coding-patterns/bit-manipulation/lonely-integer):

```python
from typing import List
from functools import reduce

def lonely_integer(nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)
```
