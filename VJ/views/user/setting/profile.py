from flask import (  # noqa
    request,
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView
from flask.ext.login import login_user, login_required  # noqa

from VJ.models import UserModel  # noqa

from VJ.forms import ProfileForm


class ProfileView(MethodView):

    template = 'user/settings/profile.html'

    @login_required
    def get(self):
        form = ProfileForm()
        return render_template(self.template, form=form)

    @login_required
    def post(self):
        pass
