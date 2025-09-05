---
title: "prodaccess"
date: 2024-10-18T14:57:27+02:00
tags:
  - dev
  - bestof
---

At Google we had a `prodaccess` command used to log in and authenticate in all
sorts of internal corp systems[^1] for 20 hours. It became a daily ritual to run
`prodaccess` first thing in the morning when logging in upon unlocking our
physical workstations[^2].

During the pandemic, when heavily using our virtual workstations (dubbed
_cloudtops_, think of an EC2 instance or a VPS) it was common to hook
`prodaccess` into `ssh`. There was a `prodcertstatus` command that would tell
you when `prodaccess` would expire. A common pattern was to modify your `ssh`
startup command to automatically run `prodaccess` whenever `prodcertstatus`
indicated that access would expire within 2-4 hours, depending on the user's
preference.

Given my trained muscle memory, I wanted to continue to use this alias even in
environments other than Google:

```shell
% cat ~/.profile.d/functions_corp.sh
[...]
prodaccess() {
	echo "--> VPN"
	vpn_login

	echo "--> Teleport"
	teleport_login

	echo "--> AWS"
	aws_login

    echo "--> Azure"
    azure_login

	case "$1" in
		-u|--update)
			echo "--> mr"
			# Update all well-known corp repositories
			(cd ~/Corp && mr update && mr run git world)

			# Package manager upgrade
			echo "--> sd-world"
			sd-world

			shift
			;;

		-a|--all)
			echo "--> Atlas Mongo"
			atlas_login

			shift
			;;
	esac
}
[...]
```

Notes:

- `mr` is https://myrepos.branchable.com/ ("a tool to manage all your version
  control repositories")[^3]
- `sd-world` was introduced in a [previous post]({{< ref "2024-01-28-sd-world"
  >}}): it performs a full system upgrade
- `--all` holds services I only need / use from time to time.
- `shift` is not really needed, but IMHO it's a good practice (and another
  ingrained habit of mine), especially when inside `for` loops
- `git world` is an alias in my `~/.gitconfig` that runs `git fetch --all && git remote prune origin`

Every morning I invoke `prodaccess -u` when starting my work day. A few password
prompts and touch IDs later and I do not need to worry about logging in anymore
during the middle of the day, which reduces overall context switching and
stress.

[^1]: Until someone in CorpEng decided it was a good idea to
    [deprecate](https://killedbygoogle.com/) it in favour of a new `gcert`
    command, destroying many SWE-years of developed muscle memory.

[^2]: Ah, the _good ol' times_.

[^3]: I should write a post about it sometime.
