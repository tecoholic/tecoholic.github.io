---
title: "Simplifying JSON parsing in Flask routes using decorators"
date: 2019-07-26T04:28:36
slug: "simplifying-json-parsing-in-flask-routes-using-decorators"
categories:
  - Coding
tags:
  - flask
  - python
---

Flask is simple and effective when it comes to reading input parameters from the URL. For example, take a look at this simple route.

```python
@app.route("/todo/<int:id>/")
def task(id):
 return jsonify({"id": id, "task": "Write code"})
```

You specify a parameter called `id` and set its type as `int`, Flask automatically parses the value from the URL converts it to an integer and makes it available as a parameter in the `task` function.

But it becomes harder when we start working with JSON being passed on as inputs when we build APIs.

```python
@app.route("/todo/", methods=["POST"])
def create_task():
 incoming = request.get_json()
 if "task" not in incoming:
 return jsonify({"status": "error", "message": "Missing parameter 'task'"}), 400

 tasks.append(incoming["task"])
 return "Task added successfully", 201
```

The above method requires the JSON input to contain `task` parameter in order to create a new task. So it has to check if that parameter is send during the request before it can add the task to the task list. This is simple to implement for just a few parameters. In the real world the APIs aren't always simple. For example, if you envision an address book API, you probably have multiple fields like first name, last name, address line 1, address line 2, city, state, zip code...etc., and writing something like

```python
if "first_name" not in incoming:
 ...
if "last_name" not in incoming:
 ...
```

is going to be tedious. We can perhaps take a more pythonic approach and write the logic as:

```python
@app.route("/address/", methods=["POST"])
def add_address():
 required_params = [
 "first_name", "last_name", "addr_1", 
 "addr_2", "city", "state", "zip_code"
 ]
 incoming = request.get_json()
 missing = [rp for rp in required_params if rp not in incoming]
 if missing:
 return jsonify({
 "status": "error",
 "message": "Missing required parameters",
 "missing": missing
 }), 400

 # Add the address to your address book
 addresses.append(incoming)
 return "Address added successfully", 201
```

As you write more routes, you will start to notice that the `missing` and `if missing` logic repeating itself in all the places where we are expecting JSON data. Instead of repeating the logic over and over, we can simplify it by putting it in a decorator like this:

```python
def required_params(*args):
 """Decorator factory to check request data for POST requests and return
 an error if required parameters are missing."""
 required = list(args)

 def decorator(fn):
 """Decorator that checks for the required parameters"""

 @wraps(fn)
 def wrapper(*args, **kwargs):
 missing = [r for r in required if r not in request.get_json()]
 if missing:
 response = {
 "status": "error",
 "message": "Request JSON is missing some required params",
 "missing": missing
 }
 return jsonify(response), 400
 return fn(*args, **kwargs)
 return wrapper
 return decorator
```

Now we can write the same `add_address` route like this:

```python
@app.route("/address/", methods=["POST"])
@required_params("first_name", "last_name", "addr_1","addr_2", "city", "state", "zip_code")
def add_address():
 addresses.append(request.get_json())
 return "Address added successfully", 201
```

Here is how it has changed

![json_decorator_diff](/img/wp-content/uploads/2019/07/json_decorator_diff.png)

The `required_params` decorator will do the job of checking for the presence of parameters and returning an error. We can add the decorator to any routes that requires JSON parameter validation.

If we put in some more work, we can even expand the logic by specifying the datatypes of those parameters pass a dictionary like this:

```python
@route(...)
@required_params({"name": str, "age": int, "married": bool})
def ...
```

and in the decorator perform the validations

```python
def required_params(required):
 def decorator(fn):
 """Decorator that checks for the required parameters"""

 @wraps(fn)
 def wrapper(*args, **kwargs):
 _json = request.get_json()
 missing = [r for r in required.keys()
 if r not in _json]
 if missing:
 response = {
 "status": "error",
 "message": "Request JSON is missing some required params",
 "missing": missing
 }
 return jsonify(response), 400
 wrong_types = [r for r in required.keys()
 if not isinstance(_json[r], required[r])]
 if wrong_types:
 response = {
 "status": "error",
 "message": "Data types in the request JSON doesn't match the required format",
 "param_types": {k: str(v) for k, v in required.items()}
 }
 return jsonify(response), 400
 return fn(*args, **kwargs)
 return wrapper
 return decorator
```

With this if a JSON field is sent with the wrong datatype an appropriate response will be returned as well.

PS: I found [this full blown decorator](https://gist.github.com/corbinbs/3791168) function with custom error messages and validations after I wrote this post. Check it out if you want even more functionality.
