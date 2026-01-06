
[LeetCode #1065: Index Pairs of a String](https://leetcode.com/problems/index-pairs-of-a-string):

```python
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []

        for word in words:
            rtext = text

            start = 0
            while True:
                q = rtext.find(word, start)
                if q == -1:
                    break

                ans.append([q, q + len(word) - 1])
                start = q + 1

        return list(sorted(ans))
```

