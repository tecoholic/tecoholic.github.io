---
title: "Avoiding Accidental Push to Upstream"
date: 2024-09-18
slug: "avoid-accidental-push-to-upstream"
categories:
  - Notes
tags:
  - TIL
  - git
---

As anyone who works with multiple remotes in Git and has rights to many of them, I run into the issue of pushing to the wrong remote.
The main issue is I will simply use `git push origin` while a simple `git push` might be sufficient.
After trying and failing many times to get rid of this muscle memory, here are the 2 options I have come up with.


### Option 1: Don't set origin

A Git clone usually sets the remote as `origin`. I change this right after a clone to something more descriptive of the source like `upstream`.

```sh
git remote rename origin upstream
```

### Option 2: Remove the "push" URL

Git smartly stores remote URLs are 2 separate values - push and pull. So setting `push` to an invalid value, I can be certain no accidental pushes
happen in places where I might have forgotten to do Option #1 after cloning, or when I have multiple remotes and I want to disable push to some
of them.

```sh
git remote set-url --push origin no_push
```


### Bonus: Different URLs for push and pull

I have never used this. But this should be doable when there are only 2 remotes to deal with. Suppose there are `upstream` and `my-fork` remotes,
we could simply set

```sh
git remote set-url --push upstream <my-fork-push-url>
```

This should technically make sure all the pushes always end up in `my-fork` even when I accidently say `upstream`.


## Closing thoughts

I know all of these are convoluted when compared to simply typing `git push` and let git push to the correct origin for that branch or
maybe even using some CLI utility that provides git aliases like `gp`. But my fear of not knowing where I am pushing or mistyping one character
that will do something I won't be able to fix is far more than the friction of typing `git push <remote-name>` every time.
