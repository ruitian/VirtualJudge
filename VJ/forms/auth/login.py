#-*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms.validators import Email, Required

class LoginForm(Form):
    pass
