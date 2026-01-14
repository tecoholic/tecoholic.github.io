---
title: "Python Gotcha #1: Extended Assignment Operator and Lists"
date: "2018-05-30T08:23:31+05:30"
slug: "python-gotcha-1-extended-assignment-operator-and-lists"
categories:
  - Coding
tags:
  - python
  - coding
---

*Extended Assignment Operators* - we use them all the time as shorthands for assigning values.
Lets see how this works when using multiple identifiers (variables) in terms of simple data like a number.

```python
>>> a = 5
>>> b = a
>>> b += 3
>>> print(a)
5
>>> print(b)  # only the value of b is changed even though we have assigned a to b
8
>>> b = b+4  # the long form assignment also doesn't affect the original a
>>> print(b)
12
>>> print(a)  
5
```

### Gotcha

Let us apply a similar set of operations on `list`

```python
>>> a = [1,2,3]
>>> b = a
>>> b += [4,5]
>>> print(a)  # surprise! - changing the value of b also affect the value of a
[1, 2, 3, 4, 5]
>>> print(b)
[1, 2, 3, 4, 5]
>>> b = b+[6,7]
>>> print(b)
[1, 2, 3, 4, 5, 6, 7]
>>> print(a)
[1, 2, 3, 4, 5]  # surprise again !! - but assigning a new value to b doesn't
```

### Takeaway

Now the question is, why does the value of `a` change when adding elements to `b`?
And furthermore why doesn't it change when we do it using the long form?

The answer is: Extended assignment operators act differently on *mutable* and *immutable* values.
So when we say `b += [4,5]` we are basically saying add 4 and 5 to the list b, but when we say
`b = b + [6,7]`, we are saying "take the list b, add 6, 7 to it and **create a new list** from it, then assign it to the identifier b".

This subtle difference will come to bite us when we least expect it. So be aware and take precautions :)
