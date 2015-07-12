from flask import (
    request,
    redirect,
    url_for,
    current_app,
    render_template
)

from flask.views import MethodView
from flask.ext.login import login_user

from VJ.models import ProblemItem
from VJ.forms import SubmitForm
from VJ.libs import submit

class ProblemListView(MethodView):

    template = 'problem/problem_list.html'

    def get(self):
        per_page = current_app.config['PROBLEM_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = ProblemItem.objects.paginate(page=page, per_page=per_page)
        problems = paginate.items
        return render_template(
            self.template,
            problems = problems,
            paginate = paginate
        )

    def post(self):
        pass

class ProblemDetailView(MethodView):

    template = 'problem/problem_detail.html'

    def get(self, origin_oj , problem_id):
        form = SubmitForm()
        problem = ProblemItem.objects.get_or_404(
            origin_oj=origin_oj,
            problem_id=problem_id
        )
        return render_template(self.template, problem=problem, form=form)

    def post(self, origin_oj , problem_id):
        form = SubmitForm()
        if not form.validate():
            return redirect(
                url_for('problem.detail',
                    origin_oj=origin_oj,
                    problem_id=problem_id
                )
            )
        form.submit()
        return redirect(url_for('index.index'))

class ProblemSubmitView(MethodView):

    template = 'problem/problem_detail.html'

    def post(self):
        pass
