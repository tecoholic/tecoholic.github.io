---
title: "Python Tip #8 - reducing looping by using dicts"
date: 2018-09-27
slug: "python-tip-8"
categories:
  - PythonTips
tags:
  - python
  - coding
---

In situations where you have a list of objects and have to retrieve then in random order, dictionaries can act as lookup tables.

```python
users = list of class User 

# Get users one by one by looking up ids
user_1 = next((u for u in users if u.id == user_1_id), None)
user_2 = next((u for u in users if u.id == user_2_id), None)
...

# Simpler solution using lookup table
lookup = dict((u.id, user) for u in users)
user_1 = lookup[user_1_id]
user_2 = lookup[user_2_id]
...
```

This tip is not very obvious, hence this explanation:

```python
user_1 = next((u for u in users if u.id == user_1_id), None)
```
This method employs a iterator looping through the list of users everytime we have to find a user, which means we have to run this loop a hundred times. This poses a complexity of **O(N<sup>2</sup>)**.

```python
lookup = dict((u.id, user) for u in users)
user_1 = lookup[user_1_id]
```
This method on the other hand iterates through the users list one time and create a lookup table that we can again and again without having to iterate through the list everytime. This reduces the complexity to **O(N)** which could theoritically lead up to 10 times faster execution of the program.