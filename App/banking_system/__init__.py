from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:kali@db:3306/bank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SALT'] = environ.get('SALT')
db = SQLAlchemy(app)

from banking_system import routes
