#!/usr/bin/env python

import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    headers = flask.request.headers
    headers_dict = dict(headers)
    print("headers = ", headers)
    return "Request headers:\n" + str(headers)
