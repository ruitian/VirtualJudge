from flask import Blueprint
from .user import UserView

bp_user = Blueprint('user', __name__)

bp_user.add_url_rule(
    '/<username>',
    endpoint='user',
    view_func=UserView.as_view('user'),
    methods=['get']
)

from .setting import *  # noqa
