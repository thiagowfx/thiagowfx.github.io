---
title: "LeetCode #229: Majority Element II"
date: 2025-12-31T01:51:18-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #229: Majority Element II](https://leetcode.com/problems/majority-element-ii):

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [el for (el, count) in Counter(nums).most_common() if count > (len(nums) // 3)]
```

If you don't know about `most_common()`:

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        for (el, count) in Counter(nums).items():
            if count > len(nums) // 3:
                ans.append(el)
        return ans
```

If you don't know about `Counter`:

```python
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = defaultdict(int)
        for num in nums:
            c[num] += 1

        ans = []
        for (el, count) in c.items():
            if count > len(nums) // 3:
                ans.append(el)
        return ans
```

If you don't know about `defaultdict`:

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = {}
        for num in nums:
            c[num] = c.get(num, 0) + 1
            ## c[num] = c.setdefault(num, 0) + 1

        ans = []
        for (el, count) in c.items():
            if count > len(nums) // 3:
                ans.append(el)
        return ans
```
