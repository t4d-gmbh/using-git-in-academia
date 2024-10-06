# Configuration file for the Sphinx documentation builder.
import sys

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Git in Academia'
copyright = '2023, T4D GmbH'
author = 'Jonas I. Liechti'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_favicon",
    "sphinx_design",
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
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" # for https://fontawesome.com/ icons
]

html_context = {
    "default_mode": "light",
}

html_theme_options = {
    "repository_url": "https://github.com/t4d-gmbh/using-git-in-academia",
    "repository_branch": "main",
    "home_page_in_toc": True,
    "path_to_docs": "source/",
    "use_edit_page_button": True,
    "use_repository_button": True,
    "toc_title": "Content",
    "use_sidenotes": True,
    "logo": {
        "image_light": "_static/T4D_logo_bw.svg",
        "image_dark": "_static/T4D_logo_wb.svg",
        "link": "https://t4d.ch",
        },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/t4d-gmbh",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        {
            "name": "GitHub Discussion",
            "url": "https://github.com/t4d-gmbh/using-git-in-academia/discussions",
            "icon": "fa-regular fa-comments",
            "type": "fontawesome",
        },
        {
            "name": "Pages",
            "url": "https://t4d-gmbh.github.io/working-with-git/index.html",
            "icon": "fa-solid fa-book",
            "type": "fontawesome",
        },
        {
            "name": "Slides",
            "url": "https://t4d-gmbh.github.io/working-with-git/slides/index.html",
            "icon": "fa-solid fa-person-chalkboard",
            "type": "fontawesome",
        },
    ],
    # "show_toc_level": 2,  # Show the table of contents up to level 2
    "navigation_with_keys": True,  # Enable keyboard navigation

    # "collapse_navigation": False,  # Do not collapse the navigation
    # "sidebar_width": "250px",  # Set the width of the sidebar
}

favicons = [
    "_static/T4D_logo_bw.svg"
]

myst_enable_extensions = [
    "colon_fence",
]

# import datetime
# 
# from setuptools_scm import get_version
# 
# from sphinx_pyproject import SphinxConfig
# 
# # Set the version from setuptools_scm
# version: str = get_version()
# release = version
# 
# 
# project = 'Git in Academia'
# copyright = datetime.date.today().strftime("%Y") + ' T4D GmbH'
# 
# # ###
# # Project Configuration
# # ###
# 
# needs_shinx = "8.0.0"
# 
# extensions = [
#     # core extensions
#     'sphinx.ext.mathjax',
#     'sphinx.ext.viewcode',
#     'sphinx.ext.intersphinx',
#     'sphinx.ext.extlinks',
#     'sphinx.ext.inheritance_diagram',
#     # iPython extensions
#     'IPython.sphinxext.ipython_directive',
#     'IPython.sphinxext.ipython_console_highlighting',
#     # Markdown support
#     'myst_parser', # only enable if `myst_nb` is not used
#     # MErmaid diagram supoort
#     "sphinxcontrib.mermaid",
#     # # Jupyter Notebook support
#     # 'myst_nb',
#     # API documentation support
#     'autoapi',
#     # responsive web component support
#     'sphinx_design',
#     # custom 404 page
#     'notfound.extension',
#     # custom favicons
#     'sphinx_favicon',
#     # copy button on code blocks
#     "sphinx_copybutton",
#     # hover-over tooltips for cross-references
#     # 'hoverxref.extension', # currently no support for markdown as per https://github.com/readthedocs/sphinx-hoverxref/issues/250
# ]
# 
# root_doc = 'index'
# exclude_patterns = [
#     '_build',
# ]
# 
# html_static_path = ['_static']
# templates_path = ['_templates']
# 
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'myst-nb',
#     '.myst': 'myst-nb',
#     # '.ipynb': 'myst-nb',
# }
# 
# # ###
# # Theme Configuration
# # ###
# html_theme = 'pydata_sphinx_theme'
# 
# html_css_files = [
#     "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" # for https://fontawesome.com/ icons
# ]
# html_show_copyright = True
# html_show_sphinx = False
# 
# html_sidebars = {
#     "**": [
#         "search-field.html",
#         "sidebar-nav-bs.html",
#     ],
# }
# html_theme_options = {
#     # "announcement": "<p><a href='#'>Hello</a>News?</p>",
#     # # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html
#     # "switcher": {
#     #     "json_url": "https://raw.githubusercontent.com/...",
#     #     "version_match": version
#     # },
#     # page elements
#     "navbar_start": ["navbar-logo", ]  # , "version-switcher"],
#     "navbar_end": ["navbar-icon-links.html"],
#     # "navbar_persistent": ["theme-switcher"],
#     "footer_start": ["copyright"],
#     "footer_end": ["footer"],
#     "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink", "support"],
#     "header_links_before_dropdown": 8,
#     # page elements content
#     "icon_links": [
#         {
#             "name": "GitHub",
#             "url": "https://github.com/t4d-gmbh",
#             "icon": "fa-brands fa-github",
#             "type": "fontawesome",
#         },
#         {
#             "name": "GitHub Discussion",
#             "url": "https://github.com/t4d-gmbh/using-git-in-academia/discussions",
#             "icon": "fa-regular fa-comments",
#             "type": "fontawesome",
#         }
#     ],
#     # various settings
#     "collapse_navigation": True,
#     "show_prev_next": False,
#     "use_edit_page_button": True,
#     "use_repository_button": True,
#     "navigation_with_keys": True,
#     # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/branding.html#different-logos-for-light-and-dark-mode
#     "logo": {
#         "text": "T4D GmbH",
#         "image_light": "_static/logo/T4D_logo_bw.svg",
#         "image_dark": "_static/logo/T4D_logo_wb.svg",
#         "link": "https://t4d.ch",
#         },
#     # own
#     "use_sidenotes": True,
# }
# 
# # required by html_theme_options: "use_edit_page_button"
# html_context = {
#     "github_user": "t4d-gmbh",
#     "github_repo": "using-git-in-academia",
#     "github_version": "main",
#     "doc_path": "source",
# }
# 
# # ###
# # Extensions Configuration
# # ###
# 
# copybutton_prompt_text = ">>>"
# 
# 
# # sphinx-favicon configuration #########################################
# # https://github.com/tcmetzger/sphinx-favicon
# 
# favicons = [
#     {
#         "rel": "icon",
#         "size": "100x100",
#         "href": "logo/T4D_logo.png"
#     },
#     {
#         "rel": "apple-touch-icon",
#         "size": "500x500",
#         "href": "logo/T4D_logo.png"
#     },
# ]
# 
# # linkcheck Configuration ###############################################
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder
# 
# linkcheck_retries = 1
# linkcheck_workers = 20
# linkcheck_exclude_documents = []
# 
# # notfound Configuration ################################################
# # https://sphinx-notfound-page.readthedocs.io
# 
# notfound_context = {
#     'title': 'Page Not Found',
#     'body': '''                                                                                                                                           
#         <h1>Page Not Found (404)</h1>
#         <p>
#         Euh! It seems we do not have what you are looking for.
#         </p>
#     ''',
# }
# 
# # myst_parser Configuration ############################################
# # https://myst-parser.readthedocs.io/en/latest/configuration.html
# 
# myst_enable_extensions = [
#     "amsmath",
#     "colon_fence",
#     "deflist",
#     "dollarmath",
#     "html_image",
#     "attrs_block",
# ]
# 
# # hoverxref configuration ###############################################
# # https://github.com/readthedocs/sphinx-hoverxref
# 
# """
# 
# hoverxref_auto_ref = True
# hoverxref_domains = ["py"]
# hoverxref_role_types = dict.fromkeys(
#     ["obj", "mod", "ref", "class", "func", "meth", "attr", "exc", "data"],
#     "tooltip",
# )
# hoverxref_default_type = 'tooltip'
# hoverxref_tooltip_lazy = False
# """

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
    source[0] = rendered

def setup(app):
    print(app.config.html_context)
    app.connect("source-read", rstjinja)
