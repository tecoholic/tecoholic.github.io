---
title: "Python Tip #5 - Get value from dict if key is present"
date: 2018-09-22
slug: "python-tip-5"
categories:
  - PythonTips
tags:
  - python
  - coding
---

Check for existence of a key in dictionary and retrieve its value if present.

```python
dictionary = { "key": "value" }

# checking for the presence and key and getting the value
wanted = None
if "key" in dictionary:
    wanted = dictionary["key"]

# Simpler version
wanted = dictionary.get("key", None)
```