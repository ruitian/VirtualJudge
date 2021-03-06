from VJ.views.user import bp_user
from .profile import ProfileView
from .account import AccountView
from .origin_oj import (
    OriginOJView,
    PojView,
    HduView,
    SdutView,
    FzuView
)

bp_user.add_url_rule(
    '/settings/profile',
    endpoint='profile',
    view_func=ProfileView.as_view('profile'),
    methods=['get', 'post']
)

bp_user.add_url_rule(
    '/settings/account',
    endpoint='account',
    view_func=AccountView.as_view('account'),
    methods=['get', 'post']
)

bp_user.add_url_rule(
    '/settings/origin_oj',
    endpoint='origin_oj',
    view_func=OriginOJView.as_view('origin_oj'),
    methods=['get', 'post']
)

bp_user.add_url_rule(
    '/settings/origin_oj/poj',
    endpoint='poj',
    view_func=PojView.as_view('poj'),
    methods=['get', 'post']
)

bp_user.add_url_rule(
    '/settings/origin_oj/hdu',
    endpoint='hdu',
    view_func=HduView.as_view('hdu'),
    methods=['get', 'post']
)

bp_user.add_url_rule(
    '/settings/origin_oj/sdut',
    endpoint='sdut',
    view_func=SdutView.as_view('sdut'),
    methods=['get', 'post']
)

bp_user.add_url_rule(
    '/settings/origin_oj/fzu',
    endpoint='fzu',
    view_func=FzuView.as_view('fzu'),
    methods=['get', 'post']
)
