# -*- coding: utf-8 -*-

from flask import Blueprint, request, flash, redirect, url_for
from flask.ext.login import current_user
from .register import RegisterView
from .login import LoginView
from .logout import LogoutView
from .views import ConfirmView, UnConfirmedView, ResendConfirmationView

bp_auth = Blueprint('auth', __name__)


@bp_auth.before_app_request
def before_request():
    if current_user.is_authenticated() \
            and not current_user.active \
            and request.endpoint[:5] != 'auth.' \
            and request.endpoint != 'static':
        flash('You account is forbiddened')
        return redirect(url_for('index.index'))

bp_auth.add_url_rule(
    '/register',
    endpoint='register',
    view_func=RegisterView.as_view('register'),
    methods=['get', 'post']
)

bp_auth.add_url_rule(
    '/login',
    endpoint='login',
    view_func=LoginView.as_view('login'),
    methods=['get', 'post']
)

bp_auth.add_url_rule(
    '/logout',
    endpoint='logout',
    view_func=LogoutView.as_view('logout'),
    methods=['get']
)

bp_auth.add_url_rule(
    '/confirm/<token>',
    endpoint='confirm',
    view_func=ConfirmView.as_view('confirm'),
    methods=['get']
)

bp_auth.add_url_rule(
    '/unconfirmed',
    endpoint='unconfirmed',
    view_func=UnConfirmedView.as_view('unconfirmed'),
    methods=['get']
)

bp_auth.add_url_rule(
    '/confirm',
    endpoint='resend_confirmation',
    view_func=ResendConfirmationView.as_view('resend_confirmation'),
    methods=['get']
)
