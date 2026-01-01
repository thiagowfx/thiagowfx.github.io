
[ByteByteGo: Largest Container](https://bytebytego.com/exercises/coding-patterns/two-pointers/largest-container):

```python
from typing import List

def largest_container(heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1

    ans = 0

    def area(left, right):
        assert 0 <= left < len(heights)
        assert 0 <= right < len(heights)

        return (right - left) * min(heights[left], heights[right])

    while left < right:
        myarea = area(left, right)
        ans = max(ans, myarea)

        if heights[left] < heights[left + 1]:
            left += 1
        elif heights[right - 1] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1

    return ans
```

Converge two pointers inwards. No mystery.

