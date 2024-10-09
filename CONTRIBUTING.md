# Contributing to the `working-with-git` course 📚

Thank you for your interest in contributing to our documentation!
We appreciate your help in making this course better.
Please follow the guidelines below to ensure a smooth contribution process.

## General Guidelines 📝

- **Be Respectful**: Treat all contributors with respect and kindness.
  We are all here to learn and improve.
- **Read the course content**: Familiarize yourself with the existing content before making changes.
  This will also help you understand the structure and style.
- **Use Clear Language**: Aim for clarity and conciseness in your writing.
  Avoid jargon unless you are using terms that are generally understood.

## Setting Up Your Environment ⚙️

To contribute to this course, you'll need to set up your build environment 🏗️.

Follow these steps:

1. **Clone the Repository**:
    ```
    git clone https://github.com/t4d-gmbh/working-with-git
    cd working-with-git
    ```

2. **Install Dependencies**:
   Make sure you have Sphinx installed.
   You can install it, along with all ohter dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Build&view the content**
   To build the content locally, run:
   ```
   sphinx-build -b html source docs/html -E -A build="pages"
   sphinx-build -b html source docs/html/slides -E -A build="slides"
   ```
   This will generate the HTML documentation in the `docs/html` directory.

   The first command will build the static html pages and the second command builds the slides 🖼️.
   
   To browse the html pages locally, open `docs/html/index.html` in your favorite browser.
   For the slides, open `docs/html/slides/index.html`

   ⚠️ Note ⚠️: The links to switch from the html pages view to the slides view are broken when locally
   viewing the files.

## Implementing Changes 🛠️

The content is situated under `source/content` and split up into topical sub-folders.
Each sub-folder should contain an `index.md` that determines which `*.md` files to include.
The content from the sub-folder is then included in the main content by including its `index.md`
file in the `toctree` of [`source/index.md`](./source/index.md):

    # source/index.md
    ...
    ```{toctree}
    ...
    content/<sub-folder>/index
    ```

### Slide vs. Page Content

The content is rendered both as slides and as html pages.
Typically, slides should contain illustrations and bullet-point like text snippets while the 
pages should be somewhat more self-contained.

Since we do not wont to duplicate content we can create markdown files that can be rendered both
as slides and included into the static view of html pages.
To achieve this we render all the markdown content with `jinja` before converting it to `html` and
pass a `build` context variable along that is either set to `"slides"` or `"pages"`.

Following this procedure we then setup the `index.md` file in each sub(-sub)-folder as follows:


    {% if build == "slides" %}
    <!-- BUILDING THE SLIDES -->
    ```{toctree}
    :maxdepth: 2
    :caption: Contents
    
    ./slide1
    ./slide2
    ...
    ```
    {% else %}
    <!-- BUILDING THE PAGES -->
    ```{include} ./slide1.md
    ```
    Maybe some extra text for the pages
    ```{include} ./slide2.md
    ```
    {% endif %}

This will render each slide on a separate page for the slides and build a document
that includes the slides for the html page.
Note that we also adapt the styling of the page depending on the value of the `build`
context variable.

Within each included or imported `.md` file you can also specify what content you want
to show in the slides and what should be shown in the page view.
You can use:

- `{% if builds == 'pages' %}...{% endif %}` or `{% if page %}...{% endif %}` to include
  content only in the static page
- `{% if builds == 'slides' %}...{% endif %}` or `{% if slide %}...{% endif %}` to include
  content only in the slide

The above `slide1.md` could look as follows:

    {% if build == "slides" %}
    # Slide 1 title
    {% else %}
    ## Subtitle for slide 1 content
    {% endif %}

    **This text is both on the slide and in the pages
    {% if slide %}
    🤪 This in only on the slide 🤪
    {% endif %}

    {% if page %}
    This text is only in the pages view and not on the slide
    {% endif %}


## Making Contributions ✨

Here are some ways you can contribute:

- **Fixing Typos**: Simple fixes like correcting typos or grammatical errors are always welcome!
- **Improving Clarity**: If you find sections that are unclear, feel free to rewrite them for better understanding.
- **Adding Examples**: Examples can greatly enhance the documentation. If you have a use case, consider adding it.
- **Suggest Additions**: If you think that the course is missing come curcial aspects, let us know by [creating an Issue](https://github.com/t4d-gmbh/using-git-in-academia/issues/new).

## Submitting Changes 🚀

Once you have made your changes, follow these steps to submit them:

1. **Create a New Branch**:
    ```
    git checkout -b my-feature-branch
    ```

2. **Commit Your Changes**:
   Make sure to write clear and descriptive commit messages:
    ```
    git commit -m "Fix typo in about git section"
    ```

3. **Push to Your Fork**:
    ```
    git push origin my-feature-branch
    ```

4. **Open a Pull Request**:
   Go to the original repository on GitHub and open a pull request.
   Provide a clear description of your changes and why they are needed.

## Additional Resources 🌐

- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

Thank you for contributing!
Your efforts help make our documentation better for everyone. If you have any questions, feel free to reach out to the maintainers.

