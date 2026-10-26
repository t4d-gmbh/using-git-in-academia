/* Remember the desktop slide sidebar preference without replacing the theme toggle. */
(() => {
  const checkbox = document.getElementById("pst-primary-sidebar-checkbox");
  const contentRoot = document.documentElement.dataset.content_root;
  if (!checkbox || contentRoot === undefined) return;

  // Sphinx supplies a relative root for every page, including nested documents.
  const rootPath = new URL(contentRoot, window.location.href).pathname;
  const storageKey = `web-course:primary-sidebar:${rootPath}`;
  // Sphinx Book Theme 1.1.x reverses the checkbox meaning below this breakpoint.
  const desktop = window.matchMedia("(min-width: 992px)");

  function restoreState() {
    if (!desktop.matches) {
      // A checked desktop checkbox must not become an open mobile overlay.
      checkbox.checked = false;
      return;
    }

    let preference = null;
    try {
      preference = window.sessionStorage.getItem(storageKey);
    } catch {
      // Storage may be disabled; retain the theme's normal default in that case.
    }
    checkbox.checked =
      preference === "collapsed" ||
      (preference !== "expanded" && checkbox.defaultChecked);
  }

  function rememberState() {
    if (!desktop.matches) return;
    try {
      window.sessionStorage.setItem(
        storageKey,
        checkbox.checked ? "collapsed" : "expanded",
      );
    } catch {
      // A storage restriction must not prevent ordinary sidebar interaction.
    }
  }

  function connectToggle() {
    document.querySelectorAll(".primary-toggle").forEach((button) => {
      // The theme assigns .checked directly, without firing a change event.
      // A task (not a microtask) waits until all theme handlers have completed.
      // Button click also covers Enter/Space activation, without another toggle.
      button.addEventListener(
        "click",
        () => window.setTimeout(rememberState, 0),
        true,
      );
    });
    checkbox.addEventListener("change", rememberState);
  }

  // The template loads this after the checkbox but before the sidebar is parsed,
  // so restoring visibility does not wait for the page to finish rendering.
  restoreState();
  desktop.addEventListener("change", restoreState);
  window.addEventListener("pageshow", restoreState);
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", connectToggle);
  } else {
    connectToggle();
  }
})();
