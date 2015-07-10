#-*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms.validators import Email, Required, EqualTo, Length

class RegisterForm(Form):
    username = StringField(u'用户名', [Length(min=4, max=25)])
    email = StringField(u'邮箱', [Required(), Email()])
    password = PasswordField(u'密码', [
        Required(),
        EqualTo('confirm', message=u'密码')
    ])
    confirm = PasswordField(u'重复密码')
