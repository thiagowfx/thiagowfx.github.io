---
title: "HashiCorp Vault from helm values"
date: 2025-04-23T16:56:16+02:00
tags:
  - dev
  - kubernetes
  - security
---

**Problem statement**: Populate HashiCorp Vault with select keys from `helm get
values` for a given chart release.

The following script works:

```shell
#!/bin/bash
# Usage: Tweak entries as needed and then run the script.

set -euo pipefail

# It's an associative array: a dictionary, a hash map
#
#   Key: the entry to be populated in vault
#   Value: a `jq` JSON selector from the output of `helm get values -o json`
declare -A entries=(
    # keep-sorted start
    [config.aws.accessKey]=".config.aws.accessKey"
    [config.aws.secretKey]=".config.aws.secretKey"
    [config.cronjob.apiPassword]=".config.cronjob.apiPassword"
    [config.cronjob.apiUser]=".config.cronjob.apiUser"
    [config.postgresql.adminpass]=".config.postgresql.adminpass"
    [config.postgresql.password]=".config.postgresql.password"
    [config.postgresql.ropass]=".config.postgresql.ropass"
    [config.postgresql.rwpass]=".config.postgresql.rwpass"
    [config.slack.token]=".config.slack.token"
    [config.slack.verificationToken]=".config.slack.verificationToken"
    # keep-sorted end
)

main() {
        vault login

        FIRST=1
        for entry in "${!entries[@]}"; do
                key="$entry"
                value="${entries[$entry]}"
                content="$(helm get values -n tools mychart -o json | jq -r "$value")"

                echo "Populating vault $key from helm value $key: $content..."

                if [[ "$FIRST" == "1" ]]; then
                  vault kv put -mount="kv-v2" "services/mychart/" "$key=$content"
                  FIRST=0
                else
                  vault kv patch -mount="kv-v2" "services/mychart/" "$key=$content"
                fi
        done

        vault kv get -mount="kv-v2" "services/mychart"

        rm ~/.vault-token
}

main
```

`FIRST`: In the first time we need to create an entry (`vault kv put`), in the
second time we need to patch it (`vault kv patch`).
