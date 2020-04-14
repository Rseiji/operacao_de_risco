from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from . import db
from project.config import Config


#db = SQLAlchemy()
bcrypt = Bcrypt()

#mail = Mail()


app = Flask(__name__)
#app.config.from_object(Config)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt.init_app(app)
#login_manager.init_app(app)
#mail.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from project.routes import index, voo, aluno, usuario, instrutor, login

'''
def create_app():
    #app = ...
    # existing code omitted

    from . import db
    db.init_app(app)returnapp

   '''