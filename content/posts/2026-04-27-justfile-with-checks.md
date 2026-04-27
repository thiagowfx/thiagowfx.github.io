---
title: "Justfile with checks"
date: 2026-04-27T10:42:00+02:00
tags:
  - bestof
  - dev
  - serenity
---

[Previously]({{< ref "2024-12-13-just" >}}).

I love [`just`](https://just.systems/) to manage a small collection of related
scripts within a given codebase. An example in our Terraform codebase[^1]:

```shell
% just check-{hit TAB for completion}
completing values
check-aws-config         -- Validate AWS profiles in ~/.aws/config
check-aws-provider-tags  -- Check AWS provider default_tags configuration
check-backend-locking    -- Verify S3 backends have use_lockfile = true
check-import-blocks      -- Check for Terraform import blocks
check-lockfiles          -- Check that all projects have lockfiles
check-moved-blocks       -- Check for Terraform moved blocks
check-secret-accounts    -- Check expected_account_id in terraform-secrets
check-secrets-tf         -- Validate secrets.tf file structure
check-shared-values      -- Check for hardcoded values that duplicate shared modules
check-stacks             -- Verify garden projects have correct stack tags
check-terraform-version  -- Validate .terraform-version format
check-terrateam-tags     -- Verify projects are tagged in Terrateam config
check-tfdocs             -- Check that all README.md have TF_DOCS blocks
```

Adopting a common prefix (`check-`) improves their discoverability.

There's no need to rely on interactivity to take advantage of `just`:

```shell
% just --list
Available recipes:
    default                                            # Show categorized help for available commands
    help                                               # Display categorized help for available commands

[...]

    [terraform]
    apply module_path=invocation_directory() *args=""  # Run terraform apply
    clean module_path=invocation_directory()           # Remove .terraform artifacts
    destroy module_path *args=""                       # Run terraform destroy
    fmt module_path=invocation_directory() *args=""    # Format terraform files
    import module_path *args=""                        # Run terraform import
    init module_path=invocation_directory() *args=""   # Initialize terraform with backend config
    output module_path=invocation_directory() *args="" # Show terraform outputs
    plan module_path=invocation_directory() *args=""   # Run terraform plan
    providers-lock module_path=invocation_directory() *args="" # Lock providers for multiple platforms
    refresh module_path=invocation_directory() *args="" # Run terraform refresh
    show module_path=invocation_directory() *args=""   # Show terraform state or plan
    stack-apply *args=""                               # Apply projects in Terrateam stack order (--dry-run for preview)
    stack-plan *args=""                                # Plan projects in Terrateam stack order
    state module_path=invocation_directory() *args=""  # Run terraform state commands
    test module_path=invocation_directory() *args=""   # Run terraform tests
    unlock *args=""                                    # Force unlock state lock (auto-detects lock ID) [alias: force-unlock]
    upgrade module_path=invocation_directory() *args="" # Upgrade providers to latest versions
    validate module_path=invocation_directory() *args="" # Validate terraform configuration

[...]
```

Justfile [groups]({{< ref "2026-02-21-justfile-groups" >}}) enhance `--list` by
grouping(!) entries together.

This is what a typical entry looks like:

```just {filename="Justfile"}
[doc('Validate AWS profiles in ~/.aws/config')]
[group('checks')]
check-aws-config:
    @./ci/check_aws_config.sh
```

`just` is _just_ (pun intended) a glue for various shell and Python scripts in
`ci/`.

[^1]: I wrote all of these.
