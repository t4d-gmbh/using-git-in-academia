```{include} ../README.md
:end-before: <!-- readme-include -->
```

```{toctree}
:caption: About
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
{% endif %}

content/about/index
```

```{toctree}
:caption: Working with Git
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
{% endif %}

content/working-with-git/source/content/index
```

```{toctree}
:caption: Git and its Remotes
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
{% endif %}

content/git-and-its-remotes/source/content/index
```

```{toctree}
:caption: CI/CD Workflows
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
{% endif %}

content/ci-cd-workflows/source/content/index
```

```{toctree}
:caption: Git and Science
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
{% endif %}

content/git-and-science/source/content/index
```
