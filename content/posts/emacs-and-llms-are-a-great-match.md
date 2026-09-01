---
title: "Emacs and LLMs"
subtitle: ""
date: 2026-09-01T20:36:45+10:00
lastmod: 2026-09-01T21:27:45+10:00
draft: false
author: "Arunmozhi"
authorLink: ""
description: "Emacs and LLMs are a great match for personalized software."
license: ""
images: []

tags:
  - llm
  - emacs
categories:
  - Coding

featuredImage: ""
featuredImagePreview: ""

hiddenFromHomePage: false
hiddenFromSearch: false
twemoji: false
lightgallery: true
ruby: true
fraction: true
fontawesome: true
linkToMarkdown: true
rssFullText: false

toc:
  enable: true
  auto: true
  keepStatic: false
code:
  copy: true
  maxShownLines: 50
math:
  enable: false
  # ...
mapbox:
  # ...
share:
  enable: true
  # ...
comment:
  enable: true
  # ...
library:
  css:
    # someCSS = "some.css"
    # located in "assets/"
    # Or
    # someCSS = "https://cdn.example.com/some.css"
  js:
    # someJS = "some.js"
    # located in "assets/"
    # Or
    # someJS = "https://cdn.example.com/some.js"
seo:
  images: []
  # ...
---

I have been using LLMs for small things here and there. My main line of work doesn't require constantly churning out code day in and day out.
So, I haven't gone for any of the crazy setups. I mostly just launch OpenCode or Claude Code and run a task here or there and move on.

But, recently I have found something that I really enjoy using LLMs for - customizing Emacs.

<!--more-->

### Doom Emacs

If you are an Emacs user (or even a [Neo]VIM one), you are probably wondering - what I am on about right now? Isn't Doom Emacs already batteries included? Isn't setting it up essentially, uncommenting a few lines here and there? Maybe setup a theme or a font in `config.el` and it should be done, right?

Well yeah. That's how I use it. Sorry! _used it_.

I am not a tinkerer, at least when it comes to editors. I don't know enough and haven't found the motivation to invest into them. The last time I had a custom config I created from scratch was pre-NeoVim days using Vim and Vundle. Since then, I have just used either dedicated IDEs like PyCharm (bought the Profession edition for many years) or off the shelf configs like LunarVim, AstroVim, Doom Emacs..etc.,


### LLMs and personalized software

Any regular visitor to Hackernews and such sites would know that the broader theme with LLMs has been personalized software. People are creating terminal applications that suit their needs[^1] or [choosing GUI over TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/) - there is something for everyone to tinker these days.

Emacs is famously called as an Operating System more than a text editor. So, I decided to take advantage of that recently and started tinkering. First I started small - making org-mode render using Sans Serif font instead of fixed width, make the checkboxes render a tick instead of a cross... things like that. Small tweaks that made things nice for me. Then I have slowly started to expand - a module that allows me to post to a discourse discussion directly from Emacs[^2], a custom Doom Emacs plugin that smartly detects Open edX Tutor environments and allows me to run Tutor commands using a few keystrokes ..etc.,

I have started managing my Emacs config with version control again, after abandoning it a couple of years ago. It seemed pointless back then. Uncommenting lines don't need version control :D

Now the config is a lot more valuable. It's built for my needs. Unique and probably flaky. But I don't care. Because LLMs can fix them when they break.

### The cool part

The coolest part of this experience has not be the _special snowflake config just for me_. It's been the way this has been built.

To start - I don't know Elisp. At least not enough to build modules. So when I prompt an LLM to do something, I closely watch how it builds the functionality. Most of it is just `grep`ping line numbers and `find`ing files. Then once it starts building, it just evals the Elisp on Emacs directly and when it need reference, it just reads Elisp files directly from the `.config/emacs` directory. Not one does it look up documentation on the internet.

That for me is the coolest part. Emacs is this piece of software that has everything written down right here on my machine. It can be shaped into a tool that I want, exactly the way I want it just using that. Nothing more needed. Amazing.

### Closing out

Yes, I know I am using an LLM that's doing all of the work. I am not learning anything..etc., I acknowledge that. At the same time, I am also happy that I can personalize Emacs to my hearts content. I don't have think if my personal software should be a TUI or GUI, what langugae or framework to choose..etc., It's been fun.


[^1]: I couldn't link something specific here. Just see the **Show HN:** section of Hackernews. There are projects shared everyday and TUIs are abundantly represented.
[^2]: Emacs-everywhere should just be enough to deal with any textbox on the browser. Unfortunately I am caught in some comptability hell between Wayland and Firfox Snap on Ubuntu. So, the best I could get was to launch the editor window with the text from a text box. And then I had to manually copy contents and paste it - that is... so... not "everywhere".
