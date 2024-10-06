# Using Git in Academia

A course for the casual git user...

 <!-- redame-include -->

## Development

We can build both pages and slides.

What content should go into `slides`, and what into `pages` can be
determined directly in each markdown file, using the `{% if build == 'pages' %}`
or `{% if build == 'slides' %} ... {% else %} ... {% endif %}` jinja tags.

Typically, the content of a slide should be written in a single markdown file
that can be either be imported into a single page, or as individual pages.
The basic syntax looks similar to this:

```markdown
{% if build == "slides" %}
```{toctree}
:maxdepth: 2

./slide1
./slide2
```
{% else %}
```{include} ./slide1.md
```
```{include} ./slide2.md
```
{% endif %}
```

### Building the content

To build the `pages`:

```bash
sphinx-build -b html source docs/html -E -A build="pages"
```

And to build the `slides`:

```bash
sphinx-build -b html source docs/html/slides -E -A build="slides"
```

_Note:_ The resulting html resides under `/docs/html/slides`

## Content

 <!-- syllabus-include -->

### 1. Part: [Working with git](https://github.com/t4d-gmbh/working-with-git)

#### Introduction to git
- Know the basic building blocks of Git (Commits, Branches, Tags) and their relation
- High-level understanding of how commits build up a history

#### The basic workflow with git
- Relate git operations (pull, push, etc.) to the typical workflow when developing a project
- Understand how local changes integrate into the remote version and vice-versa

#### Some useful commands
- Know some commands beyond commit/pull/push and specific command options that facilitate the integration of git into the personal workflow

#### Collaboration with git
- Become familiar with the idea of maintaining a healthy reference and how it benefits collaboration
- Understand how git operations and use patterns are designed to facilitate the maintenance of a healthy reference
- Learn some best practices that facilitate the maintenance of a healthy branch and thus collaboration
- Get acquainted with the "feature branch" workflow - A simple collaboration approach suitable for most cases
- Recognise the benefits of using git even when working alone in a project

#### A word on versioning
- Grasp the difference between tags and commits and how tags facilitate navigation in the history of a repository
- become acquainted with the [semver](semver.org) versioning standard and how versioning relates to tags.

#### Examples and learning by doing
- Resolve some issues (merge conflicts, etc.) on your own with the [Weekend Out](https://github.com/t4d-gmbh/Weekend-Out) project

_That would be the end of part 1_



---

### 2. Part: [Git and its Remotes](https://github.com/t4d-gmbh/git-and-its-remotes)

#### Git features vs remote services
- Be able to tell what features and tools belong to git and what belong to remote services

#### Most popular remotes
- Come to know the most popular remote services (GitLab, GitHub, ...)
- Learn what remote services are used at the university and what are good approaches to set up a collaborative project (for internal and external collaborations).

#### Organizing projects and more
- Discover how remote services can be used to organize collaboration across repositories
- Basic understanding of GitHub's organisational structure (user, organizations, teams, projects, ...)
- Basic understanding of GitLab's organisational structure ([sub-]groups)

#### Project management with remotes
- Know the elementary building blocks for project management
- Understand how these building blocks integrate into a "feature branch" development approach introduced in part 1

#### Contributing to OpenSource projects
- Become acquainted with the standard workflow for contributions to pubic GitHub/GitLab projects

#### Examples and learning by doing
- Step through a "feature branch" development cycle by means of the project management tolls provided by the remote services
- Identify and resolve some conflicts directly on the remote service


---


### 3. Part: Continuous Integration and Delivery

#### Why remotes offer automation
- Get an idea about the vast application possibilities of automation
- Discover use cases of automation for non-software developer
- Develop an idea how automation can help to maintain a healthy reference, facilitate collaboration and reduce errors

#### Basic structure of an automation workflow
- Become familiar with the principal elements that define a workflow and how workflows are defined on GitHub and GitLab

#### About runners
- Understand the purpose of runners and how they interact with remote services
- Become aware of the security implications the usage of runners might entail
- Learn about the possibility to setup and use dedicated runners
- Understand how runners can be used to create reproducible environments

#### How to integrate automation in a project
- Get familiarized with how automation workflows are triggered
- Learn how automated workflows integrate with project management tools
- Be able to safely use sensitive information (credentials, etc.) in an automation workflow

#### Examples and learning by doing
- Create your own workflow to render and publish a LaTeX document


---

### 4. Part: [Git and Science](https://github.com/t4d-gmbh/git-and-science)

#### Versioning as basis for reproducibility
- Embrace how the commit based git history allows to recreate specific states and configurations
- Apprehend the gap between versioning and reproducibility

#### git LFS
- Learn to version data and larger (binary) files with git

#### git submodules
- Become familiar with the approach to recreate environments with multiple git repositories

#### Remotes project management tools
- See how project management tools can facilitate to adhere to best practices and scientific integrity

#### CI/CD for reproducibility
- Be able to configure runners with completely reproducible environments
- Get familiar with conducting an analysis or simulation via an automation workflow
- Appreciate how automation workflows can bride the gap between versioning and reproducibility

#### Examples and learning by doing
- Complete, use and verify the reproducibility of an exemplary analysis automated with workflows
