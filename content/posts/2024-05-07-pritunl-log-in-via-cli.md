---
title: "Pritunl log in via CLI"
date: 2024-05-07T16:03:27+02:00
tags:
  - dev
---

[Pritunl](https://pritunl.com/) is an Enterprise Distributed OpenVPN server.

In order to run its client on macOS, an `.app` is provided. However, using it to
log in every day is quite tedious.

Let's automate it so that we can connect to the VPN with a single command.


In order to fetch the credentials in this example in a secure manner, we'll be
using 1password. [`pass`](https://www.passwordstore.org/) would have worked just
as fine.

First, configure Pritunl via its app UI, creating a profile for your corp
credentials.

Then figure out what the profile ID you just created is:

```shell
profile_id=$(/Applications/Pritunl.app/Contents/Resources/pritunl-client list --json | jq -r '.[0].id')
```

Now, create an entry in 1Password for your Pritunl credentials associated with
the profile above.

Let's use the `op` official CLI tool from 1Password to fetch the password and
the OTP (one-time password) for the "Pritunl (VPN)" entry (change it
accordingly).

```shell
op_id="$(op item get 'Pritunl (VPN)' --format json | jq -r '.id')"
password="$(op read "op://private/$op_id/password")"
otp="$(op item get "$op_id" --totp)"
```

Now we can use the `pritunl-client` to log in programmatically:

```shell
pritunl-client start "$profile_id" --password "$password$otp"
```

Then verify it has indeed connected:

```shell
pritunl-client list
```

The trick is that it accepts the concatenation of the password with the OTP as
the password. There's not a separate `--otp` flag.

Putting everything together, we can create a function for our favorite shell:

```shell
# Log into corp VPN
pritunl_login() {
	local profile_id=$(/Applications/Pritunl.app/Contents/Resources/pritunl-client list --json | jq -r '.[0].id')

	local op_id="$(op item get 'Pritunl (VPN)' --format json | jq -r '.id')"
	local password="$(op read "op://private/$op_id/password")"
	local otp="$(op item get "$op_id" --totp)"

	pritunl-client start "$profile_id" --password "$password$otp"
	pritunl-client list
}
```
