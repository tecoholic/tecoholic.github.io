---
title: 'Apparix &#8211; Bookmarking in terminal'
author: Arunmozhi
layout: post
permalink: /apparix-bookmarking-in-terminal/
categories:
  - Coding
tags:
  - coding
---
When working in a large code base like Quantum GIS or when dealing with a lot of repositories in the machine, it is always tedious to cd all the way to the folder we require to move to. Enter apparix, an excellent linux tool I found by googling &#8220;bookmarking in the terminal&#8221;. [This blog post ][1] has the complete details of how to use it.

Yay, no longer cd goto/project/src/core/of/module1 and again cd ../../../test/number/three. I can simply do

<div class="highlight">
  <pre><span class="nv">$ </span>bm projectsrc
<span class="nv">$ </span>bm test3
<span class="nv">$ </span>bm fancypants4
</pre>
</div>

to bookmark my locations and simply

<div class="highlight">
  <pre><span class="nv">$ </span>to projectsrc
<span class="nv">$ </span>to test3
<span class="nv">$ </span>to fancypants4
</pre>
</div>

One more tool added in the arsenal to improve productivity.

 [1]: http://dragly.org/2011/11/01/bookmarks-in-terminal/