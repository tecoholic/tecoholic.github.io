---
title: 'Python Tip #9 - sorting'
date: '2018-10-01T19:09:42'
slug: python-tip-9
categories:
  - Coding
tags:
  - python
---

Sorting is simplified in Python with sorted(). You can even sort with complex rules.

```python
>>> strings = ['alice', 'bob', 'donald', 'cathy']
>>> sorted(strings)
['alice', 'bob', 'cathy', 'donald']

>>> sorted(strings, key=len)
['bob', 'alice', 'cathy', 'donald']

>>> def secondchar(word):
...    return word[1]

>>> sorted(strings, key=secondchar)
['cathy', 'alice', 'bob', 'donald']
```