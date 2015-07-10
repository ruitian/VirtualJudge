#-*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import (
    Email,
    Required,
    EqualTo,
    Length,
    ValidationError
)

from VJ.models import UserModel

class RegisterForm(Form):
    username = StringField(u'用户名', [Required(), Length(min=4, max=25)])
    email = StringField(u'邮箱', [Required(), Email()])
    password = PasswordField(u'密码', [
        Required(),
        EqualTo('confirm', message=u'密码必须一样')
    ])
    confirm = PasswordField(u'重复密码')
    submit = SubmitField(u'注册')

    def validate_username(self, field):
        if UserModel.objects.filter(username=field.data):
            raise ValidationError(u'当前用户名已被注册')

    def validate_email(self, field):
        if UserModel.objects.filter(email=field.data):
            raise ValidationError(u'邮箱已经注册')

    def register(self):
        return UserModel.create_user(
            username=self.username.data,
            email=self.email.data,
            password=self.password.data
        )
