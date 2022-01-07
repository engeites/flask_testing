
from time import time
from flask import Flask, jsonify, request, url_for, render_template

from API_classes import PriceObtainer, AllCurrencies
from database import Database

app = Flask(__name__)
db = Database()


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
def return_token_price(token):
    getter = PriceObtainer(token)
    price = getter.run()
    db.add_entry(price['last_price'])
    return price


@app.route("/currs")
def get_currs():
    currencies = AllCurrencies()
    text = currencies.run()
    return render_template('currs.html', info=text)


@app.route("/")
def index():
    return render_template('index.html')
