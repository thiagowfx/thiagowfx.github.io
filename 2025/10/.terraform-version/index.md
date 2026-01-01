
`.terraform-version` at the root of a git repository is recognized by various
tools:

- [tfenv](https://github.com/tfutils/tfenv#terraform-version-file)
- [tfswitch](https://tfswitch.warrensbox.com/usage/config-files/#use-versiontf-file)
- [terrateam](https://docs.terrateam.io/integrations/iac-tools/terraform)

You would expect the
[`hashicorp/setup-terraform`](https://github.com/hashicorp/setup-terraform)
github action would also recognize it out-of-the-box, but it does not. We can
address this gap by reading it manually:

```
jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
        with:
          persist-credentials: false

      - name: Read Terraform version
        id: terraform-version
        run: echo "version=$(cat .terraform-version)" >> "$GITHUB_OUTPUT"

      - uses: hashicorp/setup-terraform@b9cd54a3c349d3f38e8881555d616ced269862dd # v3.1.2
        with:
          terraform_version: ${{ steps.terraform-version.outputs.version }}
```

There's a [feature
request](https://github.com/hashicorp/setup-terraform/issues/298) for it.

