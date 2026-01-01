
[terraformer](https://github.com/GoogleCloudPlatform/terraformer):

> CLI tool to generate terraform files from existing infrastructure (reverse
> Terraform). Infrastructure to Code

In other words: "reverse terraform".

I was quite excited to add this project to my tool belt, as it can save a lot of
time with scaffolding and `terraform import` commands.

Then [Claude Code](https://www.claude.com/product/claude-code), once again,
surprised me.

It turns out there's absolutely no need to adopt `terraformer` if you have a
superb agent available and a few cents/dollars to spare.

Claude can figure out which CLI arguments to pass to `aws`, `az`, etc. to list
all relevant cloud resources. Then it can generate / scaffold a basic set of
Terraform files to manage them[^1]. And then it can craft an one-off shell or
python script to import them all in terraform.

Easy. Quick. Painless.

The interesting part is that I had initially asked Claude to explicitly use
_terraformer_ to do so, but it turned out to be more complicated / less
efficient than having the agent perform the task _directly_.

I am sorry if you were expecting a `terraformer` tutorial.

[^1]: You'll need to refactor these later for maintainability.

