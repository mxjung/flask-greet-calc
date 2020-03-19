# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


# Adding route functions
@app.route("/add")
def add_route():
    "function to add a + b from imported"

    value_a = request.args["a"]
    value_b = request.args["b"]
    return str(add(int(value_a), int(value_b)))

@app.route("/sub")
def sub_route():
    "function to subtract a, b from imported"

    value_a = request.args["a"]
    value_b = request.args["b"]
    return str(sub(int(value_a), int(value_b)))

@app.route("/mult")
def mult_route():
    "function to multiply a, b from imported"

    value_a = request.args["a"]
    value_b = request.args["b"]
    return str(mult(int(value_a), int(value_b)))

@app.route("/div")
def div_route():
    "function to divide a, b from imported"

    value_a = request.args["a"]
    value_b = request.args["b"]
    return str(div(int(value_a), int(value_b)))