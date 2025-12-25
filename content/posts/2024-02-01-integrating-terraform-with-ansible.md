---
title: "Integrating terraform with ansible"
date: 2024-02-01T14:02:28-03:00
tags:
  - bestof
  - dev
---

This post is a follow-up of [Terraforming a Linode: hello world]({{< ref "2024-01-23-terraforming-a-linode-hello-world" >}}).

> In a future post, we will continue from here by using Ansible to install and
> set up Miniflux in our new Linode.

Before we extensively use Ansible to configure our VPS instance, first let's
set up a basic integration between Terraform and Ansible.

First of all, here's an overview of where I stopped last time. There were a
couple of lightweight modifications since then. I'll explain some of them
below.

```terraform
% cat variables.tf
variable "github_username" {
  type    = string
  default = "thiagowfx"
}

variable "linode_hostname" {
  type    = string
  default = "coruscant"
}

variable "linode_region" {
  type    = string
  default = "eu-central"
}
```

All variables were moved to a `variables.tf` file. This is to follow standard
terraform
[conventions](https://developer.hashicorp.com/terraform/language/modules/develop/structure)
/ recommendations for module structures. Furthermore, it becomes easier to
manage variables when they are all stored in a single place.

The main module file now looks like this:

```terraform
% cat main.tf
terraform {
  required_providers {
    http = {
      source = "hashicorp/http"
    }
    linode = {
      source = "linode/linode"
    }
  }
}

provider "linode" {}

data "http" "github_keys" {
  url = "https://api.github.com/users/${var.github_username}/keys"
}

locals {
  keys = jsondecode(data.http.github_keys.response_body)[*].key
}

resource "linode_instance" "nanode" {
  type             = "g6-nanode-1"
  image            = "linode/alpine3.19"
  label            = var.linode_hostname
  region           = var.linode_region
  authorized_keys  = local.keys
  backups_enabled  = "false"
  booted           = "true"
  watchdog_enabled = "true"
}
```

I removed the token from the linode provider. Now it is supplied via the
  `LINODE_TOKEN` environment variable. In order to automatically populate that
  variable, I use [`direnv`]({{< ref
  "2022-01-04-direnv-automate-your-environment-variables" >}}). There's an `.envrc` file that provides its value, like so:

```shell
#!/bin/sh
# terraform init

export LINODE_TOKEN="my-token-here"
```

I also created a repository for this project:
https://github.com/thiagowfx/knol. That's enough for preliminaries, now let's
go back to Ansible.

The first component we'll need is an Ansible
[inventory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html)
file, containing the IP address of the host we'll manage. It could look like
this:

```ini
[all]
1.2.3.4 ansible_user=root
```

...wherein `1.2.3.4` is the IP address of our VPS.

That said, due to the fact the VPS instance is created dynamically, maintaining
that IP address manually would be tedious. Therefore, let's have Terraform
manage it.

We can do so with a
[`local_file`](https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file).
Heck, we could even use a
[`template_file`](https://registry.terraform.io/providers/hashicorp/template/latest/docs/data-sources/file),
however it would be overkill as there are only two simple lines in our
inventory at this point. A `local_file` is created upon `terraform apply` and
deleted upon `terraform destroy`. Therefore it doesn't even need to be tracked
by our VCS:

```
resource "local_file" "ansible_inventory" {
  content  = <<-EOF
[all]
${linode_instance.nanode.ip_address} ansible_user=root
EOF
  filename = "inventory.ini"
  file_permission = "0644"
}
```

Once we run terraform (plan + apply), an `inventory.ini` file should be created
with the above contents.

Because the IP address is ephemeral and dynamic, we should have a
straightforward way to see its value. A terraform
[`output`](https://developer.hashicorp.com/terraform/language/values/outputs)
is perfect for that:

```terraform
% cat outputs.tf
output "ip_address" {
  value = linode_instance.nanode.ip_address
}
```

Later on (after terraforming) we will be able to use `terraform output` to see
the server IP address.

We have the inventory file. Now we need a
[playbook](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html).
A playbook contains a sequence of tasks to be applied to our server.

Let's start with a basic playbook that just installs and starts `nginx`:

```yaml
---
- hosts: all
  tasks:
    - name: Install the web server (nginx)
      community.general.apk:
        name: nginx
        state: present
    - name: Start the web server
      service:
        name: nginx
        state: started
```

Save this to a `playbook.yml` file.

After terraforming, we should now be able to run ansible:

```shell
% ansible-playbook -i inventory.ini playbook.yml
```

In order to make this setup more ergonomic, let's create a `Makefile`:

```makefile
TERRAFORM := terraform

all: terraform ansible

ansible:
	ansible-playbook -i inventory.ini playbook.yml

terraform:
	$(TERRAFORM) init
	$(TERRAFORM) plan
	$(TERRAFORM) apply

clean:
	$(TERRAFORM) destroy

.PHONY: all ansible terraform clean
```

Then we can just run `make terraform` or `make ansible` for granular steps. Or
just `make` to run everything in the right order.

I extracted the `terraform` binary to its own variable because it facilitates
the use of [OpenTofu](https://opentofu.org/) (a fork) in lieu of terraform.

And that's it for today! In a future post, we'll look into extending our
Ansible usage to fully bootstrap Miniflux on the server.
