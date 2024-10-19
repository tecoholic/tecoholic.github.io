---
layout: post
title: "Thoughts on The Git Branch PR Model"
date: 2020-05-13 07:33:49
category: General
tags: coding software technology tools
---

> This is just ramblings of someone who is overwhelmed when having to adapt to a new model of working with Git. There will perhaps be nothing of value here.



Git - Such a central part of everyday work. Something I learnt a decade ago. Must have spent a full month learning it well including the forking and Pull Request model from Github. Since then nothing major has changed in my workflow. It is the same routine. If it is a OpenSource project - fork the project, work on the dev branch (sometimes even master depending on how the project is maintained) and issue a pull request with the changes. If it is a team project, have a dev branch where I pushed changes. If there is a feature or refactor that will affect other people's work, then create a branch (a feature branch) and work on the branch. Once the work is done, rebase it on the dev branch and merge it to dev.

![git-rebase-model](/img/wp-content/uploads/2020/05/git-rebase-model.png)

The circles with different colors indicate different people (except the last diagram where I changed it for emphasis). This model is closely following [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/).

Most times I have been lucky to have an almost linear tree with rebases. At times of merge conflicts we do get an extra merge commit. But for the majority it has been that one branch that is the place of action and the other branches were things that kind of existed from time to time.

This has been made possible due to:

1. Small team sizes on the project. So the domain is usually non-overlapping creating less necessity to isolate work.
2. Developer discipline of not pushing any broken code.
3. When there have been large team sizes, the work has been fairly isolated.So, commit isolation at branch level was not the norm.



I had always thought Git to be one of things you learn once, until today, when I ran into a new model of working.

### Enter GitHub Flow


![github-flow](/img/wp-content/uploads/2020/05/github-flow.png)
[The GitHub Flow](https://guides.github.com/introduction/flow/) outlines something called a branch PR flow where work always starts with a branch followed by a pull request. It seems like a very simple and straight forward thing but kind of punches me in the gut.

1. So what the is source of the latest code? At a given time there are a number branches and pull requests.
2. Why do I need a separate branch if I am just push a quickfix or a bug fix?
3. Why does everything involve a PR merge? Why can't I just rebase or just push to the dev branch?



I am sure all of this has answers like:

1. It depends on what one defines as the latest. If it is latest stable, then it is perhaps the master. If there are outstanding pull requests, then they need to be reviewed and merged to get the latest.
2. So that my bugfix doesn't cause a regression in someone else's code
3. Code is peer reviewed before it is merged. Rebase kind of destroy's the history of workflow and a PR merge provides a full history of the work that went to it.



I kind of get all these reasons. But I am still not convinced that we need to branch for everything that we do on to the code. I would rather have master as the stable branch, dev as the latest branch or even the other way master as the latest branch, version-x as the stable branch and create new branches only sparingly based on need.

![git-branch-rarely](/img/wp-content/uploads/2020/05/git-branch-rarely.png)

The flow on the left involves others working on the base branch (master/dev pick anything) and a developer creating a branch for a feature that will be affecting normal development. The others keep pushing things to the base branch as they go. Once the Dev A has finished with the feature, it gets merged to the common base branch.

I don't see how the model on the right branch for everything model is better than the one on the left. Why do both developer's have to branch away? The only answer must be that developers can't be trusted to push to the base (again master/dev whichever is not stable) without review of the code.

I think the world has moved to this place where systems are designed with the notion that it is going to fail. So we have built CI systems that will run tests on PR's and hold the code for review until someone decides it can be merged and our model has evolved to accommodate such systems. It is good if it prevents disasters and head aches in teams. I have always worked on the assumption that the other developers know what they are doing and teams I have worked on have existed on those lines. Today was the first time I was told to follow the model on the right and I am simply overwhelmed.
