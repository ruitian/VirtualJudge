from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, PasswordField
from wtforms.validators import Required, ValidationError

from VJ.models import AccountItem

class OriginOJAccountForm(Form):
    origin_oj = StringField('OJ')
    username = StringField('Username')
    password = PasswordField('Password')

    def generate_account(self):
        return AccountItem(
            origin_oj = self.origin_oj.data,
            username = self.username.data,
            password = self.password.data
        )
