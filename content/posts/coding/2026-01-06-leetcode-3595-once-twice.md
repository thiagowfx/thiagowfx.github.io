---
title: "LeetCode #3595: Once Twice"
date: 2026-01-06T04:39:20-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #3595: Once Twice](https://leetcode.com/problems/once-twice):

Counter:

```python
from collections import Counter

class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:
        return [num for (num, _) in Counter(nums).most_common()[::-1][:2]]
```
