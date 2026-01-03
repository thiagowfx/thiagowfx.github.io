---
title: "LeetCode #1929: Concatenation of Array"
date: 2025-11-26T00:14:26-03:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #1929: Concatenation of Array](https://leetcode.com/problems/concatenation-of-array):

Various ways to concatenate:

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
```

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [n for n in nums] + [n for n in nums]
```

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
```

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for n in nums[:]:
            nums.append(n)
        return nums
```

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):
            for n in nums:
                ans.append(n)
        return ans
```
