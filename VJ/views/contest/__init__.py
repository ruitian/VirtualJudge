from flask import Blueprint
from .contest import (
    ContestListView,
    ContestPendingView,
    ContestRunningView,
    ContestEndedView,
    ContestCreateView,
    ContestEditView,
    ContestDetailView,
    ContestProblemView
)

bp_contest = Blueprint('contest', __name__)

bp_contest.add_url_rule(
    '',
    endpoint='list',
    view_func=ContestListView.as_view('list'),
    methods=['get', 'post']
)

bp_contest.add_url_rule(
    '/pending',
    endpoint='pending',
    view_func=ContestPendingView.as_view('pending'),
    methods=['get', 'post']
)

bp_contest.add_url_rule(
    '/running',
    endpoint='running',
    view_func=ContestRunningView.as_view('running'),
    methods=['get', 'post']
)

bp_contest.add_url_rule(
    '/ended',
    endpoint='ended',
    view_func=ContestEndedView.as_view('ended'),
    methods=['get', 'post']
)

bp_contest.add_url_rule(
    '/create',
    endpoint='create',
    view_func=ContestCreateView.as_view('create'),
    methods=['get', 'post']
)

bp_contest.add_url_rule(
    '/<int:contest_id>',
    endpoint='detail',
    view_func=ContestDetailView.as_view('detail'),
    methods=['get', 'post']
)

bp_contest.add_url_rule(
    '/edit/<int:contest_id>',
    endpoint='edit',
    view_func=ContestEditView.as_view('edit'),
    methods=['get', 'post']
)

bp_contest.add_url_rule(
    '/<int:contest_id>/problem/<index>',
    endpoint='problem',
    view_func=ContestProblemView.as_view('problem'),
    methods=['get', 'post']
)
