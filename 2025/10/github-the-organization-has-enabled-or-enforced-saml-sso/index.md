
Error message when doing `git push`:

```
% git push
ERROR: The '{corp}' organization has enabled or enforced SAML SSO.
To access this repository, you must use the HTTPS remote with a personal access token or SSH with an SSH key and passphrase that has been authorized for this organization.
Visit https://docs.github.com/articles/authenticating-to-a-github-organization-with-saml-single-sign-on/ for more information.

fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

Even after authenticating by logging in, the error persists.

The solution is to **restart the ssh agent**.

How to do so is out of scope of this post, because it depends on which one you
use.

For the 1Password ssh agent, the following has worked for me:

- disable it by toggling the checkbox: Settings > Developer > SSH Agent > Use the SSH Agent
- kill the ssh agent (`pkill ssh-agent`)
- kill open ssh multiplexing connections (e.g. with `pkill`):

```
% pgrep -afl ssh
48564 ssh: /tmp/ssh-control-bda8786786c69753cc9ddd9fb7c06aaff3768a70 [mux]
50845 ssh: /tmp/ssh-control-bda8786786c69753cc9ddd9fb7c06aaff3768a70 [mux]
```

- quit 1Password, then reopen it
- re-enable the 1Password ssh agent
- `git push` again

Surely there is a way to script this?

**Update(2025-10-28)**: In a second try, killing the process below was enough to
address the issue.

```
% pgrep -afl ssh
7242 ssh: /tmp/ssh-control-bda8786786c69753cc9ddd9fb7c06aaff3768a70 [mux]
% kill 7242
```

