from flask_wtf import Form
from wtforms import StringField


class UpdateProfileForm(Form):
    school = StringField('School')
    blog_url = StringField('URL')
    location = StringField('Location')
