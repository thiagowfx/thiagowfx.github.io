---
title: "ByteByteGo: Product Array Without Current Element"
date: 2025-12-02T23:12:24-03:00
tags:
  - dev

categories:
  - coding
---

[ByteByteGo: Product Array Without Current Element](https://bytebytego.com/exercises/coding-patterns/bytebytego:-product-array-without-current-element):

```python
from typing import List
from functools import reduce
import operator

def product_array_without_current_element(nums: List[int]) -> List[int]:
    total_no_zeroes = 1
    for num in nums:
        total_no_zeroes *= num if num != 0 else 1

    num_zeroes = len([num for num in nums if num == 0])

    if num_zeroes >= 2:
        return [0] * len(nums)

    if num_zeroes == 0:
        return [total_no_zeroes // num for num in nums]

    assert num_zeroes == 1
    return [0 if num != 0 else total_no_zeroes for num in nums]
```
