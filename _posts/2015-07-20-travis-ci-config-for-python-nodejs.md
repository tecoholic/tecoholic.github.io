---
title: Travis CI config for Python + NodeJS
author: Arunmozhi
layout: post
permalink: /travis-ci-config-for-python-nodejs/
categories:
  - Coding
tags:
  - python
---
I currently work with the [Gluu Federation][1] &#8211; an open source company. My present job is to build a Web UI for the cluster management using the available API. 

We use Python Flask for the Backend and AngularJS+Bootstrap for the Frontend. Pretty much a standard affair these days. Testing is crucial and we have the backend tests in Python Nose and the Frontend Unit tests using Karma and Jasmine running on NodeJS.

Now the question is how does one configure the Travis CI .yml file to perform tests in a both Python and Javascript. I initially set up using `language: node_js` and ran only the frontend tests. Then I went around searching and stumbled on [travis-ci &#8211; issue#4090 &#8211; Support multiple languages][2]. Thanks to the tip from [@BanzaiMan][3] I now have both frontend and backend tests running with a simple yml file.

 [1]: http://www.gluu.org
 [2]: https://github.com/travis-ci/travis-ci/issues/4090
 [3]: https://github.com/BanzaiMan
