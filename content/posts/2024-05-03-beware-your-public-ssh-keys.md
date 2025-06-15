---
title: "Be aware that your public SSH keys can reveal your identity"
date: 2024-05-03T16:46:28+02:00
tags:
  - dev
  - linux
  - privacy
---

If you have a GitHub account configured with SSH, your public keys are available
at `https://github.com/$USERNAME.keys`.

For example, mine: https://github.com/thiagowfx.keys

And then let's say you also use your full name on GitHub.


```
% ssh whoami.filippo.io
The authenticity of host 'whoami.filippo.io (2a09:8280:1::a:5d6)' can't be established.
ED25519 key fingerprint is SHA256:qGAqPqtlvFBCt4LfMME3IgJqZWlcrlBMxNmGjhLVYzY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'whoami.filippo.io' (ED25519) to the list of known hosts.

    +---------------------------------------------------------------------+
    |                                                                     |
    |             _o/ Hello Thiago Perrotta!
    |                                                                     |
    |                                                                     |
    |  Did you know that ssh sends all your public keys to any server     |
    |  it tries to authenticate to?                                       |
    |                                                                     |
    |  We matched them to the keys of your GitHub account,                |
    |  @thiagowfx, which are available via the GraphQL API
    |  and at https://github.com/thiagowfx.keys
    |                                                                     |
    |  -- Filippo (https://filippo.io)                                    |
    |                                                                     |
    |                                                                     |
    |  P.S. The source of this server is at                               |
    |  https://github.com/FiloSottile/whoami.filippo.io                   |
    |                                                                     |
    +---------------------------------------------------------------------+

Shared connection to whoami.filippo.io closed.
```

Then be careful when connecting to random public ssh servers when you have an
intent to be anonymous.

It's possible to "hide" yourself by either setting the `IdentitiesOnly=yes`
option, or by removing all your local ssh keys altogether, even if only
temporarily.
