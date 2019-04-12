import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "jasons_cook_book"
app.config["MONGO_URI"] = os.environ.get("MONG_URI")

##mongo = PyMongo(app)
mongo = 'mongodb://<dbuser>:<dbpassword>@ds123796.mlab.com:23796/jasons_cook_book'


@app.route("/")
def home():
    categories = mongo.db.categories
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())

@app.route("/get_recipes")
def get_recipes():
    categories = mongo.db.categories
    all_recipes = mongo.db.recipes 
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())
    
@app.route("/add_recipe")    
def add_recipe():
    all_recipes = mongo.db.recipes 
    return render_template("addrecipe.html", 
    categories=mongo.db.categories.find())
    
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    categories = mongo.db.categories
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for("get_recipes"))
    
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template("editrecipe.html", recipe=the_recipe, categories=all_categories)
    
@app.route('/update_recipe/<recipe_id>', methods=["GET","POST"])
def update_recipe(recipe_id):
    categories = mongo.db.categories
    recipes = mongo.db.recipes 
    
    if 'is_vegan' not in request.form:
        request.form.to_dict()['is_vegan']=False
    else:
        request.form.to_dict()['is_vegan']=True
    
    if 'is_gluten_free' not in request.form:
        request.form.to_dict()['is_gluten_free']=False 
    else:
        request.form.to_dict()['is_gluten_free']=True
        
    if 'is_vegetarian' not in request.form:
        request.form.to_dict()['is_vegetarian']=False 
    else:
        request.form.to_dict()['is_vegetarian']=True
        
    if 'category_name' not in request.form:
        request.form.to_dict()['category_name']="Unknown" 
    else:
        request.form.to_dict()['category_name']=True
    
    recipes.update( {'_id':ObjectId(recipe_id)},
        {
            'recipe_name' : request.form['recipe_name'],
            'category_name' : request.form['category_name'],
            'recipe_desc' : request.form['recipe_desc'],
        })
    return redirect(url_for('get_recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    categories = mongo.db.categories
    mongo.db.recipes.remove({'_id' : ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/get_categories')
def get_categories():
    return render_template('categories.html', categories=mongo.db.categories.find())
    
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    categories = mongo.db.categories
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))
    
@app.route('/insert_category', methods=['POST'])
def insert_category():
        categories = mongo.db.categories
        category_doc = {'category_name': request.form['category_name']}
        categories.insert_one(category_doc)
        return redirect(url_for('get_categories'))

@app.route('/new_category')
def new_category():
    categories = mongo.db.categories
    return render_template('addcategory.html')
        
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    categories = mongo.db.categories
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))
    
@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    categories = mongo.db.categories
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form['category_name']})
    return redirect(url_for('get_categories'))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)