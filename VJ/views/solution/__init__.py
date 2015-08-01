from flask import Blueprint
from .solution import (
    SolutionListView,
    SolutionDetailView
)

bp_solution = Blueprint('solution', __name__)

bp_solution.add_url_rule(
    '',
    endpoint='list',
    view_func=SolutionListView.as_view('list'),
    methods=['get', 'post']
)

bp_solution.add_url_rule(
    '/<int:solution_id>',
    endpoint='detail',
    view_func=SolutionDetailView.as_view('detail'),
    methods=['get']
)
