---
title: 'Python Tip #3 - Filtering Lists'
date: '2018-09-21T21:31:11'
slug: python-tip-3
categories:
  - Coding
tags:
  - python
---

Selecting elements from a list that satidfy a condition

```python
selected = []
for i in items:
    if condition:
        selected.append(i)

# Simpler version using List comprehension
selected = [i for i in items if condition]
```