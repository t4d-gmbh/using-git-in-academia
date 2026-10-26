/** Run with: node --test tests/slide-layout.test.cjs */
const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
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
