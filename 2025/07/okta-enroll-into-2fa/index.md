
More specifically, enroll into 2FA other than
[OTP](https://en.wikipedia.org/wiki/One-time_password).

- Log into https://{company}.okta.com/
- Go to Settings (https://{company}.okta.com/enduser/settings)
- Under "Security Key or Biometric Authenticator", click "Set up another"
- From this point, you could add _either_:
  - a hardware security key (e.g. [YubiCo](https://www.yubico.com/))
  - a [passkey](http://passkeys.dev/), which will be stored in your password
    manager, iCloud Keychain (Apple devices) or web browser profile

A hardware security key needs to be plugged in during authentication, when it
needs to be gently tapped.

A passkey does not require external hardware, but it requires you to be logged
into wherever it is stored (e.g. your password manager or your Apple ID).

What is the motivation to do this?

Previously, I would need to open up my laptop lid to touch ID, which is quite
inconvenient in clamshell mode (i.e. with the laptop lid closed).

Now, touching the security key or signing in with the passkey eliminates the
need to do so.

