---
title: "Personal Bookmarking using YACY & yacy-it"
date: 2022-06-27T08:06:09
slug: "personal-bookmarking-using-yacy-yacy-it"
categories:
  - Projects
tags:
  - bookmarking
  - internet
  - search
  - technology
---

A recent post on HackerNews titled [Ask HN: Does anybody still use bookmarking services?](https://news.ycombinator.com/item?id=31848210) caught my attention. Specifically, the top response which mentioned a distributed Search Engine YACY. 




The author of the post mentions how, he has configured it to be a standalone personal search engine. The workflow is something like this:




1. Browse the web
2. Come across an interesting link that you need to bookmark
3. Add the URL to the YACY Crawler and crawl to the depth=0, which crawls just that page and indexes it.
4. Next time you need it, just search for any word that might be present on the page.




This is brilliant, because, I don't have to spend time putting it the right folder (like in browser bookmark) or tagging it with right keywords (as I do in Notion collections). The full text indexing takes care of this automatically.




But, I do have to spend time adding the URL to the YACY Crawler. The user actions are:




* I have to open `http://localhost:8090/CrawlStartSite.html`
* Copy the URL of the page I need to bookmark
* Paste it in the Crawling page and start the crawler
* Close the Tab.




Now, this is high friction. The mental load saved by not tagging a bookmark is easily eaten away by doing all of the above.




**yacy-it**
------------




Since I like the YACY functionality so much, I decided I will reduce the friction by writing a Firefox Browser Extension - [https://github.com/tecoholic/yacy-it](https://github.com/tecoholic/yacy-it)




This extension uses the [YACY API](https://wiki.yacy.net/index.php/Dev:APICrawler) to start crawling of the current tab's URL which I click the extension's icon next to the address bar.




[![](/img/wp-content/uploads/2022/06/get-the-addon.png?w=172)](https://addons.mozilla.org/en-US/firefox/addon/yacy-it/)


**Note:** If you notice error messages when using the addon, you might have to configure YaCy for CORS headers as described here [https://github.com/tecoholic/yacy-it#configuring-yacy](https://github.com/tecoholic/yacy-it#configuring-yacy)




![](/img/wp-content/uploads/2022/07/screenshot.png?w=523)

Add pages to YaCy index directly from the address bar




![](/img/wp-content/uploads/2022/07/selection_048.png?w=840)

Right-click on a Link and add it to YaCy Index




![](/img/wp-content/uploads/2022/07/yacy-it-preferences.png?w=716)

If you running YaCy on the cloud or in a different computer on the network, set it in the Extension Preferences




**Tip** - Search your bookmarks directly from the address bar
--------------------------------------------------------------




You can search through YaCy indexed links from your addressbar by added the YaCy as a search engine in Firefox as describe here => https://community.searchlab.eu/t/adding-yacy-to-firefox-search-menue/95




1. Go to **Setting/Preferences** => **Search** and select "**Add search bar in toolbar**"
2. Now Go to the YaCy homepage at http://localhost:8090
3. Click the "Lens" icon to open the list of search engines
4. This should now show the YaCy icon with a tiny + icon. Click that to add it as a search engine.
5. Go back to search settings and select "**Use the address bar for search and navigation**" to hide the search box
6. Scroll down to **Search shortcuts** -> double click the **Keyword** column next to the Yacy and enter a keyword eg., `@yacy` or `@bm`
7. Now you can search Yacy from the address bar like `@yacy <keyword>` or `@bm <keyword>` to look through your bookmarks.



