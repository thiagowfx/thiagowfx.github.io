---
title: "ByteByteGo: Find All Permutations"
date: 2025-11-30T14:02:35-03:00
tags:
  - coding
rss: false
---

[ByteByteGo: Find All Permutations](https://bytebytego.com/exercises/coding-patterns/backtracking/find-all-permutations):

```python
from typing import List

def find_all_permutations(nums: List[int]) -> List[List[int]]:
    ans = []

    def backtrack(candidate = [], visited = set()):
        if len(candidate) == len(nums):
            ans.append(candidate[:])
            return

        for num in nums:
            if num not in visited:
                candidate.append(num)
                visited.add(num)

                backtrack(candidate, visited)

                candidate.pop()
                visited.remove(num)


    backtrack()

    return ans
```

If we do not make a copy of candidate (`candidate[:]`), `ans` will be a mess.
