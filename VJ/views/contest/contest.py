# -*- coding: utf-8 -*-
from flask import (
    request,
    redirect,
    url_for,
    flash,
    render_template
)
from flask.views import MethodView
from flask.ext.login import current_app, login_required, current_user

from VJ.models import (
    ContestModel,
    UserModel,
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
        contest = ContestModel.objects.get_or_404(contest_id=contest_id)
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
        if form.add.data:
            try:
                form.problems.append_entry()
            except:
                flash('Problem field cannot be longer than 26.')
            finally:
                for index, entrie in enumerate(form.problems.entries):
                    entrie.index.data = chr(index + 65)
            return render_template(self.template, form=form)

        for index, entrie in enumerate(form.problems.entries):
            if entrie.delete.data:
                form.problems.entries.pop(index)
                for index, entrie in enumerate(form.problems.entries):
                    entrie.index.data = chr(index + 65)
                return render_template(self.template, form=form)

        if not form.validate():
            for index, entrie in enumerate(form.problems.entries):
                entrie.index.data = chr(index + 65)
            return render_template(self.template, form=form)

        contest = form.generate_contest()

        for index, entrie in enumerate(form.problems.entries):
            problem = entrie.generate_problem(chr(index + 65))
            contest.problems.append(problem)

        contest.manager = UserModel.objects(
            username=current_user.username
        ).first()
        contest.save()
        return redirect(
            url_for(
                'contest.detail',
                contest_id=contest.contest_id
            )
        )


class ContestEditView(MethodView):

    template = 'contest/contest_edit.html'

    @login_required
    def get(self, contest_id):
        contest = ContestModel.objects.get_or_404(contest_id=contest_id)
        form = ContestEditForm(obj=contest)

        return render_template(
            self.template,
            form=form,
            contest=contest
        )

    @login_required
    def post(self, contest_id):
        form = ContestEditForm()
        contest = ContestModel.objects.get_or_404(contest_id=contest_id)
        if form.add.data:
            try:
                form.problems.append_entry()
            except:
                flash('Problem field cannot be longer than 26.')
            finally:
                for index, entrie in enumerate(form.problems.entries):
                    entrie.index.data = chr(index + 65)
            return render_template(self.template, form=form)

        for index, entrie in enumerate(form.problems.entries):
            if entrie.delete.data:
                form.problems.entries.pop(index)
                for index, entrie in enumerate(form.problems.entries):
                    entrie.index.data = chr(index + 65)
                return render_template(self.template, form=form)

        if not form.validate():
            for index, entrie in enumerate(form.problems.entries):
                entrie.index.data = chr(index + 65)
            return render_template(self.template, form=form)

        contest.update(
            title=form.title.data,
            contest_type=form.contest_type.data,
            password=form.password.data if form.password.data
            else contest.password,
            start_at=form.start_at.data,
            end_at=form.end_at.data,
            description=form.description.data,
            problems=[
                entrie.generate_problem(chr(index+65))
                for index, entrie in enumerate(form.problems.entries)
            ]
        )

        return redirect(
            url_for(
                'contest.detail',
                contest_id=contest.contest_id
            )
        )


class ContestProblemView(MethodView):

    template = 'contest/contest_problem.html'

    @login_required
    def get(self, contest_id, index):
        contest = ContestModel.objects.get_or_404(contest_id=contest_id)
        try:
            problem = contest.problems[ord(index)-65]
        except:
            flash('Problem %s is not exist.' % index)
            return redirect(
                url_for(
                    'contest.detail',
                    contest_id=contest.contest_id
                )
            )
        return render_template(
            self.template,
            contest=contest,
            problem=problem
        )

    @login_required
    def post(self):
        pass
