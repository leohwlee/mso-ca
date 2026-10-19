// Behaviour checks for the offline app; no browser packages are required.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'web/app.js'), 'utf8').replace(/boot\(\);\s*$/, '');
const questions = JSON.parse(fs.readFileSync(path.join(root, 'web/questions.json')));

function app() {
  const data = new Map();
  const sandbox = {
    console, URLSearchParams, Set, Map, Date, Math, JSON,
    setTimeout: () => 0, clearTimeout() {}, setInterval: () => 0, clearInterval() {},
    localStorage: { getItem: k => data.get(k) ?? null, setItem: (k,v) => data.set(k,v), removeItem: k => data.delete(k) },
    location: { search: '' },
    document: { addEventListener() {}, querySelector: () => null, title: 'Test' },
    window: { scrollTo() {}, matchMedia: () => ({ matches: false, addEventListener() {} }) },
    BANK: questions,
  };
  const ctx = vm.createContext(sandbox);
  vm.runInContext(source, ctx);
  vm.runInContext(`bank = BANK; bank.forEach(q => {
    byId.set(q.id,q); if (!byMod.has(q.module)) byMod.set(q.module,[]); byMod.get(q.module).push(q);
  }); S.lang='en'; render=()=>{}; toast=()=>{};`, ctx);
  return code => vm.runInContext(code, ctx);
}

test('answer citations name the real repository files in the selected language', () => {
  const run = app();
  const catalog = JSON.parse(fs.readFileSync(path.join(root, 'docs/catalog.json')));
  const guideline = catalog.documents.find(d => d.id === '03');
  for (const lang of ['en', 'tc']) {
    run(`S.lang='${lang}'`);
    const rendered = run("sourceHTML(byId.get('m6-ca7'))");
    assert.ok(rendered.includes(guideline.editions[lang.toUpperCase()].file));
    assert.ok(rendered.includes('../docs/'));
    assert.ok(rendered.includes('4.3.6'));
  }
  run("S.lang='both'");
  const both = run("sourceHTML(byId.get('m6-ca7'))");
  assert.ok(both.includes(guideline.editions.EN.file));
  assert.ok(both.includes(guideline.editions.TC.file));
});

test('Chinese citations for source 24 retain the English original and study-translation label', () => {
  const run = app();
  const quotes = JSON.parse(fs.readFileSync(path.join(root, 'docs/quotes.json')));
  const q = questions.find(q => quotes[q.id].tc.some(r => r.doc === '24'));
  const catalog = JSON.parse(fs.readFileSync(path.join(root, 'docs/catalog.json')));
  const doc = catalog.documents.find(d => d.id === '24');
  run("S.lang='tc'");
  const rendered = run(`sourceHTML(byId.get('${q.id}'))`);
  assert.ok(rendered.includes(doc.editions.EN.file));
  assert.ok(rendered.includes('學習譯文，英文原件'));
});

test('each mock contains 35 distinct questions, five from each part', () => {
  const run = app();
  for (let i=0; i<20; i++) {
    run('startExam()');
    assert.equal(run('new Set(exam.qids).size'), 35);
    assert.equal(run('exam.endsAt - exam.startedAt'), 75*60000);
    assert.equal(run('MODULES.every(m=>exam.qids.filter(id=>byId.get(id).module===m.n).length===5)'), true);
  }
});

test('custom practice respects a single or multiple selected parts and cycles without duplicates', () => {
  const run = app();
  for (const parts of ['[3]', '[1,4,7]']) {
    run(`pmodSel = new Set(${parts}); startPractice()`);
    assert.equal(run('practice.pool.every(id=>pmodSel.has(byId.get(id).module))'), true);
    assert.equal(run('practice.pool.length'), run('bank.filter(inPractice).length'));
    assert.equal(run('new Set(practice.pool).size'), run('practice.pool.length'));
    run('practice.idx=practice.pool.length-1; nextPracticeQ()');
    assert.equal(run('practice.idx'), 0);
    assert.equal(run('practice.chosen'), null);
  }
});

test('grading requires both total score and per-part floor', () => {
  const run = app();
  run('startExam(); const a = Object.fromEntries(exam.qids.map(id=>[id,byId.get(id).answer]))');
  assert.equal(run('grade(exam.qids,a).pass'), true);
  run('exam.qids.slice(0,3).forEach(id=>a[id]=(byId.get(id).answer+1)%5)');
  assert.equal(run('grade(exam.qids,a).score'), 32);
  assert.equal(run('grade(exam.qids,a).pass'), false);
  assert.equal(run('grade(exam.qids,{}).pass'), false);
});

test('source update invalidates incomplete paper but preserves completed scores and history export', () => {
  const run = app();
  run(`startExam(); const old = {qids: [...exam.qids], answers:{}, score:28,
    moduleWrong:[1,1,1,1,1,1,1], pass:true, ts:Date.now(), usedMs:1000};
    byId.delete(exam.qids[0]); store.set(attemptsKey(), [old]);`);
  assert.equal(run('loadExam()'), null);
  assert.equal(run('store.get(examKey(),null)'), null);
  assert.equal(run('recordedResult(old).score'), 28);
  assert.equal(run('recordedResult(old).pass'), true);
  assert.equal(run('store.get(attemptsKey(),[]).length'), 1);
  assert.equal(run('historyMarkdown([old]).includes("28/35")'), true);
});

test('home offers two study modes and keeps history within an expandable exam section', () => {
  const run = app();
  for (const lang of ['en','tc','both']) {
    run(`S.lang='${lang}'`);
    const html = run('homeView()');
    assert.match(html, /id="btn-start"/);
    assert.match(html, /id="btn-practice"/);
    assert.match(html, /class="exam-history"/);
    assert.doesNotMatch(html, /btn-drill|逐句判斷|Statement drill/);
    assert.equal((html.match(/data-pm=/g)||[]).length, 7);
  }
});

test('statement permutations retain the correct option and the matching explanations', () => {
  const run = app();
  assert.equal(run(`bank.every(q => {
    const p=drawPerm(q), a=arrange(q,p);
    const truth=p.map(i=>q.truth[i]);
    const key=a.shown[q.answer];
    const expected=truth.flatMap((t,i)=>t?[i+1]:[]);
    const claimed=key==='all'?p.map((_,i)=>i+1):key==='none'?[]:key;
    return p.every((i,j)=>q.en.notes[i] && q.tc.notes[i] && typeof truth[j]==='boolean') &&
      JSON.stringify(claimed)===JSON.stringify(expected) &&
      new Set(a.order).size===5 && a.order.includes(q.answer);
  })`), true);
});
