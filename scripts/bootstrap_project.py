#!/usr/bin/env python3
"""Scaffold a non-destructive project-level Perfect UI design-system baseline.

The default is a dry run. Pass --apply to write files. Existing files are never
replaced unless --force is also supplied.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = PACKAGE_ROOT / "templates"


def choose_style_dir(root: Path) -> Path:
    candidates = [
        root / "src" / "styles",
        root / "app" / "styles",
        root / "styles",
        root / "src" / "theme",
        root / "theme",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    if (root / "src").exists():
        return root / "src" / "styles"
    return root / "styles"


def plan(root: Path) -> list[tuple[Path, Path]]:
    docs = root / "docs" / "design-system"
    style_dir = choose_style_dir(root)
    return [
        (TEMPLATES / "perfect-ui.config.example.yaml", root / "perfect-ui.config.yaml"),
        (TEMPLATES / "design-system-readme.md", docs / "README.md"),
        (TEMPLATES / "component-state-matrix.md", docs / "component-state-matrix.md"),
        (TEMPLATES / "motion.md", docs / "motion.md"),
        (TEMPLATES / "ui-audit-report.md", docs / "ui-audit-report.md"),
        (TEMPLATES / "ui-plans-readme.md", root / "plans" / "ui" / "README.md"),
        (TEMPLATES / "tokens.css", style_dir / "perfect-ui.tokens.css"),
        (TEMPLATES / "tokens.json", docs / "tokens.example.json"),
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root.")
    parser.add_argument("--apply", action="store_true", help="Write the planned files.")
    parser.add_argument("--force", action="store_true", help="Replace existing target files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    print(f"Project root: {root}")
    print("Mode:", "APPLY" if args.apply else "DRY RUN")

    for source, target in plan(root):
        if target.exists() and not args.force:
            print(f"skip existing: {target}")
            continue
        print(f"{'write' if args.apply else 'would write'}: {target}")
        if args.apply:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    if not args.apply:
        print("\nNo files changed. Re-run with --apply after reviewing the plan.")
    else:
        print("\nScaffold created. Adapt tokens and documentation to the actual product; do not treat neutral defaults as approved branding.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
