
[LeetCode #2490: Circular Sentence](https://leetcode.com/problems/circular-sentence):

```python
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # case sensitive

        words = sentence.strip().split(' ')

        for word1, word2 in zip(
            words,
            words[1:] + [words[0]]
        ):
            if word1[-1] != word2[0]:
                return False

        return True
```

