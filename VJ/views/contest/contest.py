# -*- coding: utf-8 -*-
from flask import (
    request,
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView
from flask.ext.login import current_app, login_required, current_user

from VJ.models import (
    ContestModel,
    ProblemItem,
    UserModel,
    ContestProblemModel
)
from VJ.forms import ContestCreateForm, ContestEditForm
from datetime import datetime


class ContestListView(MethodView):

    template = 'contest/contest_list.html'

    def get(self):
        per_page = current_app.config['CONTEST_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = ContestModel.objects.order_by('-id').paginate(
            page=page,
            per_page=per_page
        )
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
        paginate = ContestModel.objects(
            start_at__gt=datetime.now()
        ).order_by('start_at').paginate(
            page=page,
            per_page=per_page
        )
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
        paginate = ContestModel.objects(
            start_at__lt=datetime.now(),
            end_at__gt=datetime.now()
        ).order_by('-start_at').paginate(page=page, per_page=per_page)
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
        paginate = ContestModel.objects(
            end_at__lt=datetime.now()
        ).order_by('-end_at').paginate(
            page=page,
            per_page=per_page
        )
        contests = paginate.items
        return render_template(
            self.template,
            contests=contests,
            paginate=paginate
        )

    def post(self):
        pass


class ContestDetailView(MethodView):

    template = 'contest/contest_detail.html'

    @login_required
    def get(self, contest_id):
        contest = ContestModel.objects.get_or_404(id=contest_id)
        return render_template(
            self.template,
            contest=contest,
        )

    @login_required
    def post(self):
        pass


class ContestCreateView(MethodView):

    template = 'contest/contest_create.html'

    @login_required
    def get(self):
        form = ContestCreateForm()
        return render_template(self.template, form=form)

    @login_required
    def post(self):
        form = ContestCreateForm()
        if form.remove.data:
            form.problems.pop_entry()
            print(form.problems.last_index)
            return render_template(self.template, form=form)
        elif form.add.data:
            form.problems.append_entry()
            print(form.problems.last_index)
            return render_template(self.template, form=form)

        for index, entrie in enumerate(form.problems.entries):
            if entrie.delete.data:
                form.problems.entries.pop(index)
                return render_template(self.template, form=form)

        if not form.validate():
            return render_template(self.template, form=form)

        contest = form.generate_contest()

        for index, entrie in enumerate(form.problems.entries):
            problem = ContestProblemModel()
            problem.index = chr(index + 65)
            problem.problem = ProblemItem.objects(
                origin_oj=entrie.origin_oj.data,
                problem_id=entrie.problem_id.data
            ).first()
            contest.problems.append(problem)

        contest.manager = UserModel.objects(
            username=current_user.username
        ).first()
        contest.save()
        return redirect(url_for('contest.contest', contest_id=contest.id))


class ContestEditView(MethodView):

    template = 'contest/contest_edit.html'

    @login_required
    def get(self, contest_id):
        contest = ContestModel.objects.get_or_404(id=contest_id)
        form = ContestEditForm()

        return render_template(
            self.template,
            form=form,
            contest=contest
        )

    @login_required
    def post(self):
        pass
