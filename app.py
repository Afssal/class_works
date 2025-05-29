#import package
from flask import Flask


#create instance of flask app
app = Flask(__name__)

#route
@app.route("/")

def hello_world():
    return "Hello world"

#different route
@app.route("/hello")

def hello():
    return "<h1>Hello world<h1>"


#mulitple route
@app.route("/route1")
@app.route("/route2")

def multi_route():

    return "<h2>This is mulitple route<h2>"