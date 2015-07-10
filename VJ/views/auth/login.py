#-*- coding: utf-8 -*-
from flask import (
    request,
    redirect,
    url_for,
    flash,
    render_template
)
from flask.views import MethodView
from flask.ext.login import current_user, login_user

from VJ.forms import LoginForm

class LoginView(MethodView):

    template = 'auth/login.html'

    def get(self):
        if current_user.is_authenticated():
            return redirect(url_for('index.index'))
        form = LoginForm()
        return render_template(self.template, form=form)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            login_user(form.user)
        flash(u'登录成功')
        return redirect(url_for('index.index'))