---
title: Strapi - Adding IsOwner Policy to the API
date: '2020-08-11T21:06:09'
slug: strapi-adding-isowner-policy-to-the-api
categories:
  - Coding
tags:
  - api
  - js
  - strapi
---

Strapi is an Open Source headless CMS based on NodeJS. It provides the backend admin tools to quickly create an API – both REST and GraphQL.

This is a mini series which outlines:

1. [Setting up Strapi and creating an API](https://arunmozhi.in/2020/08/08/strapi-creating-an-api-without-a-single-line-of-code/)
2. Adding ownership control to the API endpoints – (you are here)
3. Optimising REST API responses


So far...
---------



We have created models for the app and have an API setup which works with JWT Authentication without a single line of code. But we have an issue, any authenticated user can read every other user's data.

This can be rectified using setting up an access policy in the Model's controller file.

**Side Note:** Strapi's Policies section explains how to implement them and configure them for routes [here](https://strapi.io/documentation/v3.x/concepts/policies.html#how-to-create-a-policy). But that doesn't work for `IsOwner` policy because ownership is object specific and thus has to be implemented in the controller instead of policy configuration.

Writing the Is Owner Policy
---------------------------



We will be using the [Create is owner policy](https://strapi.io/documentation/v3.x/guides/is-owner.html) document as our reference material to update our API. I will be repeating all of it here with a little more information.

We have two models defined so far - Category & ExpenseItem. I am going to implement the IsOwner policy for Category and leave ExpenseItem as an exercise. Now, let's go write some code.

* Let us open our text editor and open the `api/category/controllers/category.js` file
* It should have the following content



```js
'use strict';

/**
* Read the documentation (https://strapi.io/documentation/v3.x/concepts/controllers.html#core-controllers)
* to customize this controller
*/

module.exports = {};
```

All of our code will go into the braces. We will be adding 6 functions:

1. **create** - the function executed when a new category is created. Here we will make sure that any newly created category is automatically assigned to the user creating the category.
2. **find** - the function execute when all the objects are listed. For eg., `/categories`. When a user requests categories, we will filter the results such that the user receives only their's and not others'.
3. **findOne** - Same as the one above when a single object is accessed with id like `/categories/1`
4. **count** - the count of objects in a model. We will be counting only the objects created by a particular user
5. **update** - update a specific object. Only the owner should be able to do it
6. **delete** - delete a specific object. Only the owner should be able to delete an object.



The above will cover the 4 CRUD operations and the 2 extra ones (listing and counting).

### Create function



```js
const { parseMultipartData, sanitizeEntity } = require("strapi-utils");

module.exports = {
/**
* Create a new Category
*
* @param {*} ctx The Request Context
*/
async create(ctx) {
let entity;

if (ctx.is('multipart')) {
const { data, files } = parseMultipartData(ctx);
data.user = ctx.state.user.id;
entity = await strapi.services.category.create(data, { files });
} else {
ctx.request.body.user = ctx.state.user.id;
entity = await strapi.services.category.create(ctx.request.body);
}
return sanitizeEntity(entity, { model: strapi.models.category });
},
};
```

Strapi is built on Koa.js and thus uses async await instead of callbacks. Let us break down the logic of the function and see what's happening.

* the function is passed in the Request context which has the all the request related information like the form data, the user identified in the request (from our JWT token)..etc.,
* we check if it is a `multipart` form which would mean we have uploaded files to deal with.
* we parse the form for data and files, set the user as the user executing the request and use the Strapi service for our model to create a new entity.
* if it is not a multipart form, then we just set the user of the request as an extra field into the request data and create the category using the Strapi service
* finally we need to return the new category as a response - We use strapi's function `sanitizeEntity` to pass in the newly created entity and the model.


**Side Note:** I know the Category model doesn't have any files attached to it and the IF block with 'multipart' check is not necessary in this situation. But I am leaving it here for two reasons:

1. If in the future, we want to support logos or some form of header image for the `Category` model, we don't have to come back and update the code again.
2. This might act as a reference implementation for someone reading the blog and might use it on a model with files and don't want them to wonder files are not getting saved.



If you really want to have a lean code base then the just 3 lines would be sufficient

```js
module.exports = {
/**
* Create a new Category
*
* @param {*} ctx The Request Context
*/
async create(ctx) {
ctx.request.body.user = ctx.state.user.id;
let entity = await strapi.services.category.create(ctx.request.body);
return sanitizeEntity(entity, { model: strapi.models.category });
},
};
```

#### Testing the create logic



Now we can re-run the POST request to create a new category in POST and verify that the user is automatically set for the category.

![strapi_new_category_with_user](/img/wp-content/uploads/2020/08/strapi_new_category_with_user.png)
### Update function



Now that we have the create function auto assigning the user for the categories, let us implement restrictions for updates.

```js
/**
* Update a category
*
* @param {*} ctx the request context
*/

async update(ctx) {
const { id } = ctx.params;

let entity;

// Find the category matching the ID and the user
const [category] = await strapi.services.category.find({
id: ctx.params.id,
'user.id': ctx.state.user.id,
});

if (!category) {
return ctx.unauthorized(`You can't update this entry`);
}

// Update the category
if (ctx.is('multipart')) {
const { data, files } = parseMultipartData(ctx);
entity = await strapi.services.category.update({ id }, data, {
files,
});
} else {
entity = await strapi.services.category.update({ id }, ctx.request.body);
}

return sanitizeEntity(entity, { model: strapi.models.category });
},
```

The update function adds an extra step of fetching the category and making sure that the category with that ID and userID exists before reading the request data. If the category doesn't exist, then it returns a `Unauthorized` error. If it exists, then it updates the category and returns the updated information.

We can verify it with a **PUT** request to http://localhost:1337/categories/

![strapi_update_category](/img/wp-content/uploads/2020/08/strapi_update_category.png)

Notice that the *Food* category has now been updated to *Food & Drinks*. Not just that, using the JWT token of the *intruder* user wouldn't work either.

![strapi_update_unauthorized](/img/wp-content/uploads/2020/08/strapi_update_unauthorized.png)
### Find function



```js
/**
* List all the categories beloinging to the requesting user
*
* @param {*} ctx the request context
*/

async find(ctx) {
let entities;

if (ctx.query._q) {
entities = await strapi.services.category.search({
...ctx.query,
'user.id': ctx.state.user.id
});
} else {
entities = await strapi.services.category.find({
...ctx.query,
'user.id': ctx.state.user.id
});
}

return entities.map(entity => sanitizeEntity(entity, { model: strapi.models.category }));

}
```

The find function checks if the query is a search query or a filter and calls the corresponding function. We also pass the `'user.id'` of the requesting user along with other query params from the request to filter the search results. Now when we request the url http://localhost:1337/categories, the response contains only the objects of the requesting user.

![strapi_get_categories_test_user](/img/wp-content/uploads/2020/08/strapi_get_categories_test_user.png)

Now let us see what we get when we request as a different user

![strapi_get_categories_intruder](/img/wp-content/uploads/2020/08/strapi_get_categories_intruder.png)
### FindOne function



```js
/**
* Get the category with a specific ID
*
* @param {*} ctx the request context
*/
async findOne(ctx) {
const { id } = ctx.params;

const entity = await strapi.services.category.findOne({ id, 'user.id': ctx.state.user.id });

if (!entity) {
return ctx.unauthorized(`You can't view this entry`);
}

return sanitizeEntity(entity, { model: strapi.models.category });
},
```

Fetching the category with `id=3` as the owner (test_user)

![strapi_get_one_category_test_user](/img/wp-content/uploads/2020/08/strapi_get_one_category_test_user.png)

Trying to get test_user's category as the intruder

![strapi_get_one_category_intruder](/img/wp-content/uploads/2020/08/strapi_get_one_category_intruder.png)
### Count function



```js
/**
* Count of the categories of the requesting user
*
* @param {*} ctx the request context
*/

count(ctx) {
if (ctx.query._q) {
return strapi.services.category.countSearch({
...ctx.query,
"user.id": ctx.state.user.id,
});
}
return strapi.services.category.count({
...ctx.query,
"user.id": ctx.state.user.id,
});
},
```

Count of test user

![strapi_category_count](/img/wp-content/uploads/2020/08/strapi_category_count.png)
### Delete function



```js
/**
* Delete a record
*
* @param {*} ctx the request context
*/
async delete(ctx) {
const [category] = await strapi.services.category.find({
id: ctx.params.id,
"user.id": ctx.state.user.id,
});

if (!category) {
return ctx.unauthorized(`You can't delete this entry`);
}

let entity = await strapi.services.category.delete({ id: ctx.params.id });
return sanitizeEntity(entity, { model: strapi.models.category });
},
```

Delete as a intruder - Unauthorized

![strapi_delete_intruder](/img/wp-content/uploads/2020/08/strapi_delete_intruder.png)

Delete as the owner - test_user

![strapi_delete_test_user](/img/wp-content/uploads/2020/08/strapi_delete_test_user.png)
### Final code for the controller



Here is the complete controller code with all the functions.

[gist https://gist.github.com/tecoholic/ee101b0efbf76b63b63826ebebe2c8b9]

So far ...
----------


* Created a project
* Added the models
* Setup the API
* Added the IsOwner policy to the controller


Next
----



Let's do a little bit of optimisation of the API responses. If we notice the GET request responses, the relations are always fully populated. For example, if we do a GET `/categories` each of these categories will have the user object in it. And if you add some expense items to a category, then all of those will be returned in the GET response as well. We will try to reduce this a bit and make it more streamlined in the next part.
