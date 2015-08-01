from flask import (
    request,
    redirect,
    url_for,
    flash,
    render_template
)

from flask.views import MethodView
from flask.ext.login import login_required, current_user

from VJ.forms import SubmitForm
from VJ.models import UserModel
from VJ.libs.tasks import code_submit


class ProblemSubmitView(MethodView):

    template = 'problem/problem_submit.html'

    @login_required
    def get(self):
        form = SubmitForm()
        origin_oj = request.args.get('origin_oj')
        problem_id = request.args.get('problem_id')
        return render_template(
            self.template,
            form=form,
            origin_oj=origin_oj,
            problem_id=problem_id
        )

    @login_required
    def post(self):
        form = SubmitForm()
        account = current_user.get_account(form.origin_oj.data)
        if not form.validate():
            return render_template(
                self.template,
                form=form,
                origin_oj=form.origin_oj.data,
                problem_id=form.problem_id.data
            )
        if account is None or account.status != 'Authentication Success':
            flash('Please bind the correct account.')
            return redirect(
                url_for(
                    'problem.submit',
                    origin_oj=form.origin_oj.data,
                    problem_id=form.problem_id.data,
                )
            )

        solution = form.generate_solution()
        solution.user = UserModel.objects(
            username=current_user.username
        ).first()
        solution.save()
        code_submit.delay(
            form.origin_oj.data,
            solution.solution_id,
            form.problem_id.data,
            form.language.data,
            form.code.data,
            account.username,
            account.nickname,
            account.password
        )

        return redirect(url_for('solution.list'))
