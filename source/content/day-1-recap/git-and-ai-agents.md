# Git Commands & AI Agents

**Our recommendation: Encourage inspection but keep control over changes**

:::::{grid} 1 1 2 2
:gutter: 3

::::{grid-item}
**✅ Delegate inspection**

:::{dropdown} git status
Inspect the working tree and staging area.
:::
:::{dropdown} git diff
Explain changes before deciding what belongs together.
:::
:::{dropdown} git log
Explore commit history.
:::
:::{dropdown} git show
Inspect a commit and its changes.
:::
:::{dropdown} git reflog
Find previous positions of HEAD and branches.
:::
:::{dropdown} git blame
Identify the last recorded change to each line—not its rationale.
:::
::::

::::{grid-item}
**🧑 Keep under your control**

:::{dropdown} git add
Select changes for a small, coherent commit.
:::
:::{dropdown} git commit
Define a meaningful, complete step in history.
:::
:::{dropdown} git merge
Decide when changes are ready for integration; verify the resulting state.
:::
:::{dropdown} git rebase
Reshape your branch's history; never rewrite shared history.
:::
:::{dropdown} git cherry-pick
Decide which changes belong on this branch.
:::
:::{dropdown} git switch / git checkout
Choose where development happens; checkout can also overwrite changes.
:::
::::
:::::

**Agents can advise. You remain responsible for the best practices.**

{% if page %}
These recommendations concern the usages described above, not every option a command offers. For example, `git reflog` inspects history, while `git reflog expire` modifies its records.
{% endif %}
