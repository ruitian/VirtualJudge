from flask import Blueprint
from .profile import ProfileView

bp_user = Blueprint('user', __name__)

bp_user.add_url_rule(
    '/profile',
    endpoint = 'profile',
    view_func = ProfileView.as_view('profile'),
    methods = ['get', 'post']
)
