import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://harmano:r00tUser1@cluster0-ejawl.mongodb.net/cookbook?retryWrites=true'

mongo = PyMongo(app)


@app.route('/')
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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 
            
