
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

