---
title: "Installing gluu-flask requirements.txt on Mac"
slug: "installing-gluu-flask-requirements"
categories:
  - General
tags:
  - programming
  - notes
---

Installing the `requirements.txt` of the [gluu-flask](https://github.com/GluuFederation/gluu-flask) is always a chore because of some or the other bug that crops up with the Swig related compilation of M2Crypto library.

After a clean install of homebrew on El Capitan on the Mac, the version incompatibility issues disappeared, but still there needs to be some workaround to set this up.

```bash
# set up the pre requisites
$ brew install python
$ brew install swig
$ brew install openssl
$ pip install virtualenv

# now git clone the repo
$ cd /some/where/gluu-flask
$ virtualenv env
$ source env/bin/activate
$ env LDFLAGS="-L$(brew --prefix openssl)/lib" \
> CFLAGS="-I$(brew --prefix openssl)/include" \
> SWIG_FEATURES="-cpperraswarn -includeall -I$(brew --prefix openssl)/include" \
> pip install -r requirements.txt
```
