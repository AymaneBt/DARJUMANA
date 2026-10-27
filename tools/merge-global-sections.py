#!/usr/bin/env python3
"""Prepare an additive local settings fix from an exported installed configuration.
Does not contact YouCan or change an installed store; never replaces unrelated keys.
"""
from pathlib import Path
import json,argparse,copy
p=argparse.ArgumentParser(description=__doc__);p.add_argument('exported_settings',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
if a.exported_settings.resolve()==a.output.resolve():p.error('Use a separate output file; preserve the original export for rollback.')
if a.output.exists():p.error('Output exists; choose a new path rather than overwriting it.')
data=json.loads(a.exported_settings.read_text());patched=copy.deepcopy(data)
active=patched.get('current')
if isinstance(active,str):
 if active not in patched.get('presets',{}):p.error('Active named preset does not exist.')
 active=patched['presets'][active]
if not isinstance(active,dict):p.error('Invalid active settings object.')
sections=active.setdefault('sections',{})
if not isinstance(sections,dict):p.error('Invalid global sections registry.')
root=Path(__file__).resolve().parents[1]
fix=json.loads((root/'docs/global-sections-patch.json').read_text())['sections_to_merge']
for typename,default in fix.items():
 existing=[key for key,value in sections.items() if isinstance(value,dict)and value.get('type')==typename]
 if len(existing)>1:p.error('Duplicate global registration: '+typename+'; review before changing it.')
 if existing:
  # Preserve merchant edits and only supply keys absent from the existing section.
  section=sections[existing[0]]
  section.setdefault('settings',{})
  for key,value in default.get('settings',{}).items():section['settings'].setdefault(key,copy.deepcopy(value))
  if 'blocks' not in section:
   section['blocks']=copy.deepcopy(default.get('blocks',{}));section.setdefault('order',list(section['blocks']))
  elif 'order' not in section and 'block_order' not in section:section['order']=list(section['blocks'])
 else:sections[typename]=copy.deepcopy(default)
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(patched,ensure_ascii=False,indent=2)+'\n');a.output.chmod(0o600)
print('Prepared header/footer registration in separate output. Unrelated settings and app embeds preserved. No store changes made.')
