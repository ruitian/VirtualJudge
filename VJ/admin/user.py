# -*- coding: utf-8 -*-

from .mixin import ModelViewMixin
from . import admin
from VJ.models import UserModel


class UserAdmin(ModelViewMixin):

    can_restore = True
    can_create = True
    can_edit = True
    can_delete = True

    column_list = [
        'email',
        'username',
        'created_at',
    ]
    column_filters = ['email', 'username', 'active', 'confirmed', 'created_at']
    column_searchable_list = ['username']

    form_excluded_columns = [
        'password',
        'created_at',
        'last_login_at',
        'last_login_ip',
        'current_login_at',
        'current_login_ip',
        'poj',
        'hdu',
        'sdut',
        'fzu'
    ]

    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        return form_class

    def on_model_change(self, form, model):
        pass

admin.add_view(
    UserAdmin(
        UserModel, name='User', category='User Manage', url='user'
    )
)
