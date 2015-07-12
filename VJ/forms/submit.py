from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import Required, ValidationError

from VJ.models import SolutionItem

class SubmitForm(Form):
    origin_oj = StringField('OJ', [Required()])
    problem_id = StringField('Problem ID', [Required()])
    language = SelectField('Language',
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
    code = TextAreaField('Code', [Required()])

    def submit(self):
        return SolutionItem.create_solution(
            origin_oj = self.origin_oj.data,
            problem_id = self.problem_id.data,
            language = self.language.data,
            code = self.code.data
        )
