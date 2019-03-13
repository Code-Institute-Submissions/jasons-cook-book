Project 3 - Cook Book with Python and MongoDB

------------------------------------------DEPLOYMENT------------------------------------------

The project has been deployed on Heroku:

https://cook-book-flask-mongo.herokuapp.com/

Please allow up to 60 seconds for the page to load, as it may be inactive if it hasn't been loaded in a while.

------------------------------------------BRIEFING------------------------------------------

This project was made using Python, MongoDB, Javascript, HTML and CSS. This project was created to showcase how a database (MongoDB) can be used to store and organize large amounts of data, in this case the details for recipes in an online cookbook, that users can edit and add new entries to. I used Javascript, HTML and CSS to improve the style and look of the website, and Python has been used for the back-end logic, for controlling the information in the database and also the flow of the website, ie. URLS and calling data.

------------------------------------------OVERVIEW------------------------------------------

The goal for this project was to create a website that demonstrated primarily Python and MongoDB. I followed the given specifications and created a cook book, that users can added recipes and categories to, and edit any existing entries. When a recipe is created, it is added to a database, and the website calls that information in order to display it in an easy to understand way for the end user. The user can click on individual recipes to reveal more information. I have also included a slideshow of pictures and information, which was made using SlickJS. I also added a help box at the top of every page, which uses Javascript and Materialize. I gave the website a rounded, minimalist theme with soft fonts like comic sans and muted colours that blend well together, which means that the essential information (the reicpies) is easy to look at, and users aren't distracted by strong colours and effects.

In terms of what could have been done better, I think some kind of user validation would have been good to have, so that a record could be kept of who added and edited records. If a user system could have been implemented, then some form of edit/delete lock could be pleased on records to stop malicous users editing or deleting records that they didn't create. I think if I built this from the ground up in Django, then this system could be achieved, along with an administration system that allowed certain users to moderate acitivty on the site. I looked into adding SweetJS to improve the look of warning messages that display on the page, however I was not able to successfully implement it.
