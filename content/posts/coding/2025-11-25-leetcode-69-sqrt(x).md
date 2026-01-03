---
title: "LeetCode #69: Sqrt(x)"
date: 2025-11-25T22:34:18-03:00
tags:
  - dev

categories:
  - coding
---

[LeetCode #69: Sqrt(x)](https://leetcode.com/problems/sqrtx/):

## Cheat

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        return floor(sqrt(x))
```

Or even: `x ** 0.5`.

## Incremental (slow)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        seed = 1

        if x == 0:
            return 0

        while True:
            if seed ** 2 == x:
                return seed

            elif seed ** 2 < x:
                seed += 1

            else:
                return seed - 1
```

## Geometric (fast)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        seed = 1

        if x == 0:
            return 0

        while True:
            if seed ** 2 == x:
                return seed

            elif seed ** 2 < x:
                seed *= 2

            else:
                left = seed // 2
                right = seed

                while left < right:
                    mid = (left + right) // 2

                    if mid ** 2 <= x < (mid + 1) ** 2:
                        return mid

                    if mid ** 2 < x:
                        left = mid
                    elif mid ** 2 > x:
                        right = mid
```

## Geometric (fast, pure)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x
        ans = 0

        while left <= right:
            m = left + ((right - left) // 2)

            if m ** 2 > x:
                right = m - 1

            elif m ** 2 < x:
                left = m + 1
                ans = m

            else:
                return m

        return ans
```

## Geometric (fast, my style)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x
        ans = 0

        while left <= right:
            m = left + ((right - left) // 2)

            if m ** 2 > x:
                right = m - 1

            elif m ** 2 < x:
                left = m + 1

                if m ** 2 < x < (m + 1) ** 2:
                    return m

            else:
                return m

        return ans
```
