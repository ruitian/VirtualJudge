from flask import Blueprint
from .solution import (
    SolutionListView
)

bp_solution = Blueprint('solution', __name__)

bp_solution.add_url_rule(
    '',
    endpoint='list',
    view_func=SolutionListView.as_view('list'),
    methods=['get', 'post']
)
