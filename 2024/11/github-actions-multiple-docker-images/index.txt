
**Problem statement**: Given a monorepo on Github with multiple docker images in
it, write a github workflow to build and push all of them.

Here is an abridged version of the resulting workflow. The images are listed one
by one for fine-grained control purposes, but it would also be possible to glob
them with a single command.

```yaml
name: Global services

permissions:
  id-token: write
  contents: read

# Replace with workflow trigger conditions.
on: {}

jobs:
  global-services:
    name: ${{ matrix.image }}
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        include:
          # keep-sorted start
          - dockerfile: path/to/one/Dockerfile
            image: org/one
          - dockerfile: path/to/two/Dockerfile
            image: org/two
          # keep-sorted end
    steps:
      - name: Check out source code
        uses: actions/checkout@v4

      - name: Get git SHA
        id: git-sha
        run: |
          ./scripts/get-versions.sh
          echo "sha=$(grep '^services_sha' versions.yaml | cut -d' ' -f 2)" >> "$GITHUB_OUTPUT"

      - uses: ./.github/actions/setup-ecr-buildx
        id: setup-ecr-buildx

      - name: Build and push global service images
        uses: docker/build-push-action@6.9.0
        with:
            cache-from: type=gha
            cache-to: type=gha,mode=max
            context: path/to
            file: ${{ matrix.dockerfile }}
            provenance: false
            push: true
            tags: ${{ steps.setup-ecr-buildx.outputs.ecr_registry }}/${{ matrix.image }}:${{ steps.git-sha.outputs.sha }}
```

A matrix strategy kicks off independent multiple build jobs all at once.

Docs: https://github.com/docker/build-push-action

