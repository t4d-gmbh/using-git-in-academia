# Best Practices

- **Keep a healthy reference:** Maintain a known, functional and up-to-date reference.
- **Separate changes:** Group related work into coherent chapters on separate branches.
- **Make meaningful steps:** Design each commit as a minimal, logically complete step in the history.
- **Flag states:** Use tags to name and document repository states so they can be identified later.

{% if page %}
The **healthy reference** gives everyone a reliable point of orientation as the project develops. Its state should be known, functional and as up to date as possible.

**Separate changes** as you would separate chapters in a story: each branch has a coherent purpose, and unrelated work belongs elsewhere.

**Meaningful steps** are small, complete logical steps in the history. A commit should not unnecessarily leave the branch in a broken or incomplete state.

**Tags document states**, while commit messages document changes. Naming a state makes it easier to recognize, communicate and return to it—for example, the version associated with a publication.
{% endif %}
