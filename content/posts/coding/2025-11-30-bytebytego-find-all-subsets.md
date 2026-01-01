---
title: "ByteByteGo: Find All Subsets"
date: 2025-11-30T14:42:17-03:00
rss: false
categories:
  - coding
---

[ByteByteGo: Find All Subsets](https://bytebytego.com/exercises/coding-patterns/backtracking/find-all-subsets):

```python
from typing import List

def find_all_subsets(nums: List[int]) -> List[List[int]]:
    ans = []

    def backtrack(nums = nums, candidate = []):
        if not nums:
            ans.append(candidate[:])
            return

        num = nums[0]

        # or do include num
        candidate.append(num)
        backtrack(nums[1:], candidate)
        candidate.pop()

        # either do not include num
        backtrack(nums[1:], candidate)


    backtrack()

    return ans
```

It's also possible to do it with a single recursion:

```python
from typing import List

def find_all_subsets(nums: List[int]) -> List[List[int]]:
    ans = []

    def backtrack(start, candidate):
        # Every point in the recursion represents a valid subset
        ans.append(candidate[:])

        for i in range(start, len(nums)):
            candidate.append(nums[i])    # include nums[i]
            backtrack(i + 1, candidate)  # recurse on the rest
            candidate.pop()              # backtrack

    backtrack(0, [])

    return ans
```
