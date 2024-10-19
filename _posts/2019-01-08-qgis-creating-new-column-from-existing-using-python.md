---
layout: post
title: "QGIS - Creating new column from existing using Python"
date: 2019-01-08 13:35:40
category: Coding
tags: python qgis
---
Yesterday, I was working on the [ward level parks map of Chennai](https://commons.wikimedia.org/wiki/File:Parks_in_Chennai_by_Wards.png) I had to join a CSV data layer with the boundary polygon layer, but there was one issue while my CSV file has the ward numbers as integers (1,2,3..etc), the polygon layer had them as strings (Ward 1, Ward 2, Ward 3 ...etc.,) So I was thinking, wouldn't it be nice just to strip the word Ward and put it in a new column, so that I can make a join by matching the ward numbers. Turns out Python integration in QGIS is so good that, I did it without even searching the internet. Here is how.

1. Open the Attribute table
2. Open Field Calculator.
3. Enter the "Output field name"
4. Switch to "Function Editor"
5. Click the [+] button to create a new function file.
6. Changed the function name, parameter and return the value after stripping "Ward " from the string. Read the docs given below the function editor to understand what's going on the file.



[caption id="attachment_614" align="alignnone" width="964"]![QGIS Field Calculator](/img/wp-content/uploads/2019/01/screenshot-2019-01-08-at-6.53.09-pm.png) QGIS Field Calculator[/caption]

```python
from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def strip_ward(name, feature, parent ):
 return name.split(" ")[-1]
```

Now switch back to the Expression tab and call the function to calculate the new field

![strip_ward.png](/img/wp-content/uploads/2019/01/strip_ward.png)

Click OK. Now the new field with the computed value would be created.

I had a simple use case, by one can use the power of Python to calculate anything from existing data and generate a new field based on it. I was really blown away by the level of Python integration in QGIS.
