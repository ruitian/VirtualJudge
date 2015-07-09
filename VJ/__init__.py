#_*_ coding: UTF-8 _*_
import os
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine
from config import config

app = Flask(__name__)
db = MongoEngine()
login_manager = LoginManager()

with app.app_context():
    config_name = os.getenv('FLASK_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    login_manager.setup_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'login'

from views import *
