---
title: "Python Technical Interview - An Experience"
date: 2019-01-23T05:41:37
slug: "python-technical-interview-an-experience"
categories:
  - Coding
tags:
  - documentation
  - experience
  - python
---

As a freelancer one of the things that comes with getting a project/job is handling technical interviews. I have so far managed to convince the client with a work sample, test project ...etc., This is literally the first time I sat for a full technical interview. And it did teach a few lessons. Let me document it for future use.

It started off with the basic of the language:

#### 1. What is the difference between an iterable and an iterator?



Vincent Driessen provides a clear explanation of the difference with the examples here https://nvie.com/posts/iterators-vs-generators/

As an aside, he has a number of posts which are really great like his Git workflow model that I have used in my projects. Bookmark it

#### 2. What is a Context Manager? What is its purpose? How is it different from a try...finally block? Why would you use one over another?



Context Manager are functions/classes that allow us to allocate and release resources as required. Used with the `with` keyword in code.

The difference between context manager and `try..finally` block is explained in technical detail here: https://stackoverflow.com/questions/26096435/is-python-with-statement-exactly-equivalent-to-a-try-except-finally-bloc

But a simpler more practical difference is given by Dan Bader: https://dbader.org/blog/python-context-managers-and-with-statement

#### 3. Can you tell me some advantages of Python over other languages?



I rambled something like, it is is easier to read and write. The file structure (I should have said modules/packages) is great. Even modern iterations of Javascript are copying the `import` `from` syntax. Native implementation of a lot of things in standard library...etc.,et.,

But the thing my interviewer was looking for were the words "automatic garbage collection" because the next question was

#### 4. How does Python handle memory?



Python has automated memory management and garbage collection.That is why we never worry about how much memory we are allocating like C's `malloc` `calloc functions.

#### 5. Do you know how Python does that? Do you know about GIL?


*sheepish smiles and saying no's ensued*. I ran into an issue a few months back, I think maybe with a DB connection issue or something which led me on a rabbit hole that ended with GIL. I should have learnt it that day.

Anyway, here is the article about Python's memory management. https://realpython.com/python-memory-management/

#### 6. Have you worked on projects involving multi-threading? What do you know about multi-threading?



I hadn't. Someday maybe I will.

#### 7. Can you explain in detail the steps involved in a form submit to response cycle in detail?



https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Sending_and_retrieving_form_data

#### 8. How does the browser know where your server is when the information is submitted to a particular URL?



DNS servers - IP resolution

#### 9. The server sends back text as a string how do you see colorful information in browser?



The text is converted into DOM elements which are rendered by the browsers rendering engine.

#### 10. If a browser is showing unreadable character and question marks instead of displaying the information what could be the reason?



Document Encoding mismatch. The server might send the data encoded in Unicode UTF-8 and the browser might be decoding it as ASCII or LATIN-1 resulting in weird characters and question marks being rendered in the browser.

#### 11. You said Unicode and UTF-8 what is the difference?



Unicode is the term used to describe the character set. If it is encoded with 8 bits it is called UTF-8, if encoded with 16 bits it is called UTF-16 etc.,

For deep dive into Unicode (a must): https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/

#### 12. What kind of request does the browser make to a server? And what are the types of requests that can be made?



Browsers make a HTTP requests. The types are GET, POST, PUT, DELETE, HEAD, OPTIONS ..etc., (I think I said UPDATE instead of PUT, silly)

#### 13. What is the difference between `==` and `===` in JavaScript?



StackOverflow: https://stackoverflow.com/questions/523643/difference-between-and-in-javascript

Some other questions, that were asked:
1. Do you know Docker? Have you used AWS?
2. Do you know Data Base schema design?
3. You have a SQL query that takes a long time to execute. How would you begin to make it faster? Do you know about Query optimisation and execution plans?
