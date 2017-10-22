---
layout: post
title: "Using React for parts of a Falsk App"
description: "How does one setup a Flask application to use React in only parts of the application"
category: Coding
tags: [python,react,coding]
excerpt: How does one setup a Flask application to use React in only parts of the application? React with JSX syntax, the ability to just drop the the library and use it for only selective parts of the app seemed just right. After trying out the tic-tac-toe tutorial, I ventured to setup it for our project.
---

## Background:

As a part of my work, I needed a console like viewer in a web application (like the one used in travis.ci). The frontend is simply Bootstrap 3 and some jQuery JavaScript. I have written a rudimentary one using Bootstrap's Panel and List Groups and using the helper classes to style them. But the appication has grown and it is time we got a really good log viewer.

## Requirements:

* The library should be easy to include in the project without requiring a complete overhaul of the frontend. (Things like Angular, Ember are out)
* We might decouple the app into a REST API and frontend sometime in the future, so it needs to provide a upgrade path for the full frontend.
* To me, a Python programmer, it should be easy to get started and start building, without enforcing specific new requirements.
(e.g., Angular forces TypeScript, I am willing to learn, just not now, not for this one)

React with JSX syntax, the ability to just drop the the library and use it for only selective parts of the app seemed just right. After trying out the tic-tac-toe tutorial, I ventured to setup it for our project.

## Setting up the development environment

JSX is not plain native Javascript. Eventhough I could include the React and ReactDOM libraries using the `<script>` tags, I have to setup a `node.js` based environment to compile the JSX into JS.

### Project file structure

The Flask app has a typical structure as show below
```
-- project/
    |-- flask_app/
    |   |-- static/
    |   |   |-- js/
    |   |   |-- css/
    |   |   |-- images/
    |   |-- tempaltes/
    |   |-- __init__.py
    |   |-- application.py
    |   |-- views.py
        ...
    |-- run.py
    |-- .gitgnore
    |-- README
```

### Setting up React's requirements

React's [Adding React to an Existing Application](https://reactjs.org/docs/installation.html#adding-react-to-an-existing-application) lists three requirements - a package manager, a bundler and a compiler. I used **npm** for package manager, **Webpack** for bundler and **Babel** for the compiler. Here are the steps for the setup:

* Create the `package.json` file using `npm init` inside `project` directory.
* Create a new directory named `ui` insdie the `project` to hold the React JSX files
* Install the packages `react`, `react-dom` using `npm install --save <package-name>`
* Install the packages `webpack`, `babel-core`, `babel-loader`, `babel-preset-env`, `babel-preset-react` using `npm install --save-dev <package-name>`
* Add the line `"build": "webpack --config webpack.config.js"` to the `scripts` block of `package.json`
* Create file `.babelrc` with a single line `{"presets": ["react", "env"]}`
* Create file `webpack.config.js` with the contents

```js
const path = require('path');

module.exports = {
    entry: './ui/logger.js',  // logger.js is where I plan to write the JSX code
    output: {
        path: path.resolve(__dirname, 'flask_app/static/js/'),
        filename: "logger.js"
    },
    module: {
        rules: [
            { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" }
        ]
    }
}
```

Here is what I have done so far:

* I have initiaed the project with `package.json` to manage things like requirements for the JS files, run npm commands, ...etc. I guess this is like the `setup.py` of Python world.
* Added the required packages 
* Configured **Babel** compiler to use the presets required for React to compile
* Configured **Webpack** to read the `ui/logger.js` file and compile it using Babel and put it the Flask app's `static/js/` folder so that it can be used in the Jinja templates using `url_for('static', filename='logger.js')`
* Configured **NPM** so that `npm run build` would run webpack to compile and put the file in static folder.

### New Project structure

After adding everything, this is how the project looks

```
-- project/
    |-- flask_app/
    |   |-- static/
    |   |   |-- js/
        ...
    |-- run.py
    |-- .gitgnore
    |-- README
    |-- node_modules/
    |-- ui/
    |   |-- logger.js
    |-- .babelrc
    |-- webpack.config.js
    |-- package.json

```

With the above setup, I am good to go. All I need to do is add a *script* tag with `src` pointed to the `logger.js`. With everything setup,

* I added a small JSX snippet to `ui/logger.js`
* ran `npm run build` (the file compiled and was put in the `static/js/` folder)
* started the Flask development server `python run.py`
* loaded the app in the browser.

Everything worked as expected.

### ..except it didn't the second time

Now I changed the code in `ui/logger.js` > ran `npm run build` > reloaded the page in browser. Nothing changed. **Now we have a problem.** It's the browser caching the output `static/js/logger.js` file.

## Solving Caching issue

While Caching is good from a client's point of view, it is a little tricky in a development environment. If we were building a full blown React app using the `react-cli`, we won't have this issue as the `react-scripts` would watch the file changes and reload the browser for us. In the current setup using Flask's development server, however, we need to take care of it ourselves. Webpack to the rescue.

### Webpack optimizations

I followed Webpack's [Caching](https://webpack.js.org/guides/caching/) guide and applied everything suggested. Now the `webpack.config.js` looks like this:

```js
const webpack = require('webpack');
const path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');


module.exports = {
    entry: {
        main: './ui/logger.js',
        vendor: [
            'react', 'react-dom'
        ]
    },
    output: {
        path: path.resolve(__dirname, 'flask_app/static/build'),
        filename: "[name].[chunkhash].js"
    },
    module: {
        rules: [
            { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" }
        ]
    },
    plugins: [
        new CleanWebpackPlugin(['flask_app/static/build']),
        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendor'
        }),
        new webpack.optimize.CommonsChunkPlugin({
            name: 'runtime'
        }),
    ]
}
```

This is what the updated webpack config does:
- instead of saving the generated Javascript as a single file called `logger.js` it splits the output into three files named
    * `main.[chunkhash].js` which contains the compiled `ui/logger.js`
    * `vendor.[chunkhash].js` which contains the libraries listed in `entry.vendor`
    * `runtime.[chunkhash].js` which contains the Webpack's runtime logic to load the files generated
   
    **Note:** the `chuckhash` is a value that webpack substitutes when generating the files. This changes with the changes in entry files. So we have a different filename in the output with every build, thus avoiding the caching issue.
- the `CleanWebpackPlugin` removes all the files in the output directory before generating new files so we don't have outdated files like `main.hash1.js`, `main.hash2.js`.. etc.,
- since `static/js` folder has other files like bootstrap, jquery ..etc., So the `output.path` is set to a new directory `static/build`, to prevent the Clean Webpack plugin from deleting them.

With the above config, we will have a different filename everytime we build using `npm run build`. Now the file cached by the web browser is not used as the new filename is different from the old one.

> But how do we use the latest filenames in the `<script>` tag in the Jinja templates?

There is a plugin to solve this issue called `Flask-Webpack`, but I felt it too be an overkill.

### Flask Context Processor to get the hashed filename

Add the following context processor to the Flask app:

```python
   @app.context_processor
    def hash_processor():
        def hashed_url(filepath):
            directory, filename = filepath.rsplit('/')
            name, extension = filename.rsplit(".")
            folder = os.path.join(app.root_path, 'static', directory)
            files = os.listdir(folder)
            for f in files:
                regex = name+"\.[a-z0-9]+\."+extension
                if re.match(regex, f):
                    return os.path.join('/static', directory, f)
            return os.path.join('/static', filepath)
        return dict(hashed_url=hashed_url)
```

This provides a function called `hashed_url` which looks for the file and returns its hashed form. Now we can add the files using script taks as below:

```html
    <script type="text/javascript" src="{{ hashed_url('build/runtime.js') }}"></script>
    <script type="text/javascript" src="{{ hashed_url('build/vendor.js') }}"></script>
    <script type="text/javascript" src="{{ hashed_url('build/main.js') }}"></script>
```

The `hashed_url` would match the filename passed to it with the the files in the directory and returns the hashed form. For e.g., `hashed_url("build/main.js")` returns `/static/build/main.16f45d183a4c0f0b1b37.js`s

## Conclusion

The whole process of setting this up took multiple hours of research and testing. I could have used one of the available boilerplates to set this up, but I now have it in the form I want it and I understand what the different parts mean and do. It lets me use React for small components as required and grow as the project grows. It also creates no disruption in the workflow of other developers. Happy coding time ahead :)