---
title: "New script: AWS China MFA login"
date: 2025-10-04T11:34:58+02:00
tags:
  - dev
  - security
---

[Previously]({{< ref "2024-12-17-skopeo-operate-container-images-and-registries" >}}).

[aws_china_mfa](https://github.com/thiagowfx/pancake/tree/5c4122f7ee0dd7917b3f21054a8e7d6b7101687a/aws_china_mfa):

> A script to authenticate to AWS China using MFA and export temporary session credentials.

The idea is simple. To log into AWS, we need the following environment variables
to be defined:

```shell
export AWS_PROFILE='china'
export AWS_ACCESS_KEY_ID='AKIAWHEATLICIOUSPANCAK'
export AWS_SECRET_ACCESS_KEY='wSyrupyDeliciousSecretKeyForBreakfastDelight42'
export AWS_SESSION_TOKEN='FwoGZXIvYXdzEBaaDCakesYrUpSWeetToKenArEDelIcIoUs...'
```

`AWS_PROFILE` is static and can be hard-coded. It's also possible to supply it
to the `aws` CLI via `--profile`.

The other three are fetched upon a successful authentication against AWS, using
MFA (multi-factor authentication) with an OTP.

The usage experience of the script is like this:

```shell
% ./aws_china_mfa.sh
Note: Script is being executed. To apply credentials, run:
  eval "$(./aws_china_mfa.sh china)"

Using AWS profile: china
Enter the MFA token code for your AWS China account: 123456
Retrieving MFA device ARN...
Requesting session token...

  export AWS_PROFILE='china'
  export AWS_ACCESS_KEY_ID='AKIAWHEATLICIOUSPANCAK'
  export AWS_SECRET_ACCESS_KEY='wSyrupyDeliciousSecretKeyForBreakfastDelight42'
  export AWS_SESSION_TOKEN='FwoGZXIvYXdzEBaaDCakesYrUpSWeetToKenArEDelIcIoUs...'

✓ Successfully authenticated to AWS China

Copy and paste the export commands above to apply credentials.
```

The script prompts the user for an OTP; that's the only input.

There are three ways to execute it:

- source it: the variables are then exported directly
- eval it: ditto
- execute it: in this mode it's not possible to export the variables. Instead,
  they are simply printed to stdout, and there's a message instructing the user
  to manually copy and paste the exports

Later on I added integration with 1Password, via `--op-account` and `--op-item`,
so that the OTP can be retrieved directly from it, without any user intervention
or interruption – besides using biometrics (touch ID) to confirm the
operation.
