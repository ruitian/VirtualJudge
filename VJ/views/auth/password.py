# -*- coding: utf-8 -*-

from flask import (  # noqa
    request,
    redirect,
    url_for,
    flash,
    render_template
)
from flask.views import MethodView
from flask.ext.login import current_user

from VJ.libs.tasks import send_email
from VJ.forms import PasswordResetRequestForm, PasswordResetForm
from VJ.models import UserModel


class PasswordResetRequestView(MethodView):

    template = 'auth/reset_password_request.html'

    def get(self):
        if not current_user.is_anonymous():
            return redirect(url_for('index.index'))
        form = PasswordResetRequestForm()
        return render_template(self.template, form=form)

    def post(self):
        form = PasswordResetRequestForm()
        if not form.validate():
            return render_template(self.template, form=form)
        user = UserModel.objects(email=form.email.data).first()
        if user:
            token = user.generate_reset_token()
            send_email(
                user.email,
                'Reset Your Password',
                'auth/email/reset_password',
                user=user, token=token,
                next=request.args.get('next')
            )
        flash('An email with instructions to reset your password has been '
              'sent to you.')
        return redirect(url_for('index.index'))


class PasswordResetView(MethodView):

    template = 'auth/reset_password.html'

    def get(self, token):
        if not current_user.is_anonymous():
            return redirect(url_for('index.index'))
        form = PasswordResetForm()
        return render_template(self.template, form=form)

    def post(self, token):
        form = PasswordResetForm()
        if not form.validate():
            return render_template(self.template, form=form)
        user = UserModel.objects(email=form.email.data).first()
        if user is None:
            return redirect('index.index')
        if user.reset_password(token, form.password.data):
            flash('Your password has been updated.')
            return redirect(url_for('index.index'))
        else:
            return redirect(url_for('index.index'))
