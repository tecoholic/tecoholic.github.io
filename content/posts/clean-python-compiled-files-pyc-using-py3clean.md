---
title: Clean Python compiled files (.pyc) using py3clean
date: '2022-02-03T15:23:24'
slug: clean-python-compiled-files-pyc-using-py3clean
categories:
  - Coding
tags:
  - python
---

Recently ran into some issues with Python compiled files `__pycache__` and `*.pyc` files not getting deleted when doing `git checkout`. The files have been created when I mounted the folder as a volume in a docker container and had different rights than the current user. So, I needed to use `sudo` to remove them recursively in the project.




That's when I learnt of this cool new tool called `py3clean`. Simply run `py3clean <folder>` and it will remove all the Python compiled files recursively.



