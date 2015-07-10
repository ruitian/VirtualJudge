from flask import (
    request,
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView
from flask.ext.login import login_user

from VJ.forms import RegisterForm

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
        login_user(user)
        return redirect(url_for('index.index'))
