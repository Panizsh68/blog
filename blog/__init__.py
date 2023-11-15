from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__) 
app.config['SECRET_KEY'] = '1fcb387e8aeda6dee45c5c024dd9a548'
app.config['TEMPLATES_AUTO_RELOAD'] = True 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.app_context().push()

from blog import routes