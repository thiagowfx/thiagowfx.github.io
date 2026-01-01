
**Problem statement**: Given a docker repository hosted in
[ECR](https://aws.amazon.com/ecr/) (AWS), list its **most recent** image tags.

Assuming you're already authenticated to AWS in the CLI:

```shell
% aws ecr describe-images \
  --repository-name {corp}/{repo} \
  --filter tagStatus=TAGGED \
  --query 'reverse(sort_by(imageDetails, &imagePushedAt))[*].{Tag: imageTags[0], PushedAt: imagePushedAt}' \
  [--output table]
```

The output looks like this:

```
-------------------------------------------------------------------------------------------
|                                     DescribeImages                                      |
+-----------------------------------+-----------------------------------------------------+
|             PushedAt              |                         Tag                         |
+-----------------------------------+-----------------------------------------------------+
|  2025-08-14T14:44:49.285000+02:00 |  1.0.2                                              |
|  2025-08-14T14:07:53.526000+02:00 |  app-839403421                                      |
|  2025-08-07T19:38:21.452000+02:00 |  app-1134bfa1d                                      |
|  2025-08-06T14:54:23.314000+02:00 |  app-pr-5033-07f01dd66                              |
|  2025-08-06T14:33:27.171000+02:00 |  app-pr-5033-643536a2b                              |
|  2025-07-23T09:36:20.368000+02:00 |  app-pr-4947-fe5f4c618                              |
|  2025-04-17T03:17:30.937000+02:00 |  1.0.1                                              |
|  2024-12-18T18:50:18.990000+01:00 |  latest                                             |
|  2024-12-05T17:52:09.775000+01:00 |  1.0.0                                              |
+-----------------------------------+-----------------------------------------------------+
```

If you omit `--output table`, it emits JSON instead.

This is faster than logging into the AWS Console.

