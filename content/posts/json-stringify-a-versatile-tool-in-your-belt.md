---
title: JSON.stringify - A versatile tool in your belt
date: '2020-02-05T10:00:02'
slug: json-stringify-a-versatile-tool-in-your-belt
categories:
  - Coding
tags:
  - js
---

A common scenario that we run into when writing JavaScript for the browser is showing a variable as text on the screen. JS has an inbuilt function to achieve that quite easily. Just us the `toString()` function. Here is an example:

```js
var i = 10
i.toString()

"10"
```

Where this falls short is when the variable is an object. Trying the same:

```js
var name = {"first": "Tom", "last": "Hardy"}
name.toString()

"[object Object]"
```

Here is where `JSON.stringify` comes in handy.

```js
var name2 = {"first": "Tom", "last": "Hardy"}
JSON.stringify(name2)

"{"first":"Tom","last":"Hardy"}"
```
