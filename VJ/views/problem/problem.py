from flask import (  # noqa
    request,
    redirect,
    url_for,
    jsonify,
    current_app,
    render_template
)

from flask.views import MethodView

from VJ.models import ProblemItem

import json


class ProblemListView(MethodView):

    template = 'problem/problem_list.html'

    def get(self):
        per_page = current_app.config['PROBLEM_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        paginate = ProblemItem.objects.order_by('problem_id').paginate(
            page=page,
            per_page=per_page
        )
        problems = paginate.items
        return render_template(
            self.template,
            problems=problems,
            paginate=paginate
        )

    def post(self):
        pass


class ProblemDetailView(MethodView):

    template = 'problem/problem_detail.html'

    def get(self, origin_oj, problem_id):
        problem = ProblemItem.objects.get_or_404(
            origin_oj=origin_oj,
            problem_id=problem_id
        )
        return render_template(self.template, problem=problem)


class ProblemGetView(MethodView):

    def get(self):
        origin_oj = request.args.get('origin_oj')
        problem_id = request.args.get('problem_id')
        problem = ProblemItem.objects(
            origin_oj=origin_oj,
            problem_id=problem_id
        ).first()
        return jsonify(
            {
                'problem': json.loads(
                    problem.to_json()
                ),
                'status': 'success'
            } if problem else {
                'status': 'error'
            }
        )
