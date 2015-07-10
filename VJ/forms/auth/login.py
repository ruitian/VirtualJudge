#-*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import PasswordField, StringField, BooleanField, SubmitField
from wtforms.validators import Email, Required, ValidationError

from VJ.models import UserModel

class LoginForm(Form):
    email = StringField(u'邮箱', [Required(), Email()])
    password = PasswordField(u'密码', [Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

    def validate_password(self, field):
        user = UserModel.objects.filter(
            email=self.email.data
        ).first()
        if user is not None and user.verify_password(field.data):
            self.user = user
        else:
            raise ValidationError('邮箱或密码错误')
