package main

import (
	"bytes"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
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
		{"03", regexp.MustCompile(`AML/CFT Guideline|Guideline for MSOs|\bGlossary\b`)},
		{"05", regexp.MustCompile(`Licensing Guide`)},
		{"10", regexp.MustCompile(`(?:^|[^y] )F&P Guideline|Criteria for Determining Fitness`)},
		{"11", regexp.MustCompile(`Supplementary (?:F&P|Guideline on Fitness)`)},
		{"20", regexp.MustCompile(`Business Plan`)},
		{"21", regexp.MustCompile(`AML/CFT Policy|AML Policy Guidelines`)},
		{"12", regexp.MustCompile(`Pecuniary Penalty|Disciplinary Action Guideline`)},
		{"13", regexp.MustCompile(`Disciplinary Fining`)},
		{"04", regexp.MustCompile(`AMLO|Cap\. ?615|(?:^|[\s;(,])ss?\.\s?\d|Sch(?:\.|edule) ?\d|\bPart \d`)},
		{"22", regexp.MustCompile(`MIS_06/2018`)},
		{"14", regexp.MustCompile(`MIS_05/2021`)},
		{"07", regexp.MustCompile(`MIS_03/2023`)},
		{"08", regexp.MustCompile(`MIS_01/2024`)},
		{"42", regexp.MustCompile(`MIS_01/2025`)},
		{"15", regexp.MustCompile(`MIS_02/2025`)},
		{"43", regexp.MustCompile(`MIS_03/2025`)},
		{"16", regexp.MustCompile(`MIS_04/2025`)},
		{"18", regexp.MustCompile(`MIS_01/2026`)},
		{"19", regexp.MustCompile(`FATF_02/2026`)},
		{"45", regexp.MustCompile(`FATF_03/2026`)},
		{"06", regexp.MustCompile(`\bFAQ\b`)},
		{"02", regexp.MustCompile(`CA_01/2021|Sample Questions`)},
		{"09", regexp.MustCompile(`MIS_06/2021|Identification and Mitigation of Proliferation Financing Risks|Circular on Counter-Proliferation Financing \(22 December 2021\)`)},
		{"17", regexp.MustCompile(`Money Changers Ordinance|Cap\. ?34\b`)},
		{"23", regexp.MustCompile(`Cross-boundary Movement|Cap\. ?629\b`)},
		{"24", regexp.MustCompile(`Trade-Based Money Laundering Risk Indicators`)},
		{"25", regexp.MustCompile(`Hong Kong Money Laundering and Terrorist Financing Risk Assessment|Hong Kong ML/TF Risk Assessment Report|2022.*Risk Assessment Report`)},
		{"26", regexp.MustCompile(`SAN_01/2018|United Nations Sanctions.*Principles|Circular on United Nations Sanctions \(7 February 2018\)`)},
	},
	"tc": {
		{"01", regexp.MustCompile(`能力評核須知`)},
		{"03", regexp.MustCompile(`《打擊洗錢及恐怖分子資金籌集指引》|《打擊洗錢指引》`)},
		{"05", regexp.MustCompile(`《牌照指引》`)},
		{"10", regexp.MustCompile(`《有關適當人選準則的指引》`)},
		{"11", regexp.MustCompile(`補充指引》`)},
		{"20", regexp.MustCompile(`《遞交業務計劃的指引》`)},
		{"21", regexp.MustCompile(`《遞交打擊洗錢及恐怖分子資金籌集政策的指引》`)},
		{"12", regexp.MustCompile(`《施加罰款紀律行動指引》`)},
		{"13", regexp.MustCompile(`《紀律處分罰款指引》`)},
		{"04", regexp.MustCompile(`《打擊洗錢條例》|第615章|附表\d|第\d+[A-Z]*(?:\([0-9A-Za-z]+\))*條`)},
		{"22", regexp.MustCompile(`MIS_06/2018`)},
		{"14", regexp.MustCompile(`MIS_05/2021`)},
		{"07", regexp.MustCompile(`MIS_03/2023`)},
		{"08", regexp.MustCompile(`MIS_01/2024|第三方付款通函|第三方支付涉及的洗錢及恐怖分子資金籌集風險`)},
		{"42", regexp.MustCompile(`MIS_01/2025`)},
		{"15", regexp.MustCompile(`MIS_02/2025`)},
		{"43", regexp.MustCompile(`MIS_03/2025`)},
		{"16", regexp.MustCompile(`MIS_04/2025`)},
		{"18", regexp.MustCompile(`MIS_01/2026|《打擊以貿易進行洗錢活動指引》通函`)},
		{"19", regexp.MustCompile(`FATF_02/2026`)},
		{"45", regexp.MustCompile(`FATF_03/2026`)},
		{"06", regexp.MustCompile(`常見問題`)},
		{"02", regexp.MustCompile(`CA_01/2021|參考試題`)},
		{"09", regexp.MustCompile(`MIS_06/2021|識別和緩解大殺傷力武器擴散融資風險|《打擊大殺傷力武器擴散融資通函》（2021年12月22日）`)},
		{"17", regexp.MustCompile(`《貨幣兌換商條例》|第34章`)},
		{"23", regexp.MustCompile(`《實體貨幣及不記名可轉讓票據跨境流動條例》|第629章`)},
		{"24", regexp.MustCompile(`以貿易為本的洗錢風險指標`)},
		{"25", regexp.MustCompile(`香港洗錢及恐怖分子資金籌集風險評估報告`)},
		{"26", regexp.MustCompile(`SAN_01/2018|聯合國制裁.*原則|《聯合國制裁通函》（2018年2月7日）`)},
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
	Doc      string `json:"doc"`
	Text     string `json:"text"`
	Language string `json:"language,omitempty"`
}

// quoteSet is one language's quotes for an item: one per statement for an item
// written with notes, or a single deciding quote for an item from the old bank.
type quoteSet []quote

func (s *quoteSet) UnmarshalJSON(b []byte) error {
	if len(b) > 0 && b[0] == '{' {
		var one quote
		if err := json.Unmarshal(b, &one); err != nil {
			return err
		}
		*s = quoteSet{one}
		return nil
	}
	return json.Unmarshal(b, (*[]quote)(s))
}

func loadQuotes(t *testing.T) map[string]map[string]quoteSet {
	t.Helper()
	b, err := os.ReadFile(filepath.Join("docs", "quotes.json"))
	if err != nil {
		t.Fatalf("read docs/quotes.json: %v", err)
	}
	var qs map[string]map[string]quoteSet
	if err := json.Unmarshal(b, &qs); err != nil {
		t.Fatalf("parse docs/quotes.json: %v", err)
	}
	return qs
}

// TestSourceTextsCurrent: every primary document, including archived ones, has its
// extracted text in docs/text, taken from the file that is there now. A
// document replaced without running docs/extract_text.py again would leave the
// quote check comparing the bank with the old edition, which is the mistake
// that let superseded circulars stay in the bank until September 2026.
func TestSourceTextsCurrent(t *testing.T) {
	// One document number is shared by filenames, quotes, text and transcripts.
	catalogBytes, err := os.ReadFile(filepath.Join("docs", "catalog.json"))
	if err != nil {
		t.Fatal(err)
	}
	type catalogEdition struct {
		File   string
		Path   string
		SHA256 string `json:"sha256"`
	}
	var catalog struct {
		Documents []struct {
			ID       string
			Priority string
			Editions map[string]catalogEdition
		}
	}
	if err := json.Unmarshal(catalogBytes, &catalog); err != nil {
		t.Fatal(err)
	}
	sourceIDs := map[string]map[string]string{"EN": {}, "TC": {}}
	sourcePaths := map[string]map[string]string{"EN": {}, "TC": {}}
	originalHashes := map[string]string{}
	ids := map[string]bool{}
	ranks := map[string]int{"high": 1, "medium": 2, "low": 3}
	lastRank := 0
	for i, doc := range catalog.Documents {
		if ids[doc.ID] || doc.ID != fmt.Sprintf("%02d", i+1) {
			t.Fatalf("invalid document number in catalog: %+v", doc)
		}
		ids[doc.ID] = true
		rank, ok := ranks[doc.Priority]
		if !ok || rank < lastRank {
			t.Fatalf("catalog is not in descending priority: %s", doc.ID)
		}
		lastRank = rank
		for lang, edition := range doc.Editions {
			if sourceIDs[lang] == nil {
				sourceIDs[lang] = map[string]string{}
				sourcePaths[lang] = map[string]string{}
			}
			name := edition.File
			if filepath.Base(name) != name || !strings.HasPrefix(name, doc.ID+"_") || sourceIDs[lang][name] != "" {
				t.Fatalf("invalid or duplicate catalog filename: %s/%s", lang, name)
			}
			sourceIDs[lang][name] = doc.ID
			path := doc.Editions[lang].Path
			if path == "" {
				path = lang + "/" + name
			}
			if filepath.IsAbs(path) || strings.Contains(path, "..") {
				t.Fatalf("invalid source path: %s", path)
			}
			sourcePaths[lang][name] = filepath.FromSlash(path)
			originalHashes[filepath.FromSlash(path)] = edition.SHA256
		}
	}
	b, err := os.ReadFile(filepath.Join("docs", "text", "manifest.json"))
	if err != nil {
		t.Fatalf("read docs/text/manifest.json: %v", err)
	}
	var manifest map[string]struct {
		Source           string `json:"source"`
		SHA256           string `json:"sha256"`
		TranscriptSHA256 string `json:"transcript_sha256"`
		TextSHA256       string `json:"text_sha256"`
	}
	if err := json.Unmarshal(b, &manifest); err != nil {
		t.Fatalf("parse docs/text/manifest.json: %v", err)
	}
	seen := map[string]bool{}
	for lang, sources := range sourceIDs {
		for name, num := range sources {
			key := lang + "/" + num + ".txt"
			seen[key] = true
			m, ok := manifest[key]
			if !ok || m.Source != name {
				t.Errorf("docs/%s/%s has no extracted text (run python docs/extract_text.py)", lang, name)
				continue
			}
			src, err := os.ReadFile(filepath.Join("docs", sourcePaths[lang][name]))
			if err != nil {
				t.Fatal(err)
			}
			// Line endings are folded first: git checks the FAQ page, a text file, out
			// with CRLF on Windows and LF elsewhere.
			rawSourceSum := sha256.Sum256(src)
			src = bytes.ReplaceAll(src, []byte("\r\n"), []byte("\n"))
			if sum := sha256.Sum256(src); hex.EncodeToString(sum[:]) != m.SHA256 {
				t.Errorf("docs/%s/%s has changed since its text was extracted (run python docs/extract_text.py)", lang, name)
			}
			if fi, err := os.Stat(filepath.Join("docs", "text", key)); err != nil || fi.Size() == 0 {
				t.Errorf("docs/text/%s is missing or empty", key)
			}
			text, err := os.ReadFile(filepath.Join("docs", "text", key))
			if err != nil {
				t.Fatal(err)
			}
			text = bytes.ReplaceAll(text, []byte("\r\n"), []byte("\n"))
			if sum := sha256.Sum256(text); hex.EncodeToString(sum[:]) != m.TextSHA256 {
				t.Errorf("docs/text/%s changed since extraction", key)
			}
			transcriptPath := filepath.Join("docs", "transcripts", num+".json")
			transcript, transcriptErr := os.ReadFile(transcriptPath)
			if transcriptErr == nil {
				transcript = bytes.ReplaceAll(transcript, []byte("\r\n"), []byte("\n"))
				sum := sha256.Sum256(transcript)
				if hex.EncodeToString(sum[:]) != m.TranscriptSHA256 {
					t.Errorf("%s changed since extraction; re-check labels and run docs/extract_text.py", transcriptPath)
				}
				var labels map[string]json.RawMessage
				var binding struct {
					SourceSHA256 string `json:"source_sha256"`
				}
				if err := json.Unmarshal(transcript, &labels); err != nil {
					t.Fatalf("parse %s: %v", transcriptPath, err)
				}
				if err := json.Unmarshal(labels[lang], &binding); err != nil || binding.SourceSHA256 != hex.EncodeToString(rawSourceSum[:]) {
					t.Errorf("%s is not bound to the current %s PDF", transcriptPath, lang)
				}
			} else if !os.IsNotExist(transcriptErr) || m.TranscriptSHA256 != "" {
				t.Errorf("read image transcript %s: %v", transcriptPath, transcriptErr)
			}
		}
		entries, err := os.ReadDir(filepath.Join("docs", lang))
		if os.IsNotExist(err) {
			continue // BI/ZH reference editions live only under archive/.
		}
		if err != nil {
			t.Fatal(err)
		}
		for _, entry := range entries {
			path := filepath.Join(lang, entry.Name())
			if entry.IsDir() || sourcePaths[lang][entry.Name()] != path {
				t.Errorf("unregistered reading file: docs/%s", path)
			}
		}
	}
	for path, expected := range originalHashes {
		raw, err := os.ReadFile(filepath.Join("docs", path))
		if err != nil {
			t.Fatal(err)
		}
		sum := sha256.Sum256(raw)
		if strings.HasSuffix(path, ".md") {
			sum = sha256.Sum256(bytes.ReplaceAll(raw, []byte("\r\n"), []byte("\n")))
		}
		if hex.EncodeToString(sum[:]) != expected {
			t.Errorf("official original changed: docs/%s", path)
		}
	}
	for key := range manifest {
		if !seen[key] {
			t.Errorf("docs/text/%s comes from a document no longer in docs/", key)
		}
	}
	for _, doc := range catalog.Documents {
		for lang := range doc.Editions {
			if !seen[lang+"/"+doc.ID+".txt"] {
				t.Errorf("catalog source %s/%s has no archived document and extracted text", lang, doc.ID)
			}
		}
	}
}

// TestQuotesFromCitedSources: every question stores, in each language, the
// passages that decide it, copied verbatim from a document its citation names:
// one per statement for an item written with notes (for a true statement the
// passage that supports it, for a false one the passage it departs from), and a
// single deciding quote for an item from the old bank. Until September 2026 the
// bank stored no such passage, so every blind review had to find the deciding
// words again from the citation alone; storing them makes grounding a
// mechanical check, and a quote that stops matching flags a source that has
// been edited or re-extracted since the question was written. The English quote
// comes from the English text and the Chinese from the Chinese, because each
// language follows its own edition.
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
			set, ok := entry[lang]
			want := 1
			if q.annotated() {
				want = q.n()
			}
			if !ok || len(set) != want {
				t.Errorf("%s (%s): %d quotes, want %d", q.ID, lang, len(set), want)
				continue
			}
			citation := q.Source.En
			if lang == "tc" {
				citation = q.Source.Tc
			}
			cited := citedDocs(citation, lang)
			for _, doc := range cited {
				if doc < "01" || doc > "26" {
					t.Errorf("%s (%s): citation names excluded document %s", q.ID, lang, doc)
				}
			}
			for i, qt := range set {
				where := fmt.Sprintf("%s (%s)", q.ID, lang)
				if want > 1 {
					where = fmt.Sprintf("%s (%s, statement %d)", q.ID, lang, i+1)
				}
				if strings.TrimSpace(qt.Text) == "" {
					t.Errorf("%s: empty quote", where)
					continue
				}
				if qt.Doc < "01" || qt.Doc > "26" || len(qt.Doc) != 2 {
					t.Errorf("%s: document %s is outside the approved 01–26 scope", where, qt.Doc)
				}
				quoteLang := lang
				if qt.Language != "" && qt.Language != lang {
					if lang != "tc" || qt.Doc != "24" || qt.Language != "en" || !strings.Contains(q.Source.Tc, "學習譯文") {
						t.Errorf("%s: unsupported or unlabelled source-language override", where)
					}
					quoteLang = qt.Language
				}
				if !slices.Contains(cited, qt.Doc) {
					t.Errorf("%s: the quote comes from document %q, but the citation %q names %v", where, qt.Doc, citation, cited)
					continue
				}
				if !strings.Contains(sourceText(t, quoteLang, qt.Doc), matchKey(qt.Text)) {
					t.Errorf("%s: quote not found in docs/text/%s/%s.txt: %q", where, strings.ToUpper(lang), qt.Doc, qt.Text)
				}
				// The English Ordinance prints each defined term's Chinese equivalent in
				// brackets ("director (董事) includes…"), so an English quote may carry
				// those, and nothing else in Chinese.
				if (quoteLang == "tc") != han.MatchString(bracketedHan.ReplaceAllString(qt.Text, "")) {
					t.Errorf("%s: the quote is in the wrong language: %q", where, qt.Text)
				}
				// Long enough to decide something, short enough to be the deciding words
				// rather than the paragraph around them.
				if quoteLang == "en" {
					if n := len(strings.Fields(qt.Text)); n < 3 || n > 60 {
						t.Errorf("%s: quote of %d words, want 3 to 60: %q", where, n, qt.Text)
					}
				} else if n := len([]rune(matchKey(qt.Text))); n < 6 || n > 140 {
					t.Errorf("%s: quote of %d characters, want 6 to 140: %q", where, n, qt.Text)
				}
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
// reviewed bank sources in catalog.json. A study-priority archive is not a
// withdrawal finding. In September 2026 ten circulars
// that later documents had overtaken were removed from docs/, and 49 questions
// that cited them had to be re-cited or re-aimed; this keeps a removed
// circular's number from coming back through a new or edited question.
func TestCitedCircularsAreCurrent(t *testing.T) {
	raw, err := os.ReadFile(filepath.Join("docs", "catalog.json"))
	if err != nil {
		t.Fatal(err)
	}
	number := regexp.MustCompile(`MSSB/[A-Z]+_\d+/\d{4}`)
	current := map[string]bool{}
	var catalog struct {
		Documents []struct {
			Circular      string
			ReadingStatus string `json:"reading_status"`
		}
	}
	if err := json.Unmarshal(raw, &catalog); err != nil {
		t.Fatal(err)
	}
	for _, doc := range catalog.Documents {
		if doc.ReadingStatus == "active" && number.MatchString(doc.Circular) {
			current[doc.Circular] = true
		}
	}
	if len(current) == 0 {
		t.Fatal("found no reviewed bank circulars in docs/catalog.json")
	}
	for _, q := range loadBank(t) {
		for lang, l := range map[string]qLang{"en": q.En, "tc": q.Tc} {
			source := q.Source.En
			if lang == "tc" {
				source = q.Source.Tc
			}
			for _, f := range append(l.fields(), source) {
				for _, n := range number.FindAllString(f, -1) {
					if !current[n] {
						t.Errorf("%s (%s): cites circular %s, which is not a reviewed bank source in docs/catalog.json", q.ID, lang, n)
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
	raw, err := os.ReadFile(filepath.Join("docs", "catalog.json"))
	if err != nil {
		t.Fatal(err)
	}
	var catalog struct {
		Documents []struct {
			ID            string
			ReadingStatus string `json:"reading_status"`
		}
	}
	if err := json.Unmarshal(raw, &catalog); err != nil {
		t.Fatal(err)
	}
	var texts []string
	for _, doc := range catalog.Documents {
		if doc.ReadingStatus == "active" {
			texts = append(texts, filepath.Join("docs", "text", "TC", doc.ID+".txt"))
		}
	}
	if len(texts) == 0 {
		t.Fatal("no Chinese question-bank source texts")
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
		for _, f := range append(q.En.fields(), q.Source.En) {
			if m := han.FindString(f); m != "" {
				t.Errorf("%s (en): Chinese text in an English field: %q", q.ID, f)
			}
			if m := enTag.FindString(f); m != "" {
				t.Errorf("%s (en): mentions another language edition (%q)", q.ID, m)
			}
		}
		for _, f := range append(q.Tc.fields(), q.Source.Tc) {
			// Document 24 has no official Chinese edition. Its citation must
			// explicitly identify the study translation, not invent an edition.
			labelledTranslation := f == q.Source.Tc && strings.Contains(f, "學習譯文") && slices.Contains(citedDocs(f, "tc"), "24")
			if m := tcTag.FindString(f); m != "" && !labelledTranslation {
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

// TestOfficialWording: an item marked as one of C&ED's own samples carries
// C&ED's words. Every statement and the stem, in each language, must be found in
// the sample paper (MSSB/CA_01/2021, document 23) or the Guidance Notes
// (document 01, ¶7.1), so that "official" never labels a paraphrase.
func TestOfficialWording(t *testing.T) {
	// The sample paper prints its letterhead on every page, sometimes in the
	// middle of a statement that runs over a page break.
	header := strings.NewReplacer(matchKey("香港海關"), "", matchKey("Customs and Excise Department"), "")
	for _, q := range loadBank(t) {
		if q.Official == "" {
			continue
		}
		for _, lang := range []string{"en", "tc"} {
			l := q.side(lang)
			sample := header.Replace(sourceText(t, lang, "02"))
			for _, text := range append([]string{l.Q}, l.Statements...) {
				k := matchKey(text)
				if !strings.Contains(sample, k) && !strings.Contains(sourceText(t, lang, "01"), k) {
					t.Errorf("%s (%s): %q is not in C&ED's sample questions", q.ID, lang, text)
				}
			}
		}
	}
}
