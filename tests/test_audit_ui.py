from __future__ import annotations

import importlib.util
import tempfile
import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("audit_ui", ROOT / "scripts" / "audit_ui.py")
audit_ui = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit_ui
assert SPEC.loader is not None
SPEC.loader.exec_module(audit_ui)


class AuditUiTests(unittest.TestCase):
    def scan(self, content: str):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "sample.css").write_text(content)
            return audit_ui.scan(root)

    def test_flags_motion_antipatterns(self):
        findings = self.scan(
            ".x { transition: all 500ms ease-in; transform: scale(0); }"
        )
        messages = {finding.message for finding in findings}
        self.assertIn("transition: all", messages)
        self.assertIn("UI motion uses ease-in", messages)
        self.assertIn("Entrance or state uses scale(0)", messages)
        self.assertIn("Potentially slow UI duration over 300ms", messages)
        self.assertIn(
            "Project contains motion but no prefers-reduced-motion handling was found",
            messages,
        )

    def test_reduced_motion_avoids_project_warning(self):
        findings = self.scan(
            """
            .x { transition: transform 160ms ease-out; }
            @media (prefers-reduced-motion: reduce) { .x { transition: none; } }
            """
        )
        messages = {finding.message for finding in findings}
        self.assertNotIn(
            "Project contains motion but no prefers-reduced-motion handling was found",
            messages,
        )

    def test_category_filter(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "sample.css").write_text(
                ".x { color: #fff; transition: all 500ms ease-in; }"
            )
            findings = audit_ui.scan(root, "tokens")
            self.assertTrue(findings)
            self.assertTrue(all(finding.category == "tokens" for finding in findings))


if __name__ == "__main__":
    unittest.main()
