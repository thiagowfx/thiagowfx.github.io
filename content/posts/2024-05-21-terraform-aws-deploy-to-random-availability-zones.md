---
title: "Terraform: AWS deployment to random availability zones"
date: 2024-05-21T14:31:03+02:00
tags:
  - dev
---

A common scenario: there's a new deployment you would like to roll out to AWS.
Let's say you pick "us-east-1" as your cloud region. There are multiple
availability zones within it:

- us-east-1a
- us-east-1b
- us-east-1c
- us-east-1d
- us-east-1e
- us-east-1f

Suppose you want to pick two of them for your service/app, and you don't
particularly care about which one. How to proceed?


## Option #1: Hard-coding

Pick two arbitrary zones and hard-code them.

```terraform
variable "availability_zones" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.chartmuseum.id
  cidr_block        = element(var.private_subnets, count.index)
  availability_zone = element(var.availability_zones, count.index)
  count             = length(var.private_subnets)
}
```

**Caveat**: [The paradox of
choice](https://www.goodreads.com/book/show/10639.The_Paradox_of_Choice),
unnecessary decision fatigue.

## Option #2: Pick the first two

Use the AWS data source to dynamically find all zones, and pick the first two.

```terraform
data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.chartmuseum.id
  cidr_block        = element(var.private_subnets, count.index)
  availability_zone = element(data.aws_availability_zones.available.names, count.index)
  count             = length(var.private_subnets)
}
```

Note that `terraform plan` should display the full zone list.

**Caveat**: Heavily biased towards the first two zones.

## Option #3: Random shuffling

Pick two zones at random!

```terraform
data "aws_availability_zones" "available" {
  state = "available"
}

resource "random_shuffle" "aws_availability_zone_names" {
  input        = data.aws_availability_zones.available.names
  result_count = 2
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.chartmuseum.id
  cidr_block        = element(var.private_subnets, count.index)
  availability_zone = element(random_shuffle.aws_availability_zone_names.result, count.index)
  count             = length(var.private_subnets)
}
```

**Winner**: In my opinion, this is the most elegant approach.

`random_shuffle` will output the selected regions upon running `terraform
apply`.
