{% if page %}
# Syllabus
{% else %}
# Schedule
{% endif %}

{% if page %}
```{include} ../../../README.md
:start-after: <!-- syllabus-include -->
:end-before: <!-- syllabus-exclude-->
```
{% else %}
:::{card} Day 1
1. Part: **[Working with git](https://github.com/t4d-gmbh/working-with-git)**

---
Lunch @ Green Kitchen Lab (12:30-13:30). 

---
2. Part: **[Git and its Remotes](https://github.com/t4d-gmbh/git-and-its-remotes)**

:::
:::{card} Day 2
3. Part: **[CI/CD Workflows](https://github.com/t4d-gmbh/ci-cd-workflows)**

---
Lunch @ Green Kitchen Lab (12:30-13:30). 

---
4. Part: **[Git and Science](https://github.com/t4d-gmbh/git-and-science)**
:::
{% endif %}

