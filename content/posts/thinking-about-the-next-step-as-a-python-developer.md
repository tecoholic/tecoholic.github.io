---
title: Thinking about the next step as a Python Developer
date: '2020-06-15T18:00:15'
slug: thinking-about-the-next-step-as-a-python-developer
categories:
  - General
tags:
  - python
  - thought
---

**Disclaimer:** The analysis is not a bullet proof analysis. Despite writing code, and throwing around numbers, this might still be a random observation. Stack Overflow Job board is a not an indicator of everything. So take everything with a pinch of salt.

Python or Full Stack?
---------------------



As someone who identifies as a Python Developer and uses Python as the primary language for programming, thinking about what to learn next is confusing. I primarily do "Full Stack development", that is write backend API in Python Flask/Django and use modern JS (React/Vue) for the frontend. But recently I am seeing a disconnect between the idea of "Python Developer" and "Full Stack Developer" in the job postings. Full Stack development seems to be defined more or less synonymous to JS development. Python Job postings on the other hand are more closer to dev ops, systems development, data analytics and machine learning.

A simple experiment
-------------------



So, I devised a simple experiment to verify what I seeing is in fact something of a trend and not a random observation. Look at the job postings on Stack Overflow for skill demand and use that as an indicator.

* Go to Stack Overflow Jobs
* Set the "Tech you like" to `node.js` - **139**
* Set the "Tech you like" to `django` + `flask` - **61**
* Set the "Tech you like" to `python` and "Tech you don't like" to `django`+`flask` - **266**



> huh, what?



Web Development in NodeJS is more in demand than Web Development in Python and Python's general purpose demand is way more higher than Python Web Development.

*For the sake of simplicity, I have considered Django + Flask as the entire Python Web development.*

Okay, so my observations and confusion about "Full Stack Development" becoming more and more Node.js development is in fact valid and I wasn't imagining it.

What's up with Python?
----------------------



Now I was intrigued with finding out what's happening to Python. What are those 266 other listings? Where is the demand for Python coming from? Also, I am getting a little worried about continuing as a Full Stack (Python) Developer. To get a better idea of the situation, I downloaded the RSS Feed of the Job postings for Python + NodeJS, extracted the categories for each posting and created a map of the 30 most mentioned categories.

![Selection_022](/img/wp-content/uploads/2020/06/selection_022.png)

Each Job posting is a row with the top 30 categories as columns. If a job positing falls under a category, it is marked 1, otherwise zero. Then I created a heatmap of the correlation matrix of the table, which will tell me how the technologies are related to each other.

![heatmap](/img/wp-content/uploads/2020/06/heatmap.png)

Anything that has a positive correlation has the value printed in green. Armed with this data, we can make a few observations:

1. REST and API are not correlated to Python, but to NodeJS
2. Event Flask and Django are not correlated to REST API
3. Python is associated with system languages like C, C++, and Java more than web technologies.
4. Flask is associated with more technologies than Django. Especially to Micro-Services technologies like Docker and Kubernetes.


### Predictions


1. General purpose Python web development will probably go the way of Ruby-on-Rails.
2. Python Web development's growth will increasingly come from micro-services and API systems which will sit on top of Machine Learning / AI based services.
3. PHP, .Net, Java all have their own full-stack definitions and job postings, but I think NodeJS will continue dominate this term.


Final Thoughts
--------------



Identifying the next thing to learn for a Python Developer doing Full Stack Development means identifying the area of focus. Taking the time to retool in Node.JS might be as good a choice as learning micro services architecture with a bit of DevOps or learning Data Science and ML. Picking a path and moving ahead is looking more of a necessity at this point.

And I am left wondering which path to choose.
