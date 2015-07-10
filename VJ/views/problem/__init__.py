from flask import Blueprint
from .problem import ProblemListView

bp_problem = Blueprint('problem', __name__)

bp_problem.add_url_rule(
    '',
    endpoint = 'problem',
    view_func = ProblemListView.as_view('problem'),
    methods = ['get', 'post']
)
