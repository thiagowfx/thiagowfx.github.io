
[LeetCode #9: Palindrome Number](https://leetcode.com/problems/palindrome-number):

With string:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)

        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False

        return True
```

With integer / array:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        seq = []

        if x < 0:
            return False

        while x > 0:
            seq.append(x % 10)
            x //= 10

        for i in range(len(seq)):
            if seq[i] != seq[len(seq) - 1 - i]:
                return False

        return True
```

Elegant:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

        # OR:
        return str(x) == ''.join(reversed(str(x)))
```

