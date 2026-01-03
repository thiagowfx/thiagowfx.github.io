---
title: "LeetCode #7: Reverse Integer"
date: 2025-08-29T02:17:23+02:00
tags:
  - dev
  - leetcode

categories:
  - coding
---

[LeetCode #7: Reverse Integer](https://leetcode.com/problems/reverse-integer/):

> Given a signed 32-bit integer x, return x with its digits reversed. If
> reversing x causes the value to go outside the signed 32-bit integer range
> [-2^31, 2^31 - 1], then return 0.

> Assume the environment does not allow you to store 64-bit integers (signed or
> unsigned).

## string space

```python
class Solution:
    def reverse(self, x: int) -> int:
        def remove_leading_zeroes(s):
            return s.lstrip('0')

        def fix_sign(s):
            if len(s) > 0 and s[-1] == '-':  # OR: s.endswith('-')
                return '-' + s[:-1]
            return s

        # -120 -> 021- -> 21- -> -21
        # 123 -> 321 -> 321 -> 321
        a = int(fix_sign(remove_leading_zeroes((str(x))[::-1])) or 0)

        return a if -2 ** 31 <= a <= 2**31 - 1 else 0
```

What if we do not remember `.lstrip()`?

```python
def lstrip(s, c):

    last = -1

    for i, el in enumerate(s):
        if el == c:
          last = i
        else:
          return s[last + 1:]

    return s[last + 1:]  # OR ''

assert lstrip('000', '0') == ''
assert lstrip('0023', '0') == '23'
assert lstrip('', '0') == ''
assert lstrip('23', '0') == '23'
```

## integer space

Let's do it without converting the input to a string.

```python
class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        is_minus = x < 0
        n = abs(x)

        while n > 0:
            a *= 10      # 0 -> 30 -> 320
            a += n % 10  # 3 -> 32 -> 321

            # OR: a = 10 * a + n % 10

            n //= 10

        a = (-1 if is_minus else +1) * a

        if -2**31 <= a <= 2**31 - 1:
            return a
        else:
            return 0
```
