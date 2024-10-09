# Requirements

{% if build == "slides" %}
```{toctree}
:maxdepth: 2
:caption: Contents

./knowledge
./config
```
{% else %}
```{include} ./knowledge.md
```
```{include} ./config.md
```
{% endif %}


