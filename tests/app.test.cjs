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
  const catalog = JSON.parse(fs.readFileSync(path.join(root, 'docs/catalog.json')));
  const doc = catalog.documents.find(d => d.id === '24');
  // Document 24 remains in daily reading and SOURCE_INDEX; live questions no longer cite it.
  run("S.lang='tc'");
  const rendered = run("sourceHTML({id: Object.keys(SOURCE_INDEX.questions).find(id => SOURCE_INDEX.questions[id].includes('24')), source:{en:'x', tc:'y'}})");
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
    byId.delete(exam.qids[0]); store.set(ATTEMPTS, [old]);`);
  assert.equal(run('loadExam()'), null);
  assert.equal(run('store.get(EXAM,null)'), null);
  assert.equal(run('recordedResult(old).score'), 28);
  assert.equal(run('recordedResult(old).pass'), true);
  assert.equal(run('store.get(ATTEMPTS,[]).length'), 1);
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

test('a wrong answer enters the book and leaves it after two right answers in a row', () => {
  const run = app();
  run("startPractice(['m1-gn71']); answerPractice((byId.get('m1-gn71').answer + 1) % 5)");
  assert.deepEqual([...run("Object.keys(store.get('book', {}))")], ['m1-gn71']);
  assert.deepEqual([...run("bookIds()")], ['m1-gn71']);
  run("nextPracticeQ(); answerPractice(byId.get('m1-gn71').answer)");
  assert.equal(run("store.get('book', {})['m1-gn71'].k"), 1);
  run("nextPracticeQ(); answerPractice(byId.get('m1-gn71').answer)");
  assert.deepEqual([...run("Object.keys(store.get('book', {}))")], []);
  assert.deepEqual([...run("store.get('seen', [])")], ['m1-gn71']);
  const drawn = run("startExam(); const drawn = exam.qids.includes('m1-gn71'); exam.answers = {}; finishExam(false); drawn");
  assert.equal(run("bookIds().length"), 35);
  assert.equal(run("store.get('seen', []).length"), drawn ? 35 : 36);
});

test('practice draws the unseen questions of the selected parts before the seen ones', () => {
  const run = app();
  run("pmodSel = new Set([1]); store.set('seen', byMod.get(1).slice(0, 10).map(q => q.id)); startPractice()");
  const pool = [...run('practice.pool')], seen = new Set(run("store.get('seen', [])"));
  assert.equal(pool.length, run('byMod.get(1).length'));
  assert.deepEqual(pool.map(id => seen.has(id)), pool.map((_, i) => i >= pool.length - 10));
  assert.match(run('homeView()'), /錯題本|Wrong-answer book/);
});

test('clearing the answered record restores unseen-first practice without touching history, the book or settings', () => {
  const run = app();
  run(`pmodSel = new Set([1]);
    store.set('seen', byMod.get(1).slice(0, 10).map(q => q.id));
    book.set({'m1-gn71': {w:1,k:0,t:1}});
    store.set(ATTEMPTS, [{score:25,qids:['m1-gn71'],answers:{},moduleWrong:[0,0,0,0,0,0,0],pass:true,ts:1,usedMs:1}]);
    store.set(EXAM, {cur:0});
    store.set('lang','en');
    store.set('theme','dark');`);
  const htmlBefore = run('homeView()');
  assert.match(htmlBefore, /id="btn-clear-seen"/);
  assert.match(htmlBefore, /Clear answered record/);
  run("S.lang='tc'");
  assert.match(run('homeView()'), /清除已做紀錄/);
  run("S.lang='en'; clearSeen()");
  assert.deepEqual([...run("store.get('seen', [])")], []);
  assert.equal(run("store.get('book', {})['m1-gn71'].w"), 1);
  assert.equal(run("store.get(ATTEMPTS,[]).length"), 1);
  assert.equal(run("store.get(EXAM,null).cur"), 0);
  assert.equal(run("store.get('lang',null)"), 'en');
  assert.equal(run("store.get('theme',null)"), 'dark');
  const html = run('homeView()');
  assert.doesNotMatch(html, /id="btn-clear-seen"/);
  assert.match(html, /id="btn-book-clear"/);
  const n = run('bank.filter(inPractice).length');
  assert.match(html, new RegExp(`${n} of ${n} selected questions not yet answered`));
  run('startPractice()');
  const pool = [...run('practice.pool')];
  assert.equal(pool.length, n);
  assert.equal(new Set(pool).size, n);
  run("clearSeen(true)");
  assert.deepEqual([...run("store.get('seen', [])")], []);
  assert.deepEqual([...run("Object.keys(store.get('book', {}))")], []);
  assert.equal(run("store.get(ATTEMPTS,[]).length"), 1);
  assert.equal(run("store.get(EXAM,null).cur"), 0);
});

test('clearing mock-exam history and the book still leave the answered record in place', () => {
  const run = app();
  run(`store.set('seen', ['m1-gn71']);
    book.set({'m1-gn71': {w:1,k:0,t:1}});
    store.set(ATTEMPTS, [{score:25}]);
    store.set(EXAM, {cur:0});
    store.del(ATTEMPTS);
    book.set({});`);
  assert.deepEqual([...run("store.get('seen', [])")], ['m1-gn71']);
  assert.equal(run("store.get(EXAM,null).cur"), 0);
  assert.match(run('homeView()'), /id="btn-clear-seen"/);
  assert.doesNotMatch(run('homeView()'), /id="btn-clear"/);
  assert.doesNotMatch(run('homeView()'), /id="btn-book-clear"/);
});

test('practice shows the current item out of this session pool and restarts after a round', () => {
  const run = app();
  run("startPractice(['m1-gn71','m2-ca2','m3-ca3'])");
  assert.equal(run('practice.pool.length'), 3);
  assert.notEqual(run('practice.pool.length'), run('bank.length'));
  assert.match(run('practiceView()'), /Question 1 \/ 3/);
  assert.match(run('practiceView()'), /This session/);
  run('practice.idx=1; practice.perm=drawPerm(byId.get(practice.pool[1])); practice.chosen=null');
  assert.match(run('practiceView()'), /Question 2 \/ 3/);
  run("S.lang='tc'");
  assert.match(run('practiceView()'), /第 2 \/ 3 題/);
  run("S.lang='en'; practice.idx=2; nextPracticeQ()");
  assert.equal(run('practice.idx'), 0);
  assert.match(run('practiceView()'), /Question 1 \/ 3/);
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
