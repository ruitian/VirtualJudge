from flask import (  # noqa
    request,
    redirect,
    url_for,
    flash,
    render_template
)
from flask.views import MethodView
from flask.ext.login import current_user, login_required, logout_user

from VJ.models import UserModel  # noqa

from VJ.forms import ChangePasswordForm


class AccountView(MethodView):

    template = 'user/settings/account.html'

    @login_required
    def get(self):
        form = ChangePasswordForm()
        return render_template(self.template, form=form)

    @login_required
    def post(self):
        form = ChangePasswordForm()
        if not form.validate():
            return render_template(self.template, form=form)
        if current_user.verify_password(form.old_password.data):
            current_user.set_password(form.password.data)
            current_user.save()
            flash('Your password has been updated.')
            logout_user()
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid password.')
        return redirect(url_for('user.account'))
