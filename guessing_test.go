package main

import (
	"math"
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
// that points at the key. The length, absolutes and punctuation guards in
// questions_test.go each close one such feature; these add two more that the
// item-writing literature names, and then let a model learn from the bank
// itself whatever combination of features still points at the key.

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

// uniqueMax is the index of the largest value, or -1 when it is tied.
func uniqueMax(vals []float64) int {
	best, at := math.Inf(-1), -1
	for i, v := range vals {
		switch {
		case v > best:
			best, at = v, i
		case v == best:
			at = -1
		}
	}
	return at
}

// keyMaxShare runs one "the key is the option with the most X" test over the
// four-option items: bank-wide the share may not exceed chance by more than
// two standard errors, and within a module by more than three (the bank
// deliberately has seven modules, so seven looser checks rather than a tight one).
func keyMaxShare(t *testing.T, name string, score func(q question, lang string) []float64) {
	bank := loadBank(t)
	for _, lang := range []string{"en", "tc"} {
		hits, n := 0, 0
		perHits, perN := map[int]int{}, map[int]int{}
		for _, q := range bank {
			if q.combo() {
				continue
			}
			n++
			perN[q.Module]++
			if uniqueMax(score(q, lang)) == q.Answer {
				hits++
				perHits[q.Module]++
			}
		}
		check := func(where string, h, n int, k float64) {
			p := 0.25
			limit := p + k*math.Sqrt(p*(1-p)/float64(n))
			if share := float64(h) / float64(n); share > limit {
				t.Errorf("%s%s: the key is the option with the most %s in %d of %d items (%.1f%%), above the %.1f%% limit (chance 25%%)",
					lang, where, name, h, n, share*100, limit*100)
			}
		}
		check("", hits, n, 2)
		for m := 1; m <= 7; m++ {
			if perN[m] >= 40 {
				check(" module "+strconv.Itoa(m), perHits[m], perN[m], 3)
			}
		}
		t.Logf("%s: key has the most %s in %.1f%% of %d four-option items", lang, name, 100*float64(hits)/float64(n), n)
	}
}

func optionTexts(q question, lang string) []string {
	if lang == "tc" {
		return q.Tc.Options
	}
	return q.En.Options
}

// TestNoConvergenceTell: when distractors are written by varying the key (a
// different body here, a different deadline there), the key ends up as the
// option that has most in common with all the others, and test-takers learn to
// pick it (Smith 1982; the NBME Item-Writing Guide calls it convergence). When
// measured in September 2026 the key was the most convergent option in 21.6%
// of English items and 24.1% of Chinese ones, against 25% for chance.
func TestNoConvergenceTell(t *testing.T) {
	keyMaxShare(t, "in common with the other options", func(q question, lang string) []float64 {
		opts := optionTexts(q, lang)
		toks := make([]map[string]bool, len(opts))
		for i, o := range opts {
			toks[i] = overlapTokens(o, lang)
		}
		conv := make([]float64, len(opts))
		for i := range opts {
			for j := range opts {
				if i != j {
					conv[i] += jaccard(toks[i], toks[j]) / float64(len(opts)-1)
				}
			}
		}
		return conv
	})
}

// TestNoEchoTell: an option that repeats the stem's words reads as the answer
// ("clang" in the NBME guide), and blind reviewers in September 2026 flagged
// keys that alone echoed the stem or its deciding facts. The measure is the
// share of an option's words that also appear in the stem; when first
// measured the key had the highest share in 22.6% of English items and 25.4%
// of Chinese ones.
func TestNoEchoTell(t *testing.T) {
	keyMaxShare(t, "words from the stem", func(q question, lang string) []float64 {
		stem := q.En.Q
		if lang == "tc" {
			stem = q.Tc.Q
		}
		st := overlapTokens(stem, lang)
		opts := optionTexts(q, lang)
		echo := make([]float64, len(opts))
		for i, o := range opts {
			ot := overlapTokens(o, lang)
			shared := 0
			for w := range ot {
				if st[w] {
					shared++
				}
			}
			if len(ot) > 0 {
				echo[i] = float64(shared) / float64(len(ot))
			}
		}
		return echo
	})
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

// surfaceFeatures describes each text of one item (its options, or its
// statements) relative to the others: length and how it stands against its
// neighbours, how much it shares with the rest, and the word-level cues.
func surfaceFeatures(texts []string, lang string) [][]float64 {
	n := len(texts)
	ls := make([]float64, n)
	toks := make([]map[string]bool, n)
	for i, s := range texts {
		ls[i] = float64(utf8.RuneCountInString(s))
		toks[i] = overlapTokens(s, lang)
	}
	conv := make([]float64, n)
	for i := range texts {
		for j := range texts {
			if i != j {
				conv[i] += jaccard(toks[i], toks[j]) / float64(n-1)
			}
		}
	}
	lm, lsd := meanSD(ls)
	cm, csd := meanSD(conv)
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
	best, tied, keyTop := math.Inf(-1), 0, false
	for k, row := range it.x {
		s := 0.0
		for j, v := range row {
			s += w[j] * v
		}
		switch {
		case s > best+1e-12:
			best, tied, keyTop = s, 1, k == it.key
		case math.Abs(s-best) <= 1e-12:
			tied++
			keyTop = keyTop || k == it.key
		}
	}
	if keyTop {
		return 1 / float64(tied)
	}
	return 0
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

// TestOptionsOnlyGuesser is the test-wise candidate, automated. It never sees
// a stem or a source: only the options of a four-option item, or the
// statements of a combination item. It learns, from the bank itself, which
// surface features point at keys (the whole set of cues the guards above look
// at one by one, weighted as the bank rewards them), is scored only on
// items it was not trained on, and then sits 4,000 simulated papers under the
// app's own pass rule.
//
// When this was first run, in September 2026, it picked 43% of four-option
// keys in English and 46% in Chinese (chance 25%), and 32% and 39% of
// combination keys (chance 20%), almost all of it through the absolutes and
// hedges that the owner decided on 27 September 2026 not to chase. It still
// passed about one simulated paper in 2,500. The bounds hold that line: a new
// tell big enough to matter, like the old key-is-longest pattern that passed
// 64% of simulated papers, fails the build.
func TestOptionsOnlyGuesser(t *testing.T) {
	bank := loadBank(t)
	perModule, passTotal, maxWrong := passRule(t)
	trueSets := map[int][][]int{
		4: {{0, 1, 2}, {0, 1, 3}, {1, 2, 3}, {0, 2, 3}, {0, 1, 2, 3}},
		5: {{0, 1, 2}, {1, 2, 3}, {0, 2, 3}, {0, 1, 4}, {2, 3, 4}},
	}
	for _, lang := range []string{"en", "tc"} {
		var singles, combos []guessItem
		for _, q := range bank {
			l := q.En
			if lang == "tc" {
				l = q.Tc
			}
			if !q.combo() {
				singles = append(singles, guessItem{q.ID, q.Module, surfaceFeatures(l.Options, lang), q.Answer})
				continue
			}
			// A statement's features, plus which position it is in. A printed option
			// is scored by the statements it leaves out, the ones it calls false.
			st := surfaceFeatures(l.Statements, lang)
			for i := range st {
				pos := make([]float64, 5)
				pos[i] = 1
				st[i] = append(st[i], pos...)
			}
			var x [][]float64
			for _, set := range trueSets[len(st)] {
				row := make([]float64, len(st[0]))
				for i := range st {
					if !contains(set, i) {
						for j, v := range st[i] {
							row[j] += v
						}
					}
				}
				x = append(x, row)
			}
			combos = append(combos, guessItem{q.ID, q.Module, x, q.Answer})
		}
		right := crossValidate(singles)
		for id, p := range crossValidate(combos) {
			right[id] = p
		}
		accuracy := func(items []guessItem) float64 {
			s := 0.0
			for _, it := range items {
				s += right[it.id]
			}
			return s / float64(len(items))
		}
		single, combo := accuracy(singles), accuracy(combos)
		t.Logf("%s: options-only guesser picks %.1f%% of four-option keys (chance 25%%) and %.1f%% of combination keys (chance 20%%)",
			lang, single*100, combo*100)
		if single > 0.50 {
			t.Errorf("%s: an options-only guesser picks %.1f%% of four-option keys, above the 50%% bound", lang, single*100)
		}
		if combo > 0.45 {
			t.Errorf("%s: an options-only guesser picks %.1f%% of combination keys, above the 45%% bound", lang, combo*100)
		}

		for _, mode := range []string{"mixed", "combination"} {
			pools := map[int][]question{}
			for _, q := range bank {
				if mode == "mixed" || q.combo() {
					pools[q.Module] = append(pools[q.Module], q)
				}
			}
			rng := rand.New(rand.NewPCG(2026, 928))
			const papers = 4000
			passed, total := 0, 0
			for p := 0; p < papers; p++ {
				score, ok := 0, true
				for m := 1; m <= 7; m++ {
					pool := pools[m]
					wrong := 0
					for _, i := range rng.Perm(len(pool))[:perModule] {
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
			t.Logf("%s, %s papers: mean %.1f of %d, %d of %d passed", lang, mode, float64(total)/papers, 7*perModule, passed, papers)
			if rate > 0.005 {
				t.Errorf("%s: an options-only guesser passes %.2f%% of %s papers, above 0.5%%", lang, rate*100, mode)
			}
		}
	}
}

func contains(xs []int, x int) bool {
	for _, v := range xs {
		if v == x {
			return true
		}
	}
	return false
}
