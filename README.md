# Using Git in Academia

A course for the casual git user...


## Content

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
_Also in [Git and its Remotes](https://github.com/t4d-gmbh/git-and-its-remotes) or separate repo?_

#### Why remotes offer automation
#### Basic structure of a workflow
_Covering both GitHub and GitLab is probably an overkill, maybe just focus on GitLab_
#### About runners
- how they can be set up
- a word about security
#### Automation for non-software developer
- build artifacts (like a .pdf from a .tex)
- continuously test your code 
- write documentations

#### Examples and learning by doing
Presenting the .tex paper example repo with pipeline to build .pdf and multiple
different branches (different formatting for journals).

_That would be the end of part 3_


---

### 4. Part: [Git and Science](https://github.com/t4d-gmbh/git-and-science)
_Here to focus would be on how git and its remotes can help to do better science_

#### Versioning as basis for reproducibility
#### git LFS
- what is it, how to use it
#### git submodules
- how to tie together bigger frameworks
#### Remotes project management tools
- History of Issues/P/M-Requests serves a log-book
- "code" reviewing process facilitates to work collaboratively
- A project is developed directly in a structured and "polished" manner
- ...
#### CI/CD for reproducibility
- Allows to tie application/analysis to specific code versions and tasks (issues) in the project
- Runner environment can be made completely reproducible (see e.g. the r-container repo.) and shareable

#### Examples and learning by doing
Example setup with software package, repo for analysis, some data in git lfs and a pipeline running some
analysis script with results returned via artifacts.

General question and feedback round

_That would be the end of part 3_

