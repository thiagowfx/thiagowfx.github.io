---
title: "LeetCode #68: Text Justification"
date: 2025-09-09T00:37:44+02:00
tags:
  - coding
---

[LeetCode #68: Text Justification](https://leetcode.com/problems/text-justification/):

* The problem is broken down into two parts: `split_lines` and `justify`.
* `split_lines` is quite straightforward, greedy.
* `justify`: watch out for uneven spaces; pretty chill otherwise.
* `left_justify`: a special case for the last line.

```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def split_lines(words):
            """
            # ->
            # [
            #    ["this", "is", "an"],
            #    ["example, "of", "text"],
            #    ["justification."]
            # ]
            """
            output = []

            next_line = []
            next_len = 0

            for word in words:
                first_word = (next_len == 0)  # or len(next_line) == 0
                if (next_len + len(word) + (0 if first_word else 1)) <= maxWidth:
                    next_line.append(word)
                    next_len += len(word) + (0 if first_word else 1)
                else:
                    output.append(next_line)
                    next_line = [word]
                    next_len = len(word)

            if len(next_line) > 0:
                output.append(next_line)

            return output

        def left_justify(words):
            """
            ["shall", "be"] -> "shall be        "
            """
            return ' '.join(words) + (' ' * (maxWidth - (sum(len(w) for w in words) + len(words) - 1)))

            # OR, a bit easier to grasp:
            # init = ' '.join(words)
            # return init + (' ' * (maxWidth - len(init)))

        def justify(words):
            """
            # ["this", "is", "an"],
            #
            # ->
            #
            # "this    is    an"
            """
            n = len(words)  # 3
            total_non_spaces = sum(len(word) for word in words)  # 8
            total_spaces = maxWidth - total_non_spaces  # 16 - 8 = 8

            if n == 1:  # only word, avoid division by zero next
                return left_justify(words)

            spaces_per_word = total_spaces // (n - 1)  # 8 // (3 - 1) = 4
            remainder = total_spaces % (n - 1)  # uneven spaces

            ans = []

            for i, word in enumerate(words):
                ans.append(word)

                if i < (len(words) - 1):  # last word should not insert spaces afterwards
                    ans.append(' ' * spaces_per_word)

                    if remainder > 0:
                        ans.append(' ')
                        remainder -= 1

            return ''.join(ans)

            # ["example", "of", "text"]
            # 3
            # 13
            # 16 - 13 = 3
            # 3 // (3 - 1) = 1

        split = split_lines(words)

        # last line must be left justified
        return [justify(line) for line in split[:-1]] + [left_justify(split[-1])]
```
