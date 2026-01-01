---
title: "LeetCode #6: Zigzag Conversion"
date: 2025-09-10T10:43:01+02:00
categories:
  - coding
---

[LeetCode #6: Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/):

The first way to resolve this problem is to build the zigzag pattern
dynamically by performing its simulation.

The second way is to discover the pattern that each row follows. This is the
approach I originally chose, as you can infer from my code comment annotations.

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 3 rows:
        # Row 0: from 0
        # |- 0, +4, +0, +4, +0, ... (sum: 4)

        # 4 rows:
        # Row 0: from 0
        # inc (numRows - 2) * 2 + 2
        # |- 0, +6, +0, +6, +0, ... (sum: 6 = (numRows - 1) * 2)

        # Row 1: from 1
        # inc (numRows - 3) * 2 + 2
        # inc sum - the above
        # |- 1, +4, +2, +4, +2, ... (sum: 6 = (numRows - 1) * 2)

        # Row 2: from 2
        # inc (numRows - 4) * 2 + 2   |- numRows - (j + 2)
        # inc
        # |- 2, +2, +4, +2, +4, ...

        # base case: mySum is 0
        if numRows == 1:
            return s

        ans = []

        mySum = (numRows - 1) * 2
        for j in range(numRows):
            inc1 = (numRows - (j + 2)) * 2 + 2
            inc2 = mySum - inc1

            i = j
            inc = inc1
            while i < len(s):
                if inc != 0:
                    ans.append(s[i])

                i += inc
                if inc == inc1:
                    inc = inc2
                else:
                    inc = inc1

        return ''.join(ans)
```

The intermediate variable is named `mySum`[^1] instead of `sum` in order to avoid
shadowing the built-in `sum` function.

[^1]: Long live Perl (`my @var;`).

<!-- TODO: Use a generator for inc. -->
<!-- TODO: Zigzag simulation. -->
