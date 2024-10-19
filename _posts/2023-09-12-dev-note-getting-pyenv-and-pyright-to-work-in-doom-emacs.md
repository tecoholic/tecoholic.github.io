---
layout: post
title: "dev-note: Getting pyenv and pyright to work in Doom Emacs"
date: 2023-09-12 11:10:47
category: Notes
tags: doom-emacs emacs pyenv pyright python
---

Getting Pyenv and Pyright to play nice in python-mode on Doom Emacs requires sticking to a few rules. I discovered these after multiple attempts of trial and error. All the following things might not be needed. But I got things to work only when I set all of these up. 




So, best advice is - start here and try to reduce it down. 




### Emacs Config




* Edit your `.doom.d/init.el`




2. Enable both `lsp` and `tree-sitter` in the tools. `tree-sitter` is not probably needed for this. But, I wanted to use it, so.

6. Enable python mode with `(python +lsp + tree-sitter +pyenv +pyright)`




* Add the [**Pyenv-mode - Projectile Integration** snippet](https://github.com/pythonic-emacs/pyenv-mode#projectile-integration) to your `~/.doom.d/config.el`





```
(require 'pyenv-mode)

(defun projectile-pyenv-mode-set ()
  "Set pyenv version matching project name."
  (let ((project (projectile-project-name)))
    (if (member project (pyenv-mode-versions))
        (pyenv-mode-set project)
      (pyenv-mode-unset))))

(add-hook 'projectile-after-switch-project-hook 'projectile-pyenv-mode-set)
```



* Then run `~/.emacs.d/bin/doom sync` and then `~/.emacs.d/bin/doctor` to ensure the required tools are available.




### Setting up your Python Env




Add your project as a Projectile project using `SPC p a`




Now if you have read the Projectile script you would have noticed that the "pyenv mode" sets the name of the project as the Python environment name. So, if you like me use [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to create multiple virtual environments, then create your virtualenv with the same name as your project and install the dependencies within that virtualenv. For example, 





```
# project name is awesome-sauce
cd awesome-sauce
pyenv virtualenv 3.11 awesome-sauce
pyenv local awesome-sauce
pip install -r requirements.txt  # or any way you want to setup the dependencies
```



This will create a local `.python-version` file with the virtualenv name. This **file seems to be crucial** in getting the **pyright** to work. I tried multiple times without this file and just using `pyenv shell <env>` to activate the env and install the dependencies. And when I loaded up a file in Emacs, pyright would complain that none of the dependencies were available for import.




### Results




With all of this setup clearly, now I get autocompletion for dependencies installed via pip as expected, and syntax checking is happening as I type.




![](/img/wp-content/uploads/2023/09/screenshot-2023-09-12-at-4.29.59-pm.png?w=1024)


Notice that in the modeline, pyenv has loaded the correct environment and the LSP is also using the same one (the blue Python awesome-sauce). 




I can now also run my tests quickly using `SPC m t t` using pytest.




![](/img/wp-content/uploads/2023/09/screenshot-2023-09-12-at-4.33.03-pm.png?w=1024)


### Finally - a request




There's a big chance that I might have missed something while documenting this. In case you are trying to achieve the same setup, but these rules aren't sufficient to get things working for you, kindly drop a line.



