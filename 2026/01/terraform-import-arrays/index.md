
Given an existing resource
`module.atlas_mongo_external.mongodbatlas_alert_configuration.maintenance_no_longer_needed[0]`
to be imported into terraform state through an
[`imports.tf`](https://developer.hashicorp.com/terraform/language/v1.14.x/import/bulk?page=import&page=bulk)
file with [`import`](https://developer.hashicorp.com/terraform/language/import)
blocks, a targeted imported can be performed like this:

```shell
terraform apply -target='module.atlas_mongo_external.mongodbatlas_alert_configuration.maintenance_no_longer_needed[0]'
```

Nothing special here.
The "TIL" bit of the day is that the array suffix `[0]` is not needed:

```shell
terraform apply -target='module.atlas_mongo_external.mongodbatlas_alert_configuration.maintenance_no_longer_needed'
```

...works as well.

It feels like a silly optimization to know about but, when you double-click the
resource name in most terminal emulators, only
`module.atlas_mongo_external.mongodbatlas_alert_configuration.maintenance_no_longer_needed`
gets selected by default, stopping right before `[`.

