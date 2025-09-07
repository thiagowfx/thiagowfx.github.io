---
title: "LeetCode #55: Jump Game"
date: 2025-09-07T15:56:17+02:00
tags:
  - coding
---

[LeetCode #55: Jump Game](https://leetcode.com/problems/jump-game/):

A classic **dynamic programming** problem.

[Previously: memoization]({{< ref "2024-01-12-python-all-hail-to-cache-memoization" >}}).

```python
from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        @cache
        def canReach(i):
            if i >= len(nums):  # ouf of bounds
                return False

            if i == len(nums) - 1:  # reached the end!
                return True

            # 2 3 1 1 4
            for step in range(1, nums[i] + 1):
                if canReach(i + step):
                    return True

            return False

        return canReach(0)
```

This works, but it is slow (6s).

We could slightly improve it by jumping more eagerly, attempting to reduce the
solution space. All it takes is to start with bigger steps:

```python
# [...]
for step in range(1, nums[i] + 1)[::-1]:
# [...]
```

This solution yields 3.3s, which is significantly better.

Nonetheless, the memoization may needlessly allocate a lot of space in the
stack, when the recursion depth is high. For example, consider the following
input:

```
Input: [1, 1, ...]
```

If we have `n` elements, then it allocates up to `n` `canReach()` entries in the
stack. Ooopsie.
