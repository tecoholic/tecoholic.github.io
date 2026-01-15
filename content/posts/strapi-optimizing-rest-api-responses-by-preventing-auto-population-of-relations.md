---
title: Strapi - Optimizing REST API responses by preventing auto-population of relations
date: '2020-08-18T18:24:59'
slug: strapi-optimizing-rest-api-responses-by-preventing-auto-population-of-relations
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
2. [Adding ownership control to the API endpoints](https://arunmozhi.in/2020/08/11/strapi-adding-isowner-policy-to-the-api/)
3. Optimising REST API responses – (you are here)


So far ...
----------


We have created a REST API for an expense management application with category support. We have JWT token based auth which came with Strapi to authenticate users. We have implemented the **IsOwner** policy in the controllers to restrict data access.


Optimizing the Responses while
------------------------------


The API by default automatically populates relationships and sends in all the related data. It is very useful for some cases and completely a overkill for others. Take the following for example.





![](/img/wp-content/uploads/2020/08/strapi-expense-items.png?w=926)


I have setup 5 Expense Items in the Admin dashboard for our `test_user`. 4 of them are under the category 'Travel' and one of them is under the category 'Food'. Now when we fetch the categories, let us see what we get.





![](/img/wp-content/uploads/2020/08/strapi-expense-response.png?w=1024)


When making a GET request to `/categories`, we are not only getting the categories but also all the expense items which are under every category. When a user has thousands of expense items, we cannot be querying the DB for all of them whenever a GET request is made to categories. That would cause serious performance issues.


### Preventing auto-population of relations


We can turn this off by setting the `autoPopulate` flag to false in the model.


* Open the file `/api/category/models/category.settings.json`
* Add the line `"autoPopulate": false` in the the `expense-items` block as shown below
* Let us also disable auto-population of the user. We have already implemented the IsOwner policy for all requests, so only the owner is going to be requesting their own categories and the user field is redundant data.



```
{
  "kind": "collectionType",
  "collectionName": "categories",
  "info": {
    "name": "Category"
  },
  "options": {
    "increments": true,
    "timestamps": true
  },
  "attributes": {
    "name": {
      "type": "string",
      "required": true,
      "minLength": 2
    },
    "color": {
      "type": "string"
    },
    "user": {
      "plugin": "users-permissions",
      "model": "user",
      "via": "categories",
      "autoPopulate": false
    },
    "expense_items": {
      "via": "category",
      "collection": "expense-item",
      "autoPopulate": false
    }
  }
}

```

Now as soon as we save the file, the Strapi dev server should restart. Now we can run the same GET `/categories` request to verify the results.





![](/img/wp-content/uploads/2020/08/strapi-no-relations-data.png?w=1024)


There is no expense items in the response. Just the categories.


We can use this method to turn of auto population of any relation in any of the Content Types we have created. This way the API returns only what we intend it to return.


Optimising the Login response
-----------------------------


Let us take a look at the login response.





![](/img/wp-content/uploads/2020/08/strapi-login-response.png?w=1024)


We can see that it contains all the categories and expense items of the user. This would put disastrous load on the system as the data size grows. So, let us turn off auto-populate for the users as well.


* Open `/extensions/user-permissions/models/User.settings.json`
* Scroll to the bottom and add `"autoPopulate": false` to the entries `categories` and `expense_items`





![](/img/wp-content/uploads/2020/08/strapi-user-settings.png?w=781)


Now, let us login again and check the response.





![](/img/wp-content/uploads/2020/08/strapi-optimized-login.png?w=1024)


No categories or expense items in the response, just the JWT token user object and the roles. Now every time a user logs in Strapi won't be querying the database for everything related to the user.


Conclusion
----------


This concludes this mini series. By applying the changes presented in this series, Strapi can be used a REST API backend not just for CMS purposes with strong public frontend, but also as a good backend for User focused web applications.


In my journey as a web developer, Strapi blew my mind the same way Django did almost a decade back with its built-in Admin UI. The amount of power Strapi packs right off the box is amazing.




