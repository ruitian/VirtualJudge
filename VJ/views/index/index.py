from flask import (
    request,
    redirect,
    url_for,
    render_template
)
from flask.views import MethodView

class IndexView(MethodView):

    def get(self):
        return render_template('index.html')
