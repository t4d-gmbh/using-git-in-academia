# Outro

{% if slide %}

```{toctree}
:maxdepth: {% if build == "slides" %}1{% else %}2{% endif %}

./content
./instructors
./about
```
{% else %}
```{include} ./content.md
```
```{include} ./instructors.md
```
```{include} ./about.md
```
{% endif %}




