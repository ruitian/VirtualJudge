from flask import (
    request,
    redirect,
    url_for,
    current_app,
    render_template
)

from flask.views import MethodView
from flask.ext.login import login_user, login_required

from VJ.forms import SubmitForm
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
        if not form.validate():
            return render_template(
                self.template,
                form=form,
                origin_oj=form.origin_oj.data,
                problem_id=form.problem_id.data
            )
        return redirect(url_for('solution.list'))
