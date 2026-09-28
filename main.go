// mso-ca builds the offline mock exam for the C&ED MSO Competence Assessment:
// it folds web/ into the one self-contained HTML file that is released.
package main

import (
	"bytes"
	"embed"
	"encoding/base64"
	"encoding/json"
	"flag"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

//go:embed web
var webFS embed.FS

func main() {
	exportHTML := flag.String("export-html", "", "write the whole app as one self-contained HTML file to this path")
	flag.Parse()
	if *exportHTML == "" {
		fmt.Fprintln(os.Stderr, "usage: go run . -export-html dist/mso-ca.html")
		os.Exit(2)
	}

	sub, err := fs.Sub(webFS, "web")
	if err != nil {
		fatal(err)
	}
	if err := writeSingleFile(sub, *exportHTML); err != nil {
		fatal(err)
	}
	fmt.Println("wrote", *exportHTML)
}

// writeSingleFile folds index.html, the stylesheet (with the fonts embedded as
// data URIs), the question bank and the script into one HTML file that runs
// straight from disk — no server needed.
func writeSingleFile(fsys fs.FS, path string) error {
	read := func(name string) (string, error) {
		b, err := fs.ReadFile(fsys, name)
		return string(b), err
	}
	index, err := read("index.html")
	if err != nil {
		return err
	}
	css, err := read("style.css")
	if err != nil {
		return err
	}
	js, err := read("app.js")
	if err != nil {
		return err
	}
	bank, err := read("questions.json")
	if err != nil {
		return err
	}
	// The bank is kept indented so its diffs stay readable. The page needs none of
	// that whitespace, which is about 7% of the file.
	var compact bytes.Buffer
	if err := json.Compact(&compact, []byte(bank)); err != nil {
		return fmt.Errorf("questions.json: %w", err)
	}

	fontRef := regexp.MustCompile(`url\("fonts/([^"]+)"\)`)
	css = fontRef.ReplaceAllStringFunc(css, func(m string) string {
		name := fontRef.FindStringSubmatch(m)[1]
		b, err := fs.ReadFile(fsys, "fonts/"+name)
		if err != nil {
			return m
		}
		return "url(data:font/woff2;base64," + base64.StdEncoding.EncodeToString(b) + ")"
	})

	// a literal "</script" inside inlined code would end the script element early
	safe := func(s string) string { return strings.ReplaceAll(s, "</script", `<\/script`) }

	out := strings.Replace(index, `<link rel="stylesheet" href="style.css">`, "<style>\n"+css+"\n</style>", 1)
	out = strings.Replace(out, `<script src="app.js"></script>`,
		"<script>window.BANK = "+safe(compact.String())+";</script>\n<script>\n"+safe(js)+"\n</script>", 1)
	if strings.Contains(out, `href="style.css"`) || strings.Contains(out, `src="app.js"`) {
		return fmt.Errorf("index.html did not contain the expected stylesheet/script tags")
	}

	// The fonts are embedded as data URIs, so the OFL notice has to travel with
	// them. In the served app the stylesheet points at fonts/OFL.txt; that path
	// does not exist in a one-file build, so the notice is inlined here instead.
	notice, err := fontNotice(fsys)
	if err != nil {
		return err
	}
	out = strings.Replace(out, "<!DOCTYPE html>", "<!DOCTYPE html>\n"+notice, 1)

	// dist/ is gitignored, so on a fresh clone the output folder does not exist yet.
	if err := os.MkdirAll(filepath.Dir(path), 0o755); err != nil {
		return err
	}
	return os.WriteFile(path, []byte(out), 0o644)
}

// fontNotice returns the bundled fonts' attribution and licence as an HTML
// comment, so a single-file build carries them even though fonts/ does not
// ship alongside it.
func fontNotice(fsys fs.FS) (string, error) {
	var b strings.Builder
	b.WriteString("<!--\n")
	for _, name := range []string{"fonts/README.txt", "fonts/OFL.txt"} {
		f, err := fs.ReadFile(fsys, name)
		if err != nil {
			return "", err
		}
		// A run of hyphens must not survive inside an HTML comment. Replacing
		// "--" once is not enough: the rule separators in OFL.txt are long runs,
		// and a single pass over "-----" still leaves "--" behind. Repeat until
		// no pair remains — each pass shortens the longest run, so this ends.
		text := string(f)
		for strings.Contains(text, "--") {
			text = strings.ReplaceAll(text, "--", "- -")
		}
		b.WriteString(text)
		b.WriteString("\n")
	}
	b.WriteString("-->")
	return b.String(), nil
}

func fatal(err error) {
	fmt.Fprintln(os.Stderr, "error:", err)
	os.Exit(1)
}
