from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import Required, ValidationError, Length

from VJ.models import SolutionItem
from VJ.models import ProblemItem

lang = {
    'poj': [
        ('g++', 'G++'),
        ('gcc', 'GCC'),
        ('pascal', 'Pascal'),
        ('java', 'Java'),
        ('c++', 'C++'),
        ('c', 'C'),
        ('fortran', 'Fortran'),
    ],
    'hdu': [
        ('g++', 'G++'),
        ('gcc', 'GCC'),
        ('pascal', 'Pascal'),
        ('java', 'Java'),
        ('c++', 'C++'),
        ('c', 'C'),
        ('c#', 'C#'),
    ],
    'sdut': [
        ('gcc', 'GCC'),
        ('g++', 'G++'),
        ('java', 'Java'),
        ('pascal', 'Pascal'),
        ('go', 'Go'),
        ('lua', 'Lua'),
        ('dao', 'Dao'),
        ('perl', 'Perl'),
        ('ruby', 'Ruby'),
        ('haskell', 'Haskell'),
        ('python2', 'Python2'),
        ('python3', 'Python3')
    ],
    'fzu': [
        ('g++', 'G++'),
        ('gcc', 'GCC'),
        ('pascal', 'Pascal'),
        ('java', 'Java'),
        ('c++', 'C++'),
        ('c', 'C'),
    ]
}


class SubmitForm(Form):
    origin_oj = StringField('OJ', [Required()])
    problem_id = StringField('Problem ID', [Required()])
    language = SelectField(
        'Language',
        choices=[
            ('gcc', 'GCC'),
            ('g++', 'G++'),
            ('java', 'Java'),
            ('pascal', 'Pascal'),
            ('c', 'C'),
            ('c++', 'C++'),
            ('fortran', 'Fortran'),
            ('c#', 'C#'),
            ('go', 'Go'),
            ('lua', 'Lua'),
            ('dao', 'Dao'),
            ('perl', 'Perl'),
            ('ruby', 'Ruby'),
            ('haskell', 'Haskell'),
            ('python2', 'Python2'),
            ('python3', 'Python3')
        ],
        validators=[Required()]
    )
    code = TextAreaField('Code', [Required(), Length(min=4)])

    def __init__(self, origin_oj, problem_id, *args, **kwargs):
        super(SubmitForm, self).__init__(*args, **kwargs)
        self.origin_oj.data = origin_oj
        self.problem_id.data = problem_id
        self.language.choices = lang[origin_oj]

    def validate_origin_oj(self, field):
        if not ProblemItem.objects.filter(origin_oj=field.data):
            raise ValidationError('Invalid origin oj')

    def validate_problem_id(self, field):
        if not ProblemItem.objects.filter(
                origin_oj=self.origin_oj.data,
                problem_id=field.data):
            raise ValidationError('Invalid problem id')

    def generate_solution(self):
        return SolutionItem.create_solution(
            origin_oj=self.origin_oj.data,
            problem_id=self.problem_id.data,
            language=self.language.data,
            code=self.code.data
        )
