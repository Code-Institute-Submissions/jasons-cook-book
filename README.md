# Project 3 - Cook Book

A web application utlizing python and MongoDB to create an editable database of cooking recipes.

## Table of Contents  
1. [Deployment](#Deployment)  
2. [Testing](#Testing) 
3. [Goals](#Goals)
4. [Improvements](#Improvements)
5. [Credits](#Credits)

## Deployment <a name="Deployment"></a>

The application has been deployed via Heroku and can be found at https://cook-book-flask-mongo.herokuapp.com/
Using the Heroku console within Cloud9, as well as the settings on the Heroku dashboard, I was able to push and deploy this project petty smoothly to Heroku. I have also used Heroku's config variables to store some data, such as Port and IP, as well as security keys, such as the Mlabs API key.

The deploy on Heroku I did the following:

1. Test local functionality for bugs
2. Commit all files to GitHub for version control, and as a fallback
3. Using the developer console in Cloud9 I logged into Heroku with ```heroku login```
4. I added config vars using the Heroku GUI. Config vars can also be added with ```heroku config:set VAR=XXX```
5. After committing I pushed to heroku with ```git push heroku master```


The application is viewable on any modern browser. Please allow up to 30 seconds for the page to load, especially if you have not loaded it before, as it will need some time to load on Heroku's servers.

## Testing <a name="Testing"></a>

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

In addition to testing the functionality of the backend code, I have also tested the frontend aspects by testing the website on different browsers and by using the Chromium developer console to view the website on different mobile devices such as tablets and smart phones. Using the findings from these tests, I can see that my website is responsive and suitable for uses across multiple device types.

## Goals <a name="Goals"></a>

I wanted to create a simple and easy to use Cook Book with a warm and smooth interface. I knew from the very beginning I wanted the project to be easy to use, but I didn't want the interface to be minimalistic or too modern. I think I have succeeded with that. For the colour scheme, I took inspiration fro apron and kitchen designs and settled for a light red and white background. I think the colour's work well, and don't obscure any of the text. I used Comic Sans as the font for the cookbook, as it as a friendly and appealing look to it, and isn't too sharp or modern. However, I did keep the default font for the help menu, as this has a slightly different design. I think this creates a nice contrast between the cookbook and the help section, which I wanted to keep relatively seperate for ease of use. 

A lot of modern cooking website use a modern design/UI, with a lot of muted colours like grey, black and white. I wanted to use a lot of red as this felt more tradional and friendly. <br>
![Image of Cooking Site](https://is5-ssl.mzstatic.com/image/thumb/Purple115/v4/4b/88/bb/4b88bba6-8cef-7846-f34f-0f3c9e4720e1/pr_source.png/300x0w.png)<br>
This BBC cooking recipe website is a good example of what I think a lot of modern cooking sites look like, with it's angular layout and lack of colour. I don't think one design is better over the other, and there a lot of arguments for traditionalism vs modernism/minimalism, but it highlights how my site tries to be different in that aspect.

While the recipes menu is more traditional in it's design, I wanted to help menu to be a bit more modern and sleek looking, rather than round and bubbly like the rest of the cookbook. I also wanted to keep it minimal, without pictures or too many animations. I felt like it was a good idea to not only keep the help menu separate from the application in terms of its location (and by hiding it) but also stylistically as well, so that the user can use the help interface easily and without getting lost, having to look around to try and find something.

![Image of Wire Frame](https://s3.amazonaws.com/assets.mockflow.com/app/wireframepro/company/Ce53a54608deb00512cf8206be82c6f7c/projects/M5b430db21d6fed246ca1b023294112561556183776723/pages/a98b36f009a34c0e8512a20127441b5b/image/a98b36f009a34c0e8512a20127441b5b.png)

![Mood Board](https://i.imgur.com/hdfsrLX.jpg)

## Improvements <a name="Improvements"></a>

If I were to work on this project in the future with improved skills, one area I would look into improving would be adding some more python functionality. I did attempt to implement a review system, where reviews would be stored in a text file and displayed under each recipe. I had a lot of issues with this however, with the same reviews appearing under all recipes, users being able to edit each others reviews and so on. After some discussion with my mentor I decided to abandone this feature as it seemed out of scope for the project. I would also consider adding some more visual elements, to make the website a bit more dynamic, with maybe the feature to add videos and images to recipes.

If I were to re-approach this project, I might start by designing the interface before writing the code. There are merits for both approaches, however, to see which is better for me, approaching the project at a different angle might reveal a more optimal strategy. Additionally, I might incorporate some authentication and administration, possibly by building the application from the ground up with Django. this would allow for user accounts and authentication, as well as administration with a dedicated interface.

I should also consider security concerns in my application as well. I have previously committed files with security keys that are used within my application, such as my MongoDB ID. In a real life application, having security flaws is a major issues, and presents many challenges for developers. Security flaws can damage the reputation of applications and developers, and can lead to data breaches. In the future if I were to develop an application that uses security keys, I should consider how I can remove these keys from my Git history, or prevent them from being a part of the commit in the first place. I have included my security keys as Heroku variables, which does provide some security, however the keys are part of my respository history, and can still be viewed.

## Built With <a name="Credits"></a>

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
