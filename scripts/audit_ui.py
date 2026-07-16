#!/usr/bin/env python3
"""Heuristic static UI audit. It complements, not replaces, rendered testing."""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

EXTS = {
    ".html", ".htm", ".css", ".scss", ".sass", ".less",
    ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte",
}
SKIP_PARTS = {
    "node_modules", ".git", "dist", "build", ".next", ".nuxt",
    "coverage", "vendor", ".cache", "out",
}


@dataclass(frozen=True)
class Rule:
    severity: str
    category: str
    message: str
    pattern: re.Pattern[str]


RULES = [
    Rule("HIGH", "focus", "Removed focus outline", re.compile(r"outline\s*:\s*(?:none|0)\b", re.I)),
    Rule("HIGH", "semantics", "Clickable non-semantic element", re.compile(r"<(?:div|span)[^>]+onClick\s*=", re.I)),
    Rule("HIGH", "images", "Image may be missing alt", re.compile(r"<img(?![^>]*\balt\s*=)[^>]*>", re.I | re.S)),
    Rule("HIGH", "keyboard", "Positive tabindex", re.compile(r"tabindex\s*=\s*[\"']?[1-9]", re.I)),
    Rule("HIGH", "motion", "UI motion uses ease-in", re.compile(r"(?:transition|animation|easing)[^;\n]*(?<!-)\bease-in\b(?!-out)", re.I)),
    Rule("HIGH", "motion", "Entrance or state uses scale(0)", re.compile(r"scale(?:3d)?\s*\(\s*0(?:\s*[,\)])", re.I)),
    Rule("MEDIUM", "motion", "transition: all", re.compile(r"transition(?:-property)?\s*:\s*all\b", re.I)),
    Rule("MEDIUM", "motion", "Potentially slow UI duration over 300ms", re.compile(r"(?:transition|animation)[^;\n]*(?:3(?:0[1-9]|[1-9]\d)|[4-9]\d\d|\d{4,})ms\b", re.I)),
    Rule("MEDIUM", "motion", "Infinite animation requires review", re.compile(r"animation(?:-iteration-count)?[^;\n]*\binfinite\b", re.I)),
    Rule("MEDIUM", "motion", "Potential layout-property animation", re.compile(r"transition(?:-property)?\s*:[^;\n]*\b(?:width|height|margin|padding|top|left|right|bottom)\b", re.I)),
    Rule("MEDIUM", "layout", "Large fixed width", re.compile(r"width\s*:\s*(?:[5-9]\d\d|\d{4,})px", re.I)),
    Rule("MEDIUM", "type", "Tiny text", re.compile(r"font-size\s*:\s*(?:[0-9]|1[01])px", re.I)),
    Rule("LOW", "layers", "Very large z-index", re.compile(r"z-index\s*:\s*(?:[1-9]\d{3,})", re.I)),
    Rule("LOW", "tokens", "Raw hex color", re.compile(r"#[0-9a-fA-F]{3,8}\b")),
    Rule("LOW", "performance", "Permanent will-change requires review", re.compile(r"will-change\s*:\s*(?!auto|initial|inherit|unset)", re.I)),
]


@dataclass
class Finding:
    severity: str
    category: str
    message: str
    file: str
    line: int
    evidence: str


def iter_source_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTS:
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        yield path


def scan(root: Path, category: str | None = None) -> list[Finding]:
    findings: list[Finding] = []
    saw_motion = False
    saw_reduced_motion = False
    saw_hover_transform = False
    saw_hover_gate = False

    for path in iter_source_files(root):
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue

        relative = str(path.relative_to(root))
        saw_motion = saw_motion or bool(re.search(r"\b(?:transition|animation|@keyframes|animate\s*=|motion\.)", text, re.I))
        saw_reduced_motion = saw_reduced_motion or "prefers-reduced-motion" in text
        saw_hover_transform = saw_hover_transform or bool(re.search(r":hover[^{}]*\{[^{}]*(?:transform|animation|transition)", text, re.I | re.S))
        saw_hover_gate = saw_hover_gate or bool(re.search(r"@media[^{}]*(?:hover\s*:\s*hover|pointer\s*:\s*fine)", text, re.I))

        for number, line in enumerate(text.splitlines(), 1):
            for rule in RULES:
                if category and rule.category != category:
                    continue
                if rule.pattern.search(line):
                    findings.append(Finding(
                        rule.severity,
                        rule.category,
                        rule.message,
                        relative,
                        number,
                        line.strip()[:180],
                    ))

    if (not category or category == "motion") and saw_motion and not saw_reduced_motion:
        findings.append(Finding(
            "MEDIUM", "motion", "Project contains motion but no prefers-reduced-motion handling was found",
            "<project>", 0, "Add and verify a non-vestibular reduced-motion alternative",
        ))
    if (not category or category == "motion") and saw_hover_transform and not saw_hover_gate:
        findings.append(Finding(
            "MEDIUM", "motion", "Hover motion found without a hover/pointer capability gate",
            "<project>", 0, "Use @media (hover: hover) and (pointer: fine) where appropriate",
        ))

    rank = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    return sorted(findings, key=lambda item: (rank[item.severity], item.file, item.line, item.message))


def markdown(findings: list[Finding]) -> str:
    counts = Counter(f.severity for f in findings)
    lines = [
        "# Perfect UI Static Audit",
        "",
        f"Findings: **{len(findings)}** — HIGH {counts['HIGH']}, MEDIUM {counts['MEDIUM']}, LOW {counts['LOW']}",
        "",
        "> Heuristic output only. Verify every finding in the rendered UI and reject false positives or documented exceptions.",
        "",
        "| Severity | Category | Finding | File | Line | Evidence |",
        "|---|---|---|---|---:|---|",
    ]
    for finding in findings:
        evidence = finding.evidence.replace("|", "\\|").replace("`", "\\`")
        lines.append(
            f"| {finding.severity} | {finding.category} | {finding.message} | "
            f"`{finding.file}` | {finding.line or '—'} | `{evidence}` |"
        )
    return "\n".join(lines) + "\n"


def text(findings: list[Finding]) -> str:
    return "\n".join(
        f"{f.severity} {f.file}:{f.line or '-'} [{f.category}] {f.message} — {f.evidence}"
        for f in findings
    ) + ("\n" if findings else "")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--output")
    parser.add_argument("--format", choices=["markdown", "text"], default="markdown")
    parser.add_argument("--category", choices=sorted({rule.category for rule in RULES}))
    parser.add_argument("--fail-on", choices=["low", "medium", "high", "none"], default="none")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        parser.error(f"root is not a directory: {root}")

    findings = scan(root, args.category)
    output = markdown(findings) if args.format == "markdown" else text(findings)
    if args.output:
        Path(args.output).write_text(output)
    else:
        print(output, end="")

    rank = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}
    threshold = {"none": 99, "low": 1, "medium": 2, "high": 3}[args.fail_on]
    return 1 if any(rank[f.severity] >= threshold for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
