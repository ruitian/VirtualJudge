from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import (  # noqa
    Email,
    Required,
    EqualTo,
    Regexp,
    Length,
    ValidationError
)


class ProfileForm(Form):
    name = StringField('Name')
    school = StringField('School')
    blog_url = StringField('Blog URL')
    location = StringField('Location')
