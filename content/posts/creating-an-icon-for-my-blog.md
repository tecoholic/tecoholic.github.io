---
title: "Creating an Icon for my blog"
date: 2018-11-25T04:04:41
slug: "creating-an-icon-for-my-blog"
categories:
  - Projects
tags:
  - idea
  - python
---

When I moved the site from Jekyll to Wordpress, I was asked to create a site icon by Wordpress. I was trying to play around with the letter from "t" from my screen name "tecoholic" in a couple of Vector editors using different fonts, handrawn symbols ...etc., and finally landed on what I know best. Write a Python script for it. So here it is, my blog icon and the generator. It is just a stacking of "T"s but somehoe looks like the corner of ancient Chinese houses.

```python
#!/usr/bin/env python
"""
A script to generate SVG icon for the personal blog.
"""
import svgwrite

width = 256
height = 256
mtop = mbottom = mright = mleft = 256/8

dwg = svgwrite.Drawing(filename="blog_icon.svg", size=(height, width))

def draw_pattern(width, color):
 xpos = 256/8 + mleft
 ypos = 256/8
 increment = 256*2/8
 vlines = dwg.add(dwg.g(id="vlines", stroke=color, stroke_width=width, stroke_linecap="round"))
 hlines = dwg.add(dwg.g(id="vlines", stroke=color, stroke_width=width, stroke_linecap="round"))
 while (xpos < 256*7/8):
 vlines.add(dwg.line(start=(xpos,ypos), end=(xpos, 256 - mbottom)))
 hlines.add(dwg.line(start=(mleft, ypos), end=(xpos+mright, ypos)))
 xpos += increment
 ypos += increment

draw_pattern(20, "black")
draw_pattern(8, "white")

dwg.save(pretty=True)
```

That creates the SVG, then it is just using `imagemagick` to create png files of all required sizes:

```bash
#!/usr/bin/env bash
python blog_icon_generator.py
convert -background none blog_icon.svg blogo_256.png
convert -background none -resize 512x512 blog_icon.svg blogo_512.png
convert -background none -resize 128x128 blog_icon.svg blogo_128.png
convert -background none -resize 64x64 blog_icon.svg blogo_64.png
convert -background none -resize 32x32 blog_icon.svg blogo_32.png
```

![blogo_256](/img/wp-content/uploads/2018/11/blogo_256.png)
