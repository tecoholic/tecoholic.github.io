---
title: Zimbalaka - Zim file creator for Offline Wikipedia
date: '2015-05-15T11:40:09'
slug: zimbalaka-an-openzim-creator
categories:
  - Projects
tags:
  - Coding
  - python
  - wikipedia
---

OpenZim is a Wikimedia developed format for offline reading of Wikipedia. Read more [here][1]. But the project was sadly sidelined and the support from MediaWiki, the software that runs Wikipedia sites, was also removed.

I came to know about all this from Bala Jeyaraman of [Vasippu][2]. He is planning to introduce tablets in a classroom of 6th standard students, with exceptional comprehension levels compared to average Indian classrooms, and wanted a way to load select material into the tablets. The OpenZim files have an excellent reading app called [Kiwix][3], which also offers complete Wiki sites as downloads. Tablets can&#8217;t afford to have huge amount of data, like full Wikipedia. There is no way to create a zim file with select topics. Once has to request the OpenZim team to do it for him/her.

## Enter Zimbalaka

[Zimbalaka][4] is a project which tries to solve just that. It creates offline wikipedia content files in zim file format. A person can input a list of pages that needs to be created as a zim, or at least a wikipedia category. Then Zimbalaka downloads those pages, removes all the clutter like, sidebar, toolbox, edit links &#8230;etc., and gives a cleaned version as a zim file for download. It can be opened in Kiwix. 

The zim is created with a simple welcome page with all the pages as a list of links. The openzim format also has an inbuilt search index and Kiwix uses this really well. So you can create zims of 100 articles and still navigate to them easily either way.

Zimbalaka has multi-lingual and multi-site support. That is, you can create a zim file from pages of any language of the 280+ exiting Wikipedias, and also from sites like WikiBooks, Wiktionary, Wikiversity and such. You can even input any custom url like `http://sub.domain.com/`, Zimblaka would add `/wiki/Page_title` to it and download the pages.

It is currently hosted by my good friend Srikanth (<a href="https://twitter.com/logic" target="_blank">@logic</a>) at <a href="http://srik.me/zimbalaka" target="_blank">http://srik.me/zimbalaka</a>

### Screenshots

Here is how the content looks in <a href="https://play.google.com/store/apps/details?id=org.kiwix.kiwixmobile" target="_blank">Kiwix for Android</a>. 

![Navigation in Kiwix](/img/uploads/2015/05/navigate.png)
![Multi Site and Language Support](/img/uploads/2015/05/multi.png)

### Pain points

  * A small pain point is that, Zimbalaka also strips the external references that occur at the end of the Wikipedia articles, as I didn&#8217;t find it useful in an offline setup.
  * You cannot add a custom Welcome page in the zim file. Not a very big priority. The current file does its work of listing all the pages
  * You cannot include pages from multiple sites as a single zim file. The workaround is to create multiple files or use a tool called <a href="https://sourceforge.net/p/kiwix/other/ci/master/tree/zimwriterfs/" target="_blank">zimwriterfs</a>, which has to be compiled from source (this is used by zimbalaka behind the scenes).

### Developers

This tool is written using Flask &#8211; A simple Python web framework for the backend, Bootstrap as the frontend and uses the zimwriterfs compiled binary as the workhorse. The zimming tasks are run by Celery, which has been automated by supervisord. All the co-ordination and message passing happens via Redis. 

Do you want to peek in how it is all done? Here is the source code <a href="https://github.com/tecoholic/Zimbalaka" target="_blank">https://github.com/tecoholic/Zimbalaka</a>. Feel free to fork, modify and host your own instance.

### Update

The OpenZim team has appreciated the effort I had put in and offered to host the tool on their server at <http://zimbalaka.openzim.org>. They have also pointed me to a desired backend called &#8216;mwoffliner&#8217; that they have developed to download and clean the html. I will be working on it in my free time.

 [1]: http://www.openzim.org
 [2]: http://www.vasippu.org
 [3]: http://www.kiwix.org
 [4]: http://srik.me/zimbalaka/
 [5]: http://www.arunmozhi.in/wp-content/uploads/2015/05/navigate.png
 [6]: http://www.arunmozhi.in/wp-content/uploads/2015/05/multi.png
