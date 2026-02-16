
If you ever find yourself in a hurry to get access to a Linux shell but don't
easily have one at hand (e.g. a workstation or a raspberry pi or a VPS), it's
possible to quickly get access to an ephemeral instance in the cloud.

Here's a non-exhaustive list of trusted providers:

## [Google Cloud Shell][google]

> Welcome to Google Cloud Shell, a tool for managing resources hosted on Google
> Cloud Platform! The machine comes pre-installed with the Google Cloud SDK and
> other popular developer tools.
>
> Your 5GB home directory will persist across sessions, but the VM is ephemeral
> and will be reset approximately 20 minutes after your session ends. No
> system-wide change will persist beyond that.
>
> Type "gcloud help" to get help on using Cloud SDK. For more examples, visit
> https://cloud.google.com/shell/docs/quickstart and
> https://cloud.google.com/shell/docs/examples
>
> Type "cloudshell help" to get help on using the "cloudshell" utility.  Common
> functionality is aliased to short commands in your shell, for example, you
> can type `dl <filename>` at Bash prompt to download a file. Type "cloudshell
> aliases" to see these commands.
>
> Type "help" to see this message any time. Type "builtin help" to see Bash
> interpreter help.

See also: https://cloud.google.com/shell

## [Github Codespaces][github]

> 👋 Welcome to Codespaces! You are on our default image.
>
> — It includes runtimes and tools for Python, Node.js, Docker, and more.
>   See the full list here: https://aka.ms/ghcs-default-image
> — Want to use a custom image instead? Learn more here:
>   https://aka.ms/configure-codespace
>
> 🔍 To explore VS Code to its fullest, search using the Command Palette
> (Cmd/Ctrl + Shift + P or F1).
>
> 📝 Edit away, run your app as usual, and we'll automatically make it
> available for you to access.

See also: https://github.com/codespaces

**Tip**: Replace `https://github.com/username/repository` with
`https://github.dev/username/repository` to automatically open the
repository within a github codespace. Alternatively, if you have
github shortcuts enabled, press `.` while in the repository page.

[github]: http://github.dev/
[google]: https://shell.cloud.google.com/?pli=1&show=ide&environment_deployment=ide

