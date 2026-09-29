---
title: "terraform: destroy a deleted project from git history"
date: 2026-09-17T14:15:09+02:00
tags:
  - bloggify
  - dev
  - git
  - terraform
---

**Problem statement**: how can I run `terraform destroy` after deleting a
project from the current Git checkout?

Deleting Terraform configuration does not destroy resources from its old
state. My `just destroy` wrapper could no longer find the project:

```text
% just destroy g08-opencost
Resolved path: g08-opencost
Error handling -chdir option: chdir g08-opencost: no such file or directory
error: recipe `destroy` failed with exit code 1
```

The last usable configuration is the parent of the commit that deleted its
path. I taught the recipe to find and extract that revision into a temporary
directory:

```diff
-    resolved_path=$(just _resolve_and_echo "{{ module_path }}")
+    resolved_path=$(just _resolve_path "{{ module_path }}")
+    historical_checkout=""
+    cleanup() {
+        if [[ -n "$historical_checkout" ]]; then
+            rm -rf "$historical_checkout"
+        fi
+    }
+    trap cleanup EXIT
+
+    if [[ ! -d "$resolved_path" ]]; then
+        project_name="${resolved_path%/}"
+        project_name="${project_name##*/}"
+        project_path="standalone/$project_name"
+        deletion_commit=$(git log -1 --format=%H --diff-filter=D -- "$project_path")
+
+        if [[ -z "$deletion_commit" ]] || ! git cat-file -e "$deletion_commit^:$project_path" 2>/dev/null; then
+            just _error "Project not found in current checkout or Git history: {{ module_path }}"
+            exit 1
+        fi
+
+        historical_commit=$(git rev-parse "$deletion_commit^")
+        historical_checkout=$(mktemp -d)
+        git archive "$historical_commit" | tar -x -C "$historical_checkout"
+        resolved_path="$historical_checkout/$project_path"
+        just _info "Project was deleted. Using $project_path from commit ${historical_commit:0:12}."
+    fi
```

The normal backend initialization and destroy path can then run unchanged:

```text
% just destroy g08-opencost
Project was deleted. Using standalone/g08-opencost from commit fb82317c0010.
Resolved path: /var/folders/yr/6sw3yylx6gjcy5jr38d6j6000000gn/T/tmp.0als997N54/standalone/g08-opencost
...
Plan: 0 to add, 0 to change, 8 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value:
Error: error asking for approval: EOF

Releasing state lock. This may take a few moments...
```

No automatic approval: the historical configuration only gets Terraform back
to its usual confirmation prompt.
