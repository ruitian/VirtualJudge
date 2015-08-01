from flask import (  # noqa
    request,
    redirect,
    url_for,
    current_app,
    render_template
)

from flask.views import MethodView
from flask.ext.login import current_user

from VJ.models import SolutionItem
from base64 import b64decode


class SolutionListView(MethodView):

    template = 'solution/solution_list.html'

    def get(self):
        per_page = current_app.config['STATUS_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = SolutionItem.objects.order_by('-solution_id').paginate(
            page=page,
            per_page=per_page
        )
        solutions = paginate.items
        return render_template(
            self.template,
            solutions=solutions,
            paginate=paginate
        )

    def post(self):
        pass


class SolutionDetailView(MethodView):

    template = 'solution/solution_detail.html'

    def get(self, solution_id):
        solution = SolutionItem.objects.get_or_404(solution_id=solution_id)
        if solution.user.username != current_user.username:
            return redirect(url_for('index.index'))
        code = b64decode(solution.source)
        return render_template(self.template, solution=solution, code=code)
