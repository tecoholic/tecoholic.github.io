---
layout: post
title: "Featured on TheNextWeb &amp; Lifehacker"
date: 2020-08-27 06:44:12
category: Projects
tags: experience js
---

Something really cool happened this week. I will let the tweets to take over.





https://twitter.com/tecoholic/status/1297860114066546688




https://twitter.com/tecoholic/status/1297934921562914818




https://twitter.com/tecoholic/status/1297946991599656961




https://twitter.com/tecoholic/status/1297964496275648512




https://twitter.com/tecoholic/status/1298150900033150976




https://twitter.com/tecoholic/status/1298598910164791298



![](/img/wp-content/uploads/2020/08/the_next_web_feature.png?w=1024)


... and that's how I made it to the homepage of TheNextWeb.
-----------------------------------------------------------







... and Lifehacker
------------------




![](/img/wp-content/uploads/2020/08/lifehacker-just-arrived.png?w=1024)



https://twitter.com/lifehacker/status/1298976636054966272



Source code of the extension: [https://github.com/tecoholic/Just-Arrived](https://github.com/tecoholic/Just-Arrived)




For Chrome: [Chrome Webstore](https://chrome.google.com/webstore/detail/just-arrived/mdfbpdpipgabflofhlkmehijmfghnimd?hl=en)




For Firefox: [https://addons.mozilla.org/en-GB/firefox/addon/just-arrived-ff/](https://addons.mozilla.org/en-GB/firefox/addon/just-arrived-ff/)




What did I learn from this?
---------------------------




The most important thing I learnt while doing this is probably the fact that the extension architecture is standardised across Chrome and Firefox. Thanks to Shrinivasan for asking me to port it to Firefox. 




But, I think the relationship is one sided. Firefox can work with extensions written for Chrome, but Chrome won't work with extensions written for Firefox. This is due to the nature of Firefox's API and the fallback it offers.




For example, the storage api on Firefox is `storage.*` whereas on Chrome it is `chrome.storage.*`. Since Firefox has fallbacks for all the `chrome.*` API, the code primarily written for Chrome works without modifications on Firefox. But if a developer writes the plugin first for Firefox, it would lose the namespacing and therefore won't work.




More technical details here at MDN web docs: [Building a cross-browser extension](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Build_a_cross_browser_extension)







Special thanks [@tshrinivasan](https://twitter.com/tshrinivasan) for pushing me to build it for Firefox to [@SuryaCEG](https://twitter.com/suryaceg) for the UX advised and [@IndianIdle](https://twitter.com/IndianIdle) for writing the article.



