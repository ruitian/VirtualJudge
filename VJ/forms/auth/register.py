# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import (
    Email,
    Required,
    EqualTo,
    Regexp,
    Length,
    ValidationError
)

from VJ.models import UserModel


class RegisterForm(Form):
    username = StringField(
        'Username',
        [
            Required(),
            Length(4, 11),
            Regexp(
                '^[A-Za-z][A-Za-z0-9_.]*$', 0,
                'Username must have only letters, '
                'numbers, dots or underscores'
            )
        ]
    )
    email = StringField('Email', [Required(), Email()])
    password = PasswordField('Password', [
        Required(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_username(self, field):
        if UserModel.objects(username=field.data):
            raise ValidationError('Username already in use')

    def validate_email(self, field):
        if UserModel.objects(email=field.data):
            raise ValidationError('Email has already been registered')

    def register(self):
        return UserModel.create_user(
            username=self.username.data,
            email=self.email.data,
            password=self.password.data
        )
