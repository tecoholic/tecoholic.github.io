---
title: Unit Testing with CasperJS
date: '2015-01-15T23:20:37'
slug: unit-testing-with-casperjs
categories:
  - Coding
tags:
  - github
---

Today I sat down to create a JavaScript library. I wanted to do it the way I have long dreamed of &#8211; TDD (Test Driven Development). There is no dearth of Unit testing libraries and frameworks for JavaScript, so after some reading on the internet settled on CasperJS and PhantomJS combination. CasperJS is just awesome for functional testing, but Unit testing? Even though it supports Unit Testing, it as such is not a dedicated unit testing frameowrk like [Karma][1] or [Protractor][2]. [Read this][3] for more information on TTD frameworks for JS libraries.

Loading plain JavaScript files in CasperJS for unit testing seems to be completely undocumented. I tend to think it is because it wasn&#8217;t meant to be webpage-less. But the note on [docs of tester module][4] says:

> The best way to learn how to use the Tester API and see it in action is probably to have a look at CasperJS’ own test suites.

Thanks for this quote, I found that using the `fs` module one can load local filesystem files as modules to be used. Using that now I could write unit tests while developing the library and later on write functional tests while using the library.

Here is the file structure  

```bash
library
--test
  |--unit
     |--test.js
     |--index.html
--src
  |--livetransit.js
```

And here is are the two tests &#8211; i) uses a webpage based approach; ii) uses module approach

 [1]: http://karma-runner.github.io/ "Karma"
 [2]: http://angular.github.io/protractor/#/ "Protractor"
 [3]: http://stackoverflow.com/questions/300855/javascript-unit-test-tools-for-tdd "StackOverflow TDD frameworks for JS"
 [4]: http://docs.casperjs.org/en/latest/modules/tester.html "CasperJS tester module"
