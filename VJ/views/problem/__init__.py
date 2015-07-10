from flask import Blueprint
from .problem import ProblemListView, ProblemDetailView

bp_problem = Blueprint('problem', __name__)

bp_problem.add_url_rule(
    '',
    endpoint = 'problem',
    view_func = ProblemListView.as_view('problem'),
    methods = ['get', 'post']
)

bp_problem.add_url_rule(
    '/<origin_oj>/<problem_id>',
    endpoint = 'detail',
    view_func = ProblemDetailView.as_view('detail'),
    methods = ['get', 'post']
)
