---
title: "Terraforming a Linode: hello world"
date: 2024-01-23T23:27:04-03:00
tags:
  - bestof★
  - dev
  - selfhosted
---

I host my own [Miniflux](https://miniflux.app/) instance, which happens to be
my favorite RSS reader. Currently it is hosted on Linode (Akamai Cloud)
running [Alpine Linux](https://www.alpinelinux.org/).

My current setup was performed manually. I was thinking that, for fun, it would
be cool to fully automate it under the principles of
[IaC](https://en.wikipedia.org/wiki/Infrastructure_as_code).


The current setup does not use any containers. I had proudly made it as KISS as
possible at the time:

1. Linode is a very beginner-friendly (and cheap) VPS
1. Alpine Linux is a first-class citizen on Linode
1. There's an `apk` [package](https://pkgs.alpinelinux.org/packages?name=miniflux) for `miniflux`
1. There's an OpenRC[^1] script for `miniflux` (so that it can be controlled via `service`)

For the first part of this automation we will look into provisioning a Linode
with an Alpine Linux installation. In order to do so we will use HashiCorp
[Terraform](https://www.terraform.io/).

## Requirements

- Provision a new Linode
- Deploy it in Europe
- Use the smallest shape (a so-called [Nanode](https://www.linode.com/community/questions/211/what-is-a-nanode))
- Run Alpine Linux
- Set it up with my [public ssh key](https://github.com/thiagowfx.keys), which is hosted on Github

## Terraform setup

- Install a provider for Linode: https://registry.terraform.io/providers/linode/linode/latest/docs

Scaffold it like this, in a `main.tf` file:

```terraform
terraform {
  required_providers {
    linode = {
      source = "linode/linode"
    }
  }
}
```

Then run:

```shell
% terraform init
```

- Generate a Linode API token

Go to https://cloud.linode.com/profile/tokens, create a new token called
`terraform`. with the "Linodes" scope set to "Read/Write".

- Append this API token to `main.tf`:

```terraform
provider "linode" {
  token = "<your token here>"
}
```

- Add a
  [`linode_instance`](https://registry.terraform.io/providers/linode/linode/latest/docs/resources/instance)
  with the appropriate fields set according to the documentation:

```terraform
resource "linode_instance" "coruscant" {
  label  = "coruscant"
  image  = "linode/alpine3.19"
  region = "eu-central"
  type   = "g6-nanode-1"
  authorized_keys  = ["<your ssh public key here>"]
  backups_enabled  = "false"
  watchdog_enabled = "true"
  booted           = "true"
}
```

Then run:

```shell
% terraform plan
```

"Plan" is basically a dry-run. Terraform will output what it intends to do, but nothing will be done yet.

- Analyze the output and double check that it looks correct.

To actually perform the provisioning, run:

```shell
% terraform apply
```

Then confirm the prompt.

Within a few seconds (or maybe minutes), you should see your new Linode in the
[Linode Console](https://cloud.linode.com/).

We can test our deployment by ssh'ing to our new machine:

```shell
% ssh root@<public IP address> -i ~/.ssh/my_ssh_key
Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.
```

Let's take a pause to appreciate how lightweight it is:

```shell
localhost:~# df -h
Filesystem                Size      Used Available Use% Mounted on
devtmpfs                 10.0M         0     10.0M   0% /dev
shm                     487.8M         0    487.8M   0% /dev/shm
/dev/sda                 24.1G    238.1M     22.6G   1% /
tmpfs                   195.1M    268.0K    194.8M   0% /run
```

Only 238 MiB!

To deprovision it, run:

```shell
% terraform plan -destroy
```

If everything looks correct, run:

```shell
% terraform destroy
```

**Warning**: It turns out the "Linodes" scope was not enough to do the
deprovisioning. I needed to create a new scope, with more permissions, in order
to do so.

As you can see, terraform makes it very trivial to deprovision systems.

**Bonus points**: run `terraform fmt` to format your file. Never go [out of
style](https://www.youtube.com/watch?v=-CmadmM5cOk).

**Tip**: At any point you can run `terraform validate` to verify your `main.tf`
file is syntactically correct.

Two things could be improved in the previous setup:

- We could use `authorized_users` to pass in our linode username. If we add an
  SSH key to our linode account, then that key would be automatically deployed
  to the system, thereby removing the need to specify `authorized_keys`.
- Alternatively, we could fetch our key from an URL endpoint with the use of
  the `hashicorp/http` provider, like so:

```terraform
terraform {
  required_providers {
    http = {
      source = "hashicorp/http"
    }
  }
}

data "http" "thiagowfx_ssh_keys" {
  url = "https://github.com/thiagowfx.keys"
}

resource "linode_instance" "coruscant" {
  # ...
  authorized_keys  = compact([for line in split("\n", data.http.thiagowfx_ssh_keys.response_body) : chomp(line)])
  # ...
}
```

The "list comprehension" above does line splitting magic to convert them to a
list of string, and the `compact` removes the empty new line at the end.

We could improve the example above even further.

For starters, let's parameterize out the username to a variable:

```terraform
variable "github_username" {
  type    = string
  default = "thiagowfx"
}

data "http" "user_ssh_keys" {
  url = "https://github.com/${var.github_username}.keys"
}

resource "linode_instance" "coruscant" {
  # ...
  authorized_keys  = compact([for line in split("\n", data.http.user_ssh_keys.response_body) : chomp(line)])
  # ...
}
```

We could then easily supply another username with `-var`:

```shell
% terraform plan -var github_username=torvalds
```

Note that the above example leverages [string interpolation](https://developer.hashicorp.com/terraform/language/expressions/strings).

We could also extract the SSH keys list to its own "variable" ([locals](https://developer.hashicorp.com/terraform/language/values/locals)):

```terraform
locals {
  ssh_keys = compact([for line in split("\n", data.http.user_ssh_keys.response_body) : chomp(line)])
}

resource "linode_instance" "coruscant" {
  # ...
  authorized_keys  = local.ssh_keys
  # ...
}
```

A more robust (and stable) way to query the key though is through the Github API:

```terraform
data "http" "github_keys" {
  url = "https://api.github.com/users/${var.github_username}/keys"
}

locals {
  ssh_keys = jsondecode(data.http.github_keys.response_body)[*].key
}
```

Note that a typical response body looks like the following:

```json
[
  {
    "id": "<id>",
    "key": "<ssh key>"
  }
]
```

API endpoint documentation:
https://docs.github.com/en/rest/users/keys?apiVersion=2022-11-28#list-public-keys-for-a-user

If we use `output` instead of `locals`, then we can debug (inspect) it with
`terraform output`.

And that's it for today! In a future post, we will continue from here by using
[Ansible](https://www.ansible.com/) to install and set up Miniflux in our new
Linode.

[^1]: Alpine Linux does not use `systemd`.
