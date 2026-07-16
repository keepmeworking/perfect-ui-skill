#!/usr/bin/env python3
"""Validate the local perfect-ui-skill package structure and references."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REQUIRED = [
    SKILL,
    ROOT / "README.md",
    ROOT / "VERSION",
    ROOT / "LICENSE",
    ROOT / "THIRD_PARTY_NOTICES.md",
    ROOT / "references" / "01-operating-protocol.md",
    ROOT / "references" / "02-foundations.md",
    ROOT / "references" / "03-responsive-layout.md",
    ROOT / "references" / "04-components-and-states.md",
    ROOT / "references" / "05-accessibility.md",
    ROOT / "references" / "06-motion-feedback-performance.md",
    ROOT / "references" / "07-dashboard-data-ux.md",
    ROOT / "references" / "08-existing-project-migration.md",
    ROOT / "references" / "09-quality-gates.md",
    ROOT / "references" / "10-stack-adapters.md",
    ROOT / "references" / "11-anti-patterns.md",
    ROOT / "references" / "12-motion-craft.md",
    ROOT / "references" / "13-ui-review-and-planning.md",
    ROOT / "scripts" / "audit_ui.py",
    ROOT / "scripts" / "bootstrap_project.py",
    ROOT / "scripts" / "install_global.py",
    ROOT / "templates" / "motion.md",
    ROOT / "templates" / "ui-plans-readme.md",
    ROOT / "tests" / "test_audit_ui.py",
]


def main() -> int:
    errors: list[str] = []
    for path in REQUIRED:
        if not path.exists():
            errors.append(f"missing: {path.relative_to(ROOT)}")

    if SKILL.exists():
        text = SKILL.read_text(encoding="utf-8")
        if not re.match(r"^---\nname:\s*perfect-ui-skill\ndescription:\s*.+?\n---\n", text, re.S):
            errors.append("SKILL.md frontmatter must contain name and description")
        for reference in re.findall(r"`((?:references|templates|scripts)/[^`]+)`", text):
            relative = reference.split()[0]
            if not (ROOT / relative).exists():
                errors.append(f"broken SKILL.md reference: {relative}")

    version = (ROOT / "VERSION").read_text().strip() if (ROOT / "VERSION").exists() else ""
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION must use semantic versioning")

    if errors:
        print("Package verification failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"perfect-ui-skill {version} package verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
