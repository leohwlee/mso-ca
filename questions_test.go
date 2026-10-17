package main

import (
	"encoding/json"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
	"testing"
	"unicode"
)

// Every item is a combination item in the shape of the real paper: a stem, four
// to six numbered statements, which of them are true, and five options naming
// sets of them. bank/FORMAT.md is the register of what the owner decided about
// that shape; these tests hold the bank to it.

type qLang struct {
	Q          string   `json:"q"`
	Statements []string `json:"statements"`
	Notes      []string `json:"notes,omitempty"`
	Explain    string   `json:"explain,omitempty"`
}

// fields are every piece of text a candidate can read in one language.
func (l qLang) fields() []string {
	return append(append([]string{l.Q, l.Explain}, l.Statements...), l.Notes...)
}

// option is one of an item's five options: a set of statement numbers, or
// "all" / "none" (All / None of the above).
type option struct {
	Token string
	Set   []int
}

func (o *option) UnmarshalJSON(b []byte) error {
	if len(b) > 0 && b[0] == '"' {
		return json.Unmarshal(b, &o.Token)
	}
	return json.Unmarshal(b, &o.Set)
}

func (o option) String() string {
	if o.Token != "" {
		return o.Token
	}
	return fmt.Sprint(o.Set)
}

// claims is the set of statements the option says are true, as a bit mask.
func (o option) claims(n int) uint {
	switch o.Token {
	case "all":
		return 1<<n - 1
	case "none":
		return 0
	}
	var m uint
	for _, x := range o.Set {
		m |= 1 << (x - 1)
	}
	return m
}

type question struct {
	ID       string    `json:"id"`
	Module   int       `json:"module"`
	Truth    []bool    `json:"truth"`
	Options  []option  `json:"options"`
	Answer   int       `json:"answer"`
	Traps    []*string `json:"traps,omitempty"`
	Fixed    bool      `json:"fixed,omitempty"`
	Official string    `json:"official,omitempty"`
	Source   struct {
		En string `json:"en"`
		Tc string `json:"tc"`
	} `json:"source"`
	En qLang `json:"en"`
	Tc qLang `json:"tc"`
}

func (q question) n() int { return len(q.Truth) }

func (q question) trueMask() uint {
	var m uint
	for i, t := range q.Truth {
		if t {
			m |= 1 << i
		}
	}
	return m
}

// Every active item carries a note per statement and a trap code per false one.
func (q question) annotated() bool { return len(q.En.Notes) > 0 || len(q.Tc.Notes) > 0 }

func (q question) side(lang string) qLang {
	if lang == "tc" {
		return q.Tc
	}
	return q.En
}

// The kinds of defect a false statement may carry (bank/FORMAT.md).
var trapCodes = map[string]bool{
	"offlist": true, "added": true, "scope": true, "reversed": true, "qualifier": true,
	"number": true, "period": true, "actor": true, "modal": true, "name": true, "condition": true,
}

// C&ED's printed blocks, in C&ED's order: MSSB/CA_01/2021 (then e) All of the
// above) and Guidance Notes ¶7.1 (five options, no e).
var (
	official4 = [][]int{{1, 2, 3}, {1, 2, 4}, {2, 3, 4}, {1, 3, 4}}
	gn71      = [][]int{{1, 2, 3}, {2, 3, 4}, {1, 3, 4}, {1, 2, 5}, {3, 4, 5}}
)

// Minimum bank size after the October 2026 combination-format migration.
var minPerModule = map[int]int{1: 26, 2: 45, 3: 41, 4: 45, 5: 55, 6: 45, 7: 40}

func wantTotal() int {
	n := 0
	for _, v := range minPerModule {
		n += v
	}
	return n
}

func loadBank(t *testing.T) []question {
	t.Helper()
	data, err := webFS.ReadFile("web/questions.json")
	if err != nil {
		t.Fatalf("read questions.json: %v", err)
	}
	var bank []question
	if err := json.Unmarshal(data, &bank); err != nil {
		t.Fatalf("parse questions.json: %v", err)
	}
	return bank
}

func sameSet(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

// canonicalOrder is the order the app displays options in, and the order they
// are stored in: C&ED's order for C&ED's blocks, otherwise smaller sets first and
// then by number, with All / None of the above last. bank/combo.py writes them
// so; a hand edit that breaks it would make the stored and the shown order differ.
func canonicalOrder(opts []option, n int) []option {
	var body, tail []option
	for _, o := range opts {
		if o.Token != "" {
			tail = append(tail, o)
		} else {
			body = append(body, o)
		}
	}
	is := func(block [][]int) bool {
		if len(body) != len(block) {
			return false
		}
		for _, b := range block {
			found := false
			for _, o := range body {
				found = found || sameSet(o.Set, b)
			}
			if !found {
				return false
			}
		}
		return true
	}
	var ordered []option
	switch {
	case n == 4 && len(tail) == 1 && is(official4):
		for _, b := range official4 {
			ordered = append(ordered, option{Set: b})
		}
	case n == 5 && len(tail) == 0 && is(gn71):
		for _, b := range gn71 {
			ordered = append(ordered, option{Set: b})
		}
	default:
		ordered = append(ordered, body...)
		sort.SliceStable(ordered, func(i, j int) bool {
			a, b := ordered[i].Set, ordered[j].Set
			if len(a) != len(b) {
				return len(a) < len(b)
			}
			for k := range a {
				if a[k] != b[k] {
					return a[k] < b[k]
				}
			}
			return false
		})
	}
	return append(ordered, tail...)
}

func TestBankIntegrity(t *testing.T) {
	bank := loadBank(t)
	if want := wantTotal(); len(bank) < want {
		t.Errorf("bank has %d questions, want at least %d", len(bank), want)
	}

	seen := map[string]bool{}
	perMod := map[int]int{}
	for _, q := range bank {
		if seen[q.ID] {
			t.Errorf("%s: duplicate id", q.ID)
		}
		seen[q.ID] = true
		if q.Module < 1 || q.Module > 7 {
			t.Errorf("%s: module %d out of range", q.ID, q.Module)
		}
		perMod[q.Module]++
		if want := fmt.Sprintf("m%d-", q.Module); !strings.HasPrefix(q.ID, want) {
			t.Errorf("%s: id does not match module %d (want prefix %q)", q.ID, q.Module, want)
		}
		if q.Source.En == "" || q.Source.Tc == "" {
			t.Errorf("%s: missing source citation", q.ID)
		}

		n := q.n()
		if n < 4 || n > 6 {
			t.Errorf("%s: %d statements; an item has 4 to 6", q.ID, n)
			continue
		}
		for _, lang := range []string{"en", "tc"} {
			l := q.side(lang)
			if strings.TrimSpace(l.Q) == "" {
				t.Errorf("%s (%s): empty stem", q.ID, lang)
			}
			if len(l.Statements) != n {
				t.Errorf("%s (%s): %d statements, but truth has %d", q.ID, lang, len(l.Statements), n)
			}
			for i, s := range l.Statements {
				if strings.TrimSpace(s) == "" {
					t.Errorf("%s (%s): statement %d empty", q.ID, lang, i+1)
				}
			}
			if q.annotated() {
				if len(l.Notes) != n {
					t.Errorf("%s (%s): %d notes for %d statements", q.ID, lang, len(l.Notes), n)
				}
				for i, s := range l.Notes {
					if strings.TrimSpace(s) == "" {
						t.Errorf("%s (%s): note %d empty", q.ID, lang, i+1)
					}
				}
			} else if strings.TrimSpace(l.Explain) == "" {
				t.Errorf("%s (%s): neither notes nor an explanation", q.ID, lang)
			}
		}

		// Migration is complete: no unannotated or fixed-order items may return.
		if q.Fixed || !q.annotated() {
			t.Errorf("%s: every item must allow reordering and carry a note per statement", q.ID)
		}

		if q.annotated() {
			if len(q.Traps) != n {
				t.Errorf("%s: %d trap codes for %d statements", q.ID, len(q.Traps), n)
			} else {
				for i, tr := range q.Traps {
					switch {
					case q.Truth[i] && tr != nil:
						t.Errorf("%s: statement %d is true but carries the trap %q", q.ID, i+1, *tr)
					case !q.Truth[i] && tr == nil:
						t.Errorf("%s: statement %d is false but names no trap", q.ID, i+1)
					case tr != nil && !trapCodes[*tr]:
						t.Errorf("%s: statement %d has the unknown trap %q", q.ID, i+1, *tr)
					}
				}
			}
		} else if len(q.Traps) > 0 {
			t.Errorf("%s: trap codes without notes", q.ID)
		}

		if len(q.Options) != 5 {
			t.Errorf("%s: %d options, want 5", q.ID, len(q.Options))
			continue
		}
		masks := map[uint]bool{}
		for i, o := range q.Options {
			switch {
			case o.Token == "all" || o.Token == "none":
				if i != 4 {
					t.Errorf("%s: %q is option %c; All / None of the above is always the last", q.ID, o.Token, 'a'+rune(i))
				}
			case o.Token != "":
				t.Errorf("%s: option %c is %q", q.ID, 'a'+rune(i), o.Token)
			default:
				ok := len(o.Set) > 0 && len(o.Set) < n
				for k, x := range o.Set {
					ok = ok && x >= 1 && x <= n && (k == 0 || x > o.Set[k-1])
				}
				if !ok {
					t.Errorf("%s: option %c %v is not an ascending list of some of the statements 1-%d", q.ID, 'a'+rune(i), o.Set, n)
				}
			}
			m := o.claims(n)
			if masks[m] {
				t.Errorf("%s: option %c says the same as another option", q.ID, 'a'+rune(i))
			}
			masks[m] = true
		}
		if canon := canonicalOrder(q.Options, n); fmt.Sprint(canon) != fmt.Sprint(q.Options) {
			t.Errorf("%s: options %v are not in display order %v", q.ID, q.Options, canon)
		}
		var hits []int
		for i, o := range q.Options {
			if o.claims(n) == q.trueMask() {
				hits = append(hits, i)
			}
		}
		if len(hits) != 1 {
			t.Errorf("%s: %d options match the true statements, want exactly 1", q.ID, len(hits))
		} else if hits[0] != q.Answer {
			t.Errorf("%s: answer is %d but the option matching the true statements is %d", q.ID, q.Answer, hits[0])
		}
	}
	for m := 1; m <= 7; m++ {
		if perMod[m] < minPerModule[m] {
			t.Errorf("module %d has %d questions, want at least %d", m, perMod[m], minPerModule[m])
		}
	}
}

// Retired ids remain reserved even after their full snapshots leave the tree.
// Reusing one would attach an old saved answer to an unrelated question.
func TestRetiredIDs(t *testing.T) {
	data, err := os.ReadFile("bank/retired-ids.json")
	if err != nil {
		t.Fatal(err)
	}
	var retired struct {
		SourceRevision string   `json:"source_revision"`
		IDs            []string `json:"ids"`
	}
	if err := json.Unmarshal(data, &retired); err != nil {
		t.Fatal(err)
	}
	if len(retired.SourceRevision) != 40 || len(retired.IDs) < 1509 {
		t.Fatalf("retirement register lost its source revision or ids: %q, %d ids", retired.SourceRevision, len(retired.IDs))
	}
	seen := map[string]bool{}
	for _, id := range retired.IDs {
		if seen[id] {
			t.Errorf("duplicate retired id %s", id)
		}
		seen[id] = true
	}
	for _, q := range loadBank(t) {
		if seen[q.ID] {
			t.Errorf("%s reuses a retired question id", q.ID)
		}
	}
}

// automorphisms are the renumberings of statements 1..n that map an option set
// onto itself.
func automorphisms(sets [][]int, n int) [][]int {
	key := func(s []int, p []int) string {
		var m uint
		for _, x := range s {
			m |= 1 << (p[x-1] - 1)
		}
		return strconv.FormatUint(uint64(m), 2)
	}
	id := make([]int, n)
	for i := range id {
		id[i] = i + 1
	}
	have := map[string]bool{}
	for _, s := range sets {
		have[key(s, id)] = true
	}
	var out [][]int
	var permute func(k int, p []int, used []bool)
	permute = func(k int, p []int, used []bool) {
		if k == n {
			for _, s := range sets {
				if !have[key(s, p)] {
					return
				}
			}
			out = append(out, append([]int(nil), p...))
			return
		}
		for v := 1; v <= n; v++ {
			if !used[v] {
				used[v] = true
				permute(k+1, append(p, v), used)
				used[v] = false
			}
		}
	}
	permute(0, nil, make([]bool, n+1))
	return out
}

// TestOptionSymmetry: a candidate who knows nothing can still read an option
// set — the option that shares most with the others, the statement printed in
// most options, the only subset of its size. The options are built so that none
// of that singles out the key: any option the same size as the key can be turned
// into it by renumbering statements in a way that maps the whole set onto itself
// (bank/combo.py). C&ED's own sample items keep C&ED's blocks.
func TestOptionSymmetry(t *testing.T) {
	for _, q := range loadBank(t) {
		if q.Official != "" || len(q.Options) != 5 || q.Answer < 0 || q.Answer > 4 || q.Options[q.Answer].Token != "" {
			continue
		}
		var sets [][]int
		for _, o := range q.Options {
			if o.Token == "" {
				sets = append(sets, o.Set)
			}
		}
		key := q.Options[q.Answer].Set
		orbit := map[string]bool{}
		for _, p := range automorphisms(sets, q.n()) {
			var img []int
			for _, x := range key {
				img = append(img, p[x-1])
			}
			sort.Ints(img)
			orbit[fmt.Sprint(img)] = true
		}
		for _, s := range sets {
			if len(s) == len(key) && !orbit[fmt.Sprint(s)] {
				t.Errorf("%s: option %v is the size of the key %v but no renumbering of the option set turns one into the other",
					q.ID, s, key)
			}
		}
	}
}

// TestTruthCounts: the papers sat in October 2026 had anywhere from one true
// statement to all of them, while every item in the old bank had all true or
// exactly one false (four statements) or exactly two false (five). A candidate
// trained on that learns to hunt for the one false statement. Items written to
// the new rules vary the count; once there are enough of them to measure, the
// bank must not make any count a safe assumption.
func TestTruthCounts(t *testing.T) {
	var n, allTrue, oneFalse, more int
	for _, q := range loadBank(t) {
		if !q.annotated() {
			continue
		}
		n++
		f := 0
		for _, v := range q.Truth {
			if !v {
				f++
			}
		}
		switch f {
		case 0:
			allTrue++
		case 1:
			oneFalse++
		default:
			more++
		}
	}
	if n < 40 {
		t.Logf("%d annotated items; the distribution is checked from 40", n)
		return
	}
	share := func(k int) float64 { return float64(k) / float64(n) }
	t.Logf("%d annotated items: all true %.0f%%, one false %.0f%%, two or more false %.0f%%",
		n, share(allTrue)*100, share(oneFalse)*100, share(more)*100)
	if s := share(allTrue); s < 0.10 || s > 0.30 {
		t.Errorf("all statements true in %.0f%% of items, want 10%% to 30%%", s*100)
	}
	if s := share(oneFalse); s > 0.60 {
		t.Errorf("exactly one statement false in %.0f%% of items, want at most 60%%", s*100)
	}
	if s := share(more); s < 0.20 {
		t.Errorf("two or more statements false in only %.0f%% of items, want at least 20%%", s*100)
	}
}

// TestTrapMix: the papers sat set their traps in many ways — a figure, a time
// limit, an item off the list, a qualifier dropped — and a bank that leans on one
// kind teaches candidates to check for that kind only.
func TestTrapMix(t *testing.T) {
	counts := map[string]int{}
	total := 0
	for _, q := range loadBank(t) {
		for _, tr := range q.Traps {
			if tr != nil {
				counts[*tr]++
				total++
			}
		}
	}
	if total < 60 {
		t.Logf("%d false statements carry a trap code; the mix is checked from 60", total)
		return
	}
	var kinds []string
	for k, c := range counts {
		kinds = append(kinds, fmt.Sprintf("%s %d", k, c))
		if share := float64(c) / float64(total); share > 0.35 {
			t.Errorf("%.0f%% of false statements are %q traps, want at most 35%%", share*100, k)
		}
	}
	sort.Strings(kinds)
	t.Logf("traps: %s", strings.Join(kinds, ", "))
	if len(counts) < 6 {
		t.Errorf("false statements use %d kinds of trap, want at least 6", len(counts))
	}
}

// TestNoDuplicateStems guards the bank against the main risk of a large
// question bank: the same proposition asked twice in slightly different words.
// Items are compared as 4-word shingles of stem and statements within a module,
// in both languages — see shingles, which until September 2026 cut Chinese into
// a single token and so compared Chinese stems for exact equality and nothing else.
func TestNoDuplicateStems(t *testing.T) {
	bank := loadBank(t)

	byMod := map[int][]question{}
	for _, q := range bank {
		byMod[q.Module] = append(byMod[q.Module], q)
	}
	for _, lang := range []string{"en", "tc"} {
		for m := 1; m <= 7; m++ {
			qs := byMod[m]
			sets := make([]map[string]bool, len(qs))
			for i, q := range qs {
				side := q.side(lang)
				sets[i] = shingles(side.Q + " " + strings.Join(side.Statements, " "))
			}
			for i := range qs {
				for j := i + 1; j < len(qs); j++ {
					if s := jaccard(sets[i], sets[j]); s >= 0.75 {
						t.Errorf("%s module %d: %s and %s are near-duplicates (similarity %.2f)",
							lang, m, qs[i].ID, qs[j].ID, s)
					}
				}
			}
		}
	}

	// A September 2026 review found m1-93 and m6-190 carrying byte-identical
	// Chinese stems on the same paragraph with the same answer, invisible to the
	// per-module sweep, because their English wording had drifted apart while the
	// Chinese had not. An exact match on the stem and statements catches that.
	for _, lang := range []string{"en", "tc"} {
		byText := map[string][]string{}
		for _, q := range bank {
			side := q.side(lang)
			text := strings.TrimSpace(nonWord.ReplaceAllString(strings.ToLower(side.Q+" "+strings.Join(side.Statements, " ")), " "))
			byText[text] = append(byText[text], q.ID)
		}
		for text, ids := range byText {
			if len(ids) > 1 {
				t.Errorf("%s: %s ask the same question word for word: %q", lang, strings.Join(ids, ", "), text)
			}
		}
	}
}

// TestNoTwinStatements: a statement that another item already makes is asked
// twice, and a near copy with the opposite truth tells a candidate which of the
// two to doubt; an audit in September 2026 found 77 near-identical pairs, 19 of
// them true in one item and false in the other. Exact repeats are caught here;
// a near copy needs a reader. This checks every active item after migration.
func TestNoTwinStatements(t *testing.T) {
	for _, lang := range []string{"en", "tc"} {
		seen := map[string]string{}
		for _, q := range loadBank(t) {
			if !q.annotated() {
				continue
			}
			for i, s := range q.side(lang).Statements {
				k := strings.TrimSpace(nonWord.ReplaceAllString(strings.ToLower(s), " "))
				where := fmt.Sprintf("%s statement %d", q.ID, i+1)
				if prev, ok := seen[k]; ok && !strings.HasPrefix(prev, q.ID+" ") {
					t.Errorf("%s: %s and %s make the same statement: %q", lang, prev, where, s)
				}
				seen[k] = where
			}
		}
	}
}

// TestCitationHasLocator: a citation must name a place a reader can turn to —
// a paragraph, section, item or schedule number — not just a document.
func TestCitationHasLocator(t *testing.T) {
	digit := regexp.MustCompile(`\d`)
	for _, q := range loadBank(t) {
		if !digit.MatchString(q.Source.En) {
			t.Errorf("%s: citation %q names no paragraph or section", q.ID, q.Source.En)
		}
	}
}

// TestSectionNumberWord: a numbered section of the Ordinance is 第20(1)(b)條 and a
// numbered Guideline paragraph 第2(b)段. No Chinese source writes either as 第20(1)(b)款
// (款 alone, as in 第(3)款, is a subsection referred to from inside its own section).
// The blind review of September 2026 found 29 such references in 20 questions.
// Nor does any Chinese source number a part with 節: the Licensing Guide calls
// its Roman-numbered parts 條 (請參閱第 XIV 條的收費表), where five questions had
// written 第XVI節 until the source texts were first searched for it.
var (
	sectionKuan = regexp.MustCompile(`第\d+[A-Z]*(?:\([0-9A-Za-z]+\))+款`)
	romanJie    = regexp.MustCompile(`第\s*[IVX]+\s*節`)
)

func TestSectionNumberWord(t *testing.T) {
	for _, q := range loadBank(t) {
		for _, f := range append(q.Tc.fields(), q.Source.Tc) {
			for _, m := range sectionKuan.FindAllString(f, -1) {
				t.Errorf("%s: %q writes a numbered section with 款; the Ordinance says 條, the Guideline 段", q.ID, m)
			}
			for _, m := range romanJie.FindAllString(f, -1) {
				t.Errorf("%s: %q; the Licensing Guide calls its Roman-numbered parts 條, as in 第XIV條", q.ID, m)
			}
		}
	}
}

// TestTraditionalCharacters: the Chinese side is Traditional Chinese throughout. These
// are simplified-only forms of common characters (則, 說, 這, 為, 與, 應 ...); one slipped
// into a fixer's draft during the September 2026 review.
const simplifiedOnly = "则说这为与应须时实际关条项过发会经务业资产权报单录证据审处规员责负济称纳统计认识义还进对当现并问题获确护险币汇银营类罚级构讯检视让论设读转选阶历场断备节约"

func TestTraditionalCharacters(t *testing.T) {
	for _, q := range loadBank(t) {
		for _, f := range append(q.Tc.fields(), q.Source.Tc) {
			if i := strings.IndexAny(f, simplifiedOnly); i >= 0 {
				r := []rune(f[i:])[0]
				t.Errorf("%s: Chinese text has the simplified character %q", q.ID, r)
			}
		}
	}
}

// TestChineseStatutoryTerms: the Traditional Chinese paper must use the terms
// the official Chinese editions use, so a candidate meets the same wording in
// the exam room as in the Ordinance and the Guideline. The check covers the
// citation field as well: a review in September 2026 found five citations
// carrying non-statutory terms precisely because this test used to skip it.
func TestChineseStatutoryTerms(t *testing.T) {
	banned := map[string]string{
		"電匯":      "電傳轉帳 or 電傳轉賬 (wire transfer)",
		"過渡期客戶":   "先前客戶 (pre-existing customer)",
		"單次交易":    "非經常交易 (occasional transaction)",
		"證券交易所":   "認可證券市場 or 證券市場 (recognized stock market)",
		"指明條文":    "指明的條文 (specified provision)",
		"洗錢事務主任":  "洗錢報告主任 (MLRO)",
		"安施塔特":    "機構（anstalt）",
		"通風報信":    "通風報訊 (tipping off)",
		"洩密":      "通風報訊 (tipping off)",
		"匯出機構":    "匯款機構 (ordering institution)",
		"同等司法管轄區": "對等司法管轄區 (equivalent jurisdiction)",
		// September 2026 term sweep: each of these appears in none of the 23 Chinese
		// sources; most render an English term instead of using the Chinese text's own.
		"陳述機會":         "陳詞機會 (s.22(1), s.34(3), s.44(1), s.59(3), s.60(3); Licensing Guide ¶7.2)",
		"詞彙表":          "詞彙部分 (Guideline ¶1.2), or the heading 主要用語及縮寫詞彙",
		"顯赫公職":         "重要公職 (Sch. 2 s.1, politically exposed person)",
		"密切聯繫人":        "關係密切的人 (Sch. 2 s.1)",
		"糾正命令":         "the section's words: 命令採取糾正行動 (s.43(4)), 飭令採取糾正行動的命令 (s.21(4))",
		"每日罰款":         "按日罰款 (s.21(4), s.43(4))",
		"評核中心":         "試場 (Guidance Notes)",
		"匯報責任":         "舉報責任 (Guideline ¶7.7; TBML circular)",
		"報告責任":         "舉報責任 (Guideline ¶7.7, fn 60)",
		"未遂交易":         "試圖進行的交易 (Guideline; TBML circular)",
		"加強查核":         "更嚴格的查核 (Guideline ¶6.17–6.18)",
		"打擊洗錢制度":       "打擊洗錢／恐怖分子資金籌集制度",
		"機構風險評估":       "機構層面的洗錢／恐怖分子資金籌集風險評估 (Guideline ch. 2)",
		"恐怖分子聯繫者":      "與恐怖分子有聯繫者 (Guideline)",
		"前線職員":         "前線工作人員 (Guideline ¶9.5(b)), or the cited source's own word",
		"紀律權力":         "紀律處分權力 (the Ordinance)",
		"個人持牌人":        "a description in the cited source's words (no source names this class)",
		"法團持牌人":        "屬法團的持牌人, or the cited source's words",
		"無特定處所經營者":     "在沒有特定處所的情況下經營金錢服務 (Licensing Guide ¶8.4, ¶10.1)",
		"不設特定處所":       "在沒有特定處所的情況下經營金錢服務 (Licensing Guide ¶8.4, ¶10.1)",
		"全面盡職審查":       "客戶盡職審查措施 (Sch. 2 s.2); no source says 'full CDD'",
		"標準盡職審查":       "客戶盡職審查措施 (Sch. 2 s.2); no source says 'standard CDD'",
		"視察人員":         "獲授權人 (Part 3)",
		"作出可疑交易報告":     "提交可疑交易報告 (Guideline)",
		"找換店":          "the cited source's words, e.g. 貨幣兌換",
		"遞交打擊洗錢政策的指引":  "《遞交打擊洗錢及恐怖分子資金籌集政策的指引》 (doc 07's title)",
		"在合理切實可行範圍內盡快": "the cited provision's words: 在合理地切實可行的範圍內 (Ordinance; Guideline ch. 4, 10), 在切實可行範圍內盡快 (Guideline ¶7.5(b))",
		"停止有效":         "不再有效 (s.42)",
		"非面對面客戶":       "客戶不曾為身分識別的目的而現身 (Guideline ¶4.10.1)",
		"認識你的客戶":       "the cited source's words",
		"倚賴":           "依賴, or the cited provision's words (Sch. 2 s.18: 藉著中介人執行客戶盡職審查措施)",
		"境外":           "香港以外 / 外地, as the cited provision says",
		"註冊成立":         "成立為法團 (the Ordinance; the Guideline)",
		// September 2026 blind review of modules 2-4: renderings no Chinese source uses
		"意圖欺騙":    "出於詐騙意圖 / 出於詐騙…的意圖 (s.10, s.13, s.52)",
		"小組成員":    "委員 (Sch. 4: 委員團的委員)",
		"預備會議":    "初步會議 (Sch. 4 s.7)",
		"編號戶口":    "保密號碼戶口 / 設有保密號碼的戶口 (Guideline ¶4.14.1, fn 49)",
		"有權享有或控制": "有權攤分或控制 (s.24; Sch. 2 s.1)",
		"七國集團高峰會": "七大工業國財長會議 (Guideline ch. 1)",
		"同業附屬企業":  "經營與金融機構相同的業務的附屬企業 (Sch. 2 s.22)",
		"所避免成本":   "避免的開支 (s.21(2)(c)(ii); Disciplinary Fining Guideline ¶6)",
		"保險保單":    "保險單 (Sch. 2 s.4(5))",
		"整筆保費":    "一筆整付保費 (Sch. 2 s.4(5)(c))",
		"來源司法管轄區": "目標司法管轄區 (AML/CFT policy guideline)",
		"藐視程序":    "the section's words, e.g. 按藐視法庭罪追究 (s.14)",
	}
	for _, q := range loadBank(t) {
		if q.Official != "" {
			continue // C&ED's own words
		}
		for _, f := range append(q.Tc.fields(), q.Source.Tc) {
			for bad, want := range banned {
				if strings.Contains(f, bad) {
					t.Errorf("%s: Chinese text uses %q, want %s", q.ID, bad, want)
				}
			}
		}
	}
}

// TestNoDanglingReference: 該 means "the said", so 該客戶 is a customer already
// named. Used cold it renders "the customer" or "the MSO" word for word and
// leaves the reader asking which one; the sources name it first. A candidate
// reads the stem first. The statements of an item the app reorders may come in
// any order, so each may lean only on the stem; those of a fixed item are read in
// order. A note may lean on its own statement, an explanation on everything.
var danglingRefs = []struct {
	form        *regexp.Regexp // 該, an optional classifier, the noun
	antecedents []string       // one of these, said earlier, gives it something to refer to
}{
	{regexp.MustCompile(`該[項宗筆名間位]?(?:金錢服務)?經營者`), []string{"經營者"}},
	{regexp.MustCompile(`該[項宗筆名間位]?客戶`), []string{"客戶"}},
	{regexp.MustCompile(`該[項宗筆名間位]?交易`), []string{"交易", "匯款", "電傳轉帳", "電傳轉賬", "兌換"}},
	{regexp.MustCompile(`該[項宗筆名間位]?機構`), []string{"機構"}},
	{regexp.MustCompile(`該[項宗筆名間位]?公司`), []string{"公司"}},
	{regexp.MustCompile(`該[項宗筆名間位]?業務關係`), []string{"業務關係"}},
	{regexp.MustCompile(`該[項宗筆名間位]?持牌人`), []string{"持牌人"}},
	{regexp.MustCompile(`該[項宗筆名間位]?匯款人`), []string{"匯款人"}},
	{regexp.MustCompile(`該[項宗筆名間位]?申請人`), []string{"申請人"}},
}

func TestNoDanglingReference(t *testing.T) {
	for _, q := range loadBank(t) {
		if q.Official != "" {
			continue
		}
		check := func(read, f string) {
			for _, r := range danglingRefs {
				loc := r.form.FindStringIndex(f)
				if loc == nil {
					continue
				}
				before := r.form.ReplaceAllString(read+f[:loc[0]], "")
				named := false
				for _, a := range r.antecedents {
					named = named || strings.Contains(before, a)
				}
				if !named {
					t.Errorf("%s: %s has nothing to refer back to in %q", q.ID, f[loc[0]:loc[1]], f)
				}
			}
		}
		check("", q.Tc.Q)
		read := q.Tc.Q
		for i, s := range q.Tc.Statements {
			if q.Fixed {
				check(read, s)
				read += s
			} else {
				check(q.Tc.Q, s)
				if i < len(q.Tc.Notes) {
					check(q.Tc.Q+s, q.Tc.Notes[i])
				}
			}
		}
		check(q.Tc.Q+strings.Join(q.Tc.Statements, ""), q.Tc.Explain)
	}
}

// TestGuidelineParagraphWord: the Chinese Guideline calls its numbered paragraphs
// and sub-paragraphs 段 (第[4.11.12(b)]段, 附錄A第[10]段); 款 and 條 are the
// Ordinance's words for its subsections and sections. A Guideline number followed
// by 款 renders the English "paragraph (b)" instead of using the Chinese text's
// word. The September 2026 blind review found 18 questions doing this.
var guidelineKuan = regexp.MustCompile(`第\d+\.\d+(?:\.\d+)*(?:\([a-z0-9]+\))*(?:及\([a-z0-9]+\))*款|附錄A第\d+(?:\([a-z0-9]+\))*款`)

func TestGuidelineParagraphWord(t *testing.T) {
	for _, q := range loadBank(t) {
		for _, f := range append(q.Tc.fields(), q.Source.Tc) {
			if m := guidelineKuan.FindString(f); m != "" {
				t.Errorf("%s: %q calls a Guideline paragraph 款; the Guideline says 段", q.ID, m)
			}
		}
	}
}

// TestJFIUInvestigation: C&ED's own sample (Example 5) calls the JFIU the "Joint
// Financial Investigation Unit" in a statement it keys true, so the register (B21)
// judges such a statement on the rest of what it says. The wording may appear, but
// a false statement never turns on it; the first module 5 batch had one that did.
func TestJFIUInvestigation(t *testing.T) {
	for _, q := range loadBank(t) {
		for i, s := range q.En.Statements {
			if i < len(q.Traps) && q.Traps[i] != nil && *q.Traps[i] == "name" &&
				strings.Contains(strings.ToLower(s), "financial investigation unit") {
				t.Errorf("%s: a false statement turns on the JFIU's name alone, which register B21 rules out: %q", q.ID, s)
			}
		}
	}
}

// TestMLTFPairing: where the English says ML/TF the Chinese must carry both
// limbs. Dropping the terrorist-financing half changes what is being asked.
func TestMLTFPairing(t *testing.T) {
	for _, q := range loadBank(t) {
		en, tc := q.En.fields(), q.Tc.fields()
		if len(en) != len(tc) {
			continue // TestBankIntegrity reports the mismatch
		}
		for i := range en {
			if strings.Contains(en[i], "ML/TF") &&
				strings.Contains(tc[i], "洗錢") && !strings.Contains(tc[i], "恐怖分子") {
				t.Errorf("%s: English says ML/TF but the Chinese says 洗錢 alone: %q", q.ID, tc[i])
			}
		}
	}
}

// TestNoPositionalReferences: the app reorders an item's statements at every
// draw and renumbers its options, so "statement 2", "option B" or 選項三 names
// whatever landed there in that draw, not what the author meant. Notes refer to
// what a statement says. Only a fixed item's explanation may number statements,
// because its statements never move. The September 2026 review found 37
// positional references written against the authored order.
func TestNoPositionalReferences(t *testing.T) {
	options := []*regexp.Regexp{
		regexp.MustCompile(`(?i)\b(?:option|distractor)s?\s*\(?[1-5]\)?\b`),
		// the letter stays case-sensitive: lower-cased, "answer a question" and
		// "the choice a licensee makes" would both match and fail a sound question
		regexp.MustCompile(`\b(?i:option|answer|choice)\s+[A-E]\b`),
		regexp.MustCompile(`(?i)\b(?:first|second|third|fourth|fifth|last)\s+(?:option|choice|answer)\b`),
		regexp.MustCompile(`選項\s*[一二三四五1-5A-Ea-e]`),
		regexp.MustCompile(`第[一二三四五]個?選項`),
	}
	// a statement named by its place, or leaning on the ones printed before it
	statements := []*regexp.Regexp{
		regexp.MustCompile(`(?i)\bstatements?\s*\(?\d`),
		regexp.MustCompile(`(?i)\b(?:first|second|third|fourth|fifth|sixth|last|other)\s+statements?\b`),
		regexp.MustCompile(`陳述\s*[（(]?\d`),
		regexp.MustCompile(`第\s*[\d一二三四五六]\s*[項句]陳述`),
		regexp.MustCompile(`(?i)\b(?:the|this) above\b|上述(?:各項|陳述)`),
	}
	for _, q := range loadBank(t) {
		for _, lang := range []string{"en", "tc"} {
			l := q.side(lang)
			fields := map[string]string{"q": l.Q, "explain": l.Explain}
			for i, s := range l.Statements {
				fields[fmt.Sprintf("statement %d", i+1)] = s
			}
			for i, s := range l.Notes {
				fields[fmt.Sprintf("note %d", i+1)] = s
			}
			for name, text := range fields {
				// a fixed item's statements never move, so its explanation may
				// number them; the items converted from the old bank are fixed
				pats := options
				if !q.Fixed {
					pats = append(append([]*regexp.Regexp{}, options...), statements...)
				}
				for _, re := range pats {
					if m := re.FindString(text); m != "" {
						t.Errorf("%s (%s %s): refers to a statement or option by position (%q); name it by what it says",
							q.ID, lang, name, m)
						break
					}
				}
			}
		}
	}
}

// TestNoDuplicateAnswers catches the duplicate TestNoDuplicateStems cannot see.
// That test compares wording, within one module. But the same fact asked in
// different words, in a different module, looks nothing alike and is invisible
// to it — three such pairs were found in September 2026 (m3-17/m6-268,
// m1-70/m6-198, m1-117/m6-184), each asking one thing twice. The sharp signal is
// the pair (cited passage, statements): two items that cite the same provision
// and make the same statements ask one question.
func TestNoDuplicateAnswers(t *testing.T) {
	for _, lang := range []string{"en", "tc"} {
		seen := map[string][]string{}
		for _, q := range loadBank(t) {
			src := q.Source.En
			if lang == "tc" {
				src = q.Source.Tc
			}
			body := strings.TrimSpace(nonWord.ReplaceAllString(strings.ToLower(strings.Join(q.side(lang).Statements, " ")), " "))
			src = strings.TrimSpace(nonWord.ReplaceAllString(strings.ToLower(src), " "))
			seen[src+" || "+body] = append(seen[src+" || "+body], q.ID)
		}
		for key, ids := range seen {
			if len(ids) > 1 {
				t.Errorf("%s: %s cite the same passage and make the same statements: %q", lang, strings.Join(ids, ", "), key)
			}
		}
	}
}

var nonWord = regexp.MustCompile(`[^\p{L}\p{N}]+`)

// shingles cuts a text into overlapping 4-word runs for comparison. Written
// words are separated by spaces, so Fields finds them; Chinese is not, so a
// Chinese text collapses into a single "word" and every comparison degenerates
// into an exact match. That silently disabled near-duplicate detection on half
// the bank until a September 2026 sweep found two cross-module pairs by hand.
// shinglesCJK is the Chinese equivalent, cutting 4-character runs instead.
func shingles(s string) map[string]bool {
	if cjkHeavy(s) {
		return shinglesCJK(s)
	}
	words := strings.Fields(nonWord.ReplaceAllString(strings.ToLower(s), " "))
	out := map[string]bool{}
	const k = 4
	if len(words) < k {
		out[strings.Join(words, " ")] = true
		return out
	}
	for i := 0; i+k <= len(words); i++ {
		out[strings.Join(words[i:i+k], " ")] = true
	}
	return out
}

func cjkHeavy(s string) bool {
	cjk, letters := 0, 0
	for _, r := range s {
		switch {
		case unicode.Is(unicode.Han, r):
			cjk++
			letters++
		case unicode.IsLetter(r):
			letters++
		}
	}
	return letters > 0 && cjk*100/letters >= 30
}

func shinglesCJK(s string) map[string]bool {
	runes := []rune(nonWord.ReplaceAllString(s, ""))
	out := map[string]bool{}
	const k = 4
	if len(runes) < k {
		out[string(runes)] = true
		return out
	}
	for i := 0; i+k <= len(runes); i++ {
		out[string(runes[i:i+k])] = true
	}
	return out
}

func jaccard(a, b map[string]bool) float64 {
	if len(a) == 0 || len(b) == 0 {
		return 0
	}
	inter := 0
	for k := range a {
		if b[k] {
			inter++
		}
	}
	return float64(inter) / float64(len(a)+len(b)-inter)
}

// spread reports how unevenly a set of statement texts is sized: the gap
// between the longest and the shortest, as a share of the mean.
func spread(ss []string) (gap int, share float64) {
	if len(ss) == 0 {
		return 0, 0
	}
	lo, hi, sum := 1<<30, 0, 0
	for _, s := range ss {
		n := len([]rune(s))
		sum += n
		if n < lo {
			lo = n
		}
		if n > hi {
			hi = n
		}
	}
	return hi - lo, float64(hi-lo) / (float64(sum) / float64(len(ss)))
}

// TestStatementLengthSpread carries over the lesson of the old four-option
// bank, where the key was the longest option in 83% of questions and "always
// pick the longest" passed 64% of simulated papers. In a combination item the
// statements are what can leak: when first measured, the false statement was the
// longest or the shortest of the four in 14% of high-spread items against 50% by
// chance — the outliers were reliably true, which hands over an elimination.
// Inside one item every statement should occupy about the same space. The floor
// exempts genuinely short sets: "$8,000" against "$120,000" signals nothing.
func TestStatementLengthSpread(t *testing.T) {
	const tol = 0.40
	floor := map[string]int{"en": 20, "tc": 8}
	var bad []string
	for _, q := range loadBank(t) {
		if q.Official != "" {
			continue
		}
		for _, lang := range []string{"en", "tc"} {
			if gap, share := spread(q.side(lang).Statements); gap > floor[lang] && share > tol {
				bad = append(bad, fmt.Sprintf("%s [%s]: %d runes apart, %.0f%% of mean", q.ID, lang, gap, share*100))
			}
		}
	}
	if len(bad) > 0 {
		t.Errorf("%d item/language pairs vary too much in statement length; want the longest and shortest within %.0f%% of the mean (or %d/%d runes apart)",
			len(bad), tol*100, floor["en"], floor["tc"])
		for i, s := range bad {
			if i == 15 {
				t.Logf("... and %d more", len(bad)-15)
				break
			}
			t.Logf("  %s", s)
		}
	}
}

// TestNoLengthStandout: the spread guard bounds the whole set, but an item can
// satisfy it and still have one statement that visibly stands apart from its
// nearest rival, and that is the comparison a candidate actually makes. No
// statement may stand more than 15% clear of the one next to it in length; the
// floor lets small absolute differences through.
func TestNoLengthStandout(t *testing.T) {
	const ratio = 0.15
	floor := map[string]int{"en": 8, "tc": 3}
	var bad []string
	for _, q := range loadBank(t) {
		if q.Official != "" {
			continue
		}
		for _, lang := range []string{"en", "tc"} {
			ss := q.side(lang).Statements
			if len(ss) < 2 {
				continue
			}
			n := make([]int, len(ss))
			for i, s := range ss {
				n[i] = len([]rune(s))
			}
			sort.Ints(n)
			last := len(n) - 1
			if n[1]-n[0] > floor[lang] && float64(n[0]) < float64(n[1])*(1-ratio) {
				bad = append(bad, fmt.Sprintf("%s [%s]: the shortest statement stands apart", q.ID, lang))
			}
			if n[last]-n[last-1] > floor[lang] && float64(n[last]) > float64(n[last-1])*(1+ratio) {
				bad = append(bad, fmt.Sprintf("%s [%s]: the longest statement stands apart", q.ID, lang))
			}
		}
	}
	if len(bad) > 0 {
		t.Errorf("%d cases where one statement stands more than %.0f%% clear of its nearest rival", len(bad), ratio*100)
		for i, s := range bad {
			if i == 15 {
				t.Logf("... and %d more", len(bad)-15)
				break
			}
			t.Logf("  %s", s)
		}
	}
}

// TestNoAbsoluteTell: a September 2026 audit found the wording deciding the
// statements for the candidate: one carrying an absolute — "only", "never", "in
// every case", 只限, 一律, 無須 — was true just 33% of the time in English and
// 27% in Chinese, against a 76% base rate. Marking the absolutes false scored
// 68% where the rule discriminated, against 20% for chance. Distractors drift
// that way because overstating a true rule is the easiest way to falsify it; the
// repair is to make them wrong on substance and to put accurate absolutes on true
// statements. The check is statistical: one absolute on one false statement is
// noise, a bank-wide correlation is what a candidate can learn.
func TestNoAbsoluteTell(t *testing.T) {
	absolute := map[string]*regexp.Regexp{
		"en": regexp.MustCompile(`(?i)\b(only|solely|exclusively|alone|always|never|at all|whatsoever|need not|not required|no requirement|nothing more|no more than)\b|in (every|all) cases?`),
		"tc": regexp.MustCompile(`只|僅|一律|完全|絕不|永不|毫無|無須|毋須|不得`),
	}
	statTell(t, "an absolute qualifier", absolute, 0.60, 0.45, false)
}

// TestNoNegationTell: after the absolutes were repaired, statements containing
// a negation were true 59% of the time against a 76% base rate, and 23-40% in two
// modules: negating a true rule is the next easiest way to falsify it. Negate
// true statements too. In the old module 5 a negated statement was true only
// 3 times in 13 in English; migration must remove that tell as well as add notes.
func TestNoNegationTell(t *testing.T) {
	negation := map[string]*regexp.Regexp{
		"en": regexp.MustCompile(`(?i)\b(not|no|never|neither|nor|without|cannot)\b|n't\b`),
		"tc": regexp.MustCompile(`不|無|沒有|未|非|毋|毋須|不得`),
	}
	statTell(t, "a negation", negation, 0.50, 0.35, true)
}

// statTell checks that statements matching a pattern are true at a healthy rate
// bank-wide and in each module with enough of them.
func statTell(t *testing.T, what string, re map[string]*regexp.Regexp, floor, modFloor float64, annotatedOnly bool) {
	t.Helper()
	bank := loadBank(t)
	for _, lang := range []string{"en", "tc"} {
		var total, trueOnes int
		perTotal, perTrue := map[int]int{}, map[int]int{}
		for _, q := range bank {
			if annotatedOnly && !q.annotated() {
				continue
			}
			for i, s := range q.side(lang).Statements {
				if i >= q.n() || !re[lang].MatchString(s) {
					continue
				}
				total++
				perTotal[q.Module]++
				if q.Truth[i] {
					trueOnes++
					perTrue[q.Module]++
				}
			}
		}
		if total == 0 {
			continue
		}
		if share := float64(trueOnes) / float64(total); share < floor {
			t.Errorf("%s: a statement carrying %s is true in only %.0f%% of cases (%d of %d), want at least %.0f%%",
				lang, what, share*100, trueOnes, total, floor*100)
		}
		for m := 1; m <= 7; m++ {
			if perTotal[m] < 8 {
				continue // too few to read anything into
			}
			if share := float64(perTrue[m]) / float64(perTotal[m]); share < modFloor {
				t.Errorf("%s module %d: a statement carrying %s is true in only %.0f%% of cases (%d of %d), want at least %.0f%%",
					lang, m, what, share*100, perTrue[m], perTotal[m], modFloor*100)
			}
		}
	}
}

// The guards below hold a rule the bank's owner set in September 2026, after
// meeting m3-243 in a mock paper: "What is the relationship between section
// 3(1)(a) and section 3(2) of Schedule 2?" The thing the candidate has to supply
// is always substance — a rule, a condition, a consequence — never what a number
// says. That is also how C&ED's own sample questions read: every stem names its
// topic in words, and the section appears only in the answer key.

var (
	// a fine-grained citation: section, subsection, paragraph, division, item
	fineRef = regexp.MustCompile(`(?i)(\bsections?\s+\d+[A-Z]?(\(\d+[A-Z]?\))*(\([a-z]+\))*(\([ivx]+\))*|\bs\.\s*\d+[A-Z]?(\(\d+[A-Z]?\))*(\([a-z]+\))*|\bsubsections?\s+\(\d+[A-Z]?\)|\bparagraphs?\s+\(?\d+(\.\d+)*[a-z]?\)?(\([a-z]+\))*|¶\s*\d+(\.\d+)*(\([a-z]+\))*|\bitems?\s+\d+|\bDivision\s+\d|\bclauses?\s+\d+|\bfootnote\s+\d+)`)
	// the Chinese fine-grained citation
	tcFineRef = regexp.MustCompile(`第[\dA-Za-z().]+(條|款|段|分部)`)
)

// TestStemNamesTopic: C&ED's stems name a topic in words ("Regarding the
// requirements of local management office…") and never cite a section or
// paragraph; the citation belongs in the source line. An audit in September 2026
// found 89% of stems citing one.
func TestStemNamesTopic(t *testing.T) {
	for _, q := range loadBank(t) {
		if m := fineRef.FindString(q.En.Q); m != "" {
			t.Errorf("%s (en): the stem cites %q; name the topic in words", q.ID, m)
		}
		if m := tcFineRef.FindString(q.Tc.Q); m != "" {
			t.Errorf("%s (tc): the stem cites %q; name the topic in words", q.ID, m)
		}
	}
}

// TestNoNumberInterrogatives bans the sentence shapes that make a number the
// unknown: "What is the effect of section 5(1)?", "How do sections 4 and 15
// relate?". They are checked in statements as well as stems: a statement that
// says what a section number contains asks the same recall.
func TestNoNumberInterrogatives(t *testing.T) {
	const ref = `(?:section|s\.|subsection|paragraph|¶|division)s?\s*[\d(]`
	const tref = `第[\dA-Za-z().]+(?:條|款|段|分部)`
	patterns := map[string][]*regexp.Regexp{
		"en": {
			regexp.MustCompile(`(?i)\bwhat\s+(?:is|are|was)\s+(?:the\s+)?(?:basic\s+|general\s+|main\s+|overall\s+)?(?:effect|purpose|subject\s+matter|scope|gist|thrust|significance|relationship|division|structure)\s+(?:of|between)\s+(?:the\s+)?` + ref),
			regexp.MustCompile(`(?i)\bhow\s+(?:do|does|is|are)\s+(?:the\s+)?` + ref + `[^?]*\b(?:relate|differ|distinguish|interact|align|compare|structured|divided)`),
			regexp.MustCompile(`(?i)\brelationship\s+between\s+(?:the\s+)?` + ref),
		},
		"tc": {
			regexp.MustCompile(tref + `(?:與|及|和)` + tref + `(?:在[^？]{0,8})?(?:有何關係|的關係|如何分工|有何分別|如何互動|如何配合|如何相互)`),
			regexp.MustCompile(tref + `(?:的|之)(?:結構|主題|內容|基本效力|效力|目的|範圍)(?:為何|是甚麼|是什麼)`),
		},
	}
	for _, q := range loadBank(t) {
		for _, lang := range []string{"en", "tc"} {
			l := q.side(lang)
			for _, text := range append([]string{l.Q}, l.Statements...) {
				for _, re := range patterns[lang] {
					if m := re.FindString(text); m != "" {
						t.Errorf("%s (%s): asks what a numbered provision says (%q); state the rule and ask about it instead",
							q.ID, lang, m)
						break
					}
				}
			}
		}
	}
}

// TestComboExplanationNamesFalseStatements: a fixed item's explanation says
// which statements are false, or that none is, and that must be the answer the
// truth gives. An explanation that argues for a different set of statements is
// invisible until a candidate who chose correctly reads that they were wrong.
// Collect every "statement N is false", not just the first, and read "none of
// them is false" as all true.
func TestComboExplanationNamesFalseStatements(t *testing.T) {
	falseStatements := map[string]*regexp.Regexp{
		"en": regexp.MustCompile(`\b(?i:statements?)\s+(\d+(?:(?:\s*,\s*|\s+and\s+|\s*&\s*)(?:(?i:statement)\s+)?\d+)*)\s+(?:is|are)\s+(?:false|incorrect|wrong|untrue|not correct)`),
		"tc": regexp.MustCompile(`陳述\s*(\d+(?:\s*(?:、|及|和|與|,|，)\s*(?:陳述)?\s*\d+)*)\s*(?:均|皆|都|亦)?\s*(?:不正確|錯誤|並不正確|屬錯誤|有誤|不準確)`),
	}
	noneFalse := map[string]*regexp.Regexp{
		"en": regexp.MustCompile(`none of them is false|(?i:no) statement is false|(?i:all) (?:four|five|the) statements (?:are|is) (?:correct|true)|(?i:every) statement is (?:correct|true)|(?i:none) of the (?:four |five )?statements (?:is|are) (?:false|incorrect)`),
		"tc": regexp.MustCompile(`(?:四|五)項陳述(?:均|全部|皆)(?:正確|屬實)|所有陳述(?:均|皆)正確|全部陳述(?:均|皆)?正確|各項陳述(?:均|皆)正確|(?:沒有|並無)不正確的陳述|陳述1、2、3\s*及\s*4\s*均正確|陳述1、2、3、4\s*及\s*5\s*均正確`),
	}
	digits := regexp.MustCompile(`\d+`)
	for _, q := range loadBank(t) {
		if !q.Fixed || q.annotated() {
			continue
		}
		var want []string
		for i, v := range q.Truth {
			if !v {
				want = append(want, strconv.Itoa(i+1))
			}
		}
		for _, lang := range []string{"en", "tc"} {
			explain := q.side(lang).Explain
			named := map[int]bool{}
			for _, m := range falseStatements[lang].FindAllStringSubmatch(explain, -1) {
				for _, d := range digits.FindAllString(m[1], -1) {
					n, _ := strconv.Atoi(d)
					named[n] = true
				}
			}
			var got []string
			for n := 1; n <= q.n(); n++ {
				if named[n] {
					got = append(got, strconv.Itoa(n))
				}
			}
			switch none := noneFalse[lang].MatchString(explain); {
			case len(got) == 0 && !none:
				t.Errorf("%s (%s): the explanation does not say which statements are false", q.ID, lang)
			case len(got) > 0 && none:
				t.Errorf("%s (%s): the explanation says both that statements %s are false and that none is", q.ID, lang, strings.Join(got, ", "))
			case strings.Join(got, ",") != strings.Join(want, ","):
				t.Errorf("%s (%s): the explanation calls statements [%s] false, but the truth makes [%s] false",
					q.ID, lang, strings.Join(got, ","), strings.Join(want, ","))
			}
		}
	}
}
