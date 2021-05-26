#!/usr/bin/env python

import flask
from random import choice
app = flask.Flask(__name__)

animals = ['cat', 'dog', 'moose']

@app.route("/", methods=['GET', 'POST'])
def index():
    return "None"

@app.route("/animals", methods=['GET', 'POST'])
def get_animals():
    return ",".join(animals)

@app.route("/animal", methods=['GET', 'POST'])
def get_animal():
    return choice(animals)

@app.route("/addAnimal", methods=['GET', 'POST'])
def add_animal():
    headers = flask.request.headers
    if 'animal' in headers:
        new_animal = headers['animal']
        animals.append(new_animal)
    return str(len(animals))
