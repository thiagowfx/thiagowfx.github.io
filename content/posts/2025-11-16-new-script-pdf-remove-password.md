---
title: "new script: PDF remove password"
date: 2025-11-16T20:19:18-03:00
tags:
  - bestof
  - dev
  - selfhosted
  - serenity
---

[Previously]({{< ref "2025-11-04-new-script-copy" >}}).

**Problem statement**: Given a password-protected `.pdf` file, remove its
password. It's indifferent whether the file gets overwritten or whether a new
one is created.

[`ghostscript`](https://gist.github.com/pstaender/7412245) can do it:

```shell
gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=output.pdf -c .setpdfwrite -f input.pdf
```

[`qpdf`](https://gist.github.com/raghur/f3eab7297691f2f411eec69b8032daf0) can do it:

```shell
qpdf --decrypt --password="{my pass}" input.pdf output.pdf
```

I am not expected to memorize these CLI flags.

I do not want to look them up every time either.

There are various approaches to tackle this:

- a shell alias (`alias foo=`)
- a shell function `foo() {}`
- a shell script (`*.sh`)
- a [comma script]({{< ref "2025-10-10-comma-scripts" >}})
- a copyable snippet (e.g. stored in Obsidian / LogSeq or some other digital
  garden / personal wiki / second brain app)
- a snippet (e.g. in [RayCast]({{< ref "2025-10-10-comma-scripts" >}}) or
  [Espanso]({{< ref "2025-10-10-comma-scripts" >}}))
- ask the AI each time
- ~~google~~ [search]({{< ref "2025-05-04-kagi" >}}) for it each time

Lately I've been favouring the [shell script]({{< ref "2025-09-25-pancake-potpourri-scripts" >}}) approach, so [here we go](https://github.com/thiagowfx/pancake/tree/c7c3677119c567edc432fcc1f1c0f78c9a5b3c55/pdf_password_remove) with `pdf_password_remove.sh`:

## Usage

Remove password protection from PDF files.

```bash
# Interactive password prompt (most secure)
pdf_password_remove secret.pdf

# Process multiple files
pdf_password_remove report.pdf invoice.pdf contract.pdf

# Provide password via command line
pdf_password_remove --password=BANANA42SPLIT secret.pdf

# Custom output filename (single file only)
pdf_password_remove -o unlocked.pdf secret.pdf
```

## Example Output

```
% pdf_password_remove --password=PIZZA69SLICE financial-report.pdf tax-form.pdf
✓ Successfully processed: financial-report.pdf → financial-report-unlocked.pdf
✓ Successfully processed: tax-form.pdf → tax-form-unlocked.pdf

Summary: Successfully processed 2/2 file(s)
```

## Features

- Process single or multiple PDF files in one command
- Secure interactive password prompt (hidden input)
- Command-line password option for automation/scripts
- Default output naming: adds `-unlocked` suffix
- Custom output filename with `-o` flag (single file only)
- Clear success/failure indicators for each file
- Validates PDF files before processing

## Prerequisites

Requires either `ghostscript` (preferred) or `qpdf` to be installed:

```bash
# macOS
brew install ghostscript       # Preferred
brew install qpdf              # Alternative

# Linux
sudo apt install ghostscript   # Preferred - Debian/Ubuntu
sudo apt install qpdf          # Alternative

sudo dnf install ghostscript   # Preferred - Fedora
sudo dnf install qpdf          # Alternative

sudo pacman -S ghostscript     # Preferred - Arch
sudo pacman -S qpdf            # Alternative
```

The script automatically detects and uses whichever tool is available,
preferring ghostscript if both are installed.

## Security Note

Using `--password` on the command line will expose the password in shell history
and process lists. For sensitive documents, use the interactive prompt instead
(default behavior when password is not provided).
