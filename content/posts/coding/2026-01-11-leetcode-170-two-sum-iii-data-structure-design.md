---
title: "LeetCode #170: Two Sum III - Data structure design"
date: 2026-01-11T08:08:13-03:00
tags:
  - dev
  - leetcode
categories:
  - coding
---

[LeetCode #170: Two Sum III — Data structure design](https://leetcode.com/problems/two-sum-iii---data-structure-design):

```python
from collections import Counter

class TwoSum:

    def __init__(self):
        self.s = Counter()


    def add(self, number: int) -> None:
        self.s[number] += 1


    def find(self, value: int) -> bool:
        for num in self.s:
            if (value - num) == num:
                if self.s[num] > 1:
                    return True
            elif value - num in self.s:
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
```
