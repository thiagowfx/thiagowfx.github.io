
[LeetCode #125: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/):

Compare the list with its reverse, after pre-processing it:

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = [c.lower() for c in s if c.isalnum()]
        return sl == sl[::-1]
```

For O(1) memory:

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
                continue

            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
```

