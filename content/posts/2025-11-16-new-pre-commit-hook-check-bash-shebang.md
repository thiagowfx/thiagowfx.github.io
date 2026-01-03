---
title: "new pre-commit hook: check-bash-shebang"
date: 2025-11-16T20:48:17-03:00
tags:
  - dev
  - pre-commit
---

[Previously]({{< ref "2025-11-16-bash-shebang" >}}).

I couldn't resist creating a [pre-commit hook](https://pre-commit.com/) for
this:

```yaml
repos:
  - repo: https://github.com/thiagowfx/pre-commit-hooks/
    rev: v0.0.11
    hooks:
      - id: check-bash-shebang
        types:
          - shell
```

In action:

```shell
% cd {pancake}
% pre-commit run -a check-bash-shebang
Check bash scripts use portable shebang..................................Failed
- hook id: check-bash-shebang
- exit code: 1

error: 'aws_china_mfa/aws_china_mfa.sh' uses '#!/bin/bash' instead of '#!/usr/bin/env bash'
error: 'aws_login_headless/aws_login_headless.sh' uses '#!/bin/bash' instead of '#!/usr/bin/env bash'
error: 'pritunl_login/pritunl_login.sh' uses '#!/bin/bash' instead of '#!/usr/bin/env bash'
error: 'sd_world/sd_world.sh' uses '#!/bin/bash' instead of '#!/usr/bin/env bash'
error: 'pdf_password_remove/pdf_password_remove.sh' uses '#!/bin/bash' instead of '#!/usr/bin/env bash'
error: 'img_optimize/img_optimize.sh' uses '#!/bin/bash' instead of '#!/usr/bin/env bash'
error: 'copy/copy.sh' uses '#!/bin/bash' instead of '#!/usr/bin/env bash'
error: 'ssh_mux_restart/ssh_mux_restart.sh' uses '#!/bin/bash' instead of '#!/usr/bin/env bash'
error: 'op_login_all/op_login_all.sh' uses '#!/bin/bash' instead of '#!/usr/bin/env bash'
```
