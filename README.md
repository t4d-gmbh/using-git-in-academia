# Using Git in Academia

A course for the casual git user...


## Content

### 1. Part: [Working with git](https://github.com/t4d-gmbh/working-with-git)

#### Introduction to git
A short introduction about git and its main features
- [About git](https://t4d-gmbh.github.io/working-with-git/git/about.html)
- [Basic elements](https://t4d-gmbh.github.io/working-with-git/git/basic_elements.html)
- ... _basically most of what is in `Git Workflow` in the working-with-git repo_
#### The basic workflow with git
#### Some useful commands
#### Collaboration with git
- Underlying principles
- The "feature branch" workflow
A simple collaboration approach suitable for most cases
#### A word on versioning
#### Examples and learning by doing
Resolve some issues with the [Weekend Out](https://github.com/t4d-gmbh/Weekend-Out)

_That would be the end of part 1_



---

### 2. Part: [Git and its Remotes](https://github.com/t4d-gmbh/git-and-its-remotes)

#### Git features vs remote services
A short overview what belongs to git and what belongs to the remote services
#### Most popular remotes
- A short intro do _GitLab_ and _GitHub_ (mention _bitbucket_, _gitolite_, ...)
- What exists at Uni
#### Organizing projects and more
- Intro to GitLab's (sub-)group structure and user roles
- Intro do GitHub's user/organization and project structure
#### Project management with remotes
- Issues; Pull/Merge Requests; Milestones and how to use them
- How does the "feature branch" workflow look like when using Issues and Pull/Merge Reqs.
- Creating releases from tags
#### Contributing to OpenSource projects
- How does a typical workflow look when wanting to contribute to a GitHub project
#### Examples and learning by doing
Go through the feature branch workflow by means of Issue-Pull/Merge request


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

