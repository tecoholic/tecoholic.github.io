---
title: 'Python mock &#8211; Handling namespaces'
author: Arunmozhi
layout: post
permalink: /python-mock-handling-namespaces/
categories:
  - Coding
tags:
  - python
---
Unit testing a big python application comes with its own set of worries which includes mocking calls to parts of code which we will test somewhere else.

Let us say I have a **utils.py** (every project has one anyways)

<pre class="brush: python; light: true; title: ; notranslate" title=""># utils.py

def word_length(name):
    # here it is a trivial function
    # assume that this is a costly network/DB call
    return len(name)
</pre>

And I have another module which uses **word_length** using the **from module import function** syntax.

<pre class="brush: python; light: true; title: ; notranslate" title=""># user.py
from project.utils import word_length

def calculate(name):
    length = word_length(name)
    return length
</pre>

Now I want to unit test all the functions in **user.py** and since I am going to test just the user module and want to avoid costly calls made by my utils module I am going to mock out calls to `word_length` using Python mock library.

<pre class="brush: python; light: true; title: ; notranslate" title=""># test_user.py
from project.user import calculate

from mock import patch
 
@patch('project.utils.word_length')
def test_calculate(mock_length):
    mock_length.return_value = 10
    assert calculate('hello') == 5
</pre>

One would expect this assertion to fail because we have mocked out the word_length to return 10. But this passes and our mock is not working. Why? Because **NAMESPACE**. Here we have patched the function in the namespace utils. But we have imported the function to the user.py namespace by using `from module import function`. So we need to patch the function in the user namespace where it is used and not in the utils where it is defined. So change the line

<pre class="brush: python; light: true; title: ; notranslate" title="">@patch('project.utils.word_length')

to 

@patch('project.user.word_length')
</pre>

But what if we have used simply like

<pre class="brush: python; light: true; title: ; notranslate" title=""># user.py
import utils

def calculate(name):
    length = utils.word_length(name)
    return length
</pre>

This time we can straight away use the `@patch('project.utils.word_length')` as we are importing the entire module and namespace remains as such.