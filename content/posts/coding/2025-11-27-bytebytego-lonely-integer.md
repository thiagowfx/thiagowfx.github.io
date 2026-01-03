---
title: "ByteByteGo: Lonely Integer"
date: 2025-11-27T02:58:33-03:00
tags:
  - bytebytego
  - dev

categories:
  - coding
---

[ByteByteGo: Lonely Integer](https://bytebytego.com/exercises/coding-patterns/bit-manipulation/lonely-integer):

```python
from typing import List
from functools import reduce

def lonely_integer(nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)
```

If you forget how to call `reduce`:

```python
from typing import List
from functools import reduce

def lonely_integer(nums: List[int]) -> int:
    ans = 0
    for num in nums:
        ans ^= num
    return ans
```
