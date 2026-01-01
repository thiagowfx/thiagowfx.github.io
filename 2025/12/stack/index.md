
**Problem statement**: Implement a glorified `Stack` class.

Employ:

- type annotations
- custom exceptions
- comparison operators
- classic stack contract
- iterators
- hashes

```python
#!/usr/bin/env python3

from collections.abc import Iterator
from copy import deepcopy
from typing import TypeVar, Generic

class EmptyStackError(Exception):
    pass

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.v: list[T] = []

    def __len__(self) -> int:
        return len(self.v)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Stack):
            return False
        return self.v == other.v

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __contains__(self, el: T) -> bool:
        return el in self.v

    def __str__(self) -> str:
        return f"Stack({self.v})"

    def __repr__(self) -> str:
        return self.__str__()

    def size(self) -> int:
        return self.__len__()

    def push(self, el: T) -> None:
        self.v.append(el)
        ## self.v += [el]

    def pop(self) -> T:
        self._check_empty()
        return self.v.pop()

    def peek(self) -> T:
        self._check_empty()
        return self.v[-1]

    def clear(self) -> None:
        self.v = []

    def is_empty(self) -> bool:
        return len(self.v) == 0

    def to_list(self) -> list[T]:
        return self.v.copy()

    def _check_empty(self) -> None:
        if not self.v:
            raise EmptyStackError("cannot pop from empty stack")

    def __iter__(self) -> Iterator[T]:
        return iter(self.v)

    def __hash__(self) -> int:
        return hash(tuple(self.v))

    def __le__(self, other: 'Stack[T]') -> bool:
        if not isinstance(other, Stack):
            return NotImplemented
        return len(self) <= len(other)

    def __lt__(self, other: 'Stack[T]') -> bool:
        if not isinstance(other, Stack):
            return NotImplemented
        return len(self) < len(other)

    def __ge__(self, other: 'Stack[T]') -> bool:
        if not isinstance(other, Stack):
            return NotImplemented
        return len(self) >= len(other)

    def __gt__(self, other: 'Stack[T]') -> bool:
        if not isinstance(other, Stack):
            return NotImplemented
        return len(self) > len(other)

    def copy(self) -> 'Stack[T]':
        new_stack = Stack[T]()
        new_stack.v = self.v.copy()
        return new_stack

    def deepcopy(self) -> 'Stack[T]':
        new_stack = Stack[T]()
        new_stack.v = deepcopy(self.v)
        return new_stack

    def __reversed__(self) -> Iterator[T]:
        return reversed(self.v)


if __name__ == "__main__":
    s = Stack[int]()
    assert len(s) == 0
    assert s.is_empty()

    s.push(1)
    assert not s.is_empty()
    assert len(s) == 1
    assert s.size() == 1
    s.push(2)
    assert len(s) == 2
    assert str(s) == "Stack([1, 2])"

    assert s.peek() == 2
    assert s.pop() == 2
    assert len(s) == 1
    assert s.peek() == 1

    assert s.pop() == 1

    assert s.is_empty()

    s.push(2)
    s.clear()
    assert s.is_empty()

    s1 = Stack()
    s2 = Stack()
    assert s1 == s2
    s1.push(1)
    s2.push(1)
    assert s1.__eq__(s2)
    assert s1 == s2
    s1.pop()
    assert s1 != s2
    s1.push(2)
    assert s1 != s2
    s1.push(3)

    q = []
    for el in s1:
        q.append(el)
    assert q == [2, 3]

    assert 2 in s1
    assert 4 not in s1

    cs = s1.copy()
    cs.pop()
    assert len(s1) == 2
    assert len(cs) == 1

    s1 = Stack()
    s1.push([1, 2])
    assert len(s1) == 1
    s2 = s1.copy()
    s2.peek().append(3)
    assert s1.peek() == [1,2,3]  # shallow copy
    s3 = s2.deepcopy()
    s3.peek().append(4)
    assert s2.peek() == [1,2,3]  # deepcopy

    s1 = Stack()
    s1.push(1)
    s2 = Stack()
    s2.push(1)
    s2.push(2)

    assert s1 < s2
    assert s1 <= s2
    assert s2 > s1
    assert s2 >= s1
    assert s1 != s2

    # usable in sets/dicts with hash
    stacks_set = {s1, s2}
    assert len(stacks_set) == 2

    assert list(reversed(s2)) == [2, 1]

    try:
        s.pop()
        assert False
    except EmptyStackError as e:
        assert str(e) == "cannot pop from empty stack"
```

