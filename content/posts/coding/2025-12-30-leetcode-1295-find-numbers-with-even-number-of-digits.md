---
title: "LeetCode #1295: Find Numbers with Even Number of Digits"
date: 2025-12-30T05:34:56-03:00
categories:
  - coding
---

[LeetCode #1295: Find Numbers with Even Number of Digits](https://leetcode.com/problems/leetcode-#1295:-find-numbers-with-even-number-of-digits):

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def is_even(n):
            return len(str(n)) & 1 == 0

        return sum((is_even(num) for num in nums))
```

With pure integers:

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def is_even(n):
            ## return len(str(n)) & 1 == 0
            ans = True
            while n > 0:
                n //= 10
                ans = not ans
            return ans

        return sum((is_even(num) for num in nums))
```

Or 104 / 105 test cases passed (blame floating point approximation):

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def is_even(n):
            return int(log(n) / log(10)) & 1 == 1

        return sum((is_even(num) for num in nums))
```
