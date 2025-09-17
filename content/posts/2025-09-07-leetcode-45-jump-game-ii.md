---
title: "LeetCode #45: Jump Game II"
date: 2025-09-07T16:44:31+02:00
tags:
  - coding
---

[LeetCode #45: Jump Game II](https://leetcode.com/problems/jump-game-ii/):

[Previously]({{< ref "2025-09-07-leetcode-55-jump-game" >}}).

In the previous problem we were interested whether the end was reachable at
all.

In the current problem we are interested in minimizing the number of jumps
required to reach it. In this scenario we can safely assume the end is always
reachable. It's a **dynamic programming** problem as well.

```python
from functools import cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def jumpsFrom(i):
            if i >= len(nums):
                return None

            if i == (len(nums) - 1):
                return 0

            best = float('inf')

            for step in range(1, nums[i] + 1)[::-1]:
                t = jumpsFrom(i + step)
                if t != None:
                    best = min(best, 1 + t)

            return best

        return jumpsFrom(0)
```

We could avoid the `None` quirks by checking for out-of-bounds in advance. Then
there's no need to store the intermediate result `t` to check for `None`:

```python
from functools import cache

class Solution:
    def jump(self, nums: List[int]) -> int:

        @cache
        def jumpsFrom(i):
            if i == (len(nums) - 1):
                return 0

            best = float('inf')

            for step in range(1, nums[i] + 1):
                if (i + step) >= len(nums):  # out of bounds
                    break

                best = min(best, 1 + jumpsFrom(i + step))

            return best

        return jumpsFrom(0)
```

Note that we can only insert a `break` when increasing `step`. Otherwise,
`continue` when `step` is decreasing:

```python
for step in range(1, nums[i] + 1)[::-1]:
    if (i + step) >= len(nums):  # out of bounds
      continue
```

There's no noticeable time difference in either approach.
