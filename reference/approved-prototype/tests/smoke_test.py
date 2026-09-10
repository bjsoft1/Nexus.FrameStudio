"""Offline UI smoke tests. Requires Python 3.10+ and Playwright.

Default: render an in-memory standalone document; never requests devices/network.
Optional --url URL: test an already served prototype, including actual navigation.
Optional --browser PATH: use a particular Chromium executable.
"""
from __future__ import annotations
import argparse, base64, json, os, re, sys, time
from pathlib import Path
from datetime import datetime, timezone
from importlib.metadata import version
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--browser', default=None)
parser.add_argument('--url', default=None)
parser.add_argument('--screenshots', action='store_true')
args = parser.parse_args()
OUT = ROOT / 'tests' / 'results'; OUT.mkdir(exist_ok=True)
PAGES = json.loads((ROOT / 'examples/pages.json').read_text(encoding='utf-8'))

def standalone():
    html = (ROOT/'index.html').read_text(encoding='utf-8')
    html = re.sub(r'<link rel="stylesheet" href="assets/styles.css">', lambda _: '<style>'+(ROOT/'assets/styles.css').read_text(encoding='utf-8')+'</style>', html)
    for name in ['pages', 'app']:
        html = html.replace(f'<script src="assets/{name}.js"></script>', '<script>'+(ROOT/f'assets/{name}.js').read_text(encoding='utf-8')+'</script>')
    return html

results, errors, network = [], [], []

def record(name, fn):
    print('RUN',name,flush=True)
    started = time.perf_counter()
    try:
        fn()
        results.append({'test':name,'status':'PASS','seconds':round(time.perf_counter()-started,3)})
    except Exception as exc:
        results.append({'test':name,'status':'FAIL','seconds':round(time.perf_counter()-started,3),'detail':str(exc)[:2000]})
        print('FAIL',name,str(exc)[:280], flush=True)

def require(value, msg='Assertion failed'):
    if not value: raise AssertionError(msg)

with sync_playwright() as p:
    kwargs = {'headless':True}
    if args.browser: kwargs['executable_path'] = args.browser
    browser = p.chromium.launch(**kwargs)
    ctx = browser.new_context(viewport={'width':1920,'height':1080}, accept_downloads=True)
    page = None
    def fresh():
        global page
        if page: page.close()
        page = ctx.new_page()
        page.set_default_timeout(3500)
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.on('request', lambda r: network.append(r.url))
        if args.url:
            page.add_init_script("try { localStorage.removeItem('nexus.framestudio.prototype.v1'); } catch (e) {}")
            page.goto(args.url, wait_until='load')
        else: page.set_content(standalone(), wait_until='load')
        page.wait_for_function('window.NFS !== undefined')
    def nav(pid):
        page.evaluate('(id)=>NFS.navigate(id)',pid)
        page.wait_for_function('(id)=>location.hash==="#"+id', arg=pid)
        page.wait_for_timeout(35)
    def state(): return page.evaluate('NFS.getState()')
    def action(name): page.locator(f'[data-action="{name}"]').first.click()
    def bind(path, value):
        node = page.locator(f'[data-bind="{path}"]').first
        if node.evaluate('(e)=>e.tagName')=='SELECT': node.select_option(str(value))
        elif node.get_attribute('type') in ['range','color']:
            node.evaluate('(e,v)=>{e.value=v;e.dispatchEvent(new Event("input",{bubbles:true}));e.dispatchEvent(new Event("change",{bubbles:true}));}',str(value))
        else: node.fill(str(value)); node.dispatch_event('change')
    def toggle(path): page.locator(f'[data-toggle="{path}"]').first.click()
    def download(name):
        with page.expect_download() as got: action(name)
        d=got.value
        require(d.failure() is None, 'Download failed')
        dest=OUT/d.suggested_filename;d.save_as(str(dest))
        return dest
    def upload_project(data):
        nav('import'); action('import-project')
        page.locator('#filePicker').set_input_files({'name':'test.nfsproject','mimeType':'application/json','buffer':json.dumps(data).encode()})
        page.wait_for_timeout(80)
    def check_route(desc,w,h):
        nav(desc['id'])
        require(page.locator('h1').count()==1, 'Missing/duplicate main heading')
        require(page.locator('h1').inner_text() in [desc['headline'],desc['title']], 'Wrong content')
        dims=page.evaluate('({w:innerWidth,h:innerHeight,sw:document.documentElement.scrollWidth,sh:document.documentElement.scrollHeight})')
        require(dims['sw']<=w+1 and dims['sh']<=h+1, f'Document overflow: {dims}')
        require(page.locator('[data-action="next"]').count()==1, 'Missing step navigation')

    fresh()
    baseline=state()
    (ROOT/'examples/Demo-Walkthrough.nfsproject').write_text(json.dumps(baseline,indent=2),encoding='utf-8')
    record('Catalog: exactly 54 unique screens',lambda: require(len(PAGES)==54 and len({x['id'] for x in PAGES})==54))
    def entries():
        for d in PAGES:
            f=ROOT/'pages'/f"{d['number']:02d}-{d['id']}.html"
            require(f.exists(),str(f))
            t=f.read_text(encoding='utf-8')
            require(f'data-start="{d["id"]}"' in t, 'Wrong start screen')
            for path in re.findall(r'(?:src|href)="(\.\./assets/[^"#]+)"',t):
                require((f.parent/path).resolve().exists(), path)
    record('54 physical HTML entries and relative assets',entries)
    for w,h in [(1920,1080),(1366,768)]:
        page.set_viewport_size({'width':w,'height':h})
        for d in PAGES: record(f"Route {d['number']:02d} {d['id']} at {w}x{h}",lambda d=d,w=w,h=h: check_route(d,w,h))
    page.set_viewport_size({'width':1920,'height':1080})
    def aspect():
        nav('editor')
        box=page.locator('#mainScene').bounding_box()
        require(abs(box['width']/box['height']-16/9)<0.02,str(box))
        require(page.locator('.track-row').count()>=6,'Track rows missing')
    record('Editor preview preserves 16:9 geometry',aspect)
    def prev_next():
        nav('home');action('next');page.wait_for_timeout(50)
        require(page.url.endswith('#projects'))
        action('prev');page.wait_for_timeout(50);require(page.url.endswith('#home'))
    record('Previous / next navigation',prev_next)
    def search():
        page.keyboard.press('Control+k');page.locator('#screenSearch').fill('audio')
        require(page.locator('#screenSearchResults a').count()>=2)
        page.locator('#screenSearchResults a[href="#audio"]').click()
        page.wait_for_timeout(50);require(page.url.endswith('#audio'));require(page.locator('.modal').count()==0)
    record('Search all screens with Ctrl+K',search)
    def split():
        nav('trim-split');action('split');require(len(state()['clips'])==4)
        require(abs(sum(c['duration'] for c in state()['clips'])-42)<0.01)
        action('undo');require(len(state()['clips'])==3)
        action('redo');require(len(state()['clips'])==4)
    record('Split keeps source duration; undo and redo',split)
    def reorder():
        nav('join');action('append-demo');ss=state();last=ss['clips'][-1]['id']
        action('clip-left');require(state()['clips'][-2]['id']==last)
        action('delete-clip');require(len(state()['clips'])==4)
    record('Append, reorder and delete clips non-destructively',reorder)
    def select_clip():
        nav('editor');page.locator('[data-clip-id="c1"]').first.click();require(state()['edit']['selectedClip']=='c1')
    record('Timeline clip selection',select_clip)
    def text():
        nav('text');page.locator('[data-ov="text"]').first.fill('Hello FrameStudio')
        require('Hello FrameStudio' in page.locator('#mainScene').inner_text())
        before=state()['overlays'][0]['bold'];action('format-bold');require(state()['overlays'][0]['bold']!=before)
        nav('formatted-text');action('format-span');require(state()['overlays'][0]['richFinalWord'])
    record('Edit text, bold and mixed-span emphasis',text)
    def shape():
        nav('shapes');page.locator('[data-add-shape="circle"]').first.click()
        require(state()['overlays'][-1]['type']=='circle')
        action('duplicate-overlay');require(len(state()['overlays'])==3)
        action('layer-back');require(state()['overlays'][0]['type']=='circle')
        action('delete-overlay');require(len(state()['overlays'])==2)
    record('Shape creation, duplication, stacking and deletion',shape)
    def overlay_drag():
        nav('editor');oid=state()['edit']['selectedOverlay'];before=next(o for o in state()['overlays'] if o['id']==oid)
        loc=page.locator(f'[data-overlay-id="{oid}"]');b=loc.bounding_box()
        require(b is not None)
        page.mouse.move(b['x']+b['width']/2,b['y']+b['height']/2);page.mouse.down();page.mouse.move(b['x']+b['width']/2+30,b['y']+b['height']/2-20,steps=4);page.mouse.up()
        after=next(o for o in state()['overlays'] if o['id']==oid)
        require(after['x']!=before['x'] or after['y']!=before['y'])
    record('Overlay move gizmo updates position',overlay_drag)
    def keyframe():
        nav('animation');action('add-keyframe')
        ss=state();o=next(o for o in ss['overlays'] if o['id']==ss['edit']['selectedOverlay']);require(len(o['keyframes'])==1)
    record('Full-pose animation keyframe saved',keyframe)
    def playback():
        nav('editor');old=state()['edit']['playhead'];action('play');page.wait_for_timeout(180);action('play')
        require(state()['edit']['playhead']>old)
    record('Timeline playback and pause simulation',playback)
    def mute():
        nav('audio-mixer');before=state()['session']['captured'].copy();toggle('edit.systemMute')
        ss=state();require(ss['edit']['systemMute']);require(ss['session']['captured']==before)
        plan=page.evaluate('NFS.renderPlan()');require(plan['effectiveSources']['system'] is False,str(plan))
        require(plan['effectiveSources']['microphone'] is True)
        toggle('edit.systemMute')
    record('Muting system audio leaves microphone and capture untouched',mute)
    def effects():
        nav('editor-mouse');toggle('edit.mouse');require(state()['edit']['mouse'] is False)
        require(state()['session']['captured']['mouse'] is True)
        toggle('edit.mouse');nav('editor-keys');toggle('edit.keys');require(state()['edit']['keys'] is False)
        toggle('edit.keys')
    record('Hide and restore cursor / keyboard without erasing capture',effects)
    def theme():
        before=state()['theme'];action('theme');require(state()['theme']!=before)
        require(page.locator('html').get_attribute('data-theme')=='light')
        if args.screenshots:
            nav('editor');page.screenshot(path=str(ROOT/'screenshots/editor-light-1920x1080.png'))
        action('theme')
    record('Light / dark theme switch',theme)
    def crop():
        nav('crop');page.locator('[data-set="edit.cropRatio"][data-value="1:1"]').click()
        require(state()['edit']['cropW']==state()['edit']['cropH'])
        action('reset-crop');require(state()['edit']['cropW']==1920)
    record('Crop ratio and reset controls',crop)
    def quality():
        nav('resize-quality');bind('edit.bitrate',4);action('apply-quality');page.wait_for_timeout(70)
        require(state()['export']['bitrate']==4);require(page.url.endswith('#export'))
    record('Compression settings transfer to export',quality)
    def save_reopen():
        path=download('save');data=json.loads(path.read_text())
        require(data['kind']=='nexus.framestudio.prototype')
        data['projectName']='Roundtrip acceptance test';upload_project(data)
        require(state()['projectName']=='Roundtrip acceptance test')
        require(len(state()['clips'])==len(data['clips']))
    record('Download editable JSON and reopen through file picker',save_reopen)
    def validation():
        require(page.evaluate('(s)=>NFS.validateProject(s).schemaVersion',baseline)==1)
        bad=[dict(baseline,schemaVersion=999),dict(baseline,kind='not-a-project'),dict(baseline,clips=[baseline['clips'][0]]*2)]
        bad_time=json.loads(json.dumps(baseline));bad_time['overlays'][0]['end']=-1;bad.append(bad_time)
        for d in bad:
            require(page.evaluate('(s)=>{try{NFS.validateProject(s);return false;}catch(e){return true;}}',d),'Invalid project accepted')
    record('Reject unknown schema, wrong kind, duplicate IDs, invalid ranges',validation)
    def invalid_file():
        old=state()['projectName'];nav('import');action('import-project')
        page.locator('#filePicker').set_input_files({'name':'broken.nfsproject','mimeType':'application/json','buffer':b'{broken'})
        page.wait_for_timeout(80);require(state()['projectName']==old)
        require('File not opened' in page.locator('#toastArea').inner_text())
    record('Malformed JSON does not replace the current project',invalid_file)
    def media():
        nav('import');action('import-media')
        tiny=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Zl1sAAAAASUVORK5CYII=')
        page.locator('#filePicker').set_input_files({'name':'test-overlay.png','mimeType':'image/png','buffer':tiny})
        page.wait_for_timeout(100);require(any(a['name']=='test-overlay.png' for a in state()['assets']))
    record('Import local image into media bin',media)
    def srt():
        nav('captions');f=download('export-srt');text=f.read_text();require(' --> ' in text and 'Welcome' in text)
    record('Download real SRT caption sidecar',srt)
    def json_output():
        nav('export');f=download('save-render-plan');require(json.loads(f.read_text())['prototypeOnly'] is True)
        nav('track-inspector');f=download('download-metadata');require(isinstance(json.loads(f.read_text()),dict))
    record('Download render plan and metadata JSON',json_output)
    def feedback():
        nav('editor');action('feedback');page.locator('[data-feedback="Needs changes"]').click()
        page.locator('#pageFeedback').fill('Make the playhead easier to grab.');action('save-feedback')
        require(state()['review']['decisions']['editor']=='Needs changes')
        nav('review-checklist');f=download('export-review');require('Make the playhead easier' in f.read_text())
    record('Per-screen feedback and Markdown review download',feedback)
    def preset():
        nav('record');bind('capture.preset','Small file');require(state()['capture']['bitrate']==3)
        require(state()['capture']['resolution']=='1280 × 720')
    record('Quick preset selector applies capture values',preset)

    # A fresh draft prevents recording fixtures from changing previous test expectations.
    fresh()
    def disabled_capture():
        nav('countdown');bind('capture.delay',0);nav('audio');toggle('capture.mic')
        nav('readiness');action('start-recording');page.wait_for_timeout(1150);action('stop-recording');page.wait_for_timeout(70)
        require(state()['session']['captured']['mic'] is False)
        require(state()['session']['captured']['system'] is True)
        require(any(g['source']=='mic' for g in state()['session']['gaps']))
        nav('audio-mixer');require(page.locator('[data-toggle="edit.micMute"]').first.is_disabled())
        require(page.evaluate('NFS.renderPlan().effectiveSources.microphone') is False)
    record('Capture-off microphone is unavailable, not recoverable',disabled_capture)
    def pause_gap():
        nav('audio');toggle('capture.mic');nav('readiness');action('start-recording');page.wait_for_timeout(1100)
        action('pause-recording');before=page.evaluate('NFS.getRuntime().elapsed');page.wait_for_timeout(1100)
        require(page.evaluate('NFS.getRuntime().elapsed')==before)
        toggle('capture.mic');action('pause-recording');page.wait_for_timeout(1100);action('add-marker');action('stop-recording');page.wait_for_timeout(70)
        ss=state();require(ss['session']['captured']['mic'] is True)
        require(any(g['source']=='mic' and g['endUs']>g['startUs'] for g in ss['session']['gaps']))
        require(len(ss['session']['markers'])==1)
    record('Pause freezes time; later capture-off preserves a real gap',pause_gap)
    def countdown_cancel():
        before=state()['session'];nav('countdown');bind('capture.delay',3);nav('readiness');action('start-recording')
        require(page.evaluate('NFS.getRuntime().recordPhase')=='countdown')
        action('stop-recording');page.wait_for_timeout(70)
        require(page.evaluate('NFS.getRuntime().recordPhase')=='idle');require(state()['session']==before,'Cancellation changed prior session')
    record('Countdown cancellation produces no take',countdown_cancel)
    def export_cancel():
        nav('export');before=state()['session'];action('start-export');page.wait_for_timeout(300);action('cancel-export')
        require(page.evaluate('NFS.getRuntime().exportState')=='cancelled');require(state()['session']==before)
    record('Cancel export simulation without changing source session',export_cancel)
    def export_complete():
        nav('export');action('start-export');page.wait_for_function('NFS.getRuntime().exportState==="completed"', timeout=6000)
        require('no actual MP4 generated' in page.locator('#exportStage').inner_text())
    record('Export simulation completes and explicitly reports no MP4',export_complete)
    def export_fail():
        nav('export-progress');action('export-disk-error');require(page.evaluate('NFS.getRuntime().exportState')=='failed')
    record('Disk-full export failure fixture',export_fail)

    fresh()
    if args.screenshots:
        (ROOT/'screenshots').mkdir(exist_ok=True)
        for pid in ['home','record','monitors','keyboard','editor','formatted-text','audio-mixer','track-inspector','page-map']:
            nav(pid);page.screenshot(path=str(ROOT/'screenshots'/f'{pid}-1920x1080.png'))
        page.set_viewport_size({'width':1366,'height':768});nav('editor')
        page.screenshot(path=str(ROOT/'screenshots/editor-1366x768.png'))
    for kind in ['session','frame','pointer','keyboard']:
        data=page.evaluate('(k)=>NFS.metadata(k)',kind)
        (ROOT/f'examples/{kind}.example.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    record('No unhandled JavaScript exceptions',lambda:require(not errors,'\n'.join(errors)))
    if not args.url:
        record('Offline render makes no HTTP requests',lambda:require(not any(u.startswith(('http:','https:')) for u in network),str(network)))
    report={'generatedAt':datetime.now(timezone.utc).isoformat(),'browser':browser.version,'playwright':version('playwright'),'mode':'served-url' if args.url else 'in-memory standalone document (page.set_content)', 'viewports':['1920x1080','1366x768'],'passed':sum(r['status']=='PASS' for r in results),'failed':sum(r['status']=='FAIL' for r in results),'tests':results,'javascriptErrors':errors,'networkRequests':network,'scopeNote':'Prototype UI only. No native capture, real encoding, Windows device testing, production media fidelity, or recovery testing. File/HTTP navigation is not tested in in-memory mode.'}
    (OUT/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    md=f"# Automated prototype test report\n\nRun: {report['generatedAt']}\n\n**{report['passed']} passed; {report['failed']} failed.**\n\nChromium {report['browser']}; Playwright {report['playwright']}.\n\nMode: {report['mode']}.\n\n{report['scopeNote']}\n\n| Check | Result |\n|---|---|\n"+'\n'.join(f"| {r['test']} | {r['status']}{': '+r.get('detail','').replace('|','/').replace(chr(10),' ')[:160] if r['status']=='FAIL' else ''} |" for r in results)+'\n'
    (OUT/'REPORT.md').write_text(md,encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['passed','failed','browser','mode']}),flush=True)
    browser.close()
sys.exit(1 if any(r['status']=='FAIL' for r in results) else 0)
