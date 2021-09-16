# imports
import os
from flask import Flask, flash, render_template, request, session, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo.message import query
from werkzeug.security import generate_password_hash, check_password_hash

# imports environment variables if path to "env.py" is found
if os.path.exists("env.py"):
    import env

# creates instance of Flask app
app = Flask(__name__)

# Grabs database name, connection URI, and secret key from env.py
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Creates an instance of the PyMongo class to work with MongoDB
mongo = PyMongo(app)


# Route for the home page
@app.route('/')
@app.route("/home")
def home():
    return render_template("index.html")


# Route for the recipe page
@app.route('/recipes')
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# Route for the login page
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks if the username is in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If the username is in the database, check if the password is correct
        if existing_user:
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                user = mongo.db.users.find_one(
                    {"username": request.form.get("username").lower()})
                # Check if the user is an admin
                if user["is_admin"]:
                    session["is_admin"] = True
                else:
                    session["is_admin"] = False
                flash("Welcome back, {}".format(
                    request.form.get("username").capitalize()))
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        else:
            # User isn't in the database
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))
    return render_template("login.html")


# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # Checks if username is in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If username is already in the database, flash error message
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # If username is not in the database, register the user
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into a "session" cookie\
        # so the user can be logged in
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Route for the Profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grabs the session users's username from the database
    username = mongo.db.users.find_one({"username":
                                        session["user"]})["username"]

    # If the user has submitted recipes, retrieve them
    recipes = list(mongo.db.recipes.find({"created_by": session["user"]}))

    # If the user is logged in, show their profile
    # otherwise redirect to the login page
    if session["user"]:
        return render_template("profile.html",
                               username=username,
                               recipes=recipes)

    return redirect(url_for("login"))


# Route for the logging out
@app.route("/logout")
def logout():
    # Remove the user's session cookie
    session.pop("user", None)
    flash("You have been logged out")
    return redirect(url_for("home"))


# Route for adding a recipe
@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "image_url": request.form.get("image_url"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "prep_time": request.form.get("prep_time"),
            "serves": request.form.get("serves"),
            "created_by": session["user"].lower()
        }
        # Inserts the recipe into the database
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("name", 1)
    return render_template("add_recipes.html", categories=categories)


# Route for editing a recipe
@app.route("/edit_recipes/<recipe_id>", methods=["GET", "POST"])
def edit_recipes(recipe_id):
    # Grabs recipe from database
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if request.method == "POST":
        # Grabs the recipe details from the form and stores them in a dictionary
        recipe_details = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "image_url": request.form.get("image_url"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "prep_time": request.form.get("prep_time"),
            "serves": request.form.get("serves"),
            "created_by": session["user"].lower()
        }
        # Updates the recipe in the database
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, recipe_details)
        flash("Recipe updated")
        return redirect(url_for("recipes"))

    # Grabs the categories from the database
    categories = mongo.db.categories.find().sort("name", 1)
    return render_template("edit_recipes.html",
                           recipe=recipe,
                           categories=categories)


# Route to see the full recipe
@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    # Grabs the recipe from the database
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("full_recipe.html", recipe=recipe)


# Route for user to delete their own recipes
@app.route("/delete_own_recipes/<recipe_id>")
def delete_own_recipes(recipe_id):
    # Deletes the recipe from the database
    mongo.db.recipes.remove({
        "_id": ObjectId(recipe_id),
        "created_by":
        session["user"].lower()  # Checks if the user is the creator
    })
    flash("Recipe deleted")
    return redirect(url_for(
        "profile",
        username=session["user"]))  # Redirects to the user's profile page


# Route for admin to get and manage all categories
@app.route("/manage_categories")
def manage_categories():
    # Grabs all categories from the database
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("manage_categories.html", categories=categories)



# Route for admin to create a new category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # Grabs the category details from the form and stores them in a dictionary
        category_details = {
            "category_name": request.form.get("category_name")
        }
        # Inserts the category into the database
        mongo.db.categories.insert_one(category_details)
        flash("New category added")
        return redirect(url_for("manage_categories"))
    return render_template("add_category.html")


# Route for admin to edit a category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # Grabs the category from the database
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    if request.method == "POST":
        # Grabs the category details from the form and stores them in a dictionary
        category_details = {
            "category_name": request.form.get("category_name")
        }
        # Updates the category in the database
        mongo.db.categories.update({"_id": ObjectId(category_id)},
                                   category_details)
        flash("Category updated")
        return redirect(url_for("manage_categories"))

    return render_template("edit_category.html", category=category)


# Route for admin to delete a category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    # Deletes the category from the database
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category deleted")
    return redirect(url_for("manage_categories"))


# Tells App where to run
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)