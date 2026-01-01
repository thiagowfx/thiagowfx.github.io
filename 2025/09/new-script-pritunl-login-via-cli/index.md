
[Previously]({{< ref "2024-05-07-pritunl-log-in-via-cli" >}}).

Now, instead of a shell function, it evolved to a [dedicated
script](https://github.com/thiagowfx/pancake/tree/7d35c10b4f8cccd61142bbca7a5d01e81cd5feed/pritunl_login)
in [pancake](https://github.com/thiagowfx/pancake).

In my opinion it's quite user-friendly:

```
% pritunl_login.sh stark-industries 'op://Employee/x9zm2kddpq4nvbwrfhgtsjloey/password'
Connecting to Pritunl VPN...
Account: stark-industries
Password reference: op://Employee/x9zm2kddpq4nvbwrfhgtsjloey/password

Getting Pritunl profile ID...
Using profile ID: a1b2c3d4e5f6g7h8
Retrieving credentials from 1Password...
Starting VPN connection...
✓ VPN connection started successfully

Current VPN status:
| ID               | NAME             | STATE  | AUTOSTART | ONLINE FOR     | SERVER ADDRESS | CLIENT ADDRESS |
|------------------|------------------|--------|-----------|----------------|----------------|----------------|
| a1b2c3d4e5f6g7h8 | Stark Industries | Active | Enabled   | 1 hour 52 mins | 203.0.113.42   | 10.0.0.15      |
```

