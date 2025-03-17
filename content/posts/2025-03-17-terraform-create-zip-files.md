---
title: "Terraform: create zip files"
date: 2025-03-17T21:06:28+01:00
tags:
  - dev
---

When creating `.zip` files with terraform, for example, with the purpose of
uploading them to an [AWS Lambda](https://aws.amazon.com/lambda/), at least two
approaches exist to do so.

In the examples below, assume a NodeJS source file named `index.mjs`. It should
be packaged into a `lambda.zip` archive.

## 1) Use [`null_resource`](https://registry.terraform.io/providers/hashicorp/null/latest/docs/resources/resource)

```terraform
resource "null_resource" "build_lambda" {
  triggers = {
    source_code_hash = filebase64sha256("${path.module}/lambda/index.mjs")
  }

  provisioner "local-exec" {
    command = <<EOF
            cd ${path.module}/lambda
            zip -r lambda.zip index.mjs
        EOF
  }
}

resource "aws_lambda_function" "this" {
  function_name = "dns-changer-delete"
  role          = aws_iam_role.this.arn

  filename         = "${path.module}/lambda/lambda.zip"
  source_code_hash = filebase64sha256("${path.module}/lambda/lambda.zip")
  handler          = "index.handler"
  runtime          = "nodejs22.x"

  depends_on = [null_resource.build_lambda]
}
```

## 2) Use [`archive_file`](https://registry.terraform.io/providers/hashicorp/archive/latest/docs/resources/file)

```terraform
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/lambda/index.mjs"
  output_path = "${path.module}/lambda/lambda.zip"
}

resource "aws_lambda_function" "this" {
  function_name = "dns-changer-delete"
  description   = "Delete DNS record sets for DNS Changer"
  role          = aws_iam_role.this.arn

  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  handler          = "index.handler"
  runtime          = "nodejs22.x"

  depends_on = [data.archive_file.lambda_zip]
}
```

I prefer the second approach.

Furthermore, it only requires one `terraform apply` per file update, whereas
the first one requires two.
