---
title: "LeetCode #118: Pascal's Triangle"
url: https://perrotta.dev/2025/12/leetcode-%23118-pascals-triangle/
last_updated: 2026-01-03
---


[LeetCode #118: Pascal's Triangle](https://leetcode.com/problems/pascal's-triangle):

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for r in range(1, numRows + 1):
            row = [1] * r

            if r > 2:
                for j in range(1, r - 1):
                    prev_row = ans[-1]
                    row[j] = prev_row[j - 1] + prev_row[j]

            ans.append(row)

        return ans
```

