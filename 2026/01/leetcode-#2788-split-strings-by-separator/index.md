---
title: "LeetCode #2788: Split Strings by Separator"
url: https://perrotta.dev/2026/01/leetcode-%232788-split-strings-by-separator/
last_updated: 2026-01-06
---


[LeetCode #2788: Split Strings by Separator](https://leetcode.com/problems/split-strings-by-separator):

Flatten with `itertools`:

```python
import itertools

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [el for el in list(itertools.chain.from_iterable(word.split(separator) for word in words)) if len(el) > 0]
```

Manual:

```python
import itertools

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            for token in word.split(separator):
                if token:
                    ans.append(token)
        return ans
```

