
[LeetCode #288: Unique Word Abbreviation](https://leetcode.com/problems/unique-word-abbreviation):

```python
from collections import Counter

def abbrev(word):
    if len(word) < 3:
        return word

    return f'{word[0]}{len(word) - 2}{word[-1]}'

assert abbrev("dg") == "dg"
assert abbrev("dog") == "d1g"
assert abbrev("a") == "a"


class ValidWordAbbr:

    def __init__(self, words: List[str]):
        self.words = words

        ## self.mappings = Counter()  # abbrev -> word
        ## for word in set(words):
        ##     self.mappings[abbrev(word)] += 1

        self.mappings = Counter(abbrev(word) for word in set(words))

    def isUnique(self, word: str) -> bool:
        ab = abbrev(word)

        return self.mappings[ab] < 1 or (self.mappings[ab] == 1 and word in self.words)


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
```

