
Terraform supports [state
locking](https://developer.hashicorp.com/terraform/language/state/locking):

> If supported by your backend, Terraform will lock your state for all
> operations that could write state. This prevents others from acquiring the
> lock and potentially corrupting your state.

Neat, right?

```shell
% op run --env-file=.env -- terraform plan
╷
│ Error: Error acquiring the state lock
│
│ Error message: operation error S3: PutObject, https response error
│ StatusCode: 412, RequestID: {redacted}, HostID:
│ {redacted},
│ api error PreconditionFailed: At least one of the pre-conditions you
│ specified did not hold
│ Lock Info:
│   ID:        {redacted}
│   Path:      {redacted}/chartmuseum.tfstate
│   Operation: OperationTypePlan
│   Who:       {redacted}
│   Version:   1.10.5
│   Created:   2025-08-04 09:46:55.995791 +0000 UTC
│   Info:
│
│
│ Terraform acquires a state lock to protect the state from being written
│ by multiple users at the same time. Please resolve the issue above and try
│ again. For most commands, you can disable locking with the "-lock=false"
│ flag, but this is not recommended.
```

It even uses a custom [HTTP
Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/412):

> **The HTTP 412 Precondition Failed** _client error response status code_
> indicates that access to the target resource was denied. This happens with
> conditional requests on methods other than GET or HEAD when the condition
> defined by the If-Unmodified-Since or If-Match headers is not fulfilled. In
> that case, the request (usually an upload or a modification of a resource)
> cannot be made and this error response is sent back.

If you're sure no one else is working on that workspace, you can proceed with
`-lock=false`:

```shell
% op run --env-file=.env -- terraform plan -lock=false
uptime_check_http.chartmuseum: Refreshing state... [name=chartmuseum]
data.aws_availability_zones.available: Reading...
data.aws_availability_zones.available: Read complete after 1s [id=us-east-1]
[...]
```

That's an one-off. A subsequent run without that argument will fail again:

```shell
% op run --env-file=.env -- terraform plan
╷
│ Error: Error acquiring the state lock
[...]
```

In this case it would be better to simply remove the lock with
[`force-unlock`](https://developer.hashicorp.com/terraform/language/state/locking#force-unlock):

```shell
% op run --env-file=.env -- terraform force-unlock {lock-id}
Do you really want to force-unlock?
  Terraform will remove the lock on the remote state.
  This will allow local Terraform commands to modify this state, even though it
  may still be in use. Only 'yes' will be accepted to confirm.

  Enter a value: yes

Terraform state has been successfully unlocked!

The state has been unlocked, and Terraform commands should now be able to
obtain a new lock on the remote state.
```

The `lock-id` can be obtained from the `plan` output.

Now we can `plan` as usual:

```shell
% op run --env-file=.env -- terraform plan
uptime_check_http.chartmuseum: Refreshing state... [name=chartmuseum]
data.aws_availability_zones.available: Reading...
data.aws_availability_zones.available: Read complete after 0s [id=us-east-1]
[...]
```

