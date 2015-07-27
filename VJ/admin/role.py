# -*- coding: utf-8 -*-

from .mixin import ModelViewMixin
from . import admin
from VJ.models import RoleModel


class RoleAdmin(ModelViewMixin):

    column_list = [
        'name', 'description', 'created_at']
    column_filters = ['name']
    column_searchable_list = ['name']

    form_excluded_columns = ['created_at']

admin.add_view(
    RoleAdmin(
        RoleModel, name='Role', category='User', url='role'
    )
)
