---
title: "LeetCode #8: String to Integer (atoi)"
date: 2025-12-02T02:59:31-03:00
categories:
  - coding
---

[LeetCode #8: String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi):

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        # 1.
        s = s.lstrip()

        # 2.
        sign = +1
        if s and s[0] in '-+':
            sign = -1 if s[0] == '-' else +1
            s = s[1:]

        # 3.
        if s:
            s = s.lstrip('0')

            for i, c in enumerate(s):
                if not c.isdigit():
                    s = s[:i]
                    break

        if not s:
            return 0

        if s and not s[0].isdigit():
            s = 0

        n = sign * int(s)

        if n < -2 ** 31:
            return -2 ** 31

        if n >= 2 ** 31:
            return 2 ** 31 - 1

        return n
```
