from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from decouple import config
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '899fa604ad88d2b6a64dfbef8f40a761'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = config('USER_EMAIL')
app.config['MAIL_PASSWORD'] = config('PASSWORD')
mail = Mail(app)
from flaskblog import routes