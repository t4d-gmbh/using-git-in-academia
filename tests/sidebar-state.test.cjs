/**
 * Regression tests for slide sidebar persistence, without browser dependencies.
 * Run with: node --test tests/sidebar-state.test.cjs
 * The mock toggle reproduces PyData 0.15.4's direct .checked assignment.
 */
const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const { join } = require("node:path");
const { test } = require("node:test");
const { runInNewContext } = require("node:vm");

const source = readFileSync(
  join(__dirname, "../source/_static/sidebar-state.js"),
  "utf8",
);

class EventTargetMock {
  listeners = new Map();
  afterListener = () => {};

  addEventListener(name, callback, capture = false) {
    const listeners = this.listeners.get(name) || [];
    listeners.push({ callback, capture });
    this.listeners.set(name, listeners);
  }

  emit(name) {
    const listeners = this.listeners.get(name) || [];
    for (const capture of [true, false]) {
      for (const listener of listeners) {
        if (listener.capture === capture) {
          listener.callback();
          this.afterListener();
        }
      }
    }
  }
}

/** Load a fresh slide document, optionally reusing another page's storage. */
function loadPage({
  storage = new Map(),
  href = "https://example.org/course/slides/index.html",
  contentRoot = "./",
  desktop = true,
  blockedRead = false,
  blockedWrite = false,
  missingToggle = false,
} = {}) {
  const checkbox = new EventTargetMock();
  checkbox.checked = false;
  checkbox.defaultChecked = false;
  const button = new EventTargetMock();
  // The theme does not emit a change event when the hamburger is activated.
  button.addEventListener("click", () => {
    checkbox.checked = !checkbox.checked;
  });
  const media = new EventTargetMock();
  media.matches = desktop;
  const document = new EventTargetMock();
  document.readyState = "loading";
  document.documentElement = { dataset: { content_root: contentRoot } };
  document.getElementById = (id) =>
    id === "pst-primary-sidebar-checkbox" && !missingToggle ? checkbox : null;
  document.querySelectorAll = (selector) => {
    assert.equal(selector, ".primary-toggle");
    return [button];
  };
  const window = new EventTargetMock();
  window.location = { href };
  window.matchMedia = (query) => {
    assert.equal(query, "(min-width: 992px)");
    return media;
  };
  window.sessionStorage = {
    getItem(key) {
      if (blockedRead) throw new Error("Storage is blocked");
      return storage.get(key) ?? null;
    },
    setItem(key, value) {
      if (blockedWrite) throw new Error("Storage is blocked");
      storage.set(key, value);
    },
  };
  const microtasks = [];
  const tasks = [];
  // Native browser events can run microtasks between listener callbacks.
  button.afterListener = () => {
    while (microtasks.length) microtasks.shift()();
  };
  window.setTimeout = (callback, delay) => {
    assert.equal(delay, 0);
    tasks.push(callback);
  };
  runInNewContext(source, {
    document,
    window,
    URL,
    queueMicrotask: (callback) => microtasks.push(callback),
  });

  return {
    checkbox,
    storage,
    window,
    ready() {
      document.readyState = "complete";
      document.emit("DOMContentLoaded");
    },
    click() {
      button.emit("click");
      while (microtasks.length) microtasks.shift()();
      while (tasks.length) tasks.shift()();
    },
    resize(isDesktop) {
      media.matches = isDesktop;
      media.emit("change");
    },
  };
}

test("a fresh desktop session keeps the expanded default", () => {
  const page = loadPage();
  assert.equal(page.checkbox.checked, false);
  assert.equal(page.storage.size, 0);
});

test("collapse and expand both persist across nested slide navigation", () => {
  const first = loadPage();
  first.ready();
  first.click();
  assert.equal(first.checkbox.checked, true);
  const second = loadPage({
    storage: first.storage,
    href: "https://example.org/course/slides/content/topic/index.html",
    contentRoot: "../../",
  });
  // Restore before DOMContentLoaded, while the sidebar is still being parsed.
  assert.equal(second.checkbox.checked, true);
  second.ready();
  second.click();
  assert.equal(second.checkbox.checked, false);
  assert.equal(loadPage({ storage: second.storage }).checkbox.checked, false);
});

test("reloading restores a collapsed preference", () => {
  const page = loadPage();
  page.ready();
  page.click();
  assert.equal(loadPage({ storage: page.storage }).checkbox.checked, true);
});

test("history restoration reapplies the latest preference", () => {
  const first = loadPage();
  first.ready();
  const second = loadPage({ storage: first.storage });
  second.ready();
  second.click();
  first.window.emit("pageshow");
  assert.equal(first.checkbox.checked, true);
});

test("different course roots do not share sidebar preferences", () => {
  const first = loadPage();
  first.ready();
  first.click();
  const other = loadPage({
    storage: first.storage,
    href: "https://example.org/other/slides/index.html",
  });
  assert.equal(other.checkbox.checked, false);
});

test("mobile loads never restore the collapsed desktop checkbox", () => {
  const page = loadPage();
  page.ready();
  page.click();
  const mobile = loadPage({ storage: page.storage, desktop: false });
  assert.equal(mobile.checkbox.checked, false);
  mobile.ready();
  mobile.click();
  mobile.click();
  assert.equal(loadPage({ storage: page.storage }).checkbox.checked, true);
});

test("mobile interactions do not replace an expanded desktop preference", () => {
  const page = loadPage();
  page.ready();
  page.click();
  page.click();
  page.resize(false);
  page.click();
  assert.equal(page.checkbox.checked, true);
  page.resize(true);
  assert.equal(page.checkbox.checked, false);
});

test("desktop collapse does not turn into an open overlay on resize", () => {
  const page = loadPage();
  page.ready();
  page.click();
  page.resize(false);
  assert.equal(page.checkbox.checked, false);
  page.resize(true);
  assert.equal(page.checkbox.checked, true);
});

test("blocked storage reads leave the normal toggle functional", () => {
  const page = loadPage({ blockedRead: true });
  page.ready();
  page.click();
  assert.equal(page.checkbox.checked, true);
});

test("blocked storage writes leave the normal toggle functional", () => {
  const page = loadPage({ blockedWrite: true });
  page.ready();
  page.click();
  assert.equal(page.checkbox.checked, true);
});

test("unrecognized stored values leave the expanded default", () => {
  const page = loadPage({
    storage: new Map([["web-course:primary-sidebar:/course/slides/", "invalid"]]),
  });
  assert.equal(page.checkbox.checked, false);
});

test("pages without the theme checkbox are left alone", () => {
  assert.doesNotThrow(() => loadPage({ missingToggle: true }));
});

test("the template loads persistence only for slides, before sidebar markup", () => {
  const template = readFileSync(
    join(__dirname, "../source/_templates/page.html"),
    "utf8",
  );
  assert.match(
    template,
    /{% block docs_navbar %}\s*{% if build == "slides" %}[\s\S]*?sidebar-state\.js[\s\S]*?{% endif %}\s*{{ super\(\) }}\s*{% endblock %}/,
  );
});
