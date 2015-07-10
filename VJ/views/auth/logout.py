from flask import (
    render_template,
    redirect,
    url_for
)
from flask.views import MethodView
from flask.ext.login import logout_user, login_required

class LogoutView(MethodView):

    @login_required
    def get(self):
        logout_user()
        return redirect(url_for('index.index'))
