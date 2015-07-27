# -*- coding: utf-8 -*-
from flask import redirect, url_for, request
from flask.ext.login import current_user
from flask.ext.admin import Admin, AdminIndexView as _AdminIndexView


class AdminIndexView(_AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated() and \
            current_user.is_administrator()

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next=request.url))


admin = Admin(
    name='Virtual Judge Admin',
    index_view=AdminIndexView(name='Index'),
    template_mode='admin'
)

from . import user  # noqa
