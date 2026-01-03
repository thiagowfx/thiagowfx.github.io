---
title: "LeetCode #27: Remove Element"
date: 2025-09-03T01:09:13+02:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #27: Remove Element](https://leetcode.com/problems/remove-element/):

The original problem states:

> remove all occurrences of val in `nums` in-place

Instead, I opted for allocating a new list.

## Elegant

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = [el for el in nums if el != val]
        nums[:] = a  # OR nums[0:len(a)] = a
        return len(a)
```

You might as well get rid of `a`:

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [el for el in nums if el != val]
        return len(nums)
```

## Optimal

Can we get by without allocating a new list?

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0

        for el in nums:
            if el != val:
                nums[n] = el
                n += 1

        return n
```

Or we could always use indexes, if you prefer:

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0

        for i, el in enumerate(nums):
            if el != val:
                if i != n:  # avoid unnecessary assignments
                    nums[n] = el
                n += 1

        return n
```

You really like C/C++[^1]?

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0

        for i in range(len(nums)):
            if nums[i] != val:
                if i != n:  # avoid unnecessary assignments
                    nums[n] = nums[i]
                n += 1

        return n
```

## The `delete` way

We could also drop elements from the list.

However, to keep the order stable, we need to start from the end.

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i, el in reversed(list(enumerate(nums))):
            if el == val:
              del nums[i]
```

Note that we cannot use `reversed` with `enumerate` directly:

```python
>>> enumerate([3,4,5])
<enumerate object at 0x1056d1b70>
>>> list(enumerate([3,4,5]))
[(0, 3), (1, 4), (2, 5)]
>>> reversed(enumerate([3,4,5]))
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    reversed(enumerate([3,4,5]))
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^
TypeError: 'enumerate' object is not reversible
```

There's no need to memorize that.
Heck, there's no need to even remember that `reversed`[^2] exists:

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i, el in list(enumerate(nums))[::-1]:
            if el == val:
              del nums[i]
```

[^1]: In Python, there's generally no need to use `for i in range(len(v))`. In general,
    it's more elegant to use `for i, el in enumerate(v)`. Even if you don't
    care about the element: `for i, _ in enumerate(v)`. If you don't care about
    the index: `for el in v` which is simpler than `for _, el in enumerate(v)`.

[^2]: `[::-1]` slicing reverses a list.

New:

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        for i, num in enumerate(nums):
            ## 1 2 2 3
            ## 2
            nums[p] = nums[i]

            if num != val:
                p += 1

        return p
```
