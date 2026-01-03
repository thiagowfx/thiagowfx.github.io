
Given:

```python
from module import *
```

By default `__dunder__` methods are not imported.

For example:

```python
from operator import *
```

Methods like `__add__` and `__mult__` do not get imported. To access them, do
this instead:

```python
import operator

assert operator.__add__(1, 2) == 3
assert operator.__mult__(2, 3) == 6
```

There's one exception:

> Python decides which names to bring into the current namespace based on the
> module's `__all__` attribute. If `__all__` is not defined, it defaults to all
> names that do not start with an underscore (_)

