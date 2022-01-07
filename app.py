import sqlite3
from time import time
from flask import Flask, jsonify, request, url_for, render_template

from scraping import PriceFinder

app = Flask(__name__)
 

@app.route("/class", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form.get('lname')
        some_json = request.form.values()
        return jsonify({"You sent": next(some_json)}), 200
    if request.method == "GET":
        return jsonify({"about": "My first app!"})


@app.route("/time")
def return_time():
    return jsonify({'current time': time()})


@app.route("/crypto/<string:token>")
def return_token_price(token: str):
    getter = PriceFinder(token)
    return jsonify({token: getter.run()})


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/help/<user>")
def help(user):
    return f"Help page just for you, {user}!"
