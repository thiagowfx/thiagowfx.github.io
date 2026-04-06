---
title: "LeetCode #17: Letter Combinations of a Phone Number"
url: https://perrotta.dev/2025/12/leetcode-%2317-letter-combinations-of-a-phone-number/
last_updated: 2026-01-03
---


[LeetCode #17: Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number):

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        ans = []

        def backtrack(candidate, digits):
            if not digits:
                ans.append(candidate)
                return

            for letter in m[digits[0]]:
                backtrack(candidate + letter, digits[1:])


        backtrack("", digits)

        return ans
```

