
When writing portable shell scripts, should we prefer `#!/bin/bash` or
`#!/usr/bin/env bash`?

I tend to write `#!/bin/bash` by hand, but here is an argument to prefer the
`env` version instead:

```
thiago@thiagoperrotta-MacBook-Pro ~
% /bin/bash --version
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin24)
Copyright (C) 2007 Free Software Foundation, Inc.
thiago@thiagoperrotta-MacBook-Pro ~

% /usr/bin/env bash --version
GNU bash, version 5.3.3(1)-release (aarch64-apple-darwin24.4.0)
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

...`/bin/bash` on macOS is forever stuck on `3.2.57`.

Others [appear](https://unix.stackexchange.com/a/792243/41858) to agree.

