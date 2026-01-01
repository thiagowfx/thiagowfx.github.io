
When using file managers, we're used to moving files to the Trash instead of
deleting them immediately from our systems[^1]. This is an universal pattern across
all major operating systems.

When using the command line, we're conditioned to using `rm` for files and `rm
-r` for directories. This provides no chance for regret on accidental deletions.

An evolution of this pattern is to use `trash` in the command-line as well.

Newer versions of macOS ([since
14](https://mjtsai.com/blog/2025/08/26/the-trash-command/)) come with
`/usr/bin/trash`, exactly for this purpose. From `man trash`:

> trash – Moves files and directories to the user trash folder

Linux systems can install
[`trash-cli`](https://repology.org/project/trash-cli/versions)
([source](https://github.com/andreafrancia/trash-cli)), which is available in
most distributions.

Paired with [`autotrash`](https://bneijt.nl/pr/autotrash/), we attain a clever
pattern to keep our systems tidy:

> Autotrash is a simple Python script which will purge files from your trash
> based on their age or the amount of free space left on the device. Using
> autotrash -d 30 will delete files which have been in the trash for more then
> 30 days. It uses the FreeDesktop.org Trash Info files included in the new
> GNOME system to find the correct files and the dates they where deleted.

`autotrash` can be easily integrated with the system cron and/or systemd timers.

[^1]: Deletion with `rm` is an
    [illusion](https://man.archlinux.org/man/shred.1).

