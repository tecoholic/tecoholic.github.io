---
title: Python Pitfalls
author: Arunmozhi
layout: post
permalink: /python-pitfalls/
categories:
  - Coding
tags:
  - coding
  - python
---
I was woken up today with the following question:

{% highlight python %}
def foo(x=[]):
    x.append(1)
    return x

>>> foo()
>>> foo()
{% endhighlight %}

What could be the output? The answer is  

    [1]
    [1, 1]

I was stupefied for a minute before I started DuckDuckGo-ing *Python default arguments*, *Python garbage collection*, *Python pitfalls*..etc.,

These links helped me understand mutable objects&#8217; memory management.  
[Deadly Bloody Serious &#8211; Default Argument Blunders][1]  
[Udacity Wiki &#8211; Common Python Pitfalls][2]  
[Digi Wiki &#8211; Python Garbage Collection][3]

 [1]: http://www.deadlybloodyserious.com/2008/05/default-argument-blunders/
 [2]: https://www.udacity.com/wiki/common-python-pitfalls
 [3]: http://www.digi.com/wiki/developer/index.php/Python_Garbage_Collection
