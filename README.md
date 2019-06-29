# The Cookbook
The Cookbook is a community of chefs who have come together to share and utilize some of the most unique recipes the online community has to offer. With a few simple steps, users can sign up, add a recipe and within a few seconds have it display for the world to see. Editing and deleting is also currently available, although the process is not completely secure as of yet. Future site renovation plans are set to include both a secure user login functionality, as well as a site search bar, which will allow users to filter through recipes based on a variety of key terms.

## UX
The website is intended for chefs who intend to share, and use search for new distinct recipes.
The Cookbook allows users to share their very own recipes, while having the ability to discover new recipes others have posted. Through a very sleek and user friendly interface, the Cookbook allows for quick uploads, edits and deletions.

User Stories
* User 1: As a chef, I want to go to the add recipe tab, so I can upload a recipe
* User 2: As a viewer, I would maneuver the home page, so I could view other recipes

Mock Up
* /static/media/images

## Features
The Cookbook includes the following features:
* Editing: Users 1 can edit their own recipes 
* Deleting: Users 1 can delete their own recipes 
* Adding a recipe: User 1 can upload a recipe
* Login: This allows user 1 and 2 access the site by filling in login credentials 


### Features Left to Implement
* Secure Login
* Search Bar
* A home page that displays recipes based on popularity or date added 

## Technologies Used
Flask
This project uses the Flask framework, while utilizing render_template, redirect, request and url_for, session. 
* http://flask.pocoo.org/

Pymongo
This project uses Pymongo to multiple independent databases. 
* https://api.mongodb.com/python/current/

Python
This project use the Python language to write code. 
* https://www.python.org/

HTML
This project uses HTML to create web pages.

Jinja2
This project uses jinja as a template engine for Python.
* ttp://jinja.pocoo.org/

Javascript
This project uses Javascript for animations and transitions.
* https://www.javascript.com/

Bootstrap 
This project uses bootstrap for css styling.
* https://getbootstrap.com/docs/4.3/layout/overview/

Materialize  
This project uses materialize for css styling.
* https://materializecss.com/

## Testing
Delete Recipe:
* Go to “Home” page
* Press delete recipe 
* Recipe is deleted 

Add Recipe:
* Go to “Add” page
* Submit an empty form and verify that an error message about the required fields appears
* Submit the filled form 
* Redirects to “Home” page
* Recipe Appears

Edit Recipe:
* Go to “Home” page
* Click on edit button
* Edit recipe and click “edit” recipe button
* Redirects to home, edited recipe appears

View Recipe:
* Go to “Home” page
* Click on expandable ingredients 
* Verify that ingredients appear
* Click on expandable instructions 
* Verify that instructions appear


## Deployment
This project was deployed through Heroku, and does not differ from other versions. 


## Credits
### Content
* Home Photo of number 1: https://foodrevolution.org/wp-content/uploads/2018/04/blog-featured-diabetes-20180406-1330.jpg
* Home Photo of number 2: https://images.pexels.com/photos/132694/pexels-photo-132694.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260
* Home Photo of number 3: https://images.pexels.com/photos/461198/pexels-photo-461198.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260
* Home Photo of number 4: https://images.pexels.com/photos/1268550/pexels-photo-1268550.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260
