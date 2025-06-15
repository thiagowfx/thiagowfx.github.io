---
title: "Shell text substitution"
date: 2024-04-07T23:13:09+02:00
tags:
  - dev
---

I learned a neat shell trick this week. In both `bash` and `zsh` you can use the
circumflex / caret (`^`) symbol to find & replace a word from the previous
command.

Usage: `^prev^next`. It's best illustrated with examples:


## terraform

Instead of running:

```shell
terraform init -var-file /path/to/foo.tfvars
terraform plan -var-file /path/to/foo.tfvars
terraform apply -var-file /path/to/foo.tfvars
```

Run:

```shell
terraform init -var-file /path/to/foo.tfvars
^init^plan
^plan^apply
```

## systemd

Instead of running:

```shell
sudo systemctl restart nginx
sudo systemctl status nginx
```

Run:

```shell
sudo systemctl restart nginx
^restart^status
```

## one observation

`zsh` will run the substitution right away, whereas `bash` will allow you
to review and edit the replaced command before running it.
