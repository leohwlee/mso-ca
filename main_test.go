package main

import (
	"encoding/json"
	"io/fs"
	"os"
	"path/filepath"
	"reflect"
	"strings"
	"testing"
)

// TestSingleFileBank: the one-file build must carry the whole bank, differing
// from web/questions.json in whitespace only.
func TestSingleFileBank(t *testing.T) {
	sub, err := fs.Sub(webFS, "web")
	if err != nil {
		t.Fatal(err)
	}
	path := filepath.Join(t.TempDir(), "mso-ca.html")
	if err := writeSingleFile(sub, path); err != nil {
		t.Fatal(err)
	}
	page, err := os.ReadFile(path)
	if err != nil {
		t.Fatal(err)
	}
	_, rest, found := strings.Cut(string(page), "<script>window.BANK = ")
	embedded, _, closed := strings.Cut(rest, ";</script>")
	if !found || !closed {
		t.Fatal("the page has no window.BANK script")
	}
	if strings.Contains(embedded, "\n") {
		t.Error("the embedded bank still carries its line breaks and indentation")
	}

	var got, want any
	if err := json.Unmarshal([]byte(embedded), &got); err != nil {
		t.Fatalf("the embedded bank does not parse: %v", err)
	}
	src, err := fs.ReadFile(sub, "questions.json")
	if err != nil {
		t.Fatal(err)
	}
	if err := json.Unmarshal(src, &want); err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(got, want) {
		t.Error("the embedded bank differs from web/questions.json")
	}
}
