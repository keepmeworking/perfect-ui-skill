#!/usr/bin/env python3
"""Install perfect-ui-skill globally or into a project for supported agents."""
from pathlib import Path
import argparse, os, shutil

GLOBAL={
 'codex':[Path.home()/'.agents/skills/perfect-ui-skill'],
 'claude':[Path.home()/'.claude/skills/perfect-ui-skill'],
 'cursor':[Path.home()/'.cursor/skills/perfect-ui-skill'],
 'antigravity':[Path.home()/'.gemini/config/skills/perfect-ui-skill',Path.home()/'.gemini/antigravity-cli/skills/perfect-ui-skill'],
}
PROJECT={'codex':['.agents/skills/perfect-ui-skill'],'claude':['.claude/skills/perfect-ui-skill'],'cursor':['.cursor/skills/perfect-ui-skill'],'antigravity':['.agents/skills/perfect-ui-skill']}
IGNORE=shutil.ignore_patterns('.git','__pycache__','*.pyc','perfect-ui-audit.md')
def install(src:Path,dst:Path,force:bool,mode:str):
 if dst.exists() or dst.is_symlink():
  if not force: print(f'SKIP exists: {dst}'); return
  if dst.is_dir() and not dst.is_symlink(): shutil.rmtree(dst)
  else: dst.unlink()
 dst.parent.mkdir(parents=True,exist_ok=True)
 if mode=='symlink': os.symlink(src,dst,target_is_directory=True)
 else: shutil.copytree(src,dst,ignore=IGNORE)
 print(f'INSTALLED: {dst}')
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--platform',choices=['all',*GLOBAL],default='all'); ap.add_argument('--scope',choices=['global','project'],default='global'); ap.add_argument('--project-root',default='.'); ap.add_argument('--force',action='store_true'); ap.add_argument('--mode',choices=['copy','symlink'],default='copy'); a=ap.parse_args()
 src=Path(__file__).resolve().parent.parent; platforms=list(GLOBAL) if a.platform=='all' else [a.platform]
 for platform in platforms:
  dests=GLOBAL[platform] if a.scope=='global' else [Path(a.project_root).resolve()/x for x in PROJECT[platform]]
  for dst in dests: install(src,dst,a.force,a.mode)
if __name__=='__main__': main()
