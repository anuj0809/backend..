from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import json
import os
from config import app, db
from MovieApi.utils.commands import create_db, populate_db
from MovieApi.api.admin import *
from MovieApi.api.all import *
from flask_jwt_extended import JWTManager



jwt = JWTManager(app)

base = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base, 'movie_db')
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a secret key

db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
