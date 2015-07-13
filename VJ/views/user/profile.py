from flask import (
    request,
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView
from flask.ext.login import login_user, login_required

from VJ.models import UserModel

class ProfileView(MethodView):

    template = 'user/settings/profile.html'

    @login_required
    def get(self):
        return render_template(self.template)

    @login_required
    def post(self):
        pass
