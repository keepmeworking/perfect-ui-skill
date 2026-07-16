#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parent.parent
REQUIRED=['README.md','SKILL.md','VERSION','agents/openai.yaml','references/01-operating-protocol.md','references/02-foundations.md','references/03-responsive-layout.md','references/04-components-and-states.md','references/05-accessibility.md','references/06-motion-feedback-performance.md','references/07-dashboard-data-ux.md','references/08-existing-project-migration.md','references/09-quality-gates.md','references/10-stack-adapters.md','references/11-anti-patterns.md','scripts/install_global.py','scripts/bootstrap_project.py','scripts/audit_ui.py']
missing=[x for x in REQUIRED if not (ROOT/x).exists()]
text=(ROOT/'SKILL.md').read_text()
errors=[]
if missing: errors.append('Missing: '+', '.join(missing))
if not text.startswith('---\n') or 'name: perfect-ui-skill' not in text: errors.append('Invalid SKILL.md frontmatter')
if errors:
 print('\n'.join(errors)); sys.exit(1)
print(f'Package OK: {len(REQUIRED)} required files present')
