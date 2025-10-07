---
title: "macOS homebrew: downgrade a package"
date: 2025-10-07T10:47:02+02:00
tags:
  - dev
---

Yesterday we could no longer ssh to deploy servers (via a ruby-based wrapper we
use).

This was bad™.

The error message looked like this:

```
[...]
Seahorse::Client::NetworkingError: SSL_connect returned=1 errno=0 peeraddr={redacted}:443 state=error: certificate verify failed (unable to get certificate CRL)
/Users/thiago.perrotta/.rbenv/versions/3.2.4/lib/ruby/3.2.0/net/protocol.rb:46:in `connect_nonblock'
/Users/thiago.perrotta/.rbenv/versions/3.2.4/lib/ruby/3.2.0/net/protocol.rb:46:in `ssl_socket_connect'
/Users/thiago.perrotta/.rbenv/versions/3.2.4/lib/ruby/3.2.0/net/http.rb:1674:in `connect'
/Users/thiago.perrotta/.rbenv/versions/3.2.4/lib/ruby/3.2.0/net/http.rb:1580:in `do_start'
/Users/thiago.perrotta/.rbenv/versions/3.2.4/lib/ruby/3.2.0/net/http.rb:1575:in `start'
/Users/thiago.perrotta/.rbenv/versions/3.2.4/lib/ruby/3.2.0/delegate.rb:87:in `method_missing'
[...]
```

It was an error in OpenSSL.

There had been a new release a few days earlier,
[3.6.0](https://github.com/openssl/openssl/releases/tag/openssl-3.6.0).

Suspicious!

In order to restore our ability to ssh to deploy servers as quickly as possible,
we decided to downgrade to 3.5.

This proved to be a bit more painful than it should have been in 2025:

```shell
brew install openssl@3.5
brew pin openssl@3.5  # prevent upgrades
brew uninstall --ignore-dependencies openssl@3
```

`--ignore-dependencies` is needed because there is a ton of packages that depend
on OpenSSL.

This is not enough.

Using our ruby-based tool to ssh into servers would yield another error. The
tool was still trying to use OpenSSL 3.6.0, as the library paths were
hard-coded. Ugh.

New attempt:

```shell
rbenv install 3.3.9   # compile / install a new version of ruby -> it will link against OpenSSL 3.5
$EDITOR <mulch>/.ruby-version   # upgrade to the version above
```

Installing a new version of ruby ends up compiling / linking libraries against
OpenSSL 3.5. Now we regained the ability to ssh.

Now let's investigate the root cause.

There was no bug report in homebrew.

Next: OpenSSL. [#28758](https://github.com/openssl/openssl/issues/28758):

> OpenSSL 3.6.0 results in error: certificate verify failed (unable to get certificate CRL) #28758

Yes! That's the one.

From there, someone linked to
[`ruby/openssl`](https://github.com/ruby/openssl/issues/949) (a core gem), which
was precisely the issue we were having.

There was another workaround in that thread, but we didn't need it.

Eventually a fix was
[released](https://github.com/ruby/openssl/issues/949#issuecomment-3370358680).

I thought to run `gem update openssl` (or similar) to incorporate it, but it
turned out that `openssl` is a system gem, therefore it was not listed in our
`Gemfile.lock`.

A workaround: explicitly add it to our `gemspec`:

```ruby
spec.add_runtime_dependency 'openssl', '~> 3.2.2'
```

Then run `bundle install`.

Now everything works. We can undo the original workaround:

```
brew unpin openssl@3.5
brew uninstall openssl@3.5
brew install openssl@3
```
