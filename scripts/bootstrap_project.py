#!/usr/bin/env python3
"""Create a non-destructive Perfect UI baseline in a project."""
from pathlib import Path
import argparse, shutil

MAP={
 'templates/perfect-ui.config.example.yaml':'perfect-ui.config.yaml',
 'templates/design-system-readme.md':'docs/design-system/README.md',
 'templates/component-state-matrix.md':'docs/design-system/component-state-matrix.md',
 'templates/ui-audit-report.md':'docs/design-system/ui-audit-report.md',
 'templates/tokens.css':'src/styles/perfect-ui.tokens.css',
 'templates/tokens.json':'docs/design-system/tokens.example.json',
}
def main():
 p=argparse.ArgumentParser(); p.add_argument('--root',default='.'); p.add_argument('--apply',action='store_true'); a=p.parse_args()
 here=Path(__file__).resolve().parent.parent; root=Path(a.root).resolve()
 for src,dst in MAP.items():
  target=root/dst
  status='SKIP exists' if target.exists() else ('CREATE' if a.apply else 'WOULD CREATE')
  print(f'{status}: {target}')
  if a.apply and not target.exists(): target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(here/src,target)
if __name__=='__main__': main()
