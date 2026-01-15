---
title: 'Python Tip #4 - Find an element in a list satisfying condition'
date: '2018-09-21T21:56:46'
slug: python-tip-4
categories:
  - Coding
tags:
  - python
---

What if you want to find the first item that matches the condition instead of getting a list of items?

```python
selected = None
for i in items:
    if condition:
        selected = i
        break

# Simpler version using next()
selected = next((i for i in items if condition), None)
```

> **next()** is a built in function which is not that well known.