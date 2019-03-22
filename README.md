# Project 3 - Cook Book

## Getting Started

The application has been deployed at https://cook-book-flask-mongo.herokuapp.com/

The application is viewable on any modern browser. Please allow up to 45 seconds for the page to load, especially if you have not loaded it before, as it will need some time to load on Heroku's servers.

## Testing

I have tested this application on Chrome, Vivaldi and Firefox browsers. To test the retrieval of data from MongoDB, I created test records directly inside of the database, as below:
```
{
    "_id": {
        "$oid": "5c8bf0da92437d000c58fb01"
    },
    "recipe_name": "test name",
    "category_name": "test category name",
```
This was before I had created a way for the end user to create records within this application. I tested the rendering of records before creating the user interface so that I didn't have to worry about it when the time came to create the UI. This data would be retrieved by the Python code, depending on where the user was in the application, and what they were requesting, such as when editing an existing recipe, it would pull through the name and category and description.

In addition to testing the back-end portion of the project, I also tested the Javascript and responsiveness of the website. The following Javascript I added in order to test the slideshow animations, with some text stored in an HTML element. 

```
$(document).ready(function(){
                $('.single-item').slick({
                autoplay: true,
                    });
                });
```
This code would create a simple left to right animated slideshow with some text. I made sure that the slideshow was working and responsive before I added in any images and any more text. However, adding images did create some more problems, and since I only tested with text, I did foresee complications around using images in the slideshow.

## Goals

I wanted to create a simple and easy to use Cook Book with a warm and smooth interface. I knew from the very beginning I wanted the project to be easy to use, but I didn't want the interface to be minimalistic or too modern. I think I have succeeded with that. For the colour scheme, I took inspiration fro apron and kitchen designs and settled for a light red and white background. I think the colour's work well, and don't obscure any of the text. I used Comic Sans as the font for the cookbook, as it as a friendly and appealing look to it, and isn't too sharp or modern. However, I did keep the default font for the help menu, as this has a slightly different design.

I wanted to help menu to be a bit more modern and sleek looking, rather than round and bubbly like the rest of the cookbook. I also wanted to keep it minimal, without pictures or too many animations. I felt like it was a good idea to not only keep the help menu separate from the application in terms of its location (and by hiding it) but also stylistically as well, so that the user can use the help interface easily and without getting lost, having to look around to try and find something.

I think if I were to re-approach this project, I might start by designing the interface before writing the code. There are merits for both approaches, however, to see which is better for me, approaching the project at a different angle might reveal a more optimal strategy. Additionally, I might incorporate some authentication and administration, possibly by building the application from the ground up with Django. this would allow for user accounts and authentication, as well as administration with a dedicated interface.


## Built With

* CSS3
* HTML5
* JavaScript
* Python
* MongoDB

## Authors

* **Jason Street** - *For Code Institute*

## Acknowledgments

* SlickJS (For animated gallery)
* MLabs (For MongoDB)
* Google (For images)
* Materialize (For animations and icons)
* Heroku (For hosting)
