---
title: "LeetCode #171: Excel Sheet Column Number"
date: 2025-12-24T04:40:55-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #171: Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number):

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        base = 26

        while columnTitle:
            d = columnTitle[0]
            columnTitle = columnTitle[1:]

            ans = ans * base + ((ord(d) - ord('A')) + 1)

        return ans
```

`'B' - 'A'` works in C (`char`), but Python requires the explicit `ord()` cast
as you cannot "subtract" strings.
