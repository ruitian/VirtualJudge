# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import Email, Required, ValidationError, EqualTo

from VJ.models import UserModel


class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[Required()])
    password = PasswordField(
        'New password',
        validators=[
            Required(),
            EqualTo('confirm', message='Passwords must match')
        ]
    )
    confirm = PasswordField('Confirm new password', validators=[Required()])
    submit = SubmitField('Update Password')


class PasswordResetRequestForm(Form):
    email = StringField('Email', validators=[Required(), Email()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if not UserModel.objects(email=self.email.data):
            raise ValidationError('Email is invalid')


class PasswordResetForm(Form):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField(
        'New Password',
        validators=[
            Required(), EqualTo('confirm', message='Passwords must match')
        ]
    )
    confirm = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if not UserModel.objects(email=field.data):
            raise ValidationError('Unknown email address.')
