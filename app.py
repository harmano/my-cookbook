import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.secret_key = "randomstring123"

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://harmano:r00tUser1@cluster0-ejawl.mongodb.net/cookbook?retryWrites=true'

mongo = PyMongo(app)


@app.route('/', methods=["GET", "POST"])
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
            recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', 
            cusine_type=mongo.db.cusine_type.find())
            
            
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipes/<recipe_id>')
def edit_recipes(recipe_id):
    the_recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cusine_type = mongo.db.cusine_type.find()
    return render_template('editrecipe.html', recipe=the_recipes, cusine_type=all_cusine_type)


@app.route('/update_recipes/<recipe_id>', methods=["POST"])
def update_recipes(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'author':request.form.get('author'),
        'name':request.form.get('name'),
        'ingredients':request.form.get('ingredients'),
        'instructions':request.form.get('instructions'),
        'picture':request.form.get('picture'),
        'profile_pic':request.form.get('profile_pic'),
        'cusine_cat':request.form.get('cusine_cat'),
       
    })
    return redirect(url_for('get_recipes'))

@app.route('/delete_recipes/<recipe_id>')
def delete_recipes(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 
            
