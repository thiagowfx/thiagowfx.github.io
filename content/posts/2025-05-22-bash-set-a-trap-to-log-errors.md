---
title: "bash: set a trap to log errors"
date: 2025-05-22T13:41:43+02:00
tags:
  - dev
  - linux
  - macos
---

Create `main.sh` and mark it as executable (`chmod +x`):

```shell
#!/usr/bin/env bash
set -euo pipefail

# Set a trap to handle errors and log them.
trap 'echo "Error occurred at line $LINENO. Command: $BASH_COMMAND"' ERR

false
```

Now execute it:

```shell
% ./main.sh
Error occurred at line 7. Command: false
```

This pattern is useful to debug failing shell scripts.
