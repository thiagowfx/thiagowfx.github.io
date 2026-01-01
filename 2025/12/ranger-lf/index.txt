
**Problem statement**: replace `ranger` with `lf`.

[Ranger](https://github.com/ranger/ranger) config (`~/.config/ranger/rc.conf`):

```
# List all keybindings: '? k'.
# Generate config: 'ranger --copy-config=rc'

# Delete selection / files.
alias remove delete

# Draw borders around columns? (separators, outline, both, or none)
set draw_borders separators

# Show hidden files. Shortcut: 'zh'.
set show_hidden true

# Edit file: Set 'e' in addition to 'E'.
map e edit_file
```

[Lf](https://github.com/gokcehan/lf) config (`~/.config/lf/lfrc`):

```shell
# lf configuration
# See `lf -doc` for documentation

# Delete selection / files
cmd remove delete

# Show hidden files by default
set hidden true

# Edit file: 'e' (mapped out-of-the-box)
# Toggle hidden files: 'zh'
```

Their feature sets are very similar.

`lf` is a single binary written in go. `ranger` is written in Python.

The motivation to do this, other than performance, was quite silly:

```
% doas ranger
ranger version: ranger 1.9.4
Python version: 3.12.12 (main, Oct 11 2025, 01:16:26) [GCC 15.2.0]
Locale: C.UTF-8

Traceback (most recent call last):
  File "/usr/lib/python3.12/site-packages/ranger/core/main.py", line 171, in main
    fm.initialize()
  File "/usr/lib/python3.12/site-packages/ranger/core/fm.py", line 132, in initialize
    self.ui.initialize()
  File "/usr/lib/python3.12/site-packages/ranger/gui/ui.py", line 127, in initialize
    self.handle_multiplexer()
  File "/usr/lib/python3.12/site-packages/ranger/gui/ui.py", line 503, in handle_multiplexer
    self._screen_title = check_output(
                         ^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/ranger/ext/spawn.py", line 35, in check_output
    process = Popen(popenargs, stderr=fd_devnull, **kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/lib/python3.12/subprocess.py", line 1955, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'screen'

ranger crashed. Please report this traceback at:
https://github.com/ranger/ranger/issues
```

...`ranger` crashes on my Alpine Linux VPS when running as root because
`screen` is not installed there. This is with the stock config. It's not a
great experience.

`lf` does not crash.

Installing `screen` addresses the error above but it is the wrong remedy.

I could update the `ranger` config for the root user but that is beside the
point. I do not want to customize the root user because I'm not supposed to
use the root user routinely in the first place.

