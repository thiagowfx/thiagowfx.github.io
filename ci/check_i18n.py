#!/usr/bin/env python3
"""Enforce that Hugo translation catalogs match English catalog structure."""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path


I18N_DIR = Path("i18n")
REFERENCE_CATALOG = I18N_DIR / "en.toml"


def load_catalog(path: Path) -> dict[str, str] | None:
    try:
        with path.open("rb") as file:
            catalog = tomllib.load(file)
    except tomllib.TOMLDecodeError as error:
        print(f"{path}: Invalid TOML: {error}")
        return None

    invalid = [key for key, value in catalog.items() if not isinstance(value, str) or not value]
    if invalid:
        print(f"{path}: Values must be non-empty strings: {', '.join(invalid)}")
        return None

    return catalog


def main() -> int:
    reference = load_catalog(REFERENCE_CATALOG)
    if reference is None:
        return 1

    failed = False
    reference_keys = tuple(reference)
    for path in sorted(I18N_DIR.glob("*.toml")):
        if path == REFERENCE_CATALOG:
            continue

        catalog = load_catalog(path)
        if catalog is None:
            failed = True
            continue

        catalog_keys = tuple(catalog)
        missing = [key for key in reference_keys if key not in catalog]
        extra = [key for key in catalog_keys if key not in reference]
        if missing:
            print(f"{path}: Missing keys: {', '.join(missing)}")
            failed = True
        if extra:
            print(f"{path}: Unknown keys: {', '.join(extra)}")
            failed = True
        if not missing and not extra and catalog_keys != reference_keys:
            print(f"{path}: Key order must match {REFERENCE_CATALOG}")
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
