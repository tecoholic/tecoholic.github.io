---
title: 'Thattachu &#8211; Open Source Typing Tutor'
author: Arunmozhi
layout: post
permalink: /thattachu-open-source-typing-tutor/
categories:
  - Projects
tags:
  - coding
  - documentation
  - github
  - society
  - wikipedia
---
Typing tutor is a known ancient domain to work on. There are a number of places online/offline, tangible/intangible places to learn typing. But [Srikanth (@logic)][1] stumbled on a peculiar problem when worked for the [Wikimedia Language Engineering team][2]. The new age Indic input methods involved in computers seem to have no place to learn how to type on them. The only way seems to be &#8211; have a visual reference for the layout and begin typing one key at a time. This might be the most inefficient method of learning to input information. So what do we do?

## Enter Thattachu

Thattachu is an open source typing tutor. It is built using the tool that[ Wikimedia Language Engineering Team][2] have developed called jQuery IME. [jquery.ime][3] currently supports 62 languages and 150+ input methods. This is a JavaScript library which can be used on any web page. So we (I & Srikanth) set out to build a generic typing tutor which could employ any of the 62 languages or 150+ input methods. The project was conceived in May 2014 and was worked on only by May 2015 as I was busy with my Teach For India Fellowship. Thattachu borrows its tutor style from [GNU Typist][4] or gTypist which I used to learn touch typing in English. 

#### Interface

Thattachu has three pages:

  1. **Home page** &#8211; A welcome page for those visiting the site and explaining what it is about.  
    <div id="attachment_377" style="width: 1376px" class="wp-caption aligncenter">
      <img src="http://www.arunmozhi.in/wp-content/uploads/2015/06/Thattachu_page1.png" alt="Welcome Page image" width="1366" height="637" class="size-full wp-image-377" />
      
      <p class="wp-caption-text">
        Welcome Page
      </p>
    </div>

  2. **Course Selector** &#8211; A place where you choose the course to learn. You select the language and the input method you want to learn and it lists the available courses.  
    <div id="attachment_378" style="width: 1372px" class="wp-caption aligncenter">
      <img src="http://www.arunmozhi.in/wp-content/uploads/2015/06/Thattachu_page2.png" alt="Course Selector image" width="1362" height="624" class="size-full wp-image-378" />
      
      <p class="wp-caption-text">
        Course Selector
      </p>
    </div>

  3. **Workbench** &#8211; A place where you practice typing. When you select a course in the Course Selector, the workbench loads with the course you selected and you can begin typing with the input method you chose. It remembers your most recent course and lesson so you can continue from where left it the previous session.  
    <div id="attachment_379" style="width: 1370px" class="wp-caption aligncenter">
      <img src="http://www.arunmozhi.in/wp-content/uploads/2015/06/Thattachu_page3.png" alt="Workbench Page" width="1360" height="632" class="size-full wp-image-379" />
      
      <p class="wp-caption-text">
        Workbench
      </p>
    </div>

#### Course Structure

Each language has a set of input methods &#8211; each input method has a set of courses. The courses are classified based on their difficulty as &#8220;Beginner&#8221;, &#8220;Intermediate&#8221; and &#8220;Expert&#8221;. Each course has a set of lessons to complete and and each lesson is a collection of lines that have to be typed.  


<div id="attachment_380" style="width: 675px" class="wp-caption aligncenter">
  <img src="http://www.arunmozhi.in/wp-content/uploads/2015/06/thattachu_courses.png" alt="Course Structure Diagram" width="665" height="339" class="size-full wp-image-380" />
  
  <p class="wp-caption-text">
    Course Structure
  </p>
</div>

### Thattachu Asiriyar

Creating the tool is the easier part of a content dependent system. The real work is generating the content that the tool can be used with. That way we faced the challenge of creating course.JSON files required for the tool. Hence a user friendly tool [Thattachu Asiriyar][5] was born.

Thattachu Asiriyar lets anyone author a course and generate a course file. If you want to author courses, go to [Thattachu Asiriyar][5] create the course file and mail it to   
`arun [at] arunmozhi [dot] in` -mentioning &#8220;Thattachu course&#8221; in the subject.

#### Github savvy authors

Or if you have a Github account and know about pull requests. Kindly

  1. Fork the [Thattachu repo][6]
  2. Put the course file into the data/language_code folder
  3. Update the courselist.json in your folder with the metadata and the filename
  4. Send me a pull request.
  5. Feel awesome for helping the humanity learn typing

### Developers

Here are a few points for those interested in the code or those who think they can improve Thattachu.

  * Thattachu is a web application written in HTML and JavaScript (AngularJS).
  * It is a completely static site with all the information stored as JSON files and served by XHR requests when requested by the Angular $http.
  * For input [jQuery.ime][7] is used.
  * It is a completely static site and can be hosted in any web server.
  * It uses localStorage of the user to track last worked on course and load it when the user opens the page next time.

 [1]: https://twitter.com/logic
 [2]: https://www.mediawiki.org/wiki/Wikimedia_Language_engineering
 [3]: https://github.com/wikimedia/jquery.ime
 [4]: https://www.gnu.org/software/gtypist/
 [5]: http://www.srik.me/asiriyar/
 [6]: https://github.com/tecoholic/thattachu
 [7]: https://github.com/wikimedia/jquery.ime/