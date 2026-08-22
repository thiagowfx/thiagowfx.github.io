---
title: "azure disk: resize needs the PVC patch too"
url: https://perrotta.dev/2026/08/azure-disk-resize-needs-the-pvc-patch-too/
last_updated: 2026-08-22
---


**Problem statement**: a Prometheus pod crash-looped on a full 128GiB volume. I
resized the Azure-managed disk to 256Gi in the Azure Portal (ClickOps) to no
avail.

The disk _really_ was bigger:

```shell
% az disk show -g my-cluster-k8s-nodes \
    -n pvc-86ac2c66-fb67-43c3-84b0-7209f3a23bd3 -o json | \
    jq '{diskSizeGB, diskState, provisioningState}'
{
  "diskSizeGB": 256,
  "diskState": "Attached",
  "provisioningState": "Succeeded"
}
```

Kubernetes disagreed though (well, it didn't know about the resize yet):

```shell
% kubectl -n monitoring get pvc prometheus-...-prometheus-0 -o json | \
    jq '{spec: .spec.resources.requests, status: .status.capacity, alloc: .status.allocatedResources}'
{
  "spec": {"storage": "128Gi"},
  "status": {"storage": "128Gi"},
  "alloc": null
}
```

`allocatedResources: null` means no resize was ever requested. Growing the disk
in Azure doesn't tell the CSI driver anything, so nobody ran `resize2fs`, and
the filesystem stayed exactly where it was:

```shell
% kubectl -n monitoring exec prometheus-...-prometheus-0 -c thanos-sidecar -- df -h /prometheus
Filesystem                Size      Used Available Use% Mounted on
/dev/sda                124.9G    123.0G      1.9G  98% /prometheus
```

The fix is to **patch the PVC** so the control plane catches up.
`disk.csi.azure.com` sees the block device is already large enough, skips the
Azure API call, and goes straight to the filesystem:

```shell
% kubectl -n monitoring patch pvc prometheus-...-prometheus-0 \
    -p '{"spec":{"resources":{"requests":{"storage":"256Gi"}}}}'
persistentvolumeclaim/prometheus-...-prometheus-0 patched
```

```shell
% kubectl -n monitoring exec prometheus-...-prometheus-0 -c thanos-sidecar -- df -h /prometheus
Filesystem                Size      Used Available Use% Mounted on
/dev/sda                250.9G    124.6G    126.4G  50% /prometheus
```

42MB free became 126.4GB, and the pod went `3/3 Running` after 203 crashes.

The lesson: patch the PVC and then let CSI follow up.

Resizing in Azure first just creates a split state where the volume is bigger
but nothing can use it.

- - -

🤖 *Drafted with [`/bloggify`](https://github.com/thiagowfx/skills/blob/master/plugins/thiagowfx/skills/bloggify/SKILL.md).*

