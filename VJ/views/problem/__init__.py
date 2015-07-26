from flask import Blueprint
from .problem import (
    ProblemListView,
    ProblemDetailView,
    ProblemGetView
)
from .submit import ProblemSubmitView

bp_problem = Blueprint('problem', __name__)

bp_problem.add_url_rule(
    '/get',
    endpoint = 'get',
    view_func = ProblemGetView.as_view('get'),
    methods = ['get']
)

bp_problem.add_url_rule(
    '',
    endpoint = 'list',
    view_func = ProblemListView.as_view('list'),
    methods = ['get', 'post']
)

bp_problem.add_url_rule(
    '/<origin_oj>/<problem_id>',
    endpoint = 'detail',
    view_func = ProblemDetailView.as_view('detail'),
    methods = ['get']
)

bp_problem.add_url_rule(
    '/submit',
    endpoint = 'submit',
    view_func = ProblemSubmitView.as_view('submit'),
    methods = ['get', 'post']
)
