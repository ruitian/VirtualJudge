#-*- coding: utf-8 -*-
from flask import (
    request,
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView
from flask.ext.login import current_user

from VJ.forms import LoginForm

class LoginView(MethodView):

    template = 'auth/login.html'

    def get(self):
        if current_user.is_authenticated():
            return redirect(url_for('index.index'))
        form = LoginForm()
        return render_template(self.template, form=form)

    def post(self):
        pass
        '''
        form = LoginForm()
        if not form.validate():
            return render_template(
                self.template, form=form)
        query = UserModel.query
        user = (query.filter_by(email=form.login_name.data).first()
                or query.filter_by(username=form.login_name.data).first())
        if user is not None and user.verify_password(form.password.data):
            user_login(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index.index'))
        flash('用户名或密码不正确')
        return render_template(self.template, form=form)
        '''
