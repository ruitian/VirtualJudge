from flask import (
    redirect,
    url_for,
    render_template
)

from flask.views import MethodView
from flask.ext.login import login_user

from VJ.models import ProblemItem

class ProblemListView(MethodView):

    template = 'problem/problem_list.html'

    def get(self):
        problems = ProblemItem.objects.all()
        return render_template(self.template, problems=problems)

    def post(self):
        pass

class ProblemDetailView(MethodView):

    template = 'problem/problem_detail.html'

    def get(self, origin_oj , problem_id):
        problem = ProblemItem.objects.get_or_404(
                origin_oj=origin_oj,
                problem_id=problem_id
            )
        return render_template(self.template, problem=problem)
