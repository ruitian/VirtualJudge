from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import (  # noqa
    Email,
    Required,
    EqualTo,
    Regexp,
    Length,
    ValidationError
)


class ProfileForm(Form):
    nickname = StringField('Name')
    school = StringField('School')
    location = StringField('Location')
    blog_url = StringField('Blog URL')
    submit = SubmitField('Update profile')
