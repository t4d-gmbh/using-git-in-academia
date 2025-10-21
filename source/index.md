```{include} ../README.md
:end-before: <!-- readme-include -->
```
{% if build == "slides" %}
<!-- <p style="font-size: 0.9em;"><strong>Dr. Jonas I. Liechti</strong><br>
<strong>Dr. Matteo Delucchi</strong></p> -->
:::{admonition} Authors
:class: note, margin
Dr. Jonas I. Liechti  
Dr. Matteo Delucchi
:::

:::{admonition} Editors
:class: note, margin
Barbara Mejia
:::
{% else %}
### Authors

**Dr. Jonas I. Liechti**  
**Dr. Matteo Delucchi**  


### Editors

**Barbara Mejia**
{% endif %}

### Content

```{toctree}
:caption: About
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:hidden:
{% endif %}

content/about/index
```

{% if slide %}
#### Working with <i class="fab fa-git"></i>
{% endif %}
```{toctree}
:caption: Part 1: Working with Git
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
:caption: Part 2: Git and its Remotes
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
:caption: Part 3: CI/CD Workflows
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
:caption: Part 4: Git and Science
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}
{% if build == "slides" %}:numbered:
:hidden:
{% endif %}

content/git-and-science/source/content/index
```
