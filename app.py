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
@app.route('/login')
def login():
    if request.method == "POST":
        # Checks if the username is in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        # If the username is in the database, check if the password is correct
        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                # If the password is correct, set the session to the username
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
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
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

    # If the user is logged in, show their profile
    # otherwise redirect to the login page
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# Tells App where to run
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)