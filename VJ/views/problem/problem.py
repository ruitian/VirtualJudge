from flask import (
    redirect,
    url_for,
    render_template
)

from flask.views import MethodView
from flask.ext.login import login_user

from VJ.models import ProblemItem

class ProblemListView(MethodView):

    template = 'problem/list.html'

    def get(self):
        problems = ProblemItem.objects.all()
        return render_template(self.template, problems=problems)

    def post(self):
        pass
