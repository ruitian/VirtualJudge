from flask import (  # noqa
    request,
    redirect,
    flash,
    url_for,
    render_template
)
from flask.views import MethodView
from flask.ext.login import login_user, login_required, current_user  # noqa

from VJ.models import UserModel  # noqa

from VJ.forms import ProfileForm


class ProfileView(MethodView):

    template = 'user/settings/profile.html'

    @login_required
    def get(self):
        form = ProfileForm()
        form.nickname.data = current_user.nickname
        form.school.data = current_user.school
        form.blog_url.data = current_user.blog_url
        form.location.data = current_user.location
        return render_template(self.template, form=form)

    @login_required
    def post(self):
        form = ProfileForm()
        user = UserModel.objects(username=current_user.username).first()
        if user is None:
            return redirect(url_for('user.profile'))
        if user.update_profile(
                form.nickname.data,
                form.school.data,
                form.blog_url.data,
                form.location.data
                ):
            flash('You have updated your profile!')
            return redirect(url_for('user.profile'))
