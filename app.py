# -*- coding: utf-8 -*-

"""
Basic flask API
"""

#from flask import Flask, jsonify, request, Response
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import mongoengine_goodjson as gj
from flask_restful import Api
# our libs
from database.db import initialize_db
from database.models import Movie
from resources.errors import errors
# mail
from flask_mail import Mail

# creds
import creds

# instantiate app
app = Flask(__name__)

# import JWT key
app.config["JWT_SECRET_KEY"] = creds.JWT_SECRET_KEY

#mail settings
app.config["MAIL_SERVER"] = creds.MAIL_SERVER
app.config["MAIL_PORT"] = creds.MAIL_PORT
app.config["MAIL_USERNAME"] = creds.MAIL_USERNAME
app.config["MAIL_PASSWORD"] = creds.MAIL_PASSWORD

# Add mail before routes to avoid circular dependancies.
mail = Mail(app)
from resources.routes import initialize_routes

# create api, bcrypt and jwt instances
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# MongoDB config
# must add the db name to the end of 'host' or actions revert to the 'test' db.
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://storage/movie-bag',
    'db': 'movie-bag',
    'port': 27017,
    'username': creds.mongouser,
    'password': creds.mongopassword,
    'authentication_source': 'admin',
    'authentication_mechanism': 'SCRAM-SHA-1'
}

initialize_db(app)
initialize_routes(api)

# moved app.run into run.py
