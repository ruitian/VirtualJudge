from flask import Blueprint
from .user import (
    UserView,
    FollowView,
    UnFollowView,
    FollowersView,
    FollowingView
)

bp_user = Blueprint('user', __name__)

bp_user.add_url_rule(
    '/<username>',
    endpoint='user',
    view_func=UserView.as_view('user'),
    methods=['get']
)

bp_user.add_url_rule(
    '/follow/<username>',
    endpoint='follow',
    view_func=FollowView.as_view('follow'),
    methods=['get']
)

bp_user.add_url_rule(
    '/unfollow/<username>',
    endpoint='unfollow',
    view_func=UnFollowView.as_view('unfollow'),
    methods=['get']
)

bp_user.add_url_rule(
    '/followers/<username>',
    endpoint='followers',
    view_func=FollowersView.as_view('followers'),
    methods=['get']
)

bp_user.add_url_rule(
    '/following/<username>',
    endpoint='following',
    view_func=FollowingView.as_view('following'),
    methods=['get']
)

from .setting import *  # noqa
