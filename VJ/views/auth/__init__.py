from flask import Blueprint
from .register import RegisterView
from .login import LoginView
from .logout import LogoutView

bp_auth = Blueprint('auth', __name__)

bp_auth.add_url_rule(
    '/register',
    endpoint = 'register',
    view_func = RegisterView.as_view('register'),
    methods = ['get', 'post']
)

bp_auth.add_url_rule(
    '/login',
    endpoint = 'login',
    view_func = LoginView.as_view('login'),
    methods = ['get', 'post']
)

bp_auth.add_url_rule(
    '/logout',
    endpoint = 'logout',
    view_func = LogoutView.as_view('logout'),
    methods = ['get']
)
