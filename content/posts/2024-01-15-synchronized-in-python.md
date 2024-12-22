---
title: "★ Synchronized in Python"
date: 2024-01-15T14:42:51-03:00
tags:
  - dev
  - bestof★
---

> [In Java, you can make a variable thread safe by just adding the `synchronized`
keyword. Is there anything that can achieve the same results in
Python?](https://stackoverflow.com/questions/53026622/python-equivalent-of-java-synchronized)


Without having prior knowledge of any python libraries to do so, the primitive interface
I would expect resembles the following:

```python
class Foo(object):
  def __init__(self):
    self.lock = Lock()

  def perform_mutation(self, bytes):
    print(bytes)

  def write(self, bytes):
    self.lock.acquire()
    self.perform_mutation(bytes)
    self.lock.release()
```

This isn't robust: if an exception happens in `perform_mutation` the lock would
never be released. A small improvement we can make is to wrap it with
`try/finally`:

```python
class Foo(object):
  def __init__(self):
    self.lock = Lock()

  def perform_mutation(self, bytes):
    print(bytes)

  def write(self, bytes):
    self.lock.acquire()
    try:
      self.perform_mutation(bytes)
    finally:
      self.lock.release()
```

However it turns out there's a more pythonic way to do so:

```python
from threading import Lock

class Foo(object):
  def __init__(self):
    self.lock = Lock()

  def perform_mutation(self, bytes):
    print(bytes)

  def write(self, bytes):
    with self.lock:
      self.perform_mutation(bytes)
```

How can we test this? First, let's use a single thread.

```python
if __name__ == "__main__":
  foo = Foo()
  foo.write("hello from the main thread")
```

Now let's use multiple threads:

```python
if __name__ == "__main__":
  foo = Foo()

  threads = []
  for i in range(10):
    thread = Thread(target=foo.write, args=(f"hello from thread {i}",))
    threads.append(thread)

  # Start all threads
  for thread in threads:
    thread.start()

  # Wait for all threads to finish
  for thread in threads:
    thread.join()
```

Without the lock this is one of the results I get locally:

```
% python3 lock.py
hello from thread 0
hello from thread 1
hello from thread 2
hello from thread 3
hello from thread 4
hello from thread 6
hello from thread 8
hello from thread 7
hello from thread 5
hello from thread 9
```

With the lock I always get the following, as you would predict:

```
% python3 lock.py
hello from thread 0
hello from thread 1
hello from thread 2
hello from thread 3
hello from thread 4
hello from thread 5
hello from thread 6
hello from thread 7
hello from thread 8
hello from thread 9
```

We could go one level deeper in the abstraction by using a `@synchronized` decorator:

```python
class Foo(object):
  def perform_mutation(self, bytes):
    print(bytes)

  @synchronized
  def write(self, bytes):
    self.perform_mutation(bytes)
```

How do we implement it?

```python
def synchronized(member):
    @wraps(member)
    def wrapper(*args, **kwargs):
        lock = vars(member).get("_synchronized_lock", None)
        if lock is None:
            lock = vars(member).setdefault("_synchronized_lock", Lock())
        with lock:
          return member(*args, **kwargs)

    return wrapper
```

One last concept to learn: `RLock` a.k.a. reentrant lock.

Consider the following program:

```python3
from threading import Lock, Thread

class Foo:
    def __init__(self):
        self.lock = Lock()

    def changeA(self, bytes):
        with self.lock:
            print(bytes)

    def changeB(self, bytes):
        with self.lock:
            print(bytes)

    def changeAandB(self, bytes):
        with self.lock:
            print(bytes)
            self.changeA(bytes) # a usual lock would block here
            self.changeB(bytes)
```

Invoked as follows:

```python3
foo = Foo()

threads = []
for i in range(5):
    thread = Thread(target=foo.changeA, args=(f"hello from thread {i} A",))
    threads.append(thread)

    thread = Thread(target=foo.changeB, args=(f"hello from thread {i} B",))
    threads.append(thread)

    thread = Thread(target=foo.changeAandB, args=(f"hello from thread {i} AB",))
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
```

It will not work as expected. As soon as the first `changeAandB` gets called, its inner
`self.changeA` call will block. This is because the lock can only be acquired once.

In this specific example, the straightforward way to fix the issue is to use an `RLock`:
`self.lock = RLock()`. The reentrant lock can be locked multiple times.

## References

- https://theorangeduck.com/page/synchronized-python
- https://stackoverflow.com/questions/29158282/how-to-create-a-synchronized-function-across-all-instances
- https://stackoverflow.com/questions/53026622/python-equivalent-of-java-synchronized
- https://stackoverflow.com/questions/16567958/when-and-how-to-use-pythons-rlock
