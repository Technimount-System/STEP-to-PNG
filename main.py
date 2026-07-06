
from flask import Flask, request, jsonify, Blueprint
from util.render import render
from api import register_blueprints


app = Flask(__name__)

register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)