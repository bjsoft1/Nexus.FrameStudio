#!/usr/bin/env python3
"""Validate this planning package only. Does not build or test the native app."""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def main() -> int:
    checks = []
    def check(name: str, condition: bool, detail: str = '') -> None:
        checks.append({'check': name, 'result': 'PASS' if condition else 'FAIL', 'detail': detail})
    try:
        plan = json.loads((BASE / 'data/plan.json').read_text(encoding='utf-8'))
        approvals = json.loads((BASE / 'data/approval-state.json').read_text(encoding='utf-8'))
        check('Exactly five sequential phases', [p['number'] for p in plan['phases']] == list(range(1, 6)))
        check('Native implementation and tests are unrun', plan['implementationStatus'] == 'NOT_STARTED' and plan['nativeTestsStatus'] == 'NOT_RUN')
        task_ids, test_ids = [], []
        for p in plan['phases']:
            n=p['number']; pre=f'P{n}'
            check(f'{pre}: 20 task specifications', len(p['tasks'])==20)
            check(f'{pre}: 15 manual and 15 automated specifications', len(p['manualTests'])==len(p['automatedTests'])==15)
            check(f'{pre}: task done criteria and initial state', all(t.get('implementation') and t.get('doneWhen') and t.get('status')=='NOT_STARTED' for t in p['tasks']))
            check(f'{pre}: complete manual setup, steps, expectations and evidence paths', all(t.get('prerequisites') and len(t.get('steps',[]))>=2 and t.get('expected') and t.get('evidence') and t.get('status')=='NOT_RUN' for t in p['manualTests']))
            check(f'{pre}: complete automated scenarios, assertions and future commands', all(t.get('type') and t.get('scenario') and t.get('assertions') and t['id'].replace('-','_') in t.get('futureCommand','') and t.get('status')=='NOT_RUN' for t in p['automatedTests']))
            check(f'{pre}: scope, exclusions and approval gate', all(p.get(k) for k in ('scope','excluded','gate','outcome')))
            folder=BASE/'phases'/p['slug']
            expected=['01_IMPLEMENTATION.md','02_MANUAL_TESTS.md','03_AUTOMATED_TESTS.md','04_HANDOFF_AND_REMAINING.md','AGENT_PROMPT.md']
            check(f'{pre}: all five phase handoff files exist', all((folder/f).is_file() and (folder/f).stat().st_size>500 for f in expected))
            check(f'{pre}: test IDs are present in the corresponding documents', all(t['id'] in (folder/f).read_text(encoding='utf-8') for f,key in [('02_MANUAL_TESTS.md','manualTests'),('03_AUTOMATED_TESTS.md','automatedTests')] for t in p[key]))
            task_ids += [t['id'] for t in p['tasks']]
            test_ids += [t['id'] for key in ('manualTests','automatedTests') for t in p[key]]
        check('100 unique task IDs and 150 unique test IDs',len(task_ids)==len(set(task_ids))==100 and len(test_ids)==len(set(test_ids))==150)
        expected_features={f'{c}{i:02}' for c in 'ER' for i in range(1,21)}
        check('All 20 editor and 20 recorder requirements retained',expected_features=={r['id'] for r in plan['requirements'] if r['id'][0] in 'ER'})
        check('Seven additional approved-screen capabilities retained',{r['id'] for r in plan['requirements'] if r['id'].startswith('X')}=={f'X{i:02}' for i in range(1,8)})
        check('Every requirement maps to real acceptance IDs',all(r['manualCase'] in test_ids and r['automatedCase'] in test_ids and r['primaryPhase'] in range(1,6) for r in plan['requirements']))
        check('All 54 unique approved screens retained',len(plan['screens'])==54 and {p['number'] for p in plan['screens']}==set(range(1,55)))
        check('Every screen has visual and functional ownership',all(p['visualPhase']==1 and p['functionalPhase'] in range(1,6) for p in plan['screens']))
        check('All approved screen links resolve',all((BASE/p['path']).is_file() for p in plan['screens']))
        check('No phase or release self-approval',all(p['status']=='NOT_STARTED' and p['decision']=='PENDING' and p['approvedAt'] is None for p in approvals['phases']))
        required=['index.html','assets/review.css','assets/review.js','data/plan.js','00_START_HERE.md','01_MASTER_AGENT_PROMPT.md','docs/ARCHITECTURE.md','docs/CAPTURE_DATA_CONTRACT.md','docs/TESTING_GUIDE.md','docs/FEATURES_20_PLUS_20.md','docs/SCREEN_PHASE_MAP.md','docs/SCOPE_RISKS_AND_REMAINING.md','docs/SOURCE_REUSE_REVIEW.md','docs/SOURCES.md','templates/PHASE_RESULT.json']
        check('Core reviewer and engineering files exist',all((BASE/f).is_file() for f in required))
        broken=[]
        for f in BASE.rglob('*.md'):
            if 'reference' in f.relative_to(BASE).parts: continue
            for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
                if '://' in link or link.startswith(('#','mailto:')):continue
                target=(f.parent/link.split('#')[0]).resolve()
                if not target.is_relative_to(BASE.resolve()) or not target.exists():broken.append(f'{f.relative_to(BASE)} -> {link}')
        check('Planning Markdown local links resolve safely',not broken,'; '.join(broken))
        manifest_path=BASE/'FILE_MANIFEST.json'
        if manifest_path.exists():
            manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
            errors=[]
            for row in manifest['files']:
                path=(BASE/row['path']).resolve()
                if not path.is_relative_to(BASE.resolve()) or not path.is_file():errors.append(row['path']);continue
                if path.stat().st_size!=row['sizeBytes'] or hashlib.sha256(path.read_bytes()).hexdigest()!=row['sha256']:errors.append(row['path'])
            check('Package manifest file sizes and SHA-256 hashes match',not errors,', '.join(errors))
            listed={f['path'] for f in manifest['files']}
            actual={str(p.relative_to(BASE)).replace('\\','/') for p in BASE.rglob('*') if p.is_file() and p != BASE/'FILE_MANIFEST.json'}
            check('Package manifest covers all delivery files', listed==actual)
        else:
            check('Package manifest is present', False, 'Create FILE_MANIFEST.json before distributing the package.')
        reference_manifest=BASE/'data/reference-hashes.json'
        if reference_manifest.exists():
            reference=json.loads(reference_manifest.read_text(encoding='utf-8'))
            check('Approved prototype reference is unchanged',all((BASE/'reference/approved-prototype'/x['path']).is_file() and hashlib.sha256((BASE/'reference/approved-prototype'/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in reference['files']))
        else:check('Approved reference hash list exists',False)
        js=(BASE/'assets/review.js').read_text(encoding='utf-8')
        check('Review export does not grant native completion or approval',all(s in js for s in ["nativeImplementationStatus:'NOT_STARTED'","nativeTestsStatus:'NOT_RUN'","NOT_GRANTED_BY_THIS_REVIEW_PAGE"]))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        check('Validator completed without invalid/missing input',False,str(exc))
    result={'kind':'planning-package-validation','nativeApplicationBuilt':False,'nativeTestsRun':False,'passed':sum(x['result']=='PASS' for x in checks),'failed':sum(x['result']=='FAIL' for x in checks),'checks':checks}
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 1 if result['failed'] else 0

if __name__ == '__main__':
    sys.exit(main())
