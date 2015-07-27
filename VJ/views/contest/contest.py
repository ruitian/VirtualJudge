# -*- coding: utf-8 -*-
from flask import (
    request,
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView
from flask.ext.login import current_app, login_required, current_user

from VJ.models import ContestModel, ProblemItem, UserModel
from VJ.forms import ContestForm


class ContestListView(MethodView):

    template = 'contest/contest_list.html'

    def get(self):
        per_page = current_app.config['CONTEST_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = ContestModel.objects.paginate(page=page, per_page=per_page)
        contests = paginate.items
        return render_template(
            self.template,
            contests=contests,
            paginate=paginate
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
            contests=contests,
            paginate=paginate
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
            contests=contests,
            paginate=paginate
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
            contests=contests,
            paginate=paginate
        )

    def post(self):
        pass


class ContestCreateView(MethodView):

    template = 'contest/contest_create.html'

    @login_required
    def get(self):
        form = ContestForm()
        return render_template(self.template, form=form)

    @login_required
    def post(self):
        form = ContestForm()
        if form.remove.data:
            form.problems.pop_entry()
            return render_template(self.template, form=form)
        elif form.add.data:
            form.problems.append_entry()
            return render_template(self.template, form=form)

        if not form.validate():
            return render_template(self.template, form=form)

        contest = form.generate_contest()

        contest.problems = [
            ProblemItem.objects(
                origin_oj=entrie.origin_oj.data,
                problem_id=entrie.problem_id.data
            ).first() for entrie in form.problems.entries
        ]
        contest.manager = UserModel.objects(
            username=current_user.username
        ).first()
        contest.save()
        return redirect(url_for('index.index'))
