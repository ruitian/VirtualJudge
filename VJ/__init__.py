#-*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine
from flask.ext.mail import Mail
from flask.ext.security import Security, MongoEngineUserDatastore
from config import config

from models import User, Role

app = Flask(__name__)
db = MongoEngine()
mail = Mail()
login_manager = LoginManager()
security = Security()

with app.app_context():
    config_name = os.getenv('FLASK_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)

    user_datastore = MongoEngineUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    login_manager.init__app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'login'

from views import *
