package main

import (
	"bytes"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"os"
	"path/filepath"
	"regexp"
	"slices"
	"strings"
	"testing"
	"unicode"
)

// The checks in this file tie the bank to the documents it is written from.
// docs/text holds the text of every document in docs/EN and docs/TC, extracted
// by docs/extract_text.py; docs/quotes.json holds, for every question and each
// language, the passage of a cited document that decides its key.

// docPatterns say which of the numbered documents in docs/ a citation names.
// Each language has its own, because each citation field follows its own
// language's conventions: "AMLO s.13(9)" and 《打擊洗錢條例》第13(9)條.
// A citation may name several documents. A section number with no document
// name is the Ordinance's, which is how the bank cites it.
var docPatterns = map[string][]struct {
	num string
	re  *regexp.Regexp
}{
	"en": {
		{"01", regexp.MustCompile(`Guidance Notes`)},
		{"02", regexp.MustCompile(`AML/CFT Guideline|Guideline for MSOs|\bGlossary\b`)},
		{"03", regexp.MustCompile(`Licensing Guide`)},
		{"04", regexp.MustCompile(`(?:^|[^y] )F&P Guideline|Criteria for Determining Fitness`)},
		{"05", regexp.MustCompile(`Supplementary (?:F&P|Guideline on Fitness)`)},
		{"06", regexp.MustCompile(`Business Plan`)},
		{"07", regexp.MustCompile(`AML/CFT Policy`)},
		{"08", regexp.MustCompile(`Pecuniary Penalty`)},
		{"09", regexp.MustCompile(`Disciplinary Fining`)},
		{"10", regexp.MustCompile(`AMLO|Cap\. ?615|(?:^|[\s;(,])ss?\.\s?\d|Sch(?:\.|edule) ?\d|\bPart \d`)},
		{"11", regexp.MustCompile(`MIS_06/2018`)},
		{"12", regexp.MustCompile(`MIS_05/2021`)},
		{"13", regexp.MustCompile(`MIS_03/2023`)},
		{"14", regexp.MustCompile(`MIS_01/2024`)},
		{"15", regexp.MustCompile(`MIS_01/2025`)},
		{"16", regexp.MustCompile(`MIS_02/2025`)},
		{"17", regexp.MustCompile(`MIS_03/2025`)},
		{"18", regexp.MustCompile(`MIS_04/2025`)},
		{"19", regexp.MustCompile(`MIS_01/2026`)},
		{"20", regexp.MustCompile(`FATF_02/2026`)},
		{"21", regexp.MustCompile(`FATF_03/2026`)},
		{"22", regexp.MustCompile(`\bFAQ\b`)},
		{"23", regexp.MustCompile(`CA_01/2021|Sample Questions`)},
	},
	"tc": {
		{"01", regexp.MustCompile(`能力評核須知`)},
		{"02", regexp.MustCompile(`《打擊洗錢及恐怖分子資金籌集指引》`)},
		{"03", regexp.MustCompile(`《牌照指引》`)},
		{"04", regexp.MustCompile(`《有關適當人選準則的指引》`)},
		{"05", regexp.MustCompile(`補充指引》`)},
		{"06", regexp.MustCompile(`《遞交業務計劃的指引》`)},
		{"07", regexp.MustCompile(`《遞交打擊洗錢及恐怖分子資金籌集政策的指引》`)},
		{"08", regexp.MustCompile(`《施加罰款紀律行動指引》`)},
		{"09", regexp.MustCompile(`《紀律處分罰款指引》`)},
		{"10", regexp.MustCompile(`《打擊洗錢條例》|第615章|附表\d|第\d+[A-Z]*(?:\([0-9A-Za-z]+\))*條`)},
		{"11", regexp.MustCompile(`MIS_06/2018`)},
		{"12", regexp.MustCompile(`MIS_05/2021`)},
		{"13", regexp.MustCompile(`MIS_03/2023`)},
		{"14", regexp.MustCompile(`MIS_01/2024`)},
		{"15", regexp.MustCompile(`MIS_01/2025`)},
		{"16", regexp.MustCompile(`MIS_02/2025`)},
		{"17", regexp.MustCompile(`MIS_03/2025`)},
		{"18", regexp.MustCompile(`MIS_04/2025`)},
		{"19", regexp.MustCompile(`MIS_01/2026`)},
		{"20", regexp.MustCompile(`FATF_02/2026`)},
		{"21", regexp.MustCompile(`FATF_03/2026`)},
		{"22", regexp.MustCompile(`常見問題`)},
		{"23", regexp.MustCompile(`CA_01/2021|參考試題`)},
	},
}

func citedDocs(citation, lang string) []string {
	var nums []string
	for _, p := range docPatterns[lang] {
		if p.re.MatchString(citation) {
			nums = append(nums, p.num)
		}
	}
	return nums
}

// matchKey is how a quote is compared with a source text: whitespace, quote
// marks and dashes are dropped, full-width forms folded to ASCII, and case
// folded. The PDF extracts break lines and hyphenate wherever the printed page
// did, and nobody types quote marks the same way twice; none of that changes
// the words. docs/extract_text.py already maps the look-alike CJK
// compatibility ideographs some Chinese PDFs use (行 as U+FA08) to the standard
// characters.
func matchKey(s string) string {
	const drop = "\u201c\u201d\u2018\u2019\"'\u300c\u300d\u300e\u300f\uff02\uff07" + // quote marks
		"\u2014\u2013\u2011\u2010\u2012\u2015-\u00ad\uff0d" // dashes and hyphens
	var b strings.Builder
	b.Grow(len(s))
	for _, r := range s {
		if unicode.IsSpace(r) || strings.ContainsRune(drop, r) || unicode.Is(unicode.Co, r) {
			continue
		}
		if r >= 0xFF01 && r <= 0xFF5E {
			r -= 0xFEE0
		}
		b.WriteRune(unicode.ToLower(r))
	}
	return b.String()
}

var sourceTexts = map[string]string{}

// sourceText returns a document's extracted text as matchKey sees it.
func sourceText(t *testing.T, lang, num string) string {
	t.Helper()
	key := lang + "/" + num
	if s, ok := sourceTexts[key]; ok {
		return s
	}
	b, err := os.ReadFile(filepath.Join("docs", "text", strings.ToUpper(lang), num+".txt"))
	if err != nil {
		t.Fatalf("read the text of document %s: %v (run python docs/extract_text.py)", key, err)
	}
	sourceTexts[key] = matchKey(string(b))
	return sourceTexts[key]
}

var bracketedHan = regexp.MustCompile(`\([\p{Han}、，]+\)`)

type quote struct {
	Doc  string `json:"doc"`
	Text string `json:"text"`
}

func loadQuotes(t *testing.T) map[string]map[string]quote {
	t.Helper()
	b, err := os.ReadFile(filepath.Join("docs", "quotes.json"))
	if err != nil {
		t.Fatalf("read docs/quotes.json: %v", err)
	}
	var qs map[string]map[string]quote
	if err := json.Unmarshal(b, &qs); err != nil {
		t.Fatalf("parse docs/quotes.json: %v", err)
	}
	return qs
}

// TestSourceTextsCurrent: every document in docs/EN and docs/TC has its
// extracted text in docs/text, taken from the file that is there now. A
// document replaced without running docs/extract_text.py again would leave the
// quote check comparing the bank with the old edition, which is the mistake
// that let superseded circulars stay in the bank until September 2026.
func TestSourceTextsCurrent(t *testing.T) {
	b, err := os.ReadFile(filepath.Join("docs", "text", "manifest.json"))
	if err != nil {
		t.Fatalf("read docs/text/manifest.json: %v", err)
	}
	var manifest map[string]struct {
		Source string `json:"source"`
		SHA256 string `json:"sha256"`
	}
	if err := json.Unmarshal(b, &manifest); err != nil {
		t.Fatalf("parse docs/text/manifest.json: %v", err)
	}
	seen := map[string]bool{}
	for _, lang := range []string{"EN", "TC"} {
		entries, err := os.ReadDir(filepath.Join("docs", lang))
		if err != nil {
			t.Fatal(err)
		}
		for _, e := range entries {
			name := e.Name()
			if len(name) < 3 || name[2] != '_' || name[0] < '0' || name[0] > '9' {
				continue
			}
			key := lang + "/" + name[:2] + ".txt"
			seen[key] = true
			m, ok := manifest[key]
			if !ok || m.Source != name {
				t.Errorf("docs/%s/%s has no extracted text (run python docs/extract_text.py)", lang, name)
				continue
			}
			src, err := os.ReadFile(filepath.Join("docs", lang, name))
			if err != nil {
				t.Fatal(err)
			}
			// Line endings are folded first: git checks the FAQ page, a text file, out
			// with CRLF on Windows and LF elsewhere.
			src = bytes.ReplaceAll(src, []byte("\r\n"), []byte("\n"))
			if sum := sha256.Sum256(src); hex.EncodeToString(sum[:]) != m.SHA256 {
				t.Errorf("docs/%s/%s has changed since its text was extracted (run python docs/extract_text.py)", lang, name)
			}
			if fi, err := os.Stat(filepath.Join("docs", "text", key)); err != nil || fi.Size() == 0 {
				t.Errorf("docs/text/%s is missing or empty", key)
			}
		}
	}
	for key := range manifest {
		if !seen[key] {
			t.Errorf("docs/text/%s comes from a document no longer in docs/", key)
		}
	}
}

// TestQuotesFromCitedSources: every question stores, in each language, the
// passage that decides its key, copied verbatim from a document its citation
// names. Until September 2026 the bank stored no such passage, so every blind
// review had to find the deciding words again from the citation alone; storing
// them makes grounding a mechanical check, and a quote that stops matching
// flags a source that has been edited or re-extracted since the question was
// written. The English quote comes from the English text and the Chinese from
// the Chinese, because each language follows its own edition.
//
// What this cannot see: a quote that is verbatim but decides nothing. Penalty
// wording such as "a fine at level 6 and to imprisonment for 6 months" recurs
// across the Ordinance, so the citation, not the quote, says which section is
// meant. Most quotes were recovered from the answer files of earlier blind
// reviews, and a random sample of 120 in September 2026 found every one from
// the right passage but 24 (20%) stopping short of the deciding words: the
// lead-in to a list, or the passage behind a true statement of a combination
// item. A sweep then re-read the 1,230 quotes a mechanical filter could not
// clear and replaced all but two of the 573 it found short or wrong; a fresh
// random sample of 60 afterwards found 2 more (3%), since replaced. Of the two
// kept, one decides its key after all; the other belongs to one of a handful of
// keys that rest on two passages pages apart, which a quote of one passage can
// only half carry. Blind review still checks that the key follows from the
// passage.
func TestQuotesFromCitedSources(t *testing.T) {
	bank := loadBank(t)
	quotes := loadQuotes(t)
	han := regexp.MustCompile(`\p{Han}`)
	inBank := map[string]bool{}
	for _, q := range bank {
		inBank[q.ID] = true
		entry, ok := quotes[q.ID]
		if !ok {
			t.Errorf("%s: no deciding quote in docs/quotes.json", q.ID)
			continue
		}
		for _, lang := range []string{"en", "tc"} {
			qt, ok := entry[lang]
			if !ok || strings.TrimSpace(qt.Text) == "" {
				t.Errorf("%s (%s): no deciding quote", q.ID, lang)
				continue
			}
			citation := q.Source.En
			if lang == "tc" {
				citation = q.Source.Tc
			}
			if cited := citedDocs(citation, lang); !slices.Contains(cited, qt.Doc) {
				t.Errorf("%s (%s): the quote comes from document %q, but the citation %q names %v",
					q.ID, lang, qt.Doc, citation, cited)
				continue
			}
			if !strings.Contains(sourceText(t, lang, qt.Doc), matchKey(qt.Text)) {
				t.Errorf("%s (%s): quote not found in docs/text/%s/%s.txt: %q",
					q.ID, lang, strings.ToUpper(lang), qt.Doc, qt.Text)
			}
			// The English Ordinance prints each defined term's Chinese equivalent in
			// brackets ("director (董事) includes…"), so an English quote may carry
			// those, and nothing else in Chinese.
			if (lang == "tc") != han.MatchString(bracketedHan.ReplaceAllString(qt.Text, "")) {
				t.Errorf("%s (%s): the quote is in the wrong language: %q", q.ID, lang, qt.Text)
			}
			// Long enough to decide something, short enough to be the deciding words
			// rather than the paragraph around them.
			if lang == "en" {
				if n := len(strings.Fields(qt.Text)); n < 5 || n > 50 {
					t.Errorf("%s (en): quote of %d words, want 5 to 50: %q", q.ID, n, qt.Text)
				}
			} else if n := len([]rune(matchKey(qt.Text))); n < 10 || n > 120 {
				t.Errorf("%s (tc): quote of %d characters, want 10 to 120: %q", q.ID, n, qt.Text)
			}
		}
	}
	for id := range quotes {
		if !inBank[id] {
			t.Errorf("docs/quotes.json has a quote for %s, which the bank does not hold", id)
		}
	}
}

// TestCitedCircularsAreCurrent: every circular a question names is one of the
// current documents listed in docs/README.md. In September 2026 ten circulars
// that later documents had overtaken were removed from docs/, and 49 questions
// that cited them had to be re-cited or re-aimed; this keeps a removed
// circular's number from coming back through a new or edited question.
func TestCitedCircularsAreCurrent(t *testing.T) {
	readme, err := os.ReadFile(filepath.Join("docs", "README.md"))
	if err != nil {
		t.Fatal(err)
	}
	number := regexp.MustCompile(`MSSB/[A-Z]+_\d+/\d{4}`)
	current := map[string]bool{}
	for _, line := range strings.Split(string(readme), "\n") {
		if strings.HasPrefix(line, "| ") { // the table of documents
			for _, n := range number.FindAllString(line, -1) {
				current[n] = true
			}
		}
	}
	if len(current) == 0 {
		t.Fatal("found no circular numbers in the table in docs/README.md")
	}
	for _, q := range loadBank(t) {
		for lang, l := range map[string]qLang{"en": q.En, "tc": q.Tc} {
			source := q.Source.En
			if lang == "tc" {
				source = q.Source.Tc
			}
			fields := append(append([]string{l.Q, l.Explain, source}, l.Options...), l.Statements...)
			for _, f := range fields {
				for _, n := range number.FindAllString(f, -1) {
					if !current[n] {
						t.Errorf("%s (%s): cites circular %s, which is not among the current documents in docs/README.md", q.ID, lang, n)
					}
				}
			}
		}
	}
}

// TestNoOtherLanguageText: each language's fields hold that language only, and
// never mention the other edition. Each language follows its own official text,
// so "the Chinese text says…" in an explanation, or 英文本 in a Chinese one,
// is always a slip; so are Chinese characters in an English field, which a
// September 2026 review found in three explanations ("(覆核審裁處)"). Latin
// words are allowed in a Chinese field only where the Chinese sources print
// them too: circular numbers, MT202COV, NAR1, section 53ZTL, the JFIU's web
// address.
func TestNoOtherLanguageText(t *testing.T) {
	han := regexp.MustCompile(`\p{Han}`)
	enTag := regexp.MustCompile(`\b(?:Chinese|English) (?:text|version|edition|wording)\b|\((?:Chinese|English)\)`)
	tcTag := regexp.MustCompile(`英文本|中文本|英文文本|中文文本|英文原文|中文原文`)
	latin := regexp.MustCompile(`[A-Za-z]{2,}`)

	var tcSources strings.Builder
	texts, err := filepath.Glob(filepath.Join("docs", "text", "TC", "*.txt"))
	if err != nil || len(texts) == 0 {
		t.Fatalf("no Chinese source texts in docs/text/TC (run python docs/extract_text.py): %v", err)
	}
	for _, path := range texts {
		b, err := os.ReadFile(path)
		if err != nil {
			t.Fatal(err)
		}
		tcSources.Write(b)
	}
	tcText := tcSources.String()
	printed := map[string]bool{}

	for _, q := range loadBank(t) {
		en := append(append([]string{q.En.Q, q.En.Explain, q.Source.En}, q.En.Options...), q.En.Statements...)
		for _, f := range en {
			if m := han.FindString(f); m != "" {
				t.Errorf("%s (en): Chinese text in an English field: %q", q.ID, f)
			}
			if m := enTag.FindString(f); m != "" {
				t.Errorf("%s (en): mentions another language edition (%q)", q.ID, m)
			}
		}
		tc := append(append([]string{q.Tc.Q, q.Tc.Explain, q.Source.Tc}, q.Tc.Options...), q.Tc.Statements...)
		for _, f := range tc {
			if m := tcTag.FindString(f); m != "" {
				t.Errorf("%s (tc): mentions another language edition (%q)", q.ID, m)
			}
			for _, w := range latin.FindAllString(f, -1) {
				ok, known := printed[w]
				if !known {
					ok = strings.Contains(tcText, w)
					printed[w] = ok
				}
				if !ok {
					t.Errorf("%s (tc): %q is not printed in any Chinese source", q.ID, w)
				}
			}
		}
	}
}
