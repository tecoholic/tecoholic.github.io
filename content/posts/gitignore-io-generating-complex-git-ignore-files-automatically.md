---
title: "gitignore.io - Generating Complex Git Ignore Files Automatically"
date: 2020-02-23T08:09:23
slug: "gitignore-io-generating-complex-git-ignore-files-automatically"
categories:
  - Coding
tags:
  - github
---

My way of generating `.gitignore` files has evolved over time. First it was just adding files and folder names manually to a empty file called .gitignore. Then as more and more people started sharing their **dotfiles**, I started using copies of it. One most used resource for me is the [Github gitignore Repository](https://github.com/github/gitignore). I just grab the raw url of the gitignore that I want and use wget to save in my repository, like:

```bash
wget https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore -O .gitignore
```

### gitignore.io



Recently I have started using the online app [gitignore.io](https://gitignore.io). The cool thing about this is you can add a combination of things that define your environment and the gitignore is defined based on all of them. For example see the screenshot below:

![gitignore_io](/img/wp-content/uploads/2020/02/gitignore_io.png)

This generates a gitignore file that I can use for:

* Python Django project
* that I am going to develop using PyCharm
* in a Linux Machine
* under a virtual environment



If you thought this was cool, there is also

* a command line way of doing it - https://docs.gitignore.io/install/command-line
* plugins for text editors VS Code, NeoVIM and EMacs - https://docs.gitignore.io/install/editor-extensions
* libraries and apps for Node, Go, Python & Rust - https://docs.gitignore.io/install/client-applications



..etc., In case you are not using it, give it a try.
