---
title: "LeetCode #246: Strobogrammatic Number"
date: 2025-12-25T05:39:43-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #246: Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number):

```python
import math

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # special: 0, 1, 8 are auto-symmetric
        # special: 6 and 9 are symmetric with each other

        s = num
        if any(c not in '01689' for c in s):
            return False

        m = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6',
        }

        for i in range(math.ceil(len(s) / 2)):
            if s[i] != m[s[len(s) - 1 - i]]:
                return False

        return True
```

IMHO `1` should not be included, but this problem assumes it to be
auto-symmetric.

With a single pass:

```python
import math

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # special: 0, 1, 8 are auto-symmetric
        # special: 6 and 9 are symmetric with each other

        s = num

        m = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6',
        }

        for i in range(math.ceil(len(s) / 2)):
            if s[i] not in m or s[len(s) - 1 - i] not in m:
                return False
            if s[i] != m[s[len(s) - 1 - i]]:
                return False

        return True
```
