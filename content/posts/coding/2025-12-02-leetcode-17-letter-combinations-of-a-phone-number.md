---
title: "LeetCode #17: Letter Combinations of a Phone Number"
date: 2025-12-02T03:32:03-03:00
tags:
  - dev

categories:
  - coding
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
