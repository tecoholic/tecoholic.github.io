---
layout: post
title: "Managing Open edX Tutor with mise"
date: 2024-09-18
category: Projects
tags: mise openedx tutor
---

Previously, I wrote about using [mise](https://mise.jdx.dev/) as a [replacement for Pyenv and NVM](https://arunmozhi.in/2024/09/06/replacing-pyenv-nvm-direnv-with-mise/). In this post, I will document how I use it to manage [Open edX Tutor](https://docs.tutor.edly.io/) versions for the different projects I work on.

### Tutor Version Manager

There is already an existing solution to managing multiple Tutor versions and projects called the [Tutor Version Manager](https://tvm.docs.edunext.co/en/latest/index.html) or TVM. It provides a nice cli to create projects with specific Tutor versions and handle the project environments with the correct context.

However, I have the same issues with TVM that I have with Tutor. It is a Python tool that must be `pip` installed. That means:

* I would need to set up a virtual environment dedicated to TVM
* Activate that virtual environment before using TVM

TVM doesn't simply manage Tutor versions, [it also manages Tutor Projects](https://tvm.docs.edunext.co/en/latest/tvm_topic_guides/environment_manager.html). Each TVM project comes with its own virtual environment. So, TVM requires activating and deactivating it. From the TVM docs:

> If you also have another environment like a python virtual environment, you need to deactivate each virtual environment in order. For example, if you have `(venv) [v12.2.0@project-name]`, you need to run `deactivate` and then `tvmoff`.
> 
> [TVM as Environment Manager](https://tvm.docs.edunext.co/en/latest/tvm_topic_guides/environment_manager.html)

I didn't want to do this. I don't want to hold the context of the environments I am working with.[^1]

### Mise & asdf-tutor

So, I created [asdf-tutor](https://github.com/tecoholic/asdf-tutor) to let Mise do all this work. Since Mise uses the asdf plugins as a backend, I can now use it to automatically set Tutor versions and project environments. Here is how it typically works.

#### Setting up a tutor project

1. Create a new directory
2. Tell Mise which version of tutor to use
3. Setup tutor env vars

```sh
mkdir my-project
cd my-project
mise use tutor@18 # or tutor@latest # or tutor@nightly
mise set TUTOR_ROOT=$(pwd)
mise set TUTOR_PLUGINS_ROOT=$(pwd)/plugins
mise trust
```

#### Working on a tutor project

```sh
cd my-project
```

That's all.

#### Working with multiple projects

Setup multiple projects the same way as above. Switch projects by navigating to the folder.

![screenshot](https://arunmozhi.in/wp-content/uploads/2024/09/tutor-projects-using-mise-asdf-tutor.png)

#### Removing a project

Just delete the directory.[^2]

### Finally...

I really like Mise. Offloading the job of handling tool versions and environment management is something I have really come to depend on regularly. It makes everything effortless. Changing directory is all that's needed.[^3]

### Footnotes

[^1]: I understand, remembering the order of environments and deactivating them is strictly not necessary. I could simply close the shell and create a new one which is clear of these contexts. But mise has spoiled me. I simply change directories, and it takes care of everything else.
[^2]: I just mean the project environment. You probably need to delete Docker images, containers…etc.,. But that's in the domain of "Tutor" and not "Mise".
[^3]: One can achieve a very similar setup using direnv and pyenv-virtualenv auto-activation as well. In fact, [here is a guide to do just that and much more](https://forum.opencraft.com/t/tips-and-tricks-for-using-tutor-as-devstack-replacement/1587).
