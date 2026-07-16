#!/usr/bin/env python3
"""Heuristic static UI audit. It complements, not replaces, rendered testing."""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

EXTS={'.html','.htm','.css','.scss','.sass','.less','.js','.jsx','.ts','.tsx','.vue','.svelte'}
RULES=[
 ('HIGH','focus','Removed focus outline',re.compile(r'outline\s*:\s*(?:none|0)\b',re.I)),
 ('HIGH','semantics','Clickable non-semantic element',re.compile(r'<(?:div|span)[^>]+onClick\s*=',re.I)),
 ('HIGH','images','Image may be missing alt',re.compile(r'<img(?![^>]*\balt\s*=)[^>]*>',re.I|re.S)),
 ('HIGH','keyboard','Positive tabindex',re.compile(r'tabindex\s*=\s*["\']?[1-9]',re.I)),
 ('MEDIUM','motion','transition: all',re.compile(r'transition\s*:\s*all\b',re.I)),
 ('MEDIUM','layout','Large fixed width',re.compile(r'width\s*:\s*(?:[5-9]\d\d|\d{4,})px',re.I)),
 ('MEDIUM','type','Tiny text',re.compile(r'font-size\s*:\s*(?:[0-9]|1[01])px',re.I)),
 ('LOW','layers','Very large z-index',re.compile(r'z-index\s*:\s*(?:[1-9]\d{3,})',re.I)),
 ('LOW','tokens','Raw hex color',re.compile(r'#[0-9a-fA-F]{3,8}\b')),
]

def scan(root:Path):
 findings=[]
 for p in root.rglob('*'):
  if not p.is_file() or p.suffix.lower() not in EXTS or any(x in p.parts for x in ('node_modules','.git','dist','build','.next')): continue
  try: text=p.read_text(errors='ignore')
  except OSError: continue
  for n,line in enumerate(text.splitlines(),1):
   for sev,cat,msg,rx in RULES:
    if rx.search(line): findings.append((sev,cat,msg,str(p.relative_to(root)),n,line.strip()[:180]))
 return findings

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default='.'); ap.add_argument('--output'); ap.add_argument('--format',choices=['markdown','text'],default='markdown'); ap.add_argument('--fail-on',choices=['low','medium','high','none'],default='none'); a=ap.parse_args()
 root=Path(a.root).resolve(); f=scan(root)
 if a.format=='markdown':
  lines=['# Perfect UI Static Audit','',f'Findings: **{len(f)}**','', '| Severity | Category | Finding | File | Line | Evidence |','|---|---|---|---|---:|---|']+[f'| {x[0]} | {x[1]} | {x[2]} | `{x[3]}` | {x[4]} | `{x[5].replace("|","\\|")}` |' for x in f]
 else: lines=[f'{x[0]} {x[3]}:{x[4]} {x[2]} — {x[5]}' for x in f]
 out='\n'.join(lines)+'\n'; Path(a.output).write_text(out) if a.output else print(out,end='')
 rank={'LOW':1,'MEDIUM':2,'HIGH':3}; threshold={'none':99,'low':1,'medium':2,'high':3}[a.fail_on]
 return 1 if any(rank[x[0]]>=threshold for x in f) else 0
if __name__=='__main__': sys.exit(main())
