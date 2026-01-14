---
title: "Replacing pyenv, nvm, direnv with Mise"
date: 2024-09-06T10:00:00
slug: "replacing-pyenv-nvm-direnv-with-mise"
categories:
  - Coding
tags:
  - devtool
  - mise
  - nodejs
  - python
---

I recently got a new laptop with the Ultra 7 Intel processor. My older one is an i5 8th generation. So, I as very surprised when a new terminal was usable after a visible delay. It was almost as slow as the old laptop.

### Maybe I bought a crappy Intel Processor?

Now, Intel CPUs aren't being praised for their performance. I know I don't have an AMD Ryzen 9. Surely being **54th fastest** has to mean better than **394th fastest**?

![Core i5 8265U Benchmark](/img/wp-content/uploads/2024/09/corei5_8265u_benchmark.png)

![Ultra 7 155H Benchmark](/img/wp-content/uploads/2024/09/ultra7_155h_benchmark.png)

Credits: _CPU Benchmark screenshots from [https://www.cpubenchmark.net](https://www.cpubenchmark.net)_

**16 cores at 3.8GHz** should be able to load **a terminal emulator** faster than **4 cores at 1.6GHz**. I was almost crying at the ridiculously mismatched specs of these processors and the painfully similar experiences as a user.

### Impact of pyenv and nvm

With the comfort that I didn't buy a lemon for a processor, the obvious thing to look at was my .bashrc file. There are a few methods to profile bash scripts. I tried the technique with timestamps, but settled on using [hyperfine](https://github.com/sharkdp/hyperfine), as the timestamping each bash command that runs in a terminal startup was too verbose and was difficult to understand.

With hyerfine, I was able to take the "bashrc" snippets from pyenv and nvm setup and run it independently. I didn't save the exact results, but it came to around ~220ms for NVM to load and ~180ms for pyenv to load. Together as a single script, ~330ms to load.

So, every time I open the terminal, I wait almost half a second just to get the pyenv and nvm to loaded into shell env. Okay, this is ridiculous. This reminded me of the days I ran [Bash-it](https://github.com/Bash-it/bash-it) on an Atom Processor netbook and would wait 2 seconds before the terminal was usable. Back then, I was a student and compiling a huge Qt C++ codebase. Waiting for things to happen kind of came with the territory. But, now, I am a Python programmer. I don't even compile py scripts to those pesky pyc bytecode. I digress.

Let's find something that won't waste CPU cycles for loading this overtly complex program called a terminal.

### mise-en-place

![mise google search](/img/wp-content/uploads/2024/09/image.png)

NO. Not that one.

### mise-en-place devtool

![mise-en-place devtool](/img/wp-content/uploads/2024/09/image-2.png)

[YES. That one.](https://mise.jdx.dev)

I have briefly experimented with mise, when it was called rtx.

_Sidenote to @jdx if you are reading this_: You thought you did better when you changed the name from rtx (graphics card) to mise (French cuisine)? No! Google says you didn't mate. Fantastic tool though. Thanks a lot for that.

It depended on .rtx.toml, used runtime injection for everything, and didn't have shims and IDE integration was non-existant. So, it didn't work out at that time.

But mise. mise is good. mise is great. It has everything I need, including IDE integration for [Emacs](https://mise.jdx.dev/ide-integration.html#emacs) and [Neovim](https://mise.jdx.dev/ide-integration.html#neovim). It uses [asdf](https://asdf-vm.com/)'s plugins and that means there are 100s of tools that you can manage versions of. Furthermore, it also replaces [direnv](https://direnv.net/).

"That's all great, how fast is it?" I am glad you asked. Here is the hyperfine benchmarking result for the line that goes into ".bashrc".

![Hyperfine Results](/img/wp-content/uploads/2024/09/image-3.png)

First, I was surprised to see 117 and 276 there, but it's not milliseconds. It is **micro-seconds**. Hyperfine complains that's it can't measure it accurately, as it's less than 5ms. LOL.

### Finally...

So, I have been using in my new laptop for a week and haven't actually found a use case it doesn't solve for me. I might migrate my old laptop to mise as well. That would require updating multiple projects, and that's going to take time.

Meanwhile, I created [asdf-tutor](https://github.com/tecoholic/asdf-tutor) to automatically switch between [Open edX Tutor](https://docs.tutor.edly.io/) versions. It's still a WIP and requires some testing before I can publish it publicly... That would probably be the next blog post. 👋
