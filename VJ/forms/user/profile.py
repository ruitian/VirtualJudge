from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import URL


class ProfileForm(Form):
    nickname = StringField('Name')
    school = StringField('School')
    location = StringField('Location')
    blog_url = StringField('Blog URL', [URL()])
    submit = SubmitField('Update profile')
