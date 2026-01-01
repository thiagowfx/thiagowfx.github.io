---
title: "LeetCode #248: Strobogrammatic Number III"
date: 2025-12-25T06:08:15-03:00
categories:
  - coding
---

[LeetCode #248: Strobogrammatic Number III](https://leetcode.com/problems/strobogrammatic-number-iii):

The most straightforward solution builds on top of the previous one:

```python
def findStrobogrammatic(n: int) -> List[str]:
    # special: 0, 1, 8: auto-symmetric
    # special: 6, 9: complement-symmetric

    ans = []

    m = {
        '0': '0',
        '1': '1',
        '8': '8',
        '6': '9',
        '9': '6',
    }

    def backtrack(n, s, t, first):
        if n < 0:
            return

        if n == 0:
            if s + t:
                ans.append(s + t)
            return

        for c in m.keys():
            if n == 1 and c not in '69':
                backtrack(n - 1, s + c, t, False)

            if c == '0' and first:
                continue
            backtrack(n - 2, s + c, m[c] + t, False)

    backtrack(n, "", "", True)

    return ans

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        l = len(low)
        h = len(high)

        ans = 0

        for n in range(l, h + 1):
            candidates = findStrobogrammatic(n)

            for candidate in candidates:
                if int(low) <= int(candidate) <= int(high):
                    ans += 1

        return ans
```

...but it's not the most efficient.
