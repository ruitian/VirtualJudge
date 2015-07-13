from flask import (
    request,
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView
from flask.ext.login import login_user, login_required, current_user

from VJ.models import UserModel
from VJ.forms import OriginOJAccountForm

class OriginOJView(MethodView):

    template = 'user/settings/origin_oj.html'

    @login_required
    def get(self):
        form = OriginOJAccountForm()
        return render_template(self.template, form=form)

class PojView(MethodView):

    @login_required
    def get(self):
        current_user.update(poj=None)
        return redirect(url_for('user.origin_oj'))

    @login_required
    def post(self):
        form = OriginOJAccountForm()
        account = form.generate_account()
        current_user.update(poj=account)
        return redirect(url_for('user.origin_oj'))

class HduView(MethodView):

    @login_required
    def get(self):
        current_user.update(hdu=None)
        return redirect(url_for('user.origin_oj'))

    @login_required
    def post(self):
        form = OriginOJAccountForm()
        account = form.generate_account()
        current_user.update(hdu=account)
        return redirect(url_for('user.origin_oj'))

class SdutView(MethodView):

    @login_required
    def get(self):
        current_user.update(sdut=None)
        return redirect(url_for('user.origin_oj'))

    @login_required
    def post(self):
        form = OriginOJAccountForm()
        account = form.generate_account()
        current_user.update(sdut=account)
        return redirect(url_for('user.origin_oj'))

class FzuView(MethodView):

    @login_required
    def get(self):
        current_user.update(fzu=None)
        return redirect(url_for('user.origin_oj'))

    @login_required
    def post(self):
        form = OriginOJAccountForm()
        account = form.generate_account()
        current_user.update(fzu=account)
        return redirect(url_for('user.origin_oj'))
