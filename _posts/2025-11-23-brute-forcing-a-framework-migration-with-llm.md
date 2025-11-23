---
title: Brute-forcing a Framework Migration with LLM
author: Arunmozhi
layout: post
categories:
  - Coding
tags:
  - coding
  - llm
---

I decided to migrate a Python Django application to FastAPI. The app was mainly serving APIs for triggering some background tasks. Whatever data it needed could be just put into configs or JSON files.

There are 2 parts to this app:

1. **The JSON API** - this is the main API. This was implemented with Pydantic Models and Django-Ninja.
2. **The Playground** - this is a set of web forms that allows the user to manually upload files to test the API.

I used Claude code in the Plan mode for it to gather all the information, ask questions and prepare a migration plan. The API was migrated pretty well. Use of Pydantic models and Django-Ninja really helped there. I am not sure if I had Django Rest Framework or something like that, it would have gone as smoothly.

But the "playground" was a mess. There is no directly equivalient to Django's Forms in FastAPI. After sometime manually editing Jinja templates, I came up with a way to get a 1:1 migration. It went like this:

* Checked out the main branch with Django
* Made Claude Code generate HTML page for all the URLs in the playground
* Switched to the FastAPI branch
* Asked Claude code to implement the playground so that the HTMLs matched functionally.

It mostly worked. It missed the CSRF token in the forms and reasoned that "FastAPI doesn't need it". I had to prod it a bit to get that implemented and now I have a 1:1 feature parity.


In all there were about 32 Django Forms being rendered on a single HTML template. Claude managed to keep the same 1 template setup working by defining the fields in Python Code. The form definitions in the Python code are not the best and will require some manual refactoring. Initially, I was thinking, I should ask Claude to generate some integration tests, and then use that as the reference to perform the migration. But, I borrowed the React's UI testing idea to generate artifacts instead. I think it is much simpler and effective solution when dealing with LLMs than writing integration tests.

