from pathlib import Path
import json, base64, tempfile, shutil
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1];OUT=Path(tempfile.mkdtemp(prefix='nexus-framestudio-plan-qa-'));checks=[]
def add(name,ok,detail=''): checks.append({'check':name,'result':'PASS' if ok else 'FAIL','detail':detail})
with sync_playwright() as p:
 browser_path=shutil.which('chromium') or shutil.which('google-chrome')
 launch_args={'headless':True}
 if browser_path: launch_args['executable_path']=browser_path
 browser=p.chromium.launch(**launch_args)
 context=browser.new_context(viewport={'width':1920,'height':1080},accept_downloads=True)
 page=context.new_page();page.set_default_timeout(8000);errors=[];network=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.on('request',lambda r:network.append(r.url) if r.url.startswith(('http:','https:')) else None)
 def load_memory(store=None):
  page.goto('about:blank')
  content=(root/'index.html').read_text()
  content=content.replace('<link rel="stylesheet" href="assets/review.css">','<style>'+(root/'assets/review.css').read_text()+'</style>')
  storage_code='window.__testStore='+json.dumps(store or {}).replace('<', '\\u003c')+';Object.defineProperty(window,"localStorage",{configurable:true,value:{getItem:k=>window.__testStore[k]??null,setItem:(k,v)=>{window.__testStore[k]=String(v)}}});'
  content=content.replace('<script src="data/plan.js"></script>','<script>'+storage_code+(root/'data/plan.js').read_text()+'</script>')
  js=(root/'assets/review.js').read_text()
  img='data:image/png;base64,'+base64.b64encode((root/'reference/approved-prototype/screenshots/editor-1920x1080.png').read_bytes()).decode()
  js=js.replace('reference/approved-prototype/screenshots/editor-1920x1080.png',img)
  content=content.replace('<script src="assets/review.js"></script>','<script>'+js+'</script>')
  page.set_content(content,wait_until='load')
 load_memory()
 add('Reviewer opens in browser-memory mode',page.locator('h1').inner_text().startswith('Build your studio.'))
 add('Overview has five phase cards',page.locator('.phase-card').count()==5)
 add('Overview reports 100 tasks and 150 specifications',page.locator('.stats').inner_text().find('100')>=0 and page.locator('.stats').inner_text().find('150')>=0)
 page.screenshot(path=str(OUT/'plan-overview-1920x1080.png'))
 for width,height in [(1920,1080),(1366,768)]:
  page.set_viewport_size({'width':width,'height':height})
  for n in range(1,6):
   page.locator(f'#phase-nav [data-view="{n}"]').click()
   add(f'P{n} task checklist at {width}×{height}',page.locator('.task').count()==20)
   for tab,num in [('manual',15),('auto',15)]:
    page.locator(f'[data-tab="{tab}"]').click()
    add(f'P{n} {tab} cases at {width}×{height}',page.locator('details').count()==num)
    page.locator('summary').first.click()
    add(f'P{n} {tab} case expands at {width}×{height}',page.locator('details[open] .case-content').count()==1)
   page.locator('[data-tab="handoff"]').click()
   add(f'P{n} handoff notes available at {width}×{height}',page.locator('#phase-notes').count()==1)
   add(f'P{n} no horizontal overflow at {width}×{height}',page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'))
 page.set_viewport_size({'width':1920,'height':1080})
 page.locator('#phase-nav [data-view="1"]').click()
 page.locator('[data-task="P1-T01"]').check()
 page.locator('#search').fill('P1-T12')
 add('Task search returns exact matching task',page.locator('.task').count()==1 and 'P1-T12' in page.locator('.task').inner_text())
 page.locator('#search').fill('')
 page.locator('[data-tab="manual"]').click();page.locator('summary').first.click()
 page.screenshot(path=str(OUT/'plan-phase-1-tests-1920x1080.png'))
 page.locator('[data-tab="handoff"]').click()
 note='P1 review: keep approved UI. <script>window.UNSAFE_REVIEW=true</script>'
 page.locator('#phase-notes').fill(note)
 load_memory(page.evaluate('window.__testStore'));page.locator('#phase-nav [data-view="1"]').click();page.locator('[data-tab="handoff"]').click()
 add('Draft notes restore through controlled storage and remain escaped',page.locator('#phase-notes').input_value()==note and page.evaluate('window.UNSAFE_REVIEW === undefined'))
 page.locator('#theme').click();add('Light theme switches',page.locator('body').get_attribute('class')=='light')
 load_memory(page.evaluate('window.__testStore'));add('Theme preference restores through controlled storage',page.locator('body').get_attribute('class')=='light')
 page.locator('#theme').click()
 with page.expect_download() as dl:page.locator('#export').click()
 path=OUT/'reviewer-export.json';dl.value.save_as(path)
 e=json.loads(path.read_text())
 add('Review notes export as real JSON',e['kind']=='nexus.framestudio.plan-review' and e['phaseNotes']['1']==note and 'P1-T01' in e['scopeReviewedTaskIds'])
 add('Review export never grants completion or approval',e['nativeImplementationStatus']=='NOT_STARTED' and e['nativeTestsStatus']=='NOT_RUN' and e['approval']=='NOT_GRANTED_BY_THIS_REVIEW_PAGE')
 page.locator('aside [data-view="features"]').click()
 add('All feature traceability rows displayed',page.locator('.coverage tbody tr').count()==47)
 page.locator('#search').fill('E10');add('Feature search filters correctly',page.locator('.coverage tbody tr').count()==1)
 page.locator('aside [data-view="screens"]').click()
 add('All 54 approved screen links displayed',page.locator('.screen-item').count()==54)
 add('Editor reference link targets the approved file',page.locator('.screen-item[href*="27-editor.html"]').get_attribute('href')=='reference/approved-prototype/pages/27-editor.html')
 page.locator('aside [data-view="overview"]').click();page.locator('#theme').click()
 page.screenshot(path=str(OUT/'plan-overview-light-1920x1080.png'))
 add('No unhandled reviewer JavaScript exceptions',not errors,'; '.join(errors))
 add('In-memory reviewer makes no external web requests',not network,'; '.join(network))
 browser.close()
report={'kind':'planning-reviewer-browser-checks','mode':'browser-memory with inlined resources and controlled storage adapter','limitations':['file:// and localhost navigation were blocked by this environment browser policy; real file/HTTP navigation, browser storage persistence and Windows launch remain unverified','Reference links were checked structurally, not followed in the restricted browser'],'nativeTestsRun':False,'passed':sum(x['result']=='PASS' for x in checks),'failed':sum(x['result']=='FAIL' for x in checks),'checks':checks}
(OUT/'reviewer-checks.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:report[k] for k in ['kind','passed','failed','nativeTestsRun']}))
for x in checks:
 if x['result']=='FAIL':print(x)

print('Evidence directory:', OUT)
