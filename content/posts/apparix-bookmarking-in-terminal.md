---
title: "'Apparix &#8211; Bookmarking in terminal'"
slug: "apparix-bookmarking-in-terminal"
---

When working in a large code base like Quantum GIS or when dealing with a lot of repositories in the machine, it is always tedious to cd all the way to the folder we require to move to. Enter apparix, an excellent linux tool I found by googling &#8220;bookmarking in the terminal&#8221;. [This blog post ][1] has the complete details of how to use it.

Yay, no longer `cd goto/project/src/core/of/module1` and again `cd ../../../test/number/three`. I can simply do

{% highlight bash %}
$ bm projectsrc
$ bm test3
$ bm fancypants4
{% endhighlight %}

to bookmark my locations and simply

{% highlight bash %}
$ to projectsrc
$ to test3
$ to fancypants4
{% endhighlight %}

One more tool added in the arsenal to improve productivity.

 [1]: http://dragly.org/2011/11/01/bookmarks-in-terminal/
