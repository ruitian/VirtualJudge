from flask import (
    request,
    redirect,
    url_for,
    flash,
    render_template
)
from flask.views import MethodView
from flask.ext.login import login_required, current_user

from VJ.models import UserModel  # noqa
from VJ.forms import OriginOJAccountForm
from VJ.libs.tasks import account_init


class OriginOJView(MethodView):

    template = 'user/settings/origin_oj.html'

    @login_required
    def get(self):
        form = OriginOJAccountForm()
        return render_template(self.template, form=form)


class PojView(MethodView):

    @login_required
    def get(self):
        user = current_user
        if user.poj:
            if request.args.get('unbind', None):
                if user.poj.status == 'Unauthorized':
                    flash('Your account is unauthorized.')
                else:
                    user.poj.delete()
                    flash('Unbind success.')
            elif request.args.get('refresh', None):
                account_init.delay(
                    user.poj.origin_oj,
                    user.poj.username,
                    user.poj.password
                )
        return redirect(url_for('user.origin_oj'))

    @login_required
    def post(self):
        form = OriginOJAccountForm()
        account = form.generate_account()
        account.save()
        current_user.update(poj=account)
        account_init.delay(
            form.origin_oj.data,
            form.username.data,
            form.password.data
        )
        return redirect(url_for('user.origin_oj'))


class HduView(MethodView):

    @login_required
    def get(self):
        user = current_user
        if user.hdu:
            if request.args.get('unbind', None):
                if user.hdu.status == 'Unauthorized':
                    flash('Your account is unauthorized.')
                else:
                    user.hdu.delete()
                    flash('Unbind success.')
            elif request.args.get('refresh', None):
                account_init.delay(
                    user.hdu.origin_oj,
                    user.hdu.username,
                    user.hdu.password
                )
        return redirect(url_for('user.origin_oj'))

    @login_required
    def post(self):
        form = OriginOJAccountForm()
        account = form.generate_account()
        account.save()
        current_user.update(hdu=account)
        account_init.delay(
            form.origin_oj.data,
            form.username.data,
            form.password.data
        )
        return redirect(url_for('user.origin_oj'))


class SdutView(MethodView):

    @login_required
    def get(self):
        user = current_user
        if user.sdut:
            if request.args.get('unbind', None):
                if user.sdut.status == 'Unauthorized':
                    flash('Your account is unauthorized.')
                else:
                    user.sdut.delete()
                    flash('Unbind success.')
            elif request.args.get('refresh', None):
                account_init.delay(
                    user.sdut.origin_oj,
                    user.sdut.username,
                    user.sdut.password
                )
        return redirect(url_for('user.origin_oj'))

    @login_required
    def post(self):
        form = OriginOJAccountForm()
        account = form.generate_account()
        account.save()
        current_user.update(sdut=account)
        account_init.delay(
            form.origin_oj.data,
            form.username.data,
            form.password.data
        )
        return redirect(url_for('user.origin_oj'))


class FzuView(MethodView):

    @login_required
    def get(self):
        user = current_user
        if user.fzu:
            if request.args.get('unbind', None):
                if user.fzu.status == 'Unauthorized':
                    flash('Your account is unauthorized.')
                else:
                    user.fzu.delete()
                    flash('Unbind success.')
            elif request.args.get('refresh', None):
                account_init.delay(
                    user.fzu.origin_oj,
                    user.fzu.username,
                    user.fzu.password
                )
        return redirect(url_for('user.origin_oj'))

    @login_required
    def post(self):
        form = OriginOJAccountForm()
        account = form.generate_account()
        account.save()
        current_user.update(fzu=account)
        account_init.delay(
            form.origin_oj.data,
            form.username.data,
            form.password.data
        )
        return redirect(url_for('user.origin_oj'))
