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

# Proof of concept
@app.route('/')
def hello():
    return "Hello World!"


# Tells App where to run
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)