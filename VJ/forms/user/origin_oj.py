from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import Required, ValidationError

class OriginOJForm(Form):
    origin_oj = SelectField('OJ',
        choices=[
            ('poj', 'POJ'),
            ('hdu', 'HDU'),
            ('sdut', 'SDUT'),
            ('fzu', 'FZU')
        ]
    )
    username = StringField('Username')
    password = PasswordField('Password')
