from flask import (
    request,
    redirect,
    url_for,
    current_app,
    render_template
)

from flask.views import MethodView
from flask.ext.login import login_user

from VJ.models import SolutionItem

class SolutionListView(MethodView):

    template = 'solution/solution_list.html'

    def get(self):
        per_page = current_app.config['STATUS_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = SolutionItem.objects.paginate(page=page, per_page=per_page)
        solutions = paginate.items
        return render_template(
            self.template,
            solutions = solutions,
            paginate = paginate
        )

    def post(self):
        pass
