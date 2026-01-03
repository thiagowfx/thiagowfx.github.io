---
title: "Terraform: rename resources"
date: 2025-03-19T11:40:43+01:00
tags:
  - dev
  - terraform
---

Sometimes I need to make a simple refactoring rename change to a terraform
resource that has already been applied. For example:

```terraform
resource "aws_api_gateway_request_validator" "delete" {
  name                        = "Validate body, query string parameters, and headers"
  rest_api_id                 = aws_api_gateway_rest_api.this.id
  validate_request_body       = true
  validate_request_parameters = true
}
```

to

```terraform
resource "aws_api_gateway_request_validator" "this" {
  name                        = "Validate body, query string parameters, and headers"
  rest_api_id                 = aws_api_gateway_rest_api.this.id
  validate_request_body       = true
  validate_request_parameters = true
}
```

The simplest way to do so is to `terraform apply`. However, that incurs
destruction + re-creation of the resource, which would incur downtime in case
it's already deployed in prod.

The best way is `% terraform state mv
aws_api_gateway_request_validator.{delete,this}`. In-place move, simple and
easy.

When doing it at scale, running multiple `terraform state mv` commands could be
cumbersome.

There's a second way, using the
[`moved`](https://developer.hashicorp.com/terraform/language/moved) block in HCL:

```terraform
moved {
    from = aws_api_gateway_request_validator.delete
    to = aws_api_gateway_request_validator.this
}
```

**Note**: `terraform` docs call this operation "move", instead of "rename".
