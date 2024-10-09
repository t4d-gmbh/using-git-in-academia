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

part1/index
```
