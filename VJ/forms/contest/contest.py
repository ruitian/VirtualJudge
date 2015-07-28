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
from wtforms.validators import Required, ValidationError, Length
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
    delete = SubmitField('Delete')

    def validate_delete(self, field):
        pass

    def validate_problem_id(self, field):
        if not ProblemItem.objects(
            origin_oj=self.origin_oj.data,
            problem_id=field.data
        ).first():
            raise ValidationError('Problem Id is required')


class ContestCreateForm(Form):
    title = StringField(
        'Contest Title',
        [Required(), Length(max=64)],
        default='The king asked me to look for the mountains. ',
    )
    contest_type = SelectField(
        'Contest Type',
        [Required()],
        choices=[
            ('public', 'Public'),
            ('private', 'Private'),
        ]
    )
    password = PasswordField('Password')
    start_at = DateTimeField(
        'Start Time',
        [Required()],
        default=datetime.now,
    )
    end_at = DateTimeField(
        'End Time',
        [Required()],
        default=datetime.now,
    )
    description = TextAreaField('Description')
    problems = FieldList(FormField(ProblemForm), max_entries=26)
    remove = SubmitField()
    add = SubmitField()

    def validate_end_at(self, field):
        try:
            if field.data < self.start_at.data:
                raise ValidationError(
                    'End time is not greater than start time'
                )
        except:
            raise ValidationError(
                'Invalid start or end time format'
            )

    def validate_remove(self, field):
        pass

    def validate_add(self, field):
        pass

    def validate_password(self, field):
        if self.contest_type.data == 'private' and not field.data:
            raise ValidationError('Private contest this field is required')

    def generate_contest(self):
        return ContestModel.create_contest(
            title=self.title.data,
            contest_type=self.contest_type.data,
            password=self.password.data,
            start_at=self.start_at.data,
            end_at=self.end_at.data,
            description=self.description.data
        )


class ContestEditForm(ContestCreateForm):

    def validate_password(self, field):
        pass

    def validate_contest_type(self, field):
        pass
