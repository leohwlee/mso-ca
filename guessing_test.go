package main

import (
	"math"
	"math/bits"
	"math/rand/v2"
	"regexp"
	"strconv"
	"strings"
	"testing"
	"unicode"
	"unicode/utf8"
)

// The checks in this file look at the bank the way a test-wise candidate does:
// without the source, and often without the question, for any surface feature
// that points at the key. The length, absolute and negation guards in
// questions_test.go each close one such feature; these look at the structure of
// the option sets, and then let a model learn from the bank itself whatever
// combination of features still points at the key.

var overlapStop = map[string]bool{}

func init() {
	for _, w := range strings.Fields(`the a an of to and or in on for by with is are be been being that this these
		those which its it as at from any must should may not no has have had if into than then there their them they
		such each other who whom whose what when where under within without about only also can could would will
		shall do does did so all`) {
		overlapStop[w] = true
	}
}

var overlapWord = regexp.MustCompile(`[a-z0-9$%]+`)

// overlapTokens are the units two texts can share: content words for English,
// and character pairs for Chinese, which has no spaces to find words by.
func overlapTokens(s, lang string) map[string]bool {
	out := map[string]bool{}
	if lang == "en" {
		for _, w := range overlapWord.FindAllString(strings.ToLower(s), -1) {
			if len(w) > 1 && !overlapStop[w] {
				out[w] = true
			}
		}
		return out
	}
	var han []rune
	for _, r := range s {
		if unicode.Is(unicode.Han, r) {
			han = append(han, r)
		}
	}
	for i := 0; i+1 < len(han); i++ {
		out[string(han[i:i+2])] = true
	}
	return out
}

// claimsMask is what each of an item's options says is true, as bit masks.
func claimsMask(q question) []uint {
	out := make([]uint, len(q.Options))
	for i, o := range q.Options {
		out[i] = o.claims(q.n())
	}
	return out
}

// pickShare is the chance that a strategy scoring the options this way picks
// the key: 1 split among the options tied for the highest score.
func pickShare(scores []float64, key int) float64 {
	best := math.Inf(-1)
	for _, s := range scores {
		best = math.Max(best, s)
	}
	tied, hit := 0, false
	for i, s := range scores {
		if s == best {
			tied++
			hit = hit || i == key
		}
	}
	if !hit {
		return 0
	}
	return 1 / float64(tied)
}

// structure scores an item's options by features of the option set alone:
// how popular an option's statements are across the options, how much it shares
// with the others, and its size. These are the readings of an option set that
// test-wise candidates are taught; bank/combo.py builds the sets so that none of
// them singles out the key.
func structure(q question) map[string][]float64 {
	n := q.n()
	m := claimsMask(q)
	freq := make([]float64, n)
	for i, o := range q.Options {
		if o.Token == "" {
			for b := 0; b < n; b++ {
				if m[i]&(1<<b) != 0 {
					freq[b]++
				}
			}
		}
	}
	out := map[string][]float64{"popular": {}, "convergent": {}, "largest": {}, "smallest": {}, "modal size": {}, "last": {}}
	sizes := map[int]int{}
	for _, o := range q.Options {
		if o.Token == "" {
			sizes[len(o.Set)]++
		}
	}
	modal, top := 0, 0
	for s, c := range sizes {
		if c > top || (c == top && s > modal) {
			modal, top = s, c
		}
	}
	for i, o := range q.Options {
		pop, size := -1.0, float64(bits.OnesCount(m[i]))
		if o.Token == "" {
			pop = 0
			for b := 0; b < n; b++ {
				if m[i]&(1<<b) != 0 {
					pop += freq[b]
				}
			}
			pop /= size
		}
		conv := 0.0
		for j := range q.Options {
			if j != i {
				if u := bits.OnesCount(m[i] | m[j]); u > 0 {
					conv += float64(bits.OnesCount(m[i]&m[j])) / float64(u)
				}
			}
		}
		isSet := o.Token == ""
		out["popular"] = append(out["popular"], pop)
		out["convergent"] = append(out["convergent"], conv)
		out["largest"] = append(out["largest"], map[bool]float64{true: size, false: -1}[isSet])
		out["smallest"] = append(out["smallest"], map[bool]float64{true: -size, false: -99}[isSet])
		out["modal size"] = append(out["modal size"], boolf(isSet && len(o.Set) == modal))
		out["last"] = append(out["last"], boolf(i == len(q.Options)-1))
	}
	return out
}

// TestNoStructureTell: a strategy that reads only the shape of the option set
// may not find the key more often than chance (one in five) by more than two
// standard errors, bank-wide. "last" is always picking e), All of the above,
// which is right exactly as often as every statement is true.
func TestNoStructureTell(t *testing.T) {
	bank := loadBank(t)
	hits := map[string]float64{}
	for _, q := range bank {
		if len(q.Options) != 5 {
			continue
		}
		for name, scores := range structure(q) {
			hits[name] += pickShare(scores, q.Answer)
		}
	}
	n := float64(len(bank))
	limit := 0.2 + 2*math.Sqrt(0.2*0.8/n)
	for name, h := range hits {
		share := h / n
		t.Logf("picking the %s option finds the key in %.1f%% of items", name, share*100)
		lim := limit
		if name == "last" {
			lim = 0.30 // the all-true share, which TestTruthCounts bounds for new items
		}
		if share > lim {
			t.Errorf("picking the %s option finds the key in %.1f%% of %d items, above %.1f%% (chance 20%%)",
				name, share*100, len(bank), lim*100)
		}
	}
}

// surfaceCues are word-level features a candidate can see without knowing
// anything: hedges, absolutes, sums of money, parentheses, negations, digits.
var surfaceCues = map[string][]*regexp.Regexp{
	"en": {
		regexp.MustCompile(`(?i)\b(reasonabl[ey]|appropriate(ly)?|generally|normally|usually|where (applicable|appropriate|necessary)|as soon as (reasonably )?practicable|adequate(ly)?|sufficient(ly)?|commensurate|proportionate|suitabl[ey]|may)\b`),
		regexp.MustCompile(`(?i)\b(only|solely|exclusively|alone|always|never|at all|whatsoever|need not|not required|no requirement|automatically|in (all|every) cases?|regardless|without exception|under no circumstances)\b`),
		regexp.MustCompile(`(\$|HK\$)\s?\d`),
		regexp.MustCompile(`\(`),
		regexp.MustCompile(`(?i)\b(not|no|never|neither|nor|without)\b`),
		regexp.MustCompile(`\d`),
	},
	"tc": {
		regexp.MustCompile(`合理|適當|一般|通常|可能|相稱|足夠|充分|切實可行|視乎|有需要|可`),
		regexp.MustCompile(`只|僅|一律|完全|絕不|永不|毫無|無須|毋須|自動|無論|不論|任何情況|概不`),
		regexp.MustCompile(`(\$|港元)\s?\d|\d[\d,]*元`),
		regexp.MustCompile(`[（(]`),
		regexp.MustCompile(`不|無|沒有|未|非|毋`),
		regexp.MustCompile(`\d`),
	},
}

func meanSD(xs []float64) (float64, float64) {
	var m, v float64
	for _, x := range xs {
		m += x
	}
	m /= float64(len(xs))
	for _, x := range xs {
		v += (x - m) * (x - m)
	}
	sd := math.Sqrt(v / float64(len(xs)))
	if sd == 0 {
		sd = 1
	}
	return m, sd
}

func boolf(b bool) float64 {
	if b {
		return 1
	}
	return 0
}

// statementFeatures describes each statement of one item relative to the
// others: length and how it stands against its neighbours, how much it shares
// with the rest and with the stem, and the word-level cues.
func statementFeatures(texts []string, stem, lang string) [][]float64 {
	n := len(texts)
	ls := make([]float64, n)
	toks := make([]map[string]bool, n)
	for i, s := range texts {
		ls[i] = float64(utf8.RuneCountInString(s))
		toks[i] = overlapTokens(s, lang)
	}
	st := overlapTokens(stem, lang)
	conv := make([]float64, n)
	echo := make([]float64, n)
	for i := range texts {
		for j := range texts {
			if i != j {
				conv[i] += jaccard(toks[i], toks[j]) / float64(n-1)
			}
		}
		shared := 0
		for w := range toks[i] {
			if st[w] {
				shared++
			}
		}
		if len(toks[i]) > 0 {
			echo[i] = float64(shared) / float64(len(toks[i]))
		}
	}
	lm, lsd := meanSD(ls)
	cm, csd := meanSD(conv)
	em, esd := meanSD(echo)
	out := make([][]float64, n)
	for i, s := range texts {
		longest, shortest := true, true
		below, above := 0.0, math.Inf(1)
		for j, l := range ls {
			if j == i {
				continue
			}
			if l >= ls[i] {
				longest = false
				above = min(above, l)
			}
			if l <= ls[i] {
				shortest = false
				below = max(below, l)
			}
		}
		f := []float64{
			(ls[i] - lm) / lsd,
			boolf(longest), boolf(shortest),
			boolf(longest && ls[i] > below*1.15),
			boolf(shortest && ls[i]*1.15 < above),
			(conv[i] - cm) / csd,
			(echo[i] - em) / esd,
		}
		for _, re := range surfaceCues[lang] {
			f = append(f, boolf(re.MatchString(s)))
		}
		out[i] = f
	}
	return out
}

type guessItem struct {
	id     string
	module int
	x      [][]float64 // one row per option
	key    int
}

// optionRows scores each option by the statements it calls false, the ones it
// leaves out, plus the structure of the option set.
func optionRows(q question, lang string) [][]float64 {
	l := q.side(lang)
	st := statementFeatures(l.Statements, l.Q, lang)
	sf := structure(q)
	m := claimsMask(q)
	var rows [][]float64
	for i := range q.Options {
		row := make([]float64, len(st[0]))
		for b := 0; b < q.n(); b++ {
			if m[i]&(1<<b) == 0 {
				for j, v := range st[b] {
					row[j] += v
				}
			}
		}
		row = append(row, float64(bits.OnesCount(m[i]))/float64(q.n()),
			sf["popular"][i], sf["convergent"][i], sf["modal size"][i], sf["last"][i])
		rows = append(rows, row)
	}
	return rows
}

// fitGuesser fits a conditional logit: the chance of picking an option grows
// with a weighted sum of its features, and the weights are those that best
// pick the keys of the training items.
func fitGuesser(items []guessItem) []float64 {
	d := len(items[0].x[0])
	w := make([]float64, d)
	g := make([]float64, d)
	for iter := 0; iter < 300; iter++ {
		clear(g)
		for _, it := range items {
			s := make([]float64, len(it.x))
			mx := math.Inf(-1)
			for k, row := range it.x {
				for j, v := range row {
					s[k] += w[j] * v
				}
				mx = max(mx, s[k])
			}
			z := 0.0
			for k := range s {
				s[k] = math.Exp(s[k] - mx)
				z += s[k]
			}
			for j := range g {
				g[j] += it.x[it.key][j]
				for k := range s {
					g[j] -= s[k] / z * it.x[k][j]
				}
			}
		}
		for j := range w {
			w[j] += 0.2 * (g[j]/float64(len(items)) - 0.01*w[j])
		}
	}
	return w
}

// guessRight is the chance the guesser's pick is the key: 1 or 0, split on ties.
func guessRight(w []float64, it guessItem) float64 {
	scores := make([]float64, len(it.x))
	for k, row := range it.x {
		for j, v := range row {
			scores[k] += w[j] * v
		}
		scores[k] = math.Round(scores[k]*1e9) / 1e9
	}
	return pickShare(scores, it.key)
}

// crossValidate scores every item with a guesser that never saw it.
func crossValidate(items []guessItem) map[string]float64 {
	const folds = 10
	out := map[string]float64{}
	for f := 0; f < folds; f++ {
		var train []guessItem
		for i, it := range items {
			if i%folds != f {
				train = append(train, it)
			}
		}
		w := fitGuesser(train)
		for i, it := range items {
			if i%folds == f {
				out[it.id] = guessRight(w, it)
			}
		}
	}
	return out
}

// passRule reads the paper's shape and pass mark from the app itself, so the
// simulation below always uses the rule a candidate sits.
func passRule(t *testing.T) (perModule, passTotal, maxWrong int) {
	t.Helper()
	src, err := webFS.ReadFile("web/app.js")
	if err != nil {
		t.Fatal(err)
	}
	get := func(name string) int {
		m := regexp.MustCompile(name + `:\s*(\d+)`).FindSubmatch(src)
		if m == nil {
			t.Fatalf("web/app.js: no %s in CFG", name)
		}
		n, _ := strconv.Atoi(string(m[1]))
		return n
	}
	return get("perModule"), get("passTotal"), get("maxWrongPerModule")
}

// TestOptionsOnlyGuesser is the test-wise candidate, automated. It never sees a
// source: only the statements and the option set of each item. It learns, from
// the bank itself, which surface features point at keys (the whole set of cues
// the guards look at one by one, weighted as the bank rewards them), is scored
// only on items it was not trained on, and then sits 4,000 simulated papers
// under the app's own pass rule.
//
// When this was first run on combination items, in September 2026, it picked
// 32% of keys in English and 39% in Chinese (chance 20%), almost all of it
// through the absolutes and hedges the owner decided on 27 September 2026 not
// to chase, and passed about one simulated paper in 2,500. The bounds hold that
// line: a new tell big enough to matter fails the build.
func TestOptionsOnlyGuesser(t *testing.T) {
	bank := loadBank(t)
	perModule, passTotal, maxWrong := passRule(t)
	for _, lang := range []string{"en", "tc"} {
		var items []guessItem
		for _, q := range bank {
			if len(q.Options) == 5 && len(q.side(lang).Statements) == q.n() {
				items = append(items, guessItem{q.ID, q.Module, optionRows(q, lang), q.Answer})
			}
		}
		right := crossValidate(items)
		acc := 0.0
		for _, it := range items {
			acc += right[it.id]
		}
		acc /= float64(len(items))
		t.Logf("%s: an options-only guesser picks %.1f%% of keys (chance 20%%)", lang, acc*100)
		if acc > 0.45 {
			t.Errorf("%s: an options-only guesser picks %.1f%% of keys, above the 45%% bound", lang, acc*100)
		}

		pools := map[int][]question{}
		for _, q := range bank {
			pools[q.Module] = append(pools[q.Module], q)
		}
		rng := rand.New(rand.NewPCG(2026, 928))
		const papers = 4000
		passed, total := 0, 0
		for p := 0; p < papers; p++ {
			score, ok := 0, true
			for m := 1; m <= 7; m++ {
				pool := pools[m]
				wrong := 0
				for _, i := range rng.Perm(len(pool))[:min(perModule, len(pool))] {
					if rng.Float64() < right[pool[i].ID] {
						score++
					} else {
						wrong++
					}
				}
				ok = ok && wrong <= maxWrong
			}
			total += score
			if ok && score >= passTotal {
				passed++
			}
		}
		rate := float64(passed) / papers
		t.Logf("%s papers: mean %.1f of %d, %d of %d passed", lang, float64(total)/papers, 7*perModule, passed, papers)
		if rate > 0.005 {
			t.Errorf("%s: an options-only guesser passes %.2f%% of papers, above 0.5%%", lang, rate*100)
		}
	}
}
