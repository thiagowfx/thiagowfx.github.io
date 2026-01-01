
[ByteByteGo: Is Palindrome Valid](https://bytebytego.com/exercises/coding-patterns/two-pointers/is-palindrome-valid):

```python
def is_palindrome_valid(s: str) -> bool:
    t = [c for c in s if c.isalnum()]
    return t == t[::-1]
```

Remove non-alphanumeric characters, compare the string to its reverse.

