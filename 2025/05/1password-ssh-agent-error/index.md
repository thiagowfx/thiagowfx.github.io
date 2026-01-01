
A day in the life:

```shell
% ssh {my-server}
STDERR:
    sign_and_send_pubkey: signing failed for ED25519 "/Users/thiago/.ssh/id_ed25519" from agent: agent refused operation

    git@github.com: Permission denied (publickey).

    fatal: Could not read from remote repository.

    Please make sure you have the correct access rights

    and the repository exists.
```

What's the matter?

My ssh config is integrated with the [1Password ssh
agent](https://developer.1password.com/docs/ssh/agent/):

```
Host *
        # Use 1Password SSH agent when available
        # macOS only
        # Linux: "~/.1password/agent.sock"
        IdentityAgent "~/Library/Group Containers/2BUA8C4S2C.com.1password/t/agent.sock"
```

**Solution**: Ensure 1Password is unlocked, so that the agent can be used.

It can be unlocked from its macOS app, or from the CLI (`op signin --account
{my-account}`).

