---
title: "Using Typescript V7 With Emacs Eglot"
subtitle: "Configuring Emacs' Eglot to use the new TypeScript v7 as a LSP server."
date: 2026-07-10T12:37:48+10:00
lastmod: 2026-07-10T12:37:48+10:00
draft: false
author: "Arunmozhi"
authorLink: ""
description: ""
license: ""
images: []

tags:
    - emacs
    - typescript
    - lsp
    - software development
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
seo:
  images: []
  # ...
---

TypeScript Version 7 was [released officially](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) yesterday (July 8th, 2026).
Amongst other things it also includes support for the Language Server Protocol (LSP). Let's ditch the old Javascript based `typescript-language-server`.
<!--more-->


## Install TS v7

Install TypeScript in whatever way you want and just make sure `which tsc` resolves to a valid value. You can also check `tsc --lsp` to see if you have
the right version. It should tell you `only stdio is supported`.

## Configure Eglot

Add the following to your `config.el` of Doom Emacs.

```elisp
(after! eglot
  (add-to-list 'eglot-server-programs
               '((js-mode js-ts-mode rjsx-mode typescript-mode tsx-ts-mode)
                 . ("tsc" "--lsp" "--stdio"))))
```

I use Doom Emacs, so it uses `after!` macro. If you use a custom `init.el`, then you probably know how to adapt this already :)

That's it, now your JavaScript and TypeScript code buffers should use the Go version of TypeScript for it's LSP.


## Some background

I didn't intend to use TypeScript V7 literally the day after release. I was just setting up Emacs for a new TypeScript project and LSP wouldn't work and just kept getting
the following error

```
 [eglot] (warning) [eglot] -32603: Request initialize failed with message: Could not find a valid TypeScript installation. Please ensure that the "typescript" dependency is installed in the workspace or that a valid ‘tsserver.path‘ is specified. Exiting.
```

After debugging it with Claude, I was told:

> No version of typescript-language-server works with TypeScript 7, and none is coming — because TS7 replaces it entirely. typescript-language-server is architecturally a thin adapter: it translates LSP into the proprietary protocol of tsserver.js, the JS-based server that TypeScript ≤5.x ships in its lib/ directory. TypeScript 7 (the Go-native rewrite) dropped tsserver.js — which is exactly why your global 7.0.2 install was rejected as "not a valid TypeScript installation." There's nothing for the adapter to adapt to.
>
> Instead, the TS7 native binary is itself an LSP server. I confirmed this against your actual install: running
>
> ```
> tsc --lsp --stdio
> ```
> and sending it an LSP initialize request got back a proper response advertising completion, hover, go-to-definition, references, code actions, rename, and so on. No wrapper needed — the Go compiler speaks LSP directly, which is how the TypeScript team intends editors to integrate from v7 onward.
