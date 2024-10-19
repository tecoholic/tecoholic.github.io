---
layout: post
title: "Back to Basics with En Kanakku"
date: 2023-04-16 16:53:12
category: Projects
tags: django personal-finance python
---

Everyday I work on a megalith of a software called Open edX as a part of my work. It is built on top of Django. But here is the thing, it is very big piece of software and most of time I am tweaking something that is one among the many layers of abstraction and business logic.




This has created a deep desire to get down to the basics and build something. I tried learning Rust. A systems language. How more basic can I get than that? But what do I do with Rust? I don't even know what kind of program I can write with that. A PDF Parser maybe? I downloaded the PDF 1.7 spec and started gathering 8 bits at a time. But Rust is not something that has the same velocity as Python or JavaScript. Understandably so. Compiled vs Interpreted.




In the meantime, something has also been really bothering me. My personal finance. Every year, I do a round up of my earnings and spends during the tax season and go over my savings. This year around, I have setup [Firefly III](https://www.firefly-iii.org) to consume my bank statement and do it a little easier.





> FireFly III is a fantastic software that made me realise a number of things I didn't know about my finances




But...
------




I needed more. I have tasted something sweet and I need more. Here are the things I wanted Firefly to have to make life easier for me




2. Native support for importing my bank statement. The Firefly Importer does its job, but I needed run an extra service for that and had to create a template for mapping the fields.

6. Native support for importing PDF Credit Card statements. A lot of the details are being missed because all the expenses for a month are reported as a single entry in the bank statement - CC Payment.

10. Automatic Categorisation of transactions. Firefly let us to set up static rules that can help do this, but I found it a little complex and I was always afraid one rule might override another and my categorisation would go for a toss.




So...
-----




Why don't I create a simple personal finance application in Python Django? I know the language and the framework. Creating something like this from scratch would allow me to get to the basics of Django. Get back to working with HTTP Responses, redirects, URL resolution, Middleware, Testing...etc., I use TDD and take help from ChatGPT to get the skeleton code.




I have also grown tired of the modern frontend development, the complexity is too much. This has helped me reset. Writing HTML in Django templates has been very cathartic. When I do need some interactivity, I plan on using [HTMX](https://htmx.org). No Webpack, No bundling, None of the 1000 things that come with it.




I know, this doesn't sound as sexy as "written in Rust". But, working on this project has been very satisfying. It allows me to revisit things that I haven't used in a long time. Build something I really want to use. And most importantly, takes me back to the basics - well at least to the basics of the abstraction layer Django provides.




The Project
-----------




The Project is named "[En Kanakku](https://github.com/tecoholic/en_kanakku)" (என் கணக்கு) which is Tamil for "My Accounts". Over the last couple of weeks, I have implemented:




* Setup the dependencies and the basic skeleton for the app

* Created a CSV Importer that can be subclassed to import transactions from any CSV file

* Used it to create an importer for the Firefly III export

* Added an admin action to merge account after the import




Now all of the transaction data I had in Firefly has been imported into En Kanakku, along with the accounts and categories. Baby steps...



