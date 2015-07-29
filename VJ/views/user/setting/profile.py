from flask import (
    request,
    redirect,
    url_for,
    render_template
)  # noqa
from flask.views import MethodView
from flask.ext.login import login_user, login_required  # noqa

from VJ.models import UserModel  # noqa

from VJ.forms import UpdateProfileForm


class ProfileView(MethodView):

    template = 'user/settings/profile.html'

    @login_required
    def get(self):
        return render_template(self.template)

    @login_required
    def post(self):
        pass


class UpdateProfileView(MethodView):

    template = 'user/settings/updateprofile.html'

    @login_required
    def get(self):
        form = UpdateProfileForm()
        return render_template(self.template, form=form)

    @login_required
    def post(self):
        pass
