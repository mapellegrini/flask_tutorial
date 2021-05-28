#!/usr/bin/env python

#adapted from: https://geekflare.com/securing-flask-api-with-jwt/

#import flask
from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])  
def login_user(): 
    auth = request.authorization

    if not auth or not auth.username or not auth.password:  
        return make_response('could not verify',
                             401,
                             {'WWW.Authentication':
                              'Basic realm: "login required"'})    
 
    username = auth.username
    password = auth.password


    print(username, password)
    
    if check_password_hash(user.password, auth.password):  
        token = jwt.encode({'public_id': user.public_id,
                            'exp' : datetime.datetime.utcnow() + \
                            datetime.timedelta(minutes=30)},
                           app.config['SECRET_KEY'])  
        return jsonify({'token' : token.decode('UTF-8')}) 

    return make_response('could not verify',
                         401, {'WWW.Authentication':
                               'Basic realm: "login required"'})


