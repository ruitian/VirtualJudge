# -*- coding: utf-8 -*-

from .mixin import ModelViewMixin
from . import admin
from VJ.models import SolutionItem


class SolutionAdmin(ModelViewMixin):

    can_restore = False
    can_create = False
    can_edit = False
    can_delete = False

    column_list = (
        'solution_id',
        'origin_oj',
        'problem_id',
        'result',
        'created_at'
    )
    column_filters = ['origin_oj', 'problem_id', 'result']
    column_searchable_list = ['origin_oj', 'problem_id', 'result']

admin.add_view(
    SolutionAdmin(
        SolutionItem,
        name='Solution',
        category='Solution',
        url='solution'
    )
)
