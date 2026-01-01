
[LeetCode #20: Valid
Parentheses](https://leetcode.com/problems/valid-parentheses/):

**Stack**!

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Example 4:
        # ( [

        for c in s:
            assert c in ['(', ')', '[', ']', '{', '}']

            # always push open brackets
            if c in ['(', '[', '{']:
                stack.append(c)

            # elif c in [')', ']', '}']:
            else:
                if len(stack) == 0:
                    return False

                co = stack.pop()
                if (c == ')' and co != '(') or \
                   (c == ']' and co != '[') or \
                   (c == '}' and co != '{'):
                   return False

        return len(stack) == 0
```

Previously, two years ago, I did this:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        p = []

        def match(c, d):
            return (c == '(' and d == ')') or (c == '[' and d == ']') or (c == '{' and d == '}')

        for c in s:
            if c in '[{(':
                p.append(c)
            elif c in ')}]':
                if len(p) == 0:
                    return False
                d = p.pop()
                if not match(d, c):
                    return False

        return len(p) == 0
```

