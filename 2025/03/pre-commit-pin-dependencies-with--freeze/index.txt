
**Today I learned**: [`pre-commit
autoupdate`](https://pre-commit.com/#updating-hooks-automatically) has a
`--freeze` option that replaces git tags with SHAs (hashes) on upstream hooks
(dependencies).

Here's how to adopt them, using this blog as an example:

```
% pre-commit autoupdate --jobs $(nproc) --freeze
[https://github.com/lalten/check-gha-pinning] updating v1.3.0 -> v1.3.0 (frozen)
[https://github.com/google/keep-sorted] updating v0.6.0 -> v0.6.0 (frozen)
[https://github.com/sirosen/texthooks] updating 0.6.8 -> 0.6.8 (frozen)
[https://github.com/google/yamlfmt] updating v0.16.0 -> v0.16.0 (frozen)
[https://github.com/pre-commit/pre-commit-hooks] updating v5.0.0 -> v5.0.0 (frozen)
[https://github.com/shssoichiro/oxipng] updating v9.1.3 -> v9.1.4 (frozen)
[https://github.com/codespell-project/codespell] updating v2.4.1 -> v2.4.1 (frozen)
[https://github.com/gitleaks/gitleaks] updating v8.23.3 -> v8.24.0 (frozen)
```

The resulting diff (redacted one of the hooks for brevity):

```diff
diff --git .pre-commit-config.yaml .pre-commit-config.yaml
index 30aac4a2..841eac9b 100644
--- .pre-commit-config.yaml
+++ .pre-commit-config.yaml
@@ -23,7 +23,7 @@ repos:
       - id: check-hooks-apply
       - id: check-useless-excludes
   - repo: https://github.com/pre-commit/pre-commit-hooks
-    rev: v5.0.0
+    rev: cef0300fd0fc4d2a87a85fa2093c6b283ea36f4b  # frozen: v5.0.0
     hooks:
       - id: check-executables-have-shebangs
@@ -41,27 +41,27 @@ repos:
           - -D .codespell-dictionary.txt
           - -I .codespell-ignore-words.txt
   - repo: https://github.com/gitleaks/gitleaks
-    rev: v8.23.3
+    rev: f565e4e10c6c8081e374235bb4e4bcb8c0c2fa63  # frozen: v8.24.0
     hooks:
       - id: gitleaks
   - repo: https://github.com/google/keep-sorted
-    rev: v0.6.0
+    rev: df93c2722b6126556183749880f16a9beb664bb4  # frozen: v0.6.0
     hooks:
       - id: keep-sorted
   - repo: https://github.com/google/yamlfmt
-    rev: v0.16.0
+    rev: ac76bb931851dda64a55ef746ca9b8bb41634b98  # frozen: v0.16.0
     hooks:
       - id: yamlfmt
   - repo: https://github.com/lalten/check-gha-pinning
-    rev: v1.3.0
+    rev: 225deee5dff16fae532978007ce6e37045e14c68  # frozen: v1.3.0
     hooks:
       - id: check-gha-pinning
   - repo: https://github.com/shssoichiro/oxipng
-    rev: v9.1.3
+    rev: bc8c36456858fe4678460bdea520a4ec0bc50dc4  # frozen: v9.1.4
     hooks:
       - id: oxipng
   - repo: https://github.com/sirosen/texthooks
-    rev: 0.6.8
+    rev: 13a42592dd28b6b688bb1c23fa769234984d4ca7  # frozen: 0.6.8
     hooks:
       - id: fix-ligatures
       - id: fix-smartquotes
```

This is useful to mitigate supply-chain attacks such as the recent
[`tj-actions/changed-files`](https://www.wiz.io/blog/github-action-tj-actions-changed-files-supply-chain-attack-cve-2025-30066)
one.

