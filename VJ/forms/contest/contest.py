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
from wtforms.validators import Required, ValidationError
from datetime import datetime

from VJ.models import ContestModel, ProblemItem


class ProblemForm(Form):
    origin_oj = SelectField(
        'Origin OJ',
        choices=[
            ('poj', 'POJ'),
            ('hdu', 'HDU'),
            ('sdut', 'SDUT'),
            ('fzu', 'FZU')
        ],
    )
    problem_id = StringField('Problem ID', [Required()])
    title = StringField('Title')

    def validate_problem_id(self, field):
        if not ProblemItem.objects(
            origin_oj=self.origin_oj.data,
            problem_id=field.data
        ).first():
            raise ValidationError('Problem Id is required')


class ContestForm(Form):
    title = StringField(
        'Contest Title',
        [Required()],
        default='The king asked me to look for the mountains. ',
        )
    password = PasswordField('Password')
    start_at = DateTimeField(
        'Start Time',
        [Required()],
        default=datetime.now,
    )
    end_at = DateTimeField(
        'End Time',
        [Required()]
    )
    description = TextAreaField('Description')
    problems = FieldList(FormField(ProblemForm))
    remove = SubmitField()
    add = SubmitField()

    def validate_end_at(self, field):
        if field.data < self.start_at.data:
            raise ValidationError('End time is not greater than start time')

    def validate_remove(self, field):
        pass

    def validate_add(self, field):
        pass

    def generate_contest(self):
        return ContestModel.create_contest(
            title=self.title.data,
            password=self.password.data,
            start_at=self.start_at.data,
            end_at=self.end_at.data,
            description=self.description.data
        )
