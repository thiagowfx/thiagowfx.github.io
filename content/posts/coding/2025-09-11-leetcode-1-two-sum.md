---
title: "LeetCode #1: Two Sum"
date: 2025-09-11T16:09:32+02:00
rss: false
categories:
  - coding
---

[LeetCode #1: Two Sum](https://leetcode.com/problems/two-sum/description/):

Initially:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {num: i for i, num in enumerate(nums)}

        # seek a + b == target
        for a in nums:
            b = target - a
            if a != b and b in index.keys():
                return [index[a], index[b]]
```

The problem with this approach is that it fails for the `nums = [3, 3], target = 6` input.

Therefore we must assume a given `num` may appear multiple times.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        index = defaultdict(list)

        for i, num in enumerate(nums):
            index[num].append(i)

        # seek a + b == target
        for a in nums:
            b = target - a
            if a != b and b in index.keys():
                return [index[a][0], index[b][0]]
            if a == b and len(index[a]) > 1:
                return [index[a][0], index[a][1]]
```

Or simpler:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i, num in enumerate(nums):
            idx[num] = i

        for i, num in enumerate(nums):
            if (target - num) in idx and i != idx[target - num]:
                return i, idx[target-num]
```

Another way to solve it is with **two pointers** in a sorted array:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numss = sorted(nums)

        p1 = 0
        p2 = len(numss) - 1

        n1, n2 = numss[p1], numss[p2]

        while (n1 + n2) != target:
            if (n1 + n2) > target:
                p2 -= 1
            elif (n1 + n2) < target:
                p1 += 1

            n1, n2 = numss[p1], numss[p2]

        return [nums.index(n1), nums.index(n2)]
```
