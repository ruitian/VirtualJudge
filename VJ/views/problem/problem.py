from flask import (
    request,
    redirect,
    url_for,
    current_app,
    render_template
)

from flask.views import MethodView
from flask.ext.login import login_user, login_required

from VJ.models import ProblemItem
from VJ.forms import SubmitForm
from VJ.libs.tasks import code_submit

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
