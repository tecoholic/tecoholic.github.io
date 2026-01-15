---
title: Two Days with Python & GraphQL
date: '2019-12-21T20:49:10'
slug: two-days-with-python-graphql
categories:
  - Coding
tags:
  - apollo
  - experience
  - graphql
  - js
  - python
  - vue
---

Background
----------



An web application needed to be built. An external API will give me a list of information packets as JSON. The JSON has the information and the user object. The application's job is to store this data in a local database and provide an user interface to sort and filter this data. Simple enough.

GraphQL kept coming up on on the internet. A number of tools were saying they support GraphQL in their home pages and was making me curious. The requirement also said:


> use the technology of your choice REST/GraphQL to build the backend



Now, I had to see what's it all about. So I sat down read the docs and got a basic understanding of it. It made total sense theoretically. It solved a major problem I face when building Single Page Applications and the Backed REST APIs independently. The opaqueness of incoming data and the right method to get them.

### Common Scenario I run into



While building the frontend, we assume use the schema that the backend people give as the source of truth and build it based on that. But the schema becomes stale after a while and changes need to be made. There are many reasons to it:

* adding/removal/renaming of an attribute
* optimisations that come into play, which alter the structure
* the backend API is a third party one and searching and sorting are involved
* API version changes
* access control which restricts the information contained..etc.,



And even when we have a stable API, there is the issue of information leak. When you working with user roles, it becomes very confusing very quickly because a request to `/user/` returns different objects based on the role of the requester. Admin sees different set of information than a privileged user and a privileged user sees a different set of data than an unprivileged one.

And more often than not, there is a lot of unwanted information that get dumped by APIs on to the frontend than what is required, which sometimes even lead to security issues. If you want to see API response overload take a look under the hood of Twitter web app for example, the API responses have a lot more information than what we see on screen.

![Twitter_API_Response](/img/wp-content/uploads/2019/12/twitter_api_response.png)
### Enter GraphQL



GraphQL basically said to me, let's streamline this process a little bit. First we will stop maintaining resource specific URLs, we are going to just send all our requests to `/graphql` and that's it. We won't be at the mercy of the backend developers whim's and fancies about how to construct the URL. No more confusing between `/course/course_id/lesson/lesson_id/assignments` and `/assignments?course=course_id&lesson=lesson_id`. Next, no, we are not going to use HTTP verbs, everything is just a POST request. And finally no more information overload, you get only what you ask. If you want 3 attributes, then you ask 3, if you want 5 then you ask 5. Let us eliminate the ambiguity and describe what you want as a Graphql document and post it. I mean, I have been sick of seeing `SomeObject.someAttribute is undefined` errors. So I was willing to put in the effort to define my requests clearly even it meant a little book keeping. Now I will know the exact attributes that I am going to work with. I could filter, sort, paginate all just by defining a query.

It was a breath of fresh air for me. After some hands on experiments I was hooked. This simple app with two types of objects were the perfect candidate to get some experience on the subject.

Day/Iteration 1 - Getting the basic pipeline working
-----------------------------------------------------



The first iteration went pretty smooth. I found a library called [Graphene - Python](https://graphene-python.org/) that implemented GraphQL for Python with support for SQLAlchemy, I added it to Flask with Flask-GraphQL and in almost no time I had a API up and running that will get me the objects, and it came with sorting and pagination. It was wonderful. I was a little confused initially, because, Graphene implements the [Relay spec](https://relay.dev/docs/en/graphql-server-specification). So my queries looked a little over defined with `edges` and `nodes` than plain ones. I just worked with it. I read a quick intro about Connections and realised I didn't need to worry about it, as I was going to be just querying one object. Whatever implications it had, it was for complex relations.

For the frontend, I added Vue-Apollo the app and I wrote my basic query and the application was displaying data on the web page in no time. It has replaced both Vuex state management and Axios HTTP library in one swoop.

And to help with query designing, there was a helpful auto completing UI called GraphIQL, which was wonderful.

Day/Iteration 2 - Getting search working
-----------------------------------------



Graphene came with sorting and filtering inbuilt. But the filtering is only available if you use Django as it uses `django-filter` underneath. For SQLAlchemy and Flask, it only offers some **tips**. Thankfully there was a library called [Graphene-SQLAlchemy-Filter](https://pypi.org/project/graphene-sqlalchemy-filter/) which solved this exact problem. I added that and voila, we have a searchable API.

When trying to implement searching in frontend is where things started going sideways. I have to query all the data when loading the page. So the query looked something like

```js
query queryName {
 objectINeeded {
 edges {
 nodes {
 id
 attribute_1
 attribute_2
 }
 }
 }
}
```

And in order to search for something, I needed to do:

```js
query queryName {
 objectINeeded(filters: { attribute_1: "filter_value" }) {
 ...
}
```

And to sort it would change to:

```js
query queryName {
 objectINeeded(sort: ATTRIBUTE_1_ASC, filters: { attribute_1: "filter_value" }) {
 ...
}
```

That's okay for predefined values of sorting and filtering, what if I wanted to do it based on the user input.

### 1. Sorting



If you notice closely, the sort is not exactly a string I could get from user as an input and frankly it is not even one that I could generate. It is Enum. So I will have to define an ENUM with all the supportable sorts and use that. How do I do that? I will have to define them in a separate GraphQL schema document. I tried doing that and configured webpack to build them and failed miserably. For one, I couldn't get it to compile the `.graphql` files. The webloader kept throwing the errors and I lost interest after a while.

### 2. Searching



The filters is a complex JSON like object that could support OR, AND conditions and everything. I want the values to be based on user input. Apollo supports variables for that purpose. You can do something like this in the Vue script

```js
apollo: {
 myObject: {
 gql: `query GetDataQuery($value1: String, $value2: Int) {
 objectINeed( filters: [{attr1: $value}, {attr2: $value2}] {
 ...
 }
 }`,
 variables() {
 return { value1: this.userInputValue1, value2: this.userInputValue2 }
 }
```

This is fine when I want to employ both the inputs for searching, what if I want to do only one? Well it turns out I have to define a different query altogether. There is no way to do an optional filter. See the docs on [Reactive Queries](https://vue-apollo.netlify.com/guide/apollo/queries.html#reactive-query-definition).
Now that was a lot of Yak shaving I am not willing to do.

Even if I did the Yak Shaving, I ran into trouble on the backend with nested querying. For example what if I wanted to get the objects based on the associated user? Like my query is more like:

```js
query getObjects {
 myObject {
 attr1
 attr2
 user(filters: {first_name: "adam"}) {
 }
 }
}
```

The Graphene SQLAlchemy documentation said I could do it, it even gave example documentation, but I couldn't get it working. And when I wanted to implement it myself, the abstraction was too deep that I would have to spend too many hours just doing that.

### 3. The documentation



The most frustrating part through figuring out all this was the documentation. For some reason GraphQL docs think that if I used Apollo in the frontend, then I must be using Apollo Server in the backend. Turns out there is no strict definition on the semantics for searching/filtering, only on the definition of how to do it. So what the design on the backend should match the design on the frontend. (Now where have I heard that before?) And that's the reason documentation usually shows both the client and server side implementations.

### 4. Managing state



An SPA has a state management library like Vuex, Redux to manage application state, but with GraphQL, local state is managed with a GraphQL cache. It improves efficiency by reducing the calls to the server. But here is the catch, you have to define the schema of the objects for that to work. That's right, define the schema as in write the models in GraphQL documents. It is no big deal if your stack is fully NodeJS, you can just do it once and reference it in both places.

In my case, I will have defined my SQLAlchemy models in Python in the backend, and I will have to do it again in GQL for the frontend. So changes have to be synced between them if anything changes. And remember that each query is defined separately, so I will have to update any query that will be affected by the changes.

At this point I was crying. I has spent close to 8 hours figuring out all this.

I gave up and rewrote the entire freaking app using REST API and finished the project including the UI in the next 6-7 hours and went to bed at 4 in the morning.

Learning
--------


1. GraphQL is a complex solution for a complex problem. You can solve simple problems with it but the complexity will hit you at some point.
2. It provides a level of clarity in querying data that REST API doesn't, but it comes with a cost. It is cheap for cheap work and costly for larger requirements. Almost like how AWS bills raise.
3. No it doesn't provide the kind of independence between the backend and frontend as it seems like on the surface. This might by lack of understanding and not the goal of GraphQL at all, but if you like me made this assumption, then just know it is invalid.
4. Use low-level libraries to implement GraphQL, and try to keep it NodeJS. At least for the sake of sharing the schema documents if not for anything. If I has implemented the actions myself instead of depending on Graphene and adding a filter library on top of that, I would have fared better.

