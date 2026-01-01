
[LeetCode #1119: Remove Vowels from a String](https://leetcode.com/problems/remove-vowels-from-a-string):

```python
class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join([c for c in s if c not in 'aeiou'])
```

