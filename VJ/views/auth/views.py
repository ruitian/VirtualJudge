# -*- coding: utf-8 -*-

from flask import (  # noqa
    request,
    redirect,
    url_for,
    flash,
    render_template
)
from flask.views import MethodView
from flask.ext.login import current_user, login_required
from VJ.libs.tasks import send_email


class ConfirmView(MethodView):

    @login_required
    def get(self, token):
        if current_user.confirmed:
            return redirect(url_for('index.index'))
        if current_user.confirm(token):
            flash('You have confirmed your account. Thanks!')
        else:
            flash('The confirmation link is invalid or has expired.')

        return redirect(url_for('index.index'))


class UnConfirmedView(MethodView):

    template = 'auth/unconfirmed.html'

    def get(self):
        if current_user.is_anonymous() or current_user.confirmed:
            return redirect(url_for('index.index'))
        return render_template(self.template)


class ResendConfirmationView(MethodView):

    @login_required
    def get(self):
        token = current_user.generate_confirmation_token()
        send_email(
            current_user.email,
            'Confirm Your Account',
            'auth/email/confirm',
            user=current_user,
            token=token
        )
        flash('A new confirmation email has been sent to you by email')
        return redirect(url_for('index.index'))
