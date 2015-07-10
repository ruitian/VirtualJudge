from flask import (
    request,
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView

from VJ.forms import RegisterForm

class RegisterView(MethodView):

    template = 'auth/register.html'

    def get(self):
        form = RegisterForm()
        return render_template(self.template, form=form)

    def post(self):
        pass
