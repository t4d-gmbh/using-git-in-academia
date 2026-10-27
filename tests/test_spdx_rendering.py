# SPDX-FileCopyrightText: 2023-2026 Jonas I. Liechti <j-i-l@t4d.ch>
# SPDX-FileCopyrightText: 2023-2026 Matteo Delucchi <mail@matteodelucchi.com>
#
# SPDX-License-Identifier: GPL-3.0-only

"""Check SPDX comments through Sphinx, MyST, includes, and Jinja build modes.

Run with the project's installed requirements::

    python -m unittest discover -s tests -p 'test_spdx_rendering.py'
"""

from io import StringIO
from pathlib import Path
import re
from tempfile import TemporaryDirectory
import unittest

from docutils import nodes
from sphinx.application import Sphinx


_REPOSITORY = Path(__file__).resolve().parents[1]
_CONFIGURATION = '''\
extensions = ["myst_parser"]
myst_enable_extensions = ["colon_fence"]
html_theme = "basic"
root_doc = "index"
exclude_patterns = ["fragment.md"]

def render_source(app, docname, source):
    source[0] = app.builder.templates.render_string(source[0], app.config.html_context)

def render_include(app, docname, parent_docname, source):
    render_source(app, docname, source)

def setup(app):
    app.connect("source-read", render_source)
    app.connect("include-read", render_include)
'''


class TestSpdxRendering(unittest.TestCase):
    """Verify that the real Markdown header remains an invisible comment."""

    def test_headers_are_invisible_in_both_build_modes(self) -> None:
        """Reject visible SPDX text, extra section titles, or TOC entries."""
        readme = (_REPOSITORY / "README.md").read_text(encoding="utf-8")
        match = re.match(r"<!--\nSPDX-FileCopyrightText:.*?-->\n", readme, re.DOTALL)
        self.assertIsNotNone(match, "README must start with an HTML SPDX comment")
        assert match is not None
        header = match.group(0) + "\n"

        for mode in ("pages", "slides"):
            with self.subTest(build=mode), TemporaryDirectory() as directory:
                root = Path(directory)
                source = root / "source"
                source.mkdir()
                (source / "conf.py").write_text(_CONFIGURATION, encoding="utf-8")
                (source / "index.md").write_text(
                    header
                    + "# Existing title\n\n"
                    + '{% if build == "slides" %}Slide view{% else %}Handout view{% endif %}\n\n'
                    + "```{include} fragment.md\n```\n",
                    encoding="utf-8",
                )
                (source / "fragment.md").write_text(
                    header + "## Included section\n\nExisting content.\n",
                    encoding="utf-8",
                )
                warnings = StringIO()
                app = Sphinx(
                    srcdir=str(source),
                    confdir=str(source),
                    outdir=str(root / "html"),
                    doctreedir=str(root / "doctrees"),
                    buildername="html",
                    confoverrides={"html_context": {"build": mode}},
                    status=StringIO(),
                    warning=warnings,
                    freshenv=True,
                    warningiserror=True,
                )
                app.build(force_all=True)
                self.assertEqual(app.statuscode, 0, warnings.getvalue())

                titles = [
                    title.astext()
                    for title in app.env.get_doctree("index").findall(nodes.title)
                ]
                self.assertEqual(titles, ["Existing title", "Included section"])
                self.assertNotIn("SPDX", app.env.tocs["index"].astext())

                html = (root / "html" / "index.html").read_text(encoding="utf-8")
                outside_comments = re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)
                self.assertNotIn("SPDX", outside_comments)
                self.assertNotIn("j-i-l@t4d.ch", outside_comments)
                self.assertNotIn("mail@matteodelucchi.com", outside_comments)
                expected_view = "Slide view" if mode == "slides" else "Handout view"
                self.assertIn(expected_view, outside_comments)


if __name__ == "__main__":
    unittest.main()
