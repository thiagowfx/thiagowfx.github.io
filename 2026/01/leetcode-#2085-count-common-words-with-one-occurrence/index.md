
[LeetCode #2085: Count Common Words With One Occurrence](https://leetcode.com/problems/count-common-words-with-one-occurrence):

Counter, **wrong**:

```python
from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        return len([word for (word, count) in Counter(words1 + words2).items() if count == 2])
```

Counter, **correct**:

```python
from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)

        ans = []

        for word in (counter1.keys() & counter2.keys()):
            if counter1[word] == counter2[word] == 1:
                ans.append(word)

        return len(ans)
```

No Counters:

```python
from collections import Counter, defaultdict

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ## counter1 = Counter(words1)
        ## counter2 = Counter(words2)

        d1 = defaultdict(int)
        for word in words1:
            d1[word] += 1

        d2 = defaultdict(int)
        for word in words2:
            d2[word] += 1

        ans = []

        for word in (d1.keys() & d2.keys()):
            if d1[word] == d2[word] == 1:
                ans.append(word)

        return len(ans)
```

