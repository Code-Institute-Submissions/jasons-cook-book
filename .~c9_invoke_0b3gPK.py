import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "jasons_cook_book"
app.config["MONGO_URI"] = "mongodb://admin:TLPjason1801@ds123796.mlab.com:23796/jasons_cook_book"

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())
    
@app.route("/add_recipe")    
def add_recipe():
    return render_template("addrecipe.html", 
    categories=mongo.db.categories.find())
    
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for("get_recipes"))
    
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template("editrecipe.html", recipe=the_recipe, categories=all_categories)
    

@app.route('/update_recipe/<recipe_id>', methods=["GET""POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id':ObjectId(recipe_id)},
        {
            'recipe_name' : request.form['recipe_name'],
            'category_name' : request.form['category_name'],
            'recipe_desc' : request.form['recipe_desc'],
            'is_vegan':request.form['is_vegan'],
            'is_vegetarian':request.form['is_vegetarian'],
            'is_gluten_free':request.form['is_gluten_free']
        })
    return redirect(url_for('get_recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id' : ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/get_categories')
def get_categories():
    return render_template('categories.html', categories=mongo.db.categories.find())

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)