#-*- coding: utf-8 -*-
from flask import (
    request,
    redirect,
    url_for,
    flash,
    render_template
)
from flask.views import MethodView
from flask.ext.login import current_app, login_user

from VJ.models import ContestModel

class ContestListView(MethodView):

    template = 'contest/contest_list.html'

    def get(self):
        per_page = current_app.config['CONTEST_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = ContestModel.objects.paginate(page=page, per_page=per_page)
        contests = paginate.items
        return render_template(
            self.template,
            contests = contests,
            paginate = paginate
        )

    def post(self):
        pass

class ContestPendingView(MethodView):

    template = 'contest/contest_pending.html'

    def get(self):
        per_page = current_app.config['CONTEST_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = ContestModel.objects.paginate(page=page, per_page=per_page)
        contests = paginate.items
        return render_template(
            self.template,
            contests = contests,
            paginate = paginate
        )

    def post(self):
        pass

class ContestRunningView(MethodView):

    template = 'contest/contest_running.html'

    def get(self):
        per_page = current_app.config['CONTEST_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = ContestModel.objects.paginate(page=page, per_page=per_page)
        contests = paginate.items
        return render_template(
            self.template,
            contests = contests,
            paginate = paginate
        )

    def post(self):
        pass

class ContestEndedView(MethodView):

    template = 'contest/contest_ended.html'

    def get(self):
        per_page = current_app.config['CONTEST_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = ContestModel.objects.paginate(page=page, per_page=per_page)
        contests = paginate.items
        return render_template(
            self.template,
            contests = contests,
            paginate = paginate
        )

    def post(self):
        pass

class ContestCreateView(MethodView):

    template = 'contest/contest_create.html'

    def get(self):
        return render_template(self.template)

    def post(self):
        pass
