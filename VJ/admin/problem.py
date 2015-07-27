# -*- coding: utf-8 -*-

from .mixin import ModelViewMixin
from . import admin
from VJ.models import ProblemItem


class ProblemAdmin(ModelViewMixin):

    can_restore = False
    can_create = False
    can_edit = False
    can_delete = True

    column_list = (
        'origin_oj',
        'problem_id',
        'title',
        'update_time'
    )
    column_filters = ['origin_oj', 'problem_id', 'title']
    column_searchable_list = ['problem_id', 'origin_oj', 'title']

admin.add_view(
    ProblemAdmin(
        ProblemItem,
        name='Problem',
        category='Problem',
        url='problem'
    )
)
