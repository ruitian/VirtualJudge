from flask import Blueprint
from .user import UserView
from .profile import ProfileView
from .origin_oj import (
    OriginOJView,
    PojView,
    HduView,
    SdutView,
    FzuView
)

bp_user = Blueprint('user', __name__)

bp_user.add_url_rule(
    '/<username>',
    endpoint = 'user',
    view_func = UserView.as_view('user'),
    methods = ['get']
)

bp_user.add_url_rule(
    '/settings/profile',
    endpoint = 'profile',
    view_func = ProfileView.as_view('profile'),
    methods = ['get', 'post']
)

bp_user.add_url_rule(
    '/settings/origin_oj',
    endpoint = 'origin_oj',
    view_func = OriginOJView.as_view('origin_oj'),
    methods = ['get', 'post']
)

bp_user.add_url_rule(
    '/settings/origin_oj/poj',
    endpoint = 'poj',
    view_func = PojView.as_view('poj'),
    methods = ['get', 'post']
)

bp_user.add_url_rule(
    '/settings/origin_oj/hdu',
    endpoint = 'hdu',
    view_func = HduView.as_view('hdu'),
    methods = ['get', 'post']
)

bp_user.add_url_rule(
    '/settings/origin_oj/sdut',
    endpoint = 'sdut',
    view_func = SdutView.as_view('sdut'),
    methods = ['get', 'post']
)

bp_user.add_url_rule(
    '/settings/origin_oj/fzu',
    endpoint = 'fzu',
    view_func = FzuView.as_view('fzu'),
    methods = ['get', 'post']
)
