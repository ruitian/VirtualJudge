# -*- coding: utf-8 -*-

from .mixin import ModelViewMixin
from . import admin
from VJ.models import ContestModel


class ContestAdmin(ModelViewMixin):

    can_restore = False
    can_create = True
    can_edit = False
    can_delete = True

    column_list = (
        'id',
        'title',
        'contest_type',
        'manager',
        'created_at'
    )
    column_filters = [
        'title',
        'contest_type',
        'created_at'
    ]
    column_searchable_list = [
        'title',
        'contest_type',
    ]

    form_excluded_columns = ['created_at']
    form_subdocuments = {
        'problems': {
            'form_columns': ('problem', 'index')
        }
    }

admin.add_view(
    ContestAdmin(
        ContestModel,
        name='Contest',
        category='Contest',
        url='contest'
    )
)