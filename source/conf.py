# Configuration file for the Sphinx documentation builder.
import sys

from setuptools_scm import get_version

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'Git in Academia'
copyright = '2023-2025; T4D GmbH'
author = 'Jonas I. Liechti'
# ###
# Versioning - get it from the git tag
# ###
version: str = get_version(root='..')
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_favicon",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx_tabs.tabs",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

html_context = {
    "default_mode": "light",
}

discuss_icon = {
            "name": "GitHub Discussion",
            "url": "https://github.com/t4d-gmbh/using-git-in-academia/discussions",
            "icon": "fa-regular fa-comments",
            "type": "fontawesome",
        }
pages_icon = {
            "name": "Pages",
            "url": "https://t4d-gmbh.github.io/using-git-in-academia/index.html",
            "icon": "fa-solid fa-book",
            "type": "fontawesome",
        }
slides_icon = {
            "name": "Slides",
            "url": "https://t4d-gmbh.github.io/using-git-in-academia/slides/index.html",
            "icon": "fa-solid fa-person-chalkboard",
            "type": "fontawesome",
        }
html_theme_options = {
    "repository_url": "https://github.com/t4d-gmbh/using-git-in-academia",
    "repository_branch": "main",
    "path_to_docs": "source/",
    # "home_page_in_toc": True,
    "use_edit_page_button": True,
    "use_repository_button": True,
    "toc_title": "Content",
    "use_sidenotes": True,
    "logo": {
        "image_light": "_static/T4D_logo_bw.svg",
        "image_dark": "_static/T4D_logo_wb.svg",
        "link": "https://t4d.ch",
        },
    "show_toc_level": 2,  # Show the table of contents up to level 2
    "navigation_with_keys": True,  # Enable keyboard navigation
    "collapse_navigation": False,  # Do not collapse the navigation
    # "sidebar_width": "250px",  # Set the width of the sidebar
    "icon_links": [discuss_icon, slides_icon],

}

favicons = [
    "T4D_logo.png"
]

myst_enable_extensions = [
    "colon_fence",
]

# ###
# Custom jinja parser to enable jinja templating
# ###
def rstjinja(app, docname, source):
    """
    Render source file with jinja first
    """
    print(f"{docname=}")
    # only apply to 'html' builder
    if app.builder.format == 'html':
        src = source[0]
        rendered = app.builder.templates.render_string(
            src, app.config.html_context
        )
        source[0] = rendered

def include_rstjinja(app, docname, parent_docname, source):
    """
    Render included sources widh jinja
    """
    return rstjinja(app=app, docname=docname, source=source)

def setup(app):
    builds = app.config.html_context.get('build', 'pages')
    # setting `slide` and `page` context
    app.config.html_context['page'] = True
    app.config.html_context['slide'] = False
    if builds == 'slides':
        app.config.html_context['slide'] = True
        app.config.html_context['page'] = False
        # ###
        # we do some config adaptations for the slides
        # ###
        # simpler sidebar
        app.config.html_sidebars = {
            "**": [
                # "navbar-logo.html",
                "icon-links.html",
                # "search-button-field.html",
                "sbt-sidebar-nav.html"
                ]
        }
        # only show discuss and pages icons in sidebar
        app.config.html_theme_options['icon_links'] = [discuss_icon, pages_icon]
        # adding the new styling
        app.config.html_css_files.append('slides.css')
    app.connect("source-read", rstjinja)
    app.connect("include-read", include_rstjinja)
