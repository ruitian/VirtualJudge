# -*- coding: utf-8 -*-

from flask import (  # noqa
    request,
    redirect,
    url_for,
    flash,
    render_template
)
from flask.views import MethodView
from flask.ext.login import login_user

from VJ.forms import RegisterForm
from VJ.libs.tasks import send_email


class RegisterView(MethodView):

    template = 'auth/register.html'

    def get(self):
        form = RegisterForm()
        return render_template(self.template, form=form)

    def post(self):
        form = RegisterForm()
        if not form.validate():
            return render_template(self.template, form=form)
        user = form.register()
        token = user.generate_confirmation_token()
        send_email.delay(
            user.email,
            'Confirm Your Account',
            'auth/email/confirm',
            user=user,
            token=token
        )
        flash('A confirmation email has been sent to you by email')
        login_user(user)
        return redirect(url_for('index.index'))
