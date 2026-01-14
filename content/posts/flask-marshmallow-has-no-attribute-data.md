---
title: "Flask Marshmallow - has no attribute data"
date: 2019-09-18T02:29:19
slug: "flask-marshmallow-has-no-attribute-data"
categories:
  - Coding
tags:
  - python
---

*TL,DR-*

> Remove `.data` after the `schema.dump()` calls in the code. Marshmallow 3 supplies the data directly.


### The Issue



If you use [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) in your Flask application for serialisation of models, then there are chances that you will run into this error when you upgrade dependencies. The reason for this issue is Flask Marshmallow has added support for Marshmallow 3 when moving from version `0.10.0` to `0.10.1`. And Marshmallow 3 returns the data directly when the `dump` function is called instead of creating an object with the `.data` attribute.

### The solution



This is a breaking change and requires the codebase to be updated. **Remove all .data accessors from the dump() outputs.** For example:

```py
users = user_schema.dump(query_result, many=True).data

# Will become

users = user_schema.dump(query_result, many=True)
```

### Some thoughts



I don't know why such a big support change is released as a bug fix version `0.10.0` to `0.10.1`. It at least should be released as `0.11` in my opinion. If I could go further I would say wrappers for libraries or software in general should always follow the parent's version number to the minor version. If Marshmallow is in 3.2.x then it makes sense for Flask-Marshmallow to be in 3.2.x. That provides a better idea of what we are using and what are the changes we need to account for.
