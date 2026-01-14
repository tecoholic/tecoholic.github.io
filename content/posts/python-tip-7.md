---
title: "Python Tip #7 - getattr()"
date: 2018-09-25
slug: "python-tip-7"
categories:
  - PythonTips
tags:
  - python
  - coding
---

Sometimes we have to deal with external objects and their attributes. getattr() can save you at those times.

```python
# Get the attribute name
name = obj.name  # AttributeError if name is not present

# Check if the attribute is present before fetching
try:
    name = obj.name
except AttributeError:
    name = "Guest"

# Simpler solution
name = obj.name if hasattr(obj, "name") else "Guest"

# Simplest Solution
name = getattr(obj, "name", "Guest")
```