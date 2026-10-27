/*
 * SPDX-FileCopyrightText: 2023-2026 Jonas I. Liechti <j-i-l@t4d.ch>
 * SPDX-FileCopyrightText: 2023-2026 Matteo Delucchi <mail@matteodelucchi.com>
 *
 * SPDX-License-Identifier: GPL-3.0-only
 */

/** Run with: node --test tests/slide-layout.test.cjs */
const assert = require("node:assert/strict");
const { existsSync, readFileSync } = require("node:fs");
const { join } = require("node:path");
const { test } = require("node:test");

const css = readFileSync(join(__dirname, "../source/_static/slides.css"), "utf8");
const template = readFileSync(
  join(__dirname, "../source/_templates/page.html"),
  "utf8",
);

test("collapsed slide width has an editable responsive maximum", () => {
  assert.match(
    css,
    /:root\s*\{\s*--slide-collapsed-content-max-width:\s*min\(90%,\s*100rem\);\s*\}/,
  );
});

test("only collapsed desktop slides are constrained and horizontally centred", () => {
  assert.match(
    css,
    /@media\s*\(min-width:\s*992px\)\s*\{\s*#pst-primary-sidebar-checkbox:checked\s*~\s*\.bd-container\s+\.slide-frame\s*\{\s*max-width:\s*var\(--slide-collapsed-content-max-width\);\s*margin-inline:\s*auto;\s*\}\s*\}/,
  );
});

test("the slide wrapper uses CSS instead of an overriding inline width", () => {
  assert.match(
    template,
    /{% if build == "slides" %}\s*<div class="slide-frame">\s*<div id=['"]rescaled-text['"]>/,
  );
  assert.match(css, /\.slide-frame\s*\{[^}]*width:\s*95%;[^}]*\}/);
  assert.match(css, /\.slide-frame\s*\{[^}]*height:\s*80vh;[^}]*\}/);
});

test("intro and outro use the same portraits from the shared static directory", () => {
  for (const page of ["about/presenters.md", "outro/instructors.md"]) {
    const markdown = readFileSync(
      join(__dirname, "../source/content", page),
      "utf8",
    );
    for (const name of ["jonas_github.png", "matteo_github.png"]) {
      assert.ok(markdown.includes(`{image} /_static/${name}`), page);
      assert.ok(existsSync(join(__dirname, "../source/_static", name)));
      for (const directory of ["about", "outro"]) {
        assert.ok(!existsSync(join(__dirname, "../source/content", directory, name)));
      }
    }
    assert.match(markdown, /:class: instructor-portrait/);
    assert.doesNotMatch(markdown, /:width:/);
  }
});

test("portraits are capped at 80vh without stretching; outro keeps its width cap", () => {
  const styles = readFileSync(join(__dirname, "../source/_static/custom.css"), "utf8");
  const portrait = styles.match(/img\.instructor-portrait\s*\{([^}]+)\}/);
  assert.ok(portrait);
  for (const declaration of [
    /max-height:\s*80vh;/,
    /max-width:\s*100%;/,
    /height:\s*auto;/,
    /width:\s*auto;/,
  ]) {
    assert.match(portrait[1], declaration);
  }
  assert.match(
    styles,
    /img\.instructor-portrait--outro\s*\{\s*max-width:\s*80%;\s*\}/,
  );
});
