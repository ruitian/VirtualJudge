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
        form = ProfileForm(obj=current_user)
        return render_template(self.template, form=form)

    @login_required
    def post(self):
        form = ProfileForm()
        if not form.validate():
            flash(form.errors['blog_url'][0])
            return redirect(url_for('user.profile'))
        current_user.update(
            nickname=form.nickname.data,
            school=form.school.data,
            blog_url=form.blog_url.data,
            location=form.location.data
        )
        flash('You have updated your profile!')
        return redirect(url_for('user.profile'))
