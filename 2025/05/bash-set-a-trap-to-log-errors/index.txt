
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

This pattern is useful to debug failing (non-zero exit code) shell scripts.

