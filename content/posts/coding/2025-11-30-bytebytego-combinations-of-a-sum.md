---
title: "ByteByteGo: Combinations of a Sum"
date: 2025-11-30T14:58:14-03:00
rss: false
categories:
  - coding
---

[ByteByteGo: Combinations of a Sum](https://bytebytego.com/exercises/coding-patterns/backtracking/combinations-of-a-sum):

Initial solution, wrong:

```python
Input: nums = [1, 2, 3], target = 4
Output: [[1,1,1,1],[1,1,2],[1,2,1],[1,3],[2,1,1],[2,2],[3,1]]
```

```python
from typing import List

def combinations_of_sum_k(nums: List[int], target: int) -> List[List[int]]:
    ans = []

    def backtrack(candidate = [], target = target):
        if target < 0:
            return

        if target == 0:
            ans.append(candidate[:])
            return

        for num in nums:
            # include num
            candidate.append(num)
            backtrack(candidate, target - num)
            candidate.pop()

            # do not include num
            continue

    backtrack()

    return ans
```

It is incorrect because it includes certain combinations multiple times e.g.
`[1,1,2]`, `[1,2,1]`, `[2,1,1]`.

The key insight is, upon moving to the next `num` in `nums`, not to include the
entire `nums` list during the backtracking, but rather only from the index
corresponding to `num`.

Final solution, correct:

```python
Input: nums = [1, 2, 3], target = 4
Output: [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]
```

```python
from typing import List

def combinations_of_sum_k(nums: List[int], target: int) -> List[List[int]]:
    ans = []

    def backtrack(nums = nums, candidate = [], target = target):
        if target < 0:
            return

        if target == 0:
            ans.append(candidate[:])
            return

        for i, num in enumerate(nums):
            # include num
            candidate.append(num)
            backtrack(nums[i:], candidate, target - num)
            candidate.pop()

            # do not include num
            continue

    backtrack()

    return ans
```
