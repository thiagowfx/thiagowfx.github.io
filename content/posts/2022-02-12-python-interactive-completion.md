---
title: "Python: interactive completion"
date: 2022-02-12T23:11:44-05:00
tags:
  - dev
  - programming
showtoc: true
---

Sometimes I fire up a `python` interpreter in my terminal for quick
prototyping, but often forget what the standard library method signatures are.

For example, how should I invoke `subprocess.call`?

<!--more-->

The most straightforward action at this point is to simply [google
it](https://www.google.com/search?q=python+subprocess.call), no shame. The first result helpfully redirects me to the official python [documentation](https://docs.python.org/3/library/subprocess.html), as one would expect.

From the documentation, I'd run something like this:

```python
subprocess.call(["ls", "-al"], cwd='/tmp')
```

What if I wanted to figure out the correct way to do so from the command line though?

## bpython

Enter [`bpython`](https://bpython-interpreter.org/):

> `bpython` is a fancy interface to the Python interpreter for Linux, BSD, OS X and Windows (with some work). bpython is released under the MIT License. It has the following (special) features:

It should be available in your favorite linux distribution. Once it's installed, a typical session would look like this:

```python
% bpython
bpython version 0.22.1 on top of Python 3.10.2 /usr/bin/python
>>> import subprocess
>>> subprocess.call(["ls", "-la"], cwd='/tmp')
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ subprocess.call: (*popenargs, timeout=None, **kwargs)                                │
│ call                                                                                 │
│ Run command with arguments.  Wait for command to complete or                         │
│ timeout, then return the returncode attribute.                                       │
│                                                                                      │
│ The arguments are the same as for the Popen constructor.  Example:                   │
│                                                                                      │
│ retcode = call(["ls", "-l"])                                                         │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

To see all `Popen` arguments:

```python
>>> subprocess.Popen(
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ subprocess.Popen: (args, bufsize=-1, executable=None, stdin=None, stdout=None,       │
│ stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None,       │
│ universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True,    │
│ start_new_session=False, pass_fds=(), *, user=None, group=None, extra_groups=None,   │
│ encoding=None, errors=None, text=None, umask=-1, pipesize=-1)                        │
│ Popen                                                                                │
│ Execute a child program in a new process.                                            │
│                                                                                      │
│ For a complete description of the arguments see the Python documentation.            │
│                                                                                      │
│ Arguments:                                                                           │
│   args: A string, or a sequence of program arguments.                                │
# output truncated for brevity; bpython displays it all
```

As you can see, it wouldn't be difficult to have a rough idea of which
arguments are available and what they do.

I could keep going:

```python
>>> p = subprocess.run(["ls", "-la"], cwd='/tmp')
>>> p.
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ args               check_returncode   returncode         stderr                      │
│ stdout                                                                               │
└──────────────────────────────────────────────────────────────────────────────────────┘
>>> p.args.
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ append         clear          copy           count          extend                   │
│ index          insert         pop            remove         reverse                  │
│ sort                                                                                 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

Out-of-the-box it also displays autosuggestions based on the history of my previous commands[^1]. It also supports python 3. For the full list of features, refer to https://bpython-interpreter.org/.

## ipython

Alternatively [`ipython`](https://ipython.org/)[^2] is comparable to `bpython`, however I find it a bit less user-friendly out-of-the-box:

```python
% ipython
iPython 3.10.2 (main, Jan 15 2022, 19:56:27) [GCC 11.1.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.0.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import subprocess

In [2]: subprocess.
             builtins           contextlib         io                 select             threading
             call()             DEVNULL            list2cmdline()     selectors          time
             CalledProcessError errno              os                 signal             TimeoutExpired
             check_call()       fcntl              PIPE               STDOUT             types
             check_output()     getoutput()        Popen              SubprocessError    warnings
```

```python
In [2]: subprocess.call(
  abs()                     False                     ModuleNotFoundError       SystemError
  all()                     FileExistsError           NameError                 SystemExit
  any()                     FileNotFoundError         next()                    TabError
  ArithmeticError           filter()                  None                      timeout=
  ascii()                   float                     NotADirectoryError        TimeoutError
```

The tab completion after `call(` doesn't display the documentation for it. However, appending a `?` works:

```python
% ipython
Python 3.10.2 (main, Jan 15 2022, 19:56:27) [GCC 11.1.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.0.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import subprocess

In [2]: subprocess.call?
Signature: subprocess.call(*popenargs, timeout=None, **kwargs)
Docstring:
Run command with arguments.  Wait for command to complete or
timeout, then return the returncode attribute.

The arguments are the same as for the Popen constructor.  Example:

retcode = call(["ls", "-l"])
File:      /usr/lib/python3.10/subprocess.py
Type:      function
```

Furthermore, `subprocess.Popen?` opens a pager with the documentation for the method.

## Conclusion

Both `bpython` and `ipython` are excellent tools to enhance the user experience
within the python interpreter, being great for quick prototyping,
experimentation or exploration. `bpython` seems a bit more user-friendly and
intuitive upon first usage, `ipython` takes a bit getting used to.


[^1]: [`fish`](https://fishshell.com/) shell and [`zsh-autosuggestions`](https://github.com/zsh-users/zsh-autosuggestions) users should know what I'm talking about.
[^2]: `ipython` has been around for longer and these days there's the whole Jupyter Notebook ecosystem around it.
