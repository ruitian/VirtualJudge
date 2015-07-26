from flask_wtf import Form
from wtforms import (
    StringField,
    SelectField,
    PasswordField,
    DateTimeField,
    TextAreaField,
    FieldList,
    SubmitField,
    FormField
)
from wtforms.validators import Email, Required, ValidationError
from datetime import datetime

class ProblemForm(Form):
    origin_oj = SelectField('Origin OJ',
        choices=[
            ('poj', 'POJ'),
            ('hdu', 'HDU'),
            ('sdut', 'SDUT'),
            ('fzu', 'FZU')
        ],
    )
    problem_id = StringField('Problem ID')
    title = StringField('Title')

class ContestForm(Form):
    title = StringField('Contest Title',
        default='The king asked me to look for the mountains. ')
    password = PasswordField('Password')
    start_at = DateTimeField('Start Time', default=datetime.now)
    end_at = DateTimeField('End Time')
    description = TextAreaField('Description')
    problems = FieldList(FormField(ProblemForm))
    remove = SubmitField()
    add = SubmitField()
