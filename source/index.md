```{include} ../README.md
:end-before: <!-- readme-include -->
```

```{toctree}
:caption: About
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
:hidden:
{% endif %}

content/about/index
```

{% if slide %}
#### Working with <i class="fab fa-git"></i>
{% endif %}
```{toctree}
:caption: Working with Git
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
:hidden:
{% endif %}

content/working-with-git/source/content/index
```

{% if slide %}
#### <i class="fab fa-git"></i> and its Remotes
{% endif %}
```{toctree}
:caption: Git and its Remotes
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
:hidden:
{% endif %}

content/git-and-its-remotes/source/content/index
```

{% if slide %}
#### CI/CD Workflows
{% endif %}
```{toctree}
:caption: CI/CD Workflows
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
:hidden:
{% endif %}

content/ci-cd-workflows/source/content/index
```

{% if slide %}
#### <i class="fab fa-git"></i> and Science
{% endif %}
```{toctree}
:caption: Git and Science
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
:hidden:
{% endif %}

content/git-and-science/source/content/index
```
